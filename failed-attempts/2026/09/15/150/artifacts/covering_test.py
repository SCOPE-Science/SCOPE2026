"""Covering-number recovery test for fractal dilation sets.

Compares two compact E subset [1,2] with upper Minkowski dimension beta=0.5:
  E_seq: polynomial sequence {1} U {1 + k^{-a}}, a=(1-beta)/beta = 1.
  E_cantor: homogeneous Cantor set with ratio 1/4 (dim log2/log4 = 0.5) mapped to [1,2].

Computes dyadic covering numbers N(E,delta) = min number of intervals of length
delta needed to cover E, via greedy algorithm on fine discretizations.
Reports delta^beta * N to test sup bound and limsup/liminf behavior.
"""
import numpy as np

beta = 0.5
a = (1 - beta) / beta
print(f"beta={beta}, a={a}")

# E_seq: points 1 + 1/k for k=1..Kmax plus limit 1
Kmax = 20000
seq_pts = np.array([1.0] + [1.0 + k**(-a) for k in range(1, Kmax+1)])
seq_pts = np.sort(seq_pts)

def covering_number_1d(pts, delta):
    # greedy covering of finite point set by intervals of length delta
    n = 0
    i = 0
    m = len(pts)
    while i < m:
        n += 1
        cover_until = pts[i] + delta
        i += 1
        while i < m and pts[i] <= cover_until:
            i += 1
    return n

def cantor_points(level, r=0.25):
    # intervals at given level in [0,1], return finely sampled points (endpoints + midpoints)
    intervals = [(0.0, 1.0)]
    for _ in range(level):
        new = []
        for (x0, x1) in intervals:
            L = x1 - x0
            new.append((x0, x0 + r*L))
            new.append((x1 - r*L, x1))
        intervals = new
    # sample each interval densely for covering estimate: use interval endpoints;
    # for covering number at scales >> interval length, endpoints suffice if we also
    # account for interval interiors: we cover intervals, not just endpoints.
    return intervals

def covering_number_intervals(intervals, delta):
    # minimal number of delta-intervals to cover union of intervals: greedy over sorted intervals
    # merge: walk along line
    intervals = sorted(intervals)
    n = 0
    cur_covered_until = -1e100
    i = 0
    # greedy: place delta-interval starting at leftmost uncovered point
    # leftmost uncovered = intervals[i][0] if > cur_covered_until else cur_covered_until
    while i < len(intervals):
        x0, x1 = intervals[i]
        start = max(x0, cur_covered_until)
        if start >= x1:
            i += 1
            continue
        # place cover [start, start+delta]
        n += 1
        cur_covered_until = start + delta
        # advance past covered intervals
        while i < len(intervals) and intervals[i][1] <= cur_covered_until:
            i += 1
        # if next interval partially covered, keep i (loop will handle)
        if i < len(intervals) and intervals[i][0] < cur_covered_until:
            pass
        else:
            pass
    return n

print("=== E_seq covering ===")
for j in range(2, 13):
    delta = 2.0**(-j)
    N = covering_number_1d(seq_pts, delta)
    print(f"delta=2^-{j}={delta:.6f}  N={N:5d}  delta^beta*N={delta**beta*N:.3f}")

print("=== E_cantor (level 8, r=1/4 in [1,2] via x->1+x) covering ===")
level = 8
ivs = cantor_points(level)
# map to [1,2]
ivs = [(1.0+x0, 1.0+x1) for (x0, x1) in ivs]
print(f"num intervals at level {level}: {len(ivs)}, length={(ivs[0][1]-ivs[0][0]):.2e}")
for j in range(2, 13):
    delta = 2.0**(-j)
    N = covering_number_intervals(ivs, delta)
    print(f"delta=2^-{j}={delta:.6f}  N={N:5d}  delta^beta*N={delta**beta*N:.3f}")

# Packing check at thick vs sparse scales for E_seq:
# count delta-separated subset size via greedy packing
def packing_number_1d(pts, delta):
    cnt = 0
    last = -1e100
    for x in pts:
        if x - last >= delta:
            cnt += 1
            last = x
    return cnt

print("=== E_seq packing (delta-separated subset size) ===")
for j in range(2, 13):
    delta = 2.0**(-j)
    M = packing_number_1d(seq_pts, delta)
    print(f"delta=2^-{j}  M={M:5d}  delta^beta*M={delta**beta*M:.3f}")
