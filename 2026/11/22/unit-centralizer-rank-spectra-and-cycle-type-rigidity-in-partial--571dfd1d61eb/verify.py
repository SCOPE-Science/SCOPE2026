"""Independent finite verification of unit-centralizer rank census in partial Brauer monoids.
Standard Python only; run python verify.py. This is finite testing, not an infinite proof.
"""
from functools import lru_cache
from itertools import permutations
from collections import Counter
from math import factorial

@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    a,*rest=vertices
    out=[]
    for m in matchings(tuple(rest)):
        out.append(tuple(sorted(((a,),)+m)))
    for b in rest:
        others=tuple(x for x in rest if x!=b)
        for m in matchings(others):
            out.append(tuple(sorted(((a,b),)+m)))
    return tuple(out)

def cycles(perm):
    n=len(perm);seen=set();counts=Counter()
    for a in range(n):
        if a in seen:continue
        b=a;length=0
        while b not in seen:
            seen.add(b);length+=1;b=perm[b]
        counts[length]+=1
    return dict(counts)

def rank(m,n):return sum(len(x)==2 and x[0]<n<=x[1] for x in m)

def diag_action(m,perm):
    n=len(perm)
    p=list(perm)+[n+j for j in perm]
    return tuple(sorted(tuple(sorted(p[i] for i in x)) for x in m))

def unit(n,perm):
    return tuple(sorted((i,n+perm[i]) for i in range(n)))

def multiply(a,b,n):
    # concatenate A top-to-middle with B middle-to-bottom
    parents=list(range(3*n))
    def root(i):
        while parents[i]!=i:
            parents[i]=parents[parents[i]];i=parents[i]
        return i
    def join(i,j):parents[root(i)]=root(j)
    for block in a:
        if len(block)==2:
            i,j=block
            ii=i if i<n else i # A lower vertex n+j gets middle n+j
            jj=j if j<n else j
            join(ii,jj)
    for block in b:
        if len(block)==2:
            i,j=block
            ii=n+i if i<n else n+i # B upper i => middle n+i, lower n+j=> bottom 2n+j
            jj=n+j if j<n else n+j
            join(ii,jj)
    groups={}
    for i in list(range(n))+list(range(2*n,3*n)):
        groups.setdefault(root(i),[]).append(i if i<n else i-n)
    return tuple(sorted(tuple(sorted(v)) for v in groups.values()))

def pol_add(a,b):
    c=Counter(a)
    for k,v in b.items():c[k]+=v
    return dict(c)

def pol_mul(a,b):
    c=Counter()
    for i,x in a.items():
        for j,y in b.items():c[i+j]+=x*y
    return dict(c)

def pol_scale(a,k,shift=0):return {i+shift:k*x for i,x in a.items()}

def local_poly(L,m):
    s=1+(L%2==0)
    @lru_cache(None)
    def rec(a,b):
        if a==b==0:return {0:1}
        if a:
            p=pol_scale(rec(a-1,b),s)
            if a>=2:p=pol_add(p,pol_scale(rec(a-2,b),L*(a-1)))
            if b:p=pol_add(p,pol_scale(rec(a-1,b-1),L*b,L))
            return p
        p=pol_scale(rec(0,b-1),s)
        if b>=2:p=pol_add(p,pol_scale(rec(0,b-2),L*(b-1)))
        return p
    return rec(m,m)

def formula(perm):
    f={0:1}
    for L,m in cycles(perm).items():f=pol_mul(f,local_poly(L,m))
    return f

def one_perm(ctype):
    n=sum(ctype);p=[];offset=0
    for l in ctype:
        p.extend([offset+((i+1)%l) for i in range(l)])
        offset+=l
    return tuple(p)

def partitions(n,minimum=1):
    if n==0:
        yield ()
    else:
        for x in range(minimum,n+1):
            for p in partitions(n-x,x):yield (x,)+p

def inv_number(k):
    # involutions on k symbols, permutations whose cycle lengths <=2
    return sum(factorial(k)//(factorial(k-2*j)*factorial(j)*2**j) for j in range(k//2+1))

def top_coefficient(cycle_type):
    z=1
    for L,m in Counter(cycle_type).items():z*=L**m*factorial(m)
    return z

def recover_m_from_poly(pol,n):
    # rational formal series via exact Fraction; normalize reverse polynomial
    from fractions import Fraction
    z=pol[n]
    series={k:Fraction(pol.get(n-k,0),z) for k in range(n+1)}
    result={}
    for L in range(1,n+1):
        value=series[L]*L/(1+(L%2==0))**2
        assert value.denominator==1 and value>=0,(L,value)
        m=int(value)
        result[L]=m
        if m:
            # strip local factor to length n in reverse: divide series by Q
            local=local_poly(L,m)
            leading=local[L*m]
            q={j:Fraction(local.get(L*m-j,0),leading) for j in range(n+1)}
            new={}
            for j in range(n+1):
                new[j]=series[j]-sum(q[k]*new[j-k] for k in range(1,j+1))
            series=new
    assert sum(L*m for L,m in result.items())==n
    return {L:m for L,m in result.items() if m}

if __name__=='__main__':
    print('Partial Brauer monoid rank-polynomial and permutation-centralizer verification')
    for n in range(1,5):
        ms=matchings(tuple(range(2*n)))
        print('n',n,'matching_count',len(ms),'permutations',factorial(n))
        bytype={}
        for perm in permutations(range(n)):
            count=Counter()
            u=unit(n,perm)
            iu=unit(n,tuple(perm.index(j) for j in range(n)))
            for m in ms:
                invariant=diag_action(m,perm)==m
                commutes=(multiply(m,u,n)==multiply(u,m,n))
                assert invariant==commutes,(n,perm,m,invariant,commutes)
                if invariant:count[rank(m,n)]+=1
            predicted=formula(perm)
            assert dict(count)==predicted,(n,perm,dict(count),predicted)
            assert predicted[n]==top_coefficient(tuple(sorted(cycles(perm).elements())) if False else tuple(l for l,c in cycles(perm).items() for _ in range(c)))
            assert recover_m_from_poly(predicted,n)==cycles(perm)
            bytype[tuple(sorted(l for l,c in cycles(perm).items() for _ in range(c)))]=predicted
        sums=Counter()
        for typ,pol in bytype.items():
            nperm=factorial(n)//top_coefficient(typ)
            for k,v in pol.items():sums[k]+=nperm*v
        assert all(v%factorial(n)==0 for v in sums.values())
        print('  unit_orbits_by_rank',dict(sorted((k,v//factorial(n)) for k,v in sums.items())))
    for n in (5,6):
        ms=matchings(tuple(range(2*n))) if n==5 else None
        print('n',n,'cycle_types',list(partitions(n)))
        for typ in partitions(n):
            perm=one_perm(typ)
            predicted=formula(perm)
            assert recover_m_from_poly(predicted,n)==cycles(perm)
            if ms is not None:
                count=Counter(rank(m,n) for m in ms if diag_action(m,perm)==m)
                assert dict(count)==predicted,(n,typ,predicted,count)
            print('  ',typ,'rank_counts',','.join(str(predicted.get(k,0)) for k in range(n+1)))
    for n in range(1,7):
        pred=formula(tuple(range(n)))
        expected={r:factorial(n)**2//(factorial(r)*factorial(n-r)**2)*inv_number(n-r)**2 for r in range(n+1)}
        assert pred==expected,(n,pred,expected)
    print('PASS: exhaustive n<=4 multiplication and invariance; n=5 cycle types; n<=6 rigidity and identity rank formulas.')
