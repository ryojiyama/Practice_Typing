from pathlib import Path
import PyPDF2

# Merge PDF Files

# Directory containing PDF files
pdf_dir = Path("./pdf_files")
# Get a sorted list of all PDF files in the directory
pdf_files = sorted(pdf_dir.glob("*.pdf"))

# Create a PDF writer object
pdf_writer = PyPDF2.PdfFileWriter()
# Iterate through each PDF file
for pdf_file in pdf_files:
    # Create a PDF reader object for the current file
    pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
    # Iterate through each page of the current PDF
    for i in range(pdf_reader.getNumPages()):
        # Add the current page to the writer object
        pdf_writer.addPage(pdf_reader.getPage(i))

# Create the name of the merged file using the first and last file names
merged_file = pdf_files[0].stem + "-" + pdf_files[-1].stem + ".pdf"

# Save the merged PDF
with open(merged_file, "wb") as f:
    pdf_writer.write(f)
