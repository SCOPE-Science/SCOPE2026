"""Standalone arithmetic and dynamical checks of a mass-resolved period-three formula."""
import itertools, math, collections, random

def comps3(n):
    return [(i,j,n-i-j) for i in range(1,n-1) for j in range(1,n-i)]

def mulbox(poly,width,power):
    for _ in range(power):
        out=collections.defaultdict(int)
        for k,v in poly.items():
            for t in range(width): out[k+t]+=v
        poly=dict(out)
    return poly

def prediction(a,b):
    P=collections.defaultdict(int)
    for A in comps3(a):
        for B in comps3(b):
            z=a*b+sum(A[i]*B[i] for i in range(3))
            c=math.factorial(a)*math.factorial(b)
            c=math.factorial(a)*math.factorial(b)
            for v in A: c//=math.factorial(v)
            for v in B: c//=math.factorial(v)
            poly={z:c}
            for i in range(3):
                poly=mulbox(poly,B[(i-1)%3],A[i])
                poly=mulbox(poly,A[(i-1)%3],B[i])
            for k,v in poly.items():P[k]+=v
    H=collections.Counter(P)
    for k,v in P.items():H[4*a*b-a-b-k]+=v
    return dict(H),dict(P)

def update(x,a,b):
    s=sum(v>=b for v in x[:a]);t=sum(v>=a for v in x[a:]);
    return tuple((v+(t-b if v>=b else t)) for v in x[:a])+tuple((v+(s-a if v>=a else s)) for v in x[a:])

def check_full(a,b):
    counts=collections.Counter()
    nd=0
    for x in itertools.product(range(2*b),repeat=a):
        for y in itertools.product(range(2*a),repeat=b):
            cur=x+y
            nxt=update(cur,a,b)
            after=update(update(nxt,a,b),a,b)
            if after==cur and nxt!=cur: counts[sum(cur)]+=1
            nd+=1
    formula,_=prediction(a,b)
    assert dict(counts)==formula,(a,b,counts,formula)
    print('exhaustive',a,b,'states',nd,'period3',sum(counts.values()),'support',sorted(counts),'OK')

def check_formula(a,b):
    H,P=prediction(a,b)
    if min(a,b)<3:
        assert not H
        return
    lo=a*b+a+b-3;hi=2*a*b-a-b; top=3**a-3*2**a+3
    top*=3**b-3*2**b+3
    assert set(P)==set(range(lo,hi+1)),(a,b,sorted(P),lo,hi)
    assert P[hi]==top,(a,b,'boundary',P[hi],top)
    assert set(H)==set(range(lo,hi+1))|set(range(2*a*b,3*a*b-2*a-2*b+4)) # check upper q2 = 3ab-2a-2b+3 ?
    assert sum(H.values())%3==0
    assert all(H.get(k,0)==H.get(4*a*b-a-b-k,0) for k in H)
    print('polynomial',a,b,'terms',len(H),'mass support',min(H),max(H),'sum',sum(H.values()),'OK')

if __name__=='__main__':
    for a,b in [(2,3),(3,2),(3,3),(3,4),(4,3)]: check_full(a,b)
    for a in range(3,8):
        for b in range(3,8):check_formula(a,b)
