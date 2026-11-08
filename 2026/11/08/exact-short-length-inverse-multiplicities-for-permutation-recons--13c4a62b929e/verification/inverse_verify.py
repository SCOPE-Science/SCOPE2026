"""Independent inverse-sign reconstruction and orbit checks for absolute-difference records."""
from collections import Counter
from itertools import permutations
from math import factorial


def record(p):
    return tuple(abs(b-a) for a,b in zip(p,p[1:]))


def inverse_solutions(d):
    """All solutions from first-entry choice and signed steps, not permutations()."""
    n=len(d)+1
    solutions=[]
    def dfs(path, used):
        if len(path)==n:
            solutions.append(tuple(path))
            return
        step=d[len(path)-1]
        for nxt in (path[-1]-step,path[-1]+step):
            if 1<=nxt<=n and not (used>>(nxt-1))&1:
                path.append(nxt)
                dfs(path,used | (1<<(nxt-1)))
                path.pop()
    for start in range(1,n+1):
        dfs([start],1<<(start-1))
    return solutions


def verify(n):
    # This independent generator uses permutations() solely to enumerate which records exist.
    frequency=Counter(record(p) for p in permutations(range(1,n+1)))
    assert sum(frequency.values())==factorial(n)
    maxima=max(frequency.values())
    maxrecords={d for d,k in frequency.items() if k==maxima}
    if n==8:
        assert maxima==30 and maxrecords=={(4,2,4,1,4,2,4)}
        sols=set(inverse_solutions((4,2,4,1,4,2,4)))
        assert len(sols)==30
        assert {record(s) for s in sols}==maxrecords
        orbit_sizes=[]
        while sols:
            p=next(iter(sols))
            complement=tuple(n+1-x for x in p)
            reverse=p[::-1]
            reverse_complement=complement[::-1]
            orbit={p,complement,reverse,reverse_complement}
            assert orbit<=sols
            sols-=orbit
            orbit_sizes.append(len(orbit))
        assert Counter(orbit_sizes)=={4:7,2:1}
    if n==9:
        assert maxima==12 and len(maxrecords)==20
        assert all(len(inverse_solutions(d))==12 for d in maxrecords)
    if n==10:
        assert maxima==24 and len(maxrecords)==5
        assert all(len(inverse_solutions(d))==24 for d in maxrecords)
    assert all(v%2==0 for v in frequency.values())
    print(f"n={n} total={sum(frequency.values())} records={len(frequency)} max={maxima} maximizing={len(maxrecords)}")


if __name__=='__main__':
    for n in (8,9,10):
        verify(n)
    print('VERIFY_OK')
