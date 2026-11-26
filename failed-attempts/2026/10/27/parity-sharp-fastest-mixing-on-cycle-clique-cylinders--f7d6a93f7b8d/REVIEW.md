# Independent mathematical audit

## correctness

PASS

Averaging by the graph action preserves feasibility and does not increase the convex SLEM norm, so the invariant solution gives the global value. For nonnegative directional weights a,b the full product spectrum has nonconstant displacements from 1 ranging between min(a s_n,mb) and a L_n+mb; the formula still holds on the boundary (including repeated eigenvalue 1). A gap gamma therefore requires at least a=gamma/s_n and b=gamma/m. These minima are jointly feasible precisely when gamma meets the spectral constraint gamma(2+L_n/s_n)≤2 and capacity constraint gamma(2/s_n+(m−1)/m)≤1. Either tight constraint forces both weights, proving uniqueness only in the invariant class. The spectral bound is tighter iff L_n+2s_n/m≥4, automatic when n is even; when n is odd this is m≤8 cos²(pi/(2n)), giving the n=3 equality at m=6 and the 7/8 cutoff for odd n≥5. At the Metropolis weights a=b=1/(m+1), the exact gap is min(s_n,m,2(m+1)−L_n−m)/(m+1). For m≥3 the third numerator is ≥m−2 and the first dominates eventually; for m=2 it is 4−L_n, zero on even cycles and the smallest numerator for odd cycles. Taylor expansion gives the stated ratios (m+1)/2 and 6. Replay by the spectrum and inequalities in frozen RESULT.md lines 39–91; verification materials were inspected, not executed.

## originality

FAIL

Two distinct indexed theorems cover the central claim by direct substitution, and the earlier published discrete-time symmetry and product-spectrum approach reduces it to the same elementary capacity calculation. The indexed theorems are dated Nov. 2, after the Oct. 27 frozen record; the finding is mathematical coverage, not a determination of who first derived it. The Metropolis comparison is a substitution into the same product spectrum, not a distinct surviving theorem.

## value

FAIL

The parity threshold is useful when choosing stochastic weights, but at this scope it is a direct cycle-eigenvalue substitution into the existing two-branch product optimum, with no additional sharp graph invariant beyond that specialization. The heuristic factors are obtained by substituting common edge weights and expanding the same two spectral endpoints. The record claims no new unrestricted uniqueness, separate rigidity, or independently motivated exact feature that survives the covered product formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
