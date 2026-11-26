# Exact third Zbăganu constants of real finite-dimensional cubes

## Finding
For each integer \(d\ge 1\), let \(X_d=(\mathbb R^d,\|\cdot\|_\infty)\). For vectors \(x_1,x_2,x_3\in X_d\) that are not all zero, define the three-vector geometric signed-sum quotient
\[
Z_3(x_1,x_2,x_3)=\frac{\left(\prod_{\varepsilon,\eta\in\{-1,1\}}\|x_1+\varepsilon x_2+\eta x_3\|_\infty\right)^{1/2}}{\|x_1\|_\infty^2+\|x_2\|_\infty^2+\|x_3\|_\infty^2}.
\]
Its sharp constant is
\[
\boxed{\sup Z_3=\begin{cases}1,&d=1,\\ 2,&d=2,\\1+\sqrt6/2,&d=3,\\3,&d\ge4.\end{cases}}
\]
In dimension three, the exact sharp upper bound is attained with unequal vector radii \(\sqrt6-2:1:1\). Thus the geometric-mean signed-sum constant is strictly smaller than the corresponding third von Neumann–Jordan arithmetic-mean constant \((3+\sqrt3)/2\) in \(\ell_\infty^3\). The dimension-four threshold is sharp.

## Assumptions and scope
The scalars are **real**, and \(d\) is any finite positive integer. No assertion is made for complex cube spaces. The quantity is the order-three geometric-mean Zbăganu functional (one sign fixed because global sign reversal preserves each norm); the real cube dimension is the varying parameter. A zero signed-sum norm makes the numerator zero. Scaling all three vectors by the same nonzero real constant leaves the quotient unchanged.

## Proof
Put \(a_i=\|x_i\|_\infty\), \(S=a_1+a_2+a_3\), and \(Q=a_1^2+a_2^2+a_3^2>0\). Write \(r_{\varepsilon,\eta}=\|x_1+\varepsilon x_2+\eta x_3\|_\infty\). The triangle inequality gives \(r_{\varepsilon,\eta}\le S\) for every sign choice.

**Dimension one.** For real scalars \(x_i\), the four squared signed sums have arithmetic mean \(Q\), since every mixed term cancels. The arithmetic-geometric mean inequality therefore yields \((\prod r_{\varepsilon,\eta})^{1/2}\le Q\). Equality is attained when exactly one vector is nonzero, proving the value \(1\).

**Dimension two.** Coordinatewise \(\|y\|_\infty^2\le |y_1|^2+|y_2|^2\). Averaging the four squared signed sums and using mixed-term cancellation yields
\[
\frac14\sum_{\varepsilon,\eta}r_{\varepsilon,\eta}^2
\le\sum_{i=1}^3\bigl(|(x_i)_1|^2+|(x_i)_2|^2\bigr)\le2Q.
\]
The geometric mean of the four squared numbers is no larger than their arithmetic mean, so \(Z_3\le2\). The triple \(x_1=(1,1)\), \(x_2=(1,-1)\), \(x_3=0\) has all four signed-sum norms equal to \(2\), proving equality.

**Dimension three.** Choose for each of the four sign pairs a coordinate at which its supremum norm is attained. Because only three coordinates are available, there are two distinct signs \(\sigma\ne\tau\) that choose the same coordinate. Their scalar sums at that coordinate are \(u+v\) and \(u-v\), where \(u\) is the sum of terms whose signs agree and \(v\) is the sum of terms whose signs differ. The two index sets partition \(\{1,2,3\}\) and are both nonempty: the first sign of every row is fixed, and the two sign rows are distinct. As all coordinate entries are real,
\[
 r_\sigma r_\tau=|u+v|\,|u-v|=|u^2-v^2|
\le\max\{A^2,B^2\}\le(S-m)^2,
\]
where \(A\) and \(B\) are the sums of the corresponding \(a_i\)'s and \(m=\min(a_1,a_2,a_3)\). The other two norms are at most \(S\), hence
\[
Z_3\le\frac{S(S-m)}{Q}.
\]
After permuting vectors, take \(m=a_1=a\le b=a_2\le c=a_3\), and put \(t=b+c>0\), \(u=a/t\). Then \(0\le u\le\tfrac12\), \(b^2+c^2\ge t^2/2\), so
\[
 Z_3\le\frac{t(a+t)}{a^2+b^2+c^2}
\le\frac{1+u}{u^2+1/2}.
\]
The derivative of the last function has the sign of \(\tfrac12-2u-u^2\). Its unique maximum on \([0,\tfrac12]\) occurs at \(u_*=(\sqrt6-2)/2\), where its value is \(1+\sqrt6/2\). To attain the bound, set \(a=\sqrt6-2\) and choose
\[
 x_1=(-a,-a,0),\qquad x_2=(-1,1,1),\qquad x_3=(-1,1,-1).
\]
Their four signed-sum norms, in the order \((+,+),(+,-),(-,+),(-,-)\), are \(2+a,2,2,2+a\). Therefore
\[
Z_3=\frac{2(2+a)}{a^2+2}=1+\frac{\sqrt6}{2},
\]
which proves the dimension-three value. Moreover, in **every** maximizing triple the three input radii, after reordering and common positive rescaling, must equal \((\sqrt6-2):1:1\): equality in \(b^2+c^2\ge (b+c)^2/2\) forces the larger two radii to coincide, and equality in the one-variable upper bound forces \(u=u_*\). This is a necessary radial rigidity statement, not a complete classification of the coordinatewise signs.

