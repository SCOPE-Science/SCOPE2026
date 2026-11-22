"""Independent finite tests of the bounded-alphabet dependence splitting cutoff.
Run: python3 checker.py. No external libraries.
The symbolic proof, not these finite checks, covers all parameters.
"""
from itertools import combinations


def cyclic_team(r, q):
    assert r >= 1 and q >= r+1
    rows = [set((i+j)%q for j in range(r+1)) for i in range(q)]
    rows.append(rows[0].copy())
    return {(i,j) for i,row in enumerate(rows) for j in row}


def matching_satisfies(edges, r):
    """Separate augmenting-path matcher for row capacity r and column capacity 1."""
    assign = {}
    def augment(edge,seen):
        x,y=edge
        slots=[('row',x,t) for t in range(r)]+[('column',y,0)]
        for slot in slots:
            if slot in seen:
                continue
            seen.add(slot)
            if slot not in assign or augment(assign[slot],seen):
                assign[slot]=edge
                return True
        return False
    return all(augment(e,set()) for e in sorted(edges))


def hall_satisfies(edges, r):
    if not edges:
        return True
    rows=sorted({x for x,y in edges}); columns=sorted({y for x,y in edges})
    for a in range(1,1<<len(rows)):
        U={rows[i] for i in range(len(rows)) if a>>i&1}
        for b in range(1,1<<len(columns)):
            V={columns[j] for j in range(len(columns)) if b>>j&1}
            if sum(x in U and y in V for x,y in edges)>r*len(U)+len(V):
                return False
    return True


def test():
    independent_checks=0
    cases=0
    for r in range(1,6):
        for q in range(r+1,min(9,r+5)):
            E=cyclic_team(r,q)
            assert len(E)==(r+1)*(q+1)
            assert not matching_satisfies(E,r)
            for e in sorted(E):
                assert matching_satisfies(E-{e},r)
                independent_checks+=1
            if q<=5:
                assert not hall_satisfies(E,r)
                for e in sorted(E):
                    assert hall_satisfies(E-{e},r)
                    independent_checks+=1
            cases+=1
    # Independently compare all finite edge sets for 3x3, r=1,2,3.
    cells=[(x,y) for x in range(3) for y in range(3)]
    for r in (1,2,3):
        for mask in range(1<<len(cells)):
            E={cells[i] for i in range(len(cells)) if mask>>i&1}
            assert matching_satisfies(E,r)==hall_satisfies(E,r)
            independent_checks+=1
    # If q<=r, split by assigning at most r cells in every row.
    for r in range(1,6):
        for q in range(1,r+1):
            E={(x,y) for x in range(6) for y in range(q)}
            assert matching_satisfies(E,r)
            independent_checks+=1
    print('VERIFY_OK', 'cyclic_parameter_pairs='+str(cases), 'independent_checks='+str(independent_checks), 'small_grid_all_teams=1536')

if __name__=='__main__':
    test()
