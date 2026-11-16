# Scientific review: checkerboard Hermite sampling

## Correctness

PASS. All assertions concern the full space \(PW_\pi^d\), not a finite discretization. Parity-sublattice Fourier periodization produces an exact two-alias, two-channel Gram matrix. Its trace and determinant reduce the sharp extrema to a finite signed-sum gap and a cube midpoint endpoint. Strict root monotonicity establishes that the claimed lower and upper bounds are attained as essential endpoints. Rademacher averaging and the \(\ell^1\)/\(\ell^2\) inequality prove the unique optimal direction. A scalar minimization determines the unique gain and sharp condition number, and a Taylor expansion proves the quadratic degeneration. All normalizations, complex offsets, equality cases and singularity claims were reconstructed. The reproducible checker passes 6,720 random fibers, 5,760 extreme fibers and the dimension-free closed-form constants; finite checks are corroboration, not the proof.

## Originality

PASS relative to accessible statements and searched records, subject to the risks below. General Fourier-multiplier/Hermite interpolation (Gardeazabal-Gutiérrez and Sousa, arXiv:2506.16195v2, Theorem 1 and Sections 3.3–3.4) is a one-dimensional matrix criterion and does not state the full multidimensional parity geometry, sharp signed-gap bounds, or optimal derivative channel. Ghosh, Mulleti and Seelamantula (arXiv:2610.36142v1) establish a broad polyphase framework; the abstract and externally accessible section-level material do not explicitly state this checkerboard design theorem. Published works on finite-group parity-check Fourier spectra and one-dimensional dynamical sampling were inspected at the level of their actual result documents; they concern distinct operators and do not imply this theorem without additional arguments. General alias splitting, Plancherel and the two-by-two singular-value formula are standard ingredients, not themselves claimed as new.

## Mathematical value

PASS. The result answers a natural critical-density acquisition design question for multidimensional bandlimited functions: precisely which derivative orientations recover the full bandwidth, the optimal constants for every orientation and offset, and the globally least noise-amplifying derivative direction and gain. It identifies a discrete signed subset-sum obstruction, a sharp quadratic instability near that obstruction, and a dimension-free best condition number. These exact, all-dimensional design facts go beyond a generic invertibility statement; no broader reconstruction theorem is claimed.

## Limits and priority risk

The October 2026 motivating full manuscript could not be accessed; only its primary abstract and external section-linked descriptions were available. Older multivariate Hermite interpolation or optical checkerboard sampling literature might use an equivalent normalization or implicit optimality result. The specific proof makes no claim about generalized passbands, multiderivative channels or optimality over nonlinear measurements. Numerical testing cannot establish the infinite-dimensional assertions.

Self-review: passed. Independent audit: not yet performed.
