"""Exact finite verification of the ordinary five-cut complex of KG(5,2).

Python 3.10+ standard library only. Vertex labels are ordered 2-subsets
of {0,1,2,3,4}; incidence and orientations use increasing labels.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque

BASE = tuple(combinations(range(5), 2))
FULL = (1 << len(BASE)) - 1
ADJ = tuple(frozenset(j for j, b in enumerate(BASE)
                      if set(a).isdisjoint(b)) for a in BASE)


def is_connected(mask):
    verts = {i for i in range(10) if mask & (1 << i)}
    if not verts:
        return False
    start = min(verts)
    reached = {start}
    queue = [start]
    while queue:
        u = queue.pop()
        for w in ADJ[u] & verts:
            if w not in reached:
                reached.add(w)
                queue.append(w)
    return reached == verts


def cut_faces():
    generators = []
    for combo in combinations(range(10), 5):
        mask = sum(1 << j for j in combo)
        if not is_connected(mask):
            generators.append(FULL ^ mask)
    assert len(generators) == 120
    faces = {0}
    for f in generators:
        sub = f
        while sub:
            faces.add(sub)
            sub = (sub - 1) & f
    # An independent direct test: look for a disconnected five-subset in
    # the complement, without consulting the generator list.
    for f in range(1 << 10):
        comp = [i for i in range(10) if not (f & (1 << i))]
        expected = any(not is_connected(sum(1 << i for i in q))
                       for q in combinations(comp, 5))
        assert (f in faces) == expected, ('face membership', f)
    return generators, faces


def boundary(mask):
    verts = [i for i in range(10) if mask & (1 << i)]
    return {mask ^ (1 << j): (-1)**i for i, j in enumerate(verts)}


def greedy_matching(faces):
    remaining = set(faces)
    pairs = []
    for i in range(10):
        for f in sorted(remaining, key=lambda z: (z.bit_count(), z)):
            g = f | (1 << i)
            if not f & (1 << i) and g in remaining:
                pairs.append((f, g))
                remaining.remove(f)
                remaining.remove(g)
    assert len(pairs) == (len(faces) - len(remaining)) // 2
    assert len(pairs) == 238
    assert Counter(x.bit_count()-1 for x in remaining) == {3:8, 4:12}
    return pairs, remaining


def acyclicity(faces, pairs):
    matched = set(pairs)
    indeg = {f:0 for f in faces}
    down = defaultdict(list)
    edge_count = 0
    for top in faces:
        if not top:
            continue
        for bot in boundary(top):
            # Ordinary Hasse arrow top -> bot; matching reverses.
            if (bot,top) in matched:
                u,v = bot,top
            else:
                u,v = top,bot
            down[u].append(v)
            indeg[v] += 1
            edge_count += 1
    queue = deque(sorted(u for u in faces if indeg[u] == 0))
    processed = 0
    while queue:
        u = queue.popleft()
        processed += 1
        for v in down[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    assert processed == len(faces), ('cyclic', processed, len(faces))
    return edge_count


def integral_reduced_morse(faces,pairs):
    # Reduced cellular chain complex; boundary of a vertex is the empty face.
    col = {f: boundary(f) if f else {} for f in faces}
    for a,b in pairs:
        pivot = col[b].get(a,0)
        assert abs(pivot) == 1
        cb = col[b].copy()
        same_degree = [z for z in col if z != b and z.bit_count()==b.bit_count()]
        for z in same_degree:
            if a not in col[z]:
                continue
            multiple = col[z][a] * pivot
            for w,c in cb.items():
                col[z][w] = col[z].get(w,0) - multiple*c
                if col[z][w] == 0:
                    del col[z][w]
        del col[a]
        del col[b]
        for z in col:
            col[z].pop(a,None)
            col[z].pop(b,None)
    r3=sorted(z for z in col if z.bit_count()==4)
    c4=sorted(z for z in col if z.bit_count()==5)
    assert len(col)==20 and len(r3)==8 and len(c4)==12
    assert all(col[x].get(z,0)==0 for x in col for z in col
               if z.bit_count()!=x.bit_count()-1)
    mat=[[col[c].get(r,0) for c in c4] for r in r3]
    return mat, r3, c4


def determinant(a):
    # Fraction-free Bareiss determinant on a square integer matrix.
    n=len(a)
    if n == 0:
        return 1
    A=[list(row) for row in a]
    sign=1
    prev=1
    for k in range(n-1):
        if not A[k][k]:
            z=next((i for i in range(k+1,n) if A[i][k]),None)
            if z is None:
                return 0
            A[k],A[z]=A[z],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numerator % prev==0
                A[i][j]=numerator//prev
        for i in range(k+1,n):
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]


def rank_mod_p(mat,p):
    rows=len(mat)
    cols=len(mat[0]) if rows else 0
    A=[[x%p for x in row] for row in mat]
    lead=0
    for j in range(cols):
        i=next((k for k in range(lead,rows) if A[k][j]),None)
        if i is None:
            continue
        A[lead],A[i]=A[i],A[lead]
        inv=pow(A[lead][j],-1,p)
        A[lead]=[(x*inv)%p for x in A[lead]]
        for k in range(rows):
            if k!=lead and A[k][j]:
                v=A[k][j]
                A[k]=[(x-v*y)%p for x,y in zip(A[k],A[lead])]
        lead+=1
        if lead==rows:
            break
    return lead


def ordinary_homology(faces,p):
    by_size=defaultdict(list)
    for f in faces:
        by_size[f.bit_count()].append(f)
    by_size={j:sorted(v) for j,v in by_size.items()}
    ranks={}
    for sz in range(1,6):
        r=by_size.get(sz-1,[])
        c=by_size.get(sz,[])
        rm={v:i for i,v in enumerate(r)}
        mat=[[0]*len(c) for _ in r]
        for j,f in enumerate(c):
            for g,z in boundary(f).items():
                mat[rm[g]][j]=z
        ranks[sz]=rank_mod_p(mat,p)
    bettis={sz-1:len(by_size.get(sz,[]))-ranks.get(sz,0)-ranks.get(sz+1,0)
             for sz in range(1,6)}
    assert bettis=={0:0,1:0,2:0,3:1,4:5}, (p,bettis)
    return ranks


def main():
    generators,faces=cut_faces()
    print('facets',len(generators),'faces_including_empty',len(faces))
    print('f_vector', sorted(Counter(x.bit_count()-1 for x in faces).items()))
    pairs,crit=greedy_matching(faces)
    print('matched_pairs',len(pairs),'critical_cells', sorted(Counter(x.bit_count()-1 for x in crit).items()))
    print('hasse_incidences',acyclicity(faces,pairs),'acyclic True')
    mat, rows, cols=integral_reduced_morse(faces,pairs)
    print('morse_rows',rows)
    print('morse_cols',cols)
    print('morse_matrix',mat)
    # A seven-by-seven unimodular minor gives rank >= 7 and no torsion;
    # an explicit primitive relation of the 8 rows bounds rank <= 7.
    selected_rows=list(range(7))
    selected_cols=[3,4,5,7,8,9,10]
    minor=[[mat[i][j] for j in selected_cols] for i in selected_rows]
    det=determinant(minor)
    assert abs(det)==1,det
    relation=[1,1,-1,-1,0,1,-1,1]
    assert all(sum(relation[i]*mat[i][j] for i in range(8))==0
               for j in range(12))
    print('unimodular_minor_rows',selected_rows,'columns',selected_cols,'det',det)
    print('left_null_relation',relation,'rank 7; invariant factors 1x7')
    for p in [2,3,5,7,11]:
        ranks=ordinary_homology(faces,p)
        print('characteristic',p,'ordinary_boundary_ranks',sorted(ranks.items()),
              'reduced_betti H3=1 H4=5')
    print('VERIFIED integral homotopy type S^3 wedge 5 S^4')

if __name__=='__main__':
    main()
