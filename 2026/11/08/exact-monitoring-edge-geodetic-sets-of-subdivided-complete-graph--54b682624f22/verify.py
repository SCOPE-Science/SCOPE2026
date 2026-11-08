"""Independent exhaustive verification of monitoring-edge-geodetic sets of S(K_n).

Standard-library Python 3.10+.  No external research or publication dependencies.
The graph and monitoring condition are evaluated directly by BFS after edge deletion.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb
from random import Random


def graph(n):
    original = list(range(n))
    midpoint_of = {p: n+i for i,p in enumerate(combinations(range(n),2))}
    edges = []
    for (u,v), w in midpoint_of.items():
        edges.extend(((u,w),(v,w)))
    return n+len(midpoint_of), edges, midpoint_of


def distances(order, edges):
    adj=[[] for _ in range(order)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    matrix=[]
    for source in range(order):
        d=[order+1]*order;d[source]=0
        q=deque([source])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v] > d[u]+1:
                    d[v]=d[u]+1;q.append(v)
        matrix.append(d)
    return matrix


def compute_monitor_pairs(order, edges):
    d=distances(order,edges)
    pair_index={(i,j):t for t,(i,j) in enumerate(combinations(range(order),2))}
    witnesses=[]
    for p in range(len(edges)):
        dp=distances(order,edges[:p]+edges[p+1:])
        witness=0
        for (i,j),idx in pair_index.items():
            if dp[i][j] > d[i][j]:
                witness |= 1<<idx
        witnesses.append(witness)
    return pair_index,witnesses


def original_monitoring(mask, pairs, edge_witnesses):
    selected_pairs=0
    for (u,v),j in pairs.items():
        if mask&(1<<u) and mask&(1<<v):
            selected_pairs |= 1<<j
    return all((selected_pairs & wm)!=0 for wm in edge_witnesses)


def predicted_condition(n, mask, midpoint_of):
    a={i for i in range(n) if mask&(1<<i)}
    return all((mask&(1<<w)) or ({u,v}<=a) for (u,v),w in midpoint_of.items())


def expected_all_polynomial(n):
    N=comb(n,2)
    result=Counter()
    for k in range(n+1):
        inside=comb(k,2)
        for j in range(inside+1):
            result[k+N-inside+j]+=comb(n,k)*comb(inside,j)
    return result


def expected_minimal_polynomial(n):
    N=comb(n,2)
    ans=Counter({N:1})
    for k in range(2,n+1):
        ans[k+N-comb(k,2)]+=comb(n,k)
    return ans


def verify(n, exhaustive, samples=5000):
    order,edges,midpoints=graph(n)
    pair_index,witnesses=compute_monitor_pairs(order,edges)
    rng=Random(19770813+n)
    masks=range(1<<order) if exhaustive else [rng.randrange(1<<order) for i in range(samples)]
    all_count=Counter(); minima=Counter(); examined=0
    for s in masks:
        truth=original_monitoring(s,pair_index,witnesses)
        prediction=predicted_condition(n,s,midpoints)
        assert truth==prediction,('all-set condition fails',n,s,truth,prediction)
        examined+=1
        if exhaustive and truth:
            all_count[s.bit_count()]+=1
            if all(not original_monitoring(s^(1<<i),pair_index,witnesses)
                   for i in range(order) if s&(1<<i)):
                minima[s.bit_count()]+=1
    if exhaustive:
        assert all_count==expected_all_polynomial(n),(n,'all polynomial',all_count,expected_all_polynomial(n))
        assert minima==expected_minimal_polynomial(n),(n,'minimal polynomial',minima,expected_minimal_polynomial(n))
    return examined,sum(all_count.values()),sum(minima.values()),len(edges)


def main():
    total=all_sets=minimal_sets=0
    for n in (3,4,5):
        tested,a,b,e=verify(n,True)
        total+=tested;all_sets+=a;minimal_sets+=b
    sampled,*_=verify(6,False,5000);total+=sampled
    for n in range(3,25):
        q=expected_minimal_polynomial(n)
        assert sum(q.values())==2**n-n
        assert min(q)==n
        assert max(q)==comb(n,2)+1
    print('VERIFY_OK direct_BFS_vertex_subsets='+str(total)+
          ' exhaustive_orders=3,4,5 sampled_order=6'
          ' total_monitoring_sets='+str(all_sets)+
          ' total_minimal_sets='+str(minimal_sets)+
          ' all_set_polynomials=PASS minimal_set_polynomials=PASS'
          ' full_subdivision_structure=PASS symbolic_n3to24=PASS')

if __name__=='__main__':
    main()
