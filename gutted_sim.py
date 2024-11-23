from math import pow, sqrt
import time

MAX_SPACE_X = 100
MAX_SPACE_Y = 300
TIME_STEP = 1

class Body:

    x = 0.
    y = 0.
    velocity_x = 0.
    velocity_y = 0.
    mass = 0
    character = ""
    is_interstellar = False

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
        if (self.x > MAX_SPACE_X or self.x < 0 or self.y > MAX_SPACE_Y or self.y < 0):
            return False
        else:
            return True

def accel_g(M, r):
    const_G = pow(10, -4)
    return const_G * M / pow(r, 2)

def main():
    bodies = [
        Body(
            4. * pow(10,5),
            MAX_SPACE_X / 2,
            MAX_SPACE_Y / 2,
            0,
            0,
            # colored character @
            "\u001b[33m\u2588\u001b[0m"
            ), 

        Body(
            1.0 * pow(10,4),
            MAX_SPACE_X / 2,
            MAX_SPACE_Y / 2 - 10,
            1,
            0,
            # colored character o
            "\u001b[32m\u2588\u001b[0m"
            ),

        Body(
            1.0 * pow(10,4),
            MAX_SPACE_X / 2,
            MAX_SPACE_Y / 2 + 20,
            -1,
            0,
            # colored character 0
            "\u001b[31m\u2588\u001b[0m"
            ), 

        Body(
            1.0 * pow(10,4),
            MAX_SPACE_X / 2,
            MAX_SPACE_Y / 2 - 20,
            1,
            0,
            # colored character o
            "\u001b[32m\u2588\u001b[0m"
            ),

        Body(
            1.0 * pow(10,4),
            MAX_SPACE_X / 2,
            MAX_SPACE_Y / 2 + 30,
            -1,
            0,
            # colored character o
            "\u001b[20m\u2588\u001b[0m"
            ),

        ]

    while True:
        GRID = [[" " for _ in range(MAX_SPACE_X)] for _ in range(MAX_SPACE_Y)]

        print("\x1B[2J\x1B[H")
        for body in bodies:
            if (body.is_interstellar): continue
            body_y = int(body.y)
            body_x = int(body.x)
            GRID[body_y][body_x] = body.character
            #GRID[body_y+1][body_x] = body.character
            #GRID[body_y-1][body_x] = body.character
            #GRID[body_y][body_x+1] = body.character
            #GRID[body_y][body_x-1] = body.character

        for i in range(MAX_SPACE_X):
            for j in range(MAX_SPACE_Y):
                print(GRID[j][i], end="")
            print()

        # calculate accelerations
        for i in range(len(bodies)):
            body1 = bodies[i]
            if (body1.is_interstellar): continue

            accel_x = 0
            accel_y = 0
            for j in range(len(bodies)):

                if (i == j): continue

                body2 = bodies[j]
                if (body2.is_interstellar): continue

                dist_x = body1.x - body2.x
                dist_y = body1.y - body2.y
                distance = sqrt(pow(dist_x, 2) + pow(dist_y, 2))

                acceleration = accel_g(body2.mass, distance)

                accel_x -= acceleration * dist_x / distance
                accel_y -= acceleration * dist_y / distance
                print(f"Accel: {acceleration} x: {accel_x} y: {accel_y}")

            body1.velocity_x += accel_x * TIME_STEP
            body1.velocity_y += accel_y * TIME_STEP

            in_bounds = body1.move()
            if (not in_bounds): body1.is_interstellar = True


        time.sleep(.5)

if __name__ == "__main__":
    main()
