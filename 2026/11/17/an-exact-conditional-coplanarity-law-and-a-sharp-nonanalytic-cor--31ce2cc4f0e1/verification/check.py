"""Independent numeric checks for the conditioned small-volume sphere-tetrahedron law.

Requires numpy and scipy; all pseudorandom generators use explicit fixed seeds.
Run: python verification/check.py
"""
import math
import numpy as np
from scipy.special import gamma

PI = math.pi
T_AVG = 3 / (2 * PI)
C = PI * math.sqrt(6) * gamma(.25) / gamma(.75)**3
rng = np.random.default_rng(271828)

def circle_area(a):
    u = np.stack([np.cos(a), np.sin(a)], axis=-1)
    p = u[:, 1] - u[:, 0]
    q = u[:, 2] - u[:, 0]
    return np.abs(p[:, 0]*q[:, 1]-p[:, 1]*q[:, 0])/2

def sphere_tetra_trials(N, thresholds):
    """Directly sample four independent points from normalized sphere area."""
    hit = np.zeros(len(thresholds), dtype=np.int64)
    h2_sum = np.zeros(len(thresholds))
    h_count = np.zeros(len(thresholds), dtype=np.int64)
    h2_all = 0.
    done = 0
    while done < N:
        k = min(200000, N-done)
        p = rng.normal(size=(k,4,3))
        p /= np.linalg.norm(p,axis=2)[:,:,None]
        e = p[:,1]-p[:,0]
        f = p[:,2]-p[:,0]
        cross = np.cross(e,f)
        twice_a = np.linalg.norm(cross,axis=1)
        n = cross / twice_a[:,None]
        h = np.einsum('ij,ij->i',n,p[:,0])
        vol = np.abs(np.einsum('ij,ij->i',cross,p[:,3]-p[:,0])) / 6
        h2_all += np.sum(h*h)
        for j,t in enumerate(thresholds):
            sel = vol<t
            hit[j] += np.sum(sel)
            h2_sum[j] += np.sum(h[sel]**2)
            h_count[j] += np.sum(sel)
        done += k
    return hit/N, h2_sum / h_count, h2_all/N

def product_trial(N, thresholds):
    """Exact change-of-variables rejection sampler with uniform proposal."""
    accept = np.zeros(len(thresholds), dtype=np.int64)
    done = 0
    while done < N:
        k = min(200000,N-done)
        angle = rng.uniform(0,2*PI,(k,3))
        area = circle_area(angle)
        h = rng.uniform(-1,1,k)
        z = rng.uniform(-1,1,k)
        for j,t in enumerate(thresholds):
            accept[j] += np.count_nonzero(np.abs(h+3*t*z/((1-h*h)*area))<=1)
        done += k
    return accept/N

def main():
    ts = [0.001,0.0025,0.005]
    direct,h2,h2_base = sphere_tetra_trials(2_500_000,ts)
    proposal=product_trial(1_500_000,ts)
    for t,p,h,q in zip(ts,direct,h2,proposal):
        exact_rep=3*PI*t*q
        linear=3*PI*t
        two=linear-C*t**1.5
        # Sampling uncertainty in direct frequency is < 0.00022 here.
        assert abs(p-exact_rep)<0.00048,(t,p,exact_rep)
        assert 0<exact_rep<linear
        assert abs((linear-exact_rep)/t**1.5-C)<6.2,(t,linear,exact_rep,C)
        assert 0.15<h<0.37
        print('t',t,'direct',round(p,7),'representation',round(exact_rep,7),
              'two-term',round(two,7),'conditional H^2',round(h,6))
    assert abs(h2_base-1/5)<.003
    # Independent sample of circle triples checks both Dyson moments.
    angles=rng.uniform(0,2*PI,(2_000_000,3))
    tri=circle_area(angles)
    assert abs(np.mean(tri)-T_AVG)<.0012
    assert abs(np.mean(tri**(-.5)) - 2*gamma(.25)/gamma(.75)**3)<.15
    print('three-plane H^2',round(h2_base,7),'circle area',round(np.mean(tri),7))
    # A separate classical moment formula gives a consistency check on two
    # Mellin residues; finite differences here verify normalizations only.
    from scipy.special import gamma as G
    def moment(k):
        return (6**(-k)*G(3+2*k)/G(3+1.5*k)
                *(G(1.5)/G(1.5+.5*k))**3
                *G((k+1)/2)*G((k+2)/2)/math.sqrt(PI))
    eps=1e-6
    assert abs(eps*moment(-1+eps)-3*PI)<.001
    assert abs(eps*moment(-1.5+eps)+1.5*C)<.01
    print('asymptotic C',round(C,12))
    print('SPHERE_TETRA_COPLANAR_CONDITIONAL_LAW_OK')

if __name__=='__main__':
    main()
