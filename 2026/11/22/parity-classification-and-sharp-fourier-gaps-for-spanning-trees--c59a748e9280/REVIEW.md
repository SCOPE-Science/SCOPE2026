# Independent mathematical audit

## correctness

PASS

A spanning tree deletes k−1 edges. Deleting two edges in one arm would strand internal vertices, and the terminals must be joined by an intact arm. Conversely, retaining one whole arm and deleting one edge from each other arm yields a spanning tree. Factoring out the product of all edge signs therefore gives the signed e_(k−1) of the arm sums. Each j-vector occurs with the product of binomial multiplicities, and Walsh diagonalization on the full edge group gives the rank and the singular magnitudes; the zero frequency attains the triangle-inequality maximum τ. For one even arm, exactly the monomial omitting that arm is odd; the other monomials are even (the first sentence of Proof Step 3 phrases this backwards). Taking that arm sum zero and the other sums one attains the unit minimum. If all arms are odd, the parity is that of k, and with arm sums ±1 the polynomial equals their product times their sum: odd k attains magnitude one, while even k attains both zero and magnitude two. With s≥2, two zero even-arm sums force zero, each monomial is divisible by 2^(s−1), and one zero even-arm sum with the others two and the odd sums one attains the bound. Each witness is permitted by the stated length and parity restrictions.

## originality

PASS

The added result is the arbitrary-arm parity characterization and sharp strictly positive spectral gap, with attaining frequencies on the full edge group. Credit the standard signed weighted-tree identity, prior unweighted generalized-theta counting, and the already solved all-length-two spectrum. The closest inspected unequal-length Walsh calculation includes a direct terminal edge, which fixes a different admissible arm-sign range and does not cover these hypotheses.

## value

PASS

The theorem identifies exactly which theta convolution operators are invertible, and in the singular cases separates zero from the recoverable spectrum by a sharp parity-controlled scale. The realizable arm witnesses show that a uniform divisibility bound is the actual best bound, including unequal path lengths. This yields useful conditioning data not apparent from a generic determinant or ordinary tree count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
