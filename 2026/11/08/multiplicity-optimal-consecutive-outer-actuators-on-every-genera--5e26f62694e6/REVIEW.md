# Scientific review

## Correctness — PASS

The unweighted graph is explicitly defined with \(n\ge5\) and \(2\le k<n/2\); every Fourier block is the real-symmetric two-by-two matrix displayed in RESULT.md. Each block has distinct eigenvalues, and a corresponding vector cannot vanish on the outer layer. Hence a full Laplacian eigenspace consists of one Fourier column for each distinct frequency realizing its eigenvalue. The PBH lower bound is the maximum eigenspace dimension; the square Vandermonde restriction of that many **consecutive outer** coordinates has full column rank for every eigenspace, proving equality. The nonzero leading coefficient of the Chebyshev polynomial gives the \(2k+2\) bound without any approximation. The \(\operatorname{GP}(11,2)\) illustration is established by an explicit degree-ten resultant and a characteristic-two squarefreeness argument, with further integer-modular finite checks. Remaining limits: the proof applies to the stated fixed unweighted Laplacian, not all admissible edge weightings.

## Originality — PASS on inspected evidence, with publication-priority residual risk

Gera--Stănică (2011) derive the underlying two-band spectral formula but do not solve optimal coordinate-actuator placement. Parlangeli--Notarstefano (2011) prove reachability for paths and cycles, not generalized Petersen graphs. Rashidi--Poursalavati--Tavakkoli (2020), Theorem 2.2, already give a zero-forcing set of \(2k+2\) consecutive outer vertices; their Theorem 2.5 already gives the six-vertex zero-forcing number for \(\operatorname{GP}(n,2)\), \(n\ge10\). Those facts are excluded from the novelty claim. Their uniform zero-forcing construction does not imply the multiplicity-adaptive optimal placement, and the exact eleven-circumference example distinguishes the properties sharply. Dai (2022) analyzes minimal leader sets generally and for other graph families, without this all-parameter result. Relevant indexed research comparisons returned no claim with equivalent or stronger implication. Residual risk: specialist work outside the accessible indexed literature may contain an equivalent result.

## Mathematical value — PASS

The classification settles both the minimum number of independent coordinate inputs and an explicit attaining placement in an infinite two-parameter family of cubic networks. For general graphs the eigenvalue-multiplicity lower bound need not be achievable by coordinate actuators, so equality is a structural fact, not a definition. The \(\operatorname{GP}(11,2)\) example quantitatively separates a two-input fixed-dynamics solution from a six-vertex zero-forcing requirement. This gives an actionable exact design rule not implied by the existing zero-forcing bound.

Self-review: passed. Independent audit: not yet performed.
