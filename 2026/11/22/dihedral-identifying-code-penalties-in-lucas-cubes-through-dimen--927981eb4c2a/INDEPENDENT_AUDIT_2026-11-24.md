# Independent mathematical audit

## correctness

PASS

The graph is the induced cyclic no-adjacent-ones word graph, with closed Hamming-radius-one neighborhoods. For a given sensor set, intersecting each closed neighborhood and each pairwise symmetric difference is exactly the nonempty and distinct signature condition. It is upward closed, so excluding the entire layer of size I_n−1 excludes every smaller code. The independent exhaustive boundary-layer replay (independent_lucas_audit.py and witness_run.txt under /workspace/branches/dff87c4d-ce95-452d-bdb5-d831732613b7) tested all 20,030,010 ten-subsets and 34,597,290 eleven-subsets at n=7, giving zero and 259. A second independent search /workspace/evidence/lucas.py (outputs lucas-2-6.txt and lucas-7.txt) found the same results with disjoint branching: remove redundant superset constraints, split completions by the first selected available vertex in an unhit constraint, and when no constraints remain enumerate every exact-size completion. It certifies every cardinality through each optimum and directly verifies signatures for accepted codes. Both reconstruct the coordinate action and enumerate the code orbits and every union of vertex orbits. All rows agree: unrestricted minima 2,3,4,5,7,11, counts 1,4,13,21,18,259; invariant minima 2,3,4,5,8,14, counts 1,1,1,1,1,3. At n=6 the unique invariant optimum is the six singletons and the two alternating words. At n=7 there are nine optimum orbits of size 7 and fourteen of size 14; exactly three optimal invariant unions, each the weight-one orbit plus the orbit of 0000101, 0001001 or 0010101. The explicit unrestricted witness also passes direct signature testing. Repeated representatives at n=2 do not affect orbits. Therefore 6 is the first dimension in the stated range (and among n≥2) with a penalty, and the penalty at 7 is three. No extrapolation beyond 7.

## originality

PASS

Best-of-knowledge pass for the finite identification and full symmetry census on Lucas cubes, especially the first penalty and its equality cases; not for the generic hitting-set formulation, domination, or the known vertex orbit data. The exact catalogue hit is the frozen record itself. The close same-day Fibonacci result is not equivalent and its numerical behavior differs.

## value

PASS

The cyclic cube and full coordinate symmetry define a natural constraint on identifying placements. The finite cutoff contains the first strict symmetry penalty and the next case where it increases, and explains the equality cases and the difference between labelled codes, code orbits and invariant codes. These exact small benchmarks and explicit placements are meaningful without implying a growth law or an asymptotic threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
