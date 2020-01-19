from bs4 import BeautifulSoup
import urllib.request as urllib2
import argparse

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import io

def arg():
    parser = argparse.ArgumentParser()

    parser.add_argument("url",type=str,help="Input Phrase")

    args = parser.parse_args()

    input_phrase = args.url

    return input_phrase

def get_html_text(url):
    """
    Gets the text of an html page.

    Inputs:
        url (String) - Url for the webpage
    Outputs:
        text (Concanted String)
    """
    html_page = urllib2.urlopen(url)

    soup = BeautifulSoup(html_page.read(),features="lxml",from_encoding='utf-8')
    print("PRINTING " + url)
    return soup.get_text()

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a pdf file
    """
    with open(pdf_path, 'rb') as fh:
        # iterate over all pages of PDF document
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            # creating a resoure manager
            resource_manager = PDFResourceManager()

            # create a file handle
            fake_file_handle = io.StringIO()

            # creating a text converter object
            converter = TextConverter(
                                resource_manager,
                                fake_file_handle,
                                codec='utf-8',
                                laparams=LAParams()
                        )

            # creating a page interpreter
            page_interpreter = PDFPageInterpreter(
                                resource_manager,
                                converter
                            )

            # process current page
            page_interpreter.process_page(page)

            # extract text
            text = fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()

def get_pdf_text(file_path):
    text = ""
    for page in extract_text_from_pdf(file_path):
        text += ' ' + page
    return text

if __name__ == "__main__":
    print(get_html_text(""))
