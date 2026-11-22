"""Independent finite examples for the parabolic Fourier-erasure expansion.
Only Python's standard library is required. Finite checks do not certify limits.
"""
import cmath
import math


def prime_field(p):
    elements = tuple(range(p))
    add = lambda a, b: (a+b)%p
    mul = lambda a, b: (a*b)%p
    psi = lambda a: cmath.exp(2j*math.pi*a/p)
    return elements, add, mul, psi


def field9():
    # F_9 = F_3[i]/(i^2+1). Primitive trace is 2*real coordinate.
    elements = tuple((a,b) for a in range(3) for b in range(3))
    add = lambda x,y: ((x[0]+y[0])%3,(x[1]+y[1])%3)
    mul = lambda x,y: ((x[0]*y[0]-x[1]*y[1])%3,
                       (x[0]*y[1]+x[1]*y[0])%3)
    psi = lambda x: cmath.exp(2j*math.pi*((2*x[0])%3)/3)
    return elements, add, mul, psi


def run(field, selected):
    el, add, mul, psi = field
    q = len(el); B = tuple(selected); h = len(B)
    assert 1 <= h < q and len(set(B)) == h
    G = {}; E = {}
    for a in el:
        for b in el:
            ga = 0j; er = 0j
            for t in el:
                phase = psi(add(mul(a,t),mul(b,mul(t,t))))
                ga += phase
                if t in B:
                    er += phase
            G[a,b] = ga; E[a,b] = er
    zero = el[0]
    count = q*q
    L = sum(abs(G[k]-E[k]) for k in G)/count
    Lfull = 1/q+(1-1/q)*q**0.5
    D0 = sum(abs(E[a,zero]) for a in el if a !=zero)-h
    approx = Lfull-3*h/(4*q**0.5)+D0/q**2
    # Two exact Gauss-correlation identities used in the proof.
    u = [E[a,b]*G[a,b].conjugate()/q**0.5
         for a in el for b in el if b != zero]
    s1 = sum(v.real for v in u)
    s2 = sum(abs(v)**2-v.real**2 for v in u)
    expected1 = h*q*(q-1)/q**0.5
    expected2 = h*q*(q-h)/2
    assert abs(s1-expected1)<1e-7*(1+abs(expected1)),(q,B,s1,expected1)
    assert abs(s2-expected2)<1e-7*(1+abs(expected2)),(q,B,s2,expected2)
    return q,h,round(L,11),round(approx,11),round((L-approx)*q**1.5,6)


def main():
    results=[]
    for p in (5,7,11,13,17,19,23,31,43):
        F = prime_field(p)
        for B in ((0,), (0,1), (0,2), (0,1,2), (0,1,3)):
            results.append(run(F,B))
    nine=field9()
    es=nine[0]
    for B in ((es[0],), (es[0],es[1]),(es[0],es[1],es[3])):
        results.append(run(nine,B))
    for rec in results:
        print(*rec)
    print('PASS:',len(results),'direct Fourier calculations; both proof moment identities in each case')
    print('The residual column is scaled by q^(3/2); it need not be small for small q.')


if __name__=='__main__':
    main()
