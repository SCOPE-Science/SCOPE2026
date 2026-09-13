"""Exact disc / herdisc of AP family for small N."""
import itertools

def ap_sets(N):
    # vertices 0..N-1; sets = all contiguous APs {a+id : i=0..k-1} subset of [N], k>=1
    S=set()
    for a in range(N):
        for d in range(1,N):
            # max length
            k=1
            while a+(k-1)*d < N:
                tup=tuple(a+i*d for i in range(k))
                S.add(tup)
                k+=1
    # singletons already included (d arbitrary, k=1) but ensure
    for a in range(N):
        S.add((a,))
    return list(S)

def disc_of_family_on_J(sets, J):
    # sets: list of tuples over 0..N-1; J: tuple/list of vertices
    # restrict: S cap J, drop empty
    idx={v:i for i,v in enumerate(J)}
    m=len(J)
    if m==0:
        return 0
    R=[]
    seen=set()
    for s in sets:
        t=tuple(v for v in s if v in idx)
        if t and t not in seen:
            seen.add(t)
            R.append([idx[v] for v in t])
    best=10**9
    for bits in itertools.product((-1,1), repeat=m):
        mx=0
        for r in R:
            s=sum(bits[i] for i in r)
            a=abs(s)
            if a>mx:
                mx=a
                if mx>=best:
                    break
        if mx<best:
            best=mx
            if best==0:
                break
    return best

def herdisc(N):
    sets=ap_sets(N)
    best=0
    worst=[]
    for mask in range(1<<N):
        J=[i for i in range(N) if mask>>i &1]
        d=disc_of_family_on_J(sets,J)
        if d>best:
            best=d
            worst=[J]
        elif d==best:
            worst.append(J)
    # ordinary disc = J full
    full=disc_of_family_on_J(sets,list(range(N)))
    return full,best,worst[:5],len(sets)

for N in range(2,11):
    full,her,_ex,nsets=herdisc(N)
    print(f"N={N} nsets={nsets} disc={full} herdisc={her} ex={_ex}", flush=True)
