"""Exact checks for the order-three power-sum family; Python standard library."""
from collections import deque
from math import gcd


def parameters(t):
    assert t >= 4 and t % 7 in (4, 5)
    q = 2*t + 1
    numerator = q**3 - 1
    assert numerator % 14 == 0
    e = numerator // 14
    assert e == t*(q*q+q+1)//7
    assert gcd(e, q-1) == t
    assert pow(q, 3, e) == 1
    return q, e


def digit_sum(n, q):
    total = 0
    while n:
        total += n % q
        n //= q
    return total


def exact_shortest_return(q, e):
    """BFS on the complete residue graph with edges +1,+q,+q^2."""
    steps = (1, q % e, pow(q, 2, e))
    distances = [-1]*e
    fringe = deque()
    for s in steps:
        if s == 0:
            return 1
        if distances[s] == -1:
            distances[s] = 1
            fringe.append(s)
    while fringe:
        v = fringe.popleft()
        for s in steps:
            nxt = (v+s) % e
            if nxt == 0:
                return distances[v]+1
            if distances[nxt] == -1:
                distances[nxt] = distances[v]+1
                fringe.append(nxt)
    raise AssertionError('No zero-sum return')


def run():
    tested = 0
    full_bfs = 0
    full_bfs_states = 0
    digit_sums = (3,2,3,2,3,4,3,2,3,4,3,4,3,6)
    for t in range(4, 801):
        if t % 7 not in (4,5):
            continue
        q,e = parameters(t)
        computed = tuple(digit_sum(j*e,q)//t for j in range(1,15))
        assert computed == digit_sums, (t, computed)
        for j in range(1,15):
            assert digit_sum(j*e,q) == t*digit_sums[j-1]
        m = 2*t
        witnesses = []
        for j in range(1,14):
            if digit_sum(j*e,q) == m:
                y = j*e
                digits = (y%q, (y//q)%q, (y//(q*q))%q)
                assert sum(digits) == m
                assert sum(d*q**i for i,d in enumerate(digits)) == y
                witnesses.append((j,digits))
        assert [j for j,_ in witnesses] == [2,4,8]
        assert len({tuple(x[1]) for x in witnesses}) == 3
        if t % 7 == 4:
            u = (t-4)//7
            expected=(8*u+5,4*u+2,2*u+1)
        else:
            u=(t-5)//7
            expected=(4*u+3,8*u+6,2*u+1)
        assert witnesses[0] == (2, expected), (t,witnesses[0],expected)
        assert {ds for _,ds in witnesses} == {expected, (expected[2],expected[0],expected[1]), (expected[1],expected[2],expected[0])}
        tested += 1
        if t <= 68:
            assert exact_shortest_return(q,e) == 2*t
            full_bfs += 1
            full_bfs_states += e
    assert tested > 220 and full_bfs > 15
    print('VERIFY_OK residue_parameters=%d exhaustive_bfs_cases=%d complete_residue_states=%d exact_full14_spectrum=yes 3_witness_orbit=yes' %(tested,full_bfs,full_bfs_states))

if __name__ == '__main__':
    run()
