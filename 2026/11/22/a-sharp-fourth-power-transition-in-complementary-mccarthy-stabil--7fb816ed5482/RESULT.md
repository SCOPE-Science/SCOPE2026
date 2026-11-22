# A sharp fourth-power transition in complementary McCarthy stability for projection pairs

## Finding
Let \(P,Q\) be arbitrary finite-rank orthogonal projections on a complex Hilbert space, and let \(3\le p\le5\). Define the complementary trace deficit
\[
\mathcal D_p(P,Q)=\operatorname{Tr}(P+Q)^p-\operatorname{Tr}P-\operatorname{Tr}Q-(2^p-2)\operatorname{Tr}(PQP)^{p/2}.
\]
Define
\[
 a_p=\frac{p(p-1)}2,\qquad b_p=\frac{p(2^{p-1}-2)}4.
\]
The following **two-sided inequality has both globally optimal constants**:
\[
\boxed{\min\{a_p,b_p\}\,\|PQ-QP\|_2^2\ \le\ \mathcal D_p(P,Q)\ \le\ \max\{a_p,b_p\}\,\|PQ-QP\|_2^2.}
\]
Here \(a_p>b_p\) for \(3\le p<4\), \(a_4=b_4=6\), and \(a_p<b_p\) for \(4<p\le5\). Thus the sharp lower- and upper-bound extremizing principal angles reverse at the **fourth-power transition**. For \(p<4\), the deficit-to-commutator-energy ratio decreases strictly with the cosine of a nontrivial principal angle; for \(p>4\), it increases strictly. Every ratio strictly between the sharp endpoints occurs for a pair of two-dimensional rank-one projections. If \(p\ne4\), either inequality is strict whenever \([P,Q]\ne0\). At \(p=4\), the known exact identity \(\mathcal D_4(P,Q)=6\|[P,Q]\|_2^2\) is recovered, but is **not claimed as new**.

## Assumptions and scope
All projections are orthogonal (self-adjoint idempotents), of arbitrary finite ranks, on the same complex Hilbert space. The trace is the ordinary, unnormalized trace; \(\|\cdot\|_2\) is the Schatten Hilbert–Schmidt norm. For \(p\) real in the closed interval \([3,5]\), powers of positive operators use continuous functional calculus. No invertibility, equal rank or commutation is assumed. Finite rank guarantees all traces exist. No assertion for general positive non-projection operators at nonquartic exponents or for exponents outside \([3,5]\) is made.

## Proof
**1. Two-projection reduction.** The standard principal-angle decomposition of two finite-rank orthogonal projections splits their joint finite-dimensional support into common, orthogonal and two-dimensional generic blocks. Common and orthogonal one-dimensional blocks contribute zero to \(\mathcal D_p\) and to the squared commutator norm. On a generic block choose
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad Q=\begin{pmatrix}t^2&t\sqrt{1-t^2}\\t\sqrt{1-t^2}&1-t^2\end{pmatrix},\quad0<t<1.
\]
Then \(P+Q\) has eigenvalues \(1+t\) and \(1-t\), \(PQP\) has nonzero eigenvalue \(t^2\), and direct multiplication yields \(\|[P,Q]\|_2^2=2t^2(1-t^2)\). Consequently the blockwise deficit is exactly
\[
\phi_p(t)=(1+t)^p+(1-t)^p-2-(2^p-2)t^p.
\]
Both global quantities are sums of these blockwise quantities. The desired sharp constants therefore are precisely the infimum and supremum of
\[
R_p(t)=\frac{\phi_p(t)}{2t^2(1-t^2)},\qquad0<t<1.
\]

**2. Convexity changes sign at four.** Put \(x=t^2\) and
\[
f_p(x)=\frac{(1+\sqrt x)^p+(1-\sqrt x)^p-2}{x}-(2^p-2)x^{(p-2)/2}.
\]
Thus \(f_p(1)=0\) and \(R_p(t)=f_p(x)/(2(1-x))\). For \(0<x<1\), the ordinary binomial expansion gives
\[
f_p(x)=p(p-1)+2\sum_{k\ge2}\binom p{2k}x^{k-1}-(2^p-2)x^{(p-2)/2}.
\]
The series and its first two derivatives converge locally uniformly on \((0,1)\). If \(3<p<4\), all \(\binom p{2k}\) for \(k\ge2\) are positive: for \(k\ge3\), the negative factors occur in even number \(2k-4\). Moreover \((p-2)/2<1\), so the negative power term is strictly convex. Hence \(f_p\) is strictly convex. The same conclusion holds at \(p=3\) because \(f_3(x)=6-6\sqrt x\). If \(4<p<5\), all \(\binom p{2k}\) for \(k\ge3\) are negative (there are \(2k-5\) negative factors), and the \(k=2\) term is linear. Since \((p-2)/2>1\), the negative power term is strictly concave, so \(f_p\) is strictly concave. At \(p=5\), \(f_5(x)=20+10x-30x^{3/2}\) is strictly concave. Finally \(f_4(x)=12(1-x)\) is linear.

