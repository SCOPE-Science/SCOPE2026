"""Independent brute-force checks for top vertex-connectivity layers of permutation inversion graphs."""
from itertools import permutations, combinations
from collections import Counter
from math import comb

def graph(perm):
    n=len(perm)
    return [sum(1<<j for j in range(n) if i!=j and (i-j)*(perm[i]-perm[j])<0) for i in range(n)]

def connected_on(A,S):
    if not S: return True
    start=S&-S; seen=start; boundary=start
    while boundary:
        i=(boundary&-boundary).bit_length()-1
        boundary &= boundary-1
        n=A[i]&S&~seen
        boundary |=n; seen|=n
    return seen==S

def exact_conn(A):
    n=len(A)
    full=(1<<n)-1
    if not connected_on(A,full): return 0
    for deleted in range(1,n):
        for s in combinations(range(n),deleted):
            S=full
            for i in s:S &= ~(1<<i)
            if not connected_on(A,S):return deleted
    return n-1

def claimed_class(perm):
    n=len(perm)
    A=graph(perm)
    H=[( (1<<n)-1 ) ^ (1<<i) ^ A[i] for i in range(n)]
    if any(h.bit_count()>=3 for h in H): return False
    seen=0
    for i in range(n):
        if seen>>i&1:continue
        comp=1<<i; boundary=comp
        while boundary:
            j=(boundary&-boundary).bit_length()-1;boundary&=boundary-1
            add=H[j]&~comp; comp|=add;boundary|=add
        seen|=comp
        k=comp.bit_count(); deg=[(H[j]&comp).bit_count() for j in range(n) if comp>>j&1]
        if k>=4 and all(d==2 for d in deg):return False
    return True

def coeff(n):
    blocks={1:1,2:1,3:3}
    blocks.update({j:2 for j in range(4,n+1)})
    a=[1]
    for m in range(1,n+1):a.append(sum(blocks[j]*a[m-j] for j in range(1,m+1)))
    fib=[0,1]
    for _ in range(n+1):fib.append(fib[-1]+fib[-2])
    return a[n],fib[n+1]

def weighted_coeffs(n):
    # Independent block-composition generating recurrence: isolated vertices,
    # single edges, triangles and the two path permutations of larger sizes.
    pol=[Counter({0:1})]
    for m in range(1,n+1):
        out=Counter()
        for j in range(1,m+1):
            block={0:1} if j==1 else {1:1} if j==2 else {2:2,3:1} if j==3 else {j-1:2}
            for a,c in pol[m-j].items():
                for b,mult in block.items():out[a+b]+=c*mult
        pol.append(out)
    return pol[n]

def verify():
    for n in range(4,9):
        tally=Counter(); high=0; noninv=Counter(); total=0
        for p in permutations(range(n)):
            total+=1
            A=graph(p)
            if n<=7:
                k=exact_conn(A)
                tally[k]+=1
            else:
                # Compute the high connectivity condition independently from all 4-vertex induced subgraphs.
                k=n-3 if all(connected_on(A,sum(1<<i for i in subset)) for subset in combinations(range(n),4)) else -1
            good=claimed_class(p)
            if (k>=n-3)!=good:raise AssertionError((n,p,k,'class'))
            if good:
                high+=1
                noninv[comb(n,2)-sum(a.bit_count() for a in A)//2]+=1
        exact,f=coeff(n)
        assert high==exact,(n,high,exact)
        assert noninv==weighted_coeffs(n),(n,noninv,weighted_coeffs(n))
        if n<=7:
            assert tally[n-1]==1 and tally[n-2]==f-1 and tally[n-3]==exact-f, (n,tally,exact,f)
        print('n=',n,'perms=',total,'kappa_ge_n-3=',high,'fib=',f,'high_exact=',exact-f,'WEIGHTED_PASS')
    print('VERIFY_OK')
if __name__=='__main__':verify()
