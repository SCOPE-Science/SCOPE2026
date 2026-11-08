"""Independent finite verification for crown-graph induced-forest homology and symmetry.
Uses only the Python standard library. Infinite-family proofs are in RESULT.md.
"""
import itertools
import math
from collections import defaultdict


def is_forest(n, mask):
    # Independent BFS cycle detection, without using the closed classification.
    adj = [[] for _ in range(2*n)]
    for i in range(n):
        if mask >> i & 1:
            for j in range(n):
                if i != j and (mask >> (n+j) & 1):
                    adj[i].append(n+j)
                    adj[n+j].append(i)
    seen = set()
    def dfs(x, parent):
        seen.add(x)
        for y in adj[x]:
            if y == parent:
                continue
            if y in seen or not dfs(y, x):
                return False
        return True
    return all(i in seen or dfs(i,-1) for i in range(2*n) if mask >> i & 1)


def classification(n, mask):
    bit = (1<<n)-1
    A=mask&bit;B=mask>>n;a=A.bit_count();b=B.bit_count();t=(A&B).bit_count()
    return a <= 1 or b <= 1 or (a==b==2 and t>=1) or ((a,b) in ((2,3),(3,2)) and t==2)


def reduce_rank(cols):
    piv={}
    for v in cols:
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)


def betti(n, fs):
    by=defaultdict(list)
    for mask in fs:
        if mask:by[mask.bit_count()-1].append(mask)
    ranks={}
    for d in range(1,max(by)+1):
        ids={f:i for i,f in enumerate(by[d-1])}
        cols=[]
        for f in by[d]:
            col=0
            for i in range(2*n):
                if f>>i&1:col^=1<<ids[f^(1<<i)]
            cols.append(col)
        ranks[d]=reduce_rank(cols)
    return {k:len(v)-ranks.get(k,0)-ranks.get(k+1,0)-(k==0) for k,v in by.items()}


def gmap(n,p,swap):
    return [p[i]+(n if swap else 0) for i in range(n)] + [p[i]+(0 if swap else n) for i in range(n)]


def lefschetz_direct(n,p,swap):
    # Reduced signed Lefschetz supertrace on oriented simplicial chains.
    perm=gmap(n,p,swap);seen=set();orbits=[]
    for start in range(2*n):
        if start in seen:continue
        bit=0;i=start
        while i not in seen:
            seen.add(i);bit|=1<<i;i=perm[i]
        orbits.append(bit)
    total=0
    for sub in range(1<<len(orbits)):
        mask=0
        for i,orb in enumerate(orbits):
            if sub>>i&1:mask|=orb
        if is_forest(n,mask):total+=(-1)**sub.bit_count()
    return -total


def permutation_counts(p):
    f=sum(p[i]==i for i in range(len(p)))
    t=sum(i < p[i] and p[p[i]]==i for i in range(len(p)))
    u=0;seen=set()
    for i in range(len(p)):
        if i not in seen:
            j=i;ell=0
            while j not in seen:seen.add(j);j=p[j];ell+=1
            u += (ell == 3)
    return f,t,u


def integral_top_chains(n):
    # Each C6(T) gives the oriented boundary of its five-simplex.
    # Its distinguished 4-simplex has exactly its own three labels.
    count=0
    for T in itertools.combinations(range(n),3):
        vertices=list(T)+[n+i for i in T]
        # Boundary of 5-simplex is an actual cycle in induced-forest complex.
        chain={sum(1<<v for j,v in enumerate(vertices) if j!=k):(-1)**k
               for k in range(6)}
        assert all(is_forest(n,f) for f in chain)
        boundary={}
        for face,coeff in chain.items():
            verts=[j for j in range(2*n) if face>>j&1]
            for k,j in enumerate(verts):
                low=face^(1<<j)
                boundary[low]=boundary.get(low,0)+coeff*(-1)**k
        assert all(value==0 for value in boundary.values())
        # Distinguished 4-simplex: remove a_i for least i of T.
        distinguished=sum(1<<v for v in vertices[1:])
        assert chain[distinguished] in (-1,1)
        assert (distinguished & ((1<<n)-1)).bit_count()==2
        assert (distinguished >> n).bit_count()==3
        count+=1
    return count


def run():
    for n in range(3,8):
        fs=[mask for mask in range(1<<(2*n)) if classification(n,mask)]
        assert all(is_forest(n,mask)==classification(n,mask) for mask in range(1<<(2*n)))
        B=betti(n,fs)
        exp3=math.comb(n-1,3) if n>=4 else 0
        exp4=math.comb(n,3)
        assert all(B.get(k,0)==({3:exp3,4:exp4}.get(k,0)) for k in B)
        assert integral_top_chains(n)==exp4
        print(f'FACES_AND_HOMOLOGY n={n} faces_including_empty={len(fs)} beta3={exp3} beta4={exp4} top_cycles={exp4}')
    checked=0
    for n in range(3,7):
        for p in itertools.permutations(range(n)):
            f,t,u=permutation_counts(p)
            h4=math.comb(f,3)+f*t+u
            # Generalized binomial coefficient when f=0 is accounted for algebraically.
            h3=(f-1)*(f-2)*(f-3)//6-(f-1)*t+u
            for sw in (False, True):
                s=-1 if sw else 1
                L=lefschetz_direct(n,p,sw)
                assert L==s*(h4-h3),(n,p,sw,L,s*(h4-h3))
                checked+=1
        print(f'ALL_PERMUTATIONS_CHECKED n={n} group_size={2*math.factorial(n)}')
    print(f'TOTAL_SIGNED_LEFSCHETZ_CHECKS={checked}')
    print('CROWN_FOREST_EQUIVARIANT_CHECK_PASS')

if __name__=='__main__':run()
