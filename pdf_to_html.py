from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO

def pdf_to_html(pdf_file):
    output_string = StringIO()
    with open(pdf_file, 'rb') as f:
        extract_text_to_fp(f, output_string, laparams=LAParams(), output_type='html', codec=None)
    html_content = output_string.getvalue()
    output_string.close()
    return html_content

# Example usage
pdf_file = "example.pdf"
html_content = pdf_to_html(pdf_file)
print(html_content)