**Dimensions at least four.** The general upper bound is \(Z_3\le S^2/Q\le3\) by Cauchy–Schwarz. In \(\ell_\infty^4\), choose
\[
x_1=(1,1,1,1),\quad x_2=(1,1,-1,-1),\quad x_3=(1,-1,1,-1).
\]
For each choice of \((\varepsilon,\eta)\), one coordinate of \(x_1+\varepsilon x_2+\eta x_3\) equals \(3\); all four norms therefore equal \(3\). Since \(Q=3\), the quotient is \(3\). Appending zero coordinates gives equality in every higher dimension. The proof is complete.

## Verification
`verify.py` is a standalone Python 3 script using only the standard library. It numerically evaluates the cubic radical witness, tests the general upper bounds and intermediate paired-coordinate inequality against deterministic random real triples, and independently checks the dimension-one, dimension-two and dimension-four witnesses. Its finite tests are diagnostic only: the preceding inequalities and exact witnesses prove the result for all triples and every finite dimension.

## Relationship to prior work
Wan, Duan, Fang, Wang and Liu (first publicly posted 19 July 2026) study geometric norm constants of Banach spaces, including von Neumann–Jordan and Zbăganu variants; their results do not compute the order-three geometric-mean signed-sum quotient in real finite cubes. Ifronika, Gunawan and Lindiarni (first publicly posted 18 November 2026) define the general order-\(n\) geometric-mean Zbăganu functional and prove general inequalities and values for infinite-dimensional classical sequence/Lebesgue and Morrey spaces. The present exact finite-cube dimension sequence is not supplied there. The distinction from the arithmetic-mean constant matters: published work on the third von Neumann–Jordan constant of the real three-cube yields \((3+\sqrt3)/2\), whereas the product-based functional here has the different sharp value \(1+\sqrt6/2\). The two conclusions do not imply one another by a sharp equality theorem.

## Limitations
The proof depends crucially on *real* scalar factorization \(|u+v||u-v|=|u^2-v^2|\). It does not establish the same values for complex cubes, nor determine order \(n\ge4\). Literature comparisons identify no exact pre-existing formula for this particular finite-cube order-three invariant, but cannot exclude implicit coverage under another notation. An independent mathematical audit has not been performed.

## References
1. S. Wan, P. Duan, Z. Fang, Y. Wang and Q. Liu, “A generalization of the \((\alpha,\beta,\gamma)\) von Neumann-Jordan type constant in Banach spaces,” arXiv:2607.17241, first public 19 July 2026. https://arxiv.org/abs/2607.17241
2. Ifronika, H. Gunawan and J. Lindiarni, “The n-th Zbáganu constant,” arXiv:2611.24308v1, first public 18 November 2026. https://arxiv.org/html/2611.24308v1
3. M. Ciesielski and R. Płuciennik, “On some modifications of n-th von Neumann–Jordan constant for Banach spaces,” *Banach Journal of Mathematical Analysis* 14 (2020), 650–673; first public arXiv:1811.01652 (2018).
4. “Exact third von Neumann–Jordan gap in \(\ell_\infty^3\),” published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-third-von-neumann-jordan-gap-in-ell-infty-3--425b85a56396
