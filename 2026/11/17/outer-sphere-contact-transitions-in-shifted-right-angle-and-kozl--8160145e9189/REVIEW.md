# Self-review

## Correctness: PASS

For positive legs and integer shifts, every factor lies in its coordinatewise box bounded by the first and last staircase vertices. Adding these boxes proves the global upper/lower bounds and yields an attained diameter. The midpoint-radius identity proves unique minimum-ball optimality and reduces equality to box corners. The crucial nonstandard step is verified in the written proof: a binary point of a right-angle simplex must be one of its step vertices, and overlapping variable-support intervals force a single nonincreasing binary pattern throughout their union. This gives exactly \(\prod_\alpha(\ell_\alpha+1)\) contact vertices and \(2^{c-1}\) unordered diametral pairs. Vandermonde's identity proves the Kozlov specialization; the finite exact-arithmetic verifier passed 1,245 instances and 11,278 assertions. The tests do not claim to exhaust unbounded dimensions or shifts.

## Originality: PASS (provisional historical priority)

The central primary references were inspected in material detail, not inferred from search-result titles. Kozlov (1997, Sections 4--5) supplies the skeleton-vertex description; Snellman (2026, Sections 5 and 8--10) supplies shifted right-angle Minkowski sums and rank-two vertex results, but no minimum enclosing sphere or diameter-contact classification. The companion paper (2026) counts Hilbert-function sumsets, a different invariant. Searches in mathematical records and public primary literature found no stated all-rank overlap-component theorem, nor an equivalent minimum-ball contact count. The generic bounding-box radius inequality is standard and is explicitly excluded from the claim of novelty by itself. An equivalent theorem under orthoscheme, Minkowski-sum, or order-polytope language remains possible.

## Value: PASS

The exact outer-sphere geometry is a natural metric invariant of recently studied all-rank Kozlov polytopes, whose full higher-rank vertex structure is not generally classified. The result gives the complete sphere contact set and every diametral pair for *every* positive leg vector and rank, despite the missing full vertex census. The number of contacts depends only on shift-overlap intervals, creating an exact jump from \(n+s\) to \(n^2\) for two summands when the degree gap reaches \(n-1\); the binomial autocorrelation makes the Kozlov metric dependence fully explicit. This supplies a structural invariant, not just a generic diameter upper bound or a routine finite table.

## Risks and limitations

Priority is not independently established, and exact results in older orthoscheme literature could subsume the theorem. No assertions are made about entire facet lattices, inradii, arbitrary lattice points, or independent review. The only computational role is finite corroboration, not unbounded proof.

Self-review: passed. Independent audit: not yet performed.
