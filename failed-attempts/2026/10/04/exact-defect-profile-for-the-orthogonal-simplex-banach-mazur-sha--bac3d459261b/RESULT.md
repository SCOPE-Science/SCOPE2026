# Exact defect profile for the orthogonal-simplex Banach--Mazur sharpness family
## Finding
For integers \(n\ge 2\) and \(1\le s\le n\), consider the orthogonal-simplex family from Remark 4.5 of Brandenberg--González Merino--Grundbacher: write \(q=\lfloor n/s\rfloor\), \(r=n-qs\), and form the convex hull of \(q\) regular \(s\)-simplices in pairwise orthogonal \(s\)-dimensional subspaces together with one regular \(r\)-simplex in the remaining orthogonal subspace when \(r>0\). Let \(K_{n,s}\) denote this body and put
\[
E(n,s)=\frac{d_{BM}(K_{n,s},B_2^n)}{\sqrt{ns}}.
\]
Set \(\alpha=\sqrt2-1\) and \(C=\sqrt{2(\sqrt2-1)}\). If \(x=r/s\), then the source's exact distance formula admits the exact defect decomposition
\[
E(n,s)^2
=C^2+\frac{(x-\alpha)^2+(q-1)\alpha^2}{q+x}.
\]
Consequently \(C\) is the exact best uniform lower factor for this construction:
\[
\inf_{n\ge2,\,1\le s\le n}E(n,s)=C=0.9101797211244548\ldots,
\]
and the infimum is not attained. Moreover, a sequence from this family satisfies \(E(n_j,s_j)\to C\) if and only if eventually \(\lfloor n_j/s_j\rfloor=1\) and \((n_j-s_j)/s_j\to\sqrt2-1\).

The continued-fraction convergents \(r/s\) of \(\sqrt2-1=[0;2,2,2,\ldots]\), with \(n=s+r\), give explicit near-extremizers. Along them,
\[
0<E(n,s)^2-C^2=\frac{(r/s-\alpha)^2}{1+r/s}<\frac1{s^4}.
\]
Thus the universal factor displayed in the source is not merely a convenient estimate for its canonical sharpness family: it is the exact infimum, and the decomposition identifies the complete asymptotic parameter regime that approaches it.

## Assumptions and scope
The statement concerns only the orthogonal-simplex construction in Remark 4.5 of arXiv:2607.27041v2. The Banach--Mazur distance is the usual affine Banach--Mazur distance between convex bodies, and \(B_2^n\) is the Euclidean unit ball. The source proves that the constructed body has Minkowski asymmetry \(s\) and gives its exact Banach--Mazur distance to \(B_2^n\).

No assertion is made that \(C\) is the best possible universal constant among all convex bodies with prescribed Minkowski asymmetry, nor that the source's upper estimate \(d_{BM}(K,B_2^n)\le\sqrt{n\,s(K)}\) has this exact deficit for arbitrary bodies. The finding optimizes and stabilizes the specific family used by the source to demonstrate near-sharpness when divisibility fails.

## Proof
The source gives, for the family above,
\[
d_{BM}(K_{n,s},B_2^n)^2
=ns-\bigl(n-s\lfloor n/s\rfloor\bigr)\bigl(s\lceil n/s\rceil-n\bigr).
\]
With \(q=\lfloor n/s\rfloor\) and \(r=n-qs\), the second product is \(r(s-r)\), including the divisible case \(r=0\). Since \(x=r/s\) and \(n=s(q+x)\), normalization gives
\[
E(n,s)^2=1-\frac{x(1-x)}{q+x}.
\]
Now \(\alpha=\sqrt2-1\) satisfies \(\alpha^2=1-2\alpha\), while \(C^2=2\alpha\). Therefore
\[
\begin{aligned}
E(n,s)^2-C^2
&=\frac{(q+x)(1-2\alpha)-x(1-x)}{q+x}\\
&=\frac{(q+x)\alpha^2-x+x^2}{q+x}\\
&=\frac{(x-\alpha)^2+(q-1)\alpha^2}{q+x}.
\end{aligned}
\]
This proves the decomposition and \(E(n,s)>C\) for every finite pair: equality would require simultaneously \(q=1\) and \(x=\alpha\), but \(x=r/s\) is rational whereas \(\alpha\) is irrational.

