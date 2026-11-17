"""Exact checks for the side-exchange action on graphic forest complexes.

Standard Python 3 only. Every edge-orbit subset is checked for n=2,3,4,5;
independently, every face of the original complex is enumerated for n=2,3,4
and its signed oriented-simplex trace is computed.
"""

def forest(vcount, edges):
    parent = list(range(vcount))
    size = [1]*vcount
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for a,b in edges:
        a,b=root(a),root(b)
        if a==b:
            return False
        if size[a]<size[b]:
            a,b=b,a
        parent[b]=a
        size[a]+=size[b]
    return True

def orbit_models(n):
    down=[(0,i+1) for i in range(n)]
    up=[[(i,n+i)] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            down.append((i+1,j+1))
            up.append([(i,n+j),(j,n+i)])
    return down,up

def fixed_check(n):
    down,up=orbit_models(n)
    counts=[0]*(n+1)
    for mask in range(1<<len(down)):
        e1=[e for k,e in enumerate(down) if mask>>k&1]
        e2=[e for k,orb in enumerate(up) if mask>>k&1 for e in orb]
        d=forest(n+1,e1)
        u=forest(2*n,e2)
        assert d==u, (n,mask)
        if d:
            counts[len(e1)]+=1
    assert counts[n]==(n+1)**(n-1) # Cayley's spanning-tree formula
    beta=(-1)**n*sum((-1)**j*c for j,c in enumerate(counts))
    return counts,beta

def original_trace(n):
    edge_set=[(i,j) for i in range(n) for j in range(n)]
    counts=[0]*(2*n)
    trace=-1  # augmented degree minus one
    for mask in range(1,1<<(n*n)):
        chosen=[e for k,e in enumerate(edge_set) if mask>>k&1]
        if not forest(2*n,[(i,n+j) for i,j in chosen]):
            continue
        size=len(chosen)
        counts[size]+=1
        ss=set(chosen)
        if ss=={(j,i) for i,j in ss}:
            pairs=sum(i!=j for i,j in ss)//2
            trace+=(-1)**(size-1+pairs)
    # The graphic matroid rank of K_{n,n} is 2n-1, hence the
    # only possible reduced homology degree is 2n-2 (even).
    rank=-1+sum((-1)**(j-1)*c for j,c in enumerate(counts) if j)
    return counts,rank,trace

def main():
    for n in range(2,6):
        f,b=fixed_check(n)
        print('fixed',n,'subsets',1<<(n*(n+1)//2),'faces',f,'top_beta',b)
        if n<=4:
            original,rank,trace=original_trace(n)
            assert trace==(-1)**(n-1)*b
            assert (rank+trace)%2==0 and rank>=abs(trace)
            print('ambient',n,'faces',original,'rank',rank,'trace',trace,
                  'plus',(rank+trace)//2,'minus',(rank-trace)//2)
    print('COMPLETE_BIPARTITE_FOREST_SIDE_SWAP_PASS')

if __name__=='__main__':
    main()
