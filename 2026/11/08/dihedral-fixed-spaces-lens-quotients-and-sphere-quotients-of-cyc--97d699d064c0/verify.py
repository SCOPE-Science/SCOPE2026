#!/usr/bin/env python3
"""Independent finite checks for the cyclic nonmatching orbit theorem.
Uses standard library only; does not purport to prove unbounded claims.
"""
from itertools import combinations
from collections import defaultdict
from math import gcd


def t_matchings(n,t):
    return [sum(1 << x for x in c) for c in combinations(range(n),t)
            if all((b-a)%n not in (1,n-1) for a,b in combinations(c,2))]


def faces(n,t):
    forbidden=t_matchings(n,t)
    return {m for m in range(1<<n) if not any((m&x)==x for x in forbidden)}


def gale_facets(n,t):
    d=t-1
    return {sum(1<<x for x in c) for c in combinations(range(n),2*d)
            if all(sum(1 for i in c if a<i<b)%2==0
                   for a,b in combinations((i for i in range(n) if i not in c),2))}


def action_mask(mask,n,shift,mirror):
    return sum(1<< ((shift-i if mirror else shift+i)%n) for i in range(n) if mask>>i&1)


def group(n,q,dihedral=False,offset=0):
    # q is rotation-subgroup order; group elements act i->i+shift and i->shift-i.
    shifts=[(j*n//q)%n for j in range(q)]
    return [(s,False) for s in shifts]+([(offset+s,True) for s in shifts] if dihedral else [])


def orbit_complex(n,allowed,grp):
    remaining=set(range(n)); orbits=[]
    while remaining:
        i=min(remaining)
        orb={((sh-i if mirror else sh+i)%n) for sh,mirror in grp}
        assert orb<=remaining
        remaining-=orb
        orbits.append(sum(1<<j for j in orb))
    fac=[]
    for bits in range(1<<len(orbits)):
        m=0
        for i,orb in enumerate(orbits):
            if bits>>i&1: m|=orb
        if m in allowed:fac.append(bits)
    return len(orbits),set(fac)


def rank_mod(columns,p):
    # Sparse column reduction; keys are row indices, entries in F_p.
    piv={}
    for col in columns:
        v={k:x%p for k,x in col.items() if x%p}
        while v:
            top=max(v)
            if top not in piv:
                val=v[top]; inv=pow(val,-1,p)
                piv[top]={k:(x*inv)%p for k,x in v.items()}
                break
            fac=v[top]
            for k,x in piv[top].items():
                nv=(v.get(k,0)-fac*x)%p
                if nv:v[k]=nv
                elif k in v:del v[k]
    return len(piv)


def betti_of_complex(fac,p=2):
    if fac=={0}:return {-1:1}
    cells={k:[m for m in fac if m.bit_count()==k+1] for k in range(max(x.bit_count() for x in fac))}
    ranks={};num={k:len(arr) for k,arr in cells.items()}
    for k in range(1,len(cells)):
        idx={m:i for i,m in enumerate(cells[k-1])}
        cols=[]
        for m in cells[k]:
            ids=[i for i in range(m.bit_length()) if m>>i&1]
            cols.append({idx[m^(1<<i)]:(-1 if j%2 else 1) for j,i in enumerate(ids)})
        ranks[k]=rank_mod(cols,p)
    return {k:num[k]-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0)
            for k in cells if num[k]-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0)}


def quotient_betti(n,t,p=2):
    K=faces(n,t)-{0}; grp=group(n,n,True)
    chains_by_dim=defaultdict(set)
    # Enumerate increasing flags of nonempty faces by adding proper supersets.
    face_list=sorted(K,key=lambda m:(m.bit_count(),m))
    for a in face_list:
        stack=[(a,)]
        while stack:
            chain=stack.pop(); chains_by_dim[len(chain)-1].add(chain)
            if len(chain)>=2*(t-1):continue
            last=chain[-1]
            stack.extend([chain+(b,) for b in face_list if b.bit_count()>last.bit_count() and b&last==last])
    def orbit_rep(chain):
        return min(tuple(action_mask(m,n,sh,mirror) for m in chain) for sh,mirror in grp)
    c={k:sorted({orbit_rep(chain) for chain in arr}) for k,arr in chains_by_dim.items()}
    ranks={}
    for k in range(1,max(c)+1):
        target={ch:j for j,ch in enumerate(c[k-1])}
        cols=[]
        for ch in c[k]:
            bd=defaultdict(int)
            for j in range(k+1):bd[target[orbit_rep(ch[:j]+ch[j+1:])]]+=(-1)**j
            cols.append(bd)
        ranks[k]=rank_mod(cols,p)
    return {k:len(c[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in sorted(c)},sum(map(len,c.values()))


def check():
    facet_cases=0;fixed_cases=0;quotient_cases=0;orbit_faces=0;quotient_cells=0
    for n in range(4,12):
        for t in range(2,min(4,n//2)+1):
            K=faces(n,t)
            top={x for x in K if not any(y!=x and x&y==x for y in K)}
            assert top==gale_facets(n,t),(n,t,'polytope facet mismatch')
            facet_cases+=1
            d=t-1
            for q in range(1,n+1):
                if n%q:continue
                for dihedral in (False,True):
                    for offset in ((0,1) if dihedral and n%2==0 else (0,)):
                        if q==1 and not dihedral:continue # full K covered by facet check
                        grp=group(n,q,dihedral,offset)
                        vnum,fac=orbit_complex(n,K,grp)
                        bet=betti_of_complex(fac)
                        power=d//q
                        sphere_dim=power-1 if dihedral else 2*power-1
                        want={sphere_dim:1}
                        assert bet==want,(n,t,q,dihedral,offset,bet,want)
                        fixed_cases+=1;orbit_faces+=len(fac)
    for n in range(6,10):
        for p in (2,3):
            result,cells=quotient_betti(n,3,p)
            assert result=={0:1,1:0,2:0,3:1},(n,p,result)
            quotient_cases+=1;quotient_cells+=cells
    print(f'ALL_VERIFY_OK polytope_cases={facet_cases} fixed_subgroups={fixed_cases} fixed_faces={orbit_faces} quotient_field_cases={quotient_cases} quotient_cells={quotient_cells}')

if __name__=='__main__':check()
