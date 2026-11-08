# Review of the period-realization theorem

## Correctness
PASS. The parametrization of the parallelogram gives exact horizontal section endpoints and horizontal lattice diameter. The full vertical span and its unique extremal vertices rule out every nonhorizontal diameter direction, including the equality boundary. Integer floor/ceiling arithmetic then counts exactly all diameter lines for each residue class. Distinct constituent slopes prove that a smaller eventual period cannot exist. The binary description bound is immediate from the four integer vertices. The standalone integer verifier passed 25 independent point-pair enumerations and 1,305 additional exact section-count comparisons. The finite checks are corroborative; they are not used to justify the infinitely quantified result.

## Originality
PASS (best knowledge, with the stated risk). Averkov et al. (arXiv:2508.20009, Sections 3--4 depending on revision) already prove eventual quasi-polynomial behavior and explicitly evaluate the period-three parallelogram; that particular case is credited, not claimed. Their general block theorem bounds possible periods by denominators but does not establish arbitrary **minimal** periods with a concrete primitive-edge centrally symmetric polygon for every modulus, nor the sharp coefficient-oscillation ratio or tabular-size consequence. Soprunov--Soprunova study the value of the lattice diameter/Minkowski length, not the multiplicity of diameter lines. Searches for equivalent and broader published statements yielded no direct coverage; the fact that the construction extends a documented period-three example is a meaningful residual priority/value risk.

## Mathematical value
PASS. The natural maximal-section counting function was introduced as an Ehrhart-type analogue, but unlike Ehrhart polynomials its leading coefficient can depend sharply on the dilation residue. This classification proves that the minimal quasi-period and the ratio of asymptotic leading coefficients are both unbounded **inside primitive-sided parallelograms**, and quantifies a concrete output-representation limitation with binary input. The claim is deliberately narrower than a universal period bound and the complexity consequence does not apply to compact formulas.

## Closest sources and remaining limits
The motivating 2025/2026 paper contains the precise \(q=3\) example, making overlap especially important. Its theorem for arbitrary polygons provides eventual quasi-polynomial behavior but no sharp period for the present parametrized family. The older Minkowski-length paper addresses a different invariant. The new theorem is independent of any numerical search for infinite validity, while its priority assessment remains provisional until further human literature review.

Self-review: passed. Independent audit: not yet performed.
