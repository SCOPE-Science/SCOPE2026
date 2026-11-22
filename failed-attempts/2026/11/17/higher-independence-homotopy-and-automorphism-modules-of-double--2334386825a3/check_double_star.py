#!/usr/bin/env python3
"""Exact finite checks for higher-independence homology of bistar trees.
Only Python standard library is required. All assertions are exact.
"""
from collections import defaultdict
from itertools import permutations
from math import comb
import json


def faces_from_graph(a, b, r):
    # Hubs 0 and 1; A=2,...,a+1; B=a+2,...,a+b+1
    n = a+b+2
    links = [0]*n
    E = [(0, 1)] + [(0, v) for v in range(2, 2+a)] + [(1, v) for v in range(2+a, n)]
    for v,w in E:
        links[v] |= 1 << w
        links[w] |= 1 << v
    out = defaultdict(list)
    for mask in range(1, 1 << n):
        seen = 0
        ok = True
        while mask & ~seen:
            unseen = mask & ~seen
            seed = unseen & -unseen
            comp, frontier = seed, seed
            while frontier:
                nxt = 0
                s=frontier
                while s:
                    bit=s & -s
                    s-=bit
                    nxt |= links[bit.bit_length()-1]
                frontier = (nxt & mask) & ~comp
                comp |= frontier
            if comp.bit_count() > r:
                ok = False
                break
            seen |= comp
        if ok:
            out[mask.bit_count()-1].append(mask)
    return out


def faces_formula(a,b,r):
    n=a+b+2
    amask=((1<<a)-1)<<2
    bmask=((1<<b)-1)<<(2+a)
    out=defaultdict(list)
    for mask in range(1,1<<n):
        hubs=mask&3
        if hubs==3:
            ok=2+(mask&(amask|bmask)).bit_count()<=r
        elif hubs==1:
            ok=1+(mask&amask).bit_count()<=r
        elif hubs==2:
            ok=1+(mask&bmask).bit_count()<=r
        else:
            ok=True
        if ok:out[mask.bit_count()-1].append(mask)
    return out


def rank_mod2(columns):
    pivots={}
    for col in columns:
        while col:
            p=col.bit_length()-1
            if p in pivots: col^=pivots[p]
            else: pivots[p]=col;break
    return len(pivots)


def reduced_betti_mod2(fs):
    ranks={}
    for d in sorted(fs):
        if d==0:continue
        down={mask:i for i,mask in enumerate(fs[d-1])}
        columns=[]
        for face in fs[d]:
            col=0;vbits=face
            while vbits:
                bit=vbits & -vbits
                col ^= 1 << down[face^bit]
                vbits-=bit
            columns.append(col)
        ranks[d]=rank_mod2(columns)
    return {d:len(f)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
            for d,f in fs.items()}


def cycles(perm, points):
    seen=set(); ls=[]
    for v in points:
        if v in seen:continue
        length=0;x=v
        while x not in seen:
            seen.add(x); length+=1;x=perm[x]
        ls.append(length)
    return ls


def exterior_trace(a,b,r,perm):
    # Coefficient [t^(r-2)] det(I+t*g on augmentation of leaf permutations).
    if r<2 or r>a+b+1:return 0
    n=a+b
    coeff=[1]+[0]*n
    for ell in cycles(perm, range(2,n+2)):
        for k in range(n,ell-1,-1):
            coeff[k] += ((-1)**(ell+1))*coeff[k-ell]
    quotient=[0]*(n+1)
    prev=0
    for k in range(n+1):
        quotient[k]=coeff[k]-prev
        prev=quotient[k]
    return quotient[r-2]


def reduced_lefschetz(fs,perm):
    trace=-1  # subtract the degree-zero augmentation
    for d,flist in fs.items():
        for mask in flist:
            v=[i for i in range(len(perm)) if mask & (1<<i)]
            w=[perm[i] for i in v]
            if set(v)!=set(w):continue
            inv=sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
            trace+=(-1)**(d+inv)
    return trace


def main():
    count_cases=0;count_chars=0;count_swap_chars=0;count_faces=0
    illustrative=[]
    for a in range(1,4):
      for b in range(1,4):
       n=a+b+2
       perms_a=list(permutations(range(2,a+2)))
       perms_b=list(permutations(range(a+2,n)))
       for r in range(1,n+1):
        x=faces_from_graph(a,b,r)
        y=faces_formula(a,b,r)
        assert dict(x)==dict(y), ('face predicates',a,b,r)
        count_faces+=sum(map(len,x.values()))
        B=reduced_betti_mod2(x)
        expected=(comb(a+b-1,r-2) if 2<=r<=a+b+1 else 0)
        for d,v in B.items():
            assert v==(expected if d==r-1 else 0), ('homology',a,b,r,d,v,expected)
        for pa in perms_a:
         for pb in perms_b:
          perm=list(range(n))
          for src,dst in zip(range(2,a+2),pa):perm[src]=dst
          for src,dst in zip(range(a+2,n),pb):perm[src]=dst
          actual=reduced_lefschetz(x,perm)
          pred=(-1)**(r-1)*exterior_trace(a,b,r,perm) if r>=2 else 0
          assert actual==pred, ('character',a,b,r,perm,actual,pred)
          count_chars+=1
        if a==b:
         # Full automorphism group adds hub exchange; any exchange is a leaf
         # block-permuting involution times a hub-fixing permutation.
         for pa in perms_a:
          for pb in perms_b:
           perm=list(range(n))
           perm[0],perm[1]=1,0
           for src,dst in zip(range(2,a+2),pa):perm[src]=dst+a
           for src,dst in zip(range(a+2,n),pb):perm[src]=dst-a
           actual=reduced_lefschetz(x,perm)
           pred=(-1)**r*exterior_trace(a,b,r,perm) if r>=2 else 0
           assert actual==pred, ('hub-exchange',a,b,r,perm,actual,pred)
           count_swap_chars+=1
        count_cases+=1
        if a==3 and b==3:illustrative.append({'a':a,'b':b,'r':r,'rank':expected,'faces':sum(map(len,x.values()))})
    out={'result':'BISTAR_R_INDEPENDENCE_EXACT_CHECKS_PASS',
         'graph_parameter_pairs':9,'r_parameter_cases':count_cases,
         'complete_face_lists_compared':count_faces,
         'all_leaf_group_elements_and_thresholds_checked':count_chars,
         'hub_interchange_automorphism_checks':count_swap_chars,
         'all_mod2_betti_numbers_checked':True,
         'all_signed_lefschetz_character_checks_pass':True,
         'sample_a3_b3':illustrative,
         'note':'Finite checks complement but do not replace the uniform Mayer-Vietoris and suspension proof.'}
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=='__main__':main()
