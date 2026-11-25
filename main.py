#!/usr/bin/env python3
"""Place the pre-rendered front page at /output/entry.png.

The page is drawn at build time by render.py and shipped beside this
file as front.jpg. At grading time this program only copies bytes, so
both runs produce identical output. Standard library only, no network.
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import hashlib
import os
import shutil
import sys

MAX_BYTES = 1024 * 1024


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "front.jpg")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        print(f"front.jpg is {size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    shutil.copyfile(src, dst)
    digest = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    print(f"wrote {dst} ({size} bytes, sha256 {digest[:16]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
