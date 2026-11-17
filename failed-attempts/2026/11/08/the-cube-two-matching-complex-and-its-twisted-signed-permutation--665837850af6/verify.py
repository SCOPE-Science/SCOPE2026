#!/usr/bin/env python3
"""Exact self-contained checks for the two-matching complex of the cube graph."""
from collections import Counter, defaultdict, deque
from itertools import permutations
import json
import hashlib
import sys
from pathlib import Path

VERTICES = tuple(range(8))
EDGES = tuple((i,j) for i in VERTICES for j in range(i+1,8) if (i^j).bit_count()==1)
EDGE_LOOKUP = {e:i for i,e in enumerate(EDGES)}
FULL = (1<<len(EDGES))-1
STARS = tuple(sum(1<<i for i,(a,b) in enumerate(EDGES) if x==a or x==b) for x in VERTICES)


def by_degrees(mask):
    degrees = [0]*8
    for i,(a,b) in enumerate(EDGES):
        if mask>>i & 1:
            degrees[a] += 1
            degrees[b] += 1
    return max(degrees) <= 2


def by_forbidden_stars(mask):
    return all(mask & star != star for star in STARS)


def bit_faces():
    # Ascending integer order; empty simplex included in enumeration.
    return tuple(m for m in range(FULL+1) if by_degrees(m))


def matching(faces, order):
    remaining=set(faces)-{0}    # Forman matching on the nonempty-face poset
    pairs=[]
    for i in order:
        bit=1<<i
        # Pair in ascending order, ensuring a reproducible certificate.
        for low in sorted(remaining):
            high=low|bit
            if low&bit==0 and high in remaining:
                pairs.append((low,high))
                remaining.remove(low)
                remaining.remove(high)
    return pairs,tuple(sorted(remaining))


def verify_acyclic(faces,pairs,criticals):
    cells=set(faces)-{0}
    assert all(low in cells and high in cells and (high ^ low).bit_count()==1 and low & high == low for low,high in pairs)
    endpoints=[x for a,b in pairs for x in (a,b)]
    assert len(endpoints)==len(set(endpoints))
    assert set(endpoints).isdisjoint(criticals)
    assert len(endpoints)+len(criticals)==len(cells)
    paired_edges=set(pairs)
    indeg={c:0 for c in cells}
    out={c:[] for c in cells}
    incidence_count=0
    for high in cells:
        for bit in range(len(EDGES)):
            if high>>bit & 1:
                low=high^(1<<bit)
                if not low:
                    continue
                incidence_count+=1
                if (low,high) in paired_edges:
                    source,target=low,high
                else:
                    source,target=high,low
                out[source].append(target)
                indeg[target]+=1
    queue=deque(c for c in cells if not indeg[c])
    reached=0
    while queue:
        a=queue.popleft();reached+=1
        for b in out[a]:
            indeg[b]-=1
            if not indeg[b]:queue.append(b)
    assert reached==len(cells),f"cycle detected: {reached}/{len(cells)}"
    return incidence_count


def parity(values):
    return (-1)**sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))


def symmetric_char(faces):
    char_hist=Counter()
    cases=[]
    for perm in permutations(range(3)):
        for flip in range(8):
            graph_perm=[]
            for v in VERTICES:
                image=flip
                for i in range(3):
                    image ^= ((v>>i)&1)<<perm[i]
                graph_perm.append(image)
            assert len(set(graph_perm))==8
            edge_perm=tuple(EDGE_LOOKUP[tuple(sorted((graph_perm[a],graph_perm[b])))] for a,b in EDGES)
            assert sorted(edge_perm)==list(range(len(EDGES)))
            lefschetz=0
            for mask in faces:
                if mask==0:continue
                used=[i for i in range(len(EDGES)) if mask>>i&1]
                mapped=[edge_perm[i] for i in used]
                if sorted(mapped)==used:
                    lefschetz += (-1)**(len(used)-1)*parity(mapped)
            hom_char=1-lefschetz  # connected and only reduced degree-five homology
            signed_natural=sum((-1)**((flip>>j)&1) for j in range(3) if perm[j]==j)
            expected=parity(perm)*signed_natural
            assert hom_char==expected,(perm,flip,hom_char,expected)
            char_hist[hom_char]+=1
            cases.append(dict(coordinate_permutation=list(perm),flip_mask=flip,homology_trace=hom_char))
    assert len(cases)==48
    assert cases[0]['homology_trace']==3
    return char_hist,cases


