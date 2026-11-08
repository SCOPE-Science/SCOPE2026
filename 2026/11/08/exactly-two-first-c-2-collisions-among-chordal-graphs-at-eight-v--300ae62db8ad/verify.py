"""Exact small-order C2 census of chordal graphs; Python 3 standard library."""
from collections import Counter, defaultdict
from itertools import combinations


def degree(g, v):
    return g[v].bit_count()


def edges(g):
    return sum(x.bit_count() for x in g) // 2


def add_clique_vertex(g, clique):
    n = len(g)
    return tuple(g[v] | ((1 << n) if (clique >> v) & 1 else 0)
                 for v in range(n)) + (clique,)


def is_clique(g, mask):
    for v in range(len(g)):
        if (mask >> v) & 1 and (g[v] & mask) != mask ^ (1 << v):
            return False
    return True


def vertex_signature(g, v):
    degs = tuple(x.bit_count() for x in g)
    return (degs[v], tuple(sorted(degs[w] for w in range(len(g))
                                  if (g[v] >> w) & 1)))


def invariant(g):
    return tuple(sorted(vertex_signature(g, v) for v in range(len(g))))


def isomorphic(g, h):
    n = len(g)
    if n != len(h) or edges(g) != edges(h) or invariant(g) != invariant(h):
        return False
    signatures_g = [vertex_signature(g,v) for v in range(n)]
    signatures_h = [vertex_signature(h,v) for v in range(n)]
    if Counter(signatures_g) != Counter(signatures_h):
        return False
    candidates = [[j for j in range(n) if signatures_g[v] == signatures_h[j]]
                  for v in range(n)]
    order = sorted(range(n),key=lambda v:(len(candidates[v]),-degree(g,v)))
    mapping = [-1]*n
    def recurse(depth,used):
        if depth==n:
            return True
        v=order[depth]
        for w in candidates[v]:
            if (used >> w) & 1:
                continue
            if all(bool(g[v] & (1 << u)) == bool(h[w] & (1 << mapping[u]))
                   for u in order[:depth]):
                mapping[v]=w
                if recurse(depth+1,used | (1 << w)):
                    return True
                mapping[v]=-1
        return False
    return recurse(0,0)


def is_connected(g):
    reached=1
    while True:
        nxt=reached
        for v in range(len(g)):
            if (reached >> v)&1:
                nxt |= g[v]
        if nxt==reached:
            return reached==(1<<len(g))-1
        reached=nxt


def disjoint_union(g,h):
    k=len(g)
    return g + tuple(row << k for row in h)


def graph6(g):
    n=len(g)
    bits=[(g[i]>>j)&1 for j in range(1,n) for i in range(j)]
    while len(bits)%6:
        bits.append(0)
    return chr(n+63)+''.join(chr(63+sum(bits[t+i]<<(5-i) for i in range(6))) for t in range(0,len(bits),6))


def from_graph6(s):
    n=ord(s[0])-63
    bits=[]
    for c in s[1:]:bits.extend((ord(c)-63>>j)&1 for j in range(5,-1,-1))
    g=[0]*n; pos=0
    for j in range(1,n):
        for i in range(j):
            if bits[pos]:g[i]|=1<<j;g[j]|=1<<i
            pos+=1
    return tuple(g)


def color_histograms(graphs):
    colors=[[0]*len(g) for g in graphs]
    for round in range(18):
        keys=[]
        for g,col in zip(graphs,colors):
            keys.append([(col[v],tuple(sorted(col[w] for w in range(len(g))
                              if (g[v] >> w)&1))) for v in range(len(g))])
        palette={key:i for i,key in enumerate(sorted({x for row in keys for x in row}))}
        new=[[palette[x] for x in row] for row in keys]
        if new==colors:
            break
        colors=new
    return [tuple(sorted(Counter(row).items())) for row in colors]


def is_split(g):
    n=len(g)
    for mask in range(1<<n):
        if is_clique(g,mask):
            rem=((1<<n)-1)^mask
            if all((g[v]&rem)==0 for v in range(n) if (rem>>v)&1):return True
    return False


