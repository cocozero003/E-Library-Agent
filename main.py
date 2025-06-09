from loaders.text_loader import process_text_files
from loaders.code_loader import process_code_files
from loaders.web_loader import process_web_data

if __name__ == "__main__":
    process_text_files("data/text/")
    process_code_files("data/code/")
    process_web_data("data/urls.txt")
