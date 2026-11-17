"""Independent finite Euler-characteristic checks of geometric group quotients.

The Lefschetz sign of a vertex permutation on an invariant simplex is
its sign on the ordered vertices. Burnside averaging then gives the
Euler characteristic of the geometric orbit space, including nonfree
orbits. Python 3 standard library only.
"""
from itertools import permutations


def parity(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i+1, len(seq))) % 2 else 1


def verify(k):
    left = (1 << k) - 1
    right = left << k
    faces = []
    for mask in range(1, 1 << (2*k)):
        l, r = mask & left, mask & right
        if ((l != left and r != right)
                or (l == left and r == 0)
                or (r == right and l == 0)):
            faces.append(mask)
    assert len(faces) == (2**k - 1)**2 + 1
    perms = list(permutations(range(k)))
    even = [p for p in perms if parity(p) == 1]

    def transform(mask, pl, pr, swap):
        out = []
        for i in range(2*k):
            if mask & (1 << i):
                if i < k:
                    out.append(pl[i] + (k if swap else 0))
                else:
                    out.append(pr[i-k] + (0 if swap else k))
        return sum(1 << u for u in out), parity(out)

    def quotient_euler(permutations_used, exchange):
        group_size = len(permutations_used)**2 * (2 if exchange else 1)
        fixed_signed_sum = 0
        for pl in permutations_used:
            for pr in permutations_used:
                for swap in range(2 if exchange else 1):
                    for face in faces:
                        changed, sign = transform(face, pl, pr, swap)
                        if changed == face:
                            fixed_signed_sum += (-1)**(face.bit_count()-1)*sign
        assert fixed_signed_sum % group_size == 0
        return fixed_signed_sum // group_size

    outcomes = {
        'A_k x A_k': quotient_euler(even, False),
        '(A_k x A_k) semidirect C2': quotient_euler(even, True),
        'S_k x S_k': quotient_euler(perms, False),
        'S_k wreath C2': quotient_euler(perms, True),
    }
    expected = {
        'A_k x A_k': 2*(-1)**(k-1),
        '(A_k x A_k) semidirect C2': k % 2,
        'S_k x S_k': 1,
        'S_k wreath C2': 1,
    }
    assert outcomes == expected, (k, outcomes, expected)
    print('k =', k, '; nonempty faces =', len(faces))
    for name, value in outcomes.items():
        print(' ', name, 'Euler characteristic =', value)


if __name__ == '__main__':
    for n in (3, 4):
        verify(n)
    print('All finite checks passed.')
