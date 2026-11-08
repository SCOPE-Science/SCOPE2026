# Scientific review

## Correctness — PASS

The result follows from the explicit equal-step extragradient matrix, the normal two-plane single-stage decomposition, and an exact positive-semidefinite rank-two Gram reduction for the period product. The Gram trace and determinant identify all three singular values, including parallel and orthogonal boundaries. Strict derivative negativity follows from the exact certificate \(4(1-c^2)>0\); the minimizer \(h=1/\sqrt2\) is unique even when larger steps \(h>1\) are allowed. The near-parallel expansion uses the verified derivative of the closed-form angular bound. The standalone verifier passed 16,131 assertions, including exact symbolic and rational identities. Finite numerical sampling is not used to prove universal quantifiers.

## Originality — PASS, with residual precedence risk

The closest prior source is Feng et al., arXiv:2310.02604v1, Theorem 3.1 and Appendix B: it proves general periodic extragradient convergence and stage normality, but its Floquet-eigenvalue discussion does not supply the present two-step Euclidean singular-value classification or optimize its one-period norm. Zhang and Yu, arXiv:1908.05699v4, Sec. 2–4, and Azizian et al., arXiv:1906.05945v5, study fixed-game convergence/parameter choices; these do not cover the changing rank-one payoff geometry. Targeted mathematical-record searches and primary literature comparisons did not establish an equivalent result. Noncommuting products of simple contractions and the required Gram algebra are established techniques; an unidentified specialized source could still contain the same formula. Novelty is this precise sharp classification, not the tools or general periodic convergence.

## Value — PASS

Two-period rank-one bilinear games are a minimal nontrivial time-varying example: each update leaves a one-dimensional neutral subspace, yet two nonparallel stages jointly contract every direction. The exact complete singular spectrum quantifies this effect, gives the optimal common step independently of row angle, and identifies a sharp near-degenerate slowdown of order \(\theta^2/14\). It directly addresses a periodwise robust stepsize-design question complementary to existing Floquet asymptotics. The claim concerns worst-case two-step error, not expected error, asymptotic rate optimization, or computational runtime. It is not an arbitrary parameter substitution or routine restatement of a fixed-payoff result.

## Closest literature and limitations

Relevant full-text sections inspected: Feng et al. (2023), method, Theorem 3.1 and Appendix B; Zhang and Yu (2020), equal-stage update, stability and rate sections; Azizian et al. (2020), fixed-game EG discussion. Further specialist prior results on products of rank-two normal contractions may cover the exact algebra. The scientific scope excludes noisy, nonunit, adaptive, constrained or nonlinear games and higher-dimensional untouched modes.

Self-review: passed. Independent audit: not yet performed.
