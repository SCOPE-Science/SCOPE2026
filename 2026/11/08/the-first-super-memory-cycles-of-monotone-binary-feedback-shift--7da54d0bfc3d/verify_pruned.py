"""Independent prefix-pruned exhaustive certificate for monotone FSR cycles.
Run: python3 verify_pruned.py (Python 3.8+ standard library).
"""
from math import comb


def comparable(u, v):
    return (u & v) in (u, v)


def complete_check(bits, memory):
    length = len(bits)
    windows = []
    for start in range(length):
        block = 0
        for offset in range(memory):
            block = 2 * block + bits[(start + offset) % length]
        if any(comparable(block, prior) for prior in windows):
            return False
        windows.append(block)
    return True


def recursive_count(memory, length):
    valid = []

    def search(bits, completed_windows):
        if len(bits) == length:
            if complete_check(bits, memory):
                valid.append(''.join(map(str, bits)))
            return
        for bit in (0, 1):
            extended = bits + (bit,)
            if len(extended) >= memory:
                block = 0
                for digit in extended[-memory:]:
                    block = 2 * block + digit
                if any(comparable(block, old) for old in completed_windows):
                    continue
                search(extended, completed_windows + (block,))
            else:
                search(extended, completed_windows)

    search((), ())
    return valid


def canonical(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def feedback_from_word(w, memory):
    """Monotone DNF extension of the specified cyclic feedback examples."""
    positives = []
    states = []
    length = len(w)
    for i in range(length):
        s = tuple(int(w[(i + j) % length]) for j in range(memory))
        target = int(w[(i + memory) % length])
        states.append((s, target))
        if target:
            positives.append(s)

    def f(bits):
        return int(any(all(a <= b for a, b in zip(p, bits))
                       for p in positives))

    assert all(f(s) == target for s, target in states)
    for x in range(1 << memory):
        a = tuple((x >> j) & 1 for j in range(memory))
        for y in range(1 << memory):
            b = tuple((y >> j) & 1 for j in range(memory))
            if all(aa <= bb for aa, bb in zip(a, b)):
                assert f(a) <= f(b)


def main():
    expected = {
        (6, 7): {'0001011', '0001101', '0010111', '0011101'},
        (6, 9): {'001010011', '001101011'},
    }
    for n in range(1, 7):
        for L in range(n + 1, comb(n, n // 2) + 1):
            words = recursive_count(n, L)
            necklace_set = {canonical(w) for w in words}
            assert necklace_set == expected.get((n, L), set()), (n, L)
            assert len(words) == L * len(necklace_set)
            print('memory', n, 'period', L, 'rooted', len(words),
                  'necklaces', len(necklace_set))
    feedback_from_word('001010011', 6)
    feedback_from_word('0001011', 6)
    print('PRUNED_VERIFY_OK')


if __name__ == '__main__':
    main()
