"""Independent graph-construction and trace-mask census for Chang parameter graphs."""
from itertools import combinations

verts = tuple(combinations(range(8), 2))
assert len(verts) == 28
edge_index={p:i for i,p in enumerate(verts)}

def one_graph(which):
    if which == 'triangular': switches=[]
    elif which == 'matching': switches=[(0,1),(2,3),(4,5),(6,7)]
    elif which == 'eight_cycle': switches=[tuple(sorted((u, (u+1)%8))) for u in range(8)]
    else: switches=[(0,1),(0,2),(1,2),(3,4),(4,5),(5,6),(6,7),(3,7)]
    smask=sum(1<<edge_index[p] for p in switches)
    rows=[0]*28
    for i,(a,b) in enumerate(verts):
        for j,(c,d) in enumerate(verts):
            if i==j: continue
            adjacent=(a==c or a==d or b==c or b==d)
            flip=bool((smask>>i)&1) ^ bool((smask>>j)&1)
            if adjacent ^ flip: rows[i]|=1<<j
    assert all(r.bit_count()==12 for r in rows)
    assert all((rows[i]&rows[j]).bit_count() == (6 if ((rows[i]>>j)&1) else 4) for i in range(28) for j in range(i+1,28))
    return rows

def traces(rows, support):
    # Centers are enumerated via independent intersections with the queried columns.
    masks=[0]*28
    for j,v in enumerate(support):
        for center in range(28):
            if (rows[center]>>v)&1:
                masks[center] |= 1<<j
    return len(set(masks)) == (1<<len(support))

def compute(rows):
    counts=[1]
    face_triples=set(); face_fours=set(); all_pairs=set()
    for sz in range(1,5):
        count=0
        for support in combinations(range(28),sz):
            if traces(rows,support):
                count+=1
                if sz==2: all_pairs.add(support)
                if sz==3: face_triples.add(support)
                if sz==4: face_fours.add(support)
        counts.append(count)
    assert len(all_pairs)==378
    contained=set()
    for q in face_fours:
        for t in combinations(q,3): contained.add(t)
    maximal=len(face_triples-contained)
    assert len(contained)<=len(face_triples)
    return tuple(counts),maximal

GOAL={
 'triangular':((1,28,378,2800,9520),(1,28,378,1960,2520),0),
 'matching':((1,28,378,2936,2736),(1,28,378,1968,984),1328),
 'eight_cycle':((1,28,378,2968,1152),(1,28,378,1968,576),1624),
 'triangle_pentagon':((1,28,378,2986,810),(1,28,378,1980,450),1786),
}

def main():
    for name in GOAL:
        rows=one_graph(name)
        op, facets=compute(rows)
        cl,_=compute([row | (1<<i) for i,row in enumerate(rows)])
        assert (op,cl,facets)==GOAL[name],(name,op,cl,facets)
        print(name,'open',op,'closed',cl,'open_maximal_triples',facets)
    print('CHANG_SHATTER_BITSETS_PASS')

if __name__=='__main__': main()
