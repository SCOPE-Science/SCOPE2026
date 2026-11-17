"""Arithmetic check of the local one-discrepancy lemma independent of morphism generation."""

def a(i):
    q = i + 1
    parity = 0
    while q % 2 == 0:
        parity ^= 1
        q //= 2
    return 1 ^ parity


def run():
    for k in range(11):
        m = 1 << k
        for start in range(301):
            for block in range(4):
                first = [a(start + block*m + i) for i in range(m)]
                next_one = [a(start + (block+1)*m + i) for i in range(m)]
                mismatches = [i for i in range(m) if first[i] != next_one[i]]
                assert len(mismatches) <= 1
                if mismatches:
                    assert (start + mismatches[0] + 1) % m == 0
                assert ((sum(first) == sum(next_one)) == (first == next_one))
        print(f'dyadic local Hamming/Parikh rigidity checked: m={m}')
    print('arithmetic local checks passed')

if __name__ == '__main__':
    run()
