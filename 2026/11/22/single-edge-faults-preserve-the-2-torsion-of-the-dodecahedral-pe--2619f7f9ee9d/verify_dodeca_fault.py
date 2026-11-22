#!/usr/bin/env python3
"""Exact integral discrete-Morse certificate for one-edge faults of GP(10,2).

Requires Python 3.9+ and SymPy for exact Smith normal forms.
Every subset is encoded as a bit mask in lexicographic graph-edge order.
No sampling, numeric tolerances, or external data files are used.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 10
EDGES = sorted(
    {tuple(sorted((i, (i+1)%N))) for i in range(N)}
    | {(i, N+i) for i in range(N)}
    | {tuple(sorted((N+i, N+(i+2)%N))) for i in range(N)}
)
assert len(EDGES) == 30
NEIGHBORS = [[] for _ in range(20)]
for j, (u,v) in enumerate(EDGES):
    NEIGHBORS[u].append((v,j))
    NEIGHBORS[v].append((u,j))


def perfect_matchings():
    def go(left, selected):
        if not left:
            yield tuple(sorted(selected))
            return
        u = min(left)
        for v,e in NEIGHBORS[u]:
            if v in left:
                yield from go(left-{u,v}, selected+(e,))
    return sorted(set(go(set(range(20)), ())))


def independent_count():
    @lru_cache(None)
    def ways(mask):
        if mask == 0:
            return 1
        u = (mask & -mask).bit_length()-1
        return sum(ways(mask ^ (1<<u) ^ (1<<v))
                   for v,e in NEIGHBORS[u] if mask & (1<<v))
    return ways((1<<20)-1)


def faces_of(perfect):
    result = [set() for _ in range(11)]
    for matching in perfect:
        for k in range(1,11):
            for sub in combinations(matching,k):
                result[k].add(sum(1<<e for e in sub))
    return result


def bits(mask):
    while mask:
        b = mask & -mask
        yield b
        mask ^= b


def unsigned_boundary(mask):
    return {mask^b for b in bits(mask)}


def signed_boundary(mask):
    return [(mask^b, 1 if i%2 == 0 else -1)
            for i,b in enumerate(bits(mask))]


def mod2_basis(columns):
    pivots = {}
    for col in columns:
        x = col
        while x:
            k = x.bit_length()-1
            if k not in pivots:
                pivots[k] = x
                break
            x ^= pivots[k]
    return pivots


def in_span(vector, pivots):
    while vector:
        k = vector.bit_length()-1
        if k not in pivots:
            return False
        vector ^= pivots[k]
    return True


def mask_from_vector(vector):
    return sum(1<<i for i,a in enumerate(vector) if a%2)


def morse(faces):
    universe = set().union(*faces[1:])
    unmatched = set(universe)
    lower_to_upper, upper_to_lower = {}, {}
    for j in range(30):
        bit = 1<<j
        for low in sorted(unmatched):
            upper = low|bit
            if not (low&bit) and upper in unmatched:
                unmatched.remove(low)
                unmatched.remove(upper)
                lower_to_upper[low] = upper
                upper_to_lower[upper] = low
    assert len(unmatched)+2*len(lower_to_upper) == len(universe)

    # Exhaustive test: upward for matched Hasse edges, downward otherwise.
    indegree = {f:0 for f in universe}
    successors = defaultdict(list)
    arrows = 0
    for upper in universe:
        if upper.bit_count() == 1:
            continue
        for low in unsigned_boundary(upper):
            if lower_to_upper.get(low) == upper:
                start,end = low,upper
            else:
                start,end = upper,low
            successors[start].append(end)
            indegree[end] += 1
            arrows += 1
    ready = deque(f for f,degree in indegree.items() if degree==0)
    visited = 0
    while ready:
        f = ready.popleft();visited += 1
        for nxt in successors[f]:
            indegree[nxt] -= 1
            if not indegree[nxt]:
                ready.append(nxt)
    assert visited == len(universe), 'discrete-Morse directed cycle'

    @lru_cache(None)
    def reduce(face):
        # Exact chain projection after cancelling all matched unit incidences.
        if face in unmatched:
            return {face:1}
        if face in upper_to_lower:
            return {}
        upper = lower_to_upper[face]
        incident = signed_boundary(upper)
        pivot = next(sign for low,sign in incident if low == face)
        answer = Counter()
        for low,coefficient in incident:
            if low != face:
                for critical,value in reduce(low).items():
                    answer[critical] -= pivot*coefficient*value
        return {critical:value for critical,value in answer.items() if value}

    critical0 = sorted(f for f in unmatched if f.bit_count()==1)
    critical2 = sorted(f for f in unmatched if f.bit_count()==3)
    critical3 = sorted(f for f in unmatched if f.bit_count()==4)
    assert all(f.bit_count() in (1,3,4) for f in unmatched)
    assert len(critical0)==1
    columns = []
    for upper in critical3:
        reduced = Counter()
        for lower,sgn in signed_boundary(upper):
            for crit,value in reduce(lower).items():
                reduced[crit] += sgn*value
        columns.append([reduced[c] for c in critical2])
    boundary = Matrix(columns).T
    diag = [abs(int(x)) for x in smith_normal_form(boundary,domain=ZZ).diagonal() if x]
    return {
        'critical0':critical0,'critical2':critical2,'critical3':critical3,
        'lower_to_upper':lower_to_upper, 'reduce':reduce, 'columns':columns,
        'matrix_shape':list(boundary.shape),'smith':diag,
        'nonempty_faces':len(universe),'hasse_arrows':arrows,
        'morse_pairs':len(lower_to_upper)
    }


def original_degree_three_boundaries(faces):
    triangle_index = {f:i for i,f in enumerate(sorted(faces[3]))}
    boundaries = []
    for tetra in faces[4]:
        vector = 0
        for tri in unsigned_boundary(tetra):
            vector ^= 1<<triangle_index[tri]
        boundaries.append(vector)
    return triangle_index, mod2_basis(boundaries)


def generator_cycle(fault_model, full_triangle_index, full_boundary_span):
    critical2 = fault_model['critical2']
    boundary_columns = [mask_from_vector(v) for v in fault_model['columns']]
    image = mod2_basis(boundary_columns)
    assert len(critical2)-len(image) == 1
    index = next(i for i in range(len(critical2)) if not in_span(1<<i,image))
    cycle = {critical2[index]}
    boundary = unsigned_boundary(critical2[index])
    # Lift a nonzero Morse two-cycle to an actual simplicial two-cycle.
    iterations = 0
    while boundary:
        low = next((x for x in sorted(boundary)
                   if x in fault_model['lower_to_upper']
                   and fault_model['lower_to_upper'][x].bit_count()==3),None)
        assert low is not None, 'lift did not reach a two-cycle'
        triangle = fault_model['lower_to_upper'][low]
        cycle.symmetric_difference_update({triangle})
        boundary.symmetric_difference_update(unsigned_boundary(triangle))
        iterations += 1
        assert iterations <= 10000
    projected = 0
    for tri in cycle:
        for critical,coefficient in fault_model['reduce'](tri).items():
            if coefficient%2:
                projected ^= 1<<critical2.index(critical)
    assert projected == 1<<index, 'lift projection is not the selected generator'
    vector = 0
    for tri in cycle:
        vector ^= 1<<full_triangle_index[tri]
    assert not in_span(vector,full_boundary_span), 'torsion generator dies in the intact complex'
    return sorted(cycle),iterations


def main():
    pms = perfect_matchings()
    assert len(pms)==independent_count()==36
    assert all(len(p)==10 for p in pms)
    assert [sum(j in p for p in pms) for j in range(30)] == [12]*30
    full_faces = faces_of(pms)
    assert [len(x) for x in full_faces[1:]] == [30,375,2180,5790,8352,7440,4320,1620,360,36]
    full_model = morse(full_faces)
    assert full_model['smith'] == [1]*9+[2]
    assert full_model['matrix_shape']==[10,30]
    triangle_index,full_boundary_span = original_degree_three_boundaries(full_faces)
    assert len(full_boundary_span)==1833
    summary = {
        'graph':'GP(10,2)', 'perfect_matchings_full':len(pms),
        'full_faces_nonempty':full_model['nonempty_faces'],
        'full_Morse_matrix_shape':full_model['matrix_shape'],
        'full_Smith_diagonal':full_model['smith'],
        'full_critical':[1,10,30],
        'full_original_mod2_B3_rank':len(full_boundary_span),
        'fault_edge_representatives':[]
    }
    for edge_index,shape,diag in [
        (0,[4,8],[1,1,1,2]),
        (2,[5,9],[1,1,1,1,2]),
        (20,[7,11],[1,1,1,1,1,1,2])
    ]:
        fault_pms = [p for p in pms if edge_index not in p]
        assert len(fault_pms)==24
        fault_faces = faces_of(fault_pms)
        assert [len(x) for x in fault_faces[1:]] == [29,334,1678,4076,5660,4976,2880,1080,240,24]
        model = morse(fault_faces)
        assert model['matrix_shape']==shape and model['smith']==diag
        assert model['nonempty_faces']==20977 and model['hasse_arrows']==111362
        cycle,steps = generator_cycle(model,triangle_index,full_boundary_span)
        assert len(cycle)==8 and all(f in fault_faces[3] for f in cycle)
        summary['fault_edge_representatives'].append({
            'edge_index':edge_index,'endpoints':EDGES[edge_index],
            'remaining_perfect_matchings':len(fault_pms),
            'faces_nonempty':model['nonempty_faces'],
            'hasse_arrows':model['hasse_arrows'],
            'acyclic_matching_pairs':model['morse_pairs'],
            'critical_cells_by_dimension':{'0':1,'2':len(model['critical2']),'3':len(model['critical3'])},
            'Morse_matrix_shape':model['matrix_shape'],
            'Smith_diagonal':model['smith'],
            'critical_2_masks':model['critical2'],
            'critical_3_masks':model['critical3'],
            'signed_Morse_boundary_columns':model['columns'],
            'nonzero_mod2_cycle_triangle_masks':cycle,
            'cycle_lift_steps':steps,
            'cycle_nonbounding_in_intact_complex':True
        })
    print(json.dumps(summary,sort_keys=True,indent=2))
    print('DODECA_SINGLE_EDGE_FAULT_CERTIFICATE_PASS')

if __name__ == '__main__':
    main()
