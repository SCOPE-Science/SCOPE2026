"""Direct finite persistent-homology check for dissociation matching deletion."""
from itertools import combinations
from collections import Counter

def face_ok(a,b,t,S):
    aset={v for v in S if v<a}; bset={v-a for v in S if v>=a}
    for i in aset:
        if sum(not (i==j and i<t) for j in bset)>1:return False
    for j in bset:
        if sum(not (i==j and j<t) for i in aset)>1:return False
    return True

def profile(a,b):
    m=min(a,b)
    faces=[]
    for z in range(1,a+b+1):
        for S in combinations(range(a+b),z):
            for t in range(m+1):
                if face_ok(a,b,t,S):
                    faces.append((t,z-1,S));break
    faces.sort()
    ix={r[2]:i for i,r in enumerate(faces)}
    pivots={};paired=set();births=[]; bars=Counter()
    for j,(t,dim,S) in enumerate(faces):
        col=0
        if dim>0:
            for v in S:
                facet=tuple(x for x in S if x!=v)
                col ^= 1<<ix[facet]
        while col:
            pivot=col.bit_length()-1
            if pivot in pivots:col^=pivots[pivot]
            else:break
        if col:
            pivots[pivot]=col
            paired.add(pivot)
            oldt,olddim,_=faces[pivot]
            if oldt<t:bars[(olddim,oldt,t)]+=1
        else:
            births.append(j)
    for j in births:
        if j not in paired:
            t,dim,_=faces[j]
            if dim>0:bars[(dim,t,m+1)]+=1
    expected=Counter()
    expected[(1,0,1)]=a+b-2
    for k in range(1,m):
        expected[(1,0,k+1)]=(a-k)*(b-k)-(a-k-1)*(b-k-1)
    for k in range(3,m+1):expected[(2,k,m+1)]=k-2
    expected=+expected
    bars=+bars
    assert bars==expected,((a,b),bars,expected)
    return len(faces),bars

if __name__=='__main__':
    cnt=0;fac=0
    for a in range(3,6):
        for b in range(a,6):
            n,bars=profile(a,b)
            cnt+=1;fac+=n
            print('a=%d b=%d total_faces=%d bars=%s'%(a,b,n,sorted((k,v) for k,v in bars.items())))
    print('MATCHING_DELETION_INTEGRAL_STRUCTURE_MOD2_PERSISTENCE_PASS profiles=%d faces=%d'%(cnt,fac))
