import pybullet as p 
import pybullet_data
import time 
import numpy as np 



class DogEnvironment:


    def __init__(self):

        client = p.connect(p.DIRECT)

        p.setTimeOut(2)
        p.setGravity(0,0,-9.81)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        planeID = p.loadURDF("plane.urdf")

        pass


    def reset(self, initial_state):
        '''
        Reset world state to given initial state
        '''
        #TODO Zarar
        
        return initial_obs




    def step(self, action):
        #TODONT
        return next_obs, reward, done, debug


    def get_observation(self):
        '''
        Returns the observation 
        '''
        #dog in this case is the loaded model. The "state" can be the dog's position and orientation. We can also get velocities, if they are important for the state.
        # state = p.getBasePositionAndOrientation(self.dog)
        
        return state


    def get_reward(self):
        '''
        Calculates and returns the reward that the agent maximizes
        '''
        #Not to sure on what the end goal of this dog is, so don't know what to maximize.
        return reward 



    