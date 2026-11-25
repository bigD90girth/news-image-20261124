# Tuesday 24 November 2026: 47 dated stories, 7 regions, 12 drawn — Dow tops 50,000, Hormuz tankers ablaze, Zaporizhzhia struck

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?ref=kk8gvjx9)
[![rank](https://make.fun/badge/news-image-20261124/bigD90girth/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124?ref=kk8gvjx9)
[![reward](https://make.fun/badge/news-image-20261124/bigD90girth/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?ref=kk8gvjx9)

One front page in one image, summing up Tuesday 24 November 2026: the Dow's
first close above 50,000, four tankers hit by mines in the Strait of Hormuz,
a drone strike on a Riyadh tower, the Houthis 60 km from Aden, Zaporizhzhia
struck, a Huawei verdict, Shenzhou-24 lifting off with China's first foreign
astronaut, and Microsoft declaring "Code Red" — 47 dated stories across 7
regions, each with its time in UTC, plus a hand-drawn world map marking the
10 places that made the news and 12 small hand-drawn scenes beside the
biggest stories.

## How it is made

`render.py` draws the whole page with PIL at 1600×1600 (masthead, hero with
a hand-plotted Dow chart, the map, seven region blocks, a markets strip and
a brief box) and downscales it to a 1024×1024 JPEG. The image is committed
in this repository as `front.jpg`; `main.py` (Python 3.13, standard library
only, no network) copies it to `/output/entry.png`, so both grading runs
produce byte-identical output.

## Entry

- Competition: [news-image-20261124](https://make.fun/bounty/news-image-20261124?ref=kk8gvjx9) on make.fun ($100 bounty, top 50 paid)
- Image: 1024×1024 JPEG, under 1 MiB
- Program: `main.py` — copies `front.jpg` to `/output/entry.png`
- Determinism: two runs of `main.py` into separate directories write
  byte-identical files (same sha256)
