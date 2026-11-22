"""Independent direct zero-forcing and slide-graph checks for complements of cycles."""
from itertools import combinations
from collections import deque,Counter


def forcing(n, white):
    # Graph is the complement of a cycle; implement by literal neighbors.
    blue = set(range(n)) - set(white)
    while True:
        newly = set()
        for u in blue:
            target = [v for v in range(n) if v not in blue and v != u
                      and (u-v) % n not in (1,n-1)]
            if len(target) == 1:
                newly.add(target[0])
        if not newly:
            return len(blue) == n
        blue |= newly


def census(n):
    opt = [tuple(w) for w in combinations(range(n),3) if forcing(n,w)]
    assert opt, (n,'no optimum')
    if n>=7:
        assert len(opt)==n*(n-4)
        expected = {w for w in combinations(range(n),3)
                    if any(((a-b)%n in (2,n-2)) for a,b in combinations(w,2))
                    and not any(set(w)=={i,(i+1)%n,(i+2)%n} for i in range(n))}
        assert set(opt)==expected,(n,'characterization')
    if n>=7:
        # n-4 white vertices: 4 white, at least two white neighbors at every blue vertex.
        assert all(not forcing(n,w) for w in combinations(range(n),4))
    at={w:i for i,w in enumerate(opt)}
    nbr=[set() for _ in opt]
    for i,w in enumerate(opt):
        ws=set(w)
        for remove in w:
            for add in range(n):
                if add in ws or (remove-add)%n in (1,n-1):
                    continue
                t=tuple(sorted((ws-{remove})|{add}))
                j=at.get(t)
                if j is not None and j!=i:
                    nbr[i].add(j)
    assert all(i in nbr[j] for i in range(len(opt)) for j in nbr[i])
    edges=sum(map(len,nbr))//2
    seen=set();sizes=[]
    for i in range(len(opt)):
        if i in seen:continue
        reached={i};q=deque([i]);seen.add(i)
        while q:
            v=q.popleft()
            for u in nbr[v]:
                if u not in seen:seen.add(u);reached.add(u);q.append(u)
        sizes.append(len(reached))
    sizes.sort(reverse=True)
    if len(sizes)==1:
        eccentricity=[]
        for src in range(len(opt)):
            D={src:0};q=deque([src])
            while q:
                v=q.popleft()
                for u in nbr[v]:
                    if u not in D:D[u]=D[v]+1;q.append(u)
            assert len(D)==len(opt)
            eccentricity.append(max(D.values()))
        assert set(eccentricity)=={4},(n,Counter(eccentricity))
    if n==6:
        assert (len(opt),edges,sizes)==(14,18,[12,1,1])
    elif n==7:
        assert (len(opt),edges,sizes)==(21,42,[21])
    elif n==8:
        assert (len(opt),edges,sizes)==(32,92,[32])
    else:
        assert (len(opt),edges,sizes)==(n*(n-4),n*(n-6)*(n+3)//2,[n*(n-4)])
    print('n=%d opt=%d slide_edges=%d component_sizes=%s'%(n,len(opt),edges,sizes))


if __name__=='__main__':
    for n in range(6,19):
        census(n)
    print('ALL_DIRECT_SMALL_ORDER_CHECKS_PASS')
