#!/usr/bin/env python3
"""Independent finite checks for the unipotent Alexander quandle subquandle orbit theorem."""
from itertools import permutations, product
from collections import Counter
from math import comb, gcd


def action_p(p):
    n=p*p
    return [[(a+b-d)%p + p*b for d in range(p) for c in range(p)]
            for b in range(p) for a in range(p)]


def is_subquandle(mask, table, n):
    S=[i for i in range(n) if mask>>i&1]
    for x in S:
        tx=table[x]
        for y in S:
            if not (mask>>tx[y]&1):
                return False
    return True


def aut_permutations(p):
    n=p*p
    for ell in range(1,p):
        for v in range(p):
            for u in product(range(p), repeat=p):
                yield tuple((ell*a+u[b])%p +p*((ell*b+v)%p)
                            for b in range(p) for a in range(p))


def verify_p_all_permutations(p):
    n=p*p
    table=action_p(p)
    expected=set(aut_permutations(p))
    found=set()
    for m in permutations(range(n)):
        good=True
        for x in range(n):
            for y in range(n):
                if m[table[x][y]] != table[m[x]][m[y]]:
                    good=False
                    break
            if not good: break
        if good: found.add(m)
    assert found==expected, (p,len(found),len(expected))
    return len(found)


def find_structure_subquandles(p):
    n=p*p
    ans=set()
    # Nonempty subsets in exactly one row
    for b in range(p):
        for mask in range(1,1<<p):
            ans.add(sum(1<<(a+p*b) for a in range(p) if mask>>a&1))
    # Unions of full rows, at least two selected rows
    for mask in range(1,1<<p):
        if mask.bit_count()>=2:
            ans.add(sum(1<<(a+p*b) for b in range(p) if mask>>b&1 for a in range(p)))
    return ans


def automorphism_generators(p):
    # Independent translation in each vertical fibre
    gens=[]
    for b0 in range(p):
        gens.append(tuple((a+(b==b0))%p+p*b for b in range(p) for a in range(p)))
    # Translation of base coordinate and global multiplication by a primitive unit
    gens.append(tuple(a+p*((b+1)%p) for b in range(p) for a in range(p)))
    for g in range(2,p):
        if len({pow(g,j,p) for j in range(1,p)})==p-1:
            primitive=g
            break
    else: primitive=1
    gens.append(tuple(primitive*a%p+p*(primitive*b%p) for b in range(p) for a in range(p)))
    return gens


def map_subset(mask,g):
    out=0
    while mask:
        bit=mask&-mask
        i=bit.bit_length()-1
        out|=1<<g[i]
        mask ^=bit
    return out


def quandle_subquandle_orbit_histogram(p, exhaustive=False):
    n=p*p
    predicted=find_structure_subquandles(p)
    if exhaustive:
        table=action_p(p)
        actual={mask for mask in range(1,1<<n) if is_subquandle(mask,table,n)}
        assert predicted==actual, (p,len(predicted),len(actual))
    unvisited=set(predicted)
    generators=automorphism_generators(p)
    hist=Counter()
    while unvisited:
        seed=unvisited.pop()
        orbit={seed};stack=[seed]
        while stack:
            s=stack.pop()
            for g in generators:
                t=map_subset(s,g)
                assert t in predicted
                if t not in orbit:
                    orbit.add(t);stack.append(t)
                    unvisited.discard(t)
        hist[seed.bit_count()]+=1
    return hist,len(predicted)


def agl_subset_orbit_hist(p):
    unseen=set(range(1<<p));hist=Counter()
    while unseen:
        seed=unseen.pop(); orbit=set()
        for a in range(1,p):
            for b in range(p):
                trans=sum(1<<((a*x+b)%p) for x in range(p) if seed>>x&1)
                orbit.add(trans)
        unseen.difference_update(orbit)
        hist[seed.bit_count()]+=1
    return hist


def phi(d):
    return sum(gcd(k,d)==1 for k in range(1,d+1))


