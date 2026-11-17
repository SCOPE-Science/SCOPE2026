"""Independent weighted signature enumeration for larger bipartite joins.

The signature (u,v,t,k) records the two exceptional opinions and the
numbers of ones among ordinary vertices of the a- and b-shores.
"""
from math import comb


def formula(a,b):
    if a%2: return (2,1)
    if b%2: return (2+2*comb(b,(b-1)//2) if a==4 else 2,1)
    h=2+(comb(a-2,a//2)+comb(a-2,a//2-2))*comb(b,b//2)
    c=1+comb(a-2,a//2-1)*comb(b,b//2)
    return h,c


def flip(q,d,old):
    return old if 2*q==d else int(2*q>d)


def F(state,a,b):
    u,v,t,k=state
    m=a-2
    u1=flip(k+v,b+1,u)
    v1=flip(k+u,b+1,v)
    t1= t if 2*k==b else m*int(2*k>b)
    sa=t+u+v
    k1= k if 2*sa==a else b*int(2*sa>a)
    return (u1,v1,t1,k1)


def count(a,b):
    m=a-2
    fixed=p2=0
    for u in (0,1):
        for v in (0,1):
            for t in range(m+1):
                for k in range(b+1):
                    x=(u,v,t,k)
                    y=F(x,a,b)
                    if F(y,a,b)!=x:continue
                    w=comb(m,t)*comb(b,k)
                    if y==x:fixed+=w
                    else:p2+=w
    assert p2%2==0
    return fixed,p2//2

if __name__=='__main__':
    cases=0
    for a in range(3,44):
        for b in range(3,44):
            expected=formula(a,b)
            actual=count(a,b)
            assert actual==expected,(a,b,actual,expected)
            cases+=1
    print('PASS weighted signature checker: %s parameter pairs (3<=a,b<=43)'%cases)
    for a,b in [(4,3),(4,6),(6,6),(8,8),(20,20),(43,40)]:
        f,c=count(a,b)
        print('a=%d b=%d fixed=%d primitive_two_cycles=%d'%(a,b,f,c))
