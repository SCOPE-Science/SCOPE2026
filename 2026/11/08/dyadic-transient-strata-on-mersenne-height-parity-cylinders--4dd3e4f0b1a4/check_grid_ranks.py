#!/usr/bin/env python3
"""Independent bit-matrix test of the zero-primary partition for path-cycle parity grids."""

def rank_gf2(rows):
    pivots = {}
    for original in rows:
        row = original
        while row:
            lead = row.bit_length() - 1
            if lead in pivots:
                row ^= pivots[lead]
            else:
                pivots[lead] = row
                break
    return len(pivots)


def rows_of_graph(m, n):
    out = []
    for a in range(m):
        for b in range(n):
            z = 0
            for c, d in ((a - 1,b),(a + 1,b),(a,(b-1)%n),(a,(b+1)%n)):
                if 0 <= c < m:
                    z ^= 1 << (c*n+d)
            out.append(z)
    return out


def predicted_blocks(r,n):
    q = 1 << r
    h = n & -n
    if h == 1:
        return [q-1]
    k = h//2
    if k < q:
        return [q]*(2*(k-1)) + [q-k]*2
    return [k]*(2*(q-1))


def check_case(r,n):
    m = (1 << r)-1
    dim = m*n
    rows = rows_of_graph(m,n)
    power = [1 << i for i in range(dim)]
    blocks = predicted_blocks(r,n)
    steps = max(blocks)
    for t in range(steps+2):
        nullity = dim-rank_gf2(power)
        target = sum(min(t,s) for s in blocks)
        if nullity != target:
            raise AssertionError((r,n,t,nullity,target,blocks))
        power = [reduce_xor(power, adj) for adj in rows]
    return steps+2


def reduce_xor(power, mask):
    output = 0
    while mask:
        bit = mask & -mask
        output ^= power[bit.bit_length()-1]
        mask ^= bit
    return output


def main():
    cases = 0
    powers = 0
    for r, ceilings in ((2,48),(3,40),(4,32),(5,16)):
        for n in range(3,ceilings+1):
            if ((1 << r)-1)*n>510:
                continue
            powers += check_case(r,n)
            cases += 1
    print('PASS: %d independent path-cycle adjacency cases; %d exact power/nullity comparisons' % (cases,powers))

if __name__ == '__main__':
    main()
