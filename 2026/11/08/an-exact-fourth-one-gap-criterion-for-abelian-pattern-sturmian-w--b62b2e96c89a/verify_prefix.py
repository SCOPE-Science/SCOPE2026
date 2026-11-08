"""Independent finite checks of the four-point sum-graph cycle criterion.
No infinite-word statement is inferred from this finite enumeration.
"""

def forest(E):
    cap = max(E)
    parent = list(range(2*(cap+1)))
    rank = [0]*len(parent)
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for s in E:
        for i in range(s+1):
            j=cap+1+s-i
            u,v=root(i),root(j)
            if u==v:
                return False
            if rank[u]<rank[v]:
                u,v=v,u
            parent[v]=u
            if rank[u]==rank[v]:rank[u]+=1
    return True

count=0; positives=0
for m in range(3,91):
    assert forest([0,1,m])
    for t in range(1,91):
        actual=forest([0,1,m,m+t])
        predicted=(t>1 and all(z%t for z in (m,m-1,m-2)))
        assert actual == predicted, (m,t,actual,predicted)
        count+=1
        positives+=actual
        if actual:
            E=[0,1,m,m+t]
            for k in range(3):
                E.append(2*E[-1]+1)
                assert forest(E), E
print('PASS',count,'finite four-point cases',positives,'acyclic, with checked extensions')
