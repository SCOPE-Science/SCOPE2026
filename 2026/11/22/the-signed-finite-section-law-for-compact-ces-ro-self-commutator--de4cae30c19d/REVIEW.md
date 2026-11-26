# Independent mathematical audit

## correctness

PASS

The infinite Gram products give (1) with the stated sign, and sum of squares makes C_t Hilbert–Schmidt for fixed t<1. For s=m+k, the first two terms of the scaled kernel are -t^k[A_0 k sqrt(m/s)+(ms)^{3/2}Delta_s], with s^3 Delta_s tending to 2A_1 by the bound 2l and dominated summation; the third, t^k A_0 q^m sqrt(ms), tends uniformly to zero on the remote block. Fixed diagonals converge uniformly there, and the row-sum tails are controlled by summable (1+k)t^k. Thus the comparison is in norm after a congruence, not after a similarity preserving eigenvalue magnitudes. The Fourier series equals -t times the t-derivative of (1-2t cos(theta)+t^2)^(-1), giving (4) and its two isolated zeros. Banded circulant comparison (rank at most 2K), norm bounds, and counting at thresholds on either side of zero establish the limiting sign proportions; interlacing loses at most floor(epsilon N) signs of either type on adding back the omitted head. Both positive densities imply infinite inertia by the spectral theorem. Finally C_t tends to C_0 in Hilbert–Schmidt norm (the squared off-diagonal norm is at most t^2/(1-t^2) times sum (n+1)^(-2)); the ideal product inequality gives trace-norm convergence, not uniformity of the sign law. The independent numerical check in audit-checks/cesaro.py compares two separate Gram/kernel constructions and the Fourier coefficients; at N=320 it obtains negative fractions 0.4375, 0.334375, 0.20625 at t=0.2, 0.5, 0.8. Neither this nor the frozen checker's approximated geometric tail is used as proof of the limits.

## originality

PASS

The supported distinction is the explicit limiting sign proportions for this geometrically damped family. Operator definition and compactness are known; qualitative inertia of related families and the classical Toeplitz principle do not identify this rescaled commutator or evaluate its zero crossing. No independently matching law appeared in the bounded comparison.

## value

PASS

The family interpolates from a commuting compact diagonal operator to classical Cesàro at the other endpoint. A sharp continuous signature fraction for finite principal compressions gives information not captured by compactness, trace zero or existence of both signs. In particular the limiting half-negative behavior as t decreases to zero is not predicted by trace-norm convergence to zero. The invariant is natural for comparing signed compressions, and the proof requires identifying its operator-specific symbol rather than merely reusing the Toeplitz theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