def modular_ranks(faces):
    bydim=defaultdict(list)
    for f in faces:
        if f:bydim[f.bit_count()-1].append(f)
    ranks=[]
    for d in range(1,max(bydim)+1):
        idx={f:i for i,f in enumerate(bydim[d-1])}
        piv={}
        for high in bydim[d]:
            x=0
            for i in range(12):
                if high>>i&1:x ^= 1<<idx[high^(1<<i)]
            while x:
                k=x.bit_length()-1
                if k in piv:x ^= piv[k]
                else:
                    piv[k]=x
                    break
        ranks.append(len(piv))
    return ranks


def run():
    assert len(EDGES)==12
    assert sorted((s.bit_count() for s in STARS))==[3]*8
    for m in range(FULL+1):
        assert by_degrees(m)==by_forbidden_stars(m)
    faces=bit_faces()
    counts=[sum(1 for m in faces if m.bit_count()==k) for k in range(13)]
    assert counts==[1,12,66,212,423,516,352,108,9,0,0,0,0],counts
    primary_pairs,primary_crit=matching(faces,range(11,-1,-1))
    secondary_pairs,secondary_crit=matching(faces,range(12))
    h1=verify_acyclic(faces,primary_pairs,primary_crit)
    h2=verify_acyclic(faces,secondary_pairs,secondary_crit)
    assert h1==h2==7980,(h1,h2)
    assert Counter(c.bit_count()-1 for c in primary_crit)=={0:1,5:3}
    assert Counter(c.bit_count()-1 for c in secondary_crit)=={0:1,4:1,5:4}
    assert len(primary_pairs)==847 and len(secondary_pairs)==846
    # Complete dimensionwise independent mod-two boundary check.
    mod2=modular_ranks(faces)
    assert mod2==[11,55,157,266,250,99,9],mod2
    char_hist,cases=symmetric_char(faces)
    assert dict(char_hist)=={3:1,1:15,-1:15,-3:1,0:16},dict(char_hist)
    certificate={'edges':[list(e) for e in EDGES], 'forbidden_stars':[s for s in STARS],
        'primary_matched_pairs':[list(p) for p in primary_pairs], 'primary_critical_cells':list(primary_crit),
        'secondary_critical_cells':list(secondary_crit), 'symmetry_cases':cases}
    certificate_bytes=(json.dumps(certificate,sort_keys=True,separators=(',',':'))+'\n').encode()
    certfile=Path(__file__).with_name('certificate.json')
    if '--make-certificate' in sys.argv:
        certfile.write_bytes(certificate_bytes)
    else:
        assert certfile.read_bytes()==certificate_bytes, 'embedded certificate mismatches'
    result={'graph_vertices':8,'graph_edges':12,'faces_including_empty':len(faces),
      'face_vector_dimensions_0_to_7':counts[1:9],
      'primary_pairs':len(primary_pairs),'primary_critical_by_dim':{'0':1,'5':3},
      'secondary_pairs':len(secondary_pairs),'secondary_critical_by_dim':{'0':1,'4':1,'5':4},
      'directed_hasse_incidences':h1,'mod2_boundary_ranks_d1_to_d7':mod2,
      'cube_automorphisms':len(cases),'homology_character_histogram':{str(k):v for k,v in sorted(char_hist.items())},
      'certificate_sha256':hashlib.sha256(certificate_bytes).hexdigest(),
      'result':'Q3_TWO_MATCHING_WEDGE_THREE_S5_AND_SIGN_TWIST_CHARACTER_VERIFIED'}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':run()
