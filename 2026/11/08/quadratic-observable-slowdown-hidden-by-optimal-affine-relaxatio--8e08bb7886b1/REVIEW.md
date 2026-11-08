# Self-review

## Correctness — PASS

The Gaussian conditional mirror and independent-refresh branches preserve the target, but their independent Bernoulli mixture induces a second-moment map that is the mixture of symmetric-square matrices, not the square of the affine mean matrix. A direct exact cubic calculation gives a negative value at the classical affine-optimal rate and a positive value at one. Positivity plus a strict two-step covariance deficit proves its spectral radius lies below one; the operator-norm/Gelfand argument proves the slow quadratic eigenmode is visible in the actual position variance from a legitimate centered Gaussian initialization. The extracted standard-library checker tests exact rational formulas.

## Originality — PASS, with historical priority uncertainty

The affine critical damping, Gaussian antithetic reflection and spectral SOR method are known and are **not** the new claim. The covariance result uses independently random mirror/refresh switching, breaking fixed-linear-Gaussian covariance tensorization and yielding a new explicit cubic and strict gap. The 2026 motivating paper does not supply this formula, and inspected Roberts–Sahu and Fox–Parker Gaussian Gibbs results do not imply it. Older hybrid overrelaxation literature remains a priority risk, notably Wolff's partly inaccessible full article.

## Value — PASS

The theorem is a substantive quantitative warning about using the best first-degree rate as a proxy for quadratic sampler accuracy. It gives a strict gap for every nontrivial curvature condition number and constructs an actual Gaussian initialization with slower position-variance relaxation. It does not claim a complete mixing-time or sampling-cost bound.

## Closest sources and scope

Yuan–Guo–Chen (2026), arXiv:2610.16248v1 §3.1 and Appendices B–C; Roberts–Sahu (1997), J. R. Stat. Soc. B 59, §§1–2; Fox–Parker (2015), arXiv:1505.03512v1, §§1–5; Adler (1988), Phys. Rev. D 37; Neal (1995), technical report 9508; Wolff (1992), Phys. Lett. B 288. The latter three were checked from available abstracts and contextual discussion, not falsely represented as full-text negative examinations. The mathematical limitation is explicit: only the centered affine transition operator, not global convergence, is assessed.

Self-review: passed. Independent audit: not yet performed.
