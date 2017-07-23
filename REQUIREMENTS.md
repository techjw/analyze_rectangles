# Rectangle Analysis Utility Requirements

## Language
* The chosen language for the solution will be Python3 (3.6.2)

## Coordinate Plane
* Following computer software 2D graphics standards, the origin point (0,0) will be expected in the top-left with the x-axis incrementing left-to-right and the y-axis incrementing top-to-bottom.

## Entities
#### Rectangle
Following standard rectangle definition practices:
* _Attributes_
  * Top (y-axis lower boundary)
  * Left (x-axis lower boundary)
  * Bottom (y-axis upper boundary)
  * Right (x-axis upper boundary)


## Algorithms
#### Intersection
  * _Analyze:_ Determine whether two rectangles have one or more intersecting lines
  * _Output:_ Points of intersection.
  * _Constraints:_
    1. Intersecting rectangles cannot pass containment rules.
    1. Intersecting rectangles cannot pass adjacency rules.
    1. Intersecting rectangles should only have 2 points of intersection.

#### Containment
  * _Analyze:_ Determine whether a rectangle is wholly contained within another rectangle.
  * _Output:_ Statement of containment (e.g. rectangle A contains rectangle B), or None
  * _Constraints:_
    1. Contained rectangles cannot pass intersection rules.
    1. Contained rectangles should not pass adjacency rules. (The sharing of a side implies they touch and as such are not fully contained.)
    1. Rectangles of equal areas cannot contain each other.

#### Adjacency
  * _Analyze:_ Detect whether two rectangles are adjacent. Adjacency is defined as the sharing of a side. Side sharing may be proper or sub-line, where a sub-line share is one where one side of rectangle A is a line that exists as a set of points wholly contained on some other side of rectangle B.
  * _Output:_ True|False
  * _Constraints:_
    1. Adjacent rectangles cannot pass intersection rules.
    1. Adjacent rectangles should not pass containment rules. (The sharing of a side implies they touch and as such are not fully contained.)


## Data Input Method
Data about the two rectangles to be analyzed must be provided in a consistent manner. As there is no hard requirement given for the nature of the data input, the choice has been made to provide a structured JSON data file via executable parameter. The expected structure is as follows:
```
{
  "rectangle1": {
    "top": 123,
    "left": 123,
    "bottom": 456,
    "right": 456
  },
  "rectangle2": {
    "top": 234,
    "left": 234,
    "bottom": 567,
    "right": 567
  }
}
```
