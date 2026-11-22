"""Finite consistency tests for periodic linear-spline mass and stiffness laws.

Run: python3 checker.py (Python standard library only).
Exact rational tests do not replace the analytic proof.
"""
from fractions import Fraction as Q
from math import pi, cos, sin, sqrt

checks = 0


def verify(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def matrices(m, a, b):
    n = 2*m
    K = [[Q(0) for j in range(n)] for i in range(n)]
    M = [[Q(0) for j in range(n)] for i in range(n)]
    edges = [a if i % 2 == 0 else b for i in range(n)]
    for i, h in enumerate(edges):
        j = (i+1) % n
        for q in (i,j):
            K[q][q] += 1/h
            M[q][q] += h/3
        K[i][j] -= 1/h
        K[j][i] -= 1/h
        M[i][j] += h/6
        M[j][i] += h/6
    return K,M,edges


def quadratic(A, v):
    return sum(v[i]*A[i][j]*v[j]
               for i in range(len(v)) for j in range(len(v)))


def dot(A,v,i):
    return sum(A[i][j]*v[j] for j in range(len(v)))


def bloch(m,a,b,theta):
    aa, bb = float(a),float(b)
    # K and M are 2x2 Hermitian; the offdiagonal entry is at phase -theta.
    ko = -1/aa - complex(cos(theta),-sin(theta))/bb
    mo = (aa + bb*complex(cos(theta),-sin(theta)))/6
    kd = 1/aa+1/bb
    md = (aa+bb)/3
    # Determinant of K - lambda M = c2 lambda^2 + c1 lambda + c0.
    c2 = md*md - abs(mo)**2
    c1 = -2*kd*md + 2*(ko*mo.conjugate()).real
    c0 = kd*kd - abs(ko)**2
    disc = max(0.,c1*c1-4*c2*c0)
    roots = sorted(((-c1-sqrt(disc))/(2*c2),
                    (-c1+sqrt(disc))/(2*c2)))
    return roots,(kd,md,ko,mo)


for m in range(2,11):
    for a,b in [(Q(1),Q(1)),(Q(1),Q(2)),(Q(2),Q(5)),
                (Q(3),Q(2)),(Q(1),Q(7)),(Q(5),Q(13))]:
        K,M,edges=matrices(m,a,b)
        n=2*m
        top=Q(12)/(a*b)
        vectors=([Q((-1)**i) for i in range(n)],
                 [Q(1) for i in range(n)],
                 [Q(i*i-5*i+3) for i in range(n)],
                 [Q((7*i+13)%11-5) for i in range(n)])
        for v in vectors:
            mass=quadratic(M,v)
            stiff=quadratic(K,v)
            squares=sum((1/h+2*h/(a*b))*(v[i]+v[(i+1)%n])**2
                        for i,h in enumerate(edges))
            verify(top*mass-stiff==squares,'rational sum-of-squares identity')
            verify(stiff<=top*mass,'rational sharp bound')
        v=vectors[0]
        verify(all(dot(K,v,i)==top*dot(M,v,i) for i in range(n)),
               'exact alternating eigenvector')
        w=vectors[1]
        verify(all(dot(K,w,i)==0 for i in range(n)),
               'exact constant eigenvector')
        all_roots=[]
        for j in range(m):
            theta=2*pi*j/m
            roots,blocks=bloch(m,a,b,theta)
            kd,md,ko,mo=blocks
            verify(roots[0]>=-1e-8*float(top) and roots[1]<=float(top)*(1+1e-8),
                   'Bloch spectral confinement')
            for lam in roots:
                d=kd-lam*md
                z=ko-lam*mo
                verify(abs(d*d-abs(z)**2)<1e-7*float(top)**2,
                       'Bloch determinant residual')
            all_roots.extend(roots)
        all_roots.sort()
        verify(abs(all_roots[0])<1e-7*float(top),'constant zero eigenvalue')
        verify(abs(all_roots[-1]-float(top))<1e-7*float(top),
               'highest Bloch eigenvalue')
        if m%2==0:
            d1=b*(3*a+b)
            d2=a*(a+3*b)
            lower=float(Q(12)/max(d1,d2))
            upper=float(Q(12)/min(d1,d2))
            verify(abs(all_roots[m-1]-lower)<1e-7*float(top),
                   'lower inner edge for even repeat count')
            verify(abs(all_roots[m]-upper)<1e-7*float(top),
                   'upper inner edge for even repeat count')
            width=Q(12)*abs(a*a-b*b)/(a*b*(3*a+b)*(a+3*b))
            verify(abs((upper-lower)-float(width))<1e-7*float(top),
                   'exact spectral gap width')
            delta=abs(a-b)/(a+b)
            verify(width/top == delta/(4-delta*delta),
                   'normalized gap contrast law')
print('PASS:',checks,'finite exact and floating-point checks')
