# Self-review

## Correctness — PASS

The proof gives the exact Fourier root-of-unity block diagonalization and a convergent operator-valued Taylor expansion on each block. Exterior-power leading terms use uniquely the degrees \(0,\ldots,j\); their rank-one wedge coefficients yield the full ordered singular spectrum without numerical extrapolation. The monic Legendre norm and finite Vandermonde Gram determinants fix all constants, including the outermost and innermost eigenvalues. Exact endpoint cases \(L_r=1\), nonempty intervals, all positive integers \(q\), and the conversion between operator/eigenvalue and restriction/singular-value condition numbers are addressed. The standalone computation passed 134 reproducibility assertions; the mathematical proof is independent of those tests.

## Originality — PASS, with priority risk

The closest primary literature studies clustered Fourier Vandermonde singular-value **orders** and bounds (Batenkov et al., arXiv:1809.00658, Theorem 3.2; arXiv:1909.01927, Theorems 2.2–2.3 and Section 4; Batenkov–Goldman, arXiv:2107.09326, Theorems 2.3 and 7). The inspected statements and proofs do not give the exact spectrum of periodic multi-arc concentration for arbitrary sparse Fourier supports with the asserted per-level moment-determinant constants. The classical Legendre and confluent-Vandermonde ingredients are credited. The adjacent two-arc consecutive-band problem is narrower; its special case does not state the multi-residue, arbitrary-mask, all-level formula. Main residual risk: equivalent formulas could be recoverable in older generalized prolate or singular-perturbation treatments, and no independent priority determination has been made.

## Mathematical value — PASS

Observability from periodically gated measurements is natural in sparse spectral acquisition. This theorem gives a complete spectral invariant computable directly from the arithmetic partition of the frequency mask: it distinguishes perfectly tight sampling from near-singular classes, gives **every** sharp exponent and constant, and quantifies the exact least-observable mode through the terminal Vandermonde determinant. The all-mask statement is structurally different from evaluating a particular narrow-window matrix or merely reproducing known order bounds. Finite-width and perturbed-mask optimization are deliberately not claimed.

## Limitations and literature

All asymptotics are for fixed finite masks and fixed \(q\) as \(\alpha\downarrow0\). Continuous, noiseless restriction is the only measurement model. See RESULT.md references 1–4 and the structured originality comparisons in AUDIT.json. No proof of historical uniqueness or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