For a convex function with \(f(1)=0\), the right-anchored secant quotient \(f(x)/(1-x)\) is decreasing in \(x<1\); for a concave function it is increasing. Strict curvature gives strict monotonicity here. Thus \(R_p(t)\) is strictly decreasing for \(3\le p<4\), strictly increasing for \(4<p\le5\), and identically \(6\) for \(p=4\).

**3. Exact boundary constants and sharpness.** The binomial leading term shows \(f_p(0+)=p(p-1)\), giving
\[
\lim_{t\downarrow0}R_p(t)=\frac{p(p-1)}2=a_p.
\]
By direct differentiation at \(x=1\),
\[
-f_p'(1)=\frac{p(2^{p-1}-2)}2,
\qquad\lim_{t\uparrow1}R_p(t)=-\frac{f_p'(1)}2=b_p.
\]
These formulas remain valid at the integer endpoints. The convexity/concavity result makes the two limits the exact infimum and supremum in their asserted order. To witness sharpness, take the displayed two-by-two projections with \(t\downarrow0\) and with \(t\uparrow1\); no fixed positive commutator energy is required to attain the **best universal constants**. Every finite-dimensional pair obeys the bounds by summing the block inequalities, and two-dimensional witnesses exclude any improvement. Strictness for noncommuting pairs and the exact quartic identity follow from the same ratio argument. This completes the proof.

## Verification
The standalone `verify_projection_p_bounds.py` tests 300 two-dimensional pairs at the integer exponents \(3,4,5\) with exact rational matrix multiplication, traces, commutator energies, and endpoint bounds. It also tests 20,000 scalar noninteger cases on both sides of the fourth-power transition, yielding `PROJECTION_MCCARTHY_DIAGNOSTIC_OK 20300`. The infinite family of exponents and arbitrary ranks is established by the algebraic sign proof and the principal-angle reduction, **not** by finite sampling. Reproduce by running `python3 verify_projection_p_bounds.py` beside this document.

## Relationship to prior work
Teng Zhang, *Clarkson–McCarthy type inequalities, part II* (arXiv:2611.00459v1, first public 30 October 2026), Theorem 1.2 proves \(\mathcal D_p(A,B)\ge0\) for general positive matrices and \(p\ge2\). Its Lemma 3.3 introduces the same scalar deficit \(\phi_p\) and proves nonnegativity, but does not give the **sharp comparison with squared commutator energy** or its reversal across \(p=4\). These results are fully credited.

The published finding *A sharp commutator remainder in the quartic complementary McCarthy inequality* supplies the stronger exact positive-square identity at \(p=4\) for general positive Schatten-four operators. Accordingly the quartic specialization here is old; the stated contribution is the **noninteger-exponent two-sided sharp constants and angle-monotonicity transition** for projection pairs across \([3,5]\). The principal-angle decomposition is standard, as are its block spectra; neither is claimed as new. Older scalar trace inequalities or a differently indexed sharp two-projection stability theorem could potentially subsume the nonquartic portion; no claim of exhaustive bibliographic priority is made.

## Limitations
The result concerns finite-rank orthogonal projections, not arbitrary positive matrices, and exponents between three and five only. It is a dimension-independent trace inequality, not an operator-order estimate. The best constants at nonquartic exponents are limits as projection angles degenerate and are not attained by noncommuting pairs; the zero-commutator equality cases are trivial. The work has passed only self-review, not independent refereeing or certification. Bibliographic completeness remains subject to independent scrutiny.

## References
1. T. Zhang, *Clarkson–McCarthy type inequalities, part II: refinements, unitary orbits, unitarily invariant norms and ell_s–ell_s estimates*, arXiv:2611.00459v1, 2026-10-30, Theorem 1.2 and Lemma 3.3. https://arxiv.org/html/2611.00459v1
2. *A sharp commutator remainder in the quartic complementary McCarthy inequality*, publicly available research result, 2026-11-17, especially its RESULT.md and exact quartic identity. https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-a-sharp-commutator-remainder-in-the-quartic-complementary-mccart--f1af3da8a762/RESULT.md
3. K. M. R. Audenaert, *Trace inequalities for completely monotone functions and Bernstein functions*, Linear Algebra and its Applications 437 (2012), 601–611. https://arxiv.org/abs/1109.3057
4. P. R. Halmos, *Two subspaces*, Transactions of the American Mathematical Society 144 (1969), 381–389 (classical two-projection decomposition).
