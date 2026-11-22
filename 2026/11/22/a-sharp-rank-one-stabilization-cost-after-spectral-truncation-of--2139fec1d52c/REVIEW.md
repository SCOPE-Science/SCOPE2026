# Scientific review

## Correctness (PASS)

The Riccati identity follows directly from \(2d-Kd^2+K^{-1}=0\), and the exact closed-loop eigenvalues are \(-1\) and \(-\sqrt2\). For arbitrary positive-semidefinite rank-one \(Y=zz^\top\), triangular structure proves stabilization is equivalent to \(z_2^2>K^{-1}\); the norm identity gives a strict lower bound and an explicit approaching sequence. This proves the global sharp infimum, nonattainment, and exact ratio. The packaged verifier checks algebraic identities using rational arithmetic in \(\mathbb Q(\sqrt2)\) and finite numerical witnesses, not an infinite exhaustive search.

## Originality (PASS, qualified)

Zhang--Zhou (2026) gives low-rank positive-eigenvalue truncations in mixed-precision CARE refinement but not the precise best rank-one stability-constrained Frobenius distance. Massei--Saluzzi (2026) provides safeguarded band truncation with a separate stability condition and \(A\) Hurwitz, unlike the current open-loop unstable family; these results do not imply the exact ratio. Benner et al. (2018) analyzes RADI approximations, not the stated optimal rank-one constraint. Searches for Riccati rank-one stability-preserving Frobenius approximation and small-residual post-truncation loss of stabilization located no exact covering theorem. Indexing omissions, alternative control-theory terminology, and older stabilization-aware low-rank work remain priority risks; the search is not a proof of novelty.

## Value (PASS)

A rank-pruning threshold is often chosen by spectral or residual error; this example proves that even vanishing errors and a uniformly stable exact controller do not justify that decision when actuator strength changes. More than a counterexample, it quantifies the globally optimal stabilization-preserving rank-one error and the unbounded trade-off, with a sharp nonattained boundary. It is a small, reproducible benchmark for algorithms that enforce a closed-loop test before truncating.

## Limits and nearby literature

The example is diagonal and relies on \(\|B\|_2=\sqrt K\to\infty\); it is not a uniform bounded-data failure. The 2010 Skaf--Boyd study instead truncates controller coefficients subject to a Lyapunov certificate, and its indexed summary does not resolve the present Riccati-solution approximation problem. The result makes no claim that every truncation policy is unsafe or that lower-precision CARE implementations necessarily encounter this configuration.

Self-review: passed. Independent audit: not yet performed.
