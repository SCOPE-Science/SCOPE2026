"""Independent field-rank cross-check and chain-condition test for graph-Hom 2-skeleta.

Use alongside verify.py, with only the Python standard library.
"""
from verify import all_cells, neighbours, NVERT, Forest
from collections import Counter
import json


def run(kind):
    layers = all_cells(neighbours(kind))
    V = sorted(layers[0]); E = sorted(layers[1]); F = sorted(layers[2])
    vmap = {v: i for i, v in enumerate(V)}
    emap = {e: i for i, e in enumerate(E)}
    edges = []
    forest = Forest(len(V))
    for edge in E:
        j = next(i for i, m in enumerate(edge) if m.bit_count() == 2)
        a = edge[j] & -edge[j]; b = edge[j] ^ a
        va = list(edge); vb = list(edge); va[j] = a; vb[j] = b
        x, y = vmap[tuple(va)], vmap[tuple(vb)]
        edges.append((x,y))
    chords = {}
    for e, (u, v) in enumerate(edges):
        if not forest.join(u,v):
            chords[e] = len(chords)
    components = len(set(forest.root(i) for i in range(len(V))))
    assert components == 2 and len(chords) == 23042
    boundary_columns=[]
    for cell in F:
        boundary=[]; dimensions_before=0
        for j, m in enumerate(cell):
            if m.bit_count() > 1:
                bits=[1 << k for k in range(NVERT) if m & (1 << k)]
                for k,b in enumerate(bits):
                    edge=list(cell);edge[j] ^= b
                    eid=emap[tuple(edge)]
                    sign = (-1)**(dimensions_before+k)
                    boundary.append((eid,sign))
                dimensions_before += len(bits)-1
        assert len(boundary) in (3,4)
        # Integer cellular chain condition, checked without relying on a tree.
        accumulation={}
        for e,sgn in boundary:
            a,b=edges[e]
            accumulation[a]=accumulation.get(a,0)-sgn
            accumulation[b]=accumulation.get(b,0)+sgn
        assert all(x==0 for x in accumulation.values())
        boundary_columns.append(boundary)
    answers={}
    for p in (2,3,5):
        pivots={}
        rank=0
        for boundary in boundary_columns:
            col={}
            for e,sgn in boundary:
                if e in chords:
                    idx=chords[e]
                    col[idx]=(col.get(idx,0)+sgn)%p
            col={r:x for r,x in col.items() if x}
            while col:
                r=max(col);a=col[r]
                if r not in pivots:
                    inverse=pow(a,-1,p)
                    pivots[r]={k:inverse*v%p for k,v in col.items()}
                    rank+=1
                    break
                for k,v in pivots[r].items():
                    w=(col.get(k,0)-a*v)%p
                    if w:col[k]=w
                    else:col.pop(k,None)
        answers[str(p)]={'boundary_rank':rank,'H1_dimension':len(chords)-rank}
    return {'graph':kind, 'checked_2cells':len(F), 'verified_boundary_squared_zero': True, 'fields':answers}

if __name__=='__main__':
    results=[run('rook'),run('shrikhande')]
    assert [x['fields']['2']['H1_dimension'] for x in results]==[92,60]
    assert [x['fields']['3']['H1_dimension'] for x in results]==[90,60]
    print(json.dumps({'verification':'passed', 'results':results},indent=2,sort_keys=True))
