import pypdf


class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_pdf(self):
        with open(self.file_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            pages_count = len(reader.pages)
            parts = []

            for i in range(pages_count):
                try:
                    page = reader.pages[0]
                    parts.append(page.extract_text())
                except:
                    pass

            text = " ".join(parts)
        return text
