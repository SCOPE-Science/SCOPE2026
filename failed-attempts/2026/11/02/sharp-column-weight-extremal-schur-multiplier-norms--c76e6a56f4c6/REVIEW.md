# Independent mathematical audit

## correctness

PASS

Writing c=a+bk/v, the centered symbol b(B−(k/v)J) has a Schur factorization with row-factor length sqrt((v−1)/v) and column-factor length |b| sqrt(k(v−k)/v). The tensor-diagonal implementation gives their product as an operator-norm bound; adding the constant symbol contributes |c|. This covers c=0 and b=0 directly. The dual test with the conjugate polar partial isometry and normalized constant vectors gives the rectangular nuclear lower bound. In a complete incidence system, or a nontrivial 2-design, the replication and intersection counts give BB*= (r−λ)I+λJ, with r−λ=nk(v−k)/(v(v−1)). Centering splits the constant and orthogonal directions, so the singular values are sqrt(vn)|c| and |b|sqrt(r−λ) with multiplicity v−1, attaining the uniform bound in a finite width. The complete singleton design covers k=1. Over the reals the factors and witnesses are real when a,b are real. For balanced signs the Frobenius upper bound forces n≥v−1; deleting the constant column of a normalized real Hadamard gives balanced orthogonal columns and attains the minimum when such a matrix exists, not at every even v by assertion. Substitution and expansion give the two specializations and the fixed-k sparse limit. Independently checked 105 constant-vector polar witnesses, including genuinely complex coefficients and zero components (python /workspace/branches/independent_math_checks.py, section 1). These checks are finite, and the supplied verifier was inspected, not run.

## originality

FAIL

The explicit universal maximum is a direct corollary of the pre-existing Mathias exact Schur norm theorem, not just an application of a generic upper bound. The complete incidence pencil has transitive symmetries on both index sets and every allowed symbol is a submatrix of its sufficiently repeated replication. Squaring by replication lets the square Mathias theorem evaluate the sharp bound without the frozen record's centered inequality. Its polar witness is the same trace lower bound that attains it on the complete pencil. This is verified implication of the central claim, not a title match or a claim that the prior paper prints the same formula.

## value

FAIL

The prespecified weight constraint is natural and the formula is useful, but the underlying exact optimization is already determined by the classical flat-polar norm theorem and the direct complete-incidence compression. The incidence spectrum, sign asymptotic, and width consequence are routine once that reduction is made. The frozen record does not identify an additional new equality classification or fixed-width extremum that would constitute a distinct valuable result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
