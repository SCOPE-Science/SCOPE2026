# Mathematical review of the joint acute-center limit

## Correctness — PASS
The object is the affine image of three independent uniform circle points with ellipse semiaxes \(L,1\). For an acute triangle, consecutive ordered abscissa gaps satisfy \(L^2g_1g_2<4\), forcing a close pair outside a negligible triple-collision corner. Opposite sine branches of that close pair give an allowable abscissa separation of length \(4(1-c^2)/(L^2|d-c|)\). The arcsine-law Jacobian cancels \(1-c^2\), and center enclosure forces \(cd<0\) and \(|c|<|d|\). The resulting integrable two-variable kernel integrates to \(2\pi\log2\), giving the exact coefficient \(6\log2/\pi^2\). Factorizing the conditional limiting kernel proves the independent arcsine and logarithmic-ratio marks. The exceptional triple collision and endpoint regions are bounded by truncation and integrable domination. The package's direct Cartesian checker corroborates these identities, but does not replace the analytic proof.

## Originality — PASS, with priority risk
The known equiaffine-ellipse **marginal** acuteness law has an exact dilogarithmic expression and was found in multiple earlier published findings (identifiers `a5911e351b92`, `0b2e5b1aac57`, `72d4f16967d8`). Their complete accessible mathematical texts do not state or imply the joint event with **center enclosure** or the conditional two-mark limit. The 2018 off-center circular enclosure probability is a different probability space and event. The 2013 random-circle polygon paper concerns perimeter and area extremes. The ordinary-arclength ellipse discussion in 2025 assumes a different sampling measure. None of the inspected closely related sources gives the joint constant or marked limit. Unindexed equivalent literature remains a possibility; originality is a best-knowledge assessment, not proof of absolute priority.

## Value — PASS
For the circle, a triangle is acute precisely when it encloses the circle's center, but under anisotropic affine deformation the marginal acute event may persist without central enclosure. The joint law resolves this important geometric dependence question: the conditional enclosure probability tends to zero like \(\log2/(2\log L)\), and the factorized marks explain which exceptional acute triangles do enclose the center. This is not a routine recomputation of the already-published marginal law.

## Limitations
The result is asymptotic for three independent equiaffine-uniform vertices of one ellipse, with no explicit convergence rate or Euclidean arclength version. Historical priority is not independently certified, and simulation cannot certify the total-variation limit.

Self-review: passed. Independent audit: not yet performed.
