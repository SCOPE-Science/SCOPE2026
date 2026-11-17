# Independent mathematical audit

## correctness

PASS

Schubert normalization is [pt]=sigma_(ell,ell,ell). The integral vertical Pieri operators for e1 and e2 produce each top coefficient M_(ell,b)=∫e1^(3ell-2b)e2^b with b=0..floor(3ell/2); the top subgroup of the polynomial subring is exactly their integer span, so its index is their gcd. I independently implemented the integral partition-state DP without using CHECK.py and evaluated ALL 216 coefficients for ell=1..16, recomputed each gcd and the index 3,3,3 window and return to 1. The original Git CERTIFICATE.json stores all exact integers, and its width=13 first four match 57468093927120,21172455657360,7820456594160,2896406039280; the width=16 values were read as raw decimal integers to avoid JavaScript integer precision loss. Submitted CHECK.py also offers an independent alternant coefficient evaluator, but the independent DP itself confirms the full bounded claim. No ell>=17 extrapolation.

## originality

PASS

Best-of-knowledge new explicit finite-range integral top-class gcd/primitive threshold, separate from earlier rational filtrations and classical integer intersection formulas.

## value

PASS

The primitivity of a natural 2-Chern-generated top cohomology sublattice is a motivated integral refinement of rational cohomology filtrations. The first loss at ell=13 followed by recovery at ell=16 is a nontrivial structural boundary, and complete exact classification through the first failure/recovery range is a valuable finite result, not an arbitrary tiny test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
