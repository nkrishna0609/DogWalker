import pybullet as p 
import pybullet_data 
import time 
import numpy as np 



class DogEnvironment:

    

    def __init__(self):

        #TODO Everyone

        #TODO connect to module using direct method 
        client = p.connect(p.DIRECT)
        #TODO set timeout 
        p.setTimeOut(1)
        #TODO Add pybullet_data to search path 
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        #TODO Set gravity 
        p.setGravity(0,0,-10)

        #TODO Spawn plane 
        self.planeId = p.loadURDF("plane.udrf")

        '''
        Not sure if this was the place to do it but I spawned the agent as well
        couldn't find a dog.udrf file so i spawned a r2d2 instead
        '''
        cubeStartPos = [0,0,1]
        cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
        boxId = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)


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
        #TODO Everyone
        state = p.getBasePositionAndOrientation(this.boxId)
        return state


    def get_reward(self):
        '''
        Calculates and returns the reward that the agent maximizes
        '''
        #TODO Everyone
        return reward 



    