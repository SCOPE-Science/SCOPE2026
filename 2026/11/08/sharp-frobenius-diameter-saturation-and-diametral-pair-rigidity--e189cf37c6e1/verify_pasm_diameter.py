"""Independent finite checks for the rectangular partial-alternating-sign-matrix diameter theorem."""
from itertools import combinations,product

def is_pasm(M):
    m=len(M); n=len(M[0])
    for row in M:
        t=0
        for a in row:
            if a not in (-1,0,1):return False
            t+=a
            if t not in (0,1):return False
    for j in range(n):
        t=0
        for i in range(m):
            t+=M[i][j]
            if t not in (0,1):return False
    return True

def diamond(m,n,selected):
    assert len(selected)==2*m
    A=[[0]*n for _ in range(m)]
    B=[[0]*n for _ in range(m)]
    for i in range(1,m+1):
        for h in range(2*i-1):
            A[i-1][selected[m-i+h]]=1 if h%2==0 else -1
            B[i-1][selected[m-i+h+1]]=1 if h%2==0 else -1
    return A,B

def sqdist(A,B):
    return sum((x-y)**2 for row1,row2 in zip(A,B) for x,y in zip(row1,row2))

def all_pasm(m,n):
    # All vertical binary-prefix states are enumerated independently at each column.
    choices=[]
    for col in product((0,1),repeat=m):
        entries=tuple(col[i]-(col[i-1] if i else 0) for i in range(m))
        choices.append(entries)
    def dfs(j,prefix,rows):
        if j==n:
            yield tuple(tuple(row) for row in rows)
            return
        for ent in choices:
            nxt=tuple(prefix[i]+ent[i] for i in range(m))
            if all(v in (0,1) for v in nxt):
                for i in range(m):rows[i].append(ent[i])
                yield from dfs(j+1,nxt,rows)
                for i in range(m):rows[i].pop()
    yield from dfs(0,(0,)*m,[[] for _ in range(m)])

def check():
    from math import comb
    tested=0
    for m in range(1,8):
        for n in (2*m,2*m+1,2*m+3):
            for chosen in (tuple(range(2*m)),tuple(range(n-2*m,n))):
                A,B=diamond(m,n,chosen)
                assert is_pasm(A) and is_pasm(B)
                assert sqdist(A,B)==4*m*m-2*m
                assert is_pasm(tuple(zip(*A))) and is_pasm(tuple(zip(*B)))
                assert sqdist(tuple(zip(*A)),tuple(zip(*B)))==4*m*m-2*m
                tested+=1
        for n in range(2*m, min(2*m+5,14)):
            if comb(n,2*m)>1000:continue
            for chosen in combinations(range(n),2*m):
                A,B=diamond(m,n,chosen)
                assert is_pasm(A) and is_pasm(B)
                assert sqdist(A,B)==4*m*m-2*m
                assert is_pasm(tuple(zip(*A))) and is_pasm(tuple(zip(*B)))
                assert sqdist(tuple(zip(*A)),tuple(zip(*B)))==4*m*m-2*m
                tested+=1
    # Exhaustive first ranks and sharp threshold; strict subthreshold confirmation.
    counts=[]
    for m,n in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(3,4),(3,5),(3,6)]:
        verts=list(all_pasm(m,n))
        assert all(is_pasm(v) for v in verts)
        best=-1
        witnesses=0
        for i in range(len(verts)):
            for j in range(i+1,len(verts)):
                v=sqdist(verts[i],verts[j])
                if v>best:
                    best=v
                    witnesses=1
                elif v==best:
                    witnesses+=1
        assert (best==4*m*m-2*m)==(n>=2*m)
        if n>=2*m:
            assert witnesses==comb(n,2*m), (m,n,witnesses)
        counts.append((m,n,len(verts),best,witnesses))
    print('PASM_RECTANGULAR_SHARP_DIAMETER_CHECKS_PASSED',tested,counts)
if __name__=='__main__':check()
