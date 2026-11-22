"""Exact bfloat16 graph census of K(x)=(11/2)x(1-x)/(1+x).

Requires Python 3 standard library only. All numerical operations relevant to
successor generation use rational arithmetic; neither checker uses host floats.
"""
from fractions import Fraction as F
from bisect import bisect_left
from collections import deque

def decoded(code):
    assert 0 <= code <= 0x4100
    exponent=(code >> 7)&255
    mantissa=code&127
    if exponent==0:
        return F(mantissa,2**133)
    significand=128+mantissa
    shift=exponent-134
    return F(significand*2**shift) if shift>=0 else F(significand,2**(-shift))

TABLE=tuple(decoded(i) for i in range(0x4101))
STATES=TABLE[:0x3f81]
INDEX={x:i for i,x in enumerate(STATES)}
assert len(STATES)==16257 and len(INDEX)==16257 and STATES[0]==0 and STATES[-1]==1
assert all(TABLE[j]<TABLE[j+1] for j in range(len(TABLE)-1))

def rounding_by_neighbors(x):
    assert 0 <= x <= 8
    upper=bisect_left(TABLE,x)
    if TABLE[upper]==x: return TABLE[upper]
    lower=upper-1
    delta_low=x-TABLE[lower]; delta_high=TABLE[upper]-x
    return TABLE[lower] if delta_low<delta_high or (delta_low==delta_high and lower%2==0) else TABLE[upper]

def exact_floor_log2(x):
    assert x>0
    e=x.numerator.bit_length()-x.denominator.bit_length()
    base=F(2**e) if e>=0 else F(1,2**(-e))
    if x<base: e-=1
    return e

def integer_nearest_ties_to_even(x):
    floor,remainder=divmod(x.numerator,x.denominator)
    twice=2*remainder
    return floor+(twice>x.denominator or (twice==x.denominator and floor%2==1))

def rounding_by_quantum(x):
    if x==0:return F(0)
    e=exact_floor_log2(x)
    quantum_exp=max(e-7,-133)
    quantum=F(2**quantum_exp) if quantum_exp>=0 else F(1,2**(-quantum_exp))
    return quantum*integer_nearest_ties_to_even(x/quantum)

MU=F(11,2)
def once(x,R):return R(MU*x*(1-x)/(1+x))
def staged(x,R):
    a=R(MU*x)
    b=R(1-x)
    c=R(a*b)
    d=R(1+x)
    return R(c/d)

def successor_lists(R):
    once_edges=[]; staged_edges=[]
    for x in STATES:
        p,q=once(x,R),staged(x,R)
        assert p in INDEX and q in INDEX, (x,p,q)
        once_edges.append(INDEX[p]);staged_edges.append(INDEX[q])
    return once_edges,staged_edges

def path_based(edges):
    n=len(edges); group=[-1]*n;distance=[-1]*n;cycle_members=[]
    for v0 in range(n):
        if group[v0]>=0:continue
        seen={};path=[];v=v0
        while group[v]<0 and v not in seen:
            seen[v]=len(path);path.append(v);v=edges[v]
        if v in seen:
            cycle=path[seen[v]:]
            k=len(cycle_members);cycle_members.append(cycle)
            for u in cycle:group[u]=k;distance[u]=0
            before=path[:seen[v]]
        else:before=path
        for u in reversed(before):group[u]=group[edges[u]];distance[u]=distance[edges[u]]+1
    out=[]
    for k,cyc in enumerate(cycle_members):
        out.append((tuple(sorted(cyc)),sum(j==k for j in group),max(distance[i] for i in range(n) if group[i]==k)))
    return sorted(out)

def peel_based(edges):
    n=len(edges)
    indeg=[0]*n
    for v in edges:indeg[v]+=1
    pending=deque(i for i,d in enumerate(indeg) if d==0)
    peeled=[]
    while pending:
        u=pending.popleft();peeled.append(u)
        v=edges[u];indeg[v]-=1
        if indeg[v]==0:pending.append(v)
    grp=[-1]*n;dist=[-1]*n;cycles=[]
    for start in range(n):
        if indeg[start]==0 or grp[start]>=0:continue
        k=len(cycles);cur=start;cy=[]
        while grp[cur]<0:
            grp[cur]=k;dist[cur]=0;cy.append(cur);cur=edges[cur]
        assert cur==start
        cycles.append(cy)
    for u in reversed(peeled):
        v=edges[u];grp[u]=grp[v];dist[u]=dist[v]+1
    return sorted((tuple(sorted(cyc)),sum(g==k for g in grp),max(dist[i] for i in range(n) if grp[i]==k)) for k,cyc in enumerate(cycles))

if __name__=='__main__':
    # Test rounder on all representables and all nearest-neighbor midpoints.
    for i,v in enumerate(TABLE):
        assert rounding_by_quantum(v)==v
        assert rounding_by_neighbors(v)==v
        if i+1<len(TABLE):
            mid=(v+TABLE[i+1])/2
            expected=v if i%2==0 else TABLE[i+1]
            assert rounding_by_quantum(mid)==expected
            assert rounding_by_neighbors(mid)==expected
    first,second=successor_lists(rounding_by_neighbors)
    check_first,check_second=successor_lists(rounding_by_quantum)
    assert first==check_first and second==check_second
    got_a=path_based(first);got_b=path_based(second)
    assert got_a==peel_based(first)
    assert got_b==peel_based(second)
    summary_a=sorted((len(c),basin,maxdepth) for c,basin,maxdepth in got_a)
    summary_b=sorted((len(c),basin,maxdepth) for c,basin,maxdepth in got_b)
    assert summary_a==[(1,2,1),(19,16255,74)],summary_a
    assert summary_b==[(1,2,1),(2,409,53),(6,5958,64),(21,9888,63)],summary_b
    assert sum(p!=q for p,q in zip(first,second))==1371
    assert all(i!=INDEX[0] or first[i]==0 and second[i]==0 for i in range(len(STATES)))
    print('CHECK_OK,states=16257,disagreements=1371')
    for label,records in [('once',got_a),('staged',got_b)]:
        for cycle,basin,depth in sorted(records,key=lambda r:(len(r[0]),r[0][0])):
            print(label,'period',len(cycle),'basin',basin,'maxpreperiod',depth,'codes',','.join(f'{c:04x}' for c in cycle))
