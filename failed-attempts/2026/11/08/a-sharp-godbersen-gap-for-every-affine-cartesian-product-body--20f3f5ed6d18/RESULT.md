# A sharp Godbersen gap for every affine Cartesian-product body

## Finding

Let \(n\geq2\), and let \(K\subset\mathbb R^n\) be any full-dimensional convex body that is an invertible affine image of a Cartesian product \(K_1\times\cdots\times K_r\), where \(r\geq2\), each \(K_i\) is a full-dimensional compact convex body in \(\mathbb R^{d_i}\), \(d_i\geq1\), and \(\sum_i d_i=n\). Write \(V_n\) for the symmetric mixed volume normalized by \(V_n(K[n])=\operatorname{vol}_n(K)\). Then, for each integer \(1\leq k\leq n-1\),

\[
\frac{1}{\binom nk}\ \leq\ 
\frac{V_n(K[n-k],(-K)[k])}{\binom nk\,\operatorname{vol}_n(K)}
\ \leq\ \frac{k^2+(n-k)^2}{n^2}
=1-\frac{2k(n-k)}{n^2}.
\]

The upper bound is **sharp in every dimension and for every index simultaneously**: equality in its complete coefficient profile is attained by any affine image of the prism \(I\times\Delta_{n-1}\), where \(I\) is a nondegenerate segment and \(\Delta_{n-1}\) is a nondegenerate simplex. Conversely, if the upper bound is attained for every \(1\leq k\leq n-1\) (indeed, just for \(k=1\)), the body must be an affine image of such a prism. The lower bound is attained simultaneously for all indices precisely when the body is centrally symmetric. For a central index, the upper normalized quotient is at most \(1/2\) in even dimension, and \(1/2+1/(2n^2)\) in odd dimension.

An equivalent coefficientwise form, valid for every real \(t\geq0\), is

\[
(1+t)^n\ \preceq\ \frac{\operatorname{vol}_n(K+t(-K))}{\operatorname{vol}_n(K)}
\ \preceq\ (1+t)\sum_{j=0}^{n-1}\binom{n-1}{j}^2t^j,
\]

where \(\preceq\) denotes coefficientwise comparison, not merely a pointwise comparison.

## Assumptions and scope

Bodies are compact, convex, with nonempty interior in their affine spans; the product decomposition has at least two positive-dimensional factors. All volume and mixed-volume ratios are invariant under invertible affine maps and translations, so a coordinate-product proof suffices. There is no smoothness, symmetry, lattice, or polytope assumption on the factors. The upper bound does not claim to hold for indecomposable bodies; a simplex saturates the larger Godbersen bound. The assertion about upper equality for the *complete profile* does not claim uniqueness for an arbitrary single interior coefficient; for example, in dimension four the midpoint coefficient also ties for the product of two triangles.

## Proof

**1. Factor-polynomial comparison.** For a full-dimensional body \(L\subset\mathbb R^d\), set
\[
T_L(t)=\frac{\operatorname{vol}_d(L+t(-L))}{\operatorname{vol}_d(L)}
=\sum_{j=0}^d\binom dj\frac{V_d(L[d-j],(-L)[j])}{\operatorname{vol}_d(L)}t^j.
\]
By the Alexandrov--Fenchel inequality, the positive mixed-volume sequence in this display is log-concave, while its two endpoint terms are both \(\operatorname{vol}_d(L)\). Hence every normalized mixed volume is at least one. The Godbersen inequality, proved for arbitrary convex bodies by Kotrbatý--Mouamine and with the general equality case established by Fryš--Kotrbatý--Mouamine--Wang, gives at most \(\binom dj\) for the same mixed-volume ratio. Thus
\[
(1+t)^d\preceq T_L(t)\preceq F_d(t),\qquad
F_d(t)=\sum_{j=0}^d\binom dj^2t^j.
\]
Both endpoints of these inequalities are sharp: centrally symmetric bodies give the left polynomial, and simplices give the right polynomial. Cartesian product volumes multiply, so \(T_K(t)=\prod_i T_{K_i}(t)\), up to the affine invariance already noted.

**2. The sharp upper polynomial.** For positive integers \(a,b\), Vandermonde's identity and nonnegativity yield
\[
F_a(t)F_b(t)\preceq F_{a+b}(t),
\]
since each coefficient of the former is a sum of squares of the individual Vandermonde summands, while the latter has the square of their sum. Repeatedly merging all but one factor gives \(\prod_iF_{d_i}\preceq F_aF_{n-a}\), with \(1\leq a\leq n-1\).

