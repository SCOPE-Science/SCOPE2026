# Independent mathematical audit

## correctness

PASS

With R=F_q[t]/(t^m), commutation is R-module linearity on R⊕F_q. Multiplication by f is the long-to-long map; the short-to-long map lands in the span of e=t^(m−1); the long-to-short map factors through evaluation at t=0. The basis t^(m−1),…,t, followed by the short vector, then 1 triangularizes the resulting map with diagonal f(0) repeated m times and d once. Nilpotency thus leaves m−1 coefficients in F=f∈tR and two free off-diagonal scalars b,c. Its square has long multiplier F²+bc e, and from the cube onwards it is just multiplication by F^j on the long summand, zero elsewhere. At valuation v≤m−2, the image of tR is t^(v+1)R, the image of 1 adds a dimension, and the short column already lies in t^(v+1)R. Hence the rank is m−v. For h=ceil(m/v)≥4 the index is h; for h=2 it is 2 exactly when bc=0, giving 2q−1 cases; for h=3 cancellation requires 2v=m−1 and bc=−a(0)² for F=t^v a, giving q−1 cases in any characteristic. When F=0 or v=m−1, the nonzero rank is 1 if bc=0 and 2 otherwise; the corresponding indices are 2 and 3. This gives the residual coefficients and covers m=2. For index ≤2, start with (2q−1)q^floor(m/2) choices including zero and add (q−1)²q^floor(m/2) for the middle valuation when m is odd. For index ≤j with j≥3 the count is q²q^(m−ceil(m/j)), giving the marginals by differences. Index m has count (q−1)q^m for m≥4 from v=1 and for m=3 from the index-three marginal; splitting v at sqrt(m) gives the stated bound on distinct indices. A new finite-field rank and repeated-matrix-power check matched all joint fibers in 9 parameter cases, 12026 matrices, including F_4 and F_9. Replay: python3 /workspace/branches/448a05a7-ad37-4153-be7f-04abc951c6b5/independent_nilpotent_census.py; per-case output in independent_census_output.txt in the same directory. The frozen verifier was inspected, not executed.

## originality

FAIL

The audit found complete coverage of the substantive census by a distinct indexed hook-centralizer result: its exact labeled-matrix rank-of-powers table projects directly to the frozen rank/index coefficients for every m≥3. The residual m=2 case is a three-variable entry count, not an independent new contribution. The indexed result has a later catalogue path; the mathematical implication is verified, but no priority or attribution conclusion is drawn from those dates. Earlier work also gives essentially the same coordinate stratification, though not the numerical table.

## value

FAIL

Rank and nilpotency index are natural invariants of random elements of this finite centralizer, and the full point census has mathematical use. As a distinct finding, however, this record gives a projection of an indexed complete census for the whole nontrivial family; marginal formulas and the top-index density follow by aggregation or a single row count. The uncovered m=2 case is the elementary boundary of the same residual count, not a separately motivated mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
