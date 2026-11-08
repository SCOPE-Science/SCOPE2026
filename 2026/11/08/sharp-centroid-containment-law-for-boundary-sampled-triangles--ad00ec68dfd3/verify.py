"""Reproduce exact conditional integrals and independently sample triangle boundaries.
Requires Python 3, sympy and numpy. Random checks supplement, not replace, proof.
"""
import math
import sympy as sp
import numpy as np

x = sp.symbols('x', real=True)
c21 = sp.integrate(2*x*(2*x-1)/(3*x-1)**2, (x, sp.Rational(1, 2), 1))
f = (1-x)/(2-3*x)
g = (1-2*x)/(2-3*x)
h = x/(3*x-1)
i_f = sp.integrate(f, (x, 0, sp.Rational(1, 2)))
i_g = sp.integrate(g, (x, 0, sp.Rational(1, 2)))
i_h = sp.integrate(h, (x, sp.Rational(1, 2), 1))
c111 = sp.simplify(i_f+i_h-i_g)
assert sp.simplify(c21-sp.Rational(1, 9)-4*sp.log(2)/27) == 0
assert sp.simplify(c111-2*sp.log(2)/3) == 0
assert sp.simplify(c111 - (6*sp.log(2)/9)) == 0
assert sp.simplify(3*c21/3 + (6*c111-9*c21)/27 - (sp.Rational(2,27)+20*sp.log(2)/81))==0
assert sp.simplify(3*c21/4 - (sp.Rational(1,12)+sp.log(2)/9))==0

def formula(weights):
    e2 = sum(weights[i]*weights[j] for i in range(3) for j in range(i+1,3))
    e3 = float(np.prod(weights))
    return (1/3 + 4*math.log(2)/9)*e2 + (8*math.log(2)/3-1)*e3

rng = np.random.default_rng(22162012)

def simulate(vertices, weights, trials):
    vertices = np.asarray(vertices, float)
    centroid = vertices.mean(axis=0)
    chosen_edges = rng.choice(3, size=(trials,3), p=weights)
    t = rng.random((trials,3))
    q = ((1-t)[...,None]*vertices[chosen_edges]
         + t[...,None]*vertices[(chosen_edges+1)%3])-centroid
    def cross(a,b):
        return a[...,0]*b[...,1]-a[...,1]*b[...,0]
    orientation = cross(q[:,1]-q[:,0],q[:,2]-q[:,0])
    edge_tests = [cross(q[:,0],q[:,1]),cross(q[:,1],q[:,2]),cross(q[:,2],q[:,0])]
    return np.mean(np.logical_and.reduce([orientation*e>0 for e in edge_tests]))

cases = [((0.,0.),(1.,0.),(0.5,0.866025403784)),
         ((0.,0.),(1.,0.),(0.5,0.2)),
         ((0.,0.),(1.,0.),(0.01,0.01)),
         ((0.,0.),(1.,0.),(-0.2,0.6)),
         ((0.,0.),(1.,0.),(2.,0.1))]
for vertices in cases:
    v=np.asarray(vertices)
    sides=np.linalg.norm(np.roll(v,-1,axis=0)-v,axis=1)
    weights=sides/sum(sides)
    target=formula(weights)
    measured=simulate(vertices,weights,140_000)
    se=math.sqrt(target*(1-target)/140_000)
    assert abs(measured-target) < 5*se, (vertices, measured, target, se)
for weights in ([1/3]*3,[0.8,0.1,0.1],[0.15,0.3,0.55]):
    target=formula(weights)
    measured=simulate(cases[1],weights,140_000)
    se=math.sqrt(target*(1-target)/140_000)
    assert abs(measured-target)<5*se,(weights,measured,target,se)

print('VERIFY_OK conditional_integrals=4 equilateral_and_degenerate_limits=2 independent_samples=1120000')
