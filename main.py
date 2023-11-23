import pygame

import numpy as np

# import the scene class
from scene import Scene

from lightSource import LightSource

from blender import load_obj_file

from BaseModel import DrawModelFromMesh , BaseModel

from shaders import *

from environmentMapping import *


class JurrasicScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        #location where all the model files are located and Meshes created 

        #place light source in the scene
        self.light = LightSource(self, position=[4., 20., -4.])

        #load the model from the obj file
        citylayout = load_obj_file('models/roadlayout.obj')
        #create a mesh from the pobj file with phong shader applied, Matrix M allows us to move model within the scene using functions from matutils.py
        self.citylayout = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0,-10,-20]),scaleMatrix([1,1,1])), mesh=mesh, shader=PhongShader()) for mesh in citylayout]

        #create a list of all building models so we can draw the entire list into scene instead of individual models.
        self.buildings = []

        building1_1 = load_obj_file('models/building1.obj')
        self.building1_1 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0.5,-1.25,0.5]),scaleMatrix([20,20,20])), mesh=mesh, shader=PhongShader()) for mesh in building1_1]
        #add building model to list of buildings
        self.buildings += self.building1_1

        building2_1 = load_obj_file('models/building2.obj')
        self.building2_1 = [DrawModelFromMesh(scene=self,  M=np.matmul(translationMatrix([1, -1.2, -4.5]), scaleMatrix([0.05, 0.05, 0.05])), mesh=mesh, shader=PhongShader()) for mesh in building2_1]
        self.buildings += self.building2_1

        building2_2 = load_obj_file('models/building2.obj')
        self.building2_2 = [DrawModelFromMesh(scene=self,  M=np.matmul(np.matmul(translationMatrix([19, -1.2, 10]),rotationMatrixY(np.radians(180))), scaleMatrix([0.05, 0.05, 0.05])), mesh=mesh, shader=PhongShader()) for mesh in building2_2]
        self.buildings += self.building2_2

        buildings1_1 = load_obj_file('models/buildings.obj')
        self.buildings1_1 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([4,0.7,-15]),rotationMatrixY(np.radians(90))),scaleMatrix([0.05,0.05,0.05])), mesh=mesh, shader=PhongShader()) for mesh in buildings1_1]
        self.buildings += self.buildings1_1

        buildings1_2 = load_obj_file('models/buildings.obj')
        self.buildings1_2 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([7,0.7,10.5]),scaleMatrix([0.05,0.05,0.05])), mesh=mesh, shader=PhongShader()) for mesh in buildings1_2]
        self.buildings += self.buildings1_2

        firestation= load_obj_file('models/firestation.obj')
        self.firestation = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([-3.5,0.7,-0.5]),rotationMatrixY(np.radians(270))),scaleMatrix([0.025,0.025,0.025])), mesh=mesh, shader=PhongShader()) for mesh in firestation]
        self.buildings += self.firestation

        largebuilding1_1 = load_obj_file('models/largebuilding.obj')
        self.largebuilding1_1 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([10,-1.5,-1]),scaleMatrix([0.065,0.065,0.065])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding1_1]
        self.buildings += self.largebuilding1_1

        largebuilding1_2 = load_obj_file('models/largebuilding.obj')
        self.largebuilding1_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([-13,-1.5,6]),rotationMatrixY(np.radians(90))),scaleMatrix([0.065,0.065,0.065])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding1_2]
        self.buildings += self.largebuilding1_2

        largebuilding2_1 = load_obj_file('models/largebuilding2.obj')
        self.largebuilding2_1 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0.5,-1.5,-5.5]),scaleMatrix([0.08,0.08,0.08])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding2_1]
        self.buildings += self.largebuilding2_1

        largebuilding2_2 = load_obj_file('models/largebuilding2.obj')
        self.largebuilding2_2 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([7,-1.5,17]),scaleMatrix([0.08,0.08,0.08])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding2_2]
        self.buildings += self.largebuilding2_2
    
        largebuilding3_1 = load_obj_file('models/largebuilding3.obj')
        self.largebuilding3_1 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0.2,-1.5,7.7]),scaleMatrix([0.1,0.1,0.1])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding3_1]
        self.buildings += self.largebuilding3_1
        
        largebuilding3_2 = load_obj_file('models/largebuilding3.obj')
        self.largebuilding3_2 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([19.5,-1.5,-16]),scaleMatrix([0.1,0.1,0.1])), mesh=mesh, shader=PhongShader()) for mesh in largebuilding3_2]
        self.buildings += self.largebuilding3_2

        building4_1 = load_obj_file('models/building4.obj')
        self.building4_1 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([1.2,-1,12]),scaleMatrix([0.17,0.17,0.17])), mesh=mesh, shader=PhongShader()) for mesh in building4_1]
        self.buildings += self.building4_1

        building4_2 = load_obj_file('models/building4.obj')
        self.building4_2 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([21,-1,1.7]),scaleMatrix([0.17,0.17,0.17])), mesh=mesh, shader=PhongShader()) for mesh in building4_2]
        self.buildings += self.building4_2

        largebuilding4_1 = load_obj_file('models/largebuilding4.obj')
        self.largebuilding4_1 = [DrawModelFromMesh(scene=self,M=np.matmul(translationMatrix([-4,-1,-25]),scaleMatrix([30,30,30])),mesh=mesh,shader=PhongShader())for mesh in largebuilding4_1]
        self.buildings += self.largebuilding4_1

        largebuilding4_2 = load_obj_file('models/largebuilding4.obj')
        self.largebuilding4_2 = [DrawModelFromMesh(scene=self,M=np.matmul(translationMatrix([10,-1,-11.5]),scaleMatrix([30,30,30])),mesh=mesh,shader=PhongShader())for mesh in largebuilding4_2]
        self.buildings += self.largebuilding4_2

        hospital = load_obj_file('models/hospital.obj')
        self.hospital = [DrawModelFromMesh(scene=self,M=np.matmul(np.matmul(translationMatrix([-12,-1.3,-1]),rotationMatrixY(np.radians(90))),scaleMatrix([2,2,2])),mesh=mesh,shader=PhongShader())for mesh in hospital]
        self.buildings += self.hospital

        #create a list of car models
        self.cars = []

        car1_1 = load_obj_file('models/car1.obj')
        self.car1_1 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([3,-1.3,-5]),scaleMatrix([0.002,0.002,0.002])), mesh=mesh, shader=PhongShader()) for mesh in car1_1]
        self.cars += self.car1_1

        car1_2 = load_obj_file('models/car1.obj')
        self.car1_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([-4,-1.3,3.3]),rotationMatrixY(np.radians(90))),scaleMatrix([0.002,0.002,0.002])), mesh=mesh, shader=PhongShader()) for mesh in car1_2]
        self.cars += self.car1_2

        car2_1 = load_obj_file('models/car2.obj')
        self.car2_1 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([10,-1.1,3.3]),rotationMatrixY(np.radians(270))),scaleMatrix([0.16,0.16,0.16])), mesh=mesh, shader=PhongShader()) for mesh in car2_1]
        self.cars += self.car2_1

        car2_2 = load_obj_file('models/car2.obj')
        self.car2_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(np.matmul(translationMatrix([4.8,-1.1,-3]),rotationMatrixY(np.radians(230))),rotationMatrixX(np.radians(180))),scaleMatrix([0.16,0.16,0.16])), mesh=mesh, shader=PhongShader()) for mesh in car2_2]
        self.cars += self.car2_2

        tank_1 = load_obj_file('models/tank.obj')
        self.tank_1 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([3.8,-1.2,6]),rotationMatrixY(np.radians(270))),scaleMatrix([0.006,0.006,0.006])), mesh=mesh, shader=PhongShader()) for mesh in tank_1]
        self.cars += self.tank_1

        tank_2 = load_obj_file('models/tank.obj')
        self.tank_2 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([1,-1.2,4.5]),rotationMatrixY(np.radians(220))),scaleMatrix([0.006,0.006,0.006])), mesh=mesh, shader=PhongShader()) for mesh in tank_2]
        self.cars += self.tank_2

        tank_3 = load_obj_file('models/tank.obj')
        self.tank_3 = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([5.5,-1.2,-10]),rotationMatrixY(np.radians(40))),scaleMatrix([0.006,0.006,0.006])), mesh=mesh, shader=PhongShader()) for mesh in tank_3]
        self.cars += self.tank_3

        #create a list of street light models
        self.streetlights = []
        
        streetlight_1 = load_obj_file('models/streetlight.obj')
        self.streetlight_1 = [DrawModelFromMesh(scene=self,M=np.matmul(np.matmul(translationMatrix([2,-1.2,2]),rotationMatrixY(np.radians(90))),scaleMatrix([0.4,0.4,0.4])),mesh=mesh , shader=PhongShader()) for mesh in streetlight_1]
        self.streetlights += self.streetlight_1

        streetlight_2 = load_obj_file('models/streetlight.obj')
        self.streetlight_2 = [DrawModelFromMesh(scene=self,M=np.matmul(np.matmul(translationMatrix([2,-1.2,-2]),rotationMatrixY(np.radians(90))),scaleMatrix([0.4,0.4,0.4])),mesh=mesh , shader=PhongShader()) for mesh in streetlight_2]
        self.streetlights += self.streetlight_2

        streetlight_3 = load_obj_file('models/streetlight.obj')
        self.streetlight_3 = [DrawModelFromMesh(scene=self,M=np.matmul(np.matmul(translationMatrix([2,-1.2,-6]),rotationMatrixY(np.radians(90))),scaleMatrix([0.4,0.4,0.4])),mesh=mesh , shader=PhongShader()) for mesh in streetlight_3]
        self.streetlights += self.streetlight_3

        streetlight_4 = load_obj_file('models/streetlight.obj')
        self.streetlight_4 = [DrawModelFromMesh(scene=self,M=np.matmul(np.matmul(translationMatrix([5.7,-1.2,-6]),rotationMatrixY(np.radians(270))),scaleMatrix([0.4,0.4,0.4])),mesh=mesh , shader=PhongShader()) for mesh in streetlight_4]
        self.streetlights += self.streetlight_4

        streetlight_5 = load_obj_file('models/streetlight.obj')
        self.streetlight_5 = [DrawModelFromMesh(scene=self,M=np.matmul(np.matmul(translationMatrix([5.7,-1.2,-2]),rotationMatrixY(np.radians(270))),scaleMatrix([0.4,0.4,0.4])),mesh=mesh , shader=PhongShader()) for mesh in streetlight_5]
        self.streetlights += self.streetlight_5

        streetlight_6 = load_obj_file('models/streetlight.obj')
        self.streetlight_6 = [DrawModelFromMesh(scene=self,M=np.matmul(np.matmul(translationMatrix([5.7,-1.2,2]),rotationMatrixY(np.radians(270))),scaleMatrix([0.4,0.4,0.4])),mesh=mesh , shader=PhongShader()) for mesh in streetlight_6]
        self.streetlights += self.streetlight_6

        #create a list of dinosaur models
        self.dinosaurs = []

        dinosaur = load_obj_file('models/dinosaur.obj')
        self.dinosaur =  [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([2,-1.2,-10]),rotationMatrixY(np.radians(45))),scaleMatrix([0.25,0.25,0.25])), mesh=mesh, shader=PhongShader()) for mesh in dinosaur]
        self.dinosaurs += self.dinosaur
        
        dinosaur2_1 = load_obj_file('models/dinosaur2.obj')
        self.dinosaur2_1 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([3,4,-5]),scaleMatrix([0.3,0.3,0.3])), mesh=mesh, shader=PhongShader()) for mesh in dinosaur2_1]
        self.dinosaurs += self.dinosaur2_1

        dinosaur2_2 = load_obj_file('models/dinosaur2.obj')
        self.dinosaur2_2 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([4,4,-3]),scaleMatrix([0.3,0.3,0.3])), mesh=mesh, shader=PhongShader()) for mesh in dinosaur2_2]
        self.dinosaurs += self.dinosaur2_2

        dinosaur2_3 = load_obj_file('models/dinosaur2.obj')
        self.dinosaur2_3 =  [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([5,4,-6]),scaleMatrix([0.3,0.3,0.3])), mesh=mesh, shader=PhongShader()) for mesh in dinosaur2_3]
        self.dinosaurs += self.dinosaur2_3


        #model for enviroment map
        """
        #use the EnviromentMappingTexture function to create a texture of the enviroment
        self.enviroment = EnvironmentMappingTexture(width=200,height=200)
        #load model to map the enivroment onto 
        statue = load_obj_file('models/Statue.obj')
        #create mesh for model but shader uses enviroment instead of phong
        self.statue = [DrawModelFromMesh(scene = self, M=np.matmul(translationMatrix([7,-1,1.5]),scaleMatrix([0.4,0.4,0.4])),mesh=mesh,shader=EnvironmentShader(map=self.enviroment))for mesh in statue]
        """

        #load skybox model and create mesh
        skybox = load_obj_file('models/skybox.obj')
        self.skybox = [DrawModelFromMesh(scene = self,M=np.matmul(translationMatrix([0,10,0]),scaleMatrix([0.15,0.15,0.15])),mesh=mesh ,shader=PhongShader()) for mesh in skybox]

        
        #code for stand in for animated dinosaur to decrease load time for demonstration
        dinosaur_standin = load_obj_file('models/animateddinosaur1.obj')
        self.dinosaur_standin = [DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([4,-1.3,2]),rotationMatrixY(np.radians(-45))),scaleMatrix([0.8,0.8,0.8])), mesh=mesh, shader=PhongShader()) for mesh in dinosaur_standin]
        

        """
        #functionality for animated dinosaur
        #create a list of all the individual frames of the animation
        dinosaur_frames = []
        #loop through all the models for each frame and create mesh
        for i in range(1,51):
            dinosaur_frame = load_obj_file('models/animateddinosaur{}.obj'.format(i))
            dinosaur_frames.append([DrawModelFromMesh(scene=self, M=np.matmul(np.matmul(translationMatrix([4,-1.3,2]),rotationMatrixY(np.radians(-45))),scaleMatrix([0.8,0.8,0.8])), mesh=mesh, shader=PhongShader()) for mesh in dinosaur_frame])
        self.dinosaur_frames = dinosaur_frames
        #sets the first frame
        self.current_frame = 0
        """

    #function used to increase the value of the frame by 1 and loops back to 0 once final frame reached
    def update_dinosaur_animation(self):
        self.current_frame = (self.current_frame + 1) % len(self.dinosaur_frames)

    #used to all reflections of models in the enviroment map texture
    def draw_reflections(self):
        for model in self.citylayout:
            model.draw()

        for model in self.largebuilding1_1:
            model.draw()

        for model in self.building1_1:
            model.draw()
    
        for model in self.cars:
            model.draw()

    #function used to draw models into the scene
    def draw(self, framebuffer=False):
        '''
        Draw all models in the scene
        :return: None
        '''

        # first we need to clear the scene, we also clear the depth buffer to handle occlusions
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.camera.update()
       
       #loop through lists of models and draw into scene
        for model in self.citylayout:
            model.draw()

        for model in self.buildings:
            model.draw()

        for model in self.cars:
            model.draw()

        for model in self.skybox:
            model.draw()

        for model in self.dinosaurs:
            model.draw()

        for model in self.streetlights:
            model.draw()

        #renders enviroment mapped model in the scene
        """
        if not framebuffer:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.enviroment.update(self)

            for model in self.statue:
                model.draw()
            glDisable(GL_BLEND)
        """

        #stand in code for dinosaur
        for model in self.dinosaur_standin:
            model.draw()

        #loads the correct frame of the animation in the scene
        #for model in self.dinosaur_frames[self.current_frame]:
            #model.draw()

            
        # once we are done drawing, we display the scene
        # Note that here we use double buffering to avoid artefacts:
        # we draw on a different buffer than the one we display,
        # and flip the two buffers once we are done drawing.
        pygame.display.flip()


if __name__ == '__main__':
    # initialises the scene object
    scene = JurrasicScene()

    # starts drawing the scene
    scene.run()
