"""Proof certificate numerics for lane-1320 (midpoint-retraction Dirac integrator).
Uses only numpy. Produces output/artifacts/results.json with certified numbers.

Scheme D_h (midpoint-retraction Dirac = RATTLE-mid), M=I:
  (P) q+ = q + h p - (h^2/2) F + h G0^T L,   g(q+) = 0,   G0 = Gforce(q)
  (V) p+ = (q+-q)/h - (h/2) F + G1^T M2,     G1 p+ = 0,   G1 = Gforce(q+)
Constraint rows stay g(q+)=0 with exact Jacobian G(q+) in Newton; only the
force/projection matrices G0,G1 are rescaled (G -> T G). This is exactly what
"replacing the constraint Jacobian" means; invariance follows from
range((TG)^T) = range(G^T).
"""
import numpy as np, json, math

G_GRAV = 9.81
F = np.array([0., G_GRAV, 0., G_GRAV])

def Gmat(q):
    x1, y1, x2, y2 = q
    dx, dy = x2 - x1, y2 - y1
    return np.array([[2*x1, 2*y1, 0., 0.],
                     [-2*dx, -2*dy, 2*dx, 2*dy]])

def gvec(q):
    x1, y1, x2, y2 = q
    return np.array([x1*x1 + y1*y1 - 1., (x2-x1)**2 + (y2-y1)**2 - 1.])

def lam_cont(q, p):
    G = Gmat(q)
    A = G @ G.T
    w = np.array([2*np.dot(p[:2], p[:2]), 2*np.dot(p[2:]-p[:2], p[2:]-p[:2])])
    return np.linalg.solve(A, G @ F - w)

def angles_to_state(th1, ph, w1, w2):
    q1 = np.array([math.sin(th1), -math.cos(th1)])
    d = np.array([math.sin(ph), -math.cos(ph)])
    q2 = q1 + d
    t1 = np.array([math.cos(th1), math.sin(th1)])
    t2 = np.array([math.cos(ph), math.sin(ph)])
    p1 = w1 * t1
    p2 = p1 + w2 * t2
    return np.concatenate([q1, q2]), np.concatenate([p1, p2])

def energy(q, p):
    return 0.5*np.dot(p, p) + G_GRAV*(q[1]+q[3])

def Dstep(q, p, h, Gforce=None, tol=1e-14, maxit=25):
    Gf = Gforce if Gforce is not None else Gmat
    G0 = Gf(q)
    qp = q + h*p
    Lam = np.zeros(2)
    for it in range(maxit):
        r1 = qp - q - h*p + 0.5*h*h*F - h*(G0.T @ Lam)
        r2 = gvec(qp)
        if max(np.linalg.norm(r1), np.linalg.norm(r2)) < tol:
            break
        J = np.zeros((6, 6)); J[:4, :4] = np.eye(4); J[:4, 4:] = -h*G0.T; J[4:, :4] = Gmat(qp)
        d = np.linalg.solve(J, -np.concatenate([r1, r2]))
        qp = qp + d[:4]; Lam = Lam + d[4:]
    else:
        return None
    if max(np.linalg.norm(qp-q-h*p+0.5*h*h*F-h*(G0.T@Lam)), np.linalg.norm(gvec(qp))) > 1e-11:
        return None
    v = (qp - q)/h
    G1 = Gf(qp)
    Lam2 = np.linalg.solve(G1 @ G1.T, -(G1 @ (v - 0.5*h*F)))
    return qp, v - 0.5*h*F + G1.T @ Lam2, it


import math as _m
th1 = ph = _m.pi/3; w1 = w2 = 1.5
q0, p0 = angles_to_state(th1, ph, w1, w2)