To see that \(C\) is nevertheless the infimum, take rational convergents \(r/s\) of \(\alpha=[0;2,2,2,\ldots]\), for example \(1/2,2/5,5/12,12/29,\ldots\), and set \(n=s+r\). Then \(q=1\), and the standard convergent estimate \(|r/s-\alpha|<1/s^2\) gives
\[
0<E(n,s)^2-C^2=\frac{(r/s-\alpha)^2}{1+r/s}<\frac1{s^4}.
\]
Hence \(E(n,s)\to C\).

For the asymptotic characterization, suppose \(E(n_j,s_j)^2-C^2\to0\). If \(q_j\ge2\), then because \(0\le x_j<1\),
\[
\frac{(q_j-1)\alpha^2}{q_j+x_j}\ge\frac{\alpha^2}{3},
\]
a contradiction for all sufficiently large \(j\). Thus eventually \(q_j=1\); the decomposition then reduces to
\[
E(n_j,s_j)^2-C^2=\frac{(x_j-\alpha)^2}{1+x_j},
\]
which tends to zero exactly when \(x_j\to\alpha\). The converse is immediate from the same formula.

## Verification
The algebraic identity was independently replayed from the accompanying `verify.py`. It symbolically verifies that
\[
1-\frac{x(1-x)}{q+x}-2\alpha
=\frac{(x-\alpha)^2+(q-1)\alpha^2}{q+x}
\]
under \(\alpha=\sqrt2-1\), checks the elementary lower gap for \(q\ge2\), and evaluates the first continued-fraction near-extremizers against the closed formula.

The proof itself is exact and does not rely on finite sampling. The numerical values printed by the script are illustrative checks only; the infinite statement follows from the symbolic identity and the standard continued-fraction estimate.

## Relationship to prior work
Brandenberg--González Merino--Grundbacher prove the upper estimate \(d_{BM}(K,B_2^n)\le\sqrt{n\,s(K)}\), show it is sharp when the integer asymmetry divides the dimension, and in Remark 4.5 give the orthogonal-simplex family above for nondivisibility. They derive the exact distance formula and observe the uniform lower estimate
\[
d_{BM}(K_{n,s},B_2^n)\ge \sqrt{2(\sqrt2-1)}\,\sqrt{ns}>0.91\sqrt{ns}.
\]
The inspected source does not identify that factor as the exact infimum of its construction, does not give the displayed sum-of-squares defect identity, and does not characterize all parameter sequences approaching the factor.

Grundbacher--Kobos establish exact Banach--Mazur distance formulas for \(\ell_p\)-sums and extend the relevant position argument to nonsymmetric convex bodies; this machinery underlies the source's exact block construction. It does not optimize the integer block split or supply the defect profile above.

Targeted searches for the exact constant, the orthogonal-simplex construction, the remainder product \(r(s-r)\), and equivalent normalized formulations found no published statement covering this optimization or stability characterization. The closest indexed results concerned unrelated Banach--Mazur stability problems and did not imply the claim.

## Limitations
The claim is deliberately restricted to the source's orthogonal-simplex family. It does not determine the optimal Banach--Mazur distance for every fixed pair \((n,s)\), and it does not prove that every globally near-sharp convex body must resemble this family. The originality comparison is necessarily bibliographic rather than a proof of uniqueness in the literature; an uncatalogued note could contain the same elementary optimization. The mathematical claim itself depends on the source's exact distance formula, which was inspected in the primary preprint and algebraically normalized here.

## References
1. René Brandenberg, Bernardo González Merino, and Matthias Grundbacher, *Tight Stability Estimates Near the Simplex and Applications for the Banach-Mazur Distance and Rogers-Shephard-Type Inequalities*, arXiv:2607.27041v2, first public version July 29, 2026. See Theorem 1.3 and Remark 4.5.
2. Matthias Grundbacher and Tomasz Kobos, *Exact Banach-Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268v1, March 18, 2026. See Theorem 1.1 and Remark 2.5.
