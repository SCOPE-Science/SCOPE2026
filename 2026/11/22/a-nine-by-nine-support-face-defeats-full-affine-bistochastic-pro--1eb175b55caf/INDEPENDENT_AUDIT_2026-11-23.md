# Independent mathematical audit

## correctness

PASS

The full affine derivative is double centering, so each coefficient-row absolute sum is (2-2/9)^2=256/81. The seven permutations cover exactly the 38 entries, and their mean is bistochastic and positive on that support. A fresh exact recomputation gives rank 17 and det(BBᵀ)=810332352, so the displayed grounded-incidence formula is the orthogonal projection onto supported perturbations with all row and column sums zero (the omitted column sum is redundant). The (4,8) row has ℓ¹ norm 13394263/4220481, with excess 1497389/113952987. Using its sign as the direction makes the input denominator exactly the stated epsilon. At the second candidate the minimum supported entry is 703408248411/4923894500000 and the minimum off-support dual slack is 4220474028301/4220481000000, both positive. The residual is a row/column potential plus a nonpositive term supported off the face, so its inner product with any feasible displacement is nonpositive; the same argument with zero equality potential proves the first projection. The (4,8) quotient proves the lower bound without a global sharpness or minimum-order claim.

## originality

PASS

The supported-projector method and the existence of strict obstructions at higher dimension are known. The evidence supports only the new explicit order-nine strict comparison, on a best-of-knowledge basis.

## value

PASS

The meaningful improvement is in the dimension of an explicit counterexample to the affine stability heuristic, not in the numerical size of the gap. The finite pair shows that the obstruction is a reachable effect of a proper support and provides a benchmark for work locating the first failure or estimating the sharp endpoint modulus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
