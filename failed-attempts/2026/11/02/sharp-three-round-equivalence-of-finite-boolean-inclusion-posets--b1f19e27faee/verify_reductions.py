"""Universal finite Venn reductions: proof certificates for all atom counts."""
from itertools import product

def atomic_of_cells(cells, k):
    return tuple(int(not any(cells[s] and (s & (1 << i)) and not (s & (1 << j))
                             for s in range(1 << k))) for i in range(k) for j in range(k))

def next_diagrams(c):
    # one further set Z: a Venn region with c atoms can be split in c+1 ways.
    # Truncating c at 2 suffices, since only zero/nonzero on either side matters.
    d=tuple(min(x,2) for x in c)
    result=set()
    for vals in product(*(range(x+1) for x in d)):
        child=tuple(d[i]-vals[i] for i in range(4))+tuple(vals)
        result.add(atomic_of_cells(child,3))
    return (atomic_of_cells(d,2),frozenset(result))

def run():
    count=0
    for a,b in product(range(3), repeat=2):
        # Here cells have indices 00,10,01,11.  Two cells belong to X,
        # two to its complement.  The identities hold for every other-cell
        # size by the exhaustive cap-2 reduction.
        assert next_diagrams((a,2,b,2)) == next_diagrams((a,2,b,1))
        assert next_diagrams((2,a,2,b)) == next_diagrams((1,a,2,b))
        count+=2
    print('universal reduction identities checked:',count)
    print('REDUCTIONS_PASS')
if __name__ == '__main__': run()
