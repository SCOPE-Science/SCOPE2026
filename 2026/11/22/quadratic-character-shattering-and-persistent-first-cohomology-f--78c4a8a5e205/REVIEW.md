# Independent mathematical audit

## correctness

PASS

A positive trace forces a matching. For an ordered point pair the PGL stabilizer is conjugate to the nonzero scalings, half of which have square determinant, so PSL remains 2-transitive with pair stabilizer (q−1)/2. Sharp triple transitivity of PGL gives a unique potential all-positive witness. On a supported triple, excluding the third positive removes one from the pair stabilizer, leaving a witness iff q≥5. Inclusion–exclusion gives the listed counts for the singleton and empty traces, strictly positive for n=q+1≥6; matching pairs have positive trace counts already at q=3. Four cells would violate uniqueness on three equations. Counting graph triples once gives |PSL| binom(n,3)=3 binom(n,3)², and every matched pair extends along a realizing graph. The edge character is symmetric since interchanging endpoints negates both determinants; for a projectivity the vertex rescalings occur twice around a triangle and the product equals the character of its determinant. Thus it is a cocycle on all selected triangles, and changing representatives adds the coboundary of the product of source and target rescaling characters at each cell. The triangle (∞,∞),(0,0),(1,a) for nonsquare a has a closed edge boundary with evaluation one, proving nonvanishing without any homology approximation. The compatible-pair graph is connected (any two cells have a common compatible cell in a row and column different from their own). For finite data, review_checks/psl.py closes the determinant-one permutation generators x↦x+1 and x↦−1/x, checks their group cardinalities, intersects bit masks for every labeling on every matching of size ≤3, and row-reduces the resulting incidence matrix over F₂. It independently gives (f₀,f₁,f₂; rank ∂₂)=(16,72,0;0),(36,450,1200;414),(64,1568,9408;1504) for q=3,5,7, and (β₁,β₂)=(1,786),(1,7904) for the last two. This tests prime-field claims only; the all-prime-power result is analytic. Here persistent means nonvanishing for each eligible q, not a claim about a filtration or persistence module.

## originality

PASS

The group action and full matching complex are standard, and a same-day record shares the point-image graph concept construction. The distinct content is the square-determinant half of the projective matching triples and its linked universal mod-two obstruction, with exact small-field ranks. No historical priority beyond the comparisons is claimed.

## value

PASS

The natural index-two subgroup keeps every compatible pair but deletes exactly half the matching triples, and the arithmetic deletion is detectable in first homology, not just in the face count. The complete shattering formula and universally witnessed obstruction are structurally useful; the first eligible finite cases quantify the obstruction without extrapolating a Betti formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
