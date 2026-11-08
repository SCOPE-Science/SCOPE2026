"""Independent finite enumeration and exact generating-function checks for a loopless directed public-good influence network."""
from itertools import product
from fractions import Fraction
from math import factorial

def kernels(f):
    n=len(f)
    return sum(all(((m>>v)&1) != ((m>>f[v])&1) for v in range(n)) for m in range(1<<n))

def cycles(f):
    n=len(f); seen=set(); lengths=[]
    for start in range(n):
        if start in seen: continue
        seq=[]; pos={}; x=start
        while x not in seen and x not in pos:
            pos[x]=len(seq); seq.append(x); x=f[x]
        if x in pos: lengths.append(len(seq)-pos[x])
        seen.update(seq)
    return lengths

def coeffs(n,alpha):
    # n![z^n](1-T(z)^2)^(-alpha), T=ze^T.
    if n<2:return 0
    s=Fraction(0)
    for j in range((n-2)//2+1):
        # (1-t^2)^(-alpha-1) coefficient j = (alpha+1)_j / j!
        poch=Fraction(1)
        for k in range(j): poch*=alpha+1+k
        poch/=factorial(j)
        k=n-2*j-2
        s+=2*alpha*poch*Fraction(n**k,factorial(k))
    return factorial(n)*s/n

for n in range(2,7):
    total=(n-1)**n
    by_k={}; odd=0
    for f in product(*(tuple(j for j in range(n) if j!=i) for i in range(n))):
        c=cycles(f); k=kernels(f)
        expected=0 if any(t%2 for t in c) else 2**len(c)
        assert k==expected,(n,f,c,k,expected)
        by_k[k]=by_k.get(k,0)+1
    exists=sum(v for k,v in by_k.items() if k>0)
    weighted=sum(k*v for k,v in by_k.items())
    # alpha=1/2 weights 1 for each even cycle; alpha=1 weights 2 per even cycle
    assert exists==coeffs(n,Fraction(1,2)),(n,exists,coeffs(n,Fraction(1,2)))
    assert weighted==coeffs(n,Fraction(1)),(n,weighted,coeffs(n,Fraction(1)))
    print(f'n={n}, total={total}, distribution={dict(sorted(by_k.items()))}, P_exist={Fraction(exists,total)}, E_K={Fraction(weighted,total)}')
print('PASS all exact cycle/kernel/EGF checks')

# Independently enumerate all possible one-arc reciprocity interventions.
from itertools import product

def kernel_count(arcs,n):
    return sum(all((not ((mask>>i)&1) and any((mask>>j)&1 for (u,j) in arcs if u==i)) or (((mask>>i)&1) and not any((mask>>j)&1 for (u,j) in arcs if u==i)) for i in range(n)) for mask in range(1<<n))

def odd_cycles_and_attachment(f):
    n=len(f);seen=set(); result=[]
    for i in range(n):
        if i in seen:continue
        path=[];pos={};x=i
        while x not in seen and x not in pos:
            pos[x]=len(path); path.append(x); x=f[x]
        if x in pos:
            cyc=path[pos[x]:]
            if len(cyc)%2:
                rootset=set(cyc)
                attachments={k for k in range(n) if k not in rootset and f[k] in rootset}
                result.append((rootset,attachments))
        seen.update(path)
    return result

for n in range(2,7):
    c=0
    for f in product(*(tuple(j for j in range(n) if j!=i) for i in range(n))):
        bad=odd_cycles_and_attachment(f)
        if len(bad)!=1:continue
        arcs={(i,f[i]) for i in range(n)}
        if kernel_count(arcs,n)!=0:raise AssertionError(('bad odd classification',n,f))
        cycle,attached=bad[0]
        good_arc_origins=cycle|attached
        for i in range(n):
            # add reverse of i->f(i)
            new=arcs|{(f[i],i)}
            observed=kernel_count(new,n)>0
            predicted=(i in good_arc_origins)
            if observed!=predicted:
                print('FAIL',n,f,'cycle',cycle,'attached',attached,'candidate',i,observed,predicted)
                raise SystemExit(1)
            c+=1
    print('n',n,'verified single repair tests',c)
print('PASS')


# Two disjoint directed triangles require exactly two repairs, with 3 x 3 choices.
from itertools import combinations
f=(1,2,0,4,5,3)
original={(i,f[i]) for i in range(6)}
assert kernel_count(original,6)==0
assert all(kernel_count(original|{(f[i],i)},6)==0 for i in range(6))
assert sum(kernel_count(original|{(f[i],i),(f[j],j)},6)>0 for i,j in combinations(range(6),2))==9
print("PASS two-component repair count")
