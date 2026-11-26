# Independent mathematical audit

## correctness

PASS

On first differences the map is c₀ times F(a,b)=√(a²+ab+b²), where c₀=√2/3 for population SD. For a single changed coordinate with current value v>0, each affected window derivative divided by c₀ is in (−1/2,1]; for v<0 flip both signs, and at v=0 use the ±1/2 limits where differentiable. The full output-edge column is bounded by |a|+|b−a|+|b|, strictly below 3 on this half-open square; the two-edge maximum on its closure is 5/2 and the one inner-edge maximum is 3/2, both requiring an excluded corner. The isolated columns are bounded by 1. These give precisely the dimensions in the Finding, including zero variation for n=3. For strictness on arbitrary finite segments one can telescope the change one first-difference coordinate at a time. For each nonzero coordinate change, only one or two output rows vary, and their one-variable norms are absolutely continuous with the stated strict column bound almost everywhere (a zero pair can occur at just one point of that coordinate interval). Triangle inequality then gives a strict bound for every input pair, including segments contained in sets with other, identically zero windows. The frozen contrast choices approach (1,−1/2) or its reversed pair in the required column positions, proving the supremum. The uploaded numerical checker was read, not run.

## originality

FAIL

The main gain theorem is covered by the distinct indexed theorem on sliding triple pairwise ℓ_p dispersion: at p=2 the usual pairwise ℓ₂ norm of the three absolute pairwise differences is exactly three times population SD, and its indexed two-input path-variation gain specializes to the entire frozen dimension table. This is substantive coverage independent of any ordering of the two same-date records. Nonattainment is verified mathematically here but is not demonstrated by the indexed comparison and is not treated as already established there. That unresolved refinement does not validate the frozen finding's main assertion as a distinct gain theorem.

## value

PASS

The mathematical question is meaningful for a common sliding dispersion operator: the gain measures how changes propagate along the signal, and the nonattainment analysis separates maximal instability in a high-contrast limit from the behavior of every finite input pair. This does not give separate credit for the covered gain theorem and does not imply that a narrowed claim about nonattainment has cleared originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
