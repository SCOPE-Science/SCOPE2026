"""Verify every proposed orbit representative and its entire relabeling orbit.
The separate exhaustive enumerator proves that the resulting orbit union
is complete by comparing its cardinality with the number of all optima.
"""
import itertools,json,pathlib
D=json.loads((pathlib.Path(__file__).parent/'orbit_representatives.json').read_text())
expect={3:(4,9,3),4:(4,168,10),5:(5,24,1),6:(7,4320,6)}
for q in range(3,7):
    c=D[str(q)]; m,total,orbits=expect[q]
    assert (c['minimum'],c['optimal_count'],len(c['orbits']))==(m,total,orbits)
    V=[(a,b) for a in range(q) for b in range(q) if a!=b]
    Vset=set(V)
    def valid(S):
        codes=set(S)
        assert len(codes)==len(S) and codes<=Vset
        ids=[]
        for a,b in V:
            s=frozenset((c,d) for c,d in codes if (c,d)==(a,b) or b==c or d==a)
            if not s or s in ids: return False
            ids.append(s)
        return True
    combined=set()
    for entry in c['orbits']:
        base=tuple(map(tuple,entry['representative']))
        assert len(base)==m and valid(base)
        orb=set()
        for p in itertools.permutations(range(q)):
            transformed=frozenset((p[a],p[b]) for a,b in base)
            assert valid(transformed)
            orb.add(transformed)
        assert len(orb)==entry['orbit_size']
        assert not (combined & orb), 'representatives have overlapping orbits'
        combined.update(orb)
    assert len(combined)==total
    print(q,m,total,orbits,'orbit representatives verified')
