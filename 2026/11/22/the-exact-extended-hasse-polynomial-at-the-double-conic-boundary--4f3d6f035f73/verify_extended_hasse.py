#!/usr/bin/env python3
"""Reproduce exact coefficient identities for specified small prime characteristics."""
from math import comb, factorial

MONOMIALS = ((4,0,0,0),(0,4,0,0),(0,0,4,0),
             (2,2,0,1),(0,2,2,1),(2,0,2,1))

def multiply(f, g, p):
    h = [0] * (len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g): h[i+j] = (h[i+j]+a*b)%p
    return h

def poly_power_linear(c0,c1,n,p):
    return [(comb(n,i)*pow(c0,n-i,p)*pow(c1,i,p))%p for i in range(n+1)]

def from_plane(p):
    target=(2*p-2,p-1,p-1); output=[0]*p
    def visit(i,k,x,y,z,coefficient,degree):
        if i==6:
            if k==0 and (x,y,z)==target:
                output[degree]=(output[degree]+coefficient)%p
            return
        dx,dy,dz,da=MONOMIALS[i]
        for count in range(k+1):
            xx,yy,zz=x+count*dx,y+count*dy,z+count*dz
            if xx>target[0] or yy>target[1] or zz>target[2]: break
            visit(i+1,k-count,xx,yy,zz,coefficient*comb(k,count),degree+da*count)
    visit(0,p-1,0,0,0,1,0)
    return output

def from_deuring(p):
    m=(p-1)//2
    h=[0]*(m+1)
    for j in range(m+1):
        for r in range(j+1):
            h[r]=(h[r]+comb(m,j)**2*comb(j,r)*(-1)**j)%p
    return multiply(poly_power_linear(-2,1,m,p),h,p)

def from_elliptic(p):
    m=(p-1)//2
    h=[0]*(m+1)
    for j in range(m//2+1):
        c=factorial(m)//(factorial(j)**2*factorial(m-2*j))
        term=poly_power_linear(2,1,2*j,p)
        offset=m-2*j
        for r,v in enumerate(term):
            h[r+offset]=(h[r+offset]+c*v*2**offset)%p
    return [(x*pow(4,-m,p))%p for x in multiply(poly_power_linear(-2,1,m,p),h,p)]

if __name__=='__main__':
    for p in (5,7,11,13,17,19,23,29):
        a=from_plane(p);b=from_deuring(p);c=from_elliptic(p)
        assert a==b==c,(p,a,b,c)
        print(p, 'identity checked; degree',len(a)-1)
    print('EXTENDED_CIANI_HASSE_OK')
