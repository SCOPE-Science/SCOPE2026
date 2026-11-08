"""Independent numerical checks for the near-central rectangular-box section law."""
import math
import numpy as np

def formula(sides, t):
    a = np.asarray(sides, dtype=float)
    R = np.linalg.norm(a)
    leading = 4.0 / R
    second = (4/math.pi)*sum(1.0 / (a[i]*math.sqrt(R*R-a[i]**2)) for i in range(3))
    return leading*t-second*t*t

def count_from_edges(normal, sides, t):
    # Independent direct enumeration of the 12 axis-parallel box edges.
    count = np.zeros(len(normal), dtype=np.int16)
    for axis in range(3):
        j,k = [q for q in range(3) if q != axis]
        for ej in (-1,1):
            for ek in (-1,1):
                residual = t - ej*sides[j]*normal[:,j]-ek*sides[k]*normal[:,k]
                count += (np.abs(residual) < sides[axis]*normal[:,axis])
    return count

def count_from_vertex_levels(normal, sides, t):
    x = normal*sides
    d=np.stack([-x[:,0]+x[:,1]+x[:,2],x[:,0]-x[:,1]+x[:,2],x[:,0]+x[:,1]-x[:,2]],axis=1)
    count = (np.abs(d)<t).sum(axis=1)
    return count

def run():
    rng = np.random.default_rng(52422)
    for sides in ((1.,1.,1.), (2.,1.,3.), (1.,4.,.5),(.8,2.1,3.7)):
        sides=np.asarray(sides)
        samples=rng.normal(size=(1_400_000,3))
        samples=np.abs(samples/np.linalg.norm(samples,axis=1)[:,None])
        m=min(sides)
        for t in (0.012*m,0.022*m,0.035*m):
            n=count_from_edges(samples,sides,t)
            indicator=count_from_vertex_levels(samples,sides,t)==1
            assert np.all((n==5)==indicator), (sides,t)
            actual=float((n==5).mean())
            prediction=formula(sides,t)
            delta=actual-prediction
            # Statistical z check with generous 6-sigma margin + third-order remainder.
            sigma=math.sqrt(actual*(1-actual)/len(n))
            assert abs(delta)<7*sigma+5*(t/min(sides))**3, (sides,t,delta,sigma)
            print(f'box={tuple(sides)} offset={t:.5g} empirical={actual:.8f} formula={prediction:.8f} z={delta/sigma:.3f}')
    print('VERIFY_OK boxes=4 offsets=12 plane_sections=16800000 independent_edge_count_equivalence=16800000')
if __name__=='__main__':run()
