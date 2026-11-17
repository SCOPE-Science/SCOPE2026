# Independent mathematical audit

## correctness

PASS

Let x_ij indicate selection and r_i,c_j be row/column selected counts. The exact open-neighborhood count at (i,j) is r_i+c_j−2x_ij, so admissibility is precisely 1≤r_i+c_j−2x_ij≤2 for every square. If m,n≥3 and row/column counts all ≤2, a two-selection row would force all remaining columns empty, implying all rows active; the resulting crossing contradicts the upper bound; by symmetry only ≤1 counts remain, which make any selected square have no selected neighbor. Thus an admissible matrix must have a fully selected row or column of length 3, forcing the other dimension exactly 3. In two rows, classify columns empty/single/double: 1 or 2 double columns, or one double with a same-row singleton, or all singletons in one row only for b=2,3. These disjoint exhaustive families yield for a=2: (b+2[b=2])z²+(2b(b−1)+2[b=3])z³+C(b,2)z⁴; for a=3: (b+3[b=3])z³; a≥4:0. Independent direct full subset enumeration of 2×2..2×7 and 3×3,3×4,4×4 agrees. Analytic proof covers all m,n.

## originality

PASS

The exact interval upper bound distinguishes total [1,2] domination from ordinary total k-domination (lower bound only) and non-total [1,2] sets. Full accessible Lv–Wu preprint covers general bounds, extremal classes and corona graphs, but no rectangular rook classification found in its displayed theorem/section material. Related Resultary rook-graph polynomials concern other domination predicates. No stronger implication to the full polynomial was established; historical priority still provisional.

## value

PASS

A natural two-parameter family of Hamming/rook graphs exhibits a sharp dimension cutoff and an unusually sparse complete all-cardinality enumerator, including exact labelled extremizers. This supplies a structural feasibility classification for a standard capacity-constrained total-domination parameter, not a trivial numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
