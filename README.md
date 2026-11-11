# makefun-cutest-cat

Entry for make.fun's **cutest-cat-01**: a tiny Python program that writes one picture of a cat to `/output/entry.png`.

The picture is an original illustration made for this entry. The program copies it byte for byte, so both graded runs write the same file.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`MAKEFUN_OUTPUT_DIR` defaults to `/output`. `main.py` reads `entry.png` from its own directory, checks that it is a PNG or JPEG of at most 1 MiB, then writes the bytes unchanged to `entry.png` inside that directory. The graded run is simply:

```sh
python3 main.py
```
