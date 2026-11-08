#!/usr/bin/env python3
"""Reproducible integral Morse and rational character verification for a finite graph complex."""
from itertools import combinations
from collections import Counter, deque
from math import comb

N=16
MASK=(1<<N)-1
ORDER=(12,4,5,10,15,1,2,11,6,13,9,0,8,7,14,3)

def adjacencies():
    a=[0]*N
    for i in range(4):
        for j in range(4):
            v=4*i+j
            for di,dj in ((1,0),(0,1)):
                if i+di<4 and j+dj<4:
                    w=4*(i+di)+(j+dj)
                    a[v]|=1<<w; a[w]|=1<<v
    return a

def independent_four():
    adj=adjacencies()
    ans=[]
    for c in combinations(range(N),4):
        m=sum(1<<i for i in c)
        if all(adj[i]&m==0 for i in c):ans.append(m)
    assert len(ans)==405, len(ans)
    return ans

def enumerate_faces(ind):
    facets=[MASK^t for t in ind]
    faces={0}
    for f in facets:
        t=f
        while t:
            faces.add(t)
            t=(t-1)&f
    # Fully independent second method, test EVERY one of the 2^16 subsets.
    truth={s for s in range(1<<N) if any((s&t)==0 for t in ind)}
    assert faces==truth
    assert len(faces)==60724
    assert len(set(facets))==405
    return faces-{0}

def matching(faces):
    unmatched=set(faces)
    pairs={}
    for j in ORDER:
        bit=1<<j
        stage=[s for s in unmatched if not s&bit and (s|bit) in unmatched]
        for lower in stage:
            upper=lower|bit
            unmatched.remove(lower);unmatched.remove(upper)
            pairs[lower]=upper
    c=Counter(s.bit_count()-1 for s in unmatched)
    assert c=={0:1,8:84},c
    assert len(pairs)==(len(faces)-85)//2
    return pairs,unmatched

def certify_acyclic(faces,pairs):
    F=set(faces)
    indeg={s:0 for s in F}
    out={s:[] for s in F}
    covers=0
    for upper in F:
        m=upper
        while m:
            bit=m&-m;m-=bit
            lower=upper^bit
            if not lower:continue
            assert lower in F
            covers+=1
            if pairs.get(lower)==upper:
                out[upper].append(lower);indeg[lower]+=1
            else:
                out[lower].append(upper);indeg[upper]+=1
    qu=deque(s for s in F if indeg[s]==0)
    visited=0
    while qu:
        node=qu.popleft();visited+=1
        for nex in out[node]:
            indeg[nex]-=1
            if indeg[nex]==0:qu.append(nex)
    assert visited==len(F),(visited,len(F))
    return covers

def compose(p,q):return tuple(p[q[i]] for i in range(N))

def permutation_sign(x):
    # Induced orientation on the simplex spanned by sorted vertex indices.
    parity=sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x)))%2
    return -1 if parity else 1

def reduced_lefschetz(faces,p):
    result=-1 # orientation of empty simplex: -1 in the reduced Lefschetz sum
    for s in faces:
        indices=[i for i in range(N) if (s>>i)&1]
        image=sum(1<<p[i] for i in indices)
        if image==s:
            result+=((-1)**(len(indices)-1))*permutation_sign([p[i] for i in indices])
    return result

def square_perm(p):
    squares=[frozenset((4*i+j,4*i+j+1,4*(i+1)+j,4*(i+1)+j+1)) for i in range(3) for j in range(3)]
    return [squares.index(frozenset(p[t] for t in sq)) for sq in squares]

def characters(faces):
    r=tuple(4*j+(3-i) for i in range(4) for j in range(4))
    s=tuple(4*i+(3-j) for i in range(4) for j in range(4))
    r2=compose(r,r);r3=compose(r,r2)
    group=(('e',tuple(range(N)),1),('r',r,1),('r2',r2,1),('r3',r3,1),('s',s,-1),('rs',compose(r,s),-1),('r2s',compose(r2,s),-1),('r3s',compose(r3,s),-1))
    outputs=[]
    for name,p,det in group:
        v=reduced_lefschetz(faces,p)
        sp=square_perm(p)
        fixed=sum({sp[z] for z in c}==set(c) for c in combinations(range(9),3))
        assert v==det*fixed,(name,v,det,fixed)
        outputs.append((name,v,fixed))
    assert [x[1] for x in outputs]==[84,0,4,0,-10,-10,-10,-10]
    return outputs

def main():
    ind=independent_four()
    faces=enumerate_faces(ind)
    fvec=Counter(s.bit_count()-1 for s in faces)
    assert fvec=={0:16,1:120,2:560,3:1820,4:4368,5:8008,6:11440,7:12870,8:11440,9:7096,10:2580,11:405},fvec
    print('FACES_OK',len(ind),'facets',len(faces),'nonempty faces')
    print('FVECTOR_OK',sorted(fvec.items()))
    pairs,crit=matching(faces)
    print('MATCHING_OK',len(pairs),'pairs',dict(Counter(s.bit_count()-1 for s in crit)))
    cov=certify_acyclic(faces,pairs)
    print('ACYCLIC_OK',len(faces),'nodes',cov,'cover incidences')
    print('HOMOTOPY_OK wedge_of_84_S8')
    for n,t,f in characters(faces):print('CHARACTER_OK',n,t,f)
    print('CHARACTER_MODEL_OK orientation_twist_3_subsets_of_9_squares')
    print('ALL_VERIFY_OK')
if __name__=='__main__':main()
