"""Finite, independent checks for maximal-intersecting-edge shattering.

No external packages or nonstandard libraries required.  The theorem for all n
is mathematical and does not rely on extrapolation from these tests.
"""
from itertools import combinations
from math import comb


def data(n):
    edges = list(combinations(range(n), 2))
    idx = {edge:i for i,edge in enumerate(edges)}
    stars = [sum(1 << i for i,e in enumerate(edges) if v in e)
             for v in range(n)]
    triangles = [sum(1 << idx[e] for e in combinations(t, 2))
                 for t in combinations(range(n),3)]
    return edges, stars+triangles


def graph_shape(edges):
    degree = {}
    for a,b in edges:
        degree[a] = degree.get(a,0)+1
        degree[b] = degree.get(b,0)+1
    return len(edges)<=3 and (len(edges)<=1 or
        all(any(a in e for a in edges) for e in edges) and
        (len(edges)==2 or len(degree)==3 or (len(degree)==4 and 3 in degree.values())))


def predicted(edges):
    if len(edges) <= 1: return True
    if len(edges) == 2: return len(set(edges[0]) & set(edges[1]))==1
    if len(edges) == 3:
        degrees = {}
        for a,b in edges:
            degrees[a] = degrees.get(a,0)+1
            degrees[b] = degrees.get(b,0)+1
        return sorted(degrees.values()) in ([1,1,1,3],[2,2,2])
    return False


def rank_f2(vectors):
    pivots={}
    for x in vectors:
        while x:
            j=x.bit_length()-1
            if j in pivots: x^=pivots[j]
            else:
                pivots[j]=x
                break
    return len(pivots)


def homology_check(n):
    es,_=data(n)
    pairs=[tuple(pair) for pair in combinations(range(len(es)),2)
            if set(es[pair[0]]) & set(es[pair[1]])]
    pair_idx={p:i for i,p in enumerate(pairs)}
    faces=[tuple(triple) for triple in combinations(range(len(es)),3)
           if predicted([es[i] for i in triple])]
    boundaries=[]
    for a,b,c in faces:
        boundaries.append(sum(1<<pair_idx[p] for p in ((a,b),(a,c),(b,c))))
    d2=rank_f2(boundaries)
    v,e,f=len(es),len(pairs),len(faces)
    assert e-v+1==d2, (n,v,e,f,d2)
    beta=f-d2
    assert beta == comb(n,2)+(n-5)*comb(n,3)-1,(n,beta)
    return (v,e,f,beta)


def maximal_families_bruteforce(n):
    edges,hypotheses=data(n)
    m=len(edges)
    conflicts=[sum(1<<j for j,f in enumerate(edges) if not(set(e)&set(f)))
               for e in edges]
    found=set()
    for mask in range(1<<m):
        if any(mask>>i&1 and (mask&conflicts[i]) for i in range(m)):
            continue
        if all(mask>>i&1 or (mask&conflicts[i]) for i in range(m)):
            found.add(mask)
    assert found==set(hypotheses),(n,len(found),len(hypotheses))
    return len(found)


def main():
    maxima=[]
    for n in range(4,7): maxima.append((n,maximal_families_bruteforce(n)))
    trials=0
    for n in range(4,9):
        edges,hypotheses=data(n)
        counts=[]
        for k in range(5):
            ct=0
            for subset in combinations(range(len(edges)),k):
                projection={tuple((h>>i)&1 for i in subset) for h in hypotheses}
                shat=(len(projection)==(1<<k))
                right=predicted([edges[i] for i in subset])
                assert shat==right,(n,k,subset)
                ct+=shat
                trials+=1
            counts.append(ct)
        assert counts==[1,comb(n,2),3*comb(n,3),(n-2)*comb(n,3),0],(n,counts)
        print('SHATTERING',n,counts)
    for n in range(4,9):
        ed,H=data(n)
        for i,e in enumerate(ed):
            pos=[h for h in H if h>>i&1]
            for j,f in enumerate(ed):
                if j!=i:
                    assert sum(1 for h in pos if h>>j&1)<=2
        print('POSITIVE_BRANCH',n,'PASS')
    for n in range(4,8): print('HOMOLOGY',n,homology_check(n))
    print('MAXIMAL_FAMILIES',maxima)
    print('EKR_MAXIMAL_EDGE_SHATTERING_PASS',trials)

if __name__=='__main__':main()
