'''program to calculate Radio Active Exposure
'''
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    radioactiveexposure = 0
    while start<stop:    
        radioactiveexposure= radioactiveexposure+(f(start)*step)
        start=start+step
    return radioactiveexposure