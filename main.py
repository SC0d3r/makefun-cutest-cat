"""Copy the entry's cat picture to the grader's output directory."""

import os

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"
MAX_BYTES = 1048576

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(BASE_DIR, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        raise ValueError("entry.png is missing next to main.py")

    size = os.path.getsize(SOURCE)
    if size > MAX_BYTES:
        raise ValueError("entry.png is larger than 1 MiB ({} bytes)".format(size))

    with open(SOURCE, "rb") as f:
        data = f.read()

    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        raise ValueError("entry.png is not a PNG or JPEG file")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
