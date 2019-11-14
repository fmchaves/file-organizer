# This module is used to write error messages in a log file

try:
    from time import asctime, localtime
except Exception as e:
    raise e

DEFAULT_LOGFILENAME = 'logfile.log'

def write_log_msg(file_name: str = DEFAULT_LOGFILENAME, msg: str = '') -> None:
    """Opens a log file and write a message on it.

    Parameters
    ----------
    file_name : str (default 'logfile.log')
        The file name to annotate the messages
    msg : str  (default '')
        The message to be written to the file

    Returns
    -------
    None

    Obs: if the file doesn't exist, a default (logfile.log) will be created.
    """

    try:
        with open(file = file_name, mode = 'a+') as file_handle:
            current_time = asctime(localtime())
            file_handle.write(current_time + ' -> ' + str(msg) + '\n')
    except Exception as e:
        raise e
