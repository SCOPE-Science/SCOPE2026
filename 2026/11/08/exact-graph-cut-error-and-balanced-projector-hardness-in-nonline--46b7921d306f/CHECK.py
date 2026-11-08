"""Exact-rational verification for a quadratic-flow split-projection parareal theorem.

Run: python3 CHECK.py
Only the standard Python library is required.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def phi(u,edges):
    return sum((w*u[i]*u[j] for i,j,w in edges),F(0))


def cut(u,S,edges):
    return sum((w*u[i]*u[j] for i,j,w in edges if (i in S)!=(j in S)),F(0))


def f_map(x,h,edges):
    u,z=x
    return (tuple(u),z+h*phi(u,edges))


def g_map(x,h,d,edges):
    u,z=x
    return (tuple((1+d)*ui for ui in u),z+h*phi(u,edges))


def add(x,y):
    return (tuple(a+b for a,b in zip(x[0],y[0])),x[1]+y[1])


def sub(x,y):
    return (tuple(a-b for a,b in zip(x[0],y[0])),x[1]-y[1])


def project(x,S):
    u,z=x
    return tuple(a if i in S else F(0) for i,a in enumerate(u)),F(0)


def split(x,S):
    return project(x,S),sub(x,project(x,S))


def s_map(x,h,d,S,edges):
    px,qx=split(x,S)
    return add(f_map(px,h,edges),g_map(qx,h,d,edges))


def h_map(x,h,d,S,edges):
    px,_=split(x,S)
    return add(g_map(x,h,d,edges),sub(f_map(px,h,edges),g_map(px,h,d,edges)))


def advance_first(x0,h,p,S,edges,variant):
    d=h**(p+1)
    x1_old=g_map(x0,h,d,edges)
    x1_new=f_map(x0,h,edges)
    B=s_map if variant=='S' else h_map
    x2_new=add(f_map(x1_old,h,edges),sub(B(x1_new,h,d,S,edges),B(x1_old,h,d,S,edges)))
    return x2_new,f_map(x1_new,h,edges)


def exact_error(x0,h,p,S,edges,variant):
    d=h**(p+1)
    u=x0[0]
    qu=tuple(ui if i not in S else F(0) for i,ui in enumerate(u))
    z_error = h*(2*d+d*d)*cut(u,S,edges) if variant=='S' else F(0)
    return tuple(-d*d*a for a in qu),z_error


def cut_width(S,edges):
    return sum((w for i,j,w in edges if (i in S)!=(j in S)),0)


def forest_min_cut(n,edges,target):
    """Exact cardinality-constrained minimum cut on a forest (DP)."""
    adj=[[] for _ in range(n)]
    for i,j,w in edges:
        adj[i].append((j,w)); adj[j].append((i,w))
    seen=set()
    def walk(v,parent):
        seen.add(v)
        dp={(0,0):0,(1,1):0}
        for ch,w in adj[v]:
            if ch==parent: continue
            child=walk(ch,v)
            next_dp={}
            for (cnt,lab),cost in dp.items():
                for (tc,lc),c in child.items():
                    k=(cnt+tc,lab)
                    value=cost+c+(w if lab!=lc else 0)
                    next_dp[k]=min(value,next_dp.get(k,float('inf')))
            dp=next_dp
        return dp
    all_dp={0:0}
    for root in range(n):
        if root in seen:continue
        comp=walk(root,-1)
        comp_dp={}
        for (cnt,lab),cost in comp.items():
            comp_dp[cnt]=min(comp_dp.get(cnt,float('inf')),cost)
        new={}
        for c,v in all_dp.items():
            for cc,vv in comp_dp.items():
                new[c+cc]=min(new.get(c+cc,float('inf')),v+vv)
        all_dp=new
    return all_dp[target]


def run():
    rand=Random(314159)
    checked=0
    for n in range(2,9):
        for case in range(25):
            edges=[(i,j,F(rand.randrange(0,5))) for i in range(n) for j in range(i+1,n) if rand.randrange(3)]
            S=set(rand.sample(range(n),rand.randrange(1,n)))
            u=tuple(F(rand.randrange(-4,5),rand.randrange(1,5)) for _ in range(n))
            x0=(u,F(rand.randrange(-2,3)))
            h=F(rand.randrange(1,5),rand.randrange(2,7))
            p=rand.randrange(1,4)
            for variant in ('S','H'):
                actual,reference=advance_first(x0,h,p,S,edges,variant)
                expected=exact_error(x0,h,p,S,edges,variant)
                assert sub(actual,reference)==expected,(n,case,p,variant,actual,reference,expected)
                checked+=1
    # Small independent enumeration of balanced cuts and tree DP.
    for n in (2,4,6,8):
        for case in range(20):
            forest=[(j,rand.randrange(j),rand.randrange(1,5)) for j in range(1,n) if rand.randrange(4)!=0]
            expected=min(cut_width(set(s),forest) for s in combinations(range(n),n//2))
            assert forest_min_cut(n,forest,n//2)==expected
            checked+=1
    # Connected example has a positive gap and all projection choices accounted for.
    edges=[(0,1,1),(1,2,2),(2,3,1),(0,3,3)]
    h=F(1,3); p=2; d=h**(p+1)
    all_pairs=[]
    for S_t in combinations(range(4),2):
        S=set(S_t)
        actual,ref=advance_first(((F(1),)*4,F(0)),h,p,S,edges,'S')
        dif=sub(actual,ref)
        norm2=sum(a*a for a in dif[0])+dif[1]*dif[1]
        w=cut_width(S,edges)
        assert norm2 == d**4*2+h*h*(2*d+d*d)**2*w*w
        all_pairs.append((w,norm2))
    assert min(all_pairs,key=lambda v:v[0])==min(all_pairs,key=lambda v:v[1])
    print(f'VERIFY_OK: {checked} exact split/modified recurrences and forest cut tests; 6 balanced-projection comparisons')

if __name__=='__main__':
    run()
