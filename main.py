import pygame

import numpy as np
from scipy.spatial.transform import Rotation

# import the scene class
from scene import Scene

from lightSource import LightSource

from blender import load_obj_file

from BaseModel import DrawModelFromMesh

from shaders import *


class JurrasicScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.light = LightSource(self, position=[5., 10., 5.])

        #load citylayout file and create model from meshes
        citylayout = load_obj_file('models/roadlayout.obj')
        self.citylayout = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0,-10,-20]),scaleMatrix([1,1,1])), mesh=mesh, shader=PhongShader()) for mesh in citylayout]

        self.buildings = []

        #correct place
        building1_1 = load_obj_file('models/building1.obj')
        self.building1_1 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0.5,-1.25,0.5]),scaleMatrix([20,20,20])), mesh=mesh, shader=PhongShader()) for mesh in building1_1]
        self.buildings += self.building1_1

        #correct place
        building1_2 = load_obj_file('models/building1.obj')
        self.building1_2 = [DrawModelFromMesh(scene=self,M=np.matmul(np.matmul(translationMatrix([15, -1.25, -15.5]), rotationMatrixY(np.radians(270))),scaleMatrix([20, 20, 20])),mesh=mesh,shader=PhongShader()) for mesh in building1_2]
        self.buildings += self.building1_2

        #correct place
        building2_1 = load_obj_file('models/building2.obj')
        self.building2_1 = [DrawModelFromMesh(scene=self,  M=np.matmul(translationMatrix([1, -1.2, -4.5]), scaleMatrix([0.05, 0.05, 0.05])), mesh=mesh, shader=PhongShader()) for mesh in building2_1]
        self.buildings += self.building2_1

        #correct place
        building2_2 = load_obj_file('models/building2.obj')
        self.building2_2 = [DrawModelFromMesh(scene=self,  M=np.matmul(np.matmul(translationMatrix([19, -1.2, 10]),rotationMatrixY(np.radians(180))), scaleMatrix([0.05, 0.05, 0.05])), mesh=mesh, shader=PhongShader()) for mesh in building2_2]
        self.buildings += self.building2_2

        #correct place
        buildings1_1 = load_obj_file('models/buildings.obj')
        self.buildings1_1 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([4,0.7,-15]),rotationMatrixY(np.radians(90))),scaleMatrix([0.05,0.05,0.05])), mesh=mesh, shader=PhongShader()) for mesh in buildings1_1]
        self.buildings += self.buildings1_1

        #correct place
        buildings1_2 = load_obj_file('models/buildings.obj')
        self.buildings1_2 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([7,0.7,10.5]),scaleMatrix([0.05,0.05,0.05])), mesh=mesh, shader=PhongShader()) for mesh in buildings1_2]
        self.buildings += self.buildings1_2

        #correct place
        firestation_1 = load_obj_file('models/firestation.obj')
        self.firestation_1 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([-3.5,0.7,-0.5]),rotationMatrixY(np.radians(270))),scaleMatrix([0.025,0.025,0.025])), mesh=mesh, shader=PhongShader()) for mesh in firestation_1]
        self.buildings += self.firestation_1

        #correct place
        firestation_2 = load_obj_file('models/firestation.obj')
        self.firestation_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([20.5,0.7,12.5]),rotationMatrixY(np.radians(270))),scaleMatrix([0.025,0.025,0.025])), mesh=mesh, shader=PhongShader()) for mesh in firestation_2]
        self.buildings += self.firestation_2

        #correct place
        largebuilding1_1 = load_obj_file('models/largebuilding.obj')
        self.largebuilding1_1 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([10,-1.5,-1]),scaleMatrix([0.065,0.065,0.065])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding1_1]
        self.buildings += self.largebuilding1_1

        #correct place
        largebuilding1_2 = load_obj_file('models/largebuilding.obj')
        self.largebuilding1_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([-13,-1.5,8]),rotationMatrixY(np.radians(90))),scaleMatrix([0.065,0.065,0.065])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding1_2]
        self.buildings += self.largebuilding1_2

        #correct place
        largebuilding2_1 = load_obj_file('models/largebuilding2.obj')
        self.largebuilding2_1 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0.5,-1.5,-5.5]),scaleMatrix([0.08,0.08,0.08])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding2_1]
        self.buildings += self.largebuilding2_1

        #correct place
        largebuilding2_2 = load_obj_file('models/largebuilding2.obj')
        self.largebuilding2_2 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([7,-1.5,17]),scaleMatrix([0.08,0.08,0.08])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding2_2]
        self.buildings += self.largebuilding2_2
        
        #correct place
        largebuilding3_1 = load_obj_file('models/largebuilding3.obj')
        self.largebuilding3_1 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0.2,-1.5,7.7]),scaleMatrix([0.1,0.1,0.1])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding3_1]
        self.buildings += self.largebuilding3_1#
        
        largebuilding3_2 = load_obj_file('models/largebuilding3.obj')
        self.largebuilding3_2 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0.2,-1.5,7.7]),scaleMatrix([0.1,0.1,0.1])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding3_2]
        self.buildings += self.largebuilding3_2

    def draw(self):
        '''
        Draw all models in the scene
        :return: None
        '''

        # first we need to clear the scene, we also clear the depth buffer to handle occlusions
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.camera.update()
       

        for model in self.citylayout:
            model.draw()

        for model in self.buildings:
            model.draw()

        # once we are done drawing, we display the scene
        # Note that here we use double buffering to avoid artefacts:
        # we draw on a different buffer than the one we display,
        # and flip the two buffers once we are done drawing.
        pygame.display.flip()


if __name__ == '__main__':
    # initialises the scene object
    # scene = Scene(shaders='gouraud')
    scene = JurrasicScene()

    # starts drawing the scene
    scene.run()
