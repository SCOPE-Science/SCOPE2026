"""Independent polynomial-exact quadrature and finite-difference smoke checks.

Run after verify.py: python crosscheck.py. Requires NumPy >=1.23.
Finite differences are diagnostic checks, not the infinite-dimensional proof.
"""
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

base = np.array([(1,0), (0,1), (-1,1), (-1,0), (0,-1), (1,-1)], dtype=float)
nodes, weights = leggauss(5)
nodes=(nodes+1.0)/2.0
weights=weights/2.0
bary=[]
quad_weights=[]
for i, a in enumerate(nodes):
    for j, b in enumerate(nodes):
        bary.append([a, (1-a)*b])
        quad_weights.append(weights[i]*weights[j]*(1-a))
bary=np.array(bary)
quad_weights=np.array(quad_weights)

def energy_and_area(vertices):
    points=[]
    weights=[]
    for i in range(6):
        a,b=vertices[i],vertices[(i+1)%6]
        det=a[0]*b[1]-a[1]*b[0]
        points.extend(bary[:,0,None]*a+bary[:,1,None]*b)
        weights.extend(quad_weights*det)
    points=np.array(points)
    weights=np.array(weights)
    delta=points[:,None,:]-points[None,:,:]
    d2=delta[:,:,0]**2+delta[:,:,0]*delta[:,:,1]+delta[:,:,1]**2
    return np.sum(weights[:,None]*weights[None,:]*d2**3),sum(weights)

E,A=energy_and_area(base)
assert abs(A-3)<1e-12
assert abs(E-5157/280)<1e-11
certificate=json.loads(Path('HESSIAN.json').read_text())
H=np.asarray(certificate['hessian_integer_numerators'],float)/certificate['hessian_denominator']
eigens=np.linalg.eigvalsh(H)
assert max(abs(eigens[:4]))<1e-12
assert eigens[4]>0.13
rng=np.random.default_rng(54321)
for _ in range(12):
    perturbation=rng.normal(size=(6,2))
    perturbation/=np.linalg.norm(perturbation)
    expected=perturbation.reshape(-1)@H@perturbation.reshape(-1)
    step=0.0015
    EP,AP=energy_and_area(base+step*perturbation)
    EM,AM=energy_and_area(base-step*perturbation)
    observed=(np.log(EP/AP**5)+np.log(EM/AM**5)-2*np.log(E/A**5))/step**2
    assert abs(observed-expected)<1e-5, (observed, expected)
print('PASS: independent 5-by-5 Gaussian product quadrature, base energy,')
print('      12 directional second differences and positive spectrum.')
