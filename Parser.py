from pyresparser import ResumeParser
from docx import Document

def parse(filepath):
    try:
        doc = Document()
        with open(filepath, 'r', encoding='utf-8') as file:
            doc.add_paragraph(file.read())
        doc.save("text.docx")
        data = ResumeParser('text.docx').get_extracted_data()
        return data
    except:
        data = ResumeParser(filepath).get_extracted_data()
        return data