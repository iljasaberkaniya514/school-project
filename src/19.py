import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_3d_spheres():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_values = [i for i in range(-10, 11)]
    y_values = [-i**2 + i**2 - 10 for i in x_values]
    z_values = [0.5 * (x**2 + y**2) for x in x_values]  
    ax.plot_surface(x_values, y_values, z_values, cmap='viridis')
    plt.show()

if __name__ == "__main__":
    visualize_3d_spheres()
