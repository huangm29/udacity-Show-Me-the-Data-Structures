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
    print(path)
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
            
    if os.path.isdir(path):
        filelist = os.listdir(path)
        for file_name in filelist:
            newfiles = find_files(suffix, path+'/'+file_name)
            files += newfiles
    
    return files


print(find_files('.c', '.'))