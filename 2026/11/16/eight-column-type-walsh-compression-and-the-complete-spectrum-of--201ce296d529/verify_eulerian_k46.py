"""Exact integer certificate for the Walsh spectrum of balanced 4-by-6 tables.

Usage: python3 verify_eulerian_k46.py
Reads the adjacent data/eulerian_k46_orbits.csv. Requires Python 3.9+ only.
"""
import csv
import itertools
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

PAIRS = tuple(itertools.combinations(range(4), 2))
EXPECTED = {
 -1860:256,-620:4608,-372:15360,-324:11520,-236:7680,
 -148:23040,-124:230400,-116:138240,-68:391680,-60:307200,
 -44:92160,-20:69120,-12:829440,-4:2073600,0:8388608,
 4:2073600,12:829440,20:69120,44:92160,60:307200,
 68:391680,116:138240,124:230400,148:23040,236:7680,
 324:11520,372:15360,620:4608,1860:256
}

def weak_compositions(total, parts=8):
    if parts == 1:
        yield (total,)
    else:
        for k in range(total + 1):
            for tail in weak_compositions(total-k, parts-1):
                yield (k,) + tail

def orbit_coefficient(counts):
    """Coefficient of z1^3*z2^3*z3^3*z4^3 in signed column product.

    At step t the sum of row degrees is 2t, so the fourth degree is
    determined by the first three. All arithmetic is exact in Z.
    """
    state = {(0, 0, 0): 1}
    step = 0
    for typ, repetitions in enumerate(counts):
        signs = [-1 if (typ >> j) & 1 else 1 for j in range(3)] + [1]
        for _ in range(repetitions):
            step += 1
            next_state = defaultdict(int)
            for (x,y,z), value in state.items():
                for a,b in PAIRS:
                    xx=x+int(a==0 or b==0)
                    yy=y+int(a==1 or b==1)
                    zz=z+int(a==2 or b==2)
                    ww=2*step-xx-yy-zz
                    if 0 <= xx <= 3 and 0 <= yy <= 3 and 0 <= zz <= 3 and 0 <= ww <= 3:
                        next_state[(xx,yy,zz)] += value*signs[a]*signs[b]
            state = next_state
    assert step == 6
    return state.get((3,3,3),0)

def multiplicity(counts):
    return (2**6)*math.factorial(6)//math.prod(math.factorial(k) for k in counts)

def orientation_support():
    """Independent enumeration of all 4-by-6 balanced matrices by row masks."""
    rows = [r for r in range(64) if r.bit_count() == 3]
    result = []
    for a,b,c,d in itertools.product(rows,repeat=4):
        if all(((a>>j)&1)+((b>>j)&1)+((c>>j)&1)+((d>>j)&1) == 2 for j in range(6)):
            result.append(a|(b<<6)|(c<<12)|(d<<18))
    return result

def main():
    path = Path(__file__).resolve().parent/'data'/'eulerian_k46_orbits.csv'
    with path.open(encoding='utf-8', newline='') as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==[f'c{i}' for i in range(8)]+['coefficient','multiplicity']
        table=list(reader)
    counts_seen=set()
    histogram=Counter()
    assert len(table)==math.comb(13,7)==1716
    for row, counts in zip(table, weak_compositions(6)):
        observed=tuple(int(row[f'c{i}']) for i in range(8))
        assert observed == counts and observed not in counts_seen
        counts_seen.add(observed)
        coef=orbit_coefficient(counts)
        mult=multiplicity(counts)
        assert int(row['coefficient'])==coef and int(row['multiplicity'])==mult
        histogram[coef]+=mult
    assert dict(histogram)==EXPECTED
    assert sum(histogram.values())==2**24
    assert sum(coef*coef*mult for coef,mult in histogram.items())==(2**24)*1860
    assert histogram[0] == 2**23
    assert min(abs(coef) for coef in histogram if coef) == 4
    support=orientation_support()
    assert len(support)==1860 and len(set(support))==1860
    # Direct signed sums do not use orbit DP. Validate 256 independent frequencies.
    random_generator=random.Random(202610)
    frequencies=[0,(1<<24)-1] + [random_generator.getrandbits(24) for _ in range(254)]
    cache={tuple(int(row[f'c{i}']) for i in range(8)):int(row['coefficient']) for row in table}
    for frequency in frequencies:
        column_types=[]
        for col in range(6):
            bits=[(frequency>>(6*row+col))&1 for row in range(4)]
            typ=sum((bits[j]^bits[3])<<j for j in range(3))
            column_types.append(typ)
        counts=tuple(column_types.count(k) for k in range(8))
        directly=sum(-1 if ((x & frequency).bit_count() & 1) else 1 for x in support)
        assert directly==cache[counts]
    print('EULERIAN_K46_WALSH_ORBIT_PASS orbits=1716 frequencies=16777216 direct=256')

if __name__=='__main__':
    main()
