"""Independent finite checks for coloured finite Dedekind-action rigidity.
Standard library only; group actions and relabellings are enumerated directly.
"""
import itertools
from collections import Counter
from math import prod

def group(moduli):
    elems=list(itertools.product(*(range(m) for m in moduli)))
    ix={g:i for i,g in enumerate(elems)}
    add=[[ix[tuple((x+y)%m for x,y,m in zip(a,b,moduli))] for b in elems] for a in elems]
    return elems,add

def quaternion_group():
    # 0..7 encode +1,-1,+i,-i,+j,-j,+k,-k.
    pairs=[(sg,unit) for unit in range(4) for sg in (1,-1)]
    idx={v:i for i,v in enumerate(pairs)}
    def mul(u,v):
        s,a=u; t,b=v
        if a==0:return (s*t,b)
        if b==0:return (s*t,a)
        if a==b:return (-s*t,0)
        positive={(1,2):3,(2,3):1,(3,1):2}
        if (a,b) in positive:return (s*t,positive[(a,b)])
        return (-s*t,positive[(b,a)])
    table=[[idx[mul(a,b)] for b in pairs] for a in pairs]
    return pairs,table

def subgroups(add):
    m=len(add)
    result=[]
    for mask in range(1,1<<m,2):
        h={i for i in range(m) if mask>>i&1}
        if all(add[a][b] in h for a in h for b in h):result.append(frozenset(h))
    return sorted(result,key=lambda x:(len(x),sorted(x)))

def orbit_counts_direct(add,q):
    m=len(add); unseen=set(itertools.product(range(q),repeat=m)); c=Counter()
    while unseen:
        w=next(iter(unseen)); orb={tuple(w[add[a][b]] for b in range(m)) for a in range(m)}
        assert orb<=unseen
        unseen-=orb;c[len(orb)]+=1
    return c

def orbit_counts_subgroup_mobius(add,q):
    m=len(add); hs=subgroups(add); f={}
    # q^(m/|H|) counts words with period group containing H;
    # remove strict supergroups by downward recursion.
    for h in sorted(hs,key=lambda x:-len(x)):
        z=q**(m//len(h))-sum(f[k] for k in hs if h<k)
        assert z>=0 and z%(m//len(h))==0
        f[h]=z
    c=Counter()
    for h,z in f.items():c[m//len(h)]+=z//(m//len(h))
    return c

def orbit_counts_components(add,q):
    m=len(add); out=Counter()
    for h in subgroups(add):
        reps=[]; seen=set()
        for a in range(m):
            coset=frozenset(add[a][b] for b in h)
            if coset not in seen:
                reps.append(min(coset));seen.add(coset)
        k=len(reps)
        cos_ix={a:i for i,rep in enumerate(reps) for a in (add[rep][b] for b in h)}
        trans={tuple(cos_ix[add[rep][a]] for rep in reps) for a in range(m)}
        words=set(itertools.product(range(q),repeat=k))
        while words:
            w=next(iter(words)); orb={tuple(w[t[i]] for i in range(k)) for t in trans}
            words-=orb
            if len(orb)==k:out[k]+=1 # no colour-preserving nontrivial orbit rotation
    return out

def poly(c):
    p=[1]
    for k,num in c.items():
        for _ in range(num):
            nxt=p+[0]*k
            for i,v in enumerate(p):nxt[i+k]+=v
            p=nxt
    return p

def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))
def idperm(n):return tuple(range(n))
def power(p,k):
    r=idperm(len(p))
    for _ in range(k):r=compose(r,p)
    return r

def actions_on_n(moduli,n):
    perms=list(itertools.permutations(range(n)))
    options=[[p for p in perms if power(p,d)==idperm(n)] for d in moduli]
    for generators in itertools.product(*options):
        if all(compose(p,q)==compose(q,p) for p in generators for q in generators):
            yield generators

def canonical_action(moduli, generators,colors):
    n=len(colors); best=None
    for pi in itertools.permutations(range(n)):
        inv=[pi.index(j) for j in range(n)]
        newcol=tuple(colors[inv[j]] for j in range(n))
        newgens=tuple(tuple(pi[p[inv[j]]] for j in range(n)) for p in generators)
        key=(newcol,newgens)
        if best is None or key<best:best=key
    return best

def rigid_action(generators,colors):
    n=len(colors)
    for p in itertools.permutations(range(n)):
        if p==idperm(n):continue
        if all(colors[p[j]]==colors[j] for j in range(n)) and all(compose(p,f)==compose(f,p) for f in generators):
            return False
    return True

def brute_unlabelled_rigid(moduli,q,n):
    seen=set()
    for gens in actions_on_n(moduli,n):
        for colors in itertools.product(range(q),repeat=n):
            if rigid_action(gens,colors):seen.add(canonical_action(moduli,gens,colors))
    return len(seen)

def run():
    cases=[((2,),2),((3,),2),((4,),2),((2,2),2),((6,),2),((2,3),3),((2,2),3)]
    for moduli,q in cases:
        _,add=group(moduli)
        a=orbit_counts_direct(add,q)
        b=orbit_counts_subgroup_mobius(add,q)
        c=orbit_counts_components(add,q)
        assert a==b==c,(moduli,q,a,b,c)
        P=poly(a)
        assert len(P)-1==q**len(add)
        assert P[-1]==1
        assert P[0]==1
        print('GROUP',moduli,'COLORS',q,'ORBIT_SIZES',sorted(a.items()),'CAPACITY',len(P)-1,'INITIAL',P[:8])
    _,qua=quaternion_group()
    a=orbit_counts_direct(qua,2)
    b=orbit_counts_subgroup_mobius(qua,2)
    c=orbit_counts_components(qua,2)
    assert a==b==c,(a,b,c)
    assert len(poly(a))-1==256
    assert all(all(qua[g][h] in H for h in H) for H in subgroups(qua) for g in H)
    # Q8's subgroup set is normal: left and right cosets are identical.
    for H in subgroups(qua):
        for g in range(8):
            assert {qua[g][h] for h in H}=={qua[h][g] for h in H}
    print('Q8_NONABELIAN_DEDEKIND_OK',sorted(a.items()))
    for moduli,q,top in [((2,),2,4),((3,),2,4),((4,),2,4),((2,2),2,4),((2,),3,3)]:
        _,add=group(moduli)
        P=poly(orbit_counts_direct(add,q))
        for n in range(top+1):
            got=brute_unlabelled_rigid(moduli,q,n)
            assert got==P[n],(moduli,q,n,got,P[n])
        print('BRUTE_RIGID_MATCH',moduli,q,'n<=',top)
    # Same cardinality but distinct subgroup geometry: 2-colour order four groups.
    _,cyc=group((4,));_,v4=group((2,2))
    C=poly(orbit_counts_direct(cyc,2));V=poly(orbit_counts_direct(v4,2))
    assert C[2]==2 and V[2]==4 and len(C)==len(V)==17
    # Nonabelian boundary: 3-point S_3 action on the cosets of a transposition,
    # plus one fixed point, has trivial equivariant automorphism group with one colour.
    # The 3-point action generated by a transposition (0 1) and a 3-cycle (0 1 2).
    s=(1,0,2,3);t=(1,2,0,3)
    assert rigid_action((s,t),(0,0,0,0))
    print('NONABELIAN_S3_EXAMPLE_OK')
    print('ALL_CHECKS_OK')
if __name__=='__main__':run()
