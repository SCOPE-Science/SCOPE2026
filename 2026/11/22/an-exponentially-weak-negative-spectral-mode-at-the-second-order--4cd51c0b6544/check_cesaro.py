"""Independent finite rational checks for the order-two Cesaro interrupter.
The finite checks do not establish the infinite-dimensional theorem.
"""
from fractions import Fraction as F


def arrays(h,n):
    d=(n+3-h)*(n+4-h)
    r=(4*n+10-4*h)/d
    u=(n+F(5,2)+h/2)/d
    w=1/d
    return r,u,w

def Bentry(h,i,j):
    a=-h; dj=(j+a+3)*(j+a+4)
    if i<=j+1: return (2*(j+a+1)-6*(i+a))/dj
    if i==j+2: return (j+a+1)*(j+a+2)/dj
    return F(0)

def Mentry(h,k,i):
    if i>k:return F(0)
    a=-h
    return 2*(k-i+1)/((k+a+1)*(k+a+2))

def Lentry(h,k,j):
    a=-h; scale=(j+a+1)*(j+a+2)/2
    if k==j:return scale
    if k==j+1:return -2*scale
    if k==j+2:return scale
    return F(0)

checks=0
for h in [F(0), F(1,17), F(1,5), F(1,2), F(4,5)]:
    for j in range(12):
        # Verify special B=M^* L finite sums independently.
        for i in range(j+3):
            Bcalc=sum((Mentry(h,k,i)*Lentry(h,k,j) for k in range(j,j+3)),F(0))
            assert Bentry(h,i,j)==Bcalc,(h,i,j,Bentry(h,i,j),Bcalc)
            checks+=1
    for i in range(10):
        for j in range(10):
            gram=sum((Bentry(h,k,i)*Bentry(h,k,j) for k in range(max(i,j)+3)),F(0))
            defect=(i==j)-gram
            ri,ui,wi=arrays(h,i)
            rj,uj,wj=arrays(h,j)
            expected=(ri if i==j else F(0))-4*h*ui*uj+3*h*(1-h*h)*wi*wj
            assert defect==expected,(h,i,j,defect,expected)
            checks+=1
print('EXACT_ORDER_TWO_CESARO_INTERRUPTER_OK',checks)
