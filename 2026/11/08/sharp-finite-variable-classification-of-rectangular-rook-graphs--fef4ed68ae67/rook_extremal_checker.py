"""Brute-force finite checks of clique and independence thresholds for rook graphs."""
from itertools import combinations_with_replacement, product


def test_board(a,b):
    v=list(product(range(a),range(b)))
    n=len(v)
    adj=[[False]*n for _ in range(n)]
    for i,(r,c) in enumerate(v):
        for j,(s,d) in enumerate(v):
            adj[i][j]=i!=j and (r==s or c==d)
    clique=0
    independent=0
    checked=0
    for mask in range(1,1<<n):
        ids=[i for i in range(n) if (mask>>i)&1]
        k=len(ids)
        if k<=clique and k<=independent:
            continue
        checked+=1
        is_clique=all(adj[x][y] for index,x in enumerate(ids) for y in ids[index+1:])
        if is_clique:
            clique=max(clique,k)
            if k>=3:
                assert len({v[x][0] for x in ids})==1 or len({v[x][1] for x in ids})==1
        is_independent=all(not adj[x][y] for index,x in enumerate(ids) for y in ids[index+1:])
        if is_independent:
            independent=max(independent,k)
    assert clique==max(a,b), (a,b,clique)
    assert independent==min(a,b), (a,b,independent)
    return checked, n


def main():
    boards=list(combinations_with_replacement(range(2,5),2))
    total=0
    for a,b in boards:
        checked,n=test_board(a,b)
        total+=checked
        print(f"rook_graph={a}x{b} vertices={n} subsets_examined_after_pruning={checked} alpha={min(a,b)} omega={max(a,b)} PASS")
    print(f"boards={len(boards)} total_examined_after_pruning={total} PASS")

if __name__=='__main__':
    main()
