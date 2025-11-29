# python3 -m homework data/input data/output

import argparse
import sys


def parse_args():

    parser = argparse.ArgumentParser(description="Count words in files")

    parser.add_argument("input", type=str, help="Path to the input folder")
    parser.add_argument("output", type=str, help="Path to the output folder")

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def main():
    input_folder, output_folder = parse_args()

    print(f"Input Path: {input_folder}")
    print(f"Output Path: {output_folder}")
