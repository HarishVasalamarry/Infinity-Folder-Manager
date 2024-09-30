# Infinity Folder Manager

The **Infinity Folder Manager** is a Python script that helps manage files in a specified folder by automatically compressing them to save space and uncompressing them when you need to access them. It supports various file types, including documents, images, audio, and video files, providing a menu-driven interface for easy interaction.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Notes and Considerations](#notes-and-considerations)
- [Known Issues and Limitations](#known-issues-and-limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Automatic Compression**: Compresses files placed in the designated folder to save space.
- **Menu Interface**: Allows you to access and edit files through an interactive menu.
- **Media File Handling**: Uses VLC Media Player to open audio and video files, automatically recompressing them after use.
- **Image File Handling**: Prompts you to indicate when you're done viewing images before recompressing.
- **Real-Time Monitoring**: Continuously monitors the folder for new files to compress.

---

## Installation

### Prerequisites

- **Python 3.x**: Ensure that Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **VLC Media Player**: Install VLC Media Player to handle audio and video files. Download it from [videolan.org](https://www.videolan.org/vlc/).

### Clone the Repository

```bash
git clone https://github.com/HarishVasalamarry/infinity-folder-manager.git
```

Replace `yourusername` with your GitHub username.

### Navigate to the Script Directory

```bash
cd infinity-folder-manager
```

### Adjust the VLC Path (if necessary)

- The script uses VLC Media Player located at `C:\Program Files\VideoLAN\VLC\vlc.exe` by default.
- If VLC is installed in a different location, open `infinity_manager.py` and update the `VLC_PATH` variable:

  ```python
  VLC_PATH = r"C:\Path\To\Your\VLC\vlc.exe"
  ```

### Install Required Python Packages

- The script uses standard Python libraries, so no additional packages are required.

---

## Usage

### Run the Script

1. Open Command Prompt.
2. Navigate to the directory containing `infinity_manager.py`:

   ```bash
   cd path\to\infinity-folder-manager
   ```

3. Run the script:

   ```bash
   python infinity_manager.py
   ```

### Using the Menu Interface

Upon running the script, you'll see the following menu:

```
--- Infinity Folder Manager ---
1. List files
2. Access and edit a file
3. Exit
Enter your choice (1/2/3):
```

- **Option 1: List Files**

  - Displays the list of compressed files in the infinity folder.

- **Option 2: Access and Edit a File**

  - Lists available compressed `.zip` files to choose from.
  - Enter the number corresponding to the file you wish to access.
  - The script will uncompress and open the file using the appropriate application.

- **Option 3: Exit**

  - Exits the script.

### Adding Files to the Infinity Folder

- Place any files you wish to manage into the `infinity` folder located at:

  ```
  C:\Users\YourUsername\OneDrive\Desktop\infinity
  ```

  Replace `YourUsername` with your actual username.

- The script will automatically compress new files placed in this folder.

### Accessing and Editing Files

#### For **Media Files** (Audio/Video)

- The script uses VLC Media Player to open media files.
- It monitors the VLC process and recompresses the file once VLC is closed.
- **No manual input is required** to recompress the file after use.

#### For **Image Files**

- The script opens image files using your default image viewer.
- After viewing the image, **return to the script's console window and press Enter** to recompress the file.
- This ensures the image file isn't recompressed before you're done viewing it.

#### For **Other Files**

- The script opens the file with its default application.
- It monitors the file's usage and recompresses it once it's no longer in use.
- **No manual input is required** after closing the file.

---

## Notes and Considerations

- **VLC Media Player**

  - VLC must be installed on your system for the script to handle media files.
  - If VLC is installed in a different location than the default, update the `VLC_PATH` variable in `infinity_manager.py`.

- **Image Files**

  - Remember to press Enter in the script's console window after you finish viewing an image file.

- **Permissions**

  - Ensure you have the necessary permissions to read, write, and execute files in the infinity folder.

- **File Types Supported**

  - **Documents**: `.txt`, `.docx`, `.pdf`, etc.
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.ico`
  - **Audio/Video**: `.mp3`, `.wav`, `.mp4`, `.avi`, `.mov`, `.wmv`, `.flac`, `.mkv`, `.mpeg`, `.mpg`

- **Customization**

  - Modify `media_extensions` and `image_extensions` lists in `infinity_manager.py` to support additional file types.

---

## Known Issues and Limitations

- **Manual Input for Image Files**

  - You must press Enter in the script after viewing an image to trigger recompression.

- **UWP Applications**

  - The script may not detect file usage correctly with UWP (Universal Windows Platform) apps like the Windows Photos app.

- **Process Monitoring**

  - The script relies on process monitoring for media files. If VLC spawns additional processes or doesn't close properly, the script may not recompress the file as expected.

---

## Future Enhancements

- **Improve Process Detection**

  - Implement more robust methods to detect when files are no longer in use, especially with UWP apps.

- **Enhanced User Interface**

  - Develop a graphical user interface (GUI) to improve usability.

- **Support for Additional Media Players**

  - Extend compatibility to other media players beyond VLC.

---

## Contributing

Contributions are welcome! If you'd like to contribute:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or support, please contact at harish.vasalamarry@gmail.com.

---

**Thank you for using the Infinity Folder Manager!**

Feel free to reach out if you have any questions or need assistance.
