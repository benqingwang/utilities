from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def convert_png_to_pdf(png_files, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)

    for png_file in png_files:
        img = Image.open(png_file)
        width, height = img.size
        aspect = height / float(width)
        c.setPageSize((letter[0], letter[0] * aspect))
        c.drawImage(png_file, 0, 0, width=letter[0], height=letter[0] * aspect)
        c.showPage()

    c.save()

if __name__ == '__main__':
    png_files = ['image1.png', 'image2.png', 'image3.png']  # List of PNG files to combine
    output_pdf = 'combined.pdf'  # Output PDF file name

    convert_png_to_pdf(png_files, output_pdf)
