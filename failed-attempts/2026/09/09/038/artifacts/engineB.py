"""Engine B (independent): append-rank generation of Av(1324), n<=9.

Child = parent ranks with values >= r bumped by 1, plus new last entry r.
Any 1324-occurrence not using the last entry lives in the avoiding parent,
so only quadruples (i,j,k,last) need testing. Different generation order
(append-last vs insert-max) and different pattern test (1324 quads vs 132
prefix triples) from Engine A.
"""
import sys
import time

MAXN = 9
cnt = {}  # (n,k) -> count


def quads_ok(c, m):
    """c has length m+1; check all triples i<j<k<=m-1 with last entry."""
    last = c[m]
    for i in range(m):
        ci = c[i]
        for j in range(i + 1, m):
            cj = c[j]
            for k in range(j + 1, m):
                ck = c[k]
                # 1324 pattern <=> ci<ck<cj<last
                if ci < ck < cj < last:
                    return False
    return True


def dfs(perm, inv):
    n = len(perm)
    cnt[(n, inv)] = cnt.get((n, inv), 0) + 1
    if n == MAXN:
        return
    m = n
    for r in range(1, m + 2):
        c = tuple(x + 1 if x >= r else x for x in perm) + (r,)
        if quads_ok(c, m):
            dfs(c, inv + (m + 1 - r))


def main():
    t0 = time.time()
    dfs((), 0)
    dt = time.time() - t0
    print(f"# engineB done in {dt:.1f}s", file=sys.stderr)
    for n in range(1, MAXN + 1):
        ks = sorted(k for (nn, k) in cnt if nn == n)
        tot = sum(cnt[(n, k)] for k in ks)
        print(f"n={n} total={tot} kmax={max(ks)}")
        print("row: " + " ".join(str(cnt[(n, k)]) for k in range(max(ks) + 1)))


if __name__ == "__main__":
    main()
