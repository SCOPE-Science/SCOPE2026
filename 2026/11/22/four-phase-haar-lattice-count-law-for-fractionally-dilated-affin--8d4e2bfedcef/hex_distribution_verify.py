"""Exact-rational checks for the fractional-radius hexagon translation distribution.
Standard library only; diagnostic checks complement the written infinite-family proof.
"""
from fractions import Fraction as Q
from collections import defaultdict
from math import floor, ceil


def cut(poly, a, b, c):
    if not poly:
        return []
    out=[]
    for j, p in enumerate(poly):
        q=poly[(j+1)%len(poly)]
        vp=a*p[0]+b*p[1]-c
        vq=a*q[0]+b*q[1]-c
        if vp <= 0:
            out.append(p)
        if (vp<0<vq) or (vq<0<vp):
            u=vp/(vp-vq)
            out.append((p[0]+u*(q[0]-p[0]),p[1]+u*(q[1]-p[1])))
    return [p for i,p in enumerate(out) if p!=out[i-1]]


def area(poly):
    return abs(sum(p[0]*poly[(i+1)%len(poly)][1]-p[1]*poly[(i+1)%len(poly)][0]
                   for i,p in enumerate(poly))/2) if len(poly)>=3 else Q(0)


def bin2(a):
    return a*(a-1)//2 if a>=2 else 0


def C(s,A,B):
    return bin2(s+2)-bin2(s-A+1)-bin2(s-B+1)+bin2(s-A-B)


def point_count(n, t, x, y):
    r=n+t
    lx=ceil(x-r); rx=floor(x+r)
    ly=ceil(y-r); ry=floor(y+r)
    lz=ceil(x+y-r); rz=floor(x+y+r)
    return C(rz-lx-ly,rx-lx,ry-ly)-C(lz-1-lx-ly,rx-lx,ry-ly)


def brute(n,t,x,y):
    r=n+t
    return sum(1 for i in range(-n-2,n+3) for j in range(-n-2,n+3)
               if abs(i-x)<r and abs(j-y)<r and abs(i+j-x-y)<r)


def partition(t,n):
    polys=[[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]]
    for a,b,c in ([(1,0,s) for s in (t,1-t)]+[(0,1,s) for s in (t,1-t)]
                  +[(1,1,s) for s in (t,1-t,1+t,2-t)]):
        next_polys=[]
        for p in polys:
            for x in (cut(p,a,b,c),cut(p,-a,-b,-c)):
                if area(x)>0:
                    next_polys.append(x)
        polys=next_polys
    out=defaultdict(Q)
    for p in polys:
        x=sum(v[0] for v in p)/len(p)
        y=sum(v[1] for v in p)/len(p)
        k=point_count(n,t,x,y)
        assert k==brute(n,t,x,y), (n,t,x,y,k)
        out[k-3*n*n]+=area(p)
    assert sum(out.values())==1
    return dict(out),polys


def law(n,t):
    if t<=Q(1,3):
        z=[(0,(3*t-1)**2),(n,3*t*(2-5*t)),(2*n,3*t*t),(3*n+1,3*t*t)]
    elif t<=Q(1,2):
        z=[(n,3*(2*t-1)**2),(2*n,3*(1-2*t)*(4*t-1)),
           (3*n,(3*t-1)**2),(3*n+1,3*t*t)]
    elif t<=Q(2,3):
        z=[(3*n,(3*t-2)**2),(3*n+1,3*(1-t)**2),
           (4*n+1,3*(2*t-1)*(3-4*t)),(5*n+2,3*(2*t-1)**2)]
    else:
        z=[(3*n+1,3*(1-t)**2),(4*n+1,3*(1-t)**2),
           (5*n+2,3*(1-t)*(5*t-3)),(6*n+3,(3*t-2)**2)]
    return {a:b for a,b in z if b!=0}


def main():
    trials=[Q(0),Q(1,10),Q(1,6),Q(1,4),Q(1,3),
            Q(7,20),Q(2,5),Q(9,20),Q(1,2),
            Q(11,20),Q(3,5),Q(13,20),Q(2,3),
            Q(7,10),Q(4,5),Q(9,10),Q(1)]
    checks=0
    for t in trials:
        for n in [1,2,3,4,7,13]:
            if t==0 or t==1:
                assert all(point_count(n,t,Q(i,17),Q(j,19))==3*(n+int(t))**2
                           for i in range(1,17) for j in range(1,19))
                continue
            observed,polys=partition(t,n)
            assert observed==law(n,t), (n,t,observed,law(n,t))
            assert sum((3*n*n+d)*p for d,p in observed.items())==3*(n+t)**2
            checks+=1
    print('HEX_DISTRIBUTION_CHECK_OK',checks,'exact area/point-law comparisons')

if __name__=='__main__': main()
