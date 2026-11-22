# Independent mathematical audit

## correctness

PASS

The spin-one degree-14 diagonal squared harmonic profiles expand in Legendre polynomials P_J for J=0..28. Exact Wigner 3j evaluation vanishes only for J=20; Clebsch-Gordan orthogonality gives codimension-one profile span. A positive r-latitude rule therefore has moment functional L_t=integral[1+t P20]dx/2. The 15x15 moment matrix D+tG has even and odd determinant polynomials of degrees 5 and 4; independent exact SymPy reconstruction confirmed each squarefree, their gcd 1, an isolated simple negative determinant root in (-19331/5000,-1933/500), no roots between it and zero, and strict positivity of both 14x14 localizers (1 +/- x) at both interval endpoints. Consequently matrix rank >=14 for every t, and at the first negative root is rank14 PSD. Positive localizing forms and the cyclic multiplication-operator argument give 14 distinct interior nodes with positive weights exact through degree 28 for the required moments; 29 evenly spaced azimuths remove all off-diagonal m differences. Recomputed all Wigner 3j zeros (only 20) and the rational determinant/localizer certificates independently. The algebraic construction, not numerical approximations, proves existence and sharp obstruction.

## originality

PASS

The exact rank obstruction and positive construction exploiting the known Wigner P20 gap are not supplied by the inspected bandlimited spin-s sampling theorem or Wigner-zero survey; qualified best-of-knowledge original.

## value

PASS

For a natural 29-dimensional pure spin-one spherical-harmonic band, minimum distinct sampling latitudes under positive tight weights is an intrinsic design invariant. The surprising one-node saving relative to full 28-degree Gaussian quadrature is explained by the special Wigner zero, and an exact PSD moment matrix/localizer certificate proves both necessity and sufficiency. This is a substantive structural cubature result, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
