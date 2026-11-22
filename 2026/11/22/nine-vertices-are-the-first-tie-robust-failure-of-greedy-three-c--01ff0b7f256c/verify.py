"""Exhaustive exact proof of the first three-chord greedy obstruction on cycles.
Run: python3 verification_new.py (Python >=3.8; standard library only).
No random sampling or floating-point arithmetic.
"""
from itertools import combinations


def chords(n):
    return tuple((a,b) for a in range(n) for b in range(a+2,n)
                 if (a,b)!=(0,n-1))


def resist_num(n,u,v):
    d=abs(u-v)
    return d*(n-d)


def det_bareiss(a):
    a=[list(row) for row in a]
    m=len(a)
    if m==0: return 1
    sign=1; old=1
    for k in range(m-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,m) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,m):
            for j in range(k+1,m):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%old==0
                a[i][j]=numerator//old
            a[i][k]=0
        old=pivot
    return sign*a[-1][-1]


def tree_count(n, edges):
    # Independent exact matrix-tree cofactor, not the resistance shortcut.
    L=[[0]*n for _ in range(n)]
    for a,b in tuple((i,(i+1)%n) for i in range(n))+tuple(edges):
        L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    return det_bareiss([row[:-1] for row in L[:-1]])


def fast_count(n,edges):
    # Matrix determinant lemma and cycle resistance kernel.
    k=len(edges)
    if not k:return n
    Z=[]
    for a,b in edges:
        row=[]
        for c,d in edges:
            row.append(resist_num(n,a,d)+resist_num(n,b,c)-
                       resist_num(n,a,c)-resist_num(n,b,d))
        Z.append(row)
    M=[[2*n*(i==j)+Z[i][j] for j in range(k)] for i in range(k)]
    d=det_bareiss(M)*n
    assert d%(2*n)**k==0
    return d//(2*n)**k


def optimal_extensions(n, prefixes, E):
    all_next=set()
    best_values=[]
    for S in prefixes:
        values={tuple(sorted((*S,e))):fast_count(n,(*S,e)) for e in E if e not in S}
        top=max(values.values())
        best_values.append(top)
        all_next.update(T for T,value in values.items() if value==top)
    return all_next,max(best_values)


def check():
    expected={5:(45,45),6:(81,81),7:(117,117),8:(168,168),9:(240,235)}
    checks=0
    for n in range(5,10):
        E=chords(n)
        by_count={}
        for k in (0,1,2,3):
            for S in combinations(E,k):
                v=fast_count(n,S)
                independent=tree_count(n,S)
                assert v==independent,(n,S,v,independent)
                by_count[S]=v
                checks+=1
        globally=max(by_count[S] for S in combinations(E,3))
        global_opts={S for S in combinations(E,3) if by_count[S]==globally}
        greedies={()}
        per_stage=[]
        for k in (1,2,3):
            greedies,top=optimal_extensions(n,greedies,E)
            assert all(by_count[S]==top for S in greedies)
            per_stage.append((top,len(greedies)))
        assert (globally,per_stage[-1][0])==expected[n]
        print('n=%d chords=%d global=%d optima=%d greedy stages=%r overlap=%d'%(
            n,len(E),globally,len(global_opts),per_stage,len(global_opts&greedies)))
        if n==9:
            assert per_stage==[(29,9),(93,9),(235,18)],per_stage
            assert len(global_opts)==3
            print('nine-cycle globally optimal triples:',*sorted(global_opts),sep='\n  ')
    print('PASS exact independent spanning-tree cofactor / rank-update comparisons:',checks)

if __name__=='__main__':check()
