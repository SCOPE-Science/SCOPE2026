#!/usr/bin/env python3
"""Exact independent max-cut census for rectangular strong path products.
Science-only reproducibility. Python standard library only.
"""
from itertools import product


def graph_edges(rows,cols):
    edges=[]
    for i in range(rows):
        for j in range(cols):
            u=i*cols+j
            for di,dj in [(0,1),(1,-1),(1,0),(1,1)]:
                ii,jj=i+di,j+dj
                if 0<=ii<rows and 0<=jj<cols:
                    edges.append((u,ii*cols+jj))
    assert len(edges)==rows*(cols-1)+cols*(rows-1)+2*(rows-1)*(cols-1)
    return edges


def direct_count(rows,cols):
    edges=graph_edges(rows,cols)
    maximum=-1; ways=0
    for mask in range(1<<(rows*cols-1)):
        # anchor vertex (0,0) at zero; other spins derive from mask
        x=mask<<1
        score=sum(bool((x>>u&1)^(x>>v&1)) for u,v in edges)
        if score>maximum:
            maximum,ways=score,1
        elif score==maximum:
            ways+=1
    return maximum,ways


def width_dp(rows,cols):
    # Columns of `rows` bits. Score every within-column and between-column edge once.
    S=1<<rows
    interior=[sum(((s>>i)&1)!=((s>>(i+1))&1) for i in range(rows-1)) for s in range(S)]
    links=[[sum(((a>>i)&1)!=((b>>j)&1)
                 for i in range(rows)
                 for j in range(max(0,i-1),min(rows,i+2)))
            for b in range(S)] for a in range(S)]
    best=interior[:]
    ways=[1]*S
    for _ in range(cols-1):
        nxt=[-10**9]*S; cnt=[0]*S
        for b in range(S):
            ib=interior[b]
            for a in range(S):
                v=best[a]+links[a][b]+ib
                if v>nxt[b]:nxt[b],cnt[b]=v,ways[a]
                elif v==nxt[b]:cnt[b]+=ways[a]
        best,ways=nxt,cnt
    mx=max(best)
    count=sum(ways[b] for b in range(S) if best[b]==mx)
    assert count%2==0
    return mx,count//2


def predicted(rows,cols):
    a,b=sorted((rows,cols))
    maximum=(b-1)*(3*a-2)
    opt=3 if a==b==2 else 2 if a==b else 1
    return maximum,opt


def local_extension_lemma_test():
    # Exhaustive test of the equality cases used by the proof.
    cases=0
    for length in range(2,9):
        mask=(1<<length)-1
        for a in range(mask+1):
            for b in range(mask+1):
                old=[(a>>i)&1 for i in range(length)]
                new=[(b>>i)&1 for i in range(length)]
                B=sum(old[i]==new[i] for i in range(length))
                B+=sum((new[i]==new[i+1])+(old[i]==new[i+1])+(old[i+1]==new[i]) for i in range(length-1))
                assert B>=length-1
                if B==length-1:
                    assert a in (0,mask) and b==a^mask
                if all(old[i]!=old[i+1] for i in range(length-1)):
                    assert B>=length
                    if B==length:
                        assert b==a or (length==2 and b==a^mask)
                cases+=1
    print('LOCAL_EXTENSION_EQUALITY_CASES_PASS',cases)

def main():
    local_extension_lemma_test()
    direct=0
    for a in range(2,5):
        for b in range(a,9):
            if a*b>16:continue
            assert direct_count(a,b)==predicted(a,b),(a,b,direct_count(a,b))
            direct+=1
    print('DIRECT_ALL_VERTEX_COLORINGS_PASS',direct)
    cases=0
    for a in range(2,8):
        for b in range(a,16):
            expected=predicted(a,b)
            actual=width_dp(a,b)
            assert actual==expected,(a,b,actual,expected)
            cases+=1
    print('TRANSFER_MATRIX_EXACT_MAXCUT_AND_DEGENERACY_PASS',cases)
    print('VERIFY_OK')

if __name__=='__main__':main()
