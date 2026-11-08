"""Exact count of cyclic universal height-words for weak orders; stdlib only."""
from itertools import product
from math import factorial, prod
from collections import Counter

TARGET = {
 2: (1, 1, 1, 1),
 3: (3, 2, 4, 8),
 4: (13, 37908, 2985984, 113192681472),
 5: (75, 27571102170646823740986252600397906575360,
     225390057412667141559249255183922002204556655201227127499578671104,
     6214252301172599252248681937277855126085721393995382376959963220030028306692926790213752299261892430397440),
}

def height_words(n):
    return [w for w in product(range(n), repeat=n)
            if set(w) == set(range(max(w) + 1))]

def reduced(n):
    words = height_words(n)
    incoming = Counter()
    outgoing = {}
    for w in words:
        u, v = w[:-1], w[1:]
        outgoing.setdefault(u, []).append((v, w))
        incoming[v] += 1
    assert all(incoming[u] == len(es) for u,es in outgoing.items())
    core = tuple(sorted(v for v, es in outgoing.items() if len(es)>1))
    assert core == tuple(height_words(n-1))
    core_idx = {u:i for i,u in enumerate(core)}
    adj = [[0]*len(core) for _ in core]
    reduced_labels=[]
    for u in core:
        for v, e in outgoing[u]:
            path=[e]
            while v not in core_idx:
                assert len(outgoing[v]) == 1
                v, edge = outgoing[v][0]
                path.append(edge)
                assert len(path) <= n
            adj[core_idx[u]][core_idx[v]] += 1
            reduced_labels.append((u,v,tuple(path)))
    assert sum(len(path) for _,_,path in reduced_labels) == len(words)
    assert {w for _,_,path in reduced_labels for w in path}==set(words)
    assert all(sum(adj[i])==len(outgoing[u]) for i,u in enumerate(core))
    return core, adj, outgoing, reduced_labels, len(words)

def bareiss_determinant(matrix):
    """Exact fraction-free elimination, no external computer algebra."""
    a = [row[:] for row in matrix]
    m=len(a)
    if not m: return 1
    pivot_prev=1
    sign=1
    for k in range(m-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,m) if a[j][k]),None)
            if j is None: return 0
            a[k],a[j]=a[j],a[k]
            sign=-sign
        p=a[k][k]
        for i in range(k+1,m):
            for j in range(k+1,m):
                q=a[i][j]*p-a[i][k]*a[k][j]
                assert q % pivot_prev == 0
                a[i][j]=q//pivot_prev
            a[i][k]=0
        pivot_prev=p
    return sign*a[-1][-1]

def invariant(n):
    core,adj,outgoing,paths,edges=reduced(n)
    d=[len(outgoing[u]) for u in core]
    lap=[[((d[i] if i==j else 0)-adj[i][j]) for j in range(len(core))]
         for i in range(len(core))]
    tau=bareiss_determinant([row[1:] for row in lap[1:]])
    fact=prod(factorial(x-1) for x in d)
    return len(core),tau,fact,tau*fact,len(paths),edges,tuple(sorted(Counter(d).items()))

if __name__=='__main__':
    for n in TARGET:
        v,t,p,count,short,edges,degree_hist=invariant(n)
        assert (v,t,p,count) == TARGET[n]
        print('n',n,'core',v,'tau',t,'factorial',p,'universal_cycles',count,
              'reduced_edges',short,'original_edges',edges,'degree_histogram',degree_hist)
    from pathlib import Path
    cert = Path(__file__).with_name("core_edges_n5.tsv").read_text(encoding="utf-8").splitlines()
    assert cert[0] == "source\tdestination\tpath_words"
    core,adj,out,paths,edges = reduced(5)
    expected = ["".join(map(str,u))+"\t"+"".join(map(str,v))+"\t"+
                ",".join("".join(map(str,w)) for w in path)
                for u,v,path in paths]
    assert cert[1:] == expected
    assert len(cert)==309
    print('VERIFY_OK')
