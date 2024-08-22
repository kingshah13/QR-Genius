# QR-Genius

![image](https://github.com/user-attachments/assets/71ddf670-7700-4cf3-8a0e-ae6593f66735)


Batch Create QR Code from an Excel file and save them as either PNG or in multiple formats.

# Installation

## 1.) Clone the repository.
Copy and paste the following command into the command prompt.
```bash
git clone https://github.com/kingshah13/QR-Genius.git
```

**or**


## Download the latest release.

Download: https://github.com/kingshah13/QR-Genius.git](https://github.com/kingshah13/QR-Genius/releases/tag/QRGenius)


## 2.) Install the dependencies.
  Copy and paste the following command into the command prompt.
```bash
pip install pandas pil qrcode[pil] tk
```

## 3.) Run the script.
```bash
python QRGenius.py
```

The script will launch a graphical user interface.

## Batch Generate QR-Code

### Select Excel File
  Click the **Browse** button to choose an Excel file containing the data for QR code generation.

### Select Columns for QR Code
  Enter the names of the columns from the Excel file that you want to include in the QR code—separate multiple columns with spaces.

### Select Filename Column
  Enter the name of the column containing filenames for the QR codes.
  
### Select Output Format
  You can choose between one file format or multiple file formats. Simply Click on as many file formats as you need and it will be selected.

### Select Output Directory
  Click the **Browse** button to choose the directory where the generated QR codes will be saved.

### Click Transparent Background
  Click the **Transparent Background** checkbox to save the QR code without a coloured background if you want to.

### Select Resolution (px) Column
  Enter the value in pixel you to adjust the resolution of the generated QR-Code.

### Generate QR Codes
  Click the **Generate QR Codes (Batch)** button to initiate the QR code generation process.



## Generate Single QR-Code

### Select Output Format
  You can choose between one file format or multiple file formats. Simply Click on as many file formats as you need and it will be selected.

### Select Output Directory
  Click the **Browse** button to choose the directory where the generated QR codes will be saved.

### Click Transparent Background
  Click the **Transparent Background** checkbox to save the QR code without a coloured background if you want to.

### Select Resolution (px) Column
  Enter the value in pixel you to adjust the resolution of the generated QR-Code.

### Enter Data for Single QR Code
  Enter URL, Words, or anything you want to convert as a QR code.
  
### Enter Filename
  Enter the name you want the file to be saved as. Do not enter the file extension at the end of the name.
