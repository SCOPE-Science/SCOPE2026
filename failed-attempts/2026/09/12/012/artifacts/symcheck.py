"""Attempt: derive Wilf-equivalence Av(1342,1423) ~ Av(1342,1432) via simple maps,
and probe 1432<->1423 suffix-relabelling obstruction. Checks all 8 dihedral maps
(reverse/complement/inverse group) on the pattern SETS, then checks whether the
combinatorial rewrites fix 1342."""
import itertools

def compose(p, f):
    # f: permutation of positions/values 0..3 as maps; apply dihedral ops on pattern tuple
    return f(p)

def rev(p): return p[::-1]
def comp(p): return tuple(5-x for x in p)
def inv(p):
    q=[0]*4
    for i,v in enumerate(p): q[v-1]=i+1
    return tuple(q)

def all_syms(p):
    out=set()
    for r in [lambda x:x, rev]:
        for c in [lambda x:x, comp]:
            for iv in [lambda x:x, inv]:
                out.add(iv(c(r(p))))
    return out

A={(1,3,4,2),(1,4,2,3)}
B={(1,3,4,2),(1,4,3,2)}
# check each of 8 maps sends set A to set B
maps={}
for rn,rf in [('id',lambda x:x),('r',rev)]:
    for cn,cf in [('id',lambda x:x),('c',comp)]:
        for inn,inf in [('id',lambda x:x),('i',inv)]:
            name=rn+cn+inn
            imgA={inf(cf(rf(p))) for p in A}
            maps[name]=imgA
for name,img in maps.items():
    print(name, img, "A->B" if img==B else ("A->A" if img==A else "other"))
