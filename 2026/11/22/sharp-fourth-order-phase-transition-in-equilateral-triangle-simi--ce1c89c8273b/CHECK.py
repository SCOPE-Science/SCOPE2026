"""Numerical checks of exact similarity-containment volume for an equilateral triangle in a rectangle."""
from math import sqrt

SQRT3 = sqrt(3.)
R = 2./SQRT3


def exact(r):
    return (8*SQRT3*r-7)/12+0.75*max(R-r, 0.)**4


def direct_grid(r, n=800):
    # Midpoint integration over complete (s,t)-space, using the original three transformed vertices.
    dx=2*r/n
    dy=2/n
    area=0.0
    for i in range(n):
        s=-r+(i+0.5)*dx
        for j in range(n):
            t=-1+(j+0.5)*dy
            # Triangle (0,0),(1,0),(1/2,sqrt(3)/2) under map (x,y)->(sx-ty,tx+sy).
            X=(0.,s,0.5*s-0.5*SQRT3*t)
            Y=(0.,t,0.5*t+0.5*SQRT3*s)
            wx=max(X)-min(X)
            wy=max(Y)-min(Y)
            if wx<=r and wy<=1:
                area+=(r-wx)*(1-wy)
    return area*dx*dy


def wedge_simpson(r, n=20000):
    # Independent 1D integral of translation-rectangle area over one fundamental sector
    # after an exact inner t integration.
    def fun(s):
        upper=min(s/SQRT3,2-SQRT3*s)
        if upper<0:return 0.
        return (r-s)*((1-SQRT3*s/2)*upper-upper*upper/4)
    b=min(r,R)
    # Piecewise Simpson avoids kink in integrand at s=SQRT3/2.
    def simpson(a,b):
        h=(b-a)/n
        S=fun(a)+fun(b)
        for k in range(1,n):S+=(4 if k%2 else 2)*fun(a+k*h)
        return h*S/3
    return 12*(simpson(0,SQRT3/2)+simpson(SQRT3/2,b))


def main():
    for r in [1.0,1.01,1.075,1.15,R,1.16,1.25,1.5,2.0,5.0]:
        ref=exact(r)
        grid=direct_grid(r,500)
        wedge=wedge_simpson(r,500)
        print('r=',r,'exact',ref,'grid',grid,'d=',grid-ref,'wedge',wedge,'d=',wedge-ref)
        assert abs(grid-ref)<0.00015, (r,grid,ref)
        assert abs(wedge-ref)<1e-10, (r,wedge,ref)
    print('PASS')

if __name__=='__main__':main()
