# Independent mathematical audit

## correctness

PASS

The 11-dimensional row/column character gauge fixes the first row and column to zero without changing Hamming parity. The complete labelled 6x6 margin-three matrix family is encoded injectively by its lower-right 5x5 block. Independently implemented C++ recursion over all 20 legal row masks, tracking six remaining column capacities; it enumerated exactly 297200 valid matrices. A complete exact signed 25-dimensional Walsh–Hadamard transform of all 33,554,432 representatives gave odd_nonzero=0, even_nonzero=16,777,216, wrong_even_residue_mod32=0, min_abs=16, witness W(36045)=16, Parseval sumsq=9,972,377,190,400. This is exhaustive exact-integer proof for this finite family, not sampling; the original independent column-first Python checker is consistent. Diagonalizing convolution and complement parity yields rank 2^35, inverse norm 1/16, and P=(I+tau_J)/2 of ell^p norm one.

## originality

PASS

The known count 297200 and elementary complement cancellation on odd frequencies do not imply nonvanishing of every even coefficient or its universal residue 16 mod 32. General fixed-margin table sampling/counting and Fourier analysis of partial Hadamards concern other invariants/families. Exact zero-locus plus sharp inverse are not identified as covered by those primary results.

## value

PASS

Fully labelled balanced binary matrices are natural regular bipartite graph incidence states. The uniform parity-residue theorem and exact Fourier zero set solve a complete deconvolution identifiability and sharp stability problem on this fixed natural family, beyond the already known cardinality; costly 2^25 exhaustive work has a precise mathematical interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
