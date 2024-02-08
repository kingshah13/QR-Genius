import pandas as pd
import qrcode
from tkinter import Tk, filedialog, Label, Button, OptionMenu, StringVar, Entry  # Import Entry widget
from PIL import Image

file_path_var = None
output_directory_var = None

def generate_qr_codes(file_path, selected_columns, filename_column, output_format, output_directory):
    # Load Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Check if the selected columns exist in the DataFrame
    for col in selected_columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in the Excel file.")

    # Check if the filename column exists in the DataFrame
    if filename_column not in df.columns:
        raise ValueError(f"Column '{filename_column}' not found in the Excel file.")

    # Loop through rows and generate QR codes
    for index, row in df.iterrows():
        data = ''.join([str(row[col]) for col in selected_columns])
        filename = str(row[filename_column])

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code as PNG or PDF
        if output_format == "PNG":
            img.save(f"{output_directory}/{filename}.png")
        elif output_format == "PDF":
            img.save(f"{output_directory}/{filename}.pdf", "PDF", resolution=100.0)

def browse_file():
    global file_path_var
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    file_path_var.set(file_path)

def browse_directory():
    global output_directory_var
    directory_path = filedialog.askdirectory()
    output_directory_var.set(directory_path)

def generate_qr_codes_gui():
    global file_path_var, output_directory_var
    root = Tk()
    root.title("QR Code Generator")

    file_path_var = StringVar()
    output_directory_var = StringVar()

    Label(root, text="Select Excel File:").grid(row=0, column=0)
    Button(root, text="Browse", command=browse_file).grid(row=0, column=1)

    Label(root, text="Select Columns for QR Code:").grid(row=1, column=0)
    selected_columns_var = StringVar()
    Entry(root, textvariable=selected_columns_var).grid(row=1, column=1)

    Label(root, text="Select Filename Column:").grid(row=2, column=0)
    filename_column_var = StringVar()
    Entry(root, textvariable=filename_column_var).grid(row=2, column=1)

    Label(root, text="Select Output Format:").grid(row=3, column=0)
    output_format_var = StringVar()
    OptionMenu(root, output_format_var, "PNG", "PDF").grid(row=3, column=1)

    Label(root, text="Select Output Directory:").grid(row=4, column=0)
    Button(root, text="Browse", command=browse_directory).grid(row=4, column=1)

    Button(root, text="Generate QR Codes", command=lambda: generate_qr_codes(
        file_path_var.get(),
        selected_columns_var.get().split(),  # Convert string to list
        filename_column_var.get(),
        output_format_var.get(),
        output_directory_var.get()
    )).grid(row=5, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    generate_qr_codes_gui()
