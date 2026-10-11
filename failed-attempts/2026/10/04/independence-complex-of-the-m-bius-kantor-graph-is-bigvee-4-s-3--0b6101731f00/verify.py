#!/usr/bin/env python3
from collections import Counter, defaultdict, deque

N = 16
# Vertices 0..7 are u_0..u_7, vertices 8..15 are v_0..v_7.
ORDER = [13,5,1,7,15,0,12,14,4,2,10,11,3,8,9,6]
EXPECTED_F = [16,96,272,376,240,72,16,2]
EXPECTED_CRIT = {0:1, 3:4, 4:1}
EXPECTED_PATH_COUNTS = [2,0,2,2]
EXPECTED_RANKS = [1,15,81,191,181,58,14,2]


def mk_graph():
    edges=set()
    n=8
    for i in range(n):
        edges.add(tuple(sorted((i,(i+1)%n))))
        edges.add(tuple(sorted((i,n+i))))
        edges.add(tuple(sorted((n+i,n+((i+3)%n)))))
    return edges


def consecutive_bipartite_8_3():
    edges=set()
    for i in range(8):
        for s in (0,1,2):
            edges.add(tuple(sorted((i,8+((i+s)%8)))))
    return edges


def adjacency(edges):
    adj=[0]*N
    for a,b in edges:
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    return adj


