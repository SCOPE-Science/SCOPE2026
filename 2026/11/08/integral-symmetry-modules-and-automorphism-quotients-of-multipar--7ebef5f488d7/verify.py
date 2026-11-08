"""Independent signed-chain and finite-group checks for multipartite r-independence complexes.
Only standard Python libraries. Run: python verify.py
"""
from itertools import permutations, product, combinations
from collections import defaultdict
from math import comb, factorial


def group_elements(sizes):
    groups = []
    p=0
    for a in sizes:
        groups.append(list(range(p,p+a)));p+=a
    sizeclasses=defaultdict(list)
    for i,a in enumerate(sizes):sizeclasses[a].append(i)
    source_part_perms=[list(permutations(g)) for g in groups]
    class_options = []
    for indices in sizeclasses.values(): class_options.append(list(permutations(indices)))
    for pparts in product(*class_options):
        source_to_target={}
        for indices, permuted in zip(sizeclasses.values(),pparts):
            source_to_target.update(zip(indices,permuted))
        for within in product(*source_part_perms):
            perm=[-1]*p
            for i,block in enumerate(within):
                target=groups[source_to_target[i]]
                for idx, orig_vertex in enumerate(block): perm[orig_vertex]=target[idx]
            yield tuple(perm),source_to_target,groups

def trace_wedge(permutation,r,domain=None):
    if domain is None:domain=tuple(range(len(permutation)))
    N=len(domain)
    if r<0 or r>=N:return 0
    unseen=set(domain);cycles=[]
    while unseen:
        v=min(unseen);u=v;l=0
        while u in unseen:
            unseen.remove(u);l+=1;u=permutation[u]
        assert u==v
        cycles.append(l)
    coefficients=[1]
    for c in cycles:
        next_coeff=coefficients+[0]*c
        for k,x in enumerate(coefficients):next_coeff[k+c]+=(-1)**(c+1)*x
        coefficients=next_coeff
    # division by (1+t)
    res=0
    for i in range(r+1):
        res=coefficients[i]-res if i<len(coefficients) else -res
    return res

def sign_on_face(face, perm):
    sorted_image=[perm[v] for v in face]
    inv=sum(sorted_image[i]>sorted_image[j] for i in range(len(face)) for j in range(i+1,len(face)))
    return (-1)**inv

def is_face(face,groups,r):
    if len(face)<=r:return True
    return any(set(face).issubset(set(b)) for b in groups)

def signed_lefschetz(perm,groups,r):
    N=len(perm);ans=-1
    for q in range(1,N+1):
        for face in combinations(range(N),q):
            if not is_face(face,groups,r):continue
            if set(perm[v] for v in face)!=set(face):continue
            ans+=(-1)**(q-1)*sign_on_face(face,perm)
    return ans

def rank_prediction(sizes,r):
    n=sum(sizes)
    def choose(n,k):return comb(n,k) if 0<=k<=n else 0
    return choose(n-1,r)-sum(choose(a-1,r) for a in sizes)

def verify(sizes):
    N=sum(sizes);group=list(group_elements(sizes));num=len(group)
    expect=1
    for a in sizes:expect*=factorial(a)
    for a in set(sizes):expect*=factorial(sizes.count(a))
    assert num==expect,(sizes,num,expect)
    type_count=len(set(sizes))
    check=0
    for r in range(1,N+1):
        total_trace=0
        for perm,partmap,parts in group:
            tr=trace_wedge(perm,r)
            for i,part in enumerate(parts):
                if partmap[i]==i:tr-=trace_wedge(perm,r,tuple(part))
            lef=signed_lefschetz(perm,parts,r)
            assert tr==(-1)**(r-1)*lef,(sizes,r,perm,tr,lef)
            if all(perm[i]==i for i in range(N)):
                assert tr==rank_prediction(sizes,r),(sizes,r,tr)
            total_trace+=tr;check+=1
        inv=total_trace//num
        assert total_trace%num==0
        pred=comb(type_count-1,r) if r<=type_count-1 else 0
        assert inv==pred,(sizes,r,inv,pred)
    return check,num

