# Self-review

## Correctness — PASS
Direct block inversion gives T=[[I,0,0],[X,-I,0],[0,EZ,I-E]]. The base identity I-T^2 is an exact last-block-row expression, and multiplication by I-T proves its formula for all m>=2. Positive definiteness of H(S1) and full row rank of B imply H(S2)>0; the accretive resolvent yields ||E||<=alpha/(mu+alpha)<1. GMRES minimizes over polynomials normalized at zero, proving its residual estimate and per-restart contraction. The exact scalar Gram determinant yields ||r2||^2=2 alpha^2/(1+alpha+alpha^2), validating the O(alpha) sharp order. Finite numerical and symbolic checks are supplementary.

The independent route from the matrix definitions to the residual polynomials and exact scalar example is set out in RESULT.md. `verify.py` passed 3,119 supplementary checks. Neither finite tests nor bibliographic searches are substitutes for proof.

## Originality — PASS (qualified)
The 2026 Chao–Li Theorem 8 supplies the block form and spectra but expressly declines to derive a GMRES rate because the matrix is nonnormal. The new statement uses that given form to derive a degree-by-degree last-row polynomial identity, an all-m right-preconditioned GMRES bound, a restarted-cycle guarantee, and a sharp two-step order example. Southworth–Sivas–Rhebergen 2020 prove broad two-block GMRES/Schur-complement relationships, but inspected relevant sections do not state this explicit three-block polynomial identity. Greif–He 2023 and Beik–Benzi 2022 treat different exact preconditioner families. Published mathematical-record searches produced no statement implying the exact formula. Novelty remains provisional against unindexed equivalents and alternative block regroupings.

Comparison of mathematical implications: Chao–Li provides precisely the needed block matrix but does not state the family of GMRES bounds; generic two-block polynomial/Schur theorems provide technique rather than the stated explicit three-block formula. Retrieved published records with similar terms address other preconditioners or different polynomial constructions. Residual risk: an unindexed special case or a reblocking of an older general theorem could imply the claim.

## Value — PASS
For a nonsymmetric coupled Stokes–Darcy matrix, eigenvalue clustering alone gives no quantitative GMRES residual bound, a gap explicitly flagged in the 2026 motivating work. The exact polynomial hierarchy turns the regularization parameter into a provable rate after two iterations, supplies a rigorous restarted GMRES criterion for the ideal preconditioner, and quantifies a nonremovable first-order obstruction at two steps. The constants are not asserted uniform over mesh or physical parameters, and no inexact-preconditioner conclusions are made.

## Closest literature and material limitations
- Z. Chao and T. Li, arXiv:2610.34692v1 (2026-10-26), Theorem 8 and nonnormality discussion: closest premise, block identity and spectra, no quantitative GMRES residual bound stated.
- B. S. Southworth, A. A. Sivas and S. Rhebergen, arXiv:1911.02664 (2020), introduction and results concerning two-by-two block-preconditioned GMRES: general mathematical framework, no same explicit identity seen.
- C. Greif and Y. He, DOI:10.1137/22M1518384 (2023): Stokes–Darcy MAC system, different preconditioners, available abstract and source discussion.
- F. P. A. Beik and M. Benzi, DOI:10.1007/s00211-021-01267-8 (2022): exact Stokes–Darcy three-block preconditioners with differing block matrices, accessible full HTML article inspected by matrix formulation and conclusions.
- P. Chidyagwai, S. Ladenheim and D. B. Szyld, DOI:10.1137/15M1032156 (2016): different constraint preconditioner; publisher abstract accessible but full paper not obtained.

Boundaries: the exact idealized model, real finite-dimensional matrices, accretivity, full row rank, exact arithmetic; no uniform mesh claim. Historical-priority risk is not eliminated by any database search.

Self-review: passed. Independent audit: not yet performed.
