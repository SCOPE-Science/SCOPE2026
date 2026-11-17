#!/usr/bin/env python3
"""Supplementary numerical diagnostics for the two-dimensional commutator envelope."""
import math
import numpy as np

EPS = 1e-11
I = np.eye(2)
P = np.diag([1.0, 0.0])
Q = np.array([[0.25, math.sqrt(3)/4], [math.sqrt(3)/4, 0.75]])
A = I - (2/3)*P
B = I - (2/3)*Q
C = A+B-I
assert abs(np.linalg.norm(A, 2)-1) < EPS
assert abs(np.linalg.norm(B, 2)-1) < EPS
assert np.linalg.eigvalsh(C).min() > -EPS
assert abs(np.linalg.det(C)) < EPS
assert abs(np.linalg.norm(A @ B - B @ A, 2)-1/(3*math.sqrt(3))) < EPS
checks = 5
for lam in np.linspace(0.04,0.96,24):
    for mu in np.linspace(0.03,0.97,23):
        u, v = 1-lam, 1-mu
        ratio = lam*mu/(u*v)
        optw = min(ratio, 0.5)
        q = np.array([[optw, math.sqrt(optw*(1-optw))],
                      [math.sqrt(optw*(1-optw)), 1-optw]])
        x = I-u*P
        y = I-v*q
        assert np.linalg.eigvalsh(x+y-I).min() > -2e-10
        measured = np.linalg.norm(x@y-y@x, 2)
        branch = math.sqrt(lam*mu*(1-lam-mu)) if ratio < .5 else u*v/2
        assert abs(measured-branch) < 1e-10
        assert measured < 1/(3*math.sqrt(3)) + 1e-10
        checks += 3
        for z in np.linspace(0.001, min(math.sqrt(ratio),.999), 9):
            w = z*z
            qq = np.array([[w, z*math.sqrt(1-w)],
                           [z*math.sqrt(1-w), 1-w]])
            yy = I-v*qq
            assert np.linalg.eigvalsh(x+yy-I).min() > -2e-9
            cm = np.linalg.norm(x@yy-yy@x, 2)
            assert abs(cm-u*v*z*math.sqrt(1-z*z)) < 1e-10
            assert cm < branch+1e-10
            checks += 3
print('MOMENT_COMPLETION_COMMUTATOR_DIAGNOSTICS_OK',checks)
