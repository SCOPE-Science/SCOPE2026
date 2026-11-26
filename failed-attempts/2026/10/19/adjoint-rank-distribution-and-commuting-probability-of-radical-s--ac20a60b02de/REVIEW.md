# Independent mathematical audit

## correctness

PASS

The arrow rows of [x,y] are δ_i v_i−u_i(c_i−c_{i+1}), with δ_i=d_i−d_{i+1}. A nonzero δ_i gives its own pivot, independent of the remaining incidence rows. Any proper subset of cycle incidence rows is independent by leaf elimination; the full set has rank n−1, also for the opposed arrows at n=2 and in characteristic two. The provisional rank counts the number of positions with either δ_i or u_i nonzero. Only constant diagonals with all u_i nonzero need correction down by one, giving q(q−1)^n(z^{n−1}−z^n). As an independent count of the provisional part, each zero-sum δ-vector has q diagonal preimages, and the number of zero-sum ordered lists of s nonzero differences is A_s=((q−1)^s+(q−1)(−1)^s)/q, by A_0=1 and A_{s+1}=(q−1)^s−A_s. Summing q binom(n,s) A_s (qz)^s[1+(q−1)z]^{n−s} gives the first two terms of P. The rank zero elements are scalar diagonals with no arrows; every k<n is realized by constant diagonal and k nonzero arrow coordinates, and rank n by nonconstant diagonal and nonzero arrows at all equal-diagonal edges. The probability is q^{−2n}P(q^{−1}). Independently, one can count commuting pairs by treating the pair of diagonal entries at each vertex as one of q² joint labels: each arrow permits q² choices for its two coefficients on equal labels and q on unequal labels. The cycle trace with these weights gives the same probability. Direct bounded counts gave 7/16 for (q,n)=(2,2), 1/4 for (2,3), and 17/81 for (3,2); separate full commutator-matrix checks gave the respective rank histograms (2,6,8), (2,6,32,24), and (3,24,54).

## originality

FAIL

The already catalogued October 12 graphic-matroid rank enumerator applies to every consistently oriented simple cycle n≥3. Its specialization gives the entire claimed polynomial, including the top-rank correction. The excluded n=2 case has the same commutator pencil ranks as the October 4 two-arrow Kronecker example by an explicit invertible sign change on the commutator output; it does not supply a distinct surviving invariant.

## value

FAIL

The full rank spectrum is a useful invariant of a natural family and the cycle dependence provides a clean example, but the supported contribution is a routine special case of the existing general enumerator, with the exceptional two-vertex case having an already computed commutator-equivalent spectrum. Re-presenting the specialization is not a surviving scientific advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
