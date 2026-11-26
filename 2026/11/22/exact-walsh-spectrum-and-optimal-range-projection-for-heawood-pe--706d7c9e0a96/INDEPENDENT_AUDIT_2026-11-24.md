# Independent mathematical audit

## correctness

PASS

The Fano incidence rule gives AAᵀ=2I+J, so |det A|=24. There are exactly 24 admissible bijections and all are even in this labeling, giving equality of determinant and matching sum for every signing. Independently enumerating bijections and summing signs on all 256 tree-normalized classes gives (−8:45, 0:168, 8:42, 24:1). Switching at a vertex changes the contribution of every matching by −1. The switch space has dimension 13 and exactly half its elements reverse sign (the all-vertex relation involves 14 even vertices). Normalizing all tree signs uniquely leaves the eight cotree bits, giving the claimed signed full spectrum, rank 720896, nullity 1376256, nonzero condition number 3, and pseudoinverse norm 1/8. The symbol of the range projection is constant on switch classes, so its kernel vanishes off the cycle space; the cotree bits and fundamental-cycle coordinates are dual. The replay finds integer inverse-kernel histogram (−8:77, 0:108, 8:42, 16:28, 88:1), with absolute sum 1488 at denominator 256. Averaging any projection by translation conjugacy leaves range and identity on that range unchanged, and cannot increase the norm. The unique invariant projection is Fourier truncation; the row and column absolute-sum norms are both 93/16. The frozen checker uses int.bit_count (Python ≥3.10), notwithstanding its Python 3.9 instruction; the independent calculation does not rely on running it.

## originality

PASS

The unsigned matching count and determinant coincidence are known, as are the general methods. The checked same-graph Fourier calculation has a different support, and other close computations use different graphs or ground sets. No checked source establishes the signed census and sharp projection constant for this matching support.

## value

PASS

The Heawood graph is the canonical Fano incidence example, and its matching/determinant coincidence motivates comparing its unsigned count to its full signed cancellation profile. The census determines which Walsh magnitudes are available and how large the nullspace is; the sharp endpoint norm additionally quantifies the minimum range-projection cost over all linear projections, which rank or determinant bounds alone do not give. These form an exact benchmark on a natural graph rather than an arbitrary truncation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
