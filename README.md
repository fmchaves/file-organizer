# File Organizer
Organize the files in your current directory or any directory of your choice by sorting them into Text File, Data File, Audio File, Video File, Spreadsheet File, and so on.

## Usage
1) Download the zip file and uncompress it in your computer.
2) Setup the options on the setup.json file (see the options below).
3) run the file main.py

## Configuration

```
{"config1":
    {
      "root_path": "C:/Users/username/Folder",
      "destination_path": "C:/Users/username/Folder",      
      "reorganize_files_inside_folders": "yes",
      "separate_files_per_category": "yes",
      "separate_files_per_type": "yes",
      "do_not_move": ["SubFolder", "song1.mp4"]
    }    
}
```

## Example
```
Folder
│   ├── SubFolder
│   |   ├── config.json
|   |   └── index.html
│   ├── document.txt
│   ├── img1.jpeg
│   ├── main.cpp
│   ├── main.py
│   ├── movie.avi
│   ├── paper.latex
│   ├── power-point.ppt
│   ├── sheet.csv
│   ├── song1.mp4
│   ├── song2.mp3
│   └── word-document.doc
```
