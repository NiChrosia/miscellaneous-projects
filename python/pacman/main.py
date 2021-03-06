from collections import namedtuple

import pygame

Coordinate = namedtuple('Coordinate', ['x', 'y'])

TUNNEL_SIZE = 40


def create_map(file):
    junctions = []
    rails = []
    with open(file) as blueprint:
        for line in blueprint:
            if line[0] == 'J':
                junction = []
                for item in line[1:].split(', '):
                    junction.append(int(item))
                junctions.append(Coordinate(*junction))
            elif line[0] == 'R':
                rail = []
                for item in line[1:].split(', '):
                    rail.append(int(item))
                rails.append(rail)
    return junctions, rails


def get_wall_dots(junctions):
    walldots = []
    for junction in junctions:
        walldots.append([
            Coordinate(junction[0] - TUNNEL_SIZE, junction[1] - TUNNEL_SIZE),
            Coordinate(junction[0] + TUNNEL_SIZE, junction[1] - TUNNEL_SIZE),
            Coordinate(junction[0] - TUNNEL_SIZE, junction[1] + TUNNEL_SIZE),
            Coordinate(junction[0] + TUNNEL_SIZE, junction[1] + TUNNEL_SIZE),
        ])
    return walldots


def get_walls(junctions_directions, wall_dots, junctions):
    walls = []
    for iterator, junction in enumerate(junctions):
        if 'DOWN' not in junctions_directions[iterator]:
            walls.append([wall_dots[iterator][2], wall_dots[iterator][3]])
        if 'UP' not in junctions_directions[iterator]:
            walls.append([wall_dots[iterator][0], wall_dots[iterator][1]])
        if 'LEFT' not in junctions_directions[iterator]:
            walls.append([wall_dots[iterator][0], wall_dots[iterator][2]])
        if 'RIGHT' not in junctions_directions[iterator]:
            walls.append([wall_dots[iterator][1], wall_dots[iterator][3]])
    return walls


def config_directions(rail_directions, junctions_directions, junctions, rails):
    for iterator, junction in enumerate(junctions):
        junctions_directions[iterator] = []
    for start_junction, end_junction in rails:
        if junctions[start_junction].x - junctions[end_junction].x == 0:
            rail_directions.append('VERTICAL')
            junctions_directions[start_junction].append('DOWN')
            junctions_directions[end_junction].append('UP')
        else:
            rail_directions.append('HORIZONTAL')
            junctions_directions[start_junction].append('RIGHT')
            junctions_directions[end_junction].append('LEFT')
    return rail_directions, junctions_directions


def line(screen, color, start, end, width):
    pygame.draw.line(screen, color, start, end, width)


def main():
    junctions, rails = create_map('junctions_rails.txt')
    window = (1000, 750)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption('PACMAN')
    screen.fill((255, 255, 255))
    black = (0, 0, 0)
    rail_directions, junctions_directions = config_directions([], {}, junctions, rails)
    wall_dots = get_wall_dots(junctions)
    walls = get_walls(junctions_directions, wall_dots, junctions)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for start, end in rails:
            line(screen, (0, 0, 255), junctions[start], junctions[end], 5)

        for index, junction in enumerate(junctions):
            pygame.draw.circle(screen, (100, 100, 255), junction, 20, 0)
            junctions_directions[index] = []

        for wall_dots_surrounding_junction in wall_dots:
            for walldot in wall_dots_surrounding_junction:
                pygame.draw.circle(screen, black, walldot, 2, 0)

        for start_junction, end_junction in rails:
            if junctions[start_junction].x - junctions[end_junction].x == 0:
                rail_directions.append('VERTICAL')
                junctions_directions[start_junction].append('DOWN')
                junctions_directions[end_junction].append('UP')
            else:
                rail_directions.append('HORIZONTAL')
                junctions_directions[start_junction].append('RIGHT')
                junctions_directions[end_junction].append('LEFT')

        for rail, rail_direction in zip(rails, rail_directions):
            if rail_direction == 'HORIZONTAL':
                start, end = wall_dots[rail[0]][1], wall_dots[rail[1]][0]
                line(screen, black, start, end, 5)
                start, end = wall_dots[rail[0]][3], wall_dots[rail[1]][2]
                line(screen, black, start, end, 5)
            elif rail_direction == 'VERTICAL':
                start, end = wall_dots[rail[0]][2], wall_dots[rail[1]][0]
                line(screen, black, start, end, 5)
                start, end = wall_dots[rail[0]][3], wall_dots[rail[1]][1]
                line(screen, black, start, end, 5)

        for start, end in walls:
            line(screen, black, start, end, 5)

        pygame.display.flip()


if __name__ == '__main__':
    main()