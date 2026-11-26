# Independent mathematical audit

## correctness

PASS

For a nonconstant square-zero map, the first b values are one and its entire image lies in [1,b]; equivalently a=f(n)≤b. Counting weakly increasing suffixes gives binom(n−2,b−2), whose sum plus the zero map is 2^(n−2). Every type [a,b] is represented by a nonzero map with constant suffix a. For two nonzero maps one composite is always zero, since the smaller b bounds its own a and is at most the other b. Thus commutation means both products vanish, equivalent to overlap of their intervals. The zero map has the full interval type, so removing it preserves all types. Independently, for each interval I take the incidence vector of its points and its interior adjacent pairs, concatenated in that order. Against the diagonal form diag(I_p,−I_(p−1)), the pairing of I,J counts the points of I∩J minus its adjacent pairs and therefore equals the nonempty-intersection indicator. The singleton rows followed by the adjacent-pair rows give a block lower triangular square submatrix with identity diagonal blocks. Consequently the incidence matrix (also when rows are repeated by mapping from transformations, with or without z) has full column rank and the shifted adjacency is congruent to diag(I_p,−I_(p−1)) plus zeros. This independently gives rank 2p−1 and both asserted nullities, including p=1. The frozen checker and its recorded n=3 to 10 output were inspected, not executed; it compares exact incidence factorizations and numerical inertias. The independent congruence proof does not rely on those numerical signs.

## originality

PASS

The exact shifted inertia is the supported contribution. The square-zero cardinality and mutual annihilation comparison have antecedents. The result has a graph-theoretic equivalent as the signed Gram calculation of the full interval family, and the comparison did not establish prior coverage of that exact signature.

## value

PASS

The precise sign split and exponentially large −1 eigenspace describe how an exponentially sized natural commutation graph collapses to 2n−5 nonzero shifted directions. The interval incidence argument identifies these directions without numerical diagonalization and explains why removing the zero map costs exactly one null direction. It does not compute the other eigenvalues individually.

The dated certificate retains the supplied scientific assessment, sources and limitations.
