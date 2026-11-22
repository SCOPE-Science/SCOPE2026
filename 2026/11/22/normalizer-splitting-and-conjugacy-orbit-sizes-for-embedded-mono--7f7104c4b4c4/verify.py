"""Finite sanity checks for monogenic inverse-submonoid conjugation orbits.
Uses no external packages. All permutations and partial injections up to size five.
"""
import itertools, math
from collections import defaultdict,Counter

def allmaps(n):
    for r in range(n+1):
        for dom in itertools.combinations(range(n),r):
            for image in itertools.permutations(range(n),r):
                a=[-1]*n
                for i,j in zip(dom,image): a[i]=j
                yield tuple(a)

def inv(a):
    b=[-1]*len(a)
    for x,y in enumerate(a):
        if y>=0: b[y]=x
    return tuple(b)

def mult(a,b):
    return tuple(-1 if x<0 else b[x] for x in a)

def closure(f):
    n=len(f); id_=tuple(range(n)); gen=[f,inv(f)]
    seen={id_}; queue=[id_]
    while queue:
        u=queue.pop()
        for g in gen:
            v=mult(u,g)
            if v not in seen:
                seen.add(v);queue.append(v)
    return frozenset(seen)

def conjugate(f,p):
    pi=[0]*len(p)
    for i,j in enumerate(p):pi[j]=i
    return tuple(-1 if f[pi[i]]<0 else p[f[pi[i]]] for i in range(len(p)))

def cyc_chain(f):
    n=len(f)
    invf=inv(f)
    seen=set();cycles=[];chains=[]
    for i in range(n):
        if invf[i]!=-1: continue
        j=i; count=0
        while j!=-1:
            assert j not in seen
            seen.add(j);count+=1;j=f[j]
        chains.append(count)
    for i in range(n):
        if i in seen: continue
        j=i;count=0
        while j not in seen:
            seen.add(j);count+=1;j=f[j]
        assert j==i
        cycles.append(count)
    assert len(seen)==n
    return tuple(sorted(cycles)),tuple(sorted(chains))

def csize(cyc,chain):
    a=Counter(cyc);b=Counter(chain)
    ret=1
    for d,m in a.items():ret*=d**m*math.factorial(m)
    for d,m in b.items():ret*=math.factorial(m)
    return ret

def phi(k):
    return sum(math.gcd(k,j)==1 for j in range(1,k+1))

def verify(n):
    fs=list(allmaps(n));perms=list(itertools.permutations(range(n)))
    Hs=defaultdict(list)
    for f in fs:
        Hs[closure(f)].append(f)
    orbitset=set();profiles=set();count=0
    for H,gens in Hs.items():
        f=gens[0];cyc,chain=cyc_chain(f)
        assert all(cyc_chain(g)==(cyc,chain) for g in gens)
        chain_arrows=any(l>=2 for l in chain)
        k=math.lcm(*cyc) if cyc else 1
        expected=2 if chain_arrows else phi(k)
        assert len(gens)==expected,(n,f,cyc,chain,len(gens),expected)
        centralizer=csize(cyc,chain)
        conjugates={frozenset(conjugate(h,p) for h in H) for p in perms}
        assert len(conjugates)==math.factorial(n)//(expected*centralizer),(n,cyc,chain,len(conjugates),expected,centralizer)
        if H not in orbitset:
            orbitset.update(conjugates)
            assert (cyc,chain) not in profiles
            profiles.add((cyc,chain))
            count+=1
    assert orbitset==set(Hs)
    partitions={cyc_chain(f) for f in fs}
    assert profiles==partitions
    return n,len(fs),len(Hs),count

if __name__=='__main__':
    for n in range(0,6):
        print('n maps submonoids orbits',verify(n))
    print('MONOGENIC_INVERSE_NORMALIZER_PROFILE_VERIFIED')
