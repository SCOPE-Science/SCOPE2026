"""Finite exhaustive checks for interval one-point trace/cycle-rank identity.

The checks are computational corroboration, not a proof of the universal identity.
"""
from itertools import combinations
from random import Random


def pairings(seq):
    if not seq:
        yield ()
        return
    x=seq[0]
    for j in range(1,len(seq)):
        y=seq[j]
        for rest in pairings(seq[1:j]+seq[j+1:]):
            yield ((x,y),)+rest


def trace_polynomial(intervals):
    n=len(intervals)
    # Endpoint ranks are distinct integers. All potential incidence profiles
    # are represented by witness endpoints on the doubled integer grid.
    maxx=max(r for l,r in intervals)
    traces=set()
    for a in range(-1,2*maxx+3):
        for b in range(a,2*maxx+3):
            traces.add(tuple(i for i,(l,r) in enumerate(intervals)
                             if 2*l<=b and 2*r>=a))
    return tuple(sum(len(s)==t for s in traces) for t in range(n+1)),traces


def predicted(intervals):
    n=len(intervals)
    p=[1]+[n-t+1 for t in range(1,n+1)]
    edges=[]
    for i,j in combinations(range(n),2):
        if intervals[i][1] > intervals[j][0]:
            edges.append((i,j))
            if j-i>=2:
                p[j-i-1]-=1
    c=0
    for i in range(n):
        if i==0 or intervals[i-1][1]<intervals[i][0]:
            # This is NOT the component count in general: a later interval
            # may bridge a gap. In proper interval families, if consecutive
            # intervals are disjoint, NO later interval crosses it.
            c+=1
    assert sum(p)==1+n*(n+1)//2-len(edges)+n-c
    return tuple(p)


def proper(intervals):
    return all(intervals[i][1]<intervals[j][1] for i in range(len(intervals)) for j in range(i+1,len(intervals)))


def test(intervals):
    actual,traces=trace_polynomial(intervals)
    expected=predicted(intervals)
    if actual != expected:
        raise AssertionError((intervals,actual,expected,traces))
    for tr in traces:
        if tr and tr != tuple(range(tr[0],tr[-1]+1)):
            raise AssertionError(('not contiguous',intervals,tr))


def main():
    checked=0
    for n in range(1,6):
        for raw in pairings(tuple(range(2*n))):
            intervals=tuple(sorted(raw))
            if proper(intervals):
                test(intervals)
                checked+=1
    rng=Random(2601105)
    for n in (6,7,8,9):
        for _ in range(120):
            # Generate a random proper interval representation by random
            # interleavings of n increasing left and n increasing right
            # endpoints with the prefix balance constraint.
            opens=closes=0; starts=[]; ends=[]
            for t in range(2*n):
                if opens == n: take_open=False
                elif opens == closes: take_open=True
                else: take_open=rng.randrange(2)==0
                if take_open:
                    starts.append(t);opens+=1
                else:
                    ends.append(t);closes+=1
            intervals=tuple(zip(starts,ends))
            assert proper(intervals) and all(l<r for l,r in intervals)
            test(intervals)
            checked+=1
    print('VERIFY_OK',checked)


if __name__=='__main__':
    main()
