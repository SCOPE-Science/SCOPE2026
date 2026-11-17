"""Numerical tests for the boundary-endpoint polygon fragmentation law.

Only independent corroboration; mathematical assertions are proved in RESULT.md.
Requires Python >=3.9 and numpy.
"""
import math
import numpy as np


def poly_area(v):
    v = np.asarray(v, dtype=float)
    return abs(float(np.dot(v[:, 0], np.roll(v[:, 1], -1)) -
                     np.dot(v[:, 1], np.roll(v[:, 0], -1)))) / 2


def geometry(vertices):
    v = np.asarray(vertices, dtype=float)
    assert len(v) >= 3 and poly_area(v) > 0
    edges = np.roll(v, -1, axis=0) - v
    lengths = np.linalg.norm(edges, axis=1)
    per = float(lengths.sum())
    area = poly_area(v)
    angles = []
    for i in range(len(v)):
        a = v[(i - 1) % len(v)] - v[i]
        b = v[(i + 1) % len(v)] - v[i]
        cs = float(np.linalg.det(np.array([a, b])))
        co = float(np.dot(a,b))
        alpha = math.atan2(abs(cs),co)
        assert 0 < alpha < math.pi
        angles.append(alpha)
    return v, lengths, per, area, np.array(angles)


def predicted_small_prob(vertices, s):
    v, lengths, per, area, angles = geometry(vertices)
    assert s > 0
    out = 0.0
    for i, alpha in enumerate(angles):
        a, b = lengths[i-1], lengths[i]
        t = 2*s/math.sin(alpha)
        assert t < a*b
        out += 4*s / (per**2*math.sin(alpha)) * (1+math.log(a*b/t))
    return out


def sample_boundary(v, lengths, rng):
    r = float(rng.uniform(0, lengths.sum()))
    i = int(np.searchsorted(np.cumsum(lengths),r))
    prev = lengths[:i].sum()
    t = (r-prev)/lengths[i]
    return i, v[i]+t*(v[(i+1)%len(v)]-v[i])


def smaller_piece(v, i, p, j, q, total):
    if i==j: return 0.0
    n = len(v)
    # Follow the oriented boundary from p through the next vertices to q.
    chain=[p]
    a=(i+1)%n
    while a != (j+1)%n:
        chain.append(v[a])
        a=(a+1)%n
    chain.append(q)
    z = poly_area(chain)
    return min(z,total-z)


def simulate(vertices, s, trials, seed):
    v, lengths, p, area, angles = geometry(vertices)
    rng = np.random.default_rng(seed)
    count=0; atom=0
    for _ in range(trials):
        i,x=sample_boundary(v,lengths,rng)
        j,y=sample_boundary(v,lengths,rng)
        if i==j:
            atom+=1
            continue
        cut=smaller_piece(v,i,x,j,y,area)
        if 0 < cut < s:
            count+=1
    return count/trials, atom/trials


def main():
    sq=np.array([[0,0],[1,0],[1,1],[0,1]])
    tri=np.array([[0,0],[2,0],[0.6,1.5]])
    skew=np.array([[0,0],[2.3,0],[3.2,1.1],[0.3,1.3]])
    for vert,frac,seed in ((sq,0.006,101),(tri,0.006,102),(skew,0.006,103)):
        v,ls,P,A,alpha=geometry(vert)
        s=frac*A
        p=predicted_small_prob(v,s)
        empirical,atom=simulate(v,s,110000,seed)
        p0=float(np.sum(ls**2)/P**2)
        assert abs(empirical-p)<0.003, (p,empirical)
        assert abs(atom-p0)<0.005,(atom,p0)
        if len(v)==3:
            z=s/A
            q=1-p0
            exact=q*(z*(1-math.log(z))+z+(1-z)*math.log(1-z))
            assert abs(exact-p) < 1.1*q*z*z
            assert abs(empirical-exact)<0.003
        print('polygon',len(v),'epsilon',frac,'predicted',round(p,7),
              'observed',round(empirical,7),'zero_atom',round(atom,7),
              'predicted_atom',round(p0,7))
    # Exact exponential factorization: the conditional density in z is
    # (T-log z)/(T+1), while its log-gap-share mark is Uniform(0,1).
    for T in (2.,5.,10.):
        zz=np.linspace(0.00001,1,200000)
        f=(T-np.log(zz))/(T+1)
        mass=np.trapezoid(f,zz)
        assert abs(mass-1)<0.0001
        tv=np.trapezoid(np.abs(f-1),zz)/2
        assert abs(tv-1/(math.e*(T+1)))<0.00003, (tv,T)
    # Strong convexity of cosecant: f''(alpha)>=1; near the square,
    # the stability constant 2 for K=4 sum csc alpha is sharp.
    for delta in (0.1,0.01,0.001):
        a=np.array([math.pi/2+delta,math.pi/2-delta]*2)
        K=4*np.sum(1/np.sin(a)); mn=16.
        assert K-mn >=2*float(np.sum((a-math.pi/2)**2))-1e-10
        assert abs((K-mn)/np.sum((a-math.pi/2)**2)-2)<0.1
    print('BOUNDARY_FRAGMENT_CHECKS_OK')

if __name__=='__main__':
    main()
