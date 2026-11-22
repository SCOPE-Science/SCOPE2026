"""Reproducibility checks for fixed-cardinality independent-set traces on paths.
Uses only Python's standard library; none of the finite checks replaces the proof.
"""
from itertools import combinations
from math import comb


def is_stable(mask):
    return (mask & (mask << 1)) == 0


def all_k_stable(n,k):
    return [sum(1<<(x+i) for i,x in enumerate(c))
            for c in combinations(range(n-k+1), k)]


def theorem(n,k,S):
    s=S.bit_count()
    d=min(k,n-2*k+1)
    return is_stable(S) and s<=d


def direct(n,k,S,concepts):
    return len({b&S for b in concepts}) == (1<<S.bit_count())


def component_alpha(n,forbidden):
    a=0;i=0
    while i<n:
        if forbidden & (1<<i):
            i+=1;continue
        j=i
        while j<n and not (forbidden & (1<<j)):
            j+=1
        a+=(j-i+1)//2
        i=j
    return a


def min_forced_profile(n,S):
    coords=[i for i in range(n) if S & (1<<i)]
    best=n+2
    for bits in range(1<<len(coords)):
        T=sum(1<<i for a,i in enumerate(coords) if bits & (1<<a))
        nbr=((T<<1)|(T>>1)) & ((1<<n)-1)
        f=T.bit_count()+component_alpha(n,S|nbr)
        best=min(best,f)
    return best


def rankmod(columns, p):
    # columns stored as sparse dense lists of coefficients, row-reduction over GF(p)
    basis={}
    for col in columns:
        a=col[:]
        while True:
            pivot=next((i for i,x in enumerate(a) if x%p),None)
            if pivot is None:break
            if pivot not in basis:
                inv=pow(a[pivot],-1,p)
                basis[pivot]=[(x*inv)%p for x in a]
                break
            b=basis[pivot]
            q=a[pivot]%p
            a=[(x-q*y)%p for x,y in zip(a,b)]
    return len(basis)


def homology_check(n,d):
    # Reduce boundary matrices for the full truncated stable-set complex.
    faces=[[]]
    for j in range(1,d+1):
        faces.append([tuple(c) for c in combinations(range(n),j)
                      if all(c[t]+1<c[t+1] for t in range(j-1))])
    ranks={2:[0]*(d+2),3:[0]*(d+2)}
    for j in range(2,d+1):
        idmap={f:i for i,f in enumerate(faces[j-1])}
        cols=[]
        for f in faces[j]:
            b=[0]*len(faces[j-1])
            for t in range(j):
                sub=f[:t]+f[t+1:]
                b[idmap[sub]]=1 if t%2==0 else -1
            cols.append(b)
        for p in (2,3):ranks[p][j]=rankmod(cols,p)
    target=sum((-1)**(d-j)*comb(n-j+1,j) for j in range(d+1))
    for p in (2,3):
        for j in range(1,d+1):
            b=len(faces[j])-ranks[p][j]-(ranks[p][j+1] if j<d else 0)-(1 if j==1 else 0)
            assert b==(target if j==d else 0),(n,d,p,j,b,target)
    return target


def main():
    count=0
    for n in range(1,17):
        for k in range(1,(n+1)//2+1):
            concepts=all_k_stable(n,k)
            d=min(k,n-2*k+1)
            bydeg=[0]*(d+1)
            for S in range(1<<n):
                observed=direct(n,k,S,concepts)
                predicted=theorem(n,k,S)
                assert observed==predicted, (n,k,S,observed,predicted)
                if observed:bydeg[S.bit_count()]+=1
                count+=1
            assert bydeg==[comb(n-j+1,j) for j in range(d+1)],(n,k,bydeg)
    print('TRACE_CLASSIFICATION_OK',count)
    forced_count=0
    for n in range(0,14):
        for S in range(1<<n):
            if not is_stable(S):continue
            actual=min_forced_profile(n,S)
            assert actual==(n-S.bit_count()+1)//2,(n,S,actual)
            forced_count+=1
    print('MINMAX_FORCED_PROFILE_OK',forced_count)
    checked=[]
    for n in range(3,12):
        for k in range(1,(n+1)//2+1):
            d=min(k,n-2*k+1)
            if 1<=d<=3:
                checked.append((n,k,d,homology_check(n,d)))
    print('HOMOLOGY_MOD_2_AND_3_OK',len(checked),checked[-6:])
    print('FIXED_WEIGHT_PATH_SHATTERING_PASS')

if __name__=='__main__':main()
