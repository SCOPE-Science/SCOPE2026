# Independent mathematical audit

## correctness

PASS

Generic exposing objectives induce acyclic orientations, and conversely a topological order realizes any acyclic orientation. There is a directed cycle exactly when both mixed types occur. The leaf coordinates distinguish aligned columns from mixed columns, and the hub sums determine the mixed type whenever any mixed column is present, so distinct valid words give distinct vertices. The doubled-coordinate differences split into two hub sums and a sum of leaf squares. Applying the three-set inclusion–exclusion identity in each of the two copies gives the nine kernels; remove exactly N_n diagonals and divide by two. Hub states range from −n to n and the leaf-square sum from 0 to 4n, giving the stated integer-operation bounds. Integral zero-sum differences have even squared norm, and a valid single-edge flip realizes 2. The bound |hub|≤n/2, |leaf|≤1 is attained at all coordinates only for the two antipodal all-aligned words; equality in the diameter bound requires this pair. Independent replay (python /workspace/checks/reproduce.py 4) enumerates maximizing vertices by objective orders and matches all convolution coefficients for n=2..5. For the limits, deleting exceptional words and the sampling diagonal changes the relevant product laws by exponentially small total variation. The two raw hub-sign differences per leaf have covariance 2Σ with eigenvalues 8/3 and 8/9; squaring the half-scaled sum gives 2/3 and 2/9, and the leaf squares average 4/3 by the LLN, without requiring independence of hub and leaf statistics. Opposite branches shift the raw mean by (2/3,−2/3); the squared norm's linear fluctuation divided by n^{3/2} has variance 16/81. The same/opposite branch weights tend to one half each. The finite replay does not prove the asymptotics.

## originality

PASS

The valid-word class, product-cylinder decomposition, diameter and first squared-chord moment have prior coverage. The assessed distinct result is the full polynomial-state Euclidean two-vertex distance census and two branch-conditioned asymptotic laws for the canonical K_{2,n} realization. No inspected prior enumerator retains and combines the signed hub and leaf variables needed here; priority is bounded.

## value

PASS

The natural metric census records all vertex-chord threshold counts and is computable without enumerating exponentially many vertices. More than a radial or diameter calculation, it reveals two positive-mass populations with different powers of n and different fluctuation types. The explicit limits explain this split by the same/different branch hub offsets in the canonical Euclidean embedding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
