from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2

class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        self.env = self.generated_task['env']
        # getting the initial picture
        img, _, _, _ = self.env.step([0,0])
        
        condition = True
        opposite_lane = False
        
        while condition:
            img, reward, done, info = self.env.step([1, 0])
            self.env.render()
            
            duck_ahead = img.sum(axis=(0, 1))[1] > 29000000
            
            if duck_ahead and not opposite_lane:
                self.move_left()
                opposite_lane = True
                
            if not duck_ahead and opposite_lane:
                self.move_right()
                opposite_lane = False
                
                for _ in range(20):
                    img, reward, done, info = self.env.step([1, 0])
                    self.env.render()
                
                condition = False
                
                
    def move_left(self):
        for _ in range(20):
            img, reward, done, info = self.env.step([0, 1])
            self.env.render()
            
        for _ in range(8):
            img, reward, done, info = self.env.step([1, 0])
            self.env.render()
            
        for _ in range(20):
            img, reward, done, info = self.env.step([0, -1])
            self.env.render()
            
        for _ in range(8):
            img, reward, done, info = self.env.step([1, 0])
            self.env.render()
            
            
    def move_right(self):
        for _ in range(20):
            img, reward, done, info = self.env.step([0, -1])
            self.env.render()
            
        for _ in range(8):
            img, reward, done, info = self.env.step([1, 0])
            self.env.render()
            
        for _ in range(20):
            img, reward, done, info = self.env.step([0, 1])
            self.env.render()
            
        for _ in range(8):
            img, reward, done, info = self.env.step([1, 0])
            self.env.render()
        
        
