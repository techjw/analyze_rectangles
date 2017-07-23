# analyze_rectangles
Analyze intersection, containment, and adjacency of two rectangles

## Progam components
* `rectangle.py`
  * Module defining the `Rectangle` class object
* `analyze.py`
  * Main analysis program
  * Usage: `python analyze.py -j rectangles_data.json`
    * Explicitly specifying `python` is only necessary if Windows does not have .py files configured for execution, or if the file is not given execute permissions on Linux.

## Testing data files
* `test_files/adjacent1.json`
  * Horizontally adjacent rectangles (left/right)
* `test_files/adjacent2.json`
  * Vertically adjacent rectangles (top/bottom)
* `test_files/adjacent3.json`
  * Non-adjacent rectangles
* `test_files/containment1.json`
  * Rectangle containing another rectangle
* `test_files/containment2.json`
  * Non-contained rectangles
* `test_files/intersect1.json`
  * Intersecting rectangles, both insection points on one side
* `test_files/intersect2.json`
  * Intersecting rectangles, intersection points on 2 sides
* `test_files/intersect3.json`
  * Non-intersecting rectangles
