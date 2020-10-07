from OpenGL import GL as gl
import pygame
from esper import Processor


class PrepareFrameSystem(Processor):
    def process(self):
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glClearColor(1.0, 0, 1.0, 0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)


class FinishFrameSystem(Processor):
    def process(self):
        pygame.display.flip()