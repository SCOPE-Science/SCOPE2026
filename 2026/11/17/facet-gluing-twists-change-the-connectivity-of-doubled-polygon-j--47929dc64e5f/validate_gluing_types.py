"""Exhaustive tetrahedron-identification test for the connected-sum example."""
from itertools import permutations
from check_sphere_double_sum import connected_sum

def marked_same(p):
    return {p[0],p[1]} in ({0,1},{2,3})

def verify():
    counts={1:0,2:0}
    for p in permutations(range(4)):
        f,v,e,components=connected_sum(4,5,p)
        assert f==38 and v==52 and e==114
        count=len(components);counts[count]+=1
        if marked_same(p):
            assert components==[(16,38,23),(36,76,41)]
        else:
            assert components==[(52,114,63)]
    assert counts=={1:16,2:8}
    print('ALL_24_TETRAHEDRON_IDENTIFICATIONS_PASS: 16 connected, 8 disconnected')
if __name__=='__main__':verify()
