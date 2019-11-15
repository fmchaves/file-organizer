# File Organizer
Organize the files in your current directory or any directory of your choice by sorting them into Text File, Data File, Audio File, Video File, Spreadsheet File, and so on.

## Usage
1) Download the zip file and uncompress it in your computer.
2) Setup the options on the setup.json file (see the options below).
3) run the file main.py

## Configurations
In the **setup.json** have some features to organize the folders. The first parameter, **root_path**,
is the path of the source (where the files come from) directory, and the **destination_path** is the final path where the files will be organized.

**Note: if you are using Windows, do not use the traditional left slash, use the right one.**

The parameter **organize_files_per_category** only accepts **yes** or **no**, and will organize the files per category such as: Text Files, Audio Files, Video Files, Game Files and so on. You can change the name of the categories on the file **category_names.json** inside categorization folder. Be careful to change names only after the colon.

The parameter **organize_files_per_category (yes/no)**, and will organize the files per category such as: Text Files, Audio Files, Video Files, Game Files and so on.

The parameter **organize_files_per_category (yes/no)**, and will organize the files per category such as: Text Files, Audio Files, Video Files, Game Files and so on.

```
{"config1":
    {
      "root_path": ".../.../source",
      "destination_path": ".../.../destination",            
      "organize_files_per_category": "yes/no",
      "organize_files_per_type": "yes/no",
      "organize_files_inside_folders": "yes/no",
      "do_not_move": ["folder_name1", "file_name1", ..., "folder_name", "file_name"]
    }    
}
```

## Example
```
Folder
│   ├── SubFolder1
│   |   ├── config.json
|   |   └── index.html
│   ├── SubFolder2
│   |   ├── main.cpp
|   |   └── main.py
│   ├── document.txt
│   ├── img1.jpeg
│   ├── movie.avi
│   ├── paper.latex
│   ├── power-point.ppt
│   ├── sheet.csv
│   ├── song1.mp4
│   ├── song2.mp3
│   └── word-document.doc
```
