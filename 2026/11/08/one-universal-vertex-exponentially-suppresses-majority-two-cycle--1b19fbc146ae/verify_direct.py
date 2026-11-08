#!/usr/bin/env python3
"""Exact independent bitwise majority-dynamics verification (standard library)."""
from math import comb


def update(bits: int, n: int, extra: bool) -> int:
    N = 2*n + int(extra)
    ones = bits.bit_count()
    output = 0
    for v in range(N):
        if v < 2*n:
            partner = v ^ 1
            neighbors_one = ones - ((bits >> v) & 1) - ((bits >> partner) & 1)
            degree = N - 2
        else:
            neighbors_one = ones - ((bits >> v) & 1)
            degree = N - 1
        if 2*neighbors_one > degree:
            new = 1
        elif 2*neighbors_one < degree:
            new = 0
        else:
            new = (bits >> v) & 1
        output |= new << v
    return output


def case(n: int, extra: bool) -> tuple[int, int, int, int]:
    N=2*n + int(extra)
    fixed = cyc2 = not_periodic = max_entry = 0
    for x in range(1<<N):
        y=update(x,n,extra)
        z=update(y,n,extra)
        if x==y:
            fixed+=1
            entry=0
        elif z==x:
            cyc2+=1
            entry=0
        else:
            not_periodic+=1
            w=update(z,n,extra)
            t=update(w,n,extra)
            if y == w:  # entry at 1
                entry=1
            elif z==t: # entry at 2
                entry=2
            else:
                raise AssertionError(f'entry after 2: n={n}, extra={extra}, x={x}')
        max_entry=max(max_entry,entry)
        if extra:
            assert update(update(z,n,extra),n,extra)==z
        else:
            assert z==y if x==y else (z==x if y!=x and (x.bit_count()==n) else z==y)
    expected_fixed = 2 if extra else 2+2**n
    expected_two = 2*comb(n,(n+1)//2) if extra else comb(2*n,n)-2**n
    assert (fixed,cyc2)==(expected_fixed,expected_two), (n,extra,fixed,cyc2)
    if not extra: assert max_entry<=1
    assert fixed+cyc2+not_periodic==1<<N
    return fixed,cyc2,not_periodic,max_entry


def main():
    seen=0
    for n in range(2,9):
        for extra in (False,True):
            N=2*n+int(extra)
            a,b,c,t=case(n,extra)
            seen+=1<<N
            print(f'n={n} vertices={N} center={int(extra)} fixed={a} primitive2_states={b} transient={c} max_entry={t}')
    print(f'PASS; {seen} independently updated labelled states, n=2..8, both graph families')

if __name__=='__main__':main()