def remove_vertex(g,v):
    active=[i for i in range(len(g)) if i!=v]
    return tuple(sum((1<<j) for j,w in enumerate(active) if (g[i]>>w)&1) for i in active)


def is_two_tree(g):
    n=len(g)
    if n<3:return False
    if n==3:return edges(g)==3
    for v in range(n):
        if degree(g,v)==2 and is_clique(g,g[v]) and is_two_tree(remove_vertex(g,v)):
            return True
    return False


def degree_quotient(g):
    ds=sorted({degree(g,v) for v in range(len(g))})
    rows=[]
    for d in ds:
        v=next(v for v in range(len(g)) if degree(g,v)==d)
        rows.append(tuple(sum(1 for w in range(len(g)) if (g[v]>>w)&1 and degree(g,w)==e) for e in ds))
        assert all(tuple(sum(1 for w in range(len(g)) if (g[u]>>w)&1 and degree(g,w)==e) for e in ds)==rows[-1]
                   for u in range(len(g)) if degree(g,u)==d)
    return tuple(rows)


def compute():
    connected={1:[(0,)]}
    all_graphs={}
    expected_conn=[0,1,1,2,5,15,58,272,1614]
    expected_all=[0,1,2,4,10,27,94,393,2119]
    for n in range(2,9):
        previous=connected[n-1]
        buckets=defaultdict(list)
        for g in previous:
            for mask in range(1,1<<(n-1)):
                if not is_clique(g,mask):
                    continue
                h=add_clique_vertex(g,mask)
                key=invariant(h)
                if not any(isomorphic(h,k) for k in buckets[key]):
                    buckets[key].append(h)
        connected[n]=[g for row in buckets.values() for g in row]
        assert len(connected[n])==expected_conn[n], (n,len(connected[n]))
    for n in range(1,9):
        output=[]
        def make(remaining,lower,blocks):
            if remaining==0:
                graph=(0,)
                if blocks:
                    graph=blocks[0]
                    for block in blocks[1:]:graph=disjoint_union(graph,block)
                output.append(graph)
                return
            for k in range(1,remaining+1):
                for index, g in enumerate(connected[k]):
                    if (k,index)>=lower:
                        make(remaining-k,(k,index),blocks+(g,))
        make(n,(1,0),())
        assert len(output)==expected_all[n],(n,len(output))
        all_graphs[n]=output
        hist=color_histograms(output)
        eq=defaultdict(list)
        for j, h in enumerate(hist):eq[h].append(j)
        exceptions=[group for group in eq.values() if len(group)>1]
        if n<=7:assert not exceptions,(n,exceptions)
        else:
            assert sorted(len(g) for g in exceptions)==[2,2],exceptions
            assert all(is_connected(output[j]) for group in exceptions for j in group)
            assert sorted(edges(output[group[0]]) for group in exceptions)==[13,14]
            for group in exceptions:
                a,b=(output[i] for i in group)
                assert not isomorphic(a,b)
                assert edges(a)==edges(b)
                if edges(a)==13:
                    assert is_two_tree(a) and is_two_tree(b)
                    assert not is_split(a) and not is_split(b)
                    assert degree_quotient(a)==degree_quotient(b)==((0,1,1),(2,0,2),(2,2,1))
                    known=('G}pOgg','G}TdC_')
                else:
                    assert is_split(a) and is_split(b)
                    assert degree_quotient(a)==degree_quotient(b)==((0,2),(2,3))
                    known=('G}r`HG','G}VSGg')
                assert (isomorphic(a,from_graph6(known[0])) and isomorphic(b,from_graph6(known[1]))) or (isomorphic(a,from_graph6(known[1])) and isomorphic(b,from_graph6(known[0])))
            print('EXCEPTIONS',[(edges(output[group[0]]),len(group)) for group in exceptions])
        print('CENSUS',n,'connected',len(connected[n]),'all',len(output),'C2_classes',len(eq),'exceptional_classes',len(exceptions))
    print('VERIFY_OK')

if __name__=='__main__':compute()
