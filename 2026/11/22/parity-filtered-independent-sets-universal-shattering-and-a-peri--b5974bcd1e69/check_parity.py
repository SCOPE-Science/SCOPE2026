"""Independent verification of parity-constrained independent-set learning."""
from functools import lru_cache
from itertools import combinations


def hypotheses(n, p, edges):
    adj = [0] * n
    for u,v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return [s for s in range(1 << n) if (s.bit_count() & 1) == p and all(not (s >> u & 1 and s >> v & 1) for u,v in edges)], adj


def criterion(S,p,adj,n):
    if any((S >> i & 1) and (adj[i] & S) for i in range(n)):
        return False
    if (S.bit_count() & 1) != p:
        return any(not(S >> t & 1) and not(adj[t] & S) for t in range(n))
    return all(any(not(S >> t & 1) and not(adj[t] & (S ^ (1 << v))) for t in range(n)) for v in range(n) if S >> v & 1)


def direct_shattered(S,hyp):
    seen = {h&S for h in hyp}
    return len(seen) == 1 << S.bit_count()


def online(hyp,n):
    axes=[sum(1 << i for i,h in enumerate(hyp) if h>>j&1) for j in range(n)]
    @lru_cache(None)
    def rank(mask):
        return max([1+min(rank(mask&b),rank(mask&~b)) for b in axes if mask&b and mask&~b] + [0])
    return rank((1<<len(hyp))-1),rank.cache_info().currsize


def target_vc(n,p):
    if n==1:return 0
    if n==2:return p
    if n==4 and p==0:return 2
    return (n-1)//2


def target_ld(n,p):
    if n%2:return (n-1)//2
    k=n//2
    return k if k%2==p else k-1


def main():
    total=0
    for n in range(1,17):
        edges=[(j,j+1) for j in range(n-1)]
        for p in [0,1]:
            hyp,adj=hypotheses(n,p,edges)
            vc=0;faces=0
            for S in range(1<<n):
                c=criterion(S,p,adj,n)
                if c: vc=max(vc,S.bit_count());faces+=1
                if n<=12:
                    assert c==direct_shattered(S,hyp),(n,p,S,'criterion')
            online_rank,states=online(hyp,n)
            assert (vc,online_rank)==(target_vc(n,p),target_ld(n,p)),(n,p,vc,online_rank)
            print(f'PATH n={n:02d} parity={p} hypotheses={len(hyp)} vc={vc} ldim={online_rank} faces={faces} states={states}')
            total+=1
    # Every labeled graph on at most five vertices: criterion versus direct traces.
    graph_count=0
    for n in range(1,6):
        possible=list(combinations(range(n),2))
        for emask in range(1<<len(possible)):
            edges=[e for i,e in enumerate(possible) if emask>>i&1]
            for p in (0,1):
                hyp,adj=hypotheses(n,p,edges)
                for S in range(1<<n):
                    assert criterion(S,p,adj,n)==direct_shattered(S,hyp),(n,emask,p,S)
            graph_count+=1
    print('GRAPH_TESTS',graph_count,'unlabeled? no: all labeled graphs up to five vertices')
    print('RESULT PASS',total,'path parity classes and',graph_count,'labeled graph instances')

if __name__=='__main__':main()
