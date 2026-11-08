# Scientific review

## Correctness — PASS
For every \(0<t<1\), \(K\ge1\), the root \(S\) is positive definite, and \(A=S^2\) has principal root \(S\). The identities for \(X_1\) and \(X_2\) follow by direct, uniquely solvable Sylvester equations. The exact Jacobian in a Frobenius-orthonormal basis has eigenvalues \(\{-t,0,0,t\}\), yet its largest singular value equals \(t\sqrt{(K+K^{-1})/2}\). Exact rational checking confirms the explicit indefinite second iterate. Parameter inequalities are proved symbolically rather than inferred from finite samples.

## Originality — PASS (with historical-priority risk)
Gao–Kressner–Shao (arXiv:2607.12430v1) derive the frozen Sylvester method and provide sufficient small-error convergence conditions, not a negative example under fixed relative root/guess spectral equivalence, an exact Jacobian nonnormality factor, or a two-step positive-definiteness obstruction. Higham (1986) studies recomputed-derivative Newton and inverse-based simplifications, not the same recurrence; Sra (2016) studies geometric methods. Direct source, database and semantic searches did not identify the same statement or a theorem implying its quantitative conjunction. An unindexed equivalent analysis remains possible, and published sufficient conditions must not be mistaken for converse results.

## Value — PASS
The combined counterexample isolates an actionable distinction for refinement: bounded generalized eigenvalue ratios of an initial guess and locally contracting Jacobian eigenvalues, even together with vanishing relative root error, cannot replace an absolute-error or norm-aware basin condition. It explicitly quantifies transient amplification and departure from the positive cone of symmetric matrices. This is a meaningful limitation of a concrete recent algorithmic design, rather than a generic warning about nonnormality.

## Closest literature and limits
The quantitative claim is specific to exact arithmetic, the frozen-Sylvester recurrence, and an increasingly ill-conditioned positive-definite family; it is not a counterexample to the source paper's stated sufficient convergence hypotheses, nor to a complete mixed-precision implementation. A broader classical operator-norm result or an obscure exact example could affect novelty. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
