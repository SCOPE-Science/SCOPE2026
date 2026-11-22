#!/usr/bin/env python3
"""Independent exhaustive update-rule checks on small indexed binary rings."""

def F(x, n):
    output = 0
    for i in range(n):
        left = (x >> ((i-1) % n)) & 1
        mid = (x >> i) & 1
        right = (x >> ((i+1) % n)) & 1
        if (73 >> (left*4 + mid*2 + right)) & 1:
            output |= 1 << i
    return output


def main():
    expected = {3:0, 4:0, 5:0, 6:0, 7:0, 8:24, 9:0,
                10:0, 11:0, 12:72, 13:78, 14:84, 15:270}
    examined = 0
    for n, count_expected in expected.items():
        totals = {1:0, 2:0, 3:0, 6:0}
        for x in range(1 << n):
            y = x
            for t in range(1,7):
                y = F(y,n)
                if t in totals and y == x:
                    totals[t] += 1
        primitive = totals[6]-totals[3]-totals[2]+totals[1]
        assert primitive == count_expected,(n,primitive,count_expected)
        examined += 1 << n
        print('ring',n,'period_6_states',primitive,'period_6_orbits',primitive//6)
    print('exhaustive_binary_configurations',examined)
    print('BRUTE_RING_OK')

if __name__=='__main__':
    main()
