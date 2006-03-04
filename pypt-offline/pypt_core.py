import os, shutil, string, urllib, sys, progressbar, optparse, urllib2

"""
This is the main core module. It does the main job of downloading packages/update packages,\nfiguring out if the packages are in the local cache, handling exceptions and many more stuff
"""

import shutil

def download_from_web(sUrl, sFile, sSourceDir):
    """
    Download the required file from the web
    The arguments are passed everytime to the function so that,
    may be in future, we could reuse this function
    """
       
    try:
        os.chdir(sSourceDir)
        block_size = 4096
        i = 0
        counter = 0
        temp = urllib2.urlopen(sUrl)
        headers = temp.info()
        size = int(headers['Content-Length'])
        data = open(sFile,'wb')
        sys.stdout.write("Downloading %s\n" % (sFile))
        while i < size:
            data.write (temp.read(block_size))
            i += block_size
            counter += 1
            progressbar.myReportHook(counter, block_size, size)
        print "\n"
        data.close()
        temp.close()
        
        sys.stdout.write("%s successfully downloaded from %s\n\n" % (sFile, sUrl))
        return True
        
    except OSError, (errno, strerror):
        sys.stderr.write ("%s\n" %(sSourceDir))
        errfunc(errno, strerror)
        
    except urllib2.HTTPError, errstring:
        errfunc(errstring.code, errstring.msg)
        
    except urllib2.URLError, errstring:
        #We pass error code "1" here becuase URLError
        # doesn't pass any error code.
        # URLErrors shouldn't be ignored, hence program termination
        if errstring.reason.args[0] == 10060:
            errfunc(errstring.reason.args[0], errstring.reason)
            
        #errfunc(1, errstring.reason)
        #pass
    
    except IOError, (errno, strerror):
        sys.strerr.write("%s\n" % (strerror))
        errfunc(errno, strerror)
        
    #return bFound

#TODO: walk_tree_copy_debs
# This might require simplification and optimization.
# But for now it's doing the job.
# Need to find a better algorithm, maybe os.walk()                    
def walk_tree_copy_debs(sRepository, sFile, sSourceDir):
    """
    This function checks for a package to see if its already downloaded
    It can search directories with depths.
    """
    #The core algorithm is here for the whole program to function'\n'
    #It recursively searches a tree/subtree of folders for package files'\n'
    #like the directory structure of "apt-proxy". If files are found (.deb || .rpm)'\n'
    #it checks wether they are on the list of packages to be fetched. If yes,'\n\
    #it copies them. Same goes for flat "apt archives folders" also.'\n'
    #Else it fetches the package from the net"""
    bFound = False
    try:
        if sRepository is not None:
            for name in os.listdir(sRepository) and bFound == True:
                #if bFound == True:
                #    break
                path = os.path.join(sRepository, name)
                if os.path.isdir(path):
                    walk_tree_copy_debs(path, sFile, sSourceDir)
                    #walk_tree_copy_debs(path, sFile)
                elif name.endswith('.deb') or name.endswith('.rpm'):
                    if name == sFile:
                        try:
                            shutil.copy(path, sSourceDir)
                        except IOError, (errno, errstring):
                            errfunc(errno, errstring)
                        except shutil.Error:
                            sys.stdout.write("%s is available in %s. Skipping Copy!\n" % (name, sSourceDir))
                        bFound = True
                        break
                        
                        #shutil.copy(path, sSourceDir)
                        #bFound = True
                        #break
            #return bFound
                    #return False
    except OSError, (errno, strerror):
        sys.stderr.write("%s %s\n" % (errno, strerror))
        errfunc(errno, strerror)
        
        
def files(root): 
    for path, folders, files in os.walk(root): 
        for file in files: 
            yield path, file 


def copy_first_match(repository, filename, dest_dir): # aka walk_tree_copy() 
    for path, file in files(repository): 
        if file == filename: 
            try:
                shutil.copy(os.path.join(path, file), dest_dir)
                sys.stdout.write("%s copied from local cache %s.\n" % (file, repository))
            except shutil.Error:
                sys.stdout.write("%s is available in %s. Skipping Copy!\n\n" % (file, dest_dir))
            return True 
    return False 

def compress():
    pass


