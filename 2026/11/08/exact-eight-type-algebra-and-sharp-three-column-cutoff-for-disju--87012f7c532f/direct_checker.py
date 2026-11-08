"""Independent direct valuation check on labelled two-by-m grids, m=1,2,3."""

def direct(m):
    # States are all pairs (valuation mask, world index) for m columns.
    worlds=2*m
    points=[(v,w) for v in range(1<<worlds) for w in range(worlds)]
    idx={p:i for i,p in enumerate(points)}
    rows={r:tuple(r*m+c for c in range(m)) for r in range(2)}
    cols={c:(c,m+c) for c in range(m)}
    def H(X):
        out=set()
        for i,(v,w) in enumerate(points):
            r,c=divmod(w,m)
            if len({idx[v,j] in X for j in rows[r]})==1 or len({idx[v,j] in X for j in cols[c]})==1:
                out.add(i)
        return frozenset(out)
    p=frozenset(i for i,(v,w) in enumerate(points) if (v>>w)&1)
    a=H(p)
    forms=[p,a,H(a),H(p|a),H(p-a)]
    sigs=[''.join(str(int(i in b)) for b in forms) for i in range(len(points))]
    labels=sorted(set(sigs))
    assert len(labels)=={1:2,2:6,3:8,4:8}[m]
    cells={b:frozenset(i for i in range(len(points)) if sigs[i]==b) for b in labels}
    # Semantic closure: every Boolean union of signature classes is H-closed.
    for mask in range(1<<len(labels)):
        X=frozenset().union(*(cells[b] for j,b in enumerate(labels) if mask>>j&1))
        Y=H(X)
        for b in labels:
            assert cells[b]<=Y or cells[b].isdisjoint(Y)
    depth1=len(set((i in p,i in a) for i in range(len(points))))
    assert depth1 == (2 if m==1 else 4)
    return len(points),len(labels)

for m in (1,2,3,4):
    n,q=direct(m)
    print('DIRECT_OK',m,'columns',n,'pointed instances',q,'atoms')
