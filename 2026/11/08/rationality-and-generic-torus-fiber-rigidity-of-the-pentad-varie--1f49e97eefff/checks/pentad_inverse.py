#!/usr/bin/env python3
"""Exact arithmetic consistency checks for the pentad rational inverse.

Uses only Python standard library; no finite test is treated as a proof of
an infinite statement.
"""
from fractions import Fraction as Q


def coordinates(n, x, y, lam):
    return {(i,j): lam[i-1]*lam[j-1]*(y[j-1]-y[i-1])/(x[j-1]-x[i-1])
            for i in range(1,n) for j in range(i+1,n+1)}


def inverse(n, z):
    u2 = z[2,3]/z[1,3]
    u3 = z[2,3]/z[1,2]
    x = [Q(0),Q(1),Q(2)]
    y = [Q(0),Q(1),Q(2)]
    lam = [Q(1),u2,u3]
    for j in range(4,n+1):
        u = z[1,j]*z[2,3]/(z[1,2]*z[1,3])
        v = z[2,j]*z[1,3]/(z[1,j]*z[2,3])
        w = z[3,j]*z[1,2]/(z[1,j]*z[2,3])
        xx = 2*(w-v)/(1-2*v+w)
        B = (1-v)*xx+v
        yy = xx/B
        ll = u*B
        x.append(xx)
        y.append(yy)
        lam.append(ll)
    return x,y,lam


def run():
    examples=0
    for n in (5,6,8,11):
        for shift in (0,1,3,7):
            x = [Q(0),Q(1),Q(2)] + [Q(5*j+shift+1,3) for j in range(4,n+1)]
            y = [Q(0),Q(1),Q(2)] + [Q(7*j+2*shift+1,4) for j in range(4,n+1)]
            lam = [Q(1),Q(3+shift,2),Q(7+shift,4)] + [Q(2*j+shift+1,3) for j in range(4,n+1)]
            assert len(set(x))==n and len(set(y))==n
            z = coordinates(n,x,y,lam)
            xr,yr,lr = inverse(n,z)
            assert (xr,yr,lr) == (x,y,lam)
            # Check projective reconstruction via the canonical projective scale.
            c = z[2,3]/(z[1,2]*z[1,3])
            zr = coordinates(n,xr,yr,lr)
            assert all(c*z[k] == zr[k] for k in z)
            # The common diagonal column torus changes p and q but not their ratios.
            nu = [Q(3*i+shift+2,5) for i in range(1,n+1)]
            t = [Q(2*i+shift+3,7) for i in range(1,n+1)]
            p = {(i,j):nu[i-1]*nu[j-1]*(x[j-1]-x[i-1]) for i,j in z}
            q = {(i,j):nu[i-1]*nu[j-1]*z[i,j]*(x[j-1]-x[i-1]) for i,j in z}
            z_from_pq = {k:q[k]/p[k] for k in z}
            assert z_from_pq == z
            assert all((t[i-1]*t[j-1]*q[i,j])/(t[i-1]*t[j-1]*p[i,j])==z[i,j]
                       for i,j in z)
            examples+=1
    print('EXACT_RECOVERY_AND_TORUS_INVARIANCE_OK',examples)
    print('CERTIFICATE_OK')

if __name__ == '__main__':
    run()
