"""Compute exact Sprague-Grundy values for octal game 0.007 (Treblecross) to N=200.

Rule (octal 0.007): remove exactly 3 tokens from a heap; the remainder of the
played heap (n-3 tokens) may optionally be split into two nonempty heaps, or
left whole, or (when n-3 = 0) vanish. Equivalently, from heap size n >= 3 the
options are: heap of size n-3, or a pair (i, n-3-i) for i = 0..n-3, where a
heap of size 0 is the terminal (empty) position with Grundy 0.

So G(0)=G(1)=G(2)=0, G(3)=mex{G(0)}=1, and for n > 3:
    reachable(n) = {G(n-3)} union {G(i) ^ G(n-3-i) : 0 <= i <= n-3}
    G(n) = mex(reachable(n)).

Deterministic, stdlib-only, no randomness (no seed needed).
Writes grundy_007_N200.csv with columns: n,g.
"""
import csv
import os

N = 200
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grundy_007_N200.csv")

def grundy_007(N):
    G = [0] * (N + 1)
    # G(0)=G(1)=G(2)=0 already; loop from 3
    for n in range(3, N + 1):
        if n == 3:
            reachable = {0}  # G(0)
        else:
            reachable = set()
            reachable.add(G[n - 3])
            for i in range(0, n - 2):  # i = 0..n-3
                reachable.add(G[i] ^ G[n - 3 - i])
        m = 0
        while m in reachable:
            m += 1
        G[n] = m
    return G

def main():
    G = grundy_007(N)
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "g"])
        for n, g in enumerate(G):
            w.writerow([n, g])
    print(f"wrote {OUT} ({len(G)} rows 0..{N}), max G = {max(G)}")

if __name__ == "__main__":
    main()
