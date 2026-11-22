#!/usr/bin/env python3
"""Exact finite verification for the line/square Frobenius reconstruction theorem.

No nonstandard Python dependencies. The two models of the 16 exceptional curves
are compared from their intersection graph before group enumeration.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from pathlib import Path
import csv

# Divisor coordinates (L,E_0,...,E_4) on the blow-up of five points.
def divisor(kind, indexes=()):
    if kind == 'E':
        x = [0] * 6; x[1 + indexes[0]] = 1; return tuple(x)
    if kind == 'T':
        x = [1] + [(-1 if i in indexes else 0) for i in range(5)]
        return tuple(x)
    if kind == 'Q':
        return (2, -1, -1, -1, -1, -1)
    raise ValueError(kind)

def dot(x,y):
    return x[0]*y[0] - sum(a*b for a,b in zip(x[1:],y[1:]))

classes = {('E',i):divisor('E',(i,)) for i in range(5)}
classes.update({('T',i,j):divisor('T',(i,j)) for i,j in combinations(range(5),2)})
classes[('Q',)] = divisor('Q')
labels = sorted(classes, key=str)
canonical = (3,-1,-1,-1,-1,-1)
assert len(classes) == 16
assert all(dot(v,v)==-1 and dot(v,canonical)==1 for v in classes.values())
adj = {k:{m for m in labels if m!=k and dot(classes[k],classes[m])==1} for k in labels}
assert {len(a) for a in adj.values()} == {5}
assert not any(y in adj[x] and z in adj[x] and z in adj[y]
               for x in labels for y,z in combinations(labels,2))

# Recover the folded-five-cube model from the divisor intersection matrix.
base = ('E',0)
neighbors = sorted(adj[base],key=str)
u = [(1<<5)-1 ^ (1<<i) for i in range(5)]
label_to_mask = {base:0}
label_to_mask.update({k:u[i] for i,k in enumerate(neighbors)})
for k in labels:
    if k in label_to_mask:continue
    pair = [i for i,m in enumerate(neighbors) if m in adj[k]]
    assert len(pair)==2
    label_to_mask[k] = (1<<pair[0]) | (1<<pair[1])
assert len(set(label_to_mask.values()))==16
assert all((k2 in adj[k1]) == ((label_to_mask[k1] ^ label_to_mask[k2]).bit_count()==4)
           for k1 in labels for k2 in labels if k1!=k2)

# Enumerate every geometric four-component anticanonical square in the divisor model.
squares_geom = set()
for group in combinations(labels,4):
    if sum(1 for x,y in combinations(group,2) if y in adj[x])!=4:continue
    d=tuple(sum(classes[k][i] for k in group) for i in range(6))
    assert d==canonical
    squares_geom.add(tuple(sorted(label_to_mask[k] for k in group)))
assert len(squares_geom)==40

# Independent affine-even-binary model.
V=tuple(x for x in range(32) if x.bit_count()%2==0)
assert len(V)==16 and set(V)==set(label_to_mask.values())
S=tuple(permutations(range(5)))
squares_affine={tuple(sorted((x,x^u[i],x^u[j],x^u[i]^u[j])))
                for x in V for i,j in combinations(range(5),2)}
assert len(squares_affine)==40 and squares_affine==squares_geom

def perm_mask(x,p):
    return sum(((x>>i)&1)<<p[i] for i in range(5))

def perm_comp(p,q):
    return tuple(p[q[i]] for i in range(5))

def inv(p):
    return tuple(p.index(i) for i in range(5))

def cycles(action):
    visited=set(); histogram=Counter()
    for i in range(len(action)):
        if i in visited:continue
        t=i;length=0
        while t not in visited:
            visited.add(t); length+=1; t=action[t]
        assert t==i
        histogram[length]+=1
    return tuple(sorted(histogram.items()))

def spectrum_to_str(s):
    return ' '.join(f'{length}^{count}' for length,count in s)

def fixed(s,n):
    return sum(length*count for length,count in s if n%length==0)

sq=tuple(sorted(squares_geom));sq_index={x:i for i,x in enumerate(sq)}
line_index={x:i for i,x in enumerate(V)}
ALL={}
for a in V:
    for p in S:
        f=lambda x:a^perm_mask(x,p)
        la=[line_index[f(x)] for x in V]
        sa=[sq_index[tuple(sorted(f(x) for x in square))] for square in sq]
        ALL[(a,p)]=(cycles(la),cycles(sa))
assert len(ALL)==1920

# Conjugacy graph: the four translations and four adjacent transpositions
# generate the full even-affine signed-permutation group W(D_5).
trans=[('translation',u[i]) for i in range(4)]
swap=[('permutation',tuple((j+1 if j==i else i if j==i+1 else j)
                            for j in range(5))) for i in range(4)]
def conj(g,st):
    a,p=g;kind,v=st
    if kind=='translation':return a^v^perm_mask(v,p),p
    return perm_mask(a,v),perm_comp(v,perm_comp(p,inv(v)))
classes_conj=[]
unclassified=set(ALL)
while unclassified:
    first=min(unclassified)
    queue=deque([first]); current={first}
    while queue:
        elt=queue.popleft()
        for st in trans+swap:
            next_elt=conj(elt,st)
            assert next_elt in ALL
            if next_elt not in current:
                current.add(next_elt);queue.append(next_elt)
    assert all(ALL[elt]==ALL[first] for elt in current)
    unclassified.difference_update(current)
    classes_conj.append((min(current),current))
assert len(classes_conj)==18
assert sorted(len(s) for _,s in classes_conj)==[1,5,10,20,20,60,60,60,60,80,80,120,160,160,160,240,240,384]
assert len({ALL[rep][0] for rep,_ in classes_conj})==12
assert len({ALL[rep][1] for rep,_ in classes_conj})==16
assert len({ALL[rep] for rep,_ in classes_conj})==18

# Recovery from the first three point counts over extensions.
def signature(g,k):
    l,s=ALL[g]
    return tuple((fixed(l,n),fixed(s,n)) for n in range(1,k+1))
assert len({signature(rep,1) for rep,_ in classes_conj})==13
assert len({signature(rep,2) for rep,_ in classes_conj})==17
assert len({signature(rep,3) for rep,_ in classes_conj})==18
collisions=defaultdict(list)
for rep,c in classes_conj:collisions[signature(rep,2)].append((rep,len(c)))
ambiguous=[r for r in collisions.values() if len(r)>1]
assert len(ambiguous)==1 and len(ambiguous[0])==2
assert {ALL[rep][0] for rep,_ in ambiguous[0]}=={((2,2),(6,2))}
assert {ALL[rep][1] for rep,_ in ambiguous[0]}=={
    ((1,1),(3,5),(6,4)),((1,1),(3,1),(6,6))}

records=[]
for rep,c in classes_conj:
    a,p=rep; l,s=ALL[rep]
    records.append({
        'class_size':len(c), 'translation_mask':a,
        'coordinate_permutation':','.join(str(x+1) for x in p),
        'line_cycles':spectrum_to_str(l),'square_cycles':spectrum_to_str(s),
        'line_fixed_1':fixed(l,1),'square_fixed_1':fixed(s,1),
        'line_fixed_2':fixed(l,2),'square_fixed_2':fixed(s,2),
        'line_fixed_3':fixed(l,3),'square_fixed_3':fixed(s,3)
    })
records.sort(key=lambda r:(-r['class_size'],r['line_cycles'],r['square_cycles']))
if __name__=='__main__':
    p=Path(__file__).with_name('frobenius_spectra.csv')
    with p.open('w',newline='',encoding='utf8') as fh:
        writer=csv.DictWriter(fh,fieldnames=list(records[0]))
        writer.writeheader();writer.writerows(records)
    print('DEGREE_FOUR_DEL_PEZZO_16_LINES_40_SQUARES_18_CLASSES_SHARP_3_EXTENSIONS_VERIFIED')
    print('conjugacy classes:',len(classes_conj),'line spectra:',12,'square spectra:',16)
    print('first-two-extension ambiguity:',[ALL[rep] for rep,_ in ambiguous[0]])
