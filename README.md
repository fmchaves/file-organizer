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

The parameter **organize_files_per_category (yes/no)**, if affirmative, will organize the files per category, such as: Text Files, Audio Files, Video Files, Game Files and so on. You can change the name of the categories on the file **category_names.json** inside categorization folder, but be careful to change names only after the colon.

The parameter **organize_files_per_type (yes/no)**, if affirmative, will organize the files per type, such as: Latex Document, C++ Source Code File, Python Script, Mp3 Audio File, etc.

The parameter **organize_files_inside_folders (yes/no)**, if affirmative, will organize the inner files of any folder in the **root_path**.

The parameter **do_not_move** is a list that holds names of folder or files that will not be moved or reorganized.

```
{"config_1":
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
If you want to put this script to run on the background of your system, you can add as many configurations as you want (see the example below).

```
{"config_1":
    {
      parameters
    },
  "config_2":
      {
        parameters
      },
      .
      .
      .
  "config_N":
      {
        parameters
      }     
}
```

## Example
To clarify how the program works, let's consider de following configuration, where I'm going to organize the files per category and type. I also want to organize the files that are in the folders or the root directory, but I don't want to organize the folder and concert.mp4 file.
```{"config_1":
    {
      "root_path": ".../.../Folder",
      "destination_path": ".../.../Folder",            
      "organize_files_per_category": "yes",
      "organize_files_per_type": "yes",
      "organize_files_inside_folders": "yes",
      "do_not_move": ["WebSite", "concert.mp4"]
    }    
}
```
The following structure is a view of the initial directory.
```
Folder
│   ├── WebSite
│   |   ├── config.json
|   |   └── index.html
│   ├── Programs
│   |   ├── main.cpp
|   |   └── main.py
│   ├── concert.mp4
│   ├── document.txt
│   ├── img1.jpeg
│   ├── movie.avi
│   ├── paper.tex
│   ├── power-point.ppt
│   ├── sheet.csv
│   ├── song.mp3
│   └── word-document.doc
```
After running the code, this is how the directory will look like.
```
Folder
│   ├── Audio File
│   |   ├── Mp3 Audio Files
│   |   |   └── song.mp3
│   ├── Data Files
│   |   ├── Comma Separated Values File
|   |   |   └── sheet.csv
│   |   ├── Power Point Presentation
|   |   |   └── power-point.ppt
│   ├── Raster Images
│   |   ├── Jpeg Image
|   |   |   └── img1.jpeg
│   ├── WebSite
│   |   ├── config.json
|   |   └── index.html
│   ├── Programs
│   |   ├── Developer Files
│   |   ├── C++ Source Code File
|   |   |   └── main.cpp
│   |   ├── Python Script
|   |   |   └── main.py
│   ├── Text Files
│   |   ├── Latex Document
|   |   |   └── paper.tex
│   |   ├── Plain Text File
|   |   |   └── document.txt
│   |   ├── Wordpad Document
|   |   |   └── word-document.doc
│   ├── Video Files
│   |   ├── Audio Video Interleave File
|   |   |   └── movie1.avi
│   └── concert.mp4
```

## MIT License

Copyright (c) 2019 Chaves, F. M.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
