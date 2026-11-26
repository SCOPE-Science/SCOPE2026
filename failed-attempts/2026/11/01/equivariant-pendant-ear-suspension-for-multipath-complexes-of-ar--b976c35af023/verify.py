#!/usr/bin/env python3
"""Independent finite checks for the bidirected pendant-two-ear multipath theorem.
Run with Python 3 standard library: python3 verify.py
All-order assertions are proved mathematically in RESULT.md, not inferred here.
"""
from itertools import permutations, product
from collections import defaultdict


def extension(base_vertices, base_arcs, roots):
    """Return labeled arcs; new internal/terminal vertices are all distinct."""
    arc=list(base_arcs)
    for i,u in enumerate(roots):
        v=base_vertices+2*i
        w=v+1
        arc.extend([(u,v),(v,u),(v,w),(w,v)])
    return arc


def face(arcs, mask):
    """Exact path-forest test: indegree/outdegree <=1 and no directed cycle."""
    incoming=set(); outgoing={}
    for j,(u,v) in enumerate(arcs):
        if not mask & (1<<j):continue
        if u in outgoing or v in incoming:return False
        outgoing[u]=v;incoming.add(v)
    for start in outgoing:
        visited=set();u=start
        while u in outgoing:
            if u in visited:return False
            visited.add(u);u=outgoing[u]
    return True


def retract(mask, base_length, ears):
    new=mask
    for i in range(ears):
        p,q,a,b=(base_length+4*i+j for j in range(4))
        if mask>>p&1:
            new=(new & ~(1<<p)) | (1<<a)
        if mask>>q&1:
            new=(new & ~(1<<q)) | (1<<b)
    return new


def check(base_n,base_arcs,roots):
    a=extension(base_n,base_arcs,roots)
    k=len(base_arcs);m=len(roots)
    faces=0;core_faces=set();image=set()
    for mask in range(1<<len(a)):
        if not face(a,mask):continue
        faces+=1
        r=retract(mask,k,m)
        assert face(a,r),(a,mask,r,'retraction simplex')
        assert face(a,mask|r),(a,mask,r,'contiguity')
        assert retract(r,k,m)==r
        image.add(r)
        if all(not(mask>>(k+4*i)&3) for i in range(m)):
            core_faces.add(mask)
    assert image==core_faces,(len(image),len(core_faces),'image equality')
    expected_core=0
    # Exact join count: each base face times independently (none,a,b) for each ear.
    base_face_count=sum(face(base_arcs,mask) for mask in range(1<<k))
    expected_core=base_face_count*3**m
    assert len(core_faces)==expected_core,(len(core_faces),expected_core)
    print('CASE base_vertices=%s base_arcs=%s roots=%s total_faces=%s retract_target=%s CHECK_OK'%(
        base_n,k,str(roots),faces,len(core_faces)))
    return faces


def check_equivariance(m):
    a=extension(1,[],[0]*m)
    masks=[k for k in range(1<<len(a)) if face(a,k)]
    for pi in permutations(range(m)):
        for reverse in (False,True):
            index={}
            for i in range(m):
                for j in range(4):
                    new_j=j^1 if reverse else j
                    index[4*i+j]=4*pi[i]+new_j
            for mask in masks:
                moved=0
                for p in range(len(a)):
                    if mask>>p&1:moved |= 1<<index[p]
                assert face(a,moved)
                one=retract(moved,0,m)
                r=retract(mask,0,m)
                two=0
                for p in range(len(a)):
                    if r>>p&1:two |=1<<index[p]
                assert one==two
            # The join fundamental chain transforms by the claimed 1-dimensional character.
            # The basis order is increasing arm index; permutation causes its own orientation sign.
            inv=0
            for i in range(m):
                for j in range(i+1,m):
                    inv+=(pi[i]>pi[j])
            expected=(-1)**(inv+(m if reverse else 0))
            for choices in product((0,1),repeat=m):
                transformed=[None]*m
                for i,t in enumerate(choices):
                    transformed[pi[i]]=1-t if reverse else t
                ratio=(-1)**(sum(choices)-sum(transformed)+inv)
                assert ratio==expected
    print('EQUIVARIANCE spider_m=%s group_elements=%s faces=%s CHECK_OK'%(
        m,2*__import__('math').factorial(m),len(masks)))


def ranks_mod2_spider(m):
    a=extension(1,[],[0]*m)
    by_k=[[] for _ in range(2*m+1)]
    for mask in range(1<<len(a)):
        if face(a,mask):by_k[mask.bit_count()].append(mask)
    if by_k and not by_k[-1]:
        while by_k and not by_k[-1]:by_k.pop()
    ranks=[]
    for k in range(1,len(by_k)):
        lower={x:i for i,x in enumerate(by_k[k-1])}
        pivot={}
        for sig in by_k[k]:
            col=0
            q=sig
            while q:
                x=q&-q;q-=x
                col^=1<<lower[sig^x]
            while col:
                j=(col&-col).bit_length()-1
                if j not in pivot:
                    pivot[j]=col
                    break
                col^=pivot[j]
        ranks.append(len(pivot))
    betti=[]
    for k,fs in enumerate(by_k):
        betti.append(len(fs)-(ranks[k-1] if k else 0)-(ranks[k] if k<len(ranks) else 0))
    assert betti==[1 if k==m else 0 for k in range(len(by_k))],(m,betti)
    print('SPIDER spider_m=%s fvector_aug=%s reduced_betti=%s CHECK_OK'%(
        m,list(map(len,by_k)),betti))


def main():
    # Include directed cycles, two-cycles, distinct and repeated attachment roots.
    cases=[
        (1,[],[0]),(1,[],[0,0]),(1,[],[0,0,0]),(1,[],[0,0,0,0]),
        (2,[(0,1)], [0,1]),
        (2,[(0,1),(1,0)], [0,1]),
        (3,[(0,1),(1,2),(2,0)], [0,1]),
        (3,[(0,1),(1,0),(1,2),(2,1)], [1]),
        (3,[(0,1),(1,0),(0,2),(2,0),(1,2),(2,1)], [0]),
        (3,[(0,1),(1,0),(0,2),(2,0),(1,2),(2,1)], [0,0]),
    ]
    for case in cases:check(*case)
    for m in (1,2,3,4):ranks_mod2_spider(m)
    for m in (1,2,3,4):check_equivariance(m)
    print('BIDIRECTED_EAR_EQUIVARIANT_SUSPENSION_CHECKS_OK')
if __name__=='__main__':main()
