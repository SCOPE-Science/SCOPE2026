# Independent mathematical audit

## correctness

PASS

For any two-edge matching the two sign indicators expand as 1-2I_e-2I_f+4I_e I_f. Counting disjoint partners of each edge proves W=3*C(n,4)-2*C(n-2,2)t+4q, while summing edge-sign products minus pairs meeting at vertices proves (S²-sum_v d_v²+N)/2. The signings with no negative edges, one negative edge and two disjoint negatives realize the gcd of A,2b,4; elementary binomial congruences make the gcd periodic modulo16. n=4,...,7 have odd A, and a seven-negative-edge star has W_8=0. Six negative star edges plus (1,2),(1,3) yield t=8,q=8 and W_8=2. The pinned C++17 2^27 representative Gray-code enumerator exploits the global sign symmetry, compares degree and negative-pair exact recurrences, and records the 84 signed-level histogram. A separate independently written C++ integer enumeration reproduced 2^28 total, zero count 20467680, 84 levels, min_nonzero=2 and Parseval energy 56371445760. Thus the finite rank and gap follow by Walsh diagonalization; no infinite nullity classification follows from the finite census.

## originality

PASS

The exact first-singular-order all-frequency nullity and sharp spectral gap for size-two matchings of complete graphs were not implied by the inspected unsigned matching-polynomial and intersecting-matching literature or by the eight-vertex four-edge perfect-matching spectrum; the elementary moment formula is not claimed independently new.

## value

PASS

The first dimension where the two-edge matching indicator develops a Fourier kernel is an intrinsic sharp cutoff; exact nullity and least surviving eigenvalue quantify reconstructibility and stable inversion on a natural complete-graph matching orbit. Distinguishing even-cardinality but zero-free residue classes from genuine zeros is a structural arithmetic phenomenon, not arbitrary parameter slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
