import random, pygame, math

window_size = (640, 480)
clock = pygame.time.Clock()

class Fish:
    def __init__(self, x, y, fish_image, x_s = 10, y_s = 10):
        self.x = 0
        self.y = 400
        self.x_s = 10
        self.y_s = 10
        self.velocity = (random.uniform(-1, 1)/x_s, random.uniform(-1, 1)/y_s)
        self.image = pygame.transform.scale(fish_image, (50, 50))
        self.flipped = 0

    def move(self):
        self.listen()

        # If the fish goes off the screen, wrap it around to the other side
        if self.y + 10 > window_size[1] - 30 or self.y < 110:
            self.velocity = (self.velocity[0], -self.velocity[1])

        if self.x + 20 > window_size[0] or self.x < 0:
            self.velocity = (-self.velocity[0], self.velocity[1])
        
        # Update velocity or randomly slow down
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.direction()

    def listen(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate the distance between the fish and the mouse
        dx = self.x - mouse_x
        dy = self.y - mouse_y

        # Swim away from mouse click position
        if pygame.mouse.get_pressed()[0]:
            distance = (dx ** 2 + dy ** 2) ** 0.5

            # Update the velocity of the fish based on the distance
            try:
                self.velocity = ((random.random()/10 + dx / distance)/10, (random.random()/10 + dy / distance)/10)
            except:
                self.velocity = (dx * 2, dy * 2)

        # Or just swimn
        else:
            if random.random() > .9993 and self.velocity[0] < 2 and self.velocity[1] < 2:
                self.velocity = (self.velocity[0] + random.uniform(-.01, .1)/(self.x_s+100), self.velocity[1] + random.uniform(-.01, .1)/(self.x_s+100))
            
            if random.random() < 0.001 and self.velocity[0] < 2 and self.velocity[1] < 2:
                self.velocity = (self.velocity[0] - .01, self.velocity[0] - .01)
    

    def direction(self):
        # Update fish direction
        if self.velocity[0] < 0 and not self.flipped:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.flipped = 1
        
        if self.velocity[0] > 0 and self.flipped:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.flipped = 0
