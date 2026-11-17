"""Independent finite checks of dissociation complexes on partial matching deletions.
Run: python3 research05_partial_matching_verify.py
Uses only Python standard library. Computed homology ranks are over F_2;
the theorem's integral homotopy claim rests on its proof, not these checks.
"""
from collections import Counter
from itertools import combinations
from math import comb


def allowed(mask,a,b,t):
    ai=[i for i in range(a) if (mask>>i)&1]
    bj=[j for j in range(b) if (mask>>(a+j))&1]
    return all(sum(int(i!=j or i>=t) for j in bj)<=1 for i in ai) and all(sum(int(i!=j or j>=t) for i in ai)<=1 for j in bj)


def rank_mod2(rows):
    piv={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i in piv: x^=piv[i]
            else:
                piv[i]=x
                break
    return len(piv)


def betti_mod2(faces,n):
    bydim={}
    for f in faces:
        if f: bydim.setdefault(f.bit_count()-1,[]).append(f)
    ranks={}
    for d in range(1,max(bydim)+1):
        lo={u:i for i,u in enumerate(bydim.get(d-1,[]))}
        rows=[]
        for face in bydim.get(d,[]):
            v=0
            for i in range(n):
                if face&(1<<i): v ^= 1<<lo[face^(1<<i)]
            rows.append(v)
        ranks[d]=rank_mod2(rows)
    out={}
    for d in bydim:
        x=len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0: x-=1
        if x: out[d]=x
    return out


def check(a,b,t):
    n=a+b
    faces=[s for s in range(1<<n) if allowed(s,a,b,t)]
    fac=[s for s in faces if all(not allowed(s|(1<<i),a,b,t) for i in range(n) if not(s&(1<<i)))]
    poly=Counter(f.bit_count() for f in faces)
    expected=Counter({k:comb(a,k)+comb(b,k) for k in range(max(a,b)+1)})
    expected[0]-=1
    expected[2]+=a*b
    expected[3]+=t*(a+b-2)
    expected[4]+=comb(t,2)
    assert all(poly[k]==expected[k] for k in set(poly)|set(expected)),(a,b,t,poly,expected)
    maxpoly=Counter(s.bit_count() for s in fac)
    want=Counter({a:1,b:1})
    if a==b:want[a]=2
    want[2]+=(a-t)*(b-t)
    want[3]+=t*(a+b-2*t)
    want[4]+=comb(t,2)
    assert maxpoly==want,(a,b,t,maxpoly,want)
    betti=betti_mod2(faces,n)
    expected_betti={}
    if t==0: expected_betti[1]=a*b-1
    else:
        if (a-t)*(b-t):expected_betti[1]=(a-t)*(b-t)
        if comb(t-1,2):expected_betti[2]=comb(t-1,2)
    assert betti==expected_betti,(a,b,t,betti,expected_betti)
    return len(faces),len(fac)


def main():
    profiles=0; subsets=0; facets=0
    for a in range(3,6):
        for b in range(a,6):
            for t in range(a+1):
                f,g=check(a,b,t)
                profiles+=1;subsets+=2**(a+b);facets+=g
    print(f'VERIFY_OK parameter_profiles={profiles} all_masks={subsets} maximal_sets={facets} direct_degree_constraint=PASS complete_face_polynomial=PASS facet_polynomial=PASS mod2_homology=PASS')

if __name__=='__main__':main()
