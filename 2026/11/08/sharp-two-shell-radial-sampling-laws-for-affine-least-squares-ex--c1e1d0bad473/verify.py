"""Reproduce finite numerical checks for the radial affine extrapolation theorem.
Python 3 standard library only. These checks do not certify continuum statements.
"""
from math import sqrt, gamma, pi, asin

def psi(d,a):
    if a <= 1: return 1.0
    if d == 2: return 2/pi*(sqrt(a*a-1)+asin(1/a))
    if d == 3: return (a+1/a)/2
    # Independent numerical evaluation of the first-coordinate density.
    k=gamma(d/2)/(sqrt(pi)*gamma((d-1)/2))
    lo=1/a; n=800
    dz=(1-lo)/n
    def zval(i):
        z=lo+i*dz
        return (a*z-1)*max(0,1-z*z)**((d-3)/2)
    return 1+2*k*(dz/3)*(zval(0)+zval(n)+4*sum(zval(i) for i in range(1,n,2))+2*sum(zval(i) for i in range(2,n,2)))

def slope(d,a):
    if a<=1:return 0.
    k=gamma(d/2)/(sqrt(pi)*gamma((d-1)/2))
    return 2*k/(d-1)*(1-1/(a*a))**((d-1)/2)

def root(d):
    l=sqrt(d);r=max(d*4,20.)
    def H(a):return a*slope(d,a)-2*(psi(d,a)-1)
    assert H(l)>0 and H(r)<0,(d,H(l),H(r))
    for _ in range(65):
        m=(l+r)/2
        if H(m)>0:l=m
        else:r=m
    return (l+r)/2

def theorem(d,s):
    a=root(d);c=d/s;t0=min(1.,(a/c)**2)
    if s>=t0: return psi(d,c*sqrt(s)),[(s,1.)]
    return 1+s/t0*(psi(d,c*sqrt(t0))-1),[(0.,1-s/t0),(t0,s/t0)]

def pairwise_grid_opt(d,s):
    c=d/s
    t0=min(1.,(root(d)/c)**2)
    grid=sorted(set([i/100 for i in range(101)]+[s,t0]))
    vals=[psi(d,c*sqrt(t)) for t in grid]
    best=-1.; support=None
    for i,x in enumerate(grid):
        if x>s+1e-13:break
        for j in range(i,len(grid)):
            y=grid[j]
            if y<s-1e-13:continue
            if abs(y-x)<1e-14:
                val=vals[i]
            else:
                w=(y-s)/(y-x)
                val=w*vals[i]+(1-w)*vals[j]
            if val>best:best=val;support=(x,y)
    return best,support

def circle_integral(a,n=40000):
    from math import cos
    return sum(abs(1+a*cos(2*pi*j/n)) for j in range(n))/n

def run():
    assert abs(root(2)-2.5365589892306)<1e-8
    assert abs(root(3)-3)<1e-12
    a=root(2)
    assert abs(sqrt(a*a-1)+2*asin(1/a)-pi)<1e-10
    print('TANGENCY_ROOTS_OK',round(a,12),round(root(3),12))
    print('DISK_THRESHOLDS',round(4/a**2,12),round(2/a,12))
    checked=0
    for d in (2,3,4,5,8):
        for s in (.2,.4,.55,.7,.8,.9):
            bound,support=theorem(d,s)
            grid,sup=pairwise_grid_opt(d,s)
            assert abs(bound-grid)<1e-4,(d,s,bound,grid,sup)
            assert abs(sum(t*w for t,w in support)-s)<1e-11
            assert abs(sum(w for t,w in support)-1)<1e-11
            assert abs(bound-sum(w*psi(d,(d/s)*sqrt(t)) for t,w in support))<1e-9
            checked+=1
    print('TWO_RADIUS_MOMENT_ENVELOPES_OK',checked)
    for a in (1.1,1.5,2,3,5):
        assert abs(psi(2,a)-circle_integral(a))<2e-8,(a,psi(2,a),circle_integral(a))
    print('DIRECT_CIRCLE_KERNEL_QUADRATURE_OK',5)
    # Explicitly check that all three disk phases have different optimal radii.
    s_values=(.4,.7,.9)
    solutions=[theorem(2,s)[1] for s in s_values]
    assert len(solutions[0])==1
    assert len(solutions[1])==2 and solutions[1][-1][0]<1
    assert len(solutions[2])==2 and solutions[2][-1][0]==1
    print('THREE_DISK_OPTIMIZER_REGIMES_OK')
    print('ALL_RADIAL_AFFINE_EXTRAPOLATION_CHECKS_OK')
if __name__=='__main__':run()
