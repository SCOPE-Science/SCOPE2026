#!/usr/bin/env python3
"""Independent finite numerical checks for a symmetric fishery iteration.
The infinite asymptotic statements are proved analytically in RESULT.md.
"""
import math

def step(k,y,z):
    return z*math.exp(-y)/(1+k*z),y*math.exp(-z)/(1+k*y)

def phi(k,x):
    return x-math.log1p(k*x)

def check():
    tested=0
    for k in (.4,.8,1.,1.4,2.):
        for y,z in ((.9,.3),(.2,.7),(.4,.4)):
            if y!=z:
                yy,zz=step(k,y,z)
                lhs=abs(math.log(yy/zz))-abs(math.log(y/z))
                rhs=phi(k,max(y,z))-phi(k,min(y,z))
                assert abs(lhs-rhs)<2e-13,(k,y,z,lhs,rhs)
                assert (yy>zz)==(y<z)
                tested+=2
            yy,zz=y,z
            N=200000
            for _ in range(N):
                yy,zz=step(k,yy,zz)
            assert 0<yy<y and 0<zz<z
            if y==z:
                target=1/(1+k)
                assert abs(N*yy-target)<2e-4 and abs(N*zz-target)<2e-4
            elif k==1:
                assert abs(N*(yy+zz)-1.)<1e-4
                assert (yy>zz)==(y>z)
            elif k<1:
                assert (yy>zz)==(y>z)
                assert abs(N*max(yy,zz)-1/k)<.12
            elif k>1:
                assert abs(N*(yy+zz)-2/(k+1))<.007
            tested+=2
    # Third-order Taylor control of the two-step map at several small radii.
    for k in (.5,1.,2.):
        for radius in (.01,.005,.002):
            y,z=radius, .6*radius
            u,v=step(k,y,z)
            u,v=step(k,u,v)
            pred_y=y-2*k*y*y-2*y*z
            pred_z=z-2*k*z*z-2*y*z
            assert abs(u-pred_y)<30*(y+z)**3
            assert abs(v-pred_z)<30*(y+z)**3
            tested+=2
    print('PASS',tested,'numerical and asymptotic-regime checks')
if __name__=='__main__':check()
