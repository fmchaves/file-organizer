try:
    from os.path import abspath, sep, exists
    from os import getcwd
    from json import loads
    from pkg.log_msg import write_log_msg
except Exception as e:
    raise

PATH = getcwd() + sep
FILE_NAME = 'setup.json'

def read_config(file_name: str = PATH + FILE_NAME) -> dict:
    """Loads the configuration file and validates the parameters.

    Parameters
    ----------
    file_name : str (default config.json)
        The name of the configuration file

    Returns
    -------
    dictionary

    Obs: raises exceptions on the log file.
    """
    try:
        with open(file_name, 'r') as file_handle:
            config_dict = loads(file_handle.read())
    except Exception as e:
        write_log_msg(msg = f'Problem reading {file_name}. ({e})')
    else:
        parameters = (('root_path', str), \
                      ('destination_path', str), \
                      ('move_folders', str), \
                      ('reorganize_files_inside_folders', str), \
                      ('separate_files_per_category', str), \
                      ('separate_files_per_type', str), \
                      ('do_not_move', list)) # Parameters name

        bad_configs = [] # Holds keys of the config dict with wrong names or bad values

        for config in config_dict: # This block of code will validate each key and value of the config dict
            for parameter, parameter_type in parameters:
                # Check if the parameter exist
                if parameter not in config_dict[config].keys():
                    write_log_msg(msg = f'The parameter {parameter} was not found in {config} ({file_name})')
                    if config not in bad_configs:
                        bad_configs.append(config)
                else:
                    # Check if the value of the parameter is string
                    if type(config_dict[config][parameter]) is not parameter_type:
                        write_log_msg(msg = f'The parameter {parameter} in {config} must be {parameter_type}. ({file_name})')
                        if config not in bad_configs:
                            bad_configs.append(config)
                    else:
                        # Check if root and destination path exist
                        if parameter in ('root_path', 'destination_path'):
                            if not exists(abspath(config_dict[config][parameter])):
                                write_log_msg(msg= f'The following path does not exist: {config_dict[config][parameter]} ({file_name})')
                                if config not in bad_configs:
                                    bad_configs.append(config)
                            else:
                                config_dict[config][parameter] = abspath(config_dict[config][parameter])
                        elif parameter == 'do_not_move':
                            for value in config_dict[config][parameter]:
                                if type(value) is not str:
                                    write_log_msg(msg = f'The values of the parameter {parameter} in {config} must be str. ({file_name})')
                                elif len(value.strip()) == 0:
                                    config_dict[config][parameter].remove(value)

                        # Check if the parameter has the right value (yes/no)
                        else:
                            if config_dict[config][parameter].lower() not in ('yes', 'no'):
                                write_log_msg(msg = f'The value of {parameter} in {config} is wrong: yes/no expected ({file_name})')
                                if config not in bad_configs:
                                    bad_configs.append(config)
                            else:
                                config_dict[config][parameter] = config_dict[config][parameter].lower()

        if len(bad_configs) > 0: # Remove bad configs
            for config in bad_configs:
                del config_dict[config]

        return config_dict if len(config_dict) > 0 else None
