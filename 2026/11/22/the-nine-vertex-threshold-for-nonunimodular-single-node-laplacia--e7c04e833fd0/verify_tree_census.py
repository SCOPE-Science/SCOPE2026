"""Self-contained exhaustive census of controllability determinants on trees of order <=9.
Only the Python standard library is needed. Run: python tree_integer_census.py
"""
from collections import Counter
from fractions import Fraction

def canonical_code(edges,n):
    nbr=[[] for _ in range(n)]
    for a,b in edges:
        nbr[a].append(b);nbr[b].append(a)
    def encode(v,parent):
        return '(' + ''.join(sorted(encode(w,v) for w in nbr[v] if w!=parent)) + ')'
    return min(encode(v,-1) for v in range(n))

def all_trees(upto=9):
    trees={1:[()]}
    for n in range(2,upto+1):
        found={}
        for e in trees[n-1]:
            for root in range(n-1):
                candidate=e+((root,n-1),)
                found.setdefault(canonical_code(candidate,n),candidate)
        trees[n]=list(found.values())
    return trees

def det_bareiss(A):
    n=len(A);a=[r[:] for r in A]; sign=1;prev=1
    for k in range(n-1):
        if not a[k][k]:
            j=next((i for i in range(k+1,n) if a[i][k]),None)
            if j is None: return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j]
                assert z%prev==0
                a[i][j]=z//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def det_fraction(A):
    B=[[Fraction(x) for x in r] for r in A];n=len(B);res=Fraction(1)
    for k in range(n):
        s=next((i for i in range(k,n) if B[i][k]),None)
        if s is None:return 0
        if s!=k:B[s],B[k]=B[k],B[s];res=-res
        pivot=B[k][k];res*=pivot
        for i in range(k+1,n):
            factor=B[i][k]/pivot
            for j in range(k+1,n):B[i][j]-=factor*B[k][j]
            B[i][k]=0
    assert res.denominator==1
    return int(res)

def walk_matrix(edges,n,root):
    nbr=[[] for _ in range(n)]
    for a,b in edges:nbr[a].append(b);nbr[b].append(a)
    vec=[int(i==root) for i in range(n)];cols=[]
    for _ in range(n):
        cols.append(vec)
        vec=[sum(vec[i]-vec[j] for j in nbr[i]) for i in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def left_null_mod2(A):
    n=len(A)
    # Find nonzero row vector w annihilating the columns, over F_2.
    M=[[A[r][c]&1 for r in range(n)] for c in range(n)]
    pivots=[];rank=0
    for c in range(n):
        i=next((v for v in range(rank,n) if M[v][c]),None)
        if i is None:continue
        M[i],M[rank]=M[rank],M[i]
        for j in range(n):
            if j!=rank and M[j][c]: M[j]=[a^b for a,b in zip(M[j],M[rank])]
        pivots.append(c);rank+=1
    free=[i for i in range(n) if i not in pivots]
    if not free:return None
    w=[0]*n;w[free[0]]=1
    for i,p in enumerate(pivots):w[p]=M[i][free[0]]
    assert all(sum(w[r]*A[r][c] for r in range(n))%2==0 for c in range(n))
    return [i for i,x in enumerate(w) if x]

def main():
    trees=all_trees();expected=(1,1,1,2,3,6,11,23,47)
    assert tuple(len(trees[n]) for n in range(1,10))==expected
    last=[]
    for n in range(1,10):
        freq=Counter();examples=[]
        for e in trees[n]:
            for root in range(n):
                K=walk_matrix(e,n,root)
                d=det_bareiss(K)
                assert d==det_fraction(K)
                freq[abs(d)]+=1
                if abs(d)>1:
                    examples.append((e,root,d,left_null_mod2(K)))
        print('n=',n,'trees=',len(trees[n]),'det_freq=',sorted(freq.items()),'exceptions=',examples)
        if n<=8:assert set(freq)<={0,1}
        if n==9:
            assert freq==Counter({0:361,1:60,2:2})
            assert len({canonical_code(e,n) for e,j,d,w in examples})==1
            last=examples
    assert last and all(abs(x[2])==2 for x in last)
    print('PASS all n <= 9, independent rational and fraction-free determinants')
if __name__=='__main__':main()
