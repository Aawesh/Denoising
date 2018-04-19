from scipy import interpolate
import matplotlib.pyplot as plt

def f(x):
    x_points = [ 0, 1, 2, 3, 4, 5]
    y_points = [12,14,22,39,58,77]

    plt.plot(x_points,y_points,'ro')

    tck = interpolate.splrep(x_points, y_points)

    new_x = range(100)
    print new_x
    new_y = interpolate.splev(new_x,tck,der=0)

    plt.plot(new_x, new_y, 'bo')
    plt.show()

    return interpolate.splev(x, tck)

print f(1.25)