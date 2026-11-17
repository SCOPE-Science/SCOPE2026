"""Exact, standalone integer check for the matching complex of a 4 x 5 twisted strip.

Run: python3 verify_twisted_grid.py
All graph edges and faces are generated from the specification below.
The simplicial Morse reductions use only integer arithmetic.
"""
from collections import Counter, deque
from functools import lru_cache
import json


def graph_edges(twist=True):
    v = lambda row, col: 5 * row + col
    edges = [(v(r,c), v(r+1,c)) for r in range(3) for c in range(5)]
    edges += [(v(r,c),v(r,c+1)) for r in range(4) for c in range(4)]
    edges += [(v(r,4),v(3-r if twist else r,0)) for r in range(4)]
    assert len(edges) == len(set(tuple(sorted(pair)) for pair in edges)) == 35
    return edges


def all_faces(edges):
    support = [(1 << u) | (1 << v) for u,v in edges]
    out = []
    def visit(i, occupied, face):
        if i == len(edges):
            out.append(face)
            return
        visit(i+1, occupied, face)
        if not (support[i] & occupied):
            visit(i+1, occupied | support[i], face | (1 << i))
    visit(0, 0, 0)
    return out


def boundary(face):
    i = 0
    original = face
    while face:
        bit = face & -face
        yield (original ^ bit), (1 if i % 2 == 0 else -1)
        face -= bit
        i += 1


def gradient(faces, order):
    available = set(faces)
    available.remove(0)  # Keep a single zero-cell rather than matching the empty cell.
    mates = {}
    for p in order:
        bit = 1 << p
        for x in faces:
            y = x | bit
            if not x & bit and x in available and y in available:
                mates[x] = y
                available.remove(x)
                available.remove(y)
    return available, mates


def audit_gradient(mates):
    upper_to_lower = {h:lo for lo,h in mates.items()}
    assert len(upper_to_lower) == len(mates)
    assert all((hi ^ lo).bit_count() == 1 and lo & hi == lo
               for lo,hi in mates.items())
    degree = dict.fromkeys(upper_to_lower,0)
    for higher, lower in upper_to_lower.items():
        for face,sgn in boundary(higher):
            if face != lower and face in mates:
                degree[mates[face]] += 1
    q=deque(h for h,deg in degree.items() if deg==0)
    processed=0
    while q:
        h=q.popleft()
        processed+=1
        for face,sgn in boundary(h):
            if face!=upper_to_lower[h] and face in mates:
                tgt=mates[face]
                degree[tgt]-=1
                if degree[tgt]==0:
                    q.append(tgt)
    assert processed == len(mates), 'closed gradient path'
    return processed


def morse_matrix(critical,mates,low_size):
    """Signed Morse boundary: rows size low_size, columns size low_size+1.

    Eliminating each paired size-low_size/size-(low_size+1) incidence of
    coefficient ±1, a paired lower face equals the negative signed sum
    of the other codimension-one faces of its matched upper face.
    """
    lows=sorted(f for f in critical if f.bit_count()==low_size)
    highs=sorted(f for f in critical if f.bit_count()==low_size+1)
    index={face:i for i,face in enumerate(lows)}
    paired_uppers=set(mates.values())
    active=set()

    @lru_cache(None)
    def project(face):
        if face in index:
            return {index[face]:1}
        if face in paired_uppers:
            return {}
        assert face in mates, (face, face.bit_count(), face in critical, low_size)
        assert face not in active, 'closed gradient path during reduction'
        active.add(face)
        higher=mates[face]
        sign=next(s for other,s in boundary(higher) if other==face)
        acc={}
        for other,s in boundary(higher):
            if other==face:
                continue
            for i,z in project(other).items():
                acc[i]=acc.get(i,0)-sign*s*z
                if acc[i]==0:
                    del acc[i]
        active.remove(face)
        return acc

    A=[[0]*len(highs) for _ in lows]
    for j,higher in enumerate(highs):
        for lower,sgn in boundary(higher):
            for i,z in project(lower).items():
                A[i][j]+=sgn*z
    return A,lows,highs


