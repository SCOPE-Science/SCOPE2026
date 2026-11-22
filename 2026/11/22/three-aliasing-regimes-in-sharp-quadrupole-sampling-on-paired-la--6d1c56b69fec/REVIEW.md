# Scientific review: three aliasing regimes for paired latitude rings

## Correctness — PASS
On the probability-normalized sphere, five explicit orthonormal real quadrupoles give diagonal norms \(C=5(3t-1)^2/4\), \(A=15t(1-t)/2\), \(B=15(1-t)^2/8\). Discrete root-of-unity orthogonality leaves no off-diagonal terms for ring sizes at least five, one order-two Nyquist block for four sites, and two order-one/order-two alias blocks for three sites. Reflection across the equator reverses the first-order components and gives coupling \(\sqrt{AB}|\sin(3\delta/2)|\). Exact eigenvalues and strict one-dimensional inequalities prove the full spectrum, both sharp optimization constants, the uniqueness of squared height, and complete phase equality cases. The standalone checker constructs complete Gram matrices independently for 512 configurations and verifies exact rational identities. No finite test substitutes for the supplied all-parameter proof.

## Originality — PASS under accessible sources
The published paired-ring quadrupole theorem (2026-11-01; identifier `38d9014ee346`) assumes at least five points per ring specifically to prevent aliases. It proves the shared height constant in its own nonaliasing regime, not the three- and four-point spectra, opposite angular optimalities, exceptional ranks, or the four-point E-optimal plateau. A published six-sample result (2026-11-08; `0de67cc2f408`) uses two great circles, not mirror-symmetric parallel latitude rings, and has different optimal parameters. The indexed two-ring determinant result (`35d45a63d3a2`) concerns full low-pass bands and row interpolation, not least-eigenvalue optimization on pure degree two. The 2014 iso-latitude reconstruction literature and the 2022 near-optimal sampling paper likewise do not supply these small-ring claims in inspected material. Unindexed related finite-frame designs remain a genuine priority risk.

## Value — PASS
Six equally weighted samples attain the exact best normalized worst-mode observation and condition number available for all two-ring populations in this natural symmetric family; this is the minimum feasible sample count for five quadrupole coefficients. The minimal six-point alignment is opposite to the optimal four-point half-step stagger, and the four-point E-optimality plateau is strictly larger than its condition-optimal set. These exact alias effects give actionable sensor placement distinctions beyond routine recomputation of a previously covered large-population case.

## Limits
No unrestricted six-site optimality, unequal weights, arbitrary ring geometries, or higher-degree sampling is established. The matched published large-population constant is acknowledged rather than asserted as independently new. Literature comparison is finite; independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
