"""Independent singleton-characteristic-test implementation for path types.
The bitmask at a state records which depth-k characteristic formulas become
contingent there; all such tests use the actual outgoing neighbours.
"""
def partition(vs):
    mapping={}; out=[]
    for x in vs:
        if x not in mapping:mapping[x]=len(mapping)
        out.append(mapping[x])
    return out
for n,expected in [(2,[2]),(3,[2,4]),(4,[2,4,12,14]),
                   (5,[2,4,14,36,40]),(6,[2,4,14,52,110,122]),
                   (7,[2,4,14,58,172,274,286]),
                   (8,[2,4,14,58,220,504,728,758])]:
    worlds=[(v,i) for v in range(2**n) for i in range(n)]
    ix={s:k for k,s in enumerate(worlds)}
    classes=partition([(v>>i)&1 for v,i in worlds]);got=[len(set(classes))]
    while True:
        signatures=[]
        for j,(v,i) in enumerate(worlds):
            candidates=[classes[ix[v,i-1]]] if i else []
            if i+1<n:candidates.append(classes[ix[v,i+1]])
            # All characteristic singleton tests Delta(theta_c) are true
            # unless two distinct neighbour classes include c.
            failures=0
            for c in set(candidates):
                if len(set(candidates))==2:failures|=1<<c
            signatures.append((classes[j],failures))
        new=partition(signatures)
        if len(set(new))==len(set(classes)):break
        classes=new;got.append(len(set(classes)))
    assert got==expected,(n,got,expected)
    print(n,got)
print('SINGLETON_OK')
