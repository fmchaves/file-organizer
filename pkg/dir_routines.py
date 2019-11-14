try:
    from pkg.log_msg import write_log_msg
    from os import walk, makedirs
    from os.path import abspath, exists, splitext, join
    from shutil import move
    from typing import Generator
except Exception as e:
    raise

def scan_dir(path: str) -> Generator[tuple, None, None]:
    """Directory tree generator.

    For each directory in the directory tree, yields a 3-tuple

        dirpath, dirnames, filenames

    Parameters
    ----------
    path : str
        The path name (directory) to be scanned

    Returns
    -------
    generator

    Obs: raises exceptions on the log file.
    """

    try:
        scanned_dir = walk(abspath(path), topdown = True)
    except Exception as e:
        write_log_msg(msg = str(e) + '(scan_dir funtion)')
    else:
        return scanned_dir


def move_from_to(root_path : str, destination_path : str) -> bool:
    """Move files from the root to the destination path.

    Parameters
    ----------
    root_path : str
        The root path
    destination_path : str
        The destination path

    Returns
    -------
    bool

    Obs: raises exceptions on the log file.
    """

    if not exists(path = destination_path):
        try:
            makedirs(name = destination_path)
        except Exception as e:
            write_log_msg(msg = str(e) + '(move_from_to function)')
            return False

    try:
        move(src = root_path, dst = destination_path)
    except Exception as e:
        write_log_msg(msg = str(e) + '(move_from_to function)')
        return False
    else:
        return True

def build_dst_path(filenames : list, \
                 destination_path : str, \
                 file_ext_dict : dict, \
                 folder_names_dict : dict, \
                 separate_files_per_category : bool, \
                 separate_files_per_type : bool) -> Generator[str, None, None]:
    """
    Creates the destination file path.

    Parameters
    ----------
    filenames : list
        A list containing the name of the files to be moved
    destination_path : str
        The destination path
    file_ext_dict : dict
        A dictionary containing types and categories for each extension
    folder_names_dict : dict
        A dictionary containing the name of the destination folders
    separate_files_per_category : bool
        A boolean value where files must be separated by category or not
    separate_files_per_type : bool
        A boolean value where files must be separated by type or not

    Yields
    -------
    yields a destination path

    Obs: raises exceptions on the log file.
    """

    for filename in filenames:

        aux_destination_path = destination_path

        file_ext = splitext(filename)[-1].lower()

        if separate_files_per_category:
            category = file_ext_dict.get(file_ext, '.unknown')['category']
            folder_name = folder_names_dict[category].title()
            aux_destination_path = join(aux_destination_path, folder_name)

        if separate_files_per_type:
            folder_name = file_ext_dict.get(file_ext, '.unknown')['file_type'].title()
            aux_destination_path = join(aux_destination_path, folder_name)

        yield aux_destination_path