The **coefficientwise Hankel-total positivity theorem for type-B Narayana polynomials** (Li--Li--Yang--Zhang, Theorem 4.2, also proved earlier by Wang--Zhu and independently Sokal) says that every minor of \((F_{i+j}(t))_{i,j\geq0}\) has nonnegative coefficients. Its two-by-two minor with rows \(0,1\) and columns \(a-1,n-a\), for \(2\leq a\leq n/2\), gives
\[
F_{a-1}(t)F_{n-a+1}(t)-F_a(t)F_{n-a}(t)\succeq0.
\]
Interchanging the factors if necessary and iterating yields \(F_aF_{n-a}\preceq F_1F_{n-1}\). Hence
\[
T_K(t)\preceq F_1(t)F_{n-1}(t)=(1+t)F_{n-1}(t).
\]
Its coefficient of \(t^k\), for \(0\leq k\leq n\), is
\[
\binom{n-1}{k}^2+\binom{n-1}{k-1}^2
=\binom nk^2\frac{(n-k)^2+k^2}{n^2},
\]
with out-of-range binomial coefficients taken to be zero. Comparing this with the defining coefficient \(\binom nk V_n(K[n-k],(-K)[k])/\operatorname{vol}_n(K)\) proves the claimed upper bound. Multiplication of the factor lower bounds proves the lower bound.

**3. Sharpness and complete-profile rigidity.** For \(K=I\times\Delta_{n-1}\), the two factors attain \(T_I=F_1\), \(T_{\Delta_{n-1}}=F_{n-1}\), giving the upper polynomial exactly. For any product decomposition, the \(t\)-coefficient of \(T_K\) is a sum of its factor coefficients and is at most \(\sum_i d_i^2\). Among integer partitions into at least two positive parts, \(\sum_i d_i^2\leq1+(n-1)^2\), with equality only for the two-part partition \((1,n-1)\) up to order. Equality in the factor estimate for its positive-dimensional nonsegment factor forces that factor to be a simplex by the published Godbersen equality characterization. The converse has already been shown. The lower polynomial is realized by centrally symmetric bodies. Conversely, if all lower coefficient equalities hold, then at \(t=1\) one has \(\operatorname{vol}_n(K-K)=2^n\operatorname{vol}_n(K)\), whose equality condition in Brunn--Minkowski forces \(K\) to be centrally symmetric. The central-index numerical bounds follow by substituting the integer(s) nearest \(n/2\).

## Verification

A standalone exact-integer checker, `check.py`, expands the polynomial profiles for every ordered positive-dimensional factor decomposition in dimensions two through sixteen, comparing every coefficient to both sharp envelopes. It executed successfully with 1,048,469 exact comparisons, including explicit non-simplex factor-polynomial examples (triangle, square, trapezoid). The trapezoid example's volume and difference-body coefficient were also checked independently using integer polygon shoelace geometry. These finite tests do not prove a statement in all dimensions; the proof above rests on the published general Godbersen inequality and coefficientwise Hankel-total positivity theorem, plus elementary product and binomial identities.

## Relationship to prior work

The recent solution of Godbersen's inequality establishes \(V_n(K[n-k],(-K)[k])\leq\binom nk\operatorname{vol}_n(K)\) for arbitrary bodies and characterizes the simplex equality case. This does not provide a positive explicit coefficientwise deficit for all affinely product-decomposable bodies. The 2021 type-B Narayana Hankel-total positivity theorem proves a polynomial property without a Godbersen interpretation. The new result combines these independent results to give a sharp dimension-and-index-specific gap for the entire affine-product class, with simultaneous equality classification. Exact prism formulas give the boundary family but do not assert domination over products of two higher-dimensional factors. No general quantitative stability estimate for nearly decomposable bodies is asserted.

## Limitations

The result depends on two previously published, nontrivial theorems, rather than reproving them: the all-dimensional Godbersen inequality and coefficientwise Hankel-total positivity of type-B Narayana polynomials. No assertion is made for a body which is only approximately a product. Equality for a *single* noncentral mixed-volume index need not give the same rigidity statement as equality for the entire polynomial. An independent mathematical audit and exhaustive historical-priority verification have not been conducted.

## References

- J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers--Shephard inequality*, arXiv:2607.20387v1, publicly submitted July 22, 2026. https://arxiv.org/abs/2607.20387
- F. Fryš, J. Kotrbatý, M. A. Mouamine, S. Wang, *Higher-Order Godbersen Inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v1, publicly submitted October 5, 2026, especially Theorem 1.2. https://arxiv.org/html/2610.06806v2
- E. Y. H. Li, G. M. X. Li, A. L. B. Yang, C. X. T. Zhang, *A planar network proof for Hankel total positivity of type B Narayana polynomials*, arXiv:2107.10608v1 (July 22, 2021), especially Theorem 4.2. https://arxiv.org/abs/2107.10608