def burnside_B(p):
    # cycle polynomial of AGL_1(F_p)
    coeff=Counter()
    for k in range(p+1): coeff[k]+=comb(p,k)
    coeff[0]+=p-1;coeff[p]+=p-1
    for d in range(2,p):
        if (p-1)%d: continue
        m=(p-1)//d
        for j in range(m+1):
            coeff[j*d]+=p*phi(d)*comb(m,j)
            coeff[j*d+1]+=p*phi(d)*comb(m,j)
    divisor=p*(p-1)
    assert all(coeff[k]%divisor==0 for k in range(p+1))
    return Counter({k:coeff[k]//divisor for k in range(p+1)})


def predicted_quandle_hist(p):
    b=burnside_B(p)
    hist=Counter()
    for k in range(1,p+1):hist[k]+=b[k]
    for k in range(2,p+1):hist[p*k]+=b[k]
    return hist


def f4_linear_maps():
    for a,b in product(range(4),repeat=2):
        if a==0 or b==0 or b==a: continue
        yield tuple(0 if x==0 else a if x==1 else b if x==2 else a^b for x in range(4))


def verify_f4():
    q=4; n=q*q;count=0
    for L in f4_linear_maps():
        for v in range(q):
            for u in product(range(q),repeat=q):
                perm=[L[a]^u[b]+q*(L[b]^v) for b in range(q) for a in range(q)]
                assert len(set(perm))==n
                for b in range(q):
                    for a in range(q):
                        x=a+q*b;mx=perm[x]
                        for d in range(q):
                            for c in range(q):
                                y=c+q*d
                                xy=(a^b^d)+q*b
                                by=mx//q;ay=mx%q
                                md=perm[y]//q
                                result=(ay^by^md)+q*by
                                assert perm[xy]==result
                count+=1
    assert count==6144
    return count


def main():
    for p in (2,3):
        aut=verify_p_all_permutations(p)
        hist,nsub=quandle_subquandle_orbit_histogram(p,True)
        assert hist==predicted_quandle_hist(p)
        print('ALL_PERMUTATIONS',p,'automorphisms',aut,'subquandles',nsub,'orbit_sizes',sorted(hist.items()))
    for p in (5,7):
        hist,nsub=quandle_subquandle_orbit_histogram(p,False)
        assert hist==predicted_quandle_hist(p)
        print('SUBQUANDLE_ORBITS',p,'subquandles',nsub,'orbits',sum(hist.values()),'sizes',sorted(hist.items()))
    for p in (2,3,5,7,11,13,17,19):
        assert agl_subset_orbit_hist(p)==burnside_B(p)
        print('AFFINE_CYCLE_INDEX',p,'subset_orbits',sum(burnside_B(p).values()))
    print('F4_AUTOMORPHISMS', verify_f4())
    print('UNIPOTENT_QUANDLE_AUT_ORBIT_THEOREM_CHECKS_PASSED')

if __name__=='__main__':main()

# Independent finite-vector-space and two-stage Burnside checks for all extension degrees.
from functools import lru_cache


def vector_space(p,f):
    q=p**f
    coords=[tuple((x//(p**j))%p for j in range(f)) for x in range(q)]
    back={x:i for i,x in enumerate(coords)}
    add=lambda a,b: back[tuple((coords[a][j]+coords[b][j])%p for j in range(f))]
    neg=lambda a: back[tuple(-coords[a][j]%p for j in range(f))]
    return q,coords,add,neg


def all_linear_perms(p,f):
    q,co,add,neg=vector_space(p,f)
    for images in product(range(q),repeat=f):
        L=tuple(next(j for j,c in enumerate(co) if c==tuple(sum(co[i][x]*co[images[x]][j] for x in range(f))%p for j in range(f))) for i in range(q))
        if len(set(L))==q:
            yield L


def span_vectors(gen, q, add):
    W={0}
    for g in gen:
        W.update({add(x,k) for x in tuple(W) for k in {0,g}})
        # closure under addition, finite
        while True:
            old=len(W)
            W.update({add(x,y) for x in tuple(W) for y in tuple(W)})
            if old==len(W):break
    return frozenset(W)


def quot_data(W, q, add):
    cosets=[];ix={};left=set(range(q))
    while left:
        x=min(left); c=frozenset(add(x,w) for w in W); i=len(cosets)
        cosets.append(c)
        for y in c:ix[y]=i
        left-=c
    plus=tuple(tuple(ix[add(min(c),min(d))] for d in cosets) for c in cosets)
    return cosets,ix,plus


def subset_class_polynomial(Lbar, plus):
    h=len(plus)
    bit_perms=[]
    for t in range(h):
        perm=tuple(plus[Lbar[i]][t] for i in range(h))
        bit_perms.append(perm)
    # translation classes of nonempty subsets (their orbit sizes need not be equal)
    seen=set(); classes=[]
    for mask in range(1,1<<h):
        if mask in seen:continue
        orb={map_subset(mask, tuple(plus[i][t] for i in range(h))) for t in range(h)}
        seen|=orb
        classes.append(orb)
    hist=Counter()
    linear_perm=tuple(Lbar)
    for cls in classes:
        if map_subset(next(iter(cls)),linear_perm) in cls:
            hist[next(iter(cls)).bit_count()]+=1
    return hist


def mult_poly(A,B):
    C=Counter()
    for a,x in A.items():
        for b,y in B.items():C[a+b]+=x*y
    return C


def burnside_allfield(p,f,verbose=False):
    q,coords,add,neg=vector_space(p,f)
    full=Counter(); num_L=0;fixed_B_total=0
    # product-of-polynomial terms by h and invariant B
    for L in all_linear_perms(p,f):
        num_L+=1
        for v in range(q):
            h=tuple(add(L[b],v) for b in range(q))
            for Bmask in range(1,1<<q):
                if map_subset(Bmask,h)!=Bmask:continue
                fixed_B_total+=1
                B=[b for b in range(q) if Bmask>>b&1]
                b0=B[0]
                W=span_vectors([add(b,neg(b0)) for b in B],q,add)
                cosets,ix,plus=quot_data(W,q,add)
                Lbar=tuple(ix[L[min(c)]] for c in cosets)
                unseen=set(B);prod=Counter({0:1})
                while unseen:
                    b=min(unseen);cy=[];cur=b
                    while cur not in cy:
                        cy.append(cur);unseen.remove(cur);cur=h[cur]
                    ell=len(cy)
                    Lpow=tuple(range(len(cosets)))
                    for j in range(ell):Lpow=tuple(Lbar[x] for x in Lpow)
                    base=subset_class_polynomial(Lpow,plus)
                    term=Counter({k*len(W)*ell:v for k,v in base.items()})
                    prod=mult_poly(prod,term)
                full.update(prod)
    group_order=num_L*q
    assert all(c%group_order==0 for c in full.values())
    total=Counter({k:v//group_order for k,v in full.items()})
    if verbose:print('ALL_FIELD_BURNSIDE',p,f,'GL',num_L,'fixed_B_terms',fixed_B_total,'orbit_polynomial',sorted(total.items()))
    return total


def allfield_subquandle_masks(p,f):
    q,coords,add,neg=vector_space(p,f)
    items=set()
    for Bmask in range(1,1<<q):
        B=[b for b in range(q) if Bmask>>b&1]
        W=span_vectors([add(b,neg(B[0])) for b in B],q,add)
        cosets,ix,plus=quot_data(W,q,add)
        fibers=[]
        for b in B:
            fibers.append([sum(1<<(a+q*b) for j,c in enumerate(cosets) if subset>>j&1 for a in c) for subset in range(1,1<<len(cosets))])
        for choice in product(*fibers):
            item=0
            for part in choice:item|=part
            items.add(item)
    return items


def allfield_aut_orbit_hist(p,f):
    q,coords,add,neg=vector_space(p,f)
    subs=allfield_subquandle_masks(p,f)
    if p==2 and f==2:
        table=[[((a^b^d)+q*b) for d in range(q) for c in range(q)]
               for b in range(q) for a in range(q)]
        actual={m for m in range(1,1<<(q*q)) if is_subquandle(m,table,q*q)}
        assert actual==subs, ('F4_full_operation_closure',len(actual),len(subs))
    all_L=list(all_linear_perms(p,f));gens=[]
    for b0 in range(q):
        for w in range(1,q):
            gens.append(tuple(add(a,w if b==b0 else 0)+q*b for b in range(q) for a in range(q)))
    for L in all_L:
        gens.append(tuple(L[a]+q*L[b] for b in range(q) for a in range(q)))
    for v in range(1,q):gens.append(tuple(a+q*add(b,v) for b in range(q) for a in range(q)))
    unseen=set(subs);hist=Counter()
    while unseen:
        seed=unseen.pop();orb={seed};stack=[seed]
        while stack:
            m=stack.pop()
            for g in gens:
                t=map_subset(m,g)
                assert t in subs
                if t not in orb:
                    orb.add(t);stack.append(t);unseen.discard(t)
        hist[seed.bit_count()]+=1
    print('DIRECT_EXTENSION_ORBITS',p,f,'subquandles',len(subs),'classes',sum(hist.values()),'hist',sorted(hist.items()))
    return hist


if __name__=='__main__':
    for p,f in ((2,2),(3,2)):
        comp=burnside_allfield(p,f,True)
        direct=allfield_aut_orbit_hist(p,f)
        assert direct==comp
    print('ALL_FIELD_BURNSIDE_CHECKS_PASSED')
