from math import pow, sqrt
import time

MAX_SPACE_X = 100
MAX_SPACE_Y = 500
TIME_STEP = 1

class Body:

    x = 0.
    y = 0.
    velocity_x = 0.
    velocity_y = 0.
    mass = 0
    character = ""

    def __init__(self, mass, x, y, v_x, v_y, character):
        self.mass = mass
        self.x = x
        self.y = y
        self.velocity_x = v_x
        self.velocity_y = v_y
        self.character = character

    def move(self):
        self.x += self.velocity_x * TIME_STEP
        self.y += self.velocity_y * TIME_STEP
        print(f"x: {self.x}, y: {self.y}")
        print(f"v_x: {self.velocity_x}, v_y: {self.velocity_y}")
        if (self.x > MAX_SPACE_X or self.x < 0):
            raise ValueError("Out of bounds")
        if (self.y > MAX_SPACE_Y or self.y < 0):
            raise ValueError("Out of bounds")

def accel_g(M, r):
    const_G = pow(10, -3)
    return const_G * M / pow(r, 2)

def main():
    bodies = [
        Body(
            2. * pow(10,4),
            MAX_SPACE_X / 2,
            MAX_SPACE_Y / 2,
            0,
            0,
            "@"
            ), 
        Body(
            1.0 * pow(10,2),
            MAX_SPACE_X / 2,
            MAX_SPACE_Y / 2 - 10,
            1,
            0,
            "o"
            )
        ]

    while True:
        GRID = [["." for _ in range(MAX_SPACE_X)] for _ in range(MAX_SPACE_Y)]

        print("\x1B[2J\x1B[H")
        for body in bodies:
            GRID[int(body.y)][int(body.x)] = body.character

        for i in range(MAX_SPACE_X):
            for j in range(MAX_SPACE_Y):
                print(GRID[j][i], end="")
            print()

        # calculate accelerations
        for i in range(len(bodies)):
            body1 = bodies[i]
            accel_x = 0
            accel_y = 0
            for j in range(len(bodies)):

                if (i == j): continue

                body2 = bodies[j]
                dist_x = body1.x - body2.x
                dist_y = body1.y - body2.y
                distance = sqrt(pow(dist_x, 2) + pow(dist_y, 2))

                acceleration = accel_g(body2.mass, distance)

                accel_x -= acceleration * dist_x / distance
                accel_y -= acceleration * dist_y / distance
                print(f"Accel: {acceleration} {accel_x} {accel_y}")

            body1.velocity_x += accel_x * TIME_STEP
            body1.velocity_y += accel_y * TIME_STEP

            body1.move()


        time.sleep(.5)

if __name__ == "__main__":
    main()
