#!/usr/bin/env python3
"""Finite checks for coordinate-transposition geometric fixed-point homology.
No third-party packages are required. Finite checks corroborate, but do not
replace, the integral proof of the all-dimensional assertion.
"""
from itertools import combinations
from collections import defaultdict

def cube_orbits(n):
    unseen=set(range(1<<n)); result=[]
    while unseen:
        x=min(unseen)
        y=(x & ~3)|((x&1)<<1)|((x&2)>>1)
        orb=tuple(sorted({x,y})); result.append(orb)
        unseen.difference_update(orb)
    return result

def face_lists(n):
    orbs=cube_orbits(n)
    q=len(orbs)
    compat=[0]*q
    for i in range(q):
        for j in range(i+1,q):
            if all((a^b).bit_count()<=2 for a in orbs[i] for b in orbs[j]):
                compat[i]|=1<<j
    faces_by_dim=defaultdict(list)
    faces_by_dim[-1]=[0]
    def visit(face,possible,sz):
        while possible:
            bit=possible&-possible; possible-=bit
            j=bit.bit_length()-1
            newface=face|bit
            faces_by_dim[sz].append(newface)
            visit(newface,possible&compat[j],sz+1)
    visit(0,(1<<q)-1,0)
    return orbs,compat,faces_by_dim

def gf2rank(columns):
    piv={}
    for val in columns:
        while val:
            bit=val.bit_length()-1
            if bit not in piv:
                piv[bit]=val
                break
            val^=piv[bit]
    return len(piv)

def betti_mod2(faces):
    maxdim=max(faces)
    ranks={}
    for dim in range(1,maxdim+1):
        prev={face:i for i,face in enumerate(faces[dim-1])}
        col=[]
        for face in faces[dim]:
            v=0; t=face
            while t:
                bit=t&-t; t-=bit
                v^=1<<prev[face^bit]
            col.append(v)
        ranks[dim]=gf2rank(col)
    ans={d:len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)
         for d in range(maxdim+1)}
    ans[0]-=1
    return {d:b for d,b in ans.items() if b}

def c_m(m):
    if m<3: return 0
    return sum((j+1)*((1<<(m-2))-(1<<(i-1)))
               for i in range(1,m) for j in range(i))

def orbit_label(orbit):
    z=orbit[0]>>2
    low={x&3 for x in orbit}
    if low=={0}:return ('A',z)
    if low=={3}:return ('B',z)
    assert low=={1,2}
    return ('C',z)

def model_compatible(label1,label2):
    t,z=label1; u,w=label2
    d=(z^w).bit_count()
    if t==u=='C':return False
    if t=='C' or u=='C':return d<=1
    if t!=u:return d==0
    return d<=2

def main():
    case_count=0; total_faces=0
    for n in range(2,8):
        orbs,compat,faces=face_lists(n)
        lab=list(map(orbit_label,orbs))
        assert len(orbs)==3*(1<<(n-2)),(n,len(orbs))
        for i,j in combinations(range(len(lab)),2):
            observed=bool(compat[min(i,j)] & (1<<max(i,j)))
            assert observed==model_compatible(lab[i],lab[j]),(n,i,j)
        observed=betti_mod2(faces)
        m=n-2
        expected={} if n==2 else {2:(m-1)*(1<<m)+1}
        if m>=3: expected[3]=2*c_m(m)
        assert observed==expected,(n,observed,expected)
        count=sum(map(len,faces.values()))
        total_faces+=count; case_count+=1
        print(f'n={n}: orbit_vertices={len(orbs)} faces_including_empty={count} '
              f'reduced_betti_mod2={observed}',flush=True)
    assert total_faces==10321,(total_faces,'expected 10321')
    print(f'ALL_VERIFY_OK cases={case_count} face_sets={total_faces}',flush=True)

if __name__=='__main__':main()
