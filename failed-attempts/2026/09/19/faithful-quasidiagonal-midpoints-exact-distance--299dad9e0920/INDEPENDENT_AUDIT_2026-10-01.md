# Independent mathematical audit — SCOPE-20260919-299dad9e0920

Final disposition: **FAILED**.

## Correctness
**PASS** — The norm geometry is correct. Every quasidiagonal trace in Moradi's construction annihilates the self-adjoint unitary \(h=e^1-e^0\), while \(\omega_{c,t}(h)=c(2t-1)\), giving the lower bound. The midpoint \(q_c=(1-c)\gamma+c(\mu_0+\mu_1)/2\) is quasidiagonal, and \(\omega_{c,t}-q_c=c(t-1/2)(\mu_1-\mu_0)\); complementary sector support gives \(\|\mu_1-\mu_0\|=2\), so the lower bound is attained. For \(c<1\), the positive \(\gamma\) coefficient makes the traces faithful. Amenability follows from the quasidiagonal midpoint and faciality of amenable traces.

## Originality
**FAIL** — A published September 18 theorem, 'Tensor amplification yields maximal amenable-quasidiagonal trace separation', was read in full. Applied to Moradi's very same sector projections and traces, its \(r=1\) case proves \(\operatorname{dist}(\mu_i,T_{\mathrm{qd}})=1\), proves \((\mu_0+\mu_1)/2\) quasidiagonal, and proves the sector traces amenable. The assigned two-parameter distance profile then follows mechanically by convexly mixing with Moradi's faithful quasidiagonal trace \(\gamma\) and scaling the same norm-one separator. Thus the advertised family is a direct affine corollary of prior published structure.

### Equivalent formulations
After translating the chord to the sector direction, the assigned formula is exactly the affine scaling of the earlier endpoint distance calculation.

### Broader coverage
The prior theorem broadly dominates the sector geometry; only the faithful convex interpolation is added.

### Exact database or table
This exact published same-object record is decisive prior coverage.

### Claim versus prior implication
The final assigned claim is mechanically implied by the earlier theorem plus standard convexity/norm homogeneity.

## Value
**FAIL** — The affine interpolation is correct and visually clarifies the geometry, but once the September 18 exact endpoint theorem and Moradi's faithful quasidiagonal \(\gamma\) are known, the whole \(c|2t-1|\) profile is a one-line scaling argument. It is therefore a mechanically implied refinement rather than an independently valuable unknown exact fact under the stated value standard.

## Source inspections
- **Tensor amplification yields maximal amenable-quasidiagonal trace separation** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-tensor-amplified-maximal-amenable-qd-trace-separation--497bed58636c): complete RESULT.md. Assessment: STRONGER_SAME_OBJECT_PRIOR_COVERAGE. Evidence: The \(r=1\) theorem gives exact sector-trace distance one, quasidiagonal midpoint, and amenability in Moradi's construction; higher tensor powers strengthen it further.
- **Quasidiagonal traces need not form a face** (https://arxiv.org/abs/2609.18793): primary abstract/indexed record and the construction data quoted in the audited package. Assessment: SOURCE_CONTEXT. Evidence: Moradi supplies the sector-balance obstruction and the traces used by both records.

## Residual risks
- No correctness defect is asserted; rejection is mechanical prior implication.
