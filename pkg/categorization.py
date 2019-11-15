#

try:
    from pkg.log_msg import write_log_msg
    from json import loads
    from os import getcwd
    from os.path import abspath, sep
except Exception as e:
    raise

# Folder containing configuration files
COMMON_PATH = getcwd() + sep + 'categorization' + sep

def read_file_extensions(file_name: str = abspath(COMMON_PATH + 'file_extensions.json')) -> dict:
    """Loads information about file extensions.

    Parameters
    ----------
    file_name : str (default file_extensions.json)
        The name of the file containing the categories and description for each extension

    Returns
    -------
    dictionary

    Obs: raises exceptions on the log file
    """

    try:
        with open(file = file_name, mode = 'r') as file_handle:
            file_ext_dict = loads(file_handle.read())
    except Exception as e:
        write_log_msg(msg = str(e))
    else:
        return file_ext_dict


def read_folder_names(file_name: str = COMMON_PATH + 'category_names.json') -> dict:
    """Loads a json file containing folder names by category.

    Parameters
    ----------
    file_name : str (default folder_names.json)
        The name of the file containing folder names by category

    Returns
    -------
    dictionary

    Obs: raises exceptions on the log file.
    """

    try:
        with open(file = file_name, mode = 'r') as file_handle:
            folder_names_dict = loads(file_handle.read())
    except Exception as e:
        write_log_msg(msg = str(e) + f'({file_name})')
    else:
        return folder_names_dict
