#!/usr/bin/env python3
"""Finite corroboration of Cassini-oval quadratic phase retrieval identities."""
import cmath

def determinant(a):
    a=[list(map(complex,row)) for row in a]
    n=len(a); product=1+0j
    for i in range(n):
        j=max(range(i,n),key=lambda k:abs(a[k][i]))
        if abs(a[j][i])<1e-13: return 0j
        if i!=j: a[i],a[j]=a[j],a[i];product=-product
        pivot=a[i][i]; product*=pivot
        for k in range(i+1,n):
            fac=a[k][i]/pivot
            for t in range(i+1,n): a[k][t]-=fac*a[i][t]
    return product

def features(z):
    h=abs(z)**2
    return [1.0,(z*z).real,(z*z).imag,h,z.real,z.imag,h*z.real,h*z.imag]

count=0
for r in (0.5,1.0,2.0):
    ts=(0.14,0.87,1.62,2.73)
    zs=[cmath.sqrt(1+r*cmath.exp(1j*t)) for t in ts]
    rows=[features(z) for z in zs]+[features(-z) for z in zs]
    det=determinant(rows)
    assert abs(det)>1e-11,(r,det)
    count+=1
    for z in zs+[-z for z in zs]:
        assert abs(abs(z*z-1)-r)<1e-12
        H=(z*z-1)*(z.conjugate()**2-1)-r*r
        assert abs(H)<1e-10
        count+=1
        for A,B in ((1.2+0.7j,-0.8+0.3j),(0j,1j),(2.0,0j)):
            p=A+B*(z*z-1)
            flip=r*B.conjugate()+(z*z-1)*A.conjugate()/r
            assert abs(abs(p)**2-abs(flip)**2)<1e-9
            count+=1
print('CASSINI_QUADRATIC_CHECK_PASS',count)
