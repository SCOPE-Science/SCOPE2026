# Review

## Scientific claim reviewed

For a degree-\(N\) polynomial with collinear zeros of diameter \(D>0\), and for any zero \(a\),
\[
\sum_{\zeta:p'(\zeta)=0}|a-\zeta|^{-\lambda}
\ge (N-1)(2/D)^\lambda,\qquad \lambda\ge1,
\]
with the equality cases stated in `RESULT.md`. A stronger sign-sensitive estimate is also claimed at exponent \(1\).

## Correctness

**PASS.**

The reciprocal critical points are represented, via an exact characteristic-polynomial identity that remains valid with repeated zeros, as the eigenvalues of
\[
D_0(I+J)=D_0+D_0J,
\]
where \(D_0\) is the real diagonal matrix of reciprocals of the non-distinguished zeros after translation and rotation. This matrix is similar to
\[
(I+J)^{1/2}D_0(I+J)^{1/2},
\]
which is real symmetric and has the same inertia as \(D_0\).

The key estimate is a Ky Fan compression onto the image of the positive-coordinate subspace under \((I+J)^{-1/2}\). The restricted Gram matrix is
\[
I_r-\frac1{m+1}J_r,
\]
whose inverse is
\[
I_r+\frac1{\ell+1}J_r.
\]
This yields
\[
P_+\ge\frac{\ell+2}{\ell+1}R.
\]
The negative-side calculation is symmetric:
\[
P_-\ge\frac{r+2}{r+1}L.
\]
Combining these with
\[
P_+-P_-=2(R-L)
\]
gives both displayed lower bounds in `RESULT.md`.

The passage to the diameter bound is valid in all sign cases. If zeros occur on both sides of the distinguished zero, the two principal terms \(2L\) and \(2R\), together with \(x+y=D\), force a strict bound. If all zeros are on one side, the trace identity becomes exact and the diameter estimate reduces to the elementary bound on reciprocal distances. The power-mean step correctly propagates the endpoint \(\lambda=1\) result to every \(\lambda>1\).

The equality classification was checked algebraically. For exponent \(1\), the only finite equality configuration has the distinguished zero at one endpoint and every other zero at the opposite endpoint. For \(\lambda>1\), the power-mean equality condition eliminates this configuration except in degree two.

## Originality

**PASS, to the best of our knowledge.**

The closest primary source is Tang--Zhang, arXiv:2508.10341v3. Its Conjecture 1.10 asks for the reciprocal lower bound for all \(\lambda\ge1\). The paper was inspected in full. It proves sharp negative-order Schoenberg *upper* bounds, including
\[
\sum |w_k|^{-1}\le 2\sum |z_j|^{-1},
\]
and develops the reciprocal companion-matrix representation, but it does not state the collinear lower bound, the sign-sensitive two-sided estimate, or the sharp diameter theorem proved here.

Zhang, arXiv:2609.19126, proves the quadratic reciprocal lower bound globally in the unit disk, with exponent \(2\). That result does not imply exponent \(1\); the implication runs in the other direction by power means. The present result therefore addresses the stronger endpoint, but only for collinear zeros.

Searches were run for exact and synonymous formulations involving real-rooted/collinear zeros, reciprocal critical points, root diameter, Tang--Zhang inequalities, and reciprocal-distance sums. No prior statement matching the theorem was found. The current SCOPE repository was also searched by the relevant objects, source papers, and terminology, with no overlapping record found.

Residual literature risk remains. Pereira (2003) is foundational for majorization of critical points by zeros; its full text was not inspected in this review, although its abstract and the detailed discussion in Tang--Zhang were inspected. Only the abstract and secondary descriptions of Zhang's arXiv:2411.07105 / forthcoming Proc. AMS paper were inspected; those descriptions mention an additional relation when certain zeros are nonnegative, which is relevant to the one-sided case. Cheung--Ng (2006) is prior art for the companion-matrix machinery. None of the accessible statements establishes the mixed-sign Ky Fan lower bound or the diameter theorem, but an older equivalent formulation cannot be ruled out completely.

## Value

**PASS.**

The result resolves the full Tang--Zhang conjecture for the natural collinear-zero class, including the difficult exponent-one endpoint, and it does so with a sharp scale-invariant diameter theorem and complete equality classification. The intermediate two-sided estimate contains additional information about how zeros on the two sides of the distinguished zero force reciprocal critical-point mass. This is more than a numerical special case or parameter increment.

## Review status

Same-model review: passed. Independent audit: not yet performed.

This is not independent validation, formal verification, journal peer review, or a guarantee of first discovery.
