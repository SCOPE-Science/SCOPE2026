"""Independent local period-three phase enumeration, with inactive marker 3."""
from itertools import product

def valid(word, threshold):
    n = len(word)
    for i, a in enumerate(word):
        neighbors = [word[(i + delta) % n] for delta in (-2, -1, 1, 2)]
        if a == 3:
            if any(neighbors.count(c) >= threshold for c in range(3)):
                return False
        elif neighbors.count((a + 1) % 3) < threshold:
            return False
    return True

def main():
    grand = 0
    for n in range(5, 11):
        counts = {}
        for th in (2, 3):
            cnt = 0
            for w in product(range(4), repeat=n):
                grand += 1
                if valid(w, th) and w != (3,) * n:
                    cnt += 1
                    assert 3 not in w
                    if th == 2:
                        assert tuple(w) in (tuple((a + b * i) % 3 for i in range(n)) for a in range(3) for b in (1, 2))
            counts[th] = cnt
        assert counts[2] == (6 if n % 3 == 0 else 0)
        assert counts[3] == 0
        print(f"n={n} theta2={counts[2]} theta3={counts[3]}")
    for m in range(2, 10):
        words = set()
        for blocks in product(('012', '021'), repeat=m):
            base = ''.join(blocks)
            for shift in range(3):
                s = tuple((int(c) + shift) % 3 for c in base)
                assert all(any(s[(i + delta) % (3*m)] == (s[i]+1) % 3 for delta in (-2,-1,1,2)) for i in range(3*m))
                words.add(s)
        assert len(words) == 3 * 2**m
        print(f"n={3*m} lower_construction={len(words)}")
    print(f"PHASE_OK assignments_tested={grand}")

if __name__ == '__main__':
    main()
