# Independent mathematical audit

## correctness

PASS

The fixed, nonempty, named palette is essential: even a colour missing from the host is an admissible request. An extension type of a marked word is exactly a gap and a colour. Induct on depth: after choosing a witness, the two split gaps and all unchanged gaps need depth at least one less. This is equivalent to all old gaps satisfying the next-depth interval recurrence, since the unchanged gaps then already satisfy the lower threshold. At rank at least t+1, choose a depth-t witness pivot for each colour; the leftmost pivot guarantees a depth-t prefix, the rightmost a depth-t suffix, and their ordered list is an all-colour permutation. Conversely, each colour in an embedded central permutation has the prescribed witnesses on both sides by subsequence monotonicity. The base is the empty pattern at t=0. The grammar flattens to exactly 2^t−1 permutation blocks; every minimum word has those fixed boundaries, hence length q(2^t−1), multiplicity 2^t−1 for each colour and count (q!)^(2^t−1). All other rank-at-least-t hosts contain one, so the basis is minimal; the floor-log size bound is attained by extending a basis word. This verifies the marked formula, all-depth quantifiers, and q=1 and absent-colour conventions in RESULT.md lines 27–60. The uploaded checker was inspected, not executed; no finite test is needed for the proved equivalence.

## originality

PASS

Pass is for identifying the one-point-extension rank of coloured words and of marked gaps with an exact function of existing subsequence universality. The permutation-block basis, minimum length and census for the universal-word problem are already consequences of the classical arch characterization at arbitrary k. They are not a separate original combinatorial classification. The checked rank results do not give the key rank–universality identification for q>1; the new use of the block criterion is that it decides the different adaptive extension game.

## value

PASS

The exact identification converts an adaptive marked-gap game into a static word invariant. In particular one can count greedy full-alphabet arches in each gap in one scan, rather than enumerate game strategies or use the cubic interval dynamic program; taking floor log₂ of one plus the smallest gap count gives the rank. This explains not only the optimal size but which fixed-size hosts succeed, including missing-colour and non-extremal cases. The rank transfer is the substantive value; counting already-classified permutation concatenations alone would not qualify.

The dated certificate retains the supplied scientific assessment, sources and limitations.
