"""Independent rational checks for lattice counts of square-based pyramids."""
from fractions import Fraction as Q
from collections import defaultdict
from math import floor, ceil


def law(n):
    p=defaultdict(Q)
    for j in range(n):
        for k in (j*j,j*(j+1),(j+1)*(j+1)):
            p[k]+=Q(1,3*n)
    return dict(p)


def expected_law(n):
    p={0:Q(2,3*n),n*n:Q(1,3*n)}
    for j in range(1,n):
        p[j*j]=Q(2,3*n)
        p[j*(j+1)]=Q(1,3*n)
    return p


def direct_lattice(n,a,b,t1,t2,t3):
    # Enumerate all candidates in the unique integer height section.
    h=1-t3
    xlo=t1+h*a
    xhi=xlo+n*t3
    ylo=t2+h*b
    yhi=ylo+n*t3
    return sum(xlo<=i<=xhi and ylo<=j<=yhi
               for i in range(floor(xlo)-1,ceil(xhi)+2)
               for j in range(floor(ylo)-1,ceil(yhi)+2))


checked=0
for n in range(1,81):
    p=law(n)
    assert p==expected_law(n)
    assert sum(p.values())==1
    m=sum(Q(k)*v for k,v in p.items())
    var=sum((Q(k)-m)**2*v for k,v in p.items())
    assert m==Q(n*n,3)
    assert var==Q(4*n**4+5*n*n+1,45)

for n in range(1,8):
    for a,b in ((Q(0),Q(0)),(Q(2,3),Q(-3,5)),(Q(3),Q(-4))):
        for k in range(1,14):
            t1,t2,t3=Q((3*k)%17,17),Q((7*k)%19,19),Q(k,17)
            if t1==0 or t2==0: continue
            observed=direct_lattice(n,a,b,t1,t2,t3)
            L=n*t3
            r=L-floor(L)
            xlo=t1+(1-t3)*a
            ylo=t2+(1-t3)*b
            x_count=floor(xlo+L)-ceil(xlo)+1
            y_count=floor(ylo+L)-ceil(ylo)+1
            assert observed==x_count*y_count
            assert x_count in (floor(L),floor(L)+1)
            assert y_count in (floor(L),floor(L)+1)
            checked+=1
print('PYRAMID_CHECK_OK',checked,'rational-section-tests; 80 exact moment laws')
