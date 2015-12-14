#!/bin/python3
#
# This simple agent goes up until it finds a wall, then it turns left and goes through the maze
# having the wall on its right side until it finds an exit.
#

def move(view):
    # If we can see the exit we go to it
    if view[0][1] == 'e':
        print('UP')
    elif view[1][0] == 'e':
        print('LEFT')
    elif view[1][2] == 'e':
        print('RIGHT')
    elif view[2][1] == 'e':
        print('DOWN')

    # If there is a wall to the right follow it
    elif view[1][2] == '#' and view[0][1] == '-':
        print('UP')

    # If there is a corner to the right we turn right
    elif view[2][2] == '#' and view[1][2] == '-':
        print('RIGHT')

    # If we hit a wall we go left
    elif view[0][1] == '#' and view[1][0] == '-':
        print('LEFT')

    # If we hit a wall and there is a wall to the left we turn around
    elif view[0][1] == '#' and view[1][0] == '#':
        print('DOWN')

    # Go up until we get to a wall
    elif view[0][1] == '-':
        print('UP')


def main():
    player = input()

    view = []
    view.append(input())
    view.append(input())
    view.append(input())

    move(view)


if __name__ == "__main__":
    main()