def errfunc(errno, errormsg):
    """
    We use errfunc to handler errors.
    There are some error codes (-3 and 13 as of now)
    which are temporary codes, they happen when there
    is a temporary resolution failure, for example.
    For such situations, we can't abort because the
    uri file might have other hosts also, which might
    be well accessible.
    This function does the job of behaving accordingly
    as per the error codes.
    """
    
    if errno == -3 or errno == 13:
        #TODO: Find out what these error codes are for
        # and better document them the next time you find it out.
        # 13 is for "Permission Denied" when you don't have privileges to access the destination 
        pass
    elif errno == 407 or errno == 2:
        # These, I believe are from OSError/IOError exception.
        # I'll document it as soon as I confirm it.
        sys.stderr.write("%s\n" % (errormsg))
        sys.exit(errno)
    elif errno == 504 or errno == 404 or errno == 10060:
        #TODO: Counter which will inform that some packages weren't fetched.
        # A counter needs to be implemented which will at the end inform the list of sources which 
        # failed to be downloaded with the above codes.
        
        # 504 is for gateway timeout
        # On gateway timeouts we can keep trying out becuase
        # one apt source.list might have different hosts.
        # 404 is for URL error. Page not found.
        # THere can be instances where one source is changed but the rest are working.
        # 10060 is for Operation Time out. There can be multiple reasons for this timeout
        # Primarily if the host is down or a slow network or abruption, hence not the whole execution should be aborted
        sys.stderr.write("%s %s\n" % (errno, errormsg))
        sys.stderr.write("Will still try with other package uris\n")
        pass
    elif errno == 1:
        # We'll pass error code 1 where ever we want to gracefully exit
        sys.stderr.write(errormsg)
        sys.stderr.write("Explicit program termination %s\n" % (errno))
        sys.exit(errno)
    else:
        sys.stderr.write("Aieee! I don't understand this errorcode\n" % (errno))
        sys.exit(errno)
    
def warn(exception_warn):
    sys.stderr.write(exception_warn)

def report(blockcount, bytesdownloaded, totalbytes):
    # This isn't implemented yet.
    # When implemented this would give a progress bar.        
    sys.stdout.write("\rDownloading %r from %r ... (%r of %r)" % (blockcount, bytesdownloaded, totalbytes,))
    sys.stdout.write("\rDownloading ... (%r of %r)" % (blockcount, bytesdownloaded,totalbytes,))
    sys.stdout.flush()

def starter(uri, path, cache, type = 0):
    """
    uri - The uri data whill will contain the information
    path - The path (if any) where the download needs to be done
    cache - The cache (if any) where we should check before downloading from the net
    type - type is basically used to identify wether it's a update download or upgrade download
    """
    
    if type == 1:
        #XXX: Oh! We're only downloading the update package list database
        # Package Update database changes almost daily in Debian.
        # This is at least true for Sid. Hence it doesn't make sense to copy
        # update packages' database from a cache.
        
        if path is None:
            if os.access("pypt-downloads", os.W_OK) is True:
                sSourceDir = os.path.abspath("pypt-downloads")
            else:
                os.mkdir("pypt-downloads", 0077)
                sSourceDir = os.path.abspath("pypt-downloads")
        else:
                sSourceDir = path
        
        try:
            lRawData = open(uri, 'r').readlines()
        except IOError, (errno, strerror):
            sys.stderr.write("%s %s\n" % (errno, strerror))
            errfunc(errno)
        
        for each_single_item in lRawData:
            lSplitData = each_single_item.split(' ') # Split on the basis of ' ' i.e. space
    
            # We initialize the variables "sUrl" and "sFile" here.
            # We also strip the single quote character "'" to get the real data
            sUrl = string.rstrip(string.lstrip(''.join(lSplitData[0]), chars="'"), chars="'")
            sFile = string.rstrip(string.lstrip(''.join(lSplitData[1]), chars="'"), chars="'")
            
            sys.stdout.write("Downloading %s from %s!\n") % (sFile, sUrl)
            bStatus = download_from_web(sUrl, sFile, sSourceDir)
            if bStatus != True:
                 sys.stdout.write("%s not downloaded from %s\n" % (sFile, sUrl))
                 
    if type  == 2:
        if path is None:
            if os.access("pypt-downloads", os.W_OK) is True:
                sSourceDir = os.path.abspath("pypt-downloads")
            else:
                os.mkdir("pypt-downloads", 0077)
                sSourceDir = os.path.abspath("pypt-downloads")
        else:
            sSourceDir = path
                
        if cache is None:
            sRepository = os.path.abspath(os.curdir)
        else:
            sRepository = cache
            
        try:
            lRawData = open(uri, 'r').readlines()
        except IOError, (errno, strerror):
            sys.stderr.write("%s %s\n" %(errno, strerror))
            errfunc(errno)
        
        for each_single_item in lRawData:
            lSplitData = each_single_item.split(' ') # Split on the basis of ' ' i.e. space
    
            # We initialize the variables "sUrl" and "sFile" here.
            # We also strip the single quote character "'" to get the real data
            sUrl = string.rstrip(string.lstrip(''.join(lSplitData[0]), chars="'"), chars="'")
            sFile = string.rstrip(string.lstrip(''.join(lSplitData[1]), chars="'"), chars="'")
            #bFound = False
            #bStatus = walk_tree_copy_debs(sRepository, sFile, sSourceDir)
            bStatus = copy_first_match(sRepository, sFile, sSourceDir)
            if bStatus == False:
                bStatus = download_from_web(sUrl, sFile, sSourceDir)
                if bStatus != True:
                     sys.stderr.write("%s not downloaded from %s and NA in local cache %s\n\n" % (sFile, sUrl, sRepository))