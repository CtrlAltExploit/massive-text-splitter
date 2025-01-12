import os
import argparse
from multiprocessing import Pool, cpu_count
from functools import partial

def count_lines(file_path):
    """Count the number of lines in the file, trying different encodings."""
    encodings = ['utf-8', 'latin1', 'ISO-8859-1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                print(f"Using encoding: {encoding} for counting lines.")
                return sum(1 for _ in f)
        except UnicodeDecodeError:
            print(f"Encoding {encoding} failed, trying the next one...")
    raise UnicodeDecodeError("None of the tested encodings worked.")

def process_chunk(input_file, start_line, end_line, chunk_index, output_dir):
    """Process a single chunk of lines, trying different encodings."""
    encodings = ['utf-8', 'latin1', 'ISO-8859-1']
    for encoding in encodings:
        try:
            with open(input_file, 'r', encoding=encoding) as infile:
                output_file = os.path.join(output_dir, f"chunk_{chunk_index}.txt")
                with open(output_file, 'w', encoding=encoding) as outfile:
                    for current_line_num, line in enumerate(infile, start=1):
                        if start_line <= current_line_num <= end_line:
                            outfile.write(line)
                        if current_line_num > end_line:
                            break
                print(f"Chunk {chunk_index} processed: {output_file}")
                return
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"None of the tested encodings worked for chunk {chunk_index}.")

def main():
    # Handle command-line arguments
    parser = argparse.ArgumentParser(
        description="Split large TXT files into smaller chunks with parallel processing.",
        epilog="Example usage: python split_file.py --input_file \"E:\\rockyou2021.txt\" --output_dir \"E:\\Wordlists\\rockyou2021\" --lines_per_chunk 100000000 --max_threads 16\n"
               "Note: 100 million lines are approximately 1.2 GB in size if each line contains a single word."
    )
    parser.add_argument("--input_file", required=True, help="Path to the large input file")
    parser.add_argument("--output_dir", required=True, help="Directory where the output files will be saved")
    parser.add_argument("--lines_per_chunk", type=int, required=True, help="Number of lines per chunk")
    parser.add_argument("--max_threads", type=int, required=True, help="Number of parallel threads to use")
    args = parser.parse_args()

    # Check CPU core availability
    available_cores = cpu_count()
    if args.max_threads > available_cores:
        print(f"ERROR: Specified number of threads ({args.max_threads}) exceeds the available CPU cores ({available_cores}).")
        return

    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    # Count the total number of lines
    print("Counting the total number of lines...")
    total_lines = count_lines(args.input_file)
    print(f"Total lines: {total_lines}")

    # Create ranges for processing
    print("Creating processing ranges...")
    ranges = [
        (args.input_file, i * args.lines_per_chunk + 1, min((i + 1) * args.lines_per_chunk, total_lines), i, args.output_dir)
        for i in range((total_lines + args.lines_per_chunk - 1) // args.lines_per_chunk)
    ]

    # Process chunks with parallel threads
    print("Processing chunks with parallel threads...")
    with Pool(args.max_threads) as pool:
        pool.starmap(partial(process_chunk), ranges)

if __name__ == "__main__":
    main()
