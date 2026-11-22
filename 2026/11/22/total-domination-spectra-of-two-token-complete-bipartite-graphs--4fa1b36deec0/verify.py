#!/usr/bin/env python3
"""Exact verification of total-domination formulas for two-token bicliques.
All calculations are integer-exact and require Python 3 standard library only.
"""
from math import comb, factorial, ceil
from itertools import combinations


def add(a, b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def binpow(n): return [comb(n,i) for i in range(n+1)]

def surj_rect(a,b):
    """Weighted nonempty-row and nonempty-column a-by-b binary matrices."""
    out=[0]*(a*b+1)
    for i in range(a+1):
        for j in range(b+1):
            sign=(-1)**(i+j)*comb(a,i)*comb(b,j)
            for k,c in enumerate(binpow((a-i)*(b-j))):out[k]+=sign*c
    return out

def cross_poly(r,m):
    out=[0]*(r*m+1)
    for a in (r-1,r):
        for b in (m-1,m):
            f=surj_rect(a,b)
            mult=comb(r,a)*comb(m,b)
            for i,x in enumerate(f):out[i]+=mult*x
    return out

def edgecover(n):
    count=comb(n,2)
    out=[0]*(count+1)
    for j in range(n+1):
        mult=(-1)**j*comb(n,j)
        for k,x in enumerate(binpow(comb(n-j,2))):out[k]+=mult*x
    return out

def shore_poly(r,m):
    er,em=edgecover(r),edgecover(m)
    p=mul(er,binpow(comb(m,2)))
    q=mul(em,binpow(comb(r,2)))
    sub=mul(er,em)
    out=add(p,q)
    for i,x in enumerate(sub):out[i]-=x
    return out

def full_poly(r,m):return mul(cross_poly(r,m),shore_poly(r,m))

def E(n):
    if n%2==0:
        k=n//2
        return factorial(n)//(2**k*factorial(k))
    k=(n-1)//2
    return n*comb(n-1,2)*factorial(n-3)//(2**(k-1)*factorial(k-1))

def stirling(n,k):
    if n<k or k<0:return 0
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for a in range(1,n+1):
        for b in range(1,min(a,k)+1):dp[a][b]=dp[a-1][b-1]+b*dp[a-1][b]
    return dp[n][k]

def min_count(r,m):
    a=m*factorial(r)*(stirling(m-1,r-1)+stirling(m-1,r))
    b=E(r)+(E(m) if ceil(m/2)==ceil(r/2) else 0)
    return a*b


def direct_parts(r,m):
    """Independent combinatorial enumeration using actual selected vertices of F2(Krm)."""
    f=[0]*(r*m+1)
    for mask in range(1<<(r*m)):
        rows=cols=0
        for i in range(r):
            for j in range(m):
                if (mask>>(i*m+j))&1:
                    rows|=1<<i;cols|=1<<j
        if rows.bit_count()>=r-1 and cols.bit_count()>=m-1:
            f[mask.bit_count()]+=1
    lp=list(combinations(range(r),2))
    rp=list(combinations(range(m),2))
    b=[0]*(len(lp)+len(rp)+1)
    for mask in range(1<<(len(lp)+len(rp))):
        left=right=0
        for i,(a,c) in enumerate(lp):
            if (mask>>i)&1:left|=(1<<a)|(1<<c)
        for i,(a,c) in enumerate(rp):
            if (mask>>(i+len(lp)))&1:right|=(1<<a)|(1<<c)
        if left.bit_count()==r or right.bit_count()==m:b[mask.bit_count()]+=1
    return f,b


def brute_full(r,m):
    """No bipartite-factor assumption: independently build F2 and test neighborhoods."""
    n=r+m
    pairs=list(combinations(range(n),2))
    pindex={v:i for i,v in enumerate(pairs)}
    adj=[0]*len(pairs)
    for i,p in enumerate(pairs):
        for j,q in enumerate(pairs):
            if i==j:continue
            x=list(set(p)^set(q))
            if len(x)==2 and ((x[0]<r)!=(x[1]<r)):
                adj[i]|=1<<j
    out=[0]*(len(pairs)+1)
    for mask in range(1<<len(pairs)):
        if all(adj[v]&mask for v in range(len(pairs))):out[mask.bit_count()]+=1
    return out


from functools import lru_cache

@lru_cache(None)
def star_forest(p,q):
    # Polynomial for bipartite spanning star forests on p+q labelled vertices.
    if p==q==0:return [1]
    if not p or not q:return [0]
    out=[0]*(p*q+1)
    for b in range(1,q+1):
        for k,v in enumerate(star_forest(p-1,q-b)):
            out[k+b]+=comb(q,b)*v
    for a in range(2,p+1):
        for k,v in enumerate(star_forest(p-a,q-1)):
            out[k+a]+=q*comb(p-1,a-1)*v
    return out

def minimal_cross(r,m):
    p=star_forest(r-1,m-1)
    out=[r*m*v for v in p]
    term=m*factorial(r)*stirling(m-1,r)
    if len(out)<=m-1:out.extend([0]*(m-len(out)))
    out[m-1]+=term
    term=r*factorial(m)*stirling(r-1,m)
    if len(out)<=r-1:out.extend([0]*(r-len(out)))
    out[r-1]+=term
    return out

def minimal_edgecover(n):
    # The inclusion-minimal edge covers of K_n are disjoint unions of stars.
    # Enumerate with exact recursion; an edge component K_2 has one center choice.
    @lru_cache(None)
    def go(k):
        if k==0:return [1]
        out=[0]*(comb(n,2)+1)
        for s in range(2,k+1):
            centers=1 if s==2 else s
            for i,c in enumerate(go(k-s)):
                if c:out[i+s-1]+=comb(k-1,s-1)*centers*c
        return out
    return go(n)

def minimal_poly(r,m):return mul(minimal_cross(r,m),add(minimal_edgecover(r),minimal_edgecover(m)))

def minimal_direct(parts, r,m):
    # Enumerate all inclusionwise minimal feasible members of one bipartition.
    cross=(parts=='cross')
    E= [(i,j) for i in range(r) for j in range(m)] if cross else list(combinations(range(r),2))+list(combinations(range(m),2))
    offset=comb(r,2)
    hist=[0]*(len(E)+1)
    for mask in range(1<<len(E)):
        if cross:
            rows=cols=0
            for k,(i,j) in enumerate(E):
                if mask>>k&1:rows|=1<<i;cols|=1<<j
            ok=rows.bit_count()>=r-1 and cols.bit_count()>=m-1
        else:
            rows=cols=0
            for k,(i,j) in enumerate(E):
                if mask>>k&1:
                    if k<offset:rows|=(1<<i)|(1<<j)
                    else:cols|=(1<<i)|(1<<j)
            ok=rows.bit_count()==r or cols.bit_count()==m
        if not ok:continue
        for k in range(len(E)):
            if mask>>k&1:
                masked=mask&~(1<<k)
                if cross:
                    rr=cc=0
                    for h,(i,j) in enumerate(E):
                        if masked>>h&1:rr|=1<<i;cc|=1<<j
                    good=rr.bit_count()>=r-1 and cc.bit_count()>=m-1
                else:
                    rr=cc=0
                    for h,(i,j) in enumerate(E):
                        if masked>>h&1:
                            if h<offset:rr|=1<<i|1<<j
                            else:cc|=1<<i|1<<j
                    good=rr.bit_count()==r or cc.bit_count()==m
                if good:break
        else:hist[mask.bit_count()]+=1
    return hist

def main():
    for r,m in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        f,b=direct_parts(r,m)
        assert f==cross_poly(r,m),('cross',r,m)
        assert b==shore_poly(r,m),('shore',r,m)
        pred=full_poly(r,m)
        assert pred==mul(f,b)
        min_size=next(i for i,v in enumerate(pred) if v)
        assert min_size==m-1+ceil(r/2)
        assert pred[min_size]==min_count(r,m)
        if r+m<=6:
            actual=brute_full(r,m)
            assert actual==pred,('entire graph',r,m)
        if r<=4 and m<=4:
            assert minimal_cross(r,m)==minimal_direct('cross',r,m)[:len(minimal_cross(r,m))] and not any(minimal_direct('cross',r,m)[len(minimal_cross(r,m)):]), ('mincross',r,m)
            me=add(minimal_edgecover(r),minimal_edgecover(m))
            de=minimal_direct('shore',r,m)
            assert me==de[:len(me)] and not any(de[len(me):]), ('minshore',r,m)
        print(f'CASE_K_{r}_{m} degree={len(pred)-1} minimum={min_size} multiplicity={pred[min_size]} all={sum(pred)} minimal_count={sum(minimal_poly(r,m))} PASS')
    print('INDEPENDENT_FULL_TOKEN_GRAPH_ENUMERATION_K_2_2_K_2_3_K_2_4_K_3_3 PASS')
    print('DIRECT_SHORE_AND_CROSS_ENUMERATION_THROUGH_K_4_4 PASS')
    print('INCLUSION_MINIMAL_ENUMERATION_AND_STAR_FOREST_RECURRENCE_THROUGH_K_4_4 PASS')
    print('VERIFY_OK')

if __name__=='__main__':main()
