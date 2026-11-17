"""Independent finite numerical cross-checks of a graph-wide analytic phase result.
Run with Python 3 and NumPy. This script checks examples, not universal proof.
"""
import math
import numpy as np

PI = math.pi
T1 = math.acos(1.0 / math.sqrt(3.0))
T3 = PI - T1

def q(t):
    return 0.8 * math.sin(t) * (1.0 + math.cos(t)**2)

def dq(t):
    c = math.cos(t)
    return 0.8 * c * (3.0*c*c - 1.0)

def K(t):
    return 2.0*t / q(t)

def graph(nu, nv, edges):
    w = np.zeros((nu+nv,nu+nv))
    for i,j,a in edges:
        assert a>0
        w[i,nu+j] = w[nu+j,i] = a
    du = w[:nu,:].sum(axis=1)
    dv = w[nu:,:].sum(axis=1)
    assert max(du)-min(du)<1e-12 and max(dv)-min(dv)<1e-12
    r,s = float(du[0]),float(dv[0])
    assert np.max(np.abs(w.sum(axis=1) - np.r_[np.repeat(r,nu),np.repeat(s,nv)]))<1e-12
    lap = np.diag(w.sum(axis=1))-w
    eigen = np.linalg.eigvalsh(lap)
    assert abs(eigen[-1]-(r+s))<1e-11
    assert abs(eigen[0])<1e-11 and eigen[1]>1e-9
    return w,lap,eigen,r,s

cases = [
    graph(1,1,[(0,0,1.0)]),
    graph(2,3,[(i,j,1.0) for i in range(2) for j in range(3)]),
    graph(2,2,[(0,0,1.0),(0,1,2.0),(1,0,2.0),(1,1,1.0)]),
    graph(3,3,[(i,i,1.0) for i in range(3)]+[(i,(i+1)%3,1.0) for i in range(3)])
]
assert 1.25<K(T1)<K(PI/2)<K(T3)
for x in np.linspace(.0001, PI-.0001, 5000):
    assert q(x)-x*dq(x)>-1e-11

checked = 0
for w,lap,eigen,r,s in cases:
    nu = int(np.sum(np.isclose(w.sum(axis=1),r))) if abs(r-s)>1e-8 else w.shape[0]//2
    if abs(r-s)>1e-8: # r entries form first bipartite class
        nu = int(np.sum(np.isclose(w.sum(axis=1),r)))
    # With equal degrees all examples have equal shore sizes.
    nv = len(w)-nu
    assert nu*r == nv*s
    lam = r+s
    for t in [.2,.7, 1.1, 1.4, 1.8, 2.05, 2.3, 2.6]:
        h = K(t)/lam
        delta = PI+t
        state = np.r_[np.repeat((r/lam)*delta,nu),np.repeat(-(s/lam)*delta,nv)]
        new = state.copy()
        for i in range(len(w)):
            for j in range(len(w)):
                if w[i,j]:
                    dif = state[i]-state[j]
                    new[i] += h*w[i,j]*(math.sin(dif)+0.2*math.sin(3*dif))
        expected_delta=PI-t
        expected = np.r_[np.repeat((r/lam)*expected_delta,nu),np.repeat(-(s/lam)*expected_delta,nv)]
        assert np.max(np.abs(new-expected)) < 2e-12
        J = np.eye(len(w))
        for i in range(len(w)):
            for j in range(len(w)):
                if w[i,j]:
                    dif=state[i]-state[j]
                    c=math.cos(dif)+0.6*math.cos(3*dif)
                    J[i,i] += h*w[i,j]*c
                    J[i,j] -= h*w[i,j]*c
        assert np.max(np.abs(J-(np.eye(len(w))-h*dq(t)*lap))) < 2e-11
        multipliers = np.linalg.eigvalsh(J)
        assert max(abs(multipliers - np.sort(1-h*dq(t)*eigen)))<2e-11
        stable = (0<t<T1) or (PI/2<t<T3)
        nonneutral = 1-h*dq(t)*eigen[1:]
        if stable:
            assert max(abs(nonneutral)) < 1
        else:
            assert min(nonneutral)>1
        checked += 1
print('VERIFY_OK', 'graphs',len(cases),'amplitudes_per_graph',8,'checked',checked)
print('scaled_thresholds',*[f'{x:.12f}' for x in [1.25,K(T1),K(PI/2),K(T3)]])
