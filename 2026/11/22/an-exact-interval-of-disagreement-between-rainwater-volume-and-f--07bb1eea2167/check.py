from fractions import Fraction as Q
from itertools import permutations

def simulate(rain):
    s = Q(0); overflow = Q(0); ys = []
    for rain_today in rain:
        before = s + rain_today
        overflow += max(Q(0), before-Q(7))
        available = min(Q(7), before)
        y = min(Q(4), available)
        ys.append(y)
        s = available-y
    return sum(ys), sum(y == 4 for y in ys), s, overflow, tuple(ys)

def exercise():
    assertions = 0
    for z in [Q(0),Q(1,7),Q(1,2),Q(9,10),Q(99,100),Q(1),Q(6,5),Q(3,2),Q(19,10),Q(199,100),Q(2),Q(201,100),Q(5,2),Q(3)]:
        cases={p:simulate(p) for p in set(permutations((Q(0), z, Q(6), Q(6))))}
        expected_volume = Q(12)+z
        expected_full = 2 if z < 1 else 3
        maxvol = max(res[0] for res in cases.values())
        maxfull = max(res[1] for res in cases.values())
        assert maxvol == expected_volume; assertions += 1
        assert maxfull == expected_full; assertions += 1
        joint_exists = any(v == maxvol and f == maxfull for v,f,*_ in cases.values())
        assert joint_exists == (not(Q(1) <= z < Q(2))); assertions += 1
        for p,(v,f,send,spill,ys) in cases.items():
            assert v+send+spill == Q(12)+z; assertions += 1
            assert Q(0) <= send <= Q(3); assertions += 1
            assert all(Q(0) <= y <= Q(4) for y in ys); assertions += 1
        if Q(1) <= z < Q(2):
            fullorders={p for p,(v,f,*_) in cases.items() if f==3}
            assert fullorders == {(Q(0),Q(6),Q(6),z),(Q(6),Q(6),z,Q(0))}; assertions += 1
            best_volume_with_full=max(v for v,f,*_ in cases.values() if f==maxfull)
            assert best_volume_with_full == Q(11)+z; assertions += 1
        if z < Q(2):
            assert simulate((Q(6),z,Q(6),Q(0)))[4] == (Q(4),Q(2)+z,Q(4),Q(2)); assertions+=1
        else:
            assert simulate((Q(6),z,Q(6),Q(0)))[4] == (Q(4),Q(4),Q(4),z); assertions+=1
    z=Q(3,2)
    assert simulate((Q(6),z,Q(6),Q(0)))[:2] == (Q(27,2),2); assertions+=1
    assert simulate((Q(6),Q(6),z,Q(0)))[:2] == (Q(25,2),3); assertions+=1
    return assertions

if __name__=='__main__':
    print('PASS exact rational checks:', exercise())