if __name__=='__main__':
    cases=[[1,1,1],[2,2,2],[1,2,3],[2,3,3],[1,1,2,2],[1,2,2,3],[2,3,4],[1,1,1,2],[1,2,3,3],[2,2,2,2]]
    total=0
    for sizes in cases:
        checks,group_size=verify(sizes)
        total+=checks
        print(f"sizes={sizes} group_order={group_size} checks={checks} distinct_sizes={len(set(sizes))}")
    print(f"ALL_VERIFY_OK signed_chain_comparisons={total} cases={len(cases)}")

# Completely independent invariant-chain computation of orbit-space rational
# homology over a large prime (avoiding use of the homology/trace formula).
def rank_mod_prime(rows,p):
    if not rows:return 0
    v=[list(map(lambda x:x%p,row)) for row in rows]
    ncol=len(v[0]);pivot=0
    for j in range(ncol):
        found=next((k for k in range(pivot,len(v)) if v[k][j]),None)
        if found is None:continue
        v[pivot],v[found]=v[found],v[pivot]
        inverse=pow(v[pivot][j],-1,p)
        v[pivot]=[(x*inverse)%p for x in v[pivot]]
        for i in range(pivot+1,len(v)):
            if v[i][j]:
                fac=v[i][j]
                v[i]=[(x-fac*y)%p for x,y in zip(v[i],v[pivot])]
        pivot+=1
        if pivot==len(v):break
    return pivot

def quotient_homology_direct(sizes,r,p=1009):
    group=list(group_elements(sizes));perms=[g[0] for g in group]
    parts=group[0][2];N=sum(sizes)
    face_sets={q:[face for face in combinations(range(N),q+1) if is_face(face,parts,r)]
               for q in range(N)}
    basis={};chains={};face_class={}
    for q,faces in face_sets.items():
        remain=set(faces);bases=[];lookup={}
        while remain:
            rep=min(remain);signs={};bad=False
            for perm in perms:
                image=tuple(sorted(perm[x] for x in rep))
                si=sign_on_face(rep,perm)
                if image in signs and signs[image]!=si:bad=True
                signs[image]=si
            for image in signs: remain.discard(image)
            if bad:continue
            index=len(bases);bases.append(rep)
            for image,sign in signs.items():lookup[image]=(index,sign)
        basis[q]=bases;face_class[q]=lookup
        chains[q]=len(bases)
    ranks={}
    for q in range(N):
        if not chains[q]:ranks[q]=0;continue
        if q==0:
            # reduced augmentation to the empty face
            ranks[q]=1
            continue
        mat=[[0]*chains[q] for _ in range(chains[q-1])]
        for col,rep in enumerate(basis[q]):
            # invariant orbit sum represented by this column, exact signs
            members=[(face,si) for face,(index,si) in face_class[q].items() if index==col]
            boundary=defaultdict(int)
            for face,si in members:
                for j in range(len(face)):
                    reduced_face=face[:j]+face[j+1:]
                    boundary[reduced_face]+=(-1)**j*si
            for row,target_face in enumerate(basis[q-1]):
                mat[row][col]=boundary[target_face]
        ranks[q]=rank_mod_prime(mat,p)
    betti={q:chains[q]-ranks[q]-ranks.get(q+1,0) for q in range(N) if chains[q]}
    return {q:b for q,b in betti.items() if b}

if __name__=='__main__':
    test_cases=[[1,2,3],[2,2,2],[1,1,2,2],[2,3,3]]
    checks=0
    for sizes in test_cases:
        t=len(set(sizes))
        for r in range(1,sum(sizes)+1):
            expected={r-1:comb(t-1,r)} if r<t else {}
            found=quotient_homology_direct(sizes,r)
            assert found==expected,(sizes,r,found,expected)
            checks+=1
        print('direct_orbit_chains',sizes,'PASS')
    print('DIRECT_ORBIT_HOMOLOGY_OK cases=',checks)
