"""Exact finite checks for fan matching-complex homotopy formulas.
Pure Python, only the standard library. No finite check substitutes for proof."""
from collections import defaultdict

def fan_edges(n):
    return [(0,i) for i in range(1,n+1)] + [(i,i+1) for i in range(1,n)]

def all_matchings(edges):
    bydim=defaultdict(list)
    def rec(j,used,chosen):
        if j == len(edges):
            if chosen: bydim[len(chosen)-1].append(tuple(chosen))
            return
        rec(j+1,used,chosen)
        u,v=edges[j]
        mask=(1<<u)|(1<<v)
        if not used&mask:
            chosen.append(j)
            rec(j+1,used|mask,chosen)
            chosen.pop()
    rec(0,0,[])
    return bydim

def homology_f2(faces):
    size={d:len(f) for d,f in faces.items()}
    rank={-1:0}
    for d in sorted(size):
        if d==0:
            rank[0]=0
            continue
        prev={f:i for i,f in enumerate(faces[d-1])}
        pivots={}
        for f in faces[d]:
            col=0
            for i in range(d+1):
                col ^= (1 << prev[f[:i]+f[i+1:]])
            while col:
                p=col.bit_length()-1
                if p not in pivots:
                    pivots[p]=col
                    break
                col ^= pivots[p]
        rank[d]=len(pivots)
    beta={d:size[d]-rank[d]-rank.get(d+1,0) for d in size}
    beta[0]-=1
    return {d:r for d,r in beta.items() if r!=0},size

def predicted(n):
    k,r=divmod(n,3)
    if r==0:return {k-1:k+1}
    if r==1:return {k:k}
    return {k:2*k+2}

def main():
    tally=0
    for n in range(2,16):
        edges=fan_edges(n)
        fs=all_matchings(edges)
        betti,size=homology_f2(fs)
        expectation=predicted(n)
        assert betti==expectation,(n,betti,expectation)
        assert size.get(0)==2*n-1
        print('n=%d vertices=%d faces=%d betti=%s' % (n,len(edges),sum(size.values()),betti))
        tally+=1
    print('FAN_MATCHING_COMPLEX_EXACT_MOD2_CHECKS_OK %d' % tally)
if __name__=='__main__':main()
