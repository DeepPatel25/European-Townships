# European-Townships

## Problem

You have been given the contract to paint all houses in all his townships by a European Contractor. Each township was houses of different sizes.

This has been your biggest-ever contract, so you ask the following questions for which you have been answered:

Each house has a Victorian-style hall which has 6 walls.

Bedrooms on the roof will only have 3 walls.

Each house has a standard kitchen.

All other rooms are standard rooms with 4 walls.


For painting a house, the contractor has some specific requirements for all rooms;

She wants to paint ⅓ of the room walls with an accent colour and ⅔ of the room walls with normal colour.


The accent colour required to paint each wall is 1.5 litres and it takes 2.5 hours to paint the wall.

The regular colour required to paint a wall is 2.25 litres and it takes 3.25 hours to paint the wall.


You have to write an algorithm to calculate the number of hours it would take to paint each township along with the quantity required to paint all “accent” and “regular” walls, rounded off to two decimal places.

## Input
    T = Townships
    N = houses 
    H = Victorian style halls
    S = Standard rooms
    R = Roof bed rooms

    T
    N
    Total bedrooms, R, S, H

## Output
Case #: total hours, accent qty, regular qty

<hr/>
## Limits

    1 < T < 30
    50 < N < 150 (small)
    175 < N < 500 (large)
    1 < Total bedrooms < 13 (small)
    1 < Total bedrooms < 100 (large)

# Sample
## Sample Input


    2
    1
    4, 1, 4, 1
    2
    5, 2, 4, 1
    4, 1, 4, 1

## Sample Output


    Case #1: 75.00, 12.50, 37.50
    Case #2: 159.00, 26.50, 79.50