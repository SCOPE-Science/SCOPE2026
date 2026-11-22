#!/usr/bin/env python3
"""Direct finite checks of facet support geometry. Standard Python 3 only."""
import cmath, math
for n in range(3,81):
    zeta=[cmath.exp(2j*math.pi*k/n) for k in range(n)]
    om=cmath.exp(2j*math.pi/3)
    # A real-linear functional L(z,t)=Re(a z+b t), with w_j=b+a*om**j.
    # Group edge normals for the polygon whose vertices are zeta[k].
    normals=[cmath.exp(-1j*(2*k+1)*math.pi/n) for k in range(n)]
    h=math.cos(math.pi/n)
    strict=0
    prism=0
    for k in range(n):
        w0=normals[k]
        for m in range(n):
            w1=normals[(k-m)%n] # opposite index convention gives CCW difference in w-plane
            # For group0/group1, solve w2= -om*w0-om**2*w1
            w2= -om*w0-om**2*w1
            dots=[(w2*v).real for v in zeta]
            maxv=max(dots)
            inside=maxv<=h+1e-8
            strict_inside=maxv<h-1e-8
            assert inside == (3*m<=n), (n,k,m,maxv,h)
            assert strict_inside == (0<m and 3*m<n), (n,k,m,maxv,h)
            if strict_inside: strict+=1
            if inside and not strict_inside: prism+=1
    assert strict==n*((n-1)//3)
    assert prism==n*(1+(n%3==0))
    assert 3*strict==3*n*((n-1)//3)
    print(n,3*strict,prism)
print('PASS 3<=n<=80')
