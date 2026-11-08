# Sharp mixed fourth moments and Euclidean geometry of the first two symmetric Krawtchouk levels

## Finding
Let \(n\ge2\) be an integer and let \(\varepsilon_1,\ldots,\varepsilon_n\) be independent uniform signs. Define the first two symmetric Krawtchouk modes
\[
S=\sum_{i=1}^n\varepsilon_i,\qquad Q=\sum_{1\le i<j\le n}\varepsilon_i\varepsilon_j=\frac{S^2-n}{2},
\]
and \(\mathcal X_n=\operatorname{span}_{\mathbb R}\{S,Q\}\) with its inherited probability \(L^4\)-norm. For every nonzero \(f=aS+bQ\), the attained fourth-moment quotient \(K_n(f)=\mathbb E f^4/(\mathbb E f^2)^2\) has exact range \([L_n,M_n]\), where
\[
M_n=\frac{15n^2-33n+20}{n(n+1)},\qquad L_n=\begin{cases}1,&n=2,\\7/3,&n=3,\\3-2/n,&n\ge4.\end{cases}
\]
Every maximizer is a nonzero real multiple of \(S+Q\) or \(S-Q\), with **equal raw Krawtchouk coefficients in all dimensions**. The minimizing rays are \(Q\) only when \(n=2\), both \(S\) and \(Q\) when \(n=3\), and \(S\) only when \(n\ge4\). All intermediate ratios occur.

Writing \(U=S/\sqrt n\), \(V=Q/\sqrt{n(n-1)/2}\), and \(f=uU+vV\), put \(r=v^2/(u^2+v^2)\). The sharp deficit identity is
\[
M_n-K_n(f)=\frac{2(n+1)(6n-11)}{n(n-1)}\left(r-\frac{n-1}{n+1}\right)^2.
\]
In particular, near equality forces the relative energy in the second level to be near the unique maximizing energy split.

Let
\[
\beta_n=\frac{3(5n-8)\sqrt{n-1}}{\sqrt{(3n-2)(15n^2-63n+68)}}.
\]
The exact multiplicative Banach--Mazur distance to the Euclidean plane is
\[
\boxed{d_{\mathrm{BM}}(\mathcal X_n,\ell_2^2)^4=\frac{1+\beta_n}{2}.}
\]
This distance is strictly decreasing for integer \(n\ge3\), attains its unique all-dimension maximum \(2^{1/4}\) at \(n=3\), and satisfies the exact golden-ratio limit
\[
\lim_{n\to\infty}d_{\mathrm{BM}}(\mathcal X_n,\ell_2^2)^4=\frac{1+\sqrt5}{2}.
\]

## Assumptions and scope
All signs are independent and fair, expectations use probability normalization, the coefficient field is real, and \(n\) ranges over *all* integers at least two. The space excludes the constant mode and comprises only the two permutation-invariant Walsh levels of degrees one and two. The Banach--Mazur distance is \(\inf_T\|T\|\|T^{-1}\|\), where \(T\) runs over real linear isomorphisms to \(\ell_2^2\). No other chaotic levels or coefficient functions are allowed.

## Proof
**Moments.** Orthogonality of distinct Walsh characters gives \(\mathbb ES=\mathbb EQ=\mathbb ESQ=0\), \(\mathbb ES^2=n\), and \(\mathbb EQ^2=n(n-1)/2\). The moment-generating function of \(S\) is \((\cosh t)^n\). Extracting the coefficients through order eight gives
\[
\begin{aligned}
\mathbb ES^4&=3n^2-2n,\\
\mathbb ES^6&=15n^3-30n^2+16n,\\
\mathbb ES^8&=105n^4-420n^3+588n^2-272n.
\end{aligned}
\]
Consequently, using \(Q=(S^2-n)/2\), the normalized moments are
\[
A_n=\mathbb EU^4=\frac{3n-2}{n},\quad C_n=\mathbb EU^2V^2=\frac{5n-8}{n},\quad D_n=\mathbb EV^4=\frac{15n^2-63n+68}{n(n-1)}.
\]
All mixed terms with odd powers of \(U\) vanish under simultaneous sign reversal \(\varepsilon_i\mapsto-\varepsilon_i\). Thus, *for every real* \(u,v\),
\[
\mathbb E(uU+vV)^4=A_nu^4+6C_nu^2v^2+D_nv^4,\qquad \mathbb E(uU+vV)^2=u^2+v^2.
\]

**Sharp moment interval and rigidity.** For nonzero \(f\) put \(r=v^2/(u^2+v^2)\in[0,1]\). Then
\[
K_n(f)=A_n(1-r)^2+6C_nr(1-r)+D_nr^2.
\]
A direct expansion yields
\[
A_n-6C_n+D_n=-\frac{2(n+1)(6n-11)}{n(n-1)}<0,
\]
and its vertex is \(r_*=(n-1)/(n+1)\in(0,1)\). Substitution gives the claimed \(M_n\) and exact deficit. The unique energy split \(r=r_*\) is equivalent to \(v^2/u^2=(n-1)/2\), hence to \(b^2/a^2=1\) in the raw \(S,Q\) coordinates. Both signs are allowed, giving all maximizers. Since the quadratic is strictly concave, its minimum lies at an endpoint. Explicitly,
\[
D_n-A_n=\frac{2(n-3)(6n-11)}{n(n-1)},
\]
which gives all three cases and equality rays asserted for \(L_n\). Every quotient between the endpoints occurs because projective coefficient space is connected and the quotient continuous.

