#!/usr/bin/env python3
"""Symbolic consistency checks for a four-site generalized Laplacian theorem.

Requirements: Python 3, sympy, numpy. The analytic proof is in RESULT.md.
"""
import math
import random
import sympy as sp
import numpy as np

s, w1, w2, w3, a = sp.symbols('s w1 w2 w3 a', positive=True)
t = s**2 - 1
M = sp.diag(1, t, t, 1)

def laplacian(weights):
    L = sp.zeros(4)
    for i, w in enumerate(weights):
        L[i, i] += w
        L[i + 1, i + 1] += w
        L[i, i + 1] -= w
        L[i + 1, i] -= w
    return L

L = laplacian((w1, w2, w3))
p = sp.Matrix([s + 1, 1, -1, -s - 1])
q = sp.Matrix([s - 1, -1, 1, 1 - s])
e = sp.Matrix([t, -1, -1, t])
ones = sp.ones(4, 1)

def check_scalar(x, y=0):
    assert sp.factor(x-y) == 0, (x, y)

def check_vector(x):
    for z in x:
        check_scalar(z)

check_scalar((ones.T * M * p)[0])
check_scalar((ones.T * M * q)[0])
check_scalar((ones.T * M * e)[0])
energy = s**2 * (w1+w3) + 4*w2
check_scalar((p.T * L * p)[0], energy)
check_scalar((q.T * L * q)[0], energy)
check_scalar((p.T * M * p)[0], 4*s*(s+1))
check_scalar((q.T * M * q)[0], 4*s*(s-1))
Lopt = laplacian((a, a*s**2/2, a))
check_vector(Lopt * p - a*s/(s+1) * M*p)
check_vector(Lopt * q - a*s/(s-1) * M*q)
check_vector(Lopt * e - a*s**2/(s**2-1) * M*e)
check_vector(Lopt * ones)

rng = random.Random(3729)
checks = 0
for mass in (sp.Rational(1, 3), sp.Rational(1, 2), sp.Integer(1), sp.Integer(2), sp.Integer(10)):
    sm = math.sqrt(float(mass+1))
    optimal = (sm + 1)/(sm - 1)
    for k in range(30):
        weights = [math.exp(rng.uniform(-4, 4)) for _ in range(3)]
        numeric = np.zeros((4, 4))
        for i, w in enumerate(weights):
            numeric[i, i] += w
            numeric[i+1, i+1] += w
            numeric[i, i+1] -= w
            numeric[i+1, i] -= w
        d = np.diag([1,1/math.sqrt(float(mass)),1/math.sqrt(float(mass)),1])
        z = np.linalg.eigvalsh(d @ numeric @ d)
        assert z[1] > 0 and z[-1]/z[1] >= optimal*(1-1e-10)
        checks += 1
    weights = [1, (float(mass) + 1)/2, 1]
    numeric = np.zeros((4,4))
    for i, w in enumerate(weights):
        numeric[i,i]+=w;numeric[i+1,i+1]+=w
        numeric[i,i+1]-=w;numeric[i+1,i]-=w
    d=np.diag([1,1/math.sqrt(float(mass)),1/math.sqrt(float(mass)),1])
    z=np.linalg.eigvalsh(d @ numeric @ d)
    assert abs(z[-1]/z[1]-optimal) < 1e-8
    checks += 1
print(f"PASS: exact symbolic identities and {checks} deterministic numerical checks")
