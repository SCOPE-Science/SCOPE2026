# Independent mathematical audit

## correctness

PASS

For p≥13 the sextic-in-x substitution gives a squarefree degree-twelve polynomial exactly off A=±2, so the smooth projective model has genus five. In the basis x^(j−1)dx/y the unrooted coefficient at row i, column j is [x^(pi−j)](x^12+A x^6+1)^((p−1)/2). Its support is j=i for p≡1 mod 6 and j=6−i for p≡−1 mod 6. Dividing the first three exponents by six and reflecting the other two by reciprocity gives degrees (r,2r,3r) and (r−1,2r−1,3r−1), respectively. Truncating the binomial series to degree m=(p−1)/2 is valid modulo p, giving the coefficient (−1)^d P_d(A/2). Inverse Frobenius is an automorphism of the algebraically closed ground field; on each matched one- or two-dimensional orbit Cartier is bijective when its coefficient is nonzero and zero otherwise, so 2,2,1 are stable-rank weights. The reversal in dimension five is even, leaving the determinant sign (−1)^d3. The Legendre leading coefficient 4^(−d)·binom(2d,d) is nonzero, and L_d(±2)=(±1)^d. The differential equation with leading factor A²−4 rules out a double root by successive differentiation because d<p. Hence all divisor and determinant degrees and the additivity of multiplicities at intersections follow on the smooth parameter line. Independent replay in branches/cartier_check.py used Rodrigues' formula and repeated bivariate multiplication for p=13,17,19,23, checking every symbolic entry and squarefreeness. The monic pairwise gcds in order (1,2),(1,3),(2,3) were (1,1,1) at 13 and (1,A,1) at 19. Thus the stated rank counts are correct: six of rank three and six of rank four at 13; one of rank two and eight each of ranks three and four at 19. The bounded checks corroborate the proof, not replace it; the frozen checker was inspected, not executed.

## originality

FAIL

Novoselov (2017), §2.2 Theorem 9(1)–(6) and proof, already gives the same coefficient matrix for the general even-degree family y²=x^(2g+2)−2ρx^(g+1)+1. Setting g=5 and ρ=−A/2 gives precisely the three Legendre entries with the same diagonal or antidiagonal arrangement and repetition. The exact determinant and geometric p-rank follow by multiplication and immediate counting of the nonzero Frobenius-permuted blocks. The reduced factors, degrees and multiplicities then follow from classical Legendre identities; allowing transcendental A changes nothing because the matrix formula is polynomial. The two small-prime gcds are correct worked instances, not a distinct uniform intersection result. This is demonstrated prior coverage of the principal finding, not a verdict based on unavailable sources.

## value

FAIL

The family and its geometric p-rank are mathematically natural, but the central result is an index specialization of a known explicit matrix followed by direct orbit counting and standard Legendre facts. Its two low-degree gcd examples illustrate how an overlap changes rank but do not establish a new intersection criterion, boundary or independently motivated exact gap. The correct specialization and examples are useful exposition, not a separate research finding here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
