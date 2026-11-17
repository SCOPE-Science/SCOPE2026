"""Independent weighted population-profile certificate for matching-deleted cliques.
No vertex-neighborhood loops: a matched pair has identical open neighborhood.
"""
from math import comb, factorial


def update(pairs, singles):
    r=len(pairs); u=len(singles); n=2*r+u
    total=sum(sum(p) for p in pairs)+sum(singles)
    pnext=[]
    for a,b in pairs:
        neigh=total-a-b; deg=n-2
        if neigh*2>deg:pnext.append((1,1))
        elif neigh*2<deg:pnext.append((0,0))
        else:pnext.append((a,b))
    snext=[]
    for bit in singles:
        neigh=total-bit; deg=n-1
        snext.append(1 if neigh*2>deg else 0 if neigh*2<deg else bit)
    return tuple(pnext),tuple(snext)


def target(r,u):
    n=2*r+u
    if u==0:return 2+2**r, (comb(n,r)-2**r)//2
    if u%2==0:return 2, comb(n,n//2)//2
    if u==1:return 2, comb(r,r//2)
    h=(n-1)//2
    return 2, (comb(r,(h+1)//2) if h%2 and h+1<=2*r else 0)


def check(r,u):
    F=0;Q=0;weighttotal=0
    for a in range(r+1):
        for b in range(r-a+1):
            c=r-a-b
            weightpairs=factorial(r)//(factorial(a)*factorial(b)*factorial(c))*2**c
            pairs=((0,0),)*a+((1,1),)*b+((0,1),)*c
            for w in range(u+1):
                singles=(1,)*w+(0,)*(u-w)
                t=(pairs,singles)
                s1=update(*t);s2=update(*s1)
                weight=weightpairs*comb(u,w)
                weighttotal+=weight
                if s1==t:F+=weight
                if s2==t:Q+=weight
    assert weighttotal==2**(2*r+u)
    f,c=target(r,u)
    assert F==f and Q==f+2*c,(r,u,F,Q,f,c)
    return F,c

def main():
    count=0
    for r in range(1,19):
        for u in range(0,16):
            check(r,u);count+=1
    print(f'PASS: {count} weighted profile systems (all r=1..18, u=0..15)')
    for r,u in [(3,0),(3,1),(4,1),(4,3),(3,5),(4,4),(6,3),(3,7)]:
        print('r,u',r,u,'fixed,two-cycles',check(r,u))
if __name__=='__main__':main()