def girth(edges):
    nbr=[[] for _ in range(N)]
    for a,b in edges:
        nbr[a].append(b); nbr[b].append(a)
    best=10**9
    for s in range(N):
        dist=[-1]*N; parent=[-1]*N
        dist[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in nbr[u]:
                if dist[v] < 0:
                    dist[v]=dist[u]+1; parent[v]=u; q.append(v)
                elif parent[u] != v:
                    best=min(best,dist[u]+dist[v]+1)
    return best


def independent_faces(adj):
    by_size=[[] for _ in range(N+1)]
    for m in range(1<<N):
        ok=True
        mm=m
        while mm:
            l=mm & -mm
            i=l.bit_length()-1
            mm -= l
            if adj[i] & m:
                ok=False; break
        if ok:
            by_size[m.bit_count()].append(m)
    return by_size


def sequential_matching(nonempty_faces):
    unmatched=set(nonempty_faces)
    pairs=[]
    pair_of={}
    for stage,v in enumerate(ORDER):
        bit=1<<v
        for m in sorted(list(unmatched)):
            u=m|bit
            if not (m&bit) and u in unmatched:
                unmatched.remove(m); unmatched.remove(u)
                pairs.append((m,u,stage,v))
                pair_of[m]=u; pair_of[u]=m
    return pairs, unmatched, pair_of


def verify_acyclic(nonempty_faces,pairs):
    matched={(lo,hi) for lo,hi,_,_ in pairs}
    out=defaultdict(list); indeg={m:0 for m in nonempty_faces}
    fset=set(nonempty_faces)
    for hi in nonempty_faces:
        if hi.bit_count() < 2:
            continue
        mm=hi
        while mm:
            l=mm & -mm; mm-=l
            lo=hi^l
            if lo==0 or lo not in fset:
                continue
            if (lo,hi) in matched:
                out[lo].append(hi); indeg[hi]+=1
            else:
                out[hi].append(lo); indeg[lo]+=1
    q=deque([u for u,d in indeg.items() if d==0]); seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert seen==len(nonempty_faces), (seen,len(nonempty_faces))
    return out


def rank_mod_p(columns, row_index, p):
    basis={}
    rank=0
    for m in columns:
        vec={}
        vs=[i for i in range(N) if (m>>i)&1]
        for pos,v in enumerate(vs):
            r=row_index[m^(1<<v)]
            a=1 if pos%2==0 else (p-1)
            vec[r]=(vec.get(r,0)+a)%p
            if vec[r]==0: del vec[r]
        while vec:
            piv=max(vec)
            if piv not in basis:
                inv=pow(vec[piv],-1,p)
                vec={i:(a*inv)%p for i,a in vec.items() if (a*inv)%p}
                basis[piv]=vec; rank+=1; break
            b=basis[piv]; c=vec[piv]
            for i,a in b.items():
                nv=(vec.get(i,0)-c*a)%p
                if nv: vec[i]=nv
                elif i in vec: del vec[i]
    return rank


def boundary_ranks(by_size,p):
    ranks=[1]  # augmented boundary from vertices to the empty face
    maxk=max(i for i,x in enumerate(by_size) if x)
    for k in range(2,maxk+1):
        rows={m:i for i,m in enumerate(by_size[k-1])}
        ranks.append(rank_mod_p(by_size[k],rows,p))
    return ranks


def reduced_betti(by_size,ranks):
    maxk=max(i for i,x in enumerate(by_size) if x)
    b={}
    for k in range(1,maxk+1):
        rd=ranks[k-1]
        rim=ranks[k] if k<maxk else 0
        val=len(by_size[k])-rd-rim
        if val:b[k-1]=val
    return b


def path_counts(nonempty_faces,pairs,critical):
    matched={(lo,hi) for lo,hi,_,_ in pairs if lo.bit_count()==4 and hi.bit_count()==5}
    highs=[m for m in nonempty_faces if m.bit_count()==5]
    lows=[m for m in nonempty_faces if m.bit_count()==4]
    out=defaultdict(list)
    for hi in highs:
        mm=hi
        while mm:
            l=mm & -mm; mm-=l
            lo=hi^l
            if (lo,hi) in matched: out[lo].append(hi)
            else: out[hi].append(lo)
    src=[m for m in critical if m.bit_count()==5]
    tgt=sorted(m for m in critical if m.bit_count()==4)
    assert len(src)==1 and len(tgt)==4
    src=src[0]
    reach={src}; stack=[src]
    while stack:
        u=stack.pop()
        for v in out[u]:
            if v not in reach:
                reach.add(v); stack.append(v)
    indeg={u:0 for u in reach}
    for u in reach:
        for v in out[u]:
            if v in indeg: indeg[v]+=1
    q=deque([u for u,d in indeg.items() if d==0]); topo=[]
    while q:
        u=q.popleft(); topo.append(u)
        for v in out[u]:
            if v in indeg:
                indeg[v]-=1
                if indeg[v]==0:q.append(v)
    assert len(topo)==len(reach)
    cnt=defaultdict(int); cnt[src]=1
    for u in topo:
        for v in out[u]:
            if v in reach: cnt[v]+=cnt[u]
    return [cnt[t] for t in tgt], src, tgt


def fmt_face(m):
    return [i for i in range(N) if (m>>i)&1]


def main():
    edges=mk_graph()
    assert len(edges)==24
    assert girth(edges)==6
    g83=consecutive_bipartite_8_3()
    assert len(g83)==24
    assert (0,9) in g83 and (7,9) in g83 and (7,8) in g83 and (0,8) in g83
    assert girth(g83)==4

    adj=adjacency(edges)
    by_size=independent_faces(adj)
    f=[len(by_size[k]) for k in range(1,9)]
    assert f==EXPECTED_F, f
    assert sum(f)==1090

    nonempty=[m for k in range(1,9) for m in by_size[k]]
    pairs,critical,pair_of=sequential_matching(nonempty)
    assert len(pairs)==542
    cc=Counter(m.bit_count()-1 for m in critical)
    assert dict(cc)==EXPECTED_CRIT, cc
    verify_acyclic(nonempty,pairs)

    pc,src,tgt=path_counts(nonempty,pairs,critical)
    assert pc==EXPECTED_PATH_COUNTS, pc
    assert max(pc)<=2

    for p in (2,3):
        ranks=boundary_ranks(by_size,p)
        assert ranks==EXPECTED_RANKS, (p,ranks)
        betti=reduced_betti(by_size,ranks)
        assert betti=={3:4,4:1}, (p,betti)

    # The Morse differential from the unique critical 4-cell to the four
    # critical 3-cells is an integral vector. Each coordinate is a signed
    # sum over gradient paths, so its absolute value is bounded by 2.
    # Since H_4 over F_2 and F_3 is one-dimensional and the Morse C_4 is
    # one-dimensional, that differential vanishes mod 2 and mod 3.
    # Hence every coefficient is divisible by 6 and has absolute value <=2,
    # forcing the integral differential to be zero.
    print('MK_INDEPENDENCE_VERIFY_OK')
    print('f_vector=',f)
    print('critical=',dict(sorted(cc.items())))
    print('critical_4_face=',fmt_face(src))
    print('critical_3_faces=',[fmt_face(x) for x in tgt])
    print('gradient_path_counts=',pc)
    print('mod2_mod3_reduced_betti={3:4,4:1}')
    print('girth_MK=6 girth_G8^3=4')

if __name__=='__main__':
    main()