**Optimal Euclidean comparison.** With \(x=A_n^{1/4}u\), \(y=D_n^{1/4}v\), the norm becomes
\[
N_n(x,y)^4=x^4+2\beta_n x^2y^2+y^4,
\qquad \beta_n=3C_n/\sqrt{A_nD_n}.
\]
Both \(A_n,D_n\) are positive. The identities
\[
9C_n^2-A_nD_n=\frac{2(6n-11)(15n^2-33n+20)}{n^2(n-1)}>0,
\]
and \(\beta_n\le3\) (equality only at \(n=3\)) place \(\beta_n\) in \((1,3]\). The latter assertion also follows from the monotonicity calculation below and the direct value \(\beta_2=3/\sqrt2\).

For any positive-definite quadratic form \(q\) in \((x,y)\), suppose \(mN_n^2\le q\le MN_n^2\) pointwise. Average \(q\) over independent sign changes and coordinate interchange, all isometries of \(N_n\). The averaged form satisfies the same inequalities and has the form \(c(x^2+y^2)\). Therefore no Euclidean pullback improves the distortion of the standard quadratic form. On \(x^2+y^2=1\),
\[
N_n(x,y)^4=1+2(\beta_n-1)x^2y^2,
\]
whose range is \([1,(1+\beta_n)/2]\) because \(0\le x^2y^2\le1/4\). This proves the exact distance formula for every \(n\ge2\). The optimal elliptic form in raw coefficients has squared norm proportional to \(\sqrt{A_n}\,n a^2+\sqrt{D_n}\,[n(n-1)/2]b^2\); it generally differs from the original \(L^2\) form.

Finally, the derivative of \(\beta_t^2=9(t-1)(5t-8)^2/[(3t-2)(15t^2-63t+68)]\), treated as a function of real \(t\ge3\), is
\[
-\frac{54(5t-8)(25t^3-78t^2+31t+32)}{(3t-2)^2(15t^2-63t+68)^2}<0.
\]
The cubic factor is positive at \(t=3\) (value \(98\)), with positive first derivative there (value \(238\)) and positive second derivative for \(t\ge3\). Thus \(\beta_n\) strictly decreases for \(n\ge3\); \(\beta_3=3>\beta_2\), proving the unique maximum. Taking leading coefficients gives \(\beta_n\to\sqrt5\), hence the golden-ratio limit.

## Verification
Run `python3 verify.py` from this directory. The dependency-free exact-rational checker recomputes Walsh moments directly from binomial sums for dimensions two through fourteen, verifies the quartic coefficients, the deficit identity, the exact raw-coefficient extremizers, and rational comparisons of the elliptic parameters. The script ends with `ALL_RADIAL_KRAWTCHOUK_CHECKS_PASSED`. These *finite tests* corroborate the symbolic identities; the dimension-uniform assertions follow from the displayed moment-generating-function expansion, algebraic identities, and group-averaging proof.

## Relationship to prior work
Classical Krawtchouk orthogonality and general Walsh hypercontractivity motivate this exact two-mode problem. Diaconis and Griffiths (2012) develop Krawtchouk polynomials in a bivariate-binomial/eigenfunction setting; Blais and Tan (2013) prove general Walsh-chaos hypercontractivity. Kirshner and Samorodnitsky (2019) give degree-dependent moment bounds and near-extremality properties for homogeneous Krawtchouk polynomials, not the sharp *mixture* of the first two levels. A published sharp fourth-moment theorem for the complete *homogeneous quadratic* Walsh chaos already provides the coefficient \(D_n\) in dimensions at least six but does not identify the strict mixed improvement \(M_n>D_n\). Separately, the exact Banach--Mazur formula for the general symmetric quartic norm \((x^4+2\beta x^2y^2+y^4)^{1/4}\) is previously established: the geometric averaging argument and quartic-to-Euclidean reduction are **not claimed as new**. The present exact result is the all-\(n\) Krawtchouk mixture, its equality and stability identities, and the resulting dimension-specific distance law. No proof of priority against every unindexed Krawtchouk linearization formula is asserted.

## Limitations
The result concerns exactly the real, uniform-sign two-mode radial Walsh space and fourth moments. It does not provide the unrestricted sharp norm for all degree-at-most-two Walsh polynomials, higher moments, biased Bernoulli product measures, or arbitrary Krawtchouk mode pairs. Generic product-linearization formulas might make some moment identities derivable without displaying the sharp extremizers. The 2012 Diaconis--Griffiths full article was not accessible during comparison, so an implicit related calculation there remains a residual bibliographic risk. No independent mathematical audit is represented.

## References
1. P. Diaconis and R. Griffiths, “Exchangeable pairs of Bernoulli random variables, Krawtchouck polynomials, and Ehrenfest urns,” *Australian & New Zealand Journal of Statistics* 54 (2012), 81–101, DOI `10.1111/j.1467-842X.2012.00654.x`; verified first online 2012-05-04. Full text unavailable during comparison.
2. E. Blais and L.-Y. Tan, “Hypercontractivity Via the Entropy Method,” *Theory of Computing* 9 (2013), 889–896, DOI `10.4086/toc.2013.v009a029`, full paper `https://theoryofcomputing.org/articles/v009a029/v009a029.pdf`.
3. N. Kirshner and A. Samorodnitsky, “A moment ratio bound for polynomials and some extremal properties of Krawchouk polynomials and Hamming spheres,” arXiv `1909.11929v1` (2019-09-26), `https://arxiv.org/pdf/1909.11929`.
4. “Sharp fourth moments and Euclidean distortion of complete quadratic Walsh chaoses,” published mathematical result, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-and-euclidean-distortion-of-complete-quadra--5d09daee1c04` (published 2026-10-11).
5. “Exact Euclidean Banach--Mazur profile of the quartic polynomial-index-zero plane family,” published mathematical result, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-euclidean-banach-mazur-profile-of-the-quartic-polynomial-i--584a28f6199f` (published 2026-10-04).
