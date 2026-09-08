"""Independent stdlib-only verifier: brute-force prefix backtracking with a
direct relative-order pattern test (no signature encoding), used to replay
n<=8 slices and spot-check n=9/10 counts from the C enumerator."""
import sys

def rel_order(vals):
    s = sorted(vals)
    rank = {v: i + 1 for i, v in enumerate(s)}
    return tuple(rank[v] for v in vals)

def count_avoid(n, p1, p2):
    pats = {tuple(p1), tuple(p2)}
    perm = [0] * n
    used = [False] * (n + 1)
    cnt = [0]
    def hit(pos):
        al = perm[pos]
        for i in range(pos - 2):
            for j in range(i + 1, pos - 1):
                for k in range(j + 1, pos):
                    if rel_order((perm[i], perm[j], perm[k], al)) in pats:
                        return True
        return False
    def rec(pos):
        if pos == n:
            cnt[0] += 1
            return
        for v in range(1, n + 1):
            if not used[v]:
                perm[pos] = v
                used[v] = True
                if pos < 3 or not hit(pos):
                    rec(pos + 1)
                used[v] = False
    rec(0)
    return cnt[0]

def parse(s):
    return [int(x) for x in s.split(",")]

if __name__ == "__main__":
    n = int(sys.argv[1])
    p1 = parse(sys.argv[2])
    p2 = parse(sys.argv[3])
    print(count_avoid(n, p1, p2))
