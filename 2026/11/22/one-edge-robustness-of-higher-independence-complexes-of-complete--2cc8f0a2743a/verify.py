#!/usr/bin/env python3
"""Direct exhaustive checks of edge-punctured multipartite higher-independence complexes.
Uses induced-component enumeration, verifies each elementary simplicial collapse, and checks
all residual mod-two boundary ranks, never extrapolating finite samples to infinite claims.
"""
from itertools import combinations, product
from math import comb

def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def subsets(items,k):
    return combinations(items,k)

def rank_binary(columns):
    pivots={}
    for x in columns:
        while x:
            k=x.bit_length()-1
            if k in pivots: x^=pivots[k]
            else:
                pivots[k]=x
                break
    return len(pivots)

def check(parts,r):
    n=sum(parts)
    classes=[]
    offset=0
    for p in parts:
        classes.append(tuple(range(offset,offset+p)))
        offset+=p
    u,v=classes[0][0],classes[1][0]
    membership={x:i for i,vs in enumerate(classes) for x in vs}
    def allowed(s,deleted):
        rem=set(s)
        while rem:
            start=next(iter(rem))
            seen={start}
            rem.remove(start)
            stack=[start]
            while stack:
                x=stack.pop()
                for y in tuple(rem):
                    if membership[x]!=membership[y] and (not deleted or frozenset((x,y))!=frozenset((u,v))):
                        rem.remove(y)
                        seen.add(y)
                        stack.append(y)
            if len(seen)>r: return False
        return True
    X={frozenset(s) for k in range(n+1) for s in subsets(range(n),k) if allowed(s,False)}
    Y={frozenset(s) for k in range(n+1) for s in subsets(range(n),k) if allowed(s,True)}
    assert X<=Y
    new=set()
    for side,opposite in ((0,v),(1,u)):
        cls=classes[side]
        anchor=cls[0]
        for R in subsets(cls[1:],r-1):
            new.add(frozenset((u,v,*R)))
    assert Y-X==new,(parts,r,'unexpected new faces',Y-X^new)
    current=set(Y)
    def collapse(face,top):
        assert face in current and top in current and len(top)==len(face)+1 and face<top
        extensions=[s for s in current if face<s]
        assert extensions==[top],(parts,r,face,extensions)
        current.remove(face);current.remove(top)
    for top in sorted(new,key=lambda s:tuple(sorted(s))):
        if len(top&set(classes[0]))==r: face=top-{u}
        else: face=top-{v}
        collapse(face,top)
    for cls in classes:
        anchor=cls[0]
        others=cls[1:]
        for k in range(len(others),r-1,-1):
            for S in subsets(others,k):
                face=frozenset(S)
                collapse(face,face|{anchor})
    assert not any(len(s)>r for s in current)
    assert all(frozenset(s) in current for k in range(min(r-1,n)+1) for s in subsets(range(n),k))
    dims={k:sorted(tuple(sorted(s)) for s in current if len(s)==k) for k in range(r+1)}
    rank={1:0}
    for k in range(2,r+1):
        rows={face:i for i,face in enumerate(dims[k-1])}
        columns=[]
        for s in dims[k]:
            bits=0
            for f in subsets(s,k-1): bits^=1<<rows[f]
            columns.append(bits)
        rank[k]=rank_binary(columns)
    expected=choose(n-1,r)-sum(choose(len(c)-1,r) for c in classes)-choose(len(classes[0])-1,r-1)-choose(len(classes[1])-1,r-1)
    equivalent=choose(n-1,r)-choose(len(classes[0]),r)-choose(len(classes[1]),r)-sum(choose(len(c)-1,r) for c in classes[2:])
    assert expected==equivalent and expected>=0
    for dim in range(r):
        betti=len(dims[dim+1])-rank.get(dim+1,0)-rank.get(dim+2,0)-(1 if dim==0 else 0)
        assert betti==(expected if dim==r-1 else 0),(parts,r,dim,betti,expected)
    return len(Y),len(new),(len(Y)-len(current))//2,expected

def main():
    cases=0; total_faces=0; total_pairs=0
    examples=[]
    for number_parts in range(2,5):
        for parts in product(range(1,5),repeat=number_parts):
            n=sum(parts)
            if n>9: continue
            for r in range(2,n+1):
                faces,new,pairs,beta=check(parts,r)
                cases+=1;total_faces+=faces;total_pairs+=pairs
                if (parts,r) in {((3,4),2),((3,2,2),3),((2,2,2,2),3),((3,3,2),3)}:
                    examples.append((parts,r,faces,new,pairs,beta))
    print('PASS')
    print('cases:',cases)
    print('total_face_examinations:',total_faces)
    print('verified_elementary_collapses:',total_pairs)
    print('examples (parts,r,faces,new_r_faces,elementary_pairs,top_betti):')
    for e in examples:print(e)
if __name__=='__main__':main()
