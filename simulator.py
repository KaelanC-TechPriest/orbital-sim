from math import pow, sqrt
import time

SPACE_SIZE = 100
TIME_STEP = 6 * pow(10,7)

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
        self.x += (self.velocity_x * TIME_STEP) / pow(20, 9)
        self.y += (self.velocity_y * TIME_STEP) / pow(20, 9)
        print(f"x: {self.x}, y: {self.y}")
        print(f"v_x: {self.velocity_x}, v_y: {self.velocity_y}")
        if (self.x > SPACE_SIZE or self.x < 0):
            raise ValueError("Out of bounds")
        if (self.y > SPACE_SIZE or self.y < 0):
            raise ValueError("Out of bounds")

def accel_g(M, r):
    r = r * pow(20, 9)
    const_G = 6.67408 * pow(10, -11)
    print(f"Accel: {const_G * M / pow(r, 2)}")
    return const_G * M / pow(r, 2)

def main():
    bodies = [
        Body(
            1.98892 * pow(10,30),
            50,
            50,
            0,
            0,
            "@"
            ), 
        Body(
            1.3 * pow(10,25),
            50,
            13,
            pow(13.07, 3),
            0,
            "o"
            )
        ]

    while True:
        GRID = [["#" for _ in range(SPACE_SIZE)] for _ in range(SPACE_SIZE)]

        print("\x1B[2J\x1B[H")
        for body in bodies:
            GRID[int(body.y)][int(body.x)] = body.character

        for i in range(SPACE_SIZE):
            for j in range(SPACE_SIZE):
                print(GRID[i][j], end="")
            print()

        # calculate accelerations
        for i in range(len(bodies)):
            body1 = bodies[i]
            accel_x = 0
            accel_y = 0
            for j in range(len(bodies)):

                if (i == j): continue

                body2 = bodies[j]
                dist_x = abs(body1.x - body2.x)
                dist_y = abs(body1.y - body2.y)
                distance = sqrt(pow(dist_x, 2) + pow(dist_y, 2))

                acceleration = accel_g(body2.mass, distance)

                accel_x += acceleration * dist_x / (distance * pow(20, 9))
                accel_y += acceleration * dist_y / (distance * pow(20, 9))

            body1.velocity_x += accel_x * TIME_STEP
            body1.velocity_y += accel_y * TIME_STEP

            body1.move()


        time.sleep(.5)

if __name__ == "__main__":
    main()
