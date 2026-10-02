# Independent mathematical audit

## correctness

PASS

Integrating the force-free kinetic Ornstein-Uhlenbeck SDE gives the deposited 2-by-2 scalar covariance block tensored with the identity. Its determinant is strictly positive for every positive step, so the innovation rank is 2d. Any affine simulator driven by one d-dimensional Gaussian has covariance rank at most d. The Gaussian W2/Bures rank-d approximation theorem keeps the d largest eigenvalues, yielding squared defect d times the smaller scalar-block eigenvalue. Direct series expansion gives the stated square-root defect with leading coefficient sqrt(d gamma alpha/6) h^(3/2). The committed verifier reproduces the determinant, eigenvalues and series and was inspected from the actual tree.

## originality

FAIL

Gillespie already gives exact joint simulation of an Ornstein-Uhlenbeck process and its time integral, so the full-rank exact Gaussian transition is classical. The 2023 Bures-Wasserstein Eckart-Young theorem gives the exact best covariance approximation at a prescribed rank. Combining those two prior results with rank at most d for one d-Gaussian draw mechanically yields the audited sharp one-draw defect; the small-h coefficient is then a Taylor expansion. Under the implication bar this is covered even though the exact Langevin wording is absent.

## value

FAIL

The resource interpretation is pedagogically useful, but the final theorem is a direct specialization of a classical exact Gaussian transition and a general spectral low-rank Bures theorem. The remaining rank and Taylor calculations are elementary, so no independently motivated new structural gap survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
