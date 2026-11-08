# Scientific review

## Correctness — PASS

The compression characteristic polynomial follows from the codimension-one cofactor identity, with coefficients \(u\) and \(\bar u\). The unique discriminant zero inside the spectral triangle is \(u=0\), where the compression has squared Frobenius norm one and is therefore a nonzero Jordan block. The unit-column condition-number formula follows from a direct two-by-two Schur eigenvector computation. Haar squared-coordinate weights have Dirichlet \((1,1,1)\) or \((1/2,1/2,1/2)\) laws, respectively, yielding local densities \(4/(3\sqrt3)\) and \(1/\pi\). Local gap and condition-number expansions prove the fourth-power limits and the moment frontier. The supplied checker passed 5,436 finite identity and simulation checks, which supplement rather than substitute for the limiting proof.

## Originality — PASS, qualified

The 2026 workshop explicitly raises distributions of non-Hermitian Ritz values for random subspaces. Shah's 2025 full-text pseudospectral-area estimates do not entail the fixed three-dimensional eigenvalue-gap and normalized-eigenvector tails; the prominent corollary concerns much smaller compression ranks. Carden–Hansen's known geometric characterization and Malamud's inverse-spectral perspective cover deterministic Ritz geometry, which is treated as an ingredient rather than a novel claim. Comparisons against available mathematical literature and published claim summaries did not identify the present two-field sharp constants or fourth-moment threshold. The complete Carden–Hansen paper was not accessible, leaving residual priority uncertainty, and no exhaustive literature search can establish uniqueness.

## Value — PASS

Even a compression of a **normal unitary** input can be arbitrarily close to a defective two-by-two output. The exact power-four law quantifies the frequency and severity of this eigenvector instability for both real and complex Haar trial spaces, and the finite-moment frontier is relevant when stochastic Ritz eigenvectors are averaged or stability is assessed in moments. Exact constants for a canonical three-point spectrum serve as a meaningful benchmark against general high-dimensional pseudospectral estimates.

## Closest prior literature and limitations

The closest sources are Amsel and coauthors (2026, Section 3.3), Shah (2025), Carden–Hansen (2013), and Malamud (2003). The proof does not address arbitrary spectra or actual Krylov-subspace sampling. Carden–Hansen's full text could not be checked, so probabilistic overlap with uninspected material remains a specific risk. All statements are in exact arithmetic and independent review has not yet occurred.

Self-review: passed. Independent audit: not yet performed.
