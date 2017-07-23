#!/usr/bin/env python
import json
import argparse
from rectangle import Rectangle

def intersection_points(check_rect: Rectangle, rect1: Rectangle, rect2: Rectangle):
    '''Return the intersection points'''
    # Generate the 4 corner coordinates
    check_tl = (check_rect.left, check_rect.top)
    check_tr = (check_rect.right, check_rect.top)
    check_bl = (check_rect.left, check_rect.bottom)
    check_br = (check_rect.right, check_rect.bottom)

    intersections = 0
    inter_points = []

    # Check each corner to see if it aligns with both original rectangles along x and y axes
    for coord in (check_tl, check_tr, check_br, check_bl):
        # Set/Reset validation variables
        x_coord, y_coord = None, None
        match1, match2 = False, False
        if x_coord == None:
            # Look for a match along either rectangles' X-axis
            if coord[0] in (rect1.left, rect1.right):
                x_coord = coord[0]
                match1 = True
            elif coord[0] in (rect2.left, rect2.right):
                x_coord = coord[0]
                match2 = True
        if y_coord == None:
            # Look for a match along either rectangles' Y-axis
            if coord[1] in (rect1.top, rect1.bottom):
                y_coord = coord[1]
                match1 = True
            elif coord[1] in (rect2.top, rect2.bottom):
                y_coord = coord[1]
                match2 = True

        # Only an intersection if we find both coordinates and matched both rectangles
        if (x_coord != None and y_coord != None) and (match1 and match2):
            # Find one, add it to the list as a tuple
            inter_points.append((x_coord, y_coord))
            intersections += 1

        # Once 2 intersections are found, that's all there will be
        if intersections == 2: break
    return inter_points

def intersecting(rect1: Rectangle, rect2: Rectangle):
    '''Determine if 2 Rectangles intersect and return the coordinates of the intersections'''
    intersections = []

    # Attempt to generate rectangle of overlapping area
    i_top = max(rect1.top, rect2.top)
    i_left = max(rect1.left, rect2.left)
    i_bottom = min(rect1.bottom, rect2.bottom)
    i_right = min(rect1.right, rect2.right)

    # Make sure the rectangle is valid
    if i_left < i_right and i_top < i_bottom:
        inter_rect = Rectangle(i_top, i_left, i_bottom, i_right)
        # Get intersecting points from the new rectangle
        inter_points = intersection_points(inter_rect, rect1, rect2)
        return inter_points
    return None

def containment(rect1: Rectangle, rect2: Rectangle):
    '''Determine if one rectangle fully contains another'''
    # Only check if larger contains the smaller. Equal areas cannot be contained
    if rect1.area() == rect2.area():
        return None
    elif rect1.area() > rect2.area():
        large_rect = rect1
        small_rect = rect2
    else:
        large_rect = rect2
        small_rect = rect1

    # Check for containment within X and Y axes
    hor_contain = (small_rect.left > large_rect.left and small_rect.right < large_rect.right)
    ver_contain = (small_rect.top > large_rect.top and small_rect.bottom < large_rect.bottom)
    if hor_contain and ver_contain:
        return (large_rect, small_rect)
    return None

def adjacent(rect1: Rectangle, rect2: Rectangle):
    adj = False
    if (rect1.left == rect2.right) or (rect1.right == rect2.left):
        adj = True
    elif (rect1.top == rect2.bottom) or (rect1.bottom == rect2.top):
        adj = True
    return adj


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze rectangles.')
    parser.add_argument('-j', '--json', dest='json_file', required=True)
    args = parser.parse_args()

    # Read in data file, create rectangle objects
    with open(args.json_file) as data_file:
        json_data = json.load(data_file)

    d_rect1 = json_data.pop('rectangle1')
    d_rect2 = json_data.pop('rectangle2')

    rectangle1 = Rectangle(d_rect1['top'], d_rect1['left'], d_rect1['bottom'], d_rect1['right'])
    rectangle1.name = '1'
    rectangle2 = Rectangle(d_rect2['top'], d_rect2['left'], d_rect2['bottom'], d_rect2['right'])
    rectangle2.name = '2'

    # Output the resulting rectangle coordinates
    print('Rectangle {0}: {1}'.format(rectangle1.name, rectangle1.coords()))
    print('Rectangle {0}: {1}\n'.format(rectangle2.name, rectangle2.coords()))

    # Check intersection
    intersect = intersecting(rectangle1, rectangle2)
    print('* Intersections: {0}'.format(str(intersect)))

    # Check containment
    contained = containment(rectangle1, rectangle2)
    if contained:
        print('* Containment: Rectangle {0} contains rectangle {1}'.format(contained[0].name, contained[1].name))
    else:
        print('* Containment: None')

    # Check adjacency
    adj = adjacent(rectangle1, rectangle2)
    print('* Adjacent: {0}'.format(str(adj)))
