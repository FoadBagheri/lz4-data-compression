import lz4.frame
import os


def compress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as input_file:
        original_data = input_file.read()

    compressed_data = lz4.frame.compress(original_data)

    with open(output_filename, 'wb') as output_file:
        output_file.write(compressed_data)


def decompress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as input_file:
        compressed_data = input_file.read()

    decompressed_data = lz4.frame.decompress(compressed_data)

    with open(output_filename, 'wb') as output_file:
        output_file.write(decompressed_data)


if __name__ == "__main__":
    input_filename = "input.txt"
    compressed_filename = "compressed.lz4"
    decompressed_filename = "decompressed.txt"

    original_size = os.path.getsize(input_filename)
    print(f"Original File Size: {original_size} bytes")

    compress_file(input_filename, compressed_filename)
    compressed_size = os.path.getsize(compressed_filename)
    print(f"Compressed File Size: {compressed_size} bytes. Check '{compressed_filename}'.")

    decompress_file(compressed_filename, decompressed_filename)
    decompressed_size = os.path.getsize(decompressed_filename)
    print(f"Decompressed File Size: {decompressed_size} bytes. Check '{decompressed_filename}'.")
