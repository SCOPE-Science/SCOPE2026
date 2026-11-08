"""Exact finite checks for higher-independence complexes of path-arm spiders.

Standard Python only. Direct face enumeration; no theorem formula is used to
build the complexes or calculate their homology and Lefschetz characters.
"""
from collections import defaultdict
from itertools import permutations
from math import comb


def graph(lengths):
    adjacency=[0]*(1+sum(lengths)); arms=[]; j=1
    for length in lengths:
        arm=[]; previous=0
        for _ in range(length):
            adjacency[previous] |=1<<j
            adjacency[j] |=1<<previous
            arm.append(j); previous=j; j+=1
        arms.append(tuple(arm))
    return adjacency,arms


def qualifies(mask,r,adjacency):
    remaining=mask
    while remaining:
        pending=remaining & -remaining
        component=0
        while pending:
            bit=pending & -pending; pending-=bit
            if component & bit: continue
            component|=bit
            pending|= adjacency[bit.bit_length()-1]&mask&~component
        if component.bit_count()>r: return False
        remaining &=~component
    return True


def all_faces(lengths,r):
    adjacency, arms=graph(lengths)
    return [f for f in range(1<<len(adjacency)) if qualifies(f,r,adjacency)]


def rank2(columns):
    pivots={}
    for col in columns:
        while col:
            head=col.bit_length()-1
            if head not in pivots: pivots[head]=col; break
            col ^= pivots[head]
    return len(pivots)


def homology(faces,n):
    levels=defaultdict(list)
    for f in faces: levels[f.bit_count()].append(f)
    rank={}
    for i in range(1,n+1):
        previous={f:j for j,f in enumerate(levels[i-1])}
        columns=[]
        for face in levels[i]:
            boundary=0; bits=face
            while bits:
                bit=bits&-bits;bits-=bit
                boundary^=1<<previous[face^bit]
            columns.append(boundary)
        rank[i]=rank2(columns)
    return {i-1:len(levels[i])-rank.get(i,0)-rank.get(i+1,0)
            for i in range(n+1) if len(levels[i])-rank.get(i,0)-rank.get(i+1,0)}


def sign_on_face(face,perm):
    order=[perm[j] for j in range(len(perm)) if face>>j&1]
    return -1 if sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))%2 else 1


def transform(face,perm):
    result=0
    for i,p in enumerate(perm):
        if face>>i&1: result|=1<<p
    return result


def permute_equal_length_arms(lengths,arm_perm):
    adjacency,arms=graph(lengths); full=list(range(len(adjacency)))
    for i,arm in enumerate(arms):
        target=arms[arm_perm[i]]
        assert len(arm)==len(target)
        for u,v in zip(arm,target):full[u]=v
    assert len(set(full))==len(full)
    return full


def perm_sign_on_subset(perm,subset):
    images=[perm[x] for x in sorted(subset)]
    return -1 if sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))%2 else 1


def aug_exterior_character(arm_perm,t):
    k=len(arm_perm); cycles=[];seen=set()
    for i in range(k):
        if i in seen:continue
        current=i;cycle_len=0
        while current not in seen:
            seen.add(current);cycle_len+=1;current=arm_perm[current]
        cycles.append(cycle_len)
    coeff=[1]+[0]*k
    for length in cycles:
        for j in range(k,length-1,-1):
            coeff[j]+=(-1 if length%2==0 else 1)*coeff[j-length]
    q=[0]*k
    q[0]=coeff[0]
    for j in range(1,k): q[j]=coeff[j]-q[j-1]
    return q[t]


def direct_lefschetz(faces,perm):
    total=0
    for face in faces:
        if transform(face,perm)==face:
            total+= (-1 if face.bit_count()%2==0 else 1)*sign_on_face(face,perm)
    return total


def check_matching_acyclic(lengths,r):
    adjacency,arms=graph(lengths)
    B=sum(L-1 for L in lengths)
    internal={v for arm in arms for v in arm[:-1]}
    leaf=[arm[-1] for arm in arms]
    link=[f for f in all_faces(lengths,r) if not(f&1) and qualifies(f|1,r,adjacency)]
    # Vertex 0 is the distinguished hub, and the link does not contain it.
    edges={f:[] for f in link}; indeg={f:0 for f in link};fset=set(link)
    for lower in link:
        for v in range(1,len(adjacency)):
            bit=1<<v
            if lower&bit or lower|bit not in fset:continue
            upper=lower|bit
            first=next((arm[-1] for arm in arms if not all((lower>>x)&1 for x in arm[:-1])),None)
            is_matched=(first is not None and v==first)
            x,y=(lower,upper) if is_matched else (upper,lower)
            edges[x].append(y);indeg[y]+=1
    Q=[f for f in link if indeg[f]==0];count=0
    while Q:
        x=Q.pop();count+=1
        for y in edges[x]:
            indeg[y]-=1
            if indeg[y]==0:Q.append(y)
    if count!=len(link):raise AssertionError('Directed matching cycle')
    critical=[f for f in link if not any(not all((f>>x)&1 for x in arm[:-1]) for arm in arms)]
    t=r-1-B
    expected=sum(comb(len(lengths),j) for j in range(0,min(len(lengths),t)+1)) if t>=0 else 0
    if len(critical)!=expected:raise AssertionError('critical cells')
    return len(link),len(critical)


def main():
    cases=0;faces_seen=0;matching_cases=0;matching_faces=0;characters=0
    profiles=[(2,2,3),(2,3,3),(3,3,3),(2,3,4),(2,2,4),
              (2,2,2,3),(2,2,3,3),(3,3,4)]
    for lengths in profiles:
        n=1+sum(lengths);k=len(lengths);B=sum(v-1 for v in lengths)
        for r in range(max(lengths),B+k+2):
            faces=all_faces(lengths,r)
            result=homology(faces,n)
            t=r-1-B
            expected={} if t<0 or t>=k else {r-1:comb(k-1,t)}
            if result!=expected:raise AssertionError(('homology',lengths,r,result,expected))
            cases+=1;faces_seen+=len(faces)
            if n<=10:
                L,C=check_matching_acyclic(lengths,r)
                matching_cases+=1;matching_faces+=L
            if not(0<=t<k):continue
            permutations_to_test=[]
            for a in permutations(range(k)):
                if all(lengths[i]==lengths[a[i]] for i in range(k)):
                    permutations_to_test.append(a)
            for a in permutations_to_test:
                perm=permute_equal_length_arms(lengths,a)
                lhs=direct_lefschetz(faces,perm)
                internal=[x for arm in graph(lengths)[1] for x in arm[:-1]]
                eps=perm_sign_on_subset(perm,internal)
                rhs=(-1 if (r-1)%2 else 1)*eps*aug_exterior_character(a,t)
                if lhs!=rhs:raise AssertionError(('character',lengths,r,a,lhs,rhs))
                characters+=1
    print('ALL_VERIFY_OK cases=%d face_instances=%d matching_cases=%d matching_faces=%d signed_character_checks=%d' % (
        cases,faces_seen,matching_cases,matching_faces,characters))

if __name__=='__main__':main()
