import pybullet as p 
import pybullet_data 
import time 
import numpy as np 



class DogEnvironment:


    def __init__(self):

        #TODO Everyone

        #TODO connect to module using direct method 
        client = ??? 
        #TODO set timeout 
        p.???
        #TODO Add pybullet_data to search path 
        p.????

        #TODO Set gravity 
        p.???

        #TODO Spawn plane 
        self.planeId = p.???

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


    def get_obsevation(self):
        '''
        Returns the observation 
        '''
        #TODO Everyone
        
        return state


    def get_reward(self):
        '''
        Calculates and returns the reward that the agent maximizes
        '''
        #TODO Everyone
        return reward 



    