# Independent mathematical audit

## correctness

PASS

For any 8×8 matrix A of cubic roots, write A=J+Delta, all Delta entries divisible by pi=1-omega in Eisenstein integers. Expanding permanent over partial row-column matchings gives sum_k (8-k)! times size-k products Delta. The k=0 term has pi-valuation 2v3(8!)=4, whereas k=1..8 terms have lower valuations 5,6,5,6,7,6,7,8, so cancellation of the leading 8! term is impossible: per(A) is a nonzero multiple of 9 with modulus≥9. The displayed exponent matrix yields permutation residue counts (13446,13437,13437), hence exact permanent 9. For circulant exponent words a∈F3^8, integer-pair Eisenstein subset DP enumerates all 3^8=6561 cases, minimum squared modulus 1296 (so 36), precisely 48 minimizers and 59 distinct squared-modulus levels. I independently compiled and executed a separate exact C++/integer-pair implementation: minimum 1296, 48, 59, global witness 9. Finite 6561 enumeration IS exhaustive for the stated cyclic class, not for full 3^64 space (handled by valuation + witness).

## originality

PASS

The infinite order-(p^a-1) nonvanishing of cubic-root permanents is known, and is not claimed novel. Distinct exact order-eight sharp global minimum with attaining witness, the natural cyclic Fourier-frequency minimum 36 and 48/59 census are bounded new quantitative claims. The highly relevant 2015-2016 maximum-permanent literature is not fully readable; record an explicit priority risk, not fabricated full-text noncoverage.

## value

PASS

The natural 8=3²−1 boundary case is the first useful larger prime-power-minus-one example for zero-free cubic-root permanents. An exact global inverse norm and an independently exhaustive cyclic symmetric subspace spectrum with fourfold enhanced gap, count and 59-level distribution quantify stability beyond the known yes/no nonvanishing theorem; not a decorative tiny enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
