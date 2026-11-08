# Self-review

## Correctness — PASS

For each \(0<h<2\), explicitly constructed position- and velocity-Verlet matrices have unit determinants and traces strictly between \(-2\) and \(2\), ensuring bounded powers separately. Their average Gram matrix is exactly \((1+h^6/32)I_2\). Conditional expectation under independent fair selection proves the complete finite-step energy law for all deterministic starts; taking a logarithm proves the \(h^{-5}\) physical-time scale. For arbitrary \(p\in(0,1)\), the three-dimensional covariance transfer has \(\det(I-T_p)=-h^8p(1-p)(8-h^2)^2/128<0\), whence a spectral radius greater than one, and preservation of the positive semidefinite cone proves failure of uniform mean-square stability. For deterministic alternation the explicit unimodular two-step trace crosses \(-2\) at \(h=\sqrt5-1\), with a nontrivial Jordan block there. All signs and boundary cases follow directly. The accompanying rational checker successfully tested 1,302 identities/finite-path assertions; those tests do not replace the proof.

## Originality — PASS (qualified)

Casas–Sanz-Serna–Shaw (2022) give deterministic Strang/Verlet stability and semitrace formulas; Ni–Hu (2024) identify different modified Hamiltonians for the two fixed Verlet orders. Batcho–Schlick (2001) study resonance in two-component impulse-Verlet with fixed inner method, and Lie–Stahn–Sullivan (2021) study additive-randomized one-step methods on finite horizons. These do not imply the exact independent-order mean-energy multiplier, its mixing-probability second-moment determinant, or the single-oscillator alternating-order threshold. The closely related older fixed-method, randomized-step and first-order random-order results differ in both the operator composition and quantified observable. Publication precedence remains qualified because an equivalent mixed-Verlet calculation could be embedded in older geometric integration work.

## Value — PASS

Numerical integration practice relies on long-time near-energy conservation of symplectic single-method updates. This theorem exhibits a reproducible, conceptually significant obstruction: iid random mixing of two individually bounded *second-order symplectic* maps inflates expected physical energy exactly, with a sharp sixth-power step coefficient, while deterministic alternation has its own unexpected step threshold. The exact error-growth timescale and contrasting switching laws give an interpretable test case for randomized geometric integration rather than an arbitrary parameter table.

## Sources and residual risk

Closest scientific sources: Casas, Sanz-Serna and Shaw, arXiv:2210.07048 (2022); Ni and Hu, arXiv:2407.18726 (2024); Batcho and Schlick, DOI 10.1063/1.1389855 (2001); Lie, Stahn and Sullivan, arXiv:2103.16506 (2021). An equivalent older presentation may exist; no claim of independent scientific verification, general nonlinear applicability or almost-sure exponential growth is made.

Self-review: passed. Independent audit: not yet performed.
