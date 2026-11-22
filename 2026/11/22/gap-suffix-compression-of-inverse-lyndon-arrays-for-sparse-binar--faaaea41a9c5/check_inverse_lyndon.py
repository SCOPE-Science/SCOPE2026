"""Reproduce sparse-binary inverse Lyndon array formula, with independent prefix oracle."""
from itertools import product
from random import Random


def build(a0, gaps):
    """Return (start, stop, first_value) segments for lambda inverse on binary text.

    A segment encodes lambda[p] = first_value - (p-start).  Singleton
    segments encode one-symbol starts.  Time O(r log r), space O(r).
    """
    if a0 < 0 or any(x < 0 for x in gaps):
        raise ValueError("gap lengths must be nonnegative")
    r = len(gaps)
    n = a0 + r + sum(gaps)
    if n == 0:
        return []
    if not r:
        return [(0, a0, a0)]

    vals = sorted(set(gaps[:-1]), reverse=True)
    code_of = {g: j+1 for j,g in enumerate(vals)}
    B = [code_of[g] for g in gaps[:-1]] + [0]
    # Prefix-doubling suffix array: stable counting sorts make each round O(r).
    ranks = B[:]
    sa = list(range(r))

    def count_sort(arr, keys, limit):
        cnt = [0]*(limit+1)
        for i in arr:
            cnt[keys[i]] += 1
        s = 0
        for j in range(len(cnt)):
            v = cnt[j]
            cnt[j] = s
            s += v
        out = [0]*len(arr)
        for i in arr:
            j = keys[i]
            out[cnt[j]] = i
            cnt[j] += 1
        return out

    step = 1
    while True:
        bound = max(ranks)+1
        second = [ranks[i+step]+1 if i+step<r else 0 for i in range(r)]
        first = [x+1 for x in ranks]
        sa = count_sort(sa,second,bound)
        sa = count_sort(sa,first,bound)
        newr = [0]*r
        classes = 1
        for z in range(1,r):
            i, j = sa[z-1], sa[z]
            if (ranks[i],second[i]) != (ranks[j],second[j]):
                classes += 1
            newr[j] = classes-1
        ranks = newr
        if classes == r:
            break
        step *= 2
    rank = ranks
    # Kasai adjacent-suffix LCP and iterative segment-tree RMQ.
    adjacent = [0]*(r-1)
    h = 0
    for i in range(r):
        z = rank[i]
        if z == r-1:
            h=0
            continue
        j=sa[z+1]
        while i+h<r and j+h<r and B[i+h]==B[j+h]:
            h+=1
        adjacent[z]=h
        h=max(0,h-1)
    size=1
    while size<len(adjacent):
        size <<= 1
    tree=[r+1]*(2*size)
    tree[size:size+len(adjacent)] = adjacent
    for z in range(size-1,0,-1):
        tree[z]=min(tree[2*z],tree[2*z+1])

    def lcp_suffix(i,j):
        if i==j:return r-i
        lo,hi=sorted((rank[i],rank[j]))
        lo+=size
        hi+=size
        res=r+1
        while lo<hi:
            if lo&1:
                res=min(res,tree[lo]);lo+=1
            if hi&1:
                hi-=1;res=min(res,tree[hi])
            lo//=2; hi//=2
        return res

    ng=[r]*r
    stack=[]
    for i in range(r-1,-1,-1):
        while stack and rank[stack[-1]]<=rank[i]:
            stack.pop()
        if stack:
            ng[i]=stack[-1]
        stack.append(i)

    positions=[0]*r
    pref=[0]*(r+1)
    for i in range(r):
        if i:
            positions[i]=positions[i-1]+1+gaps[i-1]
        else:
            positions[0]=a0
        pref[i+1]=pref[i]+1+gaps[i]
    oneval=[0]*r
    for i in range(r):
        j=ng[i]
        if j==r:
            oneval[i]=n-positions[i]
            continue
        h=lcp_suffix(i,j)
        # A greater later suffix must diverge at two actual integer gaps.
        assert j+h<r-1 and i+h<r-1 and gaps[j+h]<gaps[i+h]
        expanded_lcp=(pref[i+h]-pref[i]) + 1+gaps[j+h]
        oneval[i]=(positions[j]-positions[i])+expanded_lcp

    seg=[]
    if a0:seg.append((0,a0,a0))
    for i in range(r):
        p=positions[i]
        seg.append((p,p+1,oneval[i]))
        t=gaps[i]
        if t:
            seg.append((p+1,p+1+t,t))
    return seg


def expand(segments):
    out=[]
    for a,b,v in segments:
        assert a==len(out)
        out.extend(v-j for j in range(b-a))
    return out


def oracle(w):
    a=[]
    for i in range(len(w)):
        best=1
        for m in range(2,len(w)-i+1):
            u=w[i:i+m]
            if all(u>u[k:] for k in range(1,m)):
                best=m
            else:
                break
        a.append(best)
    return a


def check(a0,g):
    w='0'*a0+''.join('1'+'0'*v for v in g)
    got=expand(build(a0,g))
    want=oracle(w)
    if got!=want:
        raise AssertionError((a0,g,w,got,want))


def main():
    count=0
    for r in range(0,7):
        for a0 in range(5):
            for g in product(range(4),repeat=r):
                if a0+r+sum(g)==0:continue
                check(a0,g);count+=1
    print('exhaustive gap tuples:', count)
    rng=Random(0x23EB)
    for t in range(1500):
        r=rng.randrange(0,20)
        a0=rng.randrange(0,10)
        g=[rng.randrange(0,10) for _ in range(r)]
        if a0+r+sum(g):check(a0,g)
    print('independent random oracle cases:',1500)
    for r in [10,31,127,512,2048]:
        a0=10**8
        g=[rng.randrange(0,10**7) for _ in range(r)]
        seg=build(a0,g)
        n=a0+r+sum(g)
        assert sum(b-a for a,b,v in seg)==n
        assert len(seg)<=2*r+1
        assert all(1<=v<=n-a for a,b,v in seg)
        print('large compressed case r=',r,'n=',n,'segments=',len(seg))
    print('ALL CHECKS PASS')

if __name__=='__main__':
    main()
