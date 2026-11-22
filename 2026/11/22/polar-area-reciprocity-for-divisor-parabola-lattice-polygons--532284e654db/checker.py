"""Independent exact arithmetic checks for divisor-parabola polar area theorem.
Standard-library only. Finite tests supplement, not replace, the infinite proof.
"""
from fractions import Fraction as Q
from math import gcd, isqrt


def divisors(h):
    small=[];large=[]
    for d in range(1,isqrt(h)+1):
        if h%d==0:
            small.append(d)
            if d*d !=h:large.append(h//d)
    return small+large[::-1]


def area(vertices):
    cross=sum(x*v-y*u for (x,y),(u,v) in zip(vertices,vertices[1:]+vertices[:1]))
    return abs(Q(cross,2))


def original_vertices(ds):
    return [(0,-1)]+[(d,d*d) for d in ds]+[(-d,d*d) for d in ds[::-1]]


def polar_vertices(ds):
    h=ds[-1]
    pos=[(Q(1,a)+Q(1,b),-Q(1,a*b)) for a,b in zip(ds,ds[1:])]
    return [(Q(0),Q(1,h*h))]+pos[::-1]+[(Q(2),Q(-1)),(Q(-2),Q(-1))]+[(-x,y) for x,y in pos]


def check(h):
    ds=divisors(h)
    gapcube=sum((b-a)**3 for a,b in zip(ds,ds[1:]))
    A=area(original_vertices(ds))
    B=sum(gcd(abs(x-u),abs(y-v)) for (x,y),(u,v) in zip(original_vertices(ds),original_vertices(ds)[1:]+original_vertices(ds)[:1]))
    P=area(polar_vertices(ds))
    assert A==Q(4*h**3+2-gapcube,3),(h,'original area',A)
    assert B==4*h,(h,'boundary',B)
    assert P==Q(8*h**3+4+gapcube,3*h**3),(h,'polar area',P)
    assert P+A/h**3==4+Q(2,h**3),(h,'reciprocity')
    assert A-(B//2)+1>=1
    return (A,P)


def main():
    for h in range(2,501):check(h)
    for h in [720,840,2520,5040,27720,99991,999983,2*99991]:check(h)
    print('PASS: 507 independent exact vertex-shoelace and boundary-gcd comparisons')
    for h in [2,3,6,12,60,2520]:
        a,p=check(h)
        print('h=%d  area=%s  polar_area=%s  complement=%s' %(h,a,p,p+a/h**3))
    # Insertion triangle check via exact rational coordinates for selected rational triples.
    triples=[(Q(1),Q(1,2),Q(1,3)),(Q(1),Q(1,3),Q(1,10)),(Q(1,2),Q(1,3),Q(1,7))]
    for u,w,v in triples:
        V=lambda x,y:(x+y,-x*y)
        a,b,c=V(u,v),V(u,w),V(w,v)
        tri=abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
        assert tri==(u-v)*(u-w)*(w-v)
    print('PASS: three exact insertion-determinant comparisons')

if __name__=='__main__':main()
