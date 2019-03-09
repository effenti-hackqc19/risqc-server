from matplotlib import pylab as plt 
from shapely.geometry import Polygon, Point

poly = [[25.774252, -80.190262], [18.466465, -66.118292], [32.321384, -64.75737], [25.774252, -80.190262]] 
x = [point[0] for point in poly] 
y = [point[1] for point in poly] 
p1 = [26.254629577800088, -72.728515625] 
plt.plot(x,y,p1[0],p1[1],'*r') 
plt.show()


poly = Polygon([[25.774252, -80.190262], [18.466465, -66.118292], [32.321384, -64.75737], [25.774252, -80.190262]] )
point = Point([26.254629577800088, -72.728515625] )

poly.distance(point)