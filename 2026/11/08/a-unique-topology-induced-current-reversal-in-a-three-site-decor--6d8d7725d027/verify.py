"""Exact small-system checks for competing ASEP branch topologies.

Only the standard library is needed. Finite calculations are diagnostics,
not a substitute for the all-size algebraic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

CHECKS = 0

def check(statement, note=''):
    global CHECKS
    assert statement, note
    CHECKS += 1


def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return c

def multiply(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def binomial(n,k):
    return comb(n,k) if 0<=k<=n else 0

def current(L,N,q,depths):
    e=[F(1)]+[F(0)]*len(depths)
    for d in depths:
        w=q**d
        for i in range(len(depths),0,-1):e[i]+=w*e[i-1]
    Z=sum(binomial(L,N-i)*v for i,v in enumerate(e))
    K=sum(binomial(L-2,N-i-1)*v for i,v in enumerate(e))
    return K/Z

def factor_F(m,q):
    return ((2*m*m+6*m+4)*q**6+(m*m+3*m+2)*q**5
            -6*(m*m+m+1)*q**4-(10*m*m+6*m+2)*q**3
            -(14*m*m+6*m-2)*q**2-3*(m-1)*(5*m+4)*q-6*m*(m-1))

def sign(x): return (x>0)-(x<0)

def bisection(m,lo=1.,hi=3.):
    def ff(x):
        return ((2*m*m+6*m+4)*x**6+(m*m+3*m+2)*x**5
            -6*(m*m+m+1)*x**4-(10*m*m+6*m+2)*x**3
            -(14*m*m+6*m-2)*x**2-3*(m-1)*(5*m+4)*x-6*m*(m-1))
    assert ff(lo)<0<ff(hi)
    for _ in range(75):
        mid=(lo+hi)/2
        if ff(mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def verify_algebra():
    for m in range(2,41):
        s=F(m*(m-1),(m+1)*(m+2));t=F(m,m+1)
        ep=[[F(1)],[F(0),F(1),F(1),F(1)],[F(0)]*3+[F(1),F(1),F(1)],[F(0)]*6+[F(1)]]
        es=[[F(1)],[F(0),F(3)],[F(0),F(0),F(3)],[F(0),F(0),F(0),F(1)]]
        zs=[F(0)];zp=[F(0)];ks=[F(0)];kp=[F(0)]
        for i in range(4):
            bs=[s,t,F(1),t][i]
            val=[m*m-4,m*m-1,m*m,m*m-1][i]
            zp=add(zp,[bs*v for v in ep[i]])
            zs=add(zs,[bs*v for v in es[i]])
            kp=add(kp,[bs*val*v for v in ep[i]])
            ks=add(ks,[bs*val*v for v in es[i]])
        cross=add(multiply(kp,zs),[-v for v in multiply(ks,zp)])
        P=[-6*m*(m-1),-3*(m-1)*(5*m+4),-(14*m*m+6*m-2),
           -(10*m*m+6*m+2),-6*(m*m+m+1),m*m+3*m+2,2*m*m+6*m+4]
        pref=F(-m,(m+1)*(m+1)*(m+2))
        target=[pref*x for x in multiply([F(0),F(-1),F(1)],[F(v) for v in P])]
        check(all((cross[i] if i<len(cross) else 0)==(target[i] if i<len(target) else 0) for i in range(max(len(cross),len(target)))), ('polynomial identity',m))
        check(sum(P)==-12*(2*m-1)*(2*m+1),('F(1)',m))
        root=bisection(m)
        check(1<root<3,('unique root interval',m))
        if m>2:check(root>bisection(m-1),('threshold monotonic',m))
        for q in [F(6,5),F(3,2),F(2),F(5,2),F(4)]:
            delta=current(2*m,m+2,q,[1,2,3])-current(2*m,m+2,q,[1,1,1])
            check(sign(delta)==-sign(factor_F(m,q)),('current sign',m,q))
    for L in range(3,23):
        for N in range(1,L+2):
            for q in [F(11,10),F(3,2),F(2),F(10)]:
                delta=current(L,N,q,[1,2])-current(L,N,q,[1,1])
                expected=-1 if N<=(L+2)//2 else 1
                check(sign(delta)==expected,('two-site minimality',L,N,q))

def generator_residual(L,N,q,depths,edges):
    sites=L+len(depths)
    states=[sum(1<<i for i in c) for c in combinations(range(sites),N)]
    weights={s: q**sum(depths[i-L] for i in range(L,sites) if (s>>i)&1) for s in states}
    incoming={s:F(0) for s in states};outgoing={s:F(0) for s in states}
    for s in states:
        for src,dst,rate in edges:
            if ((s>>src)&1) and not ((s>>dst)&1):
                t=s^(1<<src)^(1<<dst)
                flow=weights[s]*rate
                outgoing[s]+=flow;incoming[t]+=flow
    for s in states:check(incoming[s]==outgoing[s],('stationarity',L,N,s))

def verify_generator():
    for L,N in [(4,3),(4,4),(4,5),(6,5)]:
        for q in [F(3,2),F(2)]:
            for depths,tree_edges in [([1,1,1],[(0,L),(1,L+1),(2,L+2)]),
                                      ([1,2,3],[(0,L),(L,L+1),(L+1,L+2)])]:
                edges=[]
                for i in range(L):
                    edges.extend([(i,(i+1)%L,F(3)),((i+1)%L,i,F(1))])
                for u,v in tree_edges:edges.extend([(u,v,q),(v,u,F(1))])
                generator_residual(L,N,q,depths,edges)

if __name__=='__main__':
    verify_algebra()
    verify_generator()
    print('PASS: %d deterministic exact rational/polynomial/state-balance checks' % CHECKS)
    print('transition ratios for ring lengths 4,6,8,20,200:')
    for m in [2,3,4,10,100]:print('L=%d: q*=%.12f' % (2*m,bisection(m)))
