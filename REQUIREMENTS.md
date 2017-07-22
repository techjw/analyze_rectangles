# Rectangle Analysis Utility Requirements

## Entities
#### Rectangle
* _Attributes_
  * Top X-axis coordinate
  * Top Y-axis coordinate
  * Bottom X-axis coordinate
  * Bottom Y-axis coordinate


## Algorithms
#### Intersection
  * _Analyze:_ Determine whether two rectangles have one or more intersecting lines
  * _Output:_ True|False, points of intersection.

#### Containment
  * _Analyze:_ Determine whether a rectangle is wholly contained within another rectangle.
  * _Output:_ True|False, statement of containment (e.g. rectangle A contains rectangle B)

#### Adjacency
  * _Analyze:_ Detect whether two rectangles are adjacent. Adjacency is defined as the sharing of a side. Side sharing may be proper or sub-line, where a sub-line share is one where one side of rectangle A is a line that exists as a set of points wholly contained on some other side of rectangle B.
  * _Output:_ True|False


## Data Input Method
Data about the two rectangles to be analyzed must be provided in a consistent manner. As there is no hard requirement given for the nature of the data input, the choice has been made to provide a structured JSON data file via executable parameter. The expected structure is as follows:
```
{
  "rectangle1": {
    "x1": 123,
    "y1": 123,
    "x2": 456,
    "y2": 456
  },
  "rectangle2": {
    "x1": 234,
    "y1": 234,
    "x2": 567,
    "y2": 567
  }
}
```
