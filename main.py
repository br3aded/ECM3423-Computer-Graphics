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

        self.light = LightSource(self, position=[0., 30., 10.])

        #load citylayout file and create model from meshes
        citylayout = load_obj_file('models/roadlayout.obj')
        self.citylayout = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0,-10,-20]),scaleMatrix([1,1,1])), mesh=mesh, shader=PhongShader()) for mesh in citylayout]

        #buildings
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
        
        #correct place
        largebuilding3_2 = load_obj_file('models/largebuilding3.obj')
        self.largebuilding3_2 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([19.5,-1.5,-16]),scaleMatrix([0.1,0.1,0.1])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding3_2]
        self.buildings += self.largebuilding3_2

        #cars
        self.cars = []

        #correct place
        car1_1 = load_obj_file('models/car1.obj')
        self.car1_1 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([3,-1.3,-5]),scaleMatrix([0.002,0.002,0.002])), mesh=mesh, shader=PhongShader()) for mesh in car1_1]
        self.cars += self.car1_1

        #correct place
        car1_2 = load_obj_file('models/car1.obj')
        self.car1_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([-4,-1.3,3.3]),rotationMatrixY(np.radians(90))),scaleMatrix([0.002,0.002,0.002])), mesh=mesh, shader=PhongShader()) for mesh in car1_2]
        self.cars += self.car1_2

        #correct place
        car2_1 = load_obj_file('models/car2.obj')
        self.car2_1 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([10,-1.1,3.3]),rotationMatrixY(np.radians(270))),scaleMatrix([0.16,0.16,0.16])), mesh=mesh, shader=PhongShader()) for mesh in car2_1]
        self.cars += self.car2_1

        #correct place
        car2_2 = load_obj_file('models/car2.obj')
        self.car2_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(np.matmul(translationMatrix([4.8,-1.1,-3]),rotationMatrixY(np.radians(230))),rotationMatrixX(np.radians(180))),scaleMatrix([0.16,0.16,0.16])), mesh=mesh, shader=PhongShader()) for mesh in car2_2]
        self.cars += self.car2_2

        #correct place
        tank_1 = load_obj_file('models/tank.obj')
        self.tank_1 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([3.8,-1.2,6]),rotationMatrixY(np.radians(270))),scaleMatrix([0.006,0.006,0.006])), mesh=mesh, shader=PhongShader()) for mesh in tank_1]
        self.cars += self.tank_1

        #correct place
        tank_2 = load_obj_file('models/tank.obj')
        self.tank_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([1,-1.2,4.5]),rotationMatrixY(np.radians(220))),scaleMatrix([0.006,0.006,0.006])), mesh=mesh, shader=PhongShader()) for mesh in tank_2]
        self.cars += self.tank_2

        #correct place
        tank_3 = load_obj_file('models/tank.obj')
        self.tank_3 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([5.5,-1.2,-10]),rotationMatrixY(np.radians(40))),scaleMatrix([0.006,0.006,0.006])), mesh=mesh, shader=PhongShader()) for mesh in tank_3]
        self.cars += self.tank_3

        """
        dinosaur_frames = []
        for i in range(1,51):
            dinosaur_frame = load_obj_file('models/animateddinosaur{}.obj'.format(i))
            dinosaur_frames.append([DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([4,-1.3,2]),rotationMatrixY(np.radians(-45))),scaleMatrix([0.8,0.8,0.8])), mesh=mesh, shader=PhongShader()) for mesh in dinosaur_frame])
        self.dinosaur_frames = dinosaur_frames
        self.current_frame = 0
        """

    def update_dinosaur_animation(self):
        self.current_frame = (self.current_frame + 1) % len(self.dinosaur_frames)


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

        for model in self.cars:
            model.draw()


        #for model in self.dinosaur_frames[self.current_frame]:
            #model.draw()

            
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
