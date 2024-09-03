import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
  
class Draw:
    def draw_figure(self, pyramid_height) -> None:
        self.__draw_pyramid(pyramid_height)
            
    def __draw_pyramid(self, height):
        fig = plt.figure(figsize=(7, 7))
        ax_3D = fig.add_subplot(111, projection='3d')

        base_size = 1
        vertices = np.array([
            [0, 0, 0],
            [base_size, 0, 0],
            [base_size, base_size, 0],
            [0, base_size, 0],
            [base_size / 2, base_size / 2, height]
        ])

        faces = [
            [vertices[0], vertices[1], vertices[4]],  # Грань 1
            [vertices[1], vertices[2], vertices[4]],  # Грань 2
            [vertices[2], vertices[3], vertices[4]],  # Грань 3
            [vertices[3], vertices[0], vertices[4]],  # Грань 4
            [vertices[0], vertices[1], vertices[2], vertices[3]]  # Основание
        ]

        ax_3D.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

        ax_3D.set_xlim([0, base_size])
        ax_3D.set_ylim([0, base_size])
        ax_3D.set_zlim([0, height])

        plt.show()