"""Finite exhaustive verification for neighborhood shattering of the Chang parameter graphs."""
from itertools import combinations
from math import comb

PAIRS = list(combinations(range(8), 2))
SWITCH = {
    "triangular": set(),
    "matching": {(0, 1), (2, 3), (4, 5), (6, 7)},
    "eight_cycle": {(min(i, (i + 1) % 8), max(i, (i + 1) % 8)) for i in range(8)},
    "triangle_pentagon": {(0, 1), (0, 2), (1, 2), (3, 4), (4, 5), (5, 6), (6, 7), (3, 7)},
}
EXPECTED = {
    "triangular": ((1,28,378,2800,9520), (1,28,378,1960,2520), 0),
    "matching": ((1,28,378,2936,2736), (1,28,378,1968,984), 1328),
    "eight_cycle": ((1,28,378,2968,1152), (1,28,378,1968,576), 1624),
    "triangle_pentagon": ((1,28,378,2986,810), (1,28,378,1980,450), 1786),
}

def matrix(selected):
    a = [[0]*28 for _ in PAIRS]
    for i, u in enumerate(PAIRS):
        for j, v in enumerate(PAIRS):
            if i != j:
                intersect = bool(set(u).intersection(v))
                a[i][j] = int(intersect != ((u in selected) != (v in selected)))
    return a

def shattering_faces(a, closed):
    faces = {0: {()}}
    for size in range(1, 5):
        hit = set()
        for support in combinations(range(28), size):
            observed = set()
            for center in range(28):
                row = tuple(int(bool(a[center][vertex] or (closed and center==vertex))) for vertex in support)
                observed.add(row)
                if len(observed) == 1 << size:
                    hit.add(support)
                    break
        faces[size] = hit
    return faces

def verify(a):
    for i in range(28):
        assert a[i][i] == 0 and sum(a[i]) == 12
        for j in range(i+1, 28):
            assert a[i][j] == a[j][i]
            assert sum(a[i][k] * a[j][k] for k in range(28)) == (6 if a[i][j] else 4)

def main():
    checks = 0
    for name, selected in SWITCH.items():
        a = matrix(selected)
        verify(a)
        results=[]
        for closed in (False,True):
            faces=shattering_faces(a, closed)
            profile=tuple(len(faces[k]) for k in range(5))
            results.append(profile)
            facets3=sum(all(tuple(sorted((*t, x))) not in faces[4] for x in range(28) if x not in t) for t in faces[3])
            if not closed:
                assert facets3==EXPECTED[name][2],(name,facets3)
                assert all(any(tuple(sorted((*t,x))) in faces[3] for x in range(28) if x not in t) for t in faces[2]);
            for k in range(5):
                assert len(faces[k]) <= comb(28,k)
                checks+=comb(28,k)
        assert tuple(results)==EXPECTED[name][:2],(name,results)
        print(name,'open',results[0],'closed',results[1],'open_maximal_triples',EXPECTED[name][2])
    print('CHANG_SHATTER_MATRIX_PASS checks=',checks,'five_support_excluded_by_28_lt_32')

if __name__=='__main__': main()
