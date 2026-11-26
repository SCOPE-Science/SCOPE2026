# Independent mathematical audit

## correctness

PASS

Reconstructed both adjacency matrices and used exact integer characteristic polynomials and finite-field matrix arithmetic (replay: python /workspace/branches/independent_replay.py 2, Python 3 with SymPy). Both give (z+1)^16(z-1)^15(z^2-z-32). The -1 nullity sequences modulo 3 are (17,18,18,18) and (16,17,18,18), with +1 nullity constantly 15. The exceptional-component sum equations give dimensions 6,7,8 for the powers of A_E+I and dimension 5 for ker(A_E-I), so this is not inferred from cospectrality. Scalar extension preserves the Jordan data. On a Jordan block of length m the wave polynomial becomes a single-root degree-2m polynomial and the eigenspace is one-dimensional (v is fixed by u in the eigenvector equations), hence a single Jordan block of length 2m. In characteristic 3 the unipotent nullity at t is min(2m,3^v_3(t)); negative blocks contribute only at even t. The fixed-space dimensions replayed at 1,2,3,6,9,18 are (17,32,35,65,36,66) and (16,31,33,63,36,66), consistent with the all-time formulas. The largest positive blocks require a factor of 9 and the negative blocks a factor of 2, giving sharp order 18. Möbius inversion on its divisors gives the stated period-18 counts; unequal time-one counts rule out permutation conjugacy. The computation verifies integer and prime-field data; the Jordan argument covers all extensions, without enumeration of configurations.

## originality

PASS

Pass for the exceptional companion's modular structure and the full dynamical comparison of the two graphs, not for construction of the cospectral pair, the reversible update, or the previously computed friendship-side census.

## value

PASS

The pair is motivated by the historically exceptional failure of friendship-graph spectral determination. At equal ordinary spectrum and equal sharp clock, the different Jordan chain lengths show why even the first fixed-point population, and hence permutation conjugacy, cannot be inferred from those data. The full periodic population formulas are reusable exact data for this pair, not an arbitrary iterate or parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
