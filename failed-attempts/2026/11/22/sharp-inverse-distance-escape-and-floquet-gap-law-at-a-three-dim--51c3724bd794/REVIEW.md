# Independent mathematical audit

## correctness

PASS

Independently reduced the upper flight using w=x-Hy+4μHz, which obeys w'=-2μw, and z''-2μz'+(1+μ²)z=1. The crossing conditions give the displayed x0,y0 and H=(ρ+E)/(1+Eρ), ρ=y0/x0 and E=e^(-2μt). For u=t-π, X=(1+k)/(k(1+μ²)), ρ=k(1-2μu)+O(u²) and E=k²(1-2μu)+O(u²), giving δ=cu+O(u²), A=cX and T=2t. For the return derivative, dt/dy=e^(μt)sin(t)/x0, and the derivative of the planar terminal y is -ρ/E by the planar flux/Jacobian identity. The involution then gives determinant ρ and trace H(ρ/E+E)+2μE(x0-Hy0)dt/dy. Expansion gives the stated trace coefficient and the simple eigenvalue derivative -2μ(1+k+k²)/D; squaring for the full return and changing parameter gives K. Rescaling the affine variation-of-constants expression in normalized time gives C¹ convergence separately on each flight; its explicit homogeneous form stays in the appropriate half-space and matches SP at π. These are fixed-μ statements, not uniform in μ or a claim about the original affine boundary orbit. Replay: RESULT.md lines 69–123 and Ferreira v1 Theorem 1 and Proposition 7. CHECK.py was inspected, not executed; no finite check is needed for the proof.

## originality

FAIL

The exact prior same-branch trajectory/return formulas mechanically supply the proposed boundary law. Ferreira already expands the crossings at the same endpoint in the half-period variable and treats the same spectral boundary. The new printed constants reduce to first-order expansion of those explicit expressions and conversion by a simple analytic parameter; the normalized flight follows by dropping the bounded affine term in the already specified exact flight and applying the same symmetry. This is demonstrated prior implication, not a claim that all the final constants appeared verbatim and not a decision based on unavailable literature.

## value

FAIL

The endpoint and the linkage of large amplitude to the loss of contraction are naturally motivated. Nevertheless, the exact output is a routinely accessible differentiation and rescaling of the earlier fully explicit classified branch. The loop convergence is just bounded-time affine ODE continuity plus the same involution, with no separate existence analysis or new control. No independently valuable nonmechanical remainder is established in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
