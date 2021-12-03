import os

def find_files(suffix = "", path = "."):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """

    files = []
    if suffix == "": #if the suffix is empty then return empty list
        return files

    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
            
    if os.path.isdir(path): 
        filelist = os.listdir(path)
        for file_name in filelist:
            newfiles = find_files(suffix, path+'/'+file_name)
            files += newfiles
    
    return files

#test 1
print("\n Test 1")
print(find_files('', './testdir')) #Empty input should return empty list
#[]

#test 2
print("\n Test 2")
print(find_files('.c', './test'))  #should return empty list as the /test folder does not exist
#[]

#test 3
print("\n Test 3")
print(find_files('.c', './testdir')) #should return all the files with .c 
#['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

