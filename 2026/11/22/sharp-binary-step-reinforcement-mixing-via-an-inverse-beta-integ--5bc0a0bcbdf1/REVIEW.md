# Scientific review

## Correctness — PASS

The exact binary count transition \(\Pr(K_{n+1}=k+1\mid K_n=k)=(1-\alpha)/2+\alpha k/n\) follows directly from uniform historical copying. The continuous-time birth coupling has the standard Yule population-size distribution independent of its type choices. Its type-weighted branching equations produce \(A'=A^2+\alpha B^2\) and \(B'=(1+\alpha)AB\) with specified initial data. Their ratio yields the inverse-beta integral without missing initial factors. Positivity of the odd coefficients of the inverse and boundary analytic continuation isolate \(\pm R_\alpha\) as the two dominant singularities. Matching the pole coefficient and the parity sign gives \(d_{2m}\sim R_\alpha^{-2m}/(1+\alpha)\), with relative error \(O_\alpha(m^{-2\alpha/(1+\alpha)})\), and \(d_{2m+1}=0\). The supplied standalone rational checker compared 683 exact assertions at finite horizons and gave separate asymptotic diagnostics. Such checks are corroborative, not exhaustive proofs; complex singularity transfer is justified in the written proof.

## Originality — PASS against examined evidence

The April 8, 2026 Peres–Qin finite-group paper gives general exponential mixing and a binary two-step example but not the exact full binary generating function and leading asymptotic constant. The 2024 elephant-polynomial paper has the related characteristic recurrence but not the inverse-beta dominant-pole analysis of its zero evaluation. The 2026 local-limit paper proves Fourier upper estimates rather than an exact parity-frequency rate. A related near-total-reinforcement result takes \(n(1-\alpha_n)\to\lambda\), different from fixed \(0<\alpha<1\). A separate general transition-probability preprint was accessible only in its abstract, and unindexed prior generating-function methods could conceivably imply the calculation. The assessment is therefore best-knowledge originality, not independently certified priority.

## Value — PASS

The problem is a natural finite-group special case of a recently established exponential-mixing theorem, where a mere unspecified exponential upper bound leaves the true rate and its sharp prefactor unknown. Exactly identifying both rate and constant for every fixed nontrivial reinforcement parameter resolves a motivated convergence question, while the exact all-time inverse-beta generating function distinguishes strict parity cancellation from even-time relaxation. The nontrivial closed value \(R_{1/2}=\pi/2\) demonstrates the quantitative gain over unspecified bounds. It is deliberately a complete two-state result; it makes no unsupported general-group extrapolation.

## Closest literature and limitations

Peres and Qin, *Mixing times of step-reinforced random walks*, arXiv:2604.07207 (2026); Guérin, Laulin and Raschel, *Elephant polynomials*, arXiv:2401.04959 (2024); Murahara and Tokumitsu, *Optimal Rates in Local and Central Limit Theorems for the Elephant Random Walk*, arXiv:2610.35019 (2026); Peres and Qin, *Transition probabilities of step-reinforced random walks*, arXiv:2604.07227 (abstract only). Primary uncertainty is historical completeness, especially the inaccessible full text of the last work or a more general analytic recurrence theorem. Parameter-endpoint uniformity is unproved.

Self-review: passed. Independent audit: not yet performed.
