#!/usr/bin/env python3
"""Independent finite diagnostics for four-disk square network formula.
Not a substitute for the analytic global-convexity proof.
"""
from itertools import combinations
from math import sqrt
import numpy as np
from scipy.optimize import minimize


def theorem(a, r):
    if r >= sqrt(2)*a:
        return 0.0
    if r <= 2*a/sqrt(3):
        return 2*a*(1+sqrt(3))-4*r
    return 2*a-2*sqrt(r*r-a*a)


def topology_cost(w, corners, parts, radius):
    u = w[:2]
    v = w[2:]
    d = float(np.linalg.norm(u-v))
    for j in parts[0]:
        d += max(0.,float(np.linalg.norm(u-corners[j]))-radius)
    for j in parts[1]:
        d += max(0.,float(np.linalg.norm(v-corners[j]))-radius)
    return d


def check(a,r):
    corners = np.asarray([(-a,-a),(-a,a),(a,-a),(a,a)], dtype=float)
    pairings = [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
    values = []
    for parts in pairings:
        starts=[np.zeros(4),np.asarray([-a*.45,0,a*.45,0]),
                np.asarray([0,-a*.45,0,a*.45]),
                np.concatenate((corners[parts[0][0]],corners[parts[1][0]]))]
        opts=[minimize(topology_cost,z,args=(corners,parts,r),method='Powell',
                       options={'maxiter':4000,'ftol':1e-12,'xtol':1e-11}) for z in starts]
        values.append(min(o.fun for o in opts))
    goal=theorem(a,r)
    assert abs(min(values)-goal)<5e-7,(a,r,values,goal)
    if r<sqrt(2)*a-1e-7:
        assert abs(values[0]-goal)<5e-7 or abs(values[1]-goal)<5e-7,(a,r,values)
        # diagonal pair is the third topology, strictly worse below point-collapse.
        assert values[2]>goal+1e-7,(a,r,values,goal)
    return values


def main():
    num=0
    for a in (1.,2.,0.7):
        for ratio in (0.,0.05,0.6,1.,2/sqrt(3)-.003,2/sqrt(3),
                      2/sqrt(3)+.003,1.23,1.35,sqrt(2)-.003,sqrt(2),1.5):
            check(a,a*ratio)
            num+=1
    # All branches join with equal values and derivatives at the nonzero threshold.
    a=1.; r=2/sqrt(3)
    assert abs(2*(1+sqrt(3))-4*r-(2-2*sqrt(r*r-1)))<1e-12
    assert abs(-4-(-2*r/sqrt(r*r-1)))<1e-12
    print(f'PASS: {num} independently optimized 3-topology numerical samples, with exact-transition diagnostics')

if __name__=='__main__':
    main()
