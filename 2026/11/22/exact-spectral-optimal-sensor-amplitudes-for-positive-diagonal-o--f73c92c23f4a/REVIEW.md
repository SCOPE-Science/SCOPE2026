# Scientific review

## Correctness — PASS
All required quantifiers and boundaries are explicit: every integer dimension at least two, every consecutive horizon at least dimension minus one, and every strictly ordered positive stable spectrum. Generalized Vandermonde minors and Cauchy–Binet prove strict total positivity of the actual finite Gram matrix; cofactor signs make its conjugated inverse strictly positive. A Rayleigh quotient bounds the inverse top eigenvalue below by the sum of its entries. A precisely constructed positive vector is a Perron eigenvector with equality, and the equality case forces every squared sensor magnitude. The zero-coordinate, too-short-horizon and repeated-eigenvalue cases are handled separately. Exact rational verification checks the illustrative example and 885 exact rational diagnostic assertions in total; it is not substituted for the infinite family proof.

## Originality — PASS, qualified
The focal 2026 dynamical-sampling paper covers the frame Gramian and forcing-error reconstruction but not the sharp free sensor-amplitude design. The 2025/2026 optimal-dynamical-frames paper optimizes the count of generating vectors. Wu's 2026 sampling optimization holds the generating vectors fixed and varies observation times and weights. A 2008 nonnegative network allocation theorem has a different linear gain-budget constraint and does not directly imply this inverse-Gram, reciprocal-square sensor optimization. Published related finite-horizon sensor and spectral-scaling records use differing objectives (determinant or condition number), not the all-dimension sharp E-optimal allocation. The component matrix techniques are classical and are credited. Residual risk: an older general diagonal-scaling theorem could implicitly contain the result; novelty is supported by specific comparisons, not certified by search absence.

## Mathematical value — PASS
The smallest eigenvalue of a dynamical Gramian controls the worst-conditioned reconstruction direction, and optimizing its true value differs from maximizing determinant or minimizing condition number. The result solves the unrestricted single-sensor modal amplitude allocation exactly for every dimension and finite horizon, proves uniqueness up to phases, and yields closed rational allocations for rational modal spectra. It is a natural full classification rather than an arbitrary fixed-size example.

## Independent status
Self-review: passed. Independent audit: not yet performed.