def unit_reduction(A):
    """Unimodular elementary row and column elimination at unit pivots."""
    M=[row[:] for row in A]
    rows,cols=len(M),len(M[0]) if M else 0
    pivots=0
    for k in range(min(rows,cols)):
        loc=next(((i,j) for i in range(k,rows) for j in range(k,cols)
                  if abs(M[i][j])==1),None)
        if loc is None:
            break
        i,j=loc
        M[k],M[i]=M[i],M[k]
        for row in M:
            row[k],row[j]=row[j],row[k]
        sign=M[k][k]
        for i in range(k+1,rows):
            if M[i][k]:
                t=M[i][k]*sign
                for j in range(k,cols):
                    M[i][j]-=t*M[k][j]
        for j in range(k+1,cols):
            if M[k][j]:
                t=M[k][j]*sign
                for row in M:
                    row[j]-=t*row[k]
        pivots+=1
    return pivots, M


def main():
    twist_faces=all_faces(graph_edges(True))
    normal_faces=all_faces(graph_edges(False))
    assert len(twist_faces)==255300
    assert len(normal_faces)==253880
    assert sum((-1)**(x.bit_count()-1) for x in normal_faces if x)==137
    fvec=tuple(Counter(x.bit_count()-1 for x in twist_faces)[i] for i in range(10))
    assert fvec==(35,505,3910,17725,48197,77455,69770,31630,5820,252)
    assert sum((-1)**(x.bit_count()-1) for x in twist_faces if x)==165

    forward_crit,forward_pairs=gradient(twist_faces,range(35))
    assert audit_gradient(forward_pairs)==127550
    forward_counts=dict(Counter(x.bit_count()-1 for x in forward_crit))
    assert forward_counts=={0:1,6:181,7:17}
    D,low,high=morse_matrix(forward_crit,forward_pairs,7)
    unit_count,diagonal=unit_reduction(D)
    assert unit_count==17
    assert all(diagonal[i][j] == (1 if i==j else 0) or
               diagonal[i][j] == (-1 if i==j else 0)
               for i in range(181) for j in range(17))

    reverse_crit,reverse_pairs=gradient(twist_faces,reversed(range(35)))
    assert audit_gradient(reverse_pairs)==127565
    reverse_counts=dict(Counter(x.bit_count()-1 for x in reverse_crit))
    assert reverse_counts=={0:1,5:1,6:166,7:1}
    B,lows6,highs7=morse_matrix(reverse_crit,reverse_pairs,7)
    C,lows5,highs6=morse_matrix(reverse_crit,reverse_pairs,6)
    assert len(B)==166 and len(B[0])==1
    assert len(C)==1 and len(C[0])==166
    assert any(abs(row[0])==1 for row in B)
    assert any(abs(z)==1 for z in C[0])
    assert sum(C[0][i]*B[i][0] for i in range(166))==0
    # Reversed matching: one unit 5-6 cancellation and one unit 6-7
    # cancellation, leaving 164 six-cells.
    print(json.dumps({
        'graph': '4x5 row-reversing seam grid',
        'vertices':20, 'edges':35,
        'augmented_faces':len(twist_faces),
        'f_vector':list(fvec),
        'untwisted_augmented_faces':len(normal_faces),
        'untwisted_reduced_euler_characteristic':136,
        'forward_critical':{str(k):v for k,v in sorted(forward_counts.items())},
        'forward_matched_pairs':len(forward_pairs),
        'forward_morse_boundary_shape':[len(D),len(D[0])],
        'forward_integer_unit_pivots':unit_count,
        'reverse_critical':{str(k):v for k,v in sorted(reverse_counts.items())},
        'reverse_matched_pairs':len(reverse_pairs),
        'reverse_unit_boundary_ranks':[1,1],
        'reverse_boundary_composition_zero':True,
        'reduced_euler_characteristic':164,
        'homotopy':'wedge of 164 copies of S^6',
        'status':'PASS'
    },sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
