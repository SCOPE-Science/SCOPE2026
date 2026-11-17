"""Exact rational checks for sharp weighted-Huber star-variation modulus."""
from fractions import Fraction as F
from itertools import combinations,product
from random import Random

def clip(x,d):return max(-d,min(d,x))
def center(x,w,d=F(1)):
    x=[F(z) for z in x];w=[F(z) for z in w];d=F(d)
    assert len(x)==len(w) and all(v>0 for v in w) and d>0
    b=sorted(set([u-d for u in x]+[u+d for u in x]))
    def g(t):return sum((ww*clip(t-xx,d) for xx,ww in zip(x,w)),F(0))
    roots=[z for z in b if g(z)==0]
    for a,c in zip(b,b[1:]):
        ga,gc=g(a),g(c)
        if ga<0<gc:roots.append(a+(c-a)*(-ga)/(gc-ga))
    assert roots
    return (min(roots)+max(roots))/2

def formula(w):
    w=[F(z) for z in w];m=len(w); best=F(0); arg=None
    for mask in range(1,1<<m):
        inside=[i for i in range(m) if (mask>>i)&1]
        outside=[i for i in range(m) if not (mask>>i)&1]
        W=sum((w[i] for i in inside),F(0))
        for signs in product((-1,1),repeat=len(outside)):
            S=sum((w[i]*s for i,s in zip(outside,signs)),F(0))
            if abs(S)<W:
                j=max(inside,key=lambda i:w[i]);q=w[j]/W
                if q>best:best,arg=q,(inside,outside,signs,j,S)
    assert arg is not None
    return 1+(m-2)*best,best,arg

def star(x):return sum(abs(v-x[0]) for v in x[1:])
def main():
    r=Random(314159265)
    for m in range(2,9):
        cases=[[1]*m]
        if m%2==0:cases.append([F(101,100)]+[1]*(m-1))
        cases += [[r.randint(1,9) for _ in range(m)] for _ in range(10)]
        for k,w in enumerate(cases):
            expected,q,arg=formula(w)
            inside,outside,signs,j,S=arg
            W=sum(F(w[i]) for i in inside)
            vals=[F(0)]*m
            for i in inside:vals[i]=F(S,W) # c - x_i = -S/W => x_i = S/W
            for i,s in zip(outside,signs):vals[i]=-F(100*s)
            assert center(vals,w)==0,(m,w,vals)
            changed=vals[:];changed[j]+=F(1,100000)
            x=[F(0)]+vals; y=[F(0)]+changed
            E=lambda a:[center(a[1:],w)]+a[1:]
            num=star([u-v for u,v in zip(E(x),E(y))]);den=star([u-v for u,v in zip(x,y)])
            assert num==expected*den,('witness',m,w,expected,num,den,arg)
            for _ in range(24):
                u=[F(r.randint(-30,30),5) for _ in range(m+1)]
                v=[a+F(r.randint(-20,20),7) for a in u]
                d=star([a-b for a,b in zip(u,v)])
                if d:
                    gain=star([a-b for a,b in zip(E(u),E(v))])/d
                    assert gain<=expected,('bound',m,w,gain,expected)
        print('WEIGHTED_HUBER_EXACT_ARCS',m,'WEIGHT_CASES',len(cases),'PASS')
    for m in range(2,13):
        v,_,_=formula([1]*m)
        assert v==(m-1 if m%2 else F(m,2))
        if m%2==0:
            w=[F(101,100)]+[F(1)]*(m-1)
            assert formula(w)[0]==m-1
        print('UNIFORM_AND_NEAR_EQUAL_WEIGHT_PHASE',m,'PASS')
    print('ALL_WEIGHTED_HUBER_EXACT_CHECKS_PASS')
if __name__=='__main__':main()
