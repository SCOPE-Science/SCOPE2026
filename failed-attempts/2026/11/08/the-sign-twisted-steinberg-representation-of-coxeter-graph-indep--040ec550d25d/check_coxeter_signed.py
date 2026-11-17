#!/usr/bin/env python3
"""Independent facewise signed Lefschetz check for all nine Coxeter conjugacy classes.

Run from the directory containing character_classes.json. Standard library only.
"""
import json
from itertools import combinations
from collections import Counter

with open('character_classes.json', encoding='utf-8') as stream:
    data = json.load(stream)
triples = [tuple(x) for x in data['graph_vertices']]
assert triples == [t for t in combinations(range(1,8),3) if t[0]^t[1]^t[2]]
neighbor = [0]*28
for a,b in data['graph_edges']:
    neighbor[a] |= 1<<b
    neighbor[b] |= 1<<a
assert len(data['graph_edges']) == 42
faces = []
def traverse(face,options):
    faces.append(face)
    while options:
        b = options & -options; options ^= b
        v = b.bit_length() - 1
        traverse(face | b, options & ~neighbor[v])
traverse(0,(1<<28)-1)
assert len(faces)==196009

for c in data['class_representatives_and_character']:
    p = c['representative']
    assert sorted(p) == list(range(28))
    actual = -1 # The empty simplex contributes -1 to reduced Lefschetz.
    for face in faces:
        if face == 0:
            continue
        selected = [i for i in range(28) if face & (1<<i)]
        image = [p[i] for i in selected]
        if set(image) != set(selected):
            continue
        inversions = sum(image[i] > image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        # Orientation on a k-face and alternating homological sign:
        sign = -1 if inversions & 1 else 1
        actual += sign * (1 if len(selected) & 1 else -1)
    assert actual == c['homology_trace'], (c['order'], actual, c['homology_trace'])
    assert c['homology_trace'] == c['sign']*(c['sylow_fixed']-1)
    print(c['order'], c['class_size'], c['sign'], c['homology_trace'], 'SIGNED_FACE_OK')
print('COXETER_NINE_CLASS_INDEPENDENT_SIGNED_LEFSCHETZ_PASS')
