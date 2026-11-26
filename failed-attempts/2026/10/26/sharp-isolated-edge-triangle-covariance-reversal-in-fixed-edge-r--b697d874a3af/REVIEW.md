# Independent mathematical audit

## correctness

PASS

Conditional on one isolated pair, the remaining graph is exactly G(n−2,m−1); triangles meeting the pair are impossible. Dividing the resulting conditional triangle mean by the unconditional mean gives K_n(m−3)/m, with K_n equal to the stated rational expression. Multiplying its excess over one by the two means gives the covariance, including m=3, where the conditional mean is zero. Where both means are positive, the sign is the sign of m−τ_n. Substitution of n/2 and n/2+1 for even n, or (n+1)/2 and (n+3)/2 for odd n, gives strict bounds on the root with the signs stated in the proof. Below m=3 triangles are absent, and above M+1 isolated edges are absent; these ranges also account for vanishing covariance below n=5. At n=5 the two active cases give −1/48 and 2/63. In G(n,p) disjoint indicators are independent and each of the (n−2)^2 intersecting triangles contributes the negative product of the two probabilities per possible isolated edge. In the sparse regime the logarithm of the absence product tends to −2c, so E[S]/n→(c/2)e^(−2c), while E[T]→c³/6 and n times the factor in parentheses tends to 6(1−1/c). This also gives zero at c=1 without asserting an eventually constant sign there. The finite checker was inspected, not run, and is not the basis for the all-integer or asymptotic claims.

## originality

FAIL

A distinct Resultary record explicitly covers the same exact covariance factorization, strict finite sign classification, independent-edge contrast and sparse covariance constant. Its threshold ceil(n/2)+1 is exactly floor((n+3)/2). Its displayed sparse statement uses m=floor(cn/2), but the unrestricted sequence version follows directly from its exact factorization by the same elementary hypergeometric limit and does not supply an independently distinct result. This is a coverage finding against an inspected separate record, not a determination of who discovered the result first, an inference from catalogue dates, or a claim of copying.

## value

PASS

The covariance between two natural but structurally different observables is a meaningful test of fixed-edge conditioning. A sharp nondegenerate finite sign classification with an independent-edge contrast and a mean-degree-one limit is scientifically useful as a statement, even though this record does not add a distinct result to the indexed finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
