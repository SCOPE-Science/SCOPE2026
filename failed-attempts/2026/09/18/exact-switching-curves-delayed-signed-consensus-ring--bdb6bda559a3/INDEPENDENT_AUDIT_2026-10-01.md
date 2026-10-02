# Independent scientific audit — SCOPE-20260918-bdb6bda559a3

Audited at: 2026-10-01T08:23:38.851470Z

Disposition: **failed**

## Correctness — PASS

Starting from the published Fourier-mode characteristic equation, the half-sum/half-difference factorization gives \(\omega=2\sqrt{K_pK_n}\sin s\) and reconstructs both delay branches reversibly. For equal delays the scalar equation gives the displayed first crossing; implicit differentiation gives a positive crossing speed, and the stated modal ordering follows from monotonicity of the closed expression. The no-open-neutral-phase statement follows from the analytic switching curves plus standard retarded-DDE spectral continuity.

## Originality — FAIL

The final result is a direct specialization of the source characteristic equation together with established exact two-delay frequency-domain/D-decomposition methods and the standard scalar one-delay crossing analysis. The source-specific closed form is useful algebra, but under an implication-based originality bar it does not constitute a new mathematical mechanism.

### Equivalent formulations

The audited parametrization is the explicit solution of those same imaginary-root equations for this trigonometric ring coefficient.

### Broader coverage

General two-delay exact-spectrum machinery plus the already-published ring characteristic equation covers the substantive stability-switching mechanism.

### Exact database or table

This check is not decisive because originality fails by implication from broader published methods, even without identical tabulation.

### Claim versus prior implication

The final claim is a source-specific closed-form specialization of established machinery.

## Value — FAIL

The closed forms clarify the motivating numerical paper, but the mathematical content is chiefly direct spectral algebra and a standard switching-set interpretation. Under the stated bar, that is a useful derivation rather than a distinct new structural theorem.

## Sources inspected

- Delay-Induced Stability Transitions in Directed Signed Consensus Networks — https://arxiv.org/abs/2604.15570. COVERING_INGREDIENT: The source publishes the exact equation whose modulus/argument decomposition produces the audited curves.
- A Novel Frequency-Domain Approach for the Exact Range of Imaginary Spectra and the Stability Analysis of LTI Systems With Two Delays — https://doi.org/10.1109/ACCESS.2020.2973834. BROADER_COVERAGE: The published method treats exact imaginary spectra and stability for a general two-delay LTI class.

## Checked sources

- https://arxiv.org/abs/2604.15570
- https://doi.org/10.1109/ACCESS.2020.2973834
- https://arxiv.org/abs/2608.15133

## Residual risks

- The exact ring-specific closed form may not have been printed previously, but exact wording is not sufficient for originality when the implication is routine from the published equation and general method.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The conclusions concern the finite linear homogeneous ring with K_p>K_n>0.
- Special initial histories and nonlinear or time-varying models are outside the claim.
