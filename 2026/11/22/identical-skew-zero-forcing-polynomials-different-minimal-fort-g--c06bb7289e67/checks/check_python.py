"""Independent finite check of forcing on two sixteen-vertex graphs.
Run with Python >=3.10; no external modules. All subsets are visited.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import csv

V = tuple((a,b) for a in range(4) for b in range(4))

def neighborhoods(name):
    out = []
    for (x,y) in V:
        if name == 'rook':
            nei = {j for j,(u,v) in enumerate(V) if (u,v)!=(x,y) and (u==x or v==y)}
        else:
            step = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
            nei = {j for j,(u,v) in enumerate(V) if ((u-x)%4,(v-y)%4) in step}
        out.append(nei)
    return out

def propagate(blue,nb,skew):
    blue = set(blue)
    white = set(range(16)) - blue
    while white:
        witnesses = range(16) if skew else blue
        forced = set()
        for v in witnesses:
            choices = white.intersection(nb[v])
            if len(choices) == 1:
                forced.update(choices)
        if not forced:
            break
        blue.update(forced)
        white.difference_update(forced)
    return not white

def run(name):
    nb = neighborhoods(name)
    skew = Counter(); ordinary = Counter(); forts = []; types4 = Counter()
    assert all(len(nb[i])==6 for i in range(16))
    assert all(len(nb[i]&nb[j])==2 for i in range(16) for j in range(16) if i!=j)
    for k in range(17):
        for vertices in combinations(range(16), k):
            white = frozenset(vertices)
            blue = set(range(16))-white
            if propagate(blue,nb,True):skew[len(blue)] += 1
            if propagate(blue,nb,False):ordinary[len(blue)] += 1
            if white and all(len(white & nei)!=1 for nei in nb):
                forts.append(white)
    minimal=[]
    for fort in forts:
        if not any(s.issubset(fort) for s in minimal):
            minimal.append(fort)
            if len(fort)==4:
                types4[tuple(sorted(len(nb[v]&fort) for v in fort))] += 1
    # Independently compare every certificate row, not just totals.
    root = Path(__file__).resolve().parent.parent
    with (root/'data'/'FORCING_COUNTS.csv').open(newline='', encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == 34
    actual_counts = {
        int(r['blue_count']): (int(r['skew_successes']),int(r['ordinary_successes']))
        for r in rows if r['graph']==name
    }
    assert len(actual_counts)==17
    assert all(actual_counts[k]==(skew[k],ordinary[k]) for k in range(17))
    with (root/'data'/'MINIMAL_SKEW_FORTS.csv').open(newline='', encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows)==632
    listed = {}
    for r in rows:
        if r['graph']!=name: continue
        F = frozenset(i for i in range(16) if (int(r['white_mask_hex'],16)>>i)&1)
        assert len(F)==int(r['size'])
        assert r['induced_degree_sequence']==','.join(str(x) for x in sorted(len(nb[v]&F) for v in F))
        assert F not in listed
        listed[F] = r
    assert len(listed)==316 and set(listed)==set(minimal)
    print(name)
    print('skew', [skew[j] for j in range(17)])
    print('ordinary', [ordinary[j] for j in range(17)])
    print('minimal_forts', sorted(Counter(map(len,minimal)).items()))
    print('four_fort_induced_degrees',sorted(types4.items()))
    assert [skew[j] for j in range(10,17)] == [4032,3648,1760,560,120,16,1]
    assert [ordinary[j] for j in range(10,17)] == ([3456,3504,1760,560,120,16,1] if name=='rook' else [3616,3600,1760,560,120,16,1])
    assert Counter(map(len,minimal))=={4:60,6:256}
    assert sum(types4.values())==60

if __name__=='__main__':
    run('rook');run('shrikhande')
