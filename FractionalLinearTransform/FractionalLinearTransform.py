from numpy import *
import matplotlib.pyplot as plt
from os import listdir, getcwd, remove
import imageio
import multiprocessing
from re import sub
from collections import deque

def FractionalLinearTransform(a,b,c,d,z):
    return (a*z+b)/(c*z+d)

def MakePlot(func):
    Xrange = linspace(-5,5,50)
    Yrange = linspace(-5,5,50)
    Domain = [[x +y*1j for x in Xrange] for y in Yrange]
    Image = [exp(z) for z in Domain]
    
    cm = plt.cm.get_cmap('RdYlBu')
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.title.set_text('Domain')
    ax1.set_xlim([-5, 5])
    ax1.set_ylim([-5, 5])
    ax2.set_xlim([-5, 5])
    ax2.set_ylim([-5, 5])
    ax2.title.set_text('Range')
    for ii,x in enumerate(Domain):
        ax1.scatter(Domain.real,Domain.imag,c=cm(ii/len(X)))
        ax2.scatter(Image[ii].real, Image[ii].imag,c=cm(ii/len(X)))

    plt.savefig("expz.png")
    return 

def ChooseyTravsChooseGIF(n):
    images = []
    pngs = [file for file in listdir(getcwd()) if '.png' in file]
    pngs.sort(key=lambda f: int(sub('\D', '', f)))
    for file in pngs:
        if '.png' in file:
            #Take all of the png's generated above and form a GIF
            images.append(imageio.imread(file))
            remove(file)
    imageio.mimsave('exp(z).gif', images, format='GIF', duration=10/n, fps=60)
    return


def main():
    if __name__ == "__main__":
        points = 300
        MakePlot(points)
        
        return

main()

