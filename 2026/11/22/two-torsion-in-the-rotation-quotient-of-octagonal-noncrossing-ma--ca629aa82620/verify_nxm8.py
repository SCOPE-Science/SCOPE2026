#!/usr/bin/env python3
"""Exact, standalone verification of polygonal noncrossing-matching orbit spaces.
Only the Python standard library is required. All face orbits are rebuilt.
"""
from collections import Counter, defaultdict
from itertools import combinations, product


def original_faces(n):
    edges=list(combinations(range(n),2))
    def compatible(a,b):
        x,y=a; u,v=b
        return not (len({x,y,u,v})<4 or x<u<y<v or u<x<v<y)
    ok={(i,j):compatible(edges[i],edges[j]) for i,j in combinations(range(len(edges)),2)}
    faces=[]
    for k in range(1,n//2+1):
        faces += [frozenset(s) for s in combinations(range(len(edges)),k)
                  if all(ok[i,j] for i,j in combinations(s,2))]
    return edges,faces


def group(n,edges,dihedral):
    index={edge:i for i,edge in enumerate(edges)}
    return [tuple(index[tuple(sorted(((s*a+t)%n,(s*b+t)%n)))] for a,b in edges)
            for s in ([1,-1] if dihedral else [1]) for t in range(n)]


def quotient(n,dihedral):
    edges,faces=original_faces(n)
    permutations=group(n,edges,dihedral)
    chains=[]
    for r in range(1,n//2+1):
        level=[]
        for top in faces:
            if len(top)<r:continue
            for sizes in combinations(range(1,len(top)),r-1):
                subchoices=[[frozenset(s) for s in combinations(sorted(top),k)] for k in sizes]
                for portions in product(*subchoices):
                    if all(portions[i]<portions[i+1] for i in range(len(portions)-1)):
                        level.append(portions+(top,))
        chains.append(level)
    reps={};orb={}
    for d,level in enumerate(chains):
        reps[d]=[]
        for c in level:
            if c in orb:continue
            i=len(reps[d]); reps[d].append(c)
            for perm in permutations:
                image=tuple(frozenset(perm[x] for x in f) for f in c)
                if image in orb:assert orb[image]==(d,i)
                orb[image]=(d,i)
    assert sum(len(x) for x in chains)==len(orb)
    return edges,faces,reps,orb


def free_collapse(reps,orb):
    alive={(d,i) for d in reps for i in range(len(reps[d]))}
    faces_of={};cofaces=defaultdict(list)
    for d in reps:
        if d==0:continue
        for j,chain in enumerate(reps[d]):
            cell=(d,j)
            boundary=[(d-1,orb[chain[:k]+chain[k+1:]][1]) for k in range(d+1)]
            assert len(boundary)==len(set(boundary))
            faces_of[cell]=boundary
            for facet in boundary:cofaces[facet].append(cell)
    deleted=[]
    while True:
        eligible=[]
        for facet in sorted(alive):
            extensions=[c for c in cofaces[facet] if c in alive]
            if len(extensions)==1:
                cell=extensions[0]
                assert faces_of[cell].count(facet)==1
                # Higher cofaces of cell must be gone for a true elementary collapse.
                higher=[z for z in cofaces[cell] if z in alive]
                if not higher:eligible.append((facet,cell))
        if not eligible:break
        highest=max(facet[0] for facet,cell in eligible)
        facet,cell=next(x for x in eligible if x[0][0]==highest)
        assert facet in alive and cell in alive
        alive.remove(facet);alive.remove(cell)
        deleted.append((facet,cell))
    return alive,deleted,faces_of


def simple_word(word):
    stack=[]
    for letter in word:
        if stack and stack[-1]==-letter:stack.pop()
        else:stack.append(letter)
    while len(stack)>1 and stack[0]==-stack[-1]:
        stack=stack[1:-1]
    return stack


def words_after_tree(alive,reps,orb):
    vertices={i for d,i in alive if d==0}
    edges={i for d,i in alive if d==1}
    triangles={i for d,i in alive if d==2}
    adjacency=defaultdict(list)
    for e in edges:
        a,b=(orb[(f,)][1] for f in reps[1][e])
        assert a!=b
        adjacency[a].append((b,e));adjacency[b].append((a,e))
    root=min(vertices)
    seen={root};queue=[root];tree=set()
    for v in queue:
        for w,e in adjacency[v]:
            if w not in seen:
                seen.add(w);queue.append(w);tree.add(e)
    assert seen==vertices and len(tree)==len(vertices)-1
    basis={e:i+1 for i,e in enumerate(sorted(edges-tree))}
    relators=[]
    for tri in sorted(triangles):
        ch=reps[2][tri]
        oriented=[(ch[1:],1),((ch[0],ch[2]),-1),(ch[:2],1)]
        letters=[]
        for eface,sign in oriented:
            e=orb[eface][1]
            if e in basis:letters.append(sign*basis[e])
        relators.append(simple_word(letters))
    return basis,tree,relators


def eliminate(relators,number_of_gens):
    relators=[r.copy() for r in relators]
    active=set(range(1,number_of_gens+1))
    operations=[]
    while True:
        options=[]
        for index,word in enumerate(relators):
            counts=Counter(abs(x) for x in word)
            for generator,occurrences in counts.items():
                if occurrences==1:
                    options.append((len(word),index,generator))
        if not options:break
        _,index,generator=min(options)
        word=relators.pop(index)
        at=next(k for k,x in enumerate(word) if abs(x)==generator)
        remain=word[at+1:]+word[:at]
        solution=[-x for x in reversed(remain)] if word[at]>0 else remain
        revised=[]
        for relator in relators:
            updated=[]
            for letter in relator:
                if letter==generator: updated.extend(solution)
                elif letter==-generator: updated.extend(-x for x in reversed(solution))
                else: updated.append(letter)
            revised.append(simple_word(updated))
        relators=revised
        active.remove(generator)
        operations.append(generator)
    return active,relators,operations


def run(n,dihedral,verbose=True):
    es,faces,reps,orb=quotient(n,dihedral)
    face_vector=tuple(sum(len(f)==r for f in faces) for r in range(1,n//2+1))
    cells=tuple(len(reps[d]) for d in reps)
    alive,steps,facets=free_collapse(reps,orb)
    survivors=tuple(sum(d==j for d,i in alive) for j in reps)
    basis,tree,rels=words_after_tree(alive,reps,orb)
    gens,final,elims=eliminate(rels,len(basis))
    data=(n,'dihedral' if dihedral else 'rotational',face_vector,cells,len(steps),survivors,len(tree),len(basis),len(elims),sorted(gens),final)
    if verbose:print(data)
    return data


def main():
    tests=[run(n,dihedral) for n in range(5,9) for dihedral in (False,True)]
    n8rot=tests[-2];n8dih=tests[-1]
    assert n8rot[2]==(28,140,140,14)
    assert n8rot[3]==(45,169,168,42)
    assert n8rot[4:9]==(149,(20,62,44,0),19,43,42)
    assert len(n8rot[9])==1 and len(n8rot[10])==2
    assert sorted([tuple(abs(x) for x in w) for w in n8rot[10]])==[(),(n8rot[9][0],n8rot[9][0])]
    assert n8dih[3]==(35,112,105,27)
    assert n8dih[4:6]==(139,(1,0,0,0))
    expected_small={5:(1,0),6:(1,0),7:(3,1)}
    for j,n in enumerate(range(5,8)):
        rot,dih=tests[2*j:2*j+2]
        assert rot[5][2:]==(0,)*(n//2-2)
        assert dih[5][2:]==(0,)*(n//2-2)
        assert len(rot[9])==expected_small[n][0] and not rot[10]
        assert len(dih[9])==expected_small[n][1] and not dih[10]
    print('VERIFY_OK')

if __name__=='__main__':main()
