# Independent mathematical audit

## correctness

PASS

For every n≥w≥2 and deleted rank r∈{1,…,w}, F_{n,w,r} averages the w−1 remaining order statistics in each cyclic w-window. On each strict input-order chamber, the spatially ordered retained index selections of consecutive windows interlace coordinatewise: a_{i,k}≤b_{i,k}. Cumulative threshold differences q_{i,j}=(count selected left in earlier window−count in later)/(w−1) are nonnegative. Summing q_{i,j} over windows i=j−w+1,…,j telescopes to exactly 1, even with periodic wraparound. Thus each piecewise-linear chamber derivative acts on cyclic differences via a nonnegative column-stochastic matrix and has ℓ¹ norm ≤1. Integrating chamber derivatives along any x-to-y line segment proves the global two-input TV(Fx−Fy)≤TV(x−y), including tie cases via continuity. For n=w output is spatially constant (coefficient 0); arc indicator of width w attains coefficient 1 for n≥2w; special w=3,r=2, n=4,5 explicit rational pairs also attain 1. Independently checked 119,700 seeded pair/window/rank tests n=3..16, exact ratio-one examples for n=4,5, and inspected source checker which exhausts 925,164 chamber/arc combinations. No claim of all intermediate sharp constants for w<n<2w except midrange.

## originality

PASS

Best-of-knowledge originality after actual statement-level comparison: new scope not logically covered by primary work or published stronger indexed analogues; prior constituent lemmas and any exact known special cases are explicitly acknowledged.

## value

PASS

Uniform nonlinear two-input edge-TV nonexpansivity across every deletion rank and every window size, with a transparent positive-gradient mechanism and nontrivial sharp boundary (zero when n=w, one when n≥2w; midrange for all n). Directly separates robust deleted-rank means from amplified running medians, giving structural signal-processing stability beyond one-input smoothing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
