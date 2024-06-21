# QR-Genius

![image](https://github.com/kingshah13/QR-Genius/assets/67662365/c3e5f142-cad2-4b53-88b0-160b4f47f199)


Batch Create QR Code from an Excel file and save them as either PNG or PDF

This Python script provides a simple GUI application for batch-generating QR codes from an Excel file. It utilizes the `pandas` library to handle Excel files and the `qrcode` library to generate QR codes.

# Installation

## 1.) Clone this repository to your local machine.
Copy and paste the following command into the command prompt.

```bash
git clone https://github.com/kingshah13/QR-Genius.git
```
wait for the installation to finish then
copy and paste this

```bash
cd QR-Genius
```
## 2.) Install the dependencies.
  Copy and paste the following command into the command prompt.
```bash
pip install pandas openpyxl qrcode[pil] tk
```

## 3.) Run the script.
```bash
pyhton GQRcode.py
```

The script will launch a graphical user interface.

## How to Use

### Select Excel File
  Click the **Browse** button to choose an Excel file containing the data for QR code generation.

### Select Columns for QR Code
  Enter the names of the columns from the Excel file that you want to include in the QR code—separate multiple columns with spaces.

### Select Filename Column
  Enter the name of the column containing filenames for the QR codes.
  
### Select Output Format
  Choose between **PNG** and **PDF** as the desired output format.

### Select Output Directory
  Click the **Browse** button to choose the directory where the generated QR codes will be saved.

### Generate QR Codes
  Click the **Generate QR Codes** button to initiate the QR code generation process.
