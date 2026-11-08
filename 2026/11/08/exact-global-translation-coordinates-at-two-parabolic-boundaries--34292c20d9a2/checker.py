"""Exact-rational checks for the piecewise translation normal forms.
All tests use independently evaluated rational coordinates and branches.
They do not substitute for the unrestricted algebraic proof.
"""
from fractions import Fraction as Q


def phi(b,c,t):
    if t<=1:
        return -c*t,c*(1-t)
    if b==0:
        if t<=2:
            return c*(t-2),c*(1-t)
        return c*(t-2),c*(t-3)
    if t<=2:
        return -c,c*(1-t)
    if t<=3:
        return c*(t-3),-c
    return c*(t-3),c*(t-4)


def f(b,x,y):
    return ((2 if x>=0 else b)*x-y,x)


def h(b,x,y):
    return max(abs(x-y),-x-y) if b==0 else max(abs(x-y),-x,-y)


def inverse(b,x,y):
    c=h(b,x,y)
    if not c:
        raise ValueError('fixed ray excluded')
    if y-x == c and (x<=0 or y>=0):
        # incoming ray: t=-x/c; for t<=1; b=0 only t<=1 and b=1 same.
        t=-x/c
        if t<=1:
            return c,t
    if b==0:
        if -x-y==c and x<=0 and y<=0:
            return c,x/c+2
        return c,x/c+2
    if x==-c and -c<=y<=0:
        return c,1-y/c
    if y==-c and -c<=x<=0:
        return c,3+x/c
    return c,3+x/c


def verify():
    tests=0
    cvals=[Q(1,7),Q(2,5),Q(1),Q(3),Q(13,4)]
    tvals=[Q(k,12) for k in range(-144,241)]
    for b in (0,1):
        for c in cvals:
            for t in tvals:
                x,y=phi(b,c,t)
                assert h(b,x,y)==c,(b,c,t,'height')
                ci,ti=inverse(b,x,y)
                assert ci==c and ti==t,(b,c,t,ci,ti,'inverse')
                assert f(b,x,y)==phi(b,c,t+1),(b,c,t,'conjugacy')
                xx,yy=x,y
                for n in range(1,5):
                    xx,yy=f(b,xx,yy)
                    assert (xx,yy)==phi(b,c,t+n),(b,c,t,n,'iterate')
                tests+=7
                # Check first entry into outgoing positive cone among forward iterates.
                nmax=max(0,((Q(3+b)-t).__ceil__()))
                def cone(x,y): return x>=y>=0
                assert cone(*phi(b,c,t+nmax))
                if nmax:
                    assert not cone(*phi(b,c,t+nmax-1))
                tests+=2
    # Determinant of each affine parametrization in (c,t) is c, away from seams.
    # Test exact area of small rectangles lying in an affine piece.
    for b in (0,1):
        pieces=[Q(-2),Q(1,2),Q(3,2),Q(5,2),Q(7,2)] if b else [Q(-2),Q(1,2),Q(3,2),Q(7,2)]
        for t in pieces:
            eps=Q(1,100)
            c=Q(7,5)
            xy=phi(b,c,t); xy_c=phi(b,c+eps,t); xy_t=phi(b,c,t+eps)
            determinant=(xy_c[0]-xy[0])*(xy_t[1]-xy[1])-(xy_t[0]-xy[0])*(xy_c[1]-xy[1])
            assert determinant==c*eps**2
            tests+=1
    return tests


if __name__=='__main__':
    print('Exact-rational assertions:',verify())
