# Sharp half-unit Fermat–Torricelli convex-hull gap and extremizer rigidity in real \(\ell_1^d\)

## Finding
For every integer \(d\ge3\) the largest distance of the Fermat–Torricelli median of \(\{0,x,y\}\) from the convex hull of the three sites, over unit vectors satisfying the one-sided Birkhoff–James relation \(x\perp_B y\), is exactly
\[
\sup_{\substack{\|x\|_1=\|y\|_1=1\\x\perp_B y}}
\operatorname{dist}_1\bigl(m(0,x,y),\operatorname{co}\{0,x,y\}\bigr)=\frac12.
\]
This upper bound holds for **all** pairs of unit vectors, even without the orthogonality constraint. More precisely, equality holds **if and only if**
\[
x=c+u,\qquad y=c+v,
\]
where \(c,u,v\in\mathbb R^d\) have pairwise disjoint coordinate supports and
\[
\|c\|_1=\|u\|_1=\|v\|_1=\frac12.
\]
Every equality pair is Birkhoff–James orthogonal in both directions. For \(d=3\), up to simultaneous signed-coordinate permutations and interchanging \(x,y\), the only equality configuration is
\[
x=(1/2,1/2,0),\qquad y=(1/2,0,1/2).
\]
The result quantifies and classifies maximal failure of the convex-hull location property for a canonical non-Hilbert norm.

## Assumptions and scope
Work in the **real** normed space \(X=(\mathbb R^d,\|\cdot\|_1)\), where \(d\) is an integer at least three. Set \(x\perp_B y\) if \(\|x+ty\|_1\ge\|x\|_1\) for every real \(t\). The unique Fermat–Torricelli median \(m=m(0,x,y)\) minimizes
\[
F(z)=\|z\|_1+\|z-x\|_1+\|z-y\|_1
\]
over all \(z\in X\). Uniqueness follows because each coordinate is the unique median of three real numbers. Write \(C=\{\alpha x+\beta y:\alpha,\beta\ge0,\alpha+\beta\le1\}\), and \(\Delta(x,y)=\inf_{z\in C}\|m-z\|_1\).

## Proof
**1. Exact coordinate identities.** On each coordinate, the median of \(0,x_i,y_i\) equals zero when \(x_i y_i\le0\), and otherwise it has their common sign and magnitude \(\min\{|x_i|,|y_i|\}\). Therefore, with
\[
a=\sum_{i=1}^{d}\min(|x_i|,|y_i|),
\]
we have \(\|m\|_1\le a\). In every coordinate, direct checking of the two possible sign patterns shows
\[
\left|m_i-\frac{x_i+y_i}{2}\right|=\frac12\big||x_i|-|y_i|\big|.
\]
Since \(\|x\|_1=\|y\|_1=1\), summing gives
\[
\left\|m-\frac{x+y}{2}\right\|_1=1-a.
\]
Both \(0\) and \((x+y)/2\) belong to \(C\), so
\[
0\le\Delta(x,y)\le\min(a,1-a)\le\frac12.
\]
Neither Birkhoff–James orthogonality nor the dimension restriction is needed for this estimate.

**2. Necessary equality structure.** Suppose \(\Delta(x,y)=1/2\). The two endpoint estimates force \(a=1/2\) and \(\|m\|_1=a\). Thus there can be no coordinate with \(x_i y_i<0\) and both entries nonzero: such a coordinate contributes strictly to \(a\) but zero to \(\|m\|_1\). Set \(S=\{i:x_i y_i>0\}\), so \(\sum_{i\in S}\min(|x_i|,|y_i|)=1/2\) and \(m\) is supported on \(S\).

The origin is a nearest point of \(C\) to \(m\), since \(\|m\|_1=\Delta=1/2\). Hence, along the segment from \(0\) to \(x\), the right derivative at zero of \(t\mapsto\|m-tx\|_1\) is nonnegative. At coordinates in \(S\) the derivative is \(-|x_i|\), and outside \(S\) it is \(+|x_i|\). Therefore
\[
0\le 1-2\sum_{i\in S}|x_i|.
\]
But \(\sum_{i\in S}|x_i|\ge a=1/2\), so this sum equals \(1/2\). Applying the same reasoning to \(y\) proves \(\sum_{i\in S}|y_i|=1/2\). Since both sums equal \(\sum_{i\in S}\min(|x_i|,|y_i|)\), every coordinate in \(S\) satisfies \(x_i=y_i\). Outside \(S\), no coordinate may have both \(x_i\ne0\) and \(y_i\ne0\), because opposite-sign overlap was excluded and same-sign overlap would put it in \(S\). Thus setting \(c_i=x_i=y_i\) on \(S\) and zero elsewhere, \(u=x-c\), \(v=y-c\), yields pairwise disjoint supports and \(\|c\|_1=\|u\|_1=\|v\|_1=1/2\).

