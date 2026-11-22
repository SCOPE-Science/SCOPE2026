"""Reproduce exact support-code checks and finite numerical decoder diagnostics.

Only finite diagnostics: the all-even-order assertion is proved in RESULT.md.
Run: python3 CHECK.py
"""
from __future__ import annotations
import cmath
import math
import random


def exponents(h):
    assert h >= 2
    L = 2*h*h + 1
    R = 2*h + 1
    B = [L*j + j*j for j in range(h)]
    E = [R*v for v in B] + [R*B[j] + j+1 for j in range(h)]
    return E


def masks(h):
    E = exponents(h)
    M = max(E)+1
    w = [2**(e/M) for e in E]
    return [1+0j]*(2*h), [complex(w[j] if j<h else 0.0, 0.0 if j<h else w[j]) for j in range(2*h)], w


def intensities(x, mask):
    n = len(x)
    return [abs(sum(mask[j]*x[j]*cmath.exp(-2j*math.pi*j*k/n) for j in range(n)))**2 for k in range(n)]


def corrs(data):
    n = len(data)
    return [sum(data[k]*cmath.exp(2j*math.pi*k*d/n) for k in range(n))/n for d in range(n)]


def decode(y0, y1, h):
    n = 2*h
    _, mask1, w = masks(h)
    c0, c1 = corrs(y0), corrs(y1)
    D = c0[0].real
    if D < 1e-10:
        return [0j]*n
    nonzero = [d for d in range(1,n) if max(abs(c0[d]),abs(c1[d])) > 1e-8]
    E = exponents(h)
    M = max(E)+1
    if not nonzero:
        ratio = c1[0].real / D
        pos = min(range(n),key=lambda j: abs(ratio-w[j]**2))
        ans=[0j]*n
        ans[pos]=math.sqrt(D)
        return ans
    if nonzero == [h]:
        ratio = c1[0].real / D
        pairs = [j for j in range(h) if w[j]**2-1e-8 <= ratio <= w[j+h]**2+1e-8]
        if len(pairs)!=1:
            raise ValueError(('antipodal support',h,ratio,pairs))
        a=pairs[0]; b=a+h
        u=(c1[0].real-w[b]**2*D)/(w[a]**2-w[b]**2)
        v=D-u
        z=complex(c0[h].real/2, c1[h].real/(2*w[a]*w[b]))
        ans=[0j]*n
        ans[a]=math.sqrt(u)
        ans[b]=z.conjugate()/ans[a]
        assert abs(abs(ans[b])**2-v)<1e-6
        return ans
    d=nonzero[0]
    assert len(nonzero)==2 and nonzero==[d,n-d] or len(nonzero)==2 and nonzero==[n-d,d]
    code=(abs(c1[d])/abs(c0[d]))
    candidate=min(((a,b) for a in range(n) for b in range(a+1,n)),key=lambda pair:abs(w[pair[0]]*w[pair[1]]-code))
    a,b=candidate
    if (a-b)%n not in nonzero:
        raise ValueError(('nonantipodal support lag',h,candidate,nonzero))
    u=(c1[0].real-w[b]**2*D)/(w[a]**2-w[b]**2)
    v=D-u
    ans=[0j]*n
    ans[a]=math.sqrt(u)
    ans[b]=c0[(b-a)%n]/ans[a]
    assert abs(abs(ans[b])**2-v) < 1e-6
    return ans


def main():
    rng=random.Random(20261119)
    code_checks=0
    anti_checks=0
    for h in range(2,61):
        E=exponents(h)
        assert all(E[j]<E[j+h]<E[j+1] for j in range(h-1))
        assert E[h-1]<E[2*h-1]
        sums=[E[i]+E[j] for i in range(2*h) for j in range(i+1,2*h)]
        assert len(sums)==len(set(sums)), h
        code_checks+=len(sums)
    tests=0
    for h in (2,3,4,5,6,7,8,9):
        n=2*h
        m0,m1,w=masks(h)
        for a in range(n):
            x=[0j]*n
            x[a]=cmath.exp(1j*(0.2+a))*(1+0.13*a)
            rec=decode(intensities(x,m0),intensities(x,m1),h)
            assert max(abs(rec[j]*x[a]/rec[a]-x[j]) for j in range(n)) < 1e-6
            tests+=1
        for a in range(n):
            for b in range(a+1,n):
                for trial in range(3):
                    x=[0j]*n
                    x[a]=(0.9+0.4*rng.random())*cmath.exp(1j*2*math.pi*rng.random())
                    x[b]=(1.1+0.3*rng.random())*cmath.exp(1j*2*math.pi*rng.random())
                    rec=decode(intensities(x,m0),intensities(x,m1),h)
                    if max(abs(rec[j]*x[a]/rec[a]-x[j]) for j in range(n)) > 1e-6:
                        raise AssertionError((n,a,b,trial,x,rec))
                    tests+=1
                    if b==a+h: anti_checks+=1
    print(f'CHECK_OK exact_integer_pair_sums={code_checks} decoder_tests={tests} antipodal_tests={anti_checks}')

if __name__ == '__main__':
    main()
