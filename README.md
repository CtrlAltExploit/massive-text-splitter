# massive-text-splitter

`massive-text-splitter` is a Python-based tool designed to split large text files into smaller chunks with the power of parallel processing. It is efficient, highly customizable, and perfect for handling massive files like wordlists.

## Features

- **Parallel processing**: Utilizes all available CPU cores for maximum performance.
- **Customizable**: Configure input/output paths, chunk size, and the number of threads.
- **Large file support**: Easily handles files with billions of lines.
- **Error handling**: Ensures threads do not exceed CPU core limits.

## Requirements

- Python 3.8 or higher
- Works on Windows, Linux, and macOS

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/CtrlAltExploit/massive-text-splitter.git
cd txt-splitter
```

## Usage
```bash
python split_file.py --input_file "C:\path\to\wordlist.txt" --output_dir "C:\path\to\dir" --lines_per_chunk 100000000 --max_threads 16
```

## Parameters

- --input_file: Path to the large input file.
- --output_dir: Directory where the split files will be saved.
- --lines_per_chunk: Number of lines per chunk (e.g., 100 million lines = ~1.2 GB).
- --max_threads: Number of parallel threads to use (do not exceed your CPU core count).

## Example

To split the file E:\rockyou2021.txt into 100 million-line chunks, saving to E:\Wordlists\rockyou2021, and using 16 threads:

```bash
python split_file.py --input_file "E:\rockyou2021.txt" --output_dir "E:\Wordlists\rockyou2021" --lines_per_chunk 100000000 --max_threads 16
```
**Note: 100 million lines are approximately 1.2 GB in size if each line contains a single word.**

## Output
The tool will create files in the specified output directory, named as:
```bash
chunk_0.txt
chunk_1.txt
chunk_2.txt
...
```
Each file will contain the specified number of lines (except the last one, which may contain fewer).

## Contribution
Feel free to fork this repository and contribute! Open a pull request with your improvements or bug fixes.