**3. Sufficiency and orthogonality.** Conversely, suppose the displayed decomposition holds. The median is \(m=c\). For any \(\alpha,\beta\ge0\) with \(\alpha+\beta\le1\), pairwise support disjointness gives
\[
\|m-\alpha x-\beta y\|_1
=(1-\alpha-\beta)\|c\|_1+\alpha\|u\|_1+\beta\|v\|_1
=\frac12.
\]
Hence \(\Delta=1/2\). Define a linear functional of dual \(\ell_\infty\)-norm one by taking the coordinate sign of \(c\) on its support, the sign of \(u\) on its support, and the opposite sign of \(v\) on its support (arbitrary values of modulus at most one elsewhere). Then \(f(x)=1\) and \(f(y)=0\), so \(\|x+ty\|_1\ge f(x+ty)=1\) for all real \(t\): \(x\perp_B y\). Interchanging \(u\) and \(v\) constructs the reverse relation.

**4. Sharp witness and dimension-three rigidity.** Take \(c=e_1/2\), \(u=e_2/2\), \(v=e_3/2\) (zeros in additional coordinates). It realizes \(\Delta=1/2\) and both orthogonality relations. Conversely, when \(d=3\), each of the three disjoint nonzero supports must consist of exactly one coordinate. Signs and coordinate permutations reduce any equality pair to this witness, up to interchange.

## Verification
The standalone script `checks/median_hull_exact.py` uses only Python's standard library and exact `fractions.Fraction` arithmetic. It computes the \(\ell_1\)-distance from the median to the triangle by enumerating all pairwise intersections of affine sign-break lines with the triangle boundary; this is exhaustive for the *finite test instances*, because the objective is convex piecewise affine in the two barycentric parameters. It checked 1,500 reproducible rational three-dimensional pairs and explicit witnesses in dimensions three through seven, producing `TORRICELLI_L1_RIGIDITY_EXACT_CHECK_OK 4510`. The proof above, not the finite tests, establishes the universal statement.

## Relationship to prior work
Fang, Qi and Liu (arXiv:2611.09226v1; posted 6 November 2026) establish a qualitative characterization of inner-product spaces by the condition that each Birkhoff–James-orthogonal test triple has a Fermat–Torricelli median meeting its convex hull. That theorem does not quantify the distance in the non-Hilbert \(\ell_1\) model or characterize maximizers. Dragomir, Comănescu and Kikianty (2013, Theorem 6.3) supply the standard coordinatewise median formula in taxicab geometry, which is an essential previously known input. Martini, Swanepoel and Weiss (2002; open arXiv version 2007) study Fermat–Torricelli loci and convex-hull geometry, establishing in particular containment for odd numbers of sites in normed planes; the present statement concerns the sharp positive gap in dimension at least three. Paul, Roy, Sain and Sohel (arXiv:2501.10718) treat general optimization duality but no equal-unit-sharp hull-gap extremizer classification. The new contribution is the sharp dimension-independent bound **and complete disjoint-support rigidity** for the stated three-point \(\ell_1\) class.

## Limitations
The theorem covers real coordinate \(\ell_1^d\) spaces, three equally weighted sites, unit norms on the two nonzero sites, and ordinary convex-hull distance. It does not claim a stability modulus for near-equality, nor a formula for unequal norm ratios or general Banach spaces. The originality assessment concerns accessible literature and indexed search; an unindexed equivalent quantitative characterization remains possible. Independent validation has not been performed.

## References
1. Z. Fang, J. Qi, Q. Liu, *A Fermat–Torricelli convex-hull characterization of inner-product spaces via Birkhoff–James orthogonality*, arXiv:2611.09226v1, 6 November 2026. https://arxiv.org/abs/2611.09226
2. S. S. Dragomir, D. Comănescu, E. Kikianty, *Torricellian points in normed linear spaces*, Journal of Inequalities and Applications 2013:258, Theorem 6.3. https://doi.org/10.1186/1029-242X-2013-258
3. H. Martini, K. J. Swanepoel, G. Weiss, *The Fermat–Torricelli problem in normed planes and spaces*, Journal of Optimization Theory and Applications 115 (2002), 283–314; open arXiv version 0707.2592. https://arxiv.org/abs/0707.2592
4. K. Paul, S. Roy, D. Sain, S. Sohel, *A unified approach to a family of optimization problems in Banach spaces*, arXiv:2501.10718, 18 January 2025. https://arxiv.org/abs/2501.10718
