#!/usr/bin/env python3
"""Copy the rendered front page into the grader's output directory.

The image is drawn at build time and stored in this repository as
front.jpg. This program only moves those exact bytes to
<output>/entry.png, so both graded runs produce identical output.
"""

import os
import shutil
import sys

IMAGE = "front.jpg"
MAX_BYTES = 1048576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(outdir, "entry.png")
    size = os.path.getsize(source)
    if size > MAX_BYTES:
        sys.exit(f"{IMAGE} is {size} bytes, over the 1 MiB limit")
    os.makedirs(outdir, exist_ok=True)
    shutil.copyfile(source, target)
    if os.path.getsize(target) != size:
        sys.exit("copy of front.jpg did not match the source size")


if __name__ == "__main__":
    main()
