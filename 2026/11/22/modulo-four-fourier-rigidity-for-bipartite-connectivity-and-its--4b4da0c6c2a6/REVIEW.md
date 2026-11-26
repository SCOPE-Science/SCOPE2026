# Independent mathematical audit

## correctness

PASS

For an edge subset with no isolated right vertex, its nonempty right neighborhoods generate a partition of the left shore by equivalence closure. The subset is connected exactly when this generated partition is one block. Summing the signed weights of neighborhoods lying inside blocks, then applying the partition-lattice Möbius function, proves equation (1). The source's phrase 'common coarsest partition' should be understood as this finest compatible partition, or join of neighborhood-generated relations; the actual inversion uses the correct containment. Even numbers of blocks give even column factors and hence products divisible by four; factorials discard all block counts ≥5. The surviving one-block term is (−1)^n and each three-block term is 2 modulo four. The Stirling recurrence gives S(m,3)≡m mod 2, including m=2. For m=2 opposite signs in every column kill the two-block term. For m=3 columns (++−) and (−−+) include one column annihilating each two-block term, as do (++−) and (+−+); the specified multiplicities give −1 for even n and +1 for odd n, with transposition covering n=2. Nonzero integer multipliers give invertibility and the sharp thin unit gaps. Fresh BFS plus integer Walsh transform reproduced all 65,536 coefficients and every bin of the 49-level frozen histogram: rank 65,536, |W|min=3 (11,664 instances of −3), |W|max=W(0)=36,317, and Parseval sum 2,380,070,912. Counting convolution on the unitary character basis therefore has inverse norm 1/3 and condition number 36,317/3.

## originality

PASS

The signed connected-subgraph polynomial, Fourier diagonalization, and Möbius machinery are established. The distinct content is the residue for every edge-sign assignment, the simultaneous sharp thin-shore unit gaps, and the first unrestricted nonunit gap and complete histogram. The closest inspected sources concern vertex-colouring data, fixed edge counts including spanning trees, or known polynomial expressions rather than the evaluated congruence and gaps. In particular the K(2,n) layer formulas give overlap in the summands of the thin case, not a formula in the inspected statements for the whole theorem.

## value

PASS

The natural connected-spanning indicator defines a recovery operator whose nonvanishing is not guaranteed by generic Fourier theory. A sign-uniform mod-4 invariant establishes exact recoverability across all bicliques; explicit small-shore witnesses and the complete first thicker case identify where the unit spectral floor first increases. The exact multiplicity and extremal coefficients answer conditioning questions for a standard host and distinguish the observable sharply from the spanning-tree projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
