try:
    from pkg.log_msg import *
    from pkg.categorization import *
    from pkg.dir_routines import *
    from pkg.setup import *
    from os import getcwd
    from os.path import abspath, sep, join
    from shutil import rmtree
except Exception as e:
    raise

CURRENT_WD = getcwd() + sep

if __name__ == '__main__':

    config_dict  = read_config(file_name = CURRENT_WD + sep +'setup.json') # Reads the config file
    category_names_dict = read_category_names(file_name = CURRENT_WD + 'categorization' + sep + 'category_names.json') # Reads the file containing the folder names
    file_ext_dict = read_file_extensions(file_name = CURRENT_WD + 'categorization' + sep + 'file_extensions.json') # Reads the file containing informations about the extensios


    if None not in (config_dict, category_names_dict, file_ext_dict):

        for config in config_dict:

            root_path = abspath(config_dict[config]['root_path'])
            destination_path = abspath(config_dict[config]['destination_path'])
            organize_files_per_category = config_dict[config]['organize_files_per_category'] == 'yes'
            organize_files_per_type = config_dict[config]['organize_files_per_type'] == 'yes'
            organize_files_inside_subfolders = config_dict[config]['organize_files_inside_subfolders'] == 'yes'
            do_not_move = config_dict[config]['do_not_move']

            # If the destination path is a subdirectory of the root path, add it to the list of directories not to visit.
            aux = list(set(destination_path.split(sep)) - set(root_path.split(sep)))
            if aux:
                do_not_move.extend(aux)

            scanned_dir = scan_dir(root_path) # Scan generator for root path

            directories_to_remove = [] # Stores folder names to be removed after moving files.

            for dirpath, dirnames, filenames in scanned_dir:
                aux_destination_path = destination_path
                # If the destination path is a subdirectory of the root path,
                # this next block of code will avoid the directories within it.
                if do_not_move and dirnames:
                    for forbidden in do_not_move:
                        if forbidden in dirnames:
                            dirnames.remove(forbidden)
                        elif forbidden in filenames:
                            filenames.remove(forbidden)
                if dirpath > root_path: # Folders that are in the root directory
                    directory_name = dirpath.split(sep)[-1]
                    aux_destination_path = join(aux_destination_path, directory_name)
                    if dirpath not in directories_to_remove and root_path != destination_path: # Stores the name of the folder to be removed later.
                        print(f'{dirpath} {destination_path}')
                        directories_to_remove.append(dirpath)
                    if filenames: # If files available, build the destination path
                        paths = build_dst_path(filenames,\
                                               aux_destination_path,\
                                               file_ext_dict, \
                                               category_names_dict, \
                                               organize_files_inside_subfolders and organize_files_per_category, \
                                               organize_files_inside_subfolders and organize_files_per_type)
                else:
                    if filenames: # If files available, build the destination path
                        paths = build_dst_path(filenames, \
                                             aux_destination_path, \
                                             file_ext_dict, \
                                             category_names_dict, \
                                             organize_files_per_category, \
                                             organize_files_per_type)
                # Move files
                for rt_path, dst_path in zip((join(dirpath, filename) for filename in filenames), paths):
                    move_from_to(root_path = rt_path, destination_path = dst_path)

            # Delete empty folders
            for dir_path in directories_to_remove:
                rmtree(path = dir_path)
    else:
         write_log_msg(msg = 'It was not possible to complete the process! (Check out the messages above)')
