import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [colour for colour, amount in kwargs.items() for _ in range(amount)]

    def draw(self, balls_to_draw):
        if balls_to_draw > len(self.contents):
            return self.contents
        
        drawn_balls = []
        for _ in range(balls_to_draw):
            random_choice = random.randint(0, len(self.contents) - 1)
            removed_ball = self.contents.pop(random_choice)
            drawn_balls.append(removed_ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        this_draw = hat_copy.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if this_draw.count(key) < value:
                success = False
                break
        if success:
            successful_experiments += 1
    return successful_experiments/num_experiments