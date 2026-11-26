# Independent mathematical audit

## correctness

PASS

There are 1+21+35+105=162 partitions in block-size patterns (7), (5,2), (4,3), and (3,2,2); consecutive arcs determine the partition by recovering the connected paths. The exact independent restricted-growth-word replay in /workspace/branches/83a45965-603f-4b54-99fe-67131a410611/independent_replay.py (results independent_replay_n5.json and independent_replay_n7.json in the same directory) reproduced 157808 zeros, rank 1939344, least nonzero magnitude 2, the first 19 zero modes all of weight 3, projection-kernel support 521828 and absolute numerator 298503520. All first zeros were checked by direct parity summation; Plancherel and Walsh involution also held. The maximum 162 occurs at the trivial character and is an upper bound by the triangle inequality, giving condition 81. The second transform gives the kernel numerator because the inverse Walsh transform divides by 2^21; the quotient for the absolute sum is 9328235/65536. A projection onto the range fixes that range, so averaging conjugates by translations still fixes it and still maps into it. The average commutes with translations and is forced to be the nonzero-frequency cutoff, since each Walsh character spans a one-dimensional simultaneous translation eigenspace over either field. The absolute row and column sums both equal the kernel l1 norm, proving the global minima without requiring uniqueness among arbitrary optimal projections. The replay and conclusions are for the specified labeled incidence encoding, not all partitions or arbitrary n.

## originality

PASS

The checked sources establish the underlying partition enumeration and arc convention, or analyze substantially different Fourier encodings. They do not cover the seven-point singleton-free consecutive-arc spectral census and exact endpoint constant. The Walsh diagonalization and averaging argument are standard, not themselves originality claims.

## value

PASS

Singleton exclusion and consecutive arcs define a natural constrained partition code, also a path-cover model with no isolated vertices. The seven-label census gives an exact recovery boundary within this cube: one- and two-coordinate signs never cancel, while cubic signs do, despite the large recoverable space. A researcher using this fixed code needs the whole rank, conditioning and the optimal endpoint cost to distinguish local cancellations from operator-level stability. These statistics are not apparent from the ordinary partition count. No general-order classification is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
