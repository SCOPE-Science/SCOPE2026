"""Numerical corroboration for the three-time spectral defect theorem.
Requires Python 3, numpy and scipy. Finite sampling is not an infinite proof.
"""
import math
import cmath
import numpy as np
from scipy.optimize import minimize_scalar

PI=math.pi

def squared_trinomial(m, t):
    return abs(1+cmath.exp(1j*t)+cmath.exp(1j*m*t))**2

def trig_defect(m, t):
    return .5*squared_trinomial(m,t)

def numerical_global_minimum(m):
    grid_count=300*m
    theta=2*PI*np.arange(grid_count)/grid_count
    vals=3 + 2*(np.cos(theta)+np.cos((m-1)*theta)+np.cos(m*theta))
    k=int(np.argmin(vals))
    dtheta=2*PI/grid_count
    res=minimize_scalar(lambda t:squared_trinomial(m,t),
                        bounds=(theta[k]-2*dtheta,theta[k]+2*dtheta),
                        method='bounded',options={'xatol':1e-15})
    return max(0.,float(res.fun)),float(res.x)

def main():
    for m in range(2,52):
        for j in range(17):
            t=(j+0.375)*2*PI/17
            lhs=squared_trinomial(m,t)
            rhs=3+2*(math.cos(t)+math.cos((m-1)*t)+math.cos(m*t))
            assert abs(lhs-rhs)<3e-12, (m,t,lhs,rhs)
    for m in [2,5,8,11,101]:
        t=2*PI/3
        assert squared_trinomial(m,t)<1e-22,(m,squared_trinomial(m,t))
    for m in [3,4,6,7,9,10,12,13,21,22,30,31,60,61,120,121,300,301]:
        val,t=numerical_global_minimum(m)
        assert val>1e-11,(m,val)
        assert abs(m*m*val-PI**2/3)<25/m, (m,m*m*val,PI**2/3)
        # Symmetric atomless measures: uniform small arcs around two angles.
        n=2
        eps=1e-7/(n*m)
        def corr(k):
            return math.cos(k*t/n)*np.sinc(k*eps/PI)
        measure_total=corr(n)+corr((m-1)*n)+corr(m*n)
        point_total=val/2-1.5
        assert abs(measure_total-point_total)<1e-8,(m,measure_total,point_total)
    print('PASS: 867 algebraic samples; five resonant cases; 18 nonresonant minima and smooth spectral approximations')
    for m in [30,31,60,61,120,121,300,301]:
        val,t=numerical_global_minimum(m)
        print(f'm={m:3d} m^2 |1+z+z^m|^2={m*m*val:.9f} target={PI**2/3:.9f}')

if __name__=='__main__':
    main()
