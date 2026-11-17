"""Independent finite checks for exact total-matching polytope diameters."""
from math import comb, factorial


def falling(n, k):
    return factorial(n)//factorial(n-k) if 0 <= k <= n else 0


def formula_count(p, q):
    assert 2 <= p < q
    if q >= 2*p:
        return factorial(q)//factorial(q-2*p) * 2**(q-2*p)//2
    oriented=0
    for a in range(p+1):
        for b in range(p+1):
            t=a+b-q
            if not 0<=t<=min(a,b):
                continue
            choose=factorial(q)//(factorial(t)*factorial(q-a)*factorial(q-b))
            ways=sum((-1)**s*comb(t,s)*falling(p,a)*falling(p-s,b-s)
                     for s in range(t+1))
            oriented += choose*ways
    assert oriented % 2==0
    return oriented//2


def exhaustive(p, q):
    n=p+q
    edges=[(i,p+j) for i in range(p) for j in range(q)]
    N=n+len(edges)
    forbidden=[0]*N
    for u in range(N):
        for v in range(u+1,N):
            bad=(u<n and v<n and ((u<p)!=(v<p))) or (u<n and v>=n and u in edges[v-n]) or (u>=n and v>=n and bool(set(edges[u-n]) & set(edges[v-n])))
            if bad:
                forbidden[u] |= 1<<v
                forbidden[v] |= 1<<u
    matchings=[]
    def generate(i, mask):
        if i==N:
            matchings.append(mask)
            return
        generate(i+1,mask)
        if not (mask & forbidden[i]):
            generate(i+1,mask | (1<<i))
    generate(0,0)
    best=-1;count=0
    for i,v in enumerate(matchings):
        for w in matchings[i+1:]:
            squared=(v^w).bit_count()
            if squared>best:
                best=squared;count=1
            elif squared==best:
                count+=1
    expected=q+min(q,2*p)
    assert (best,count)==(expected,formula_count(p,q)),(p,q,best,count,expected,formula_count(p,q))
    for i,v in enumerate(matchings):
        for w in matchings[i+1:]:
            if (v^w).bit_count()!=best:
                continue
            assert not (v&w)
            assert not (v & ((1<<p)-1)) and not (w & ((1<<p)-1))
            # Edges are actually indexed left-major; compute endpoint sets directly.
            R1={j for a in range(p) for j in range(q) if (v>>(n+a*q+j))&1}
            R2={j for a in range(p) for j in range(q) if (w>>(n+a*q+j))&1}
            x1={j for j in range(q) if (v>>(p+j))&1}
            x2={j for j in range(q) if (w>>(p+j))&1}
            if q>=2*p:
                assert len(R1)==len(R2)==p and not(R1&R2)
                assert x1==R2-R1 | (x1-(R1|R2))
                assert x2==R1-R2 | (x2-(R1|R2))
                assert (x1|x2)==set(range(q))
            else:
                assert R1|R2==set(range(q))
                assert x1==R2-R1 and x2==R1-R2
    return len(matchings),best,count


def witness(p, q):
    assert 2<=p<q
    # First matching uses first p distinct right nodes.
    # Second matching uses next p nodes if possible, otherwise the last p.
    R1=list(range(p))
    R2=list(range(q-p,q))
    if q>=2*p: R2=list(range(p,2*p))
    m1={(i,j) for i,j in enumerate(R1)}
    # Search simple shifts for a second injection that avoids edges of m1.
    m2=None
    for shift in range(p):
        cand={((i+shift)%p,j) for i,j in enumerate(R2)}
        if cand.isdisjoint(m1):m2=cand;break
    assert m2 is not None
    touched1={j for _,j in m1}; touched2={j for _,j in m2}
    right1=touched2-touched1
    right2=touched1-touched2
    for j in range(q):
        if j not in touched1|touched2:
            right1.add(j)
    # 2 colors: each contains its own edges and only right vertices uncovered by its edges.
    assert not (right1&touched1) and not (right2&touched2)
    assert right1.isdisjoint(right2) and m1.isdisjoint(m2)
    dist2=len(m1)+len(m2)+len(right1)+len(right2)
    assert dist2 == q+min(q,2*p), (p,q,dist2)
    return dist2


if __name__=='__main__':
    checked=[]
    for p,q in [(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)]:
        n,diam,cnt=exhaustive(p,q)
        checked.append((p,q,n,diam,cnt))
    for p in range(2,25):
        for q in range(p+1,70):
            witness(p,q)
    for p in range(2,16):
        for q in range(p+1,3*p+1):
            assert formula_count(p,q)>0
    print('TOTAL_MATCHING_DIAMETER_PASS exhaustive='+repr(checked)+' witnesses=1288')
