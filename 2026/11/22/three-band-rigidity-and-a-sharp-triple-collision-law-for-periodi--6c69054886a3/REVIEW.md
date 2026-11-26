# Independent mathematical audit

## correctness

PASS

Checked both the frozen mathematics and the revised exact-spectrum claim in /workspace/repairs/1/RESULT.md. In the exponent with k=q+sm, s times j is integral, so the cell DFT selects q exactly and leaves the normalized three-row block after a unit phase is removed. Centering the frequencies to −1,0,1 gives a real Gram matrix with adjacent entry a and endpoint entry b. Reflection gives the stated one-dimensional odd and two-dimensional even restrictions, and their dimensions yield the m-fold levels. The Vandermonde nodes are distinct before ε=1, making every level positive. Setting c=cos θ gives a−b=2(1−c)(1+2c)/3>0 in the open interval. Then Δ>3b/2 when b>0, ensuring that the odd level exceeds the lower even level, and for b<0 the upper-branch difference has the sign of 2(a−b)(a+b), with a+b=2ac. For b≥0 the upper even wins and c must be positive; hence the unique interior crossing is c=0, i.e. ε=1/4. Substitution gives (1/3,4/3,4/3); at ε=0 the Gram is the identity and at ε=1 it is all ones, giving rank m. The lower and upper comparisons establish the exact piecewise condition number. For the corroborating collision calculation, the Vandermonde product is (2 sin(θ/2))^4(2 sin θ)^2/27, leading 4θ^6/27; dividing by the odd level of order 4θ²/3 and the upper even level tending to 3 gives θ^4/27 for the least squared level, with even O(θ²) relative error. This independently verifies the constants and uniformity without relying on the finite power-sum tests. The inspected checker.py is standard-library only and was not executed. Scope is consecutive frequencies, equal weights and this symmetry, with no arbitrary-jitter extension.

## originality

PASS

The frozen finding's separate advertised sharp leading collision law does not pass as a distinct contribution: the 2026-11-08 midpoint theorem gives both leading constants by exact unitary reduction and rescaling. This is established coverage, not a correctness defect or an inference from failed retrieval. The repaired finding is the exact repeated three-band spectrum and quarter-grid ordering transition over the full displacement interval. The collision expansion is retained only as a credited check and consequence. No inspected source yields the repaired spectrum and branch comparison, which are not implied by prior limiting constants or order bounds.

## value

PASS

The revised result gives a complete conditioning diagnostic for the natural three-site extension of a periodically interleaved Fourier grid. A practitioner can identify the least stable mode and which parity controls the norm at any displacement, across all critically sampled grid sizes, rather than knowing only that instability develops at a triple collision. The interior change of maximizing mode is a concrete spectral boundary not detected in the known collision limits. This is an exact narrow invariant, not credit for a standard Fourier decomposition or for rederiving a known leading constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
