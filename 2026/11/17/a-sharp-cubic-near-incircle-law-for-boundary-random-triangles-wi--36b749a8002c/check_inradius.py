"""Independent numerical checks for the near-maximal inradius law.

Run with Python 3 and NumPy: python check_inradius.py
Numerical checks are diagnostics, not substitutes for the proof.
"""
import numpy as np


def inradius(a, b, c):
    a, b, c = (np.asarray(x, dtype=float) for x in (a, b, c))
    return (np.sqrt(np.maximum(0, (a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))) /
            (a+b+c))


def calc_inradius(vertices):
    x, y, z = [vertices[..., k, :] for k in range(3)]
    a = np.linalg.norm(y-z, axis=-1)
    b = np.linalg.norm(x-z, axis=-1)
    c = np.linalg.norm(x-y, axis=-1)
    area2 = abs((y[..., 0]-x[..., 0])*(z[..., 1]-x[..., 1])-
                (y[..., 1]-x[..., 1])*(z[..., 0]-x[..., 0]))
    return area2/(a+b+c)


def coeff(vertices):
    vv = np.array(vertices, dtype=float)
    a, b, c = np.linalg.norm(vv[1]-vv[2]), np.linalg.norm(vv[0]-vv[2]), np.linalg.norm(vv[0]-vv[1])
    s = (a+b+c)/2
    P = 2*s
    r = calc_inradius(vv)
    rate = np.zeros((3,2))
    for i in range(3):
        for h,j in enumerate([(i+1)%3, (i+2)%3]):
            k = 3-i-j
            dij = np.linalg.norm(vv[i]-vv[j]); dik = np.linalg.norm(vv[i]-vv[k])
            rate[i,h] = r*(s-dij)/(dij*dik)
            delta = 1e-7
            moved = vv.copy()
            moved[i] += delta*(vv[j]-vv[i])/dij
            finite_diff = (r-calc_inradius(moved))/delta
            assert abs(finite_diff-rate[i,h]) < 2e-7
    K = np.prod(np.sum(1/rate,axis=1))/P**3
    G = ((a*b*c)**3)/(P**3*(s-a)**2*(s-b)**2*(s-c)**2)
    assert abs(K*r**3/G - 1) < 1e-10
    assert G >= 64/27-1e-10
    return float(r), float(P), rate, float(K), float(G)


def check_case(vv, seed):
    r,P,rate,K,G = coeff(vv)
    rng=np.random.default_rng(seed)
    rel=0.018
    d=r*rel
    lim=1.5*d/np.min(rate)
    total=0; trials=0
    per=40000
    for mask in range(8):
        offset=rng.random((per,3))*lim
        sample=np.tile(np.array(vv,dtype=float),(per,1,1))
        for k in range(3):
            j=(k+1)%3 if ((mask>>k)&1)==0 else (k+2)%3
            vec=vv[j]-vv[k]
            sample[:,k,:] += offset[:,k,None]*vec/np.linalg.norm(vec)
        assert np.all(offset < np.min([np.linalg.norm(vv[j]-vv[i]) for i in range(3) for j in range(3) if i!=j]))
        total += np.count_nonzero(calc_inradius(sample)>r-d)
        trials+=per
    estimate=6*8*(total/trials)*lim**3/P**3
    ratio=estimate/(K*d**3)
    assert 0.92 < ratio < 1.05, (G,ratio)
    print('shape_coeff', format(G,'.10f'), 'asymptotic_probability_ratio',format(ratio,'.6f'))


def main():
    eq=np.array([[0.,0.],[1.,0.],[.5,np.sqrt(3)/2]])
    sc=np.array([[0.,0.],[2.3,0.],[.6,1.5]])
    right=np.array([[0.,0.],[3.,0.],[0.,4.]])
    for idx,tri in enumerate((eq,sc,right)):
        check_case(tri,20261110+idx)
    rng=np.random.default_rng(431)
    for _ in range(5000):
        x,y,z=rng.uniform(.05,3,3)
        s=x+y+z
        a=y+z;b=x+z;c=x+y
        G=(a*b*c)**3/(8*s**3*(x*y*z)**2)
        assert G >= 64/27-1e-10
    assert abs(coeff(eq)[4]-64/27)<1e-10
    print('INRADIUS_CORNER_CUBIC_DIAGNOSTICS_OK')

if __name__=='__main__':
    main()
