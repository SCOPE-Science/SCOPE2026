# Independent mathematical audit

## correctness

PASS

Longitude integration makes the four real azimuthal sectors orthogonal for both energies and makes the sine and cosine modes contribute the same scalar at each nonzero order. The cap-to-full ratio is the integral from t to 1 divided by that from 0 to 1 of the even squared associated Legendre density. The four polynomials and trace 7(1−t) check exactly. The first three pairwise gaps change sign or vanish only as shown by the factors 5t²−1 and 5t²−3; all gaps to order 3 are positive on (0,1), including the one with quartic 15(t²−2/5)²+13/5. The signs give every asserted ordering, and evaluation at the two squared cutoffs yields the stated five- and three-dimensional top eigenspaces and eigenvalues. Positivity on the interior makes the restriction injective and yields the stated square root condition number. Independent exact reconstruction from Cartesian harmonic basis polynomials and evaluation at both algebraic cutoffs agreed: python3 /workspace/reproductions/frozen_checks.py 5.

## originality

FAIL

The distinct 2026-10-26 Resultary record on cubic spherical harmonics on antipodal caps proves the same normalized spectral problem for every ambient dimension d≥3. Its theorem explicitly gives both transitions and maximizing spaces, including the first top multiplicity d(d+1)/2−1. At d=3 and earlier squared cutoff s=t², these are exactly the fivefold and threefold resonances here. The four spectral branches, full ordering, least branch, crossing values and condition number are determined directly by its exact general spectral formulas; expanding the polynomials is not a new mathematical result.

## value

FAIL

An extremal phase diagram for this natural cap problem is useful, but the frozen contribution is a mechanically implied fixed-dimension specialization of the prior phase diagram and exact branches. Expanded coefficients and surd evaluations do not supply an independently useful unknown invariant here; neither does taking the standard singular-value ratio from the known spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
