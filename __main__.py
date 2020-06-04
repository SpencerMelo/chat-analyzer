import sys
from .file_processor import FileProcessor
from .chart_generator import ChartGenerator


def main():
    file_path = sys.argv[1]
    FileProcessor().process(file_path)
    ChartGenerator().generate()


if __name__ == "__main__":
    main()
