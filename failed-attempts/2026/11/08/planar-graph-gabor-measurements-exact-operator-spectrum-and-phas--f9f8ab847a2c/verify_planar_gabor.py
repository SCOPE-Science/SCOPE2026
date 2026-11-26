"""Finite checks for the planar-graph Gabor ambiguity and phase fibres.

Run with Python 3 and NumPy. Uses f(x)=x^2 on prime fields.
"""
import numpy as np


def setup(p):
    points = [(x, y) for x in range(p) for y in range(p)]
    z = {point: i for i, point in enumerate(points)}
    g = np.array([int(y == x*x % p) for x, y in points], dtype=float)
    characters = np.array([[np.exp(2j*np.pi*(r*x+s*y)/p)
                            for x, y in points]
                           for r, s in points])
    return points, z, g, characters


def ambiguity(p, pts, loc, g, chars):
    out = []
    for a, b in pts:
        shifted = np.array([g[loc[((x+a)%p, (y+b)%p)]]
                            for x, y in pts])
        out.append(chars.conj() @ (g*shifted))
    return np.array(out)


def intensities(p, pts, loc, g, chars, signal):
    measurements = []
    for a, b in pts:
        shifted = np.array([g[loc[((x-a)%p, (y-b)%p)]]
                            for x, y in pts])
        measurements.extend(np.abs(chars @ (np.conj(signal)*shifted))**2)
    return np.array(measurements)


def check(p):
    pts, loc, g, chars = setup(p)
    amb = ambiguity(p, pts, loc, g, chars)
    spectrum = []
    for i, (a,b) in enumerate(pts):
        for j, (r,s) in enumerate(pts):
            magnitude = abs(amb[i, j])
            expected = 1.0 if a else (0.0 if b else (
                p if r==0 and s==0 else (0.0 if s==0 else p**0.5)))
            if not np.isclose(magnitude, expected, atol=2e-9):
                raise AssertionError((p,(a,b),(r,s),magnitude,expected))
            spectrum.append(expected)
    assert sum(v != 0 for v in spectrum) == p**4-p**3+p**2-p+1
    if p==3:
        N=p*p
        matrix=[]
        for a,b in pts:
            shifted=np.array([g[loc[((x-a)%p,(y-b)%p)]] for x,y in pts]);
            for c in chars:
                v=c*shifted
                matrix.append(np.kron(v,np.conj(v)))
        svals=np.linalg.svd(np.asarray(matrix),compute_uv=False)
        predicted=np.array([p*p] + [p**1.5]*(p*(p-1)) +
                           [p]*(p**3*(p-1)) +
                           [0]*((p-1)*(p*p+1)))
        assert np.allclose(np.sort(svals),np.sort(predicted),atol=1e-8)
    # Exact ambiguity examples for the same measurement operator.
    a=np.zeros(p*p,dtype=complex); b=a.copy()
    for y in range(p):
        a[loc[(0,y)]]=2*np.exp(2j*np.pi*y/p)
        a[loc[(1,y)]]=5*np.exp(4j*np.pi*y/p)
        b[loc[(0,y)]]=5*np.exp(2j*np.pi*y/p)
        b[loc[(1,y)]]=2*np.exp(4j*np.pi*y/p)
    assert np.allclose(intensities(p,pts,loc,g,chars,a),
                       intensities(p,pts,loc,g,chars,b),atol=1e-7)
    assert not np.allclose(a,b*b[loc[(0,0)]]/a[loc[(0,0)]])
    c=np.zeros(p*p,dtype=complex); d=c.copy()
    for y in range(p):
        c[loc[(0,y)]]=np.exp(2j*np.pi*y/p)
        d[loc[(0,y)]]=np.exp(4j*np.pi*y/p)
    assert np.allclose(intensities(p,pts,loc,g,chars,c),
                       intensities(p,pts,loc,g,chars,d),atol=1e-7)
    print(f'field_size={p}; rank={sum(v != 0 for v in spectrum)}; '
          f'nullity={(p-1)*(p*p+1)}; ambiguity_and_phase_examples_pass')


if __name__=='__main__':
    for p in (3,5,7):
        check(p)
    print('PLANAR_GABOR_SPECTRUM_AND_PHASE_CHECKS_OK')
