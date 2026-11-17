"""Independent halfplane-intersection audit of tangent-polygon area identity."""
import numpy as np
from scipy.spatial import HalfspaceIntersection,ConvexHull

rng=np.random.default_rng(515)
for n in (3,4,5,8):
    for _ in range(15):
        gaps=rng.dirichlet(np.ones(n))
        if np.max(gaps)>=0.5:
            continue
        angles=2*np.pi*np.r_[0,np.cumsum(gaps[:-1])]
        normals=np.column_stack((np.cos(angles),np.sin(angles)))
        halfspaces=np.column_stack((normals,-np.ones(n)))
        polygon=HalfspaceIntersection(halfspaces,np.zeros(2)).intersections
        area=ConvexHull(polygon).volume
        formula=np.sum(np.tan(np.pi*gaps))
        assert abs(area-formula)<2e-8*max(1,formula), (n,gaps,area,formula)
print('GEOMETRIC_POLYGON_AREA_INDEPENDENT_OK')
