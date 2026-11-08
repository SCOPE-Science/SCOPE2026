# Sharp even-moment anisotropy and cubic reversal for centered affine functions on triangles

## Finding
For every nondegenerate Euclidean triangle with normalized uniform area measure, all centered nonzero real affine functions admit an explicit **sharp all-even-moment directional profile**. Write their vertex values as \(a,b,c\), so \(a+b+c=0\), and define
\[
s_2=a^2+b^2+c^2>0,\quad s_3=a^3+b^3+c^3,\quad \eta=\frac{6s_3^2}{s_2^3}\in[0,1].
\]
For each integer \(m\ge1\) the precise identity is
\[
\boxed{\frac{\|f\|_{2m}^{2m}}{\|f\|_2^{2m}}
= L_m\sum_{j=0}^{\lfloor m/3\rfloor}\binom{m-j}{2j}\left(\frac{4\eta}{27}\right)^j,\qquad
L_m=\frac{2\cdot6^m}{(2m+1)(2m+2)}.}
\]
At \(m=1\) this is \(1\); at \(m=2\) it is the direction-independent constant \(12/5\). For every integer \(m\ge3\), the expression is strictly increasing on \(0\le\eta\le1\) and yields the sharp range
\[
\boxed{L_m\le\frac{\|f\|_{2m}^{2m}}{\|f\|_2^{2m}}\le
U_m=\frac{2^{m+1}(2^{2m+2}+6m+5)}{9(2m+1)(2m+2)}.}
\]
The lower equality case is exactly a permutation of a nonzero multiple of \((1,-1,0)\); the upper equality case is exactly a permutation of a nonzero multiple of \((2,-1,-1)\). A quantified exact remainder holds:
\[
\frac{\|f\|_{2m}^{2m}}{\|f\|_2^{2m}}-L_m
=L_m\sum_{j=1}^{\lfloor m/3\rfloor}\binom{m-j}{2j}\left(\frac{4\eta}{27}\right)^j\ge0.
\]
In particular, the first directional variation occurs at sixth order and reads \((54+8\eta)/7\).

For **absolute cubic moments**, the extremal directions reverse:
\[
\boxed{\frac{46\sqrt2}{45}\le\frac{\|f\|_3^3}{\|f\|_2^3}\le\frac{3\sqrt6}{5}.}
\]
The lower equality class is \((2,-1,-1)\) and the upper is \((1,-1,0)\), modulo permutation and nonzero scaling. All bounds are affine-invariant in the triangle shape.

## Assumptions and scope
A triangle means the convex hull of three noncollinear points in \(\mathbb R^2\), with Lebesgue area divided by its total area. Let \(\lambda_1,\lambda_2,\lambda_3\) denote barycentric coordinates. Every affine function with vanishing area mean is uniquely represented as \(f=a\lambda_1+b\lambda_2+c\lambda_3\), where \(a+b+c=0\). The norms are with respect to probability area measure. Coefficients are real. The equalities allow scalar multiplication by any nonzero real constant and permutation of the triangle vertices.

## Proof
**1. Exact simplex moments.** Under normalized area measure, the random barycentric vector has the \(\operatorname{Dirichlet}(1,1,1)\) law. Therefore, for nonnegative integers \(i,j,k\),
\[
\mathbb E[\lambda_1^i\lambda_2^j\lambda_3^k]=\frac{2i!j!k!}{(i+j+k+2)!}.
\]
Writing \(h_n(a,b,c)=\sum_{i+j+k=n}a^ib^jc^k\), multinomial expansion gives
\[
\mathbb E[f^n]=\frac{2n!}{(n+2)!}h_n(a,b,c)
=\frac{2h_n(a,b,c)}{(n+1)(n+2)}.
\]
The generating series is \(\sum_{n\ge0}h_nt^n=1/((1-at)(1-bt)(1-ct))\). Since \(a+b+c=0\), Newton's identities yield
\[
\sum_{n\ge0}h_nt^n=\frac1{1-(s_2/2)t^2-(s_3/3)t^3}.
\]
Thus \(h_2=s_2/2\), and \(\|f\|_2^2=s_2/12\).

**2. All even orders.** Extracting coefficient \(t^{2m}\) in the geometric series, the nonnegative solutions of \(2k+3\ell=2m\) have \(\ell=2j\), \(k=m-3j\), and the corresponding coefficient is \(\binom{m-j}{2j}(s_2/2)^{m-3j}(s_3/3)^{2j}\). Dividing the expected even power by \((s_2/12)^m\) proves the formula, including its exact normalization \(4\eta/27\). For the roots \(a,b,c\) of \(z^3-(s_2/2)z-(s_3/3)=0\), the discriminant is
\[
(a-b)^2(b-c)^2(c-a)^2=\frac{s_2^3}{2}-3s_3^2=\frac{s_2^3}{2}(1-\eta)\ge0.
\]
Hence \(0\le\eta\le1\); the upper endpoint is equivalent to a repeated vertex value and therefore to the orbit of \((2,-1,-1)\). Since \(s_3=3abc\), the lower endpoint means one vertex value vanishes, hence the orbit of \((1,-1,0)\). For \(m\ge3\), the \(j=1\) coefficient is strictly positive; every other coefficient is nonnegative, giving strict monotonicity, full equality classification, and the displayed exact remainder. At \(\eta=1\), one may take \(a=2,b=c=-1\), so \(f=3\lambda_1-1\). Since \(\lambda_1\) has density \(2(1-t)\) on \([0,1]\), direct integration yields
\[
\mathbb E[(3\lambda_1-1)^{2m}]=\frac{2(2^{2m+2}+6m+5)}{9(2m+1)(2m+2)}.
\]
Its variance is \(1/2\); division by \((1/2)^m\) gives \(U_m\).

**3. The third absolute moment and reverse ordering.** Modulo vertex permutation, nonzero real scaling, and simultaneous sign reversal, any centered triple has values proportional to \((-1,-r,1+r)\) for exactly one \(r\in[0,1]\). For a uniform triangle and distinct vertex values \(v_1,v_2,v_3\), the Hermite–Genocchi divided-difference formula gives
\[
\mathbb E|f|^3=\frac1{10}\sum_{i=1}^3\frac{|v_i|^5}{\prod_{j\ne i}(v_i-v_j)},
\]
with coincident vertices interpreted by continuous limits. This follows by applying the two-dimensional simplex integration formula to \(g(t)=|t|^3\), whose second primitive is \(G(t)=|t|^5/20\). Substitution of \((-1,-r,1+r)\), together with \(\|f\|_2^2=(1+r+r^2)/6\), yields
\[
\frac{\|f\|_3^3}{\|f\|_2^3}=\frac{6^{3/2}}{10}G(r),\quad
G(r)=\frac{(1+r)(2r^4+6r^3+7r^2+6r+2)}{(r+2)(2r+1)(1+r+r^2)^{3/2}}.
\]
An exact differentiation and factorization give
\[
G'(r)=\frac{r(r-1)(2r^4+14r^3+25r^2+14r+2)}{2(r+2)^2(2r+1)^2(1+r+r^2)^{5/2}}<0
\quad (0<r<1).
\]
Its endpoint values are \(G(0)=1\) and \(G(1)=46/(27\sqrt3)\), giving respectively \(3\sqrt6/5\) and \(46\sqrt2/45\) after multiplication by \(6^{3/2}/10\). The strict derivative proves both equality classes. (The ratio is unchanged by any affine deformation of the triangle.)

## Verification
The standalone `check_triangle_moments.py` runs with Python 3 and SymPy. It compares the barycentric-moment expansion against the generating function for all degrees through \(18\), verifies the even profile algebraically for the first nine integer exponents, checks the discriminant factorization, the absolute-cubic derivative and both endpoint formulas, and tests the closed upper envelope. These finite symbolic checks support the proof but do not replace its all-order coefficient-extraction argument. Command: `python check_triangle_moments.py`.

## Relationship to prior work
Gravin, Pasechnik, Shapiro and Shapiro give general rational generating functions for moments of polytopes (arXiv:1210.3193, Corollary 3). The complete-homogeneous moment identity above follows directly from that general theorem; it is **not** claimed as novel. The contribution here is the **sharp all-even-order extremum profile over coefficient directions**, exact directional stability and equality classes, together with the distinct absolute-cubic reversal. Anderson, Goyal and Rademacher (arXiv:1211.2227, third-moment analysis and Theorem 8) optimize a *signed* third moment in simplex learning; their statistic differs from the absolute third moment optimized here. General discrete zero-sum \(\ell_p\) distortion results concern a different measure and do not imply the displayed continuum-area formulas. Related published work has been checked by mathematical implication as well as keywords; hidden historical equivalents cannot be excluded.

## Limitations
Only real centered affine functions and normalized uniform area on a nondegenerate triangle are covered. All even integer exponents are resolved, as is absolute exponent three. No general extremal classification is asserted for arbitrary noninteger exponents, for higher-degree polynomial spaces, higher-dimensional simplices, or nonuniform densities. The proof is analytic and internally checked; no independent mathematical audit has occurred.

## References
- A. Gravin, D. Pasechnik, B. Shapiro and M. Shapiro, *On moments of a polytope*, first preprint 2012-10-11, arXiv:1210.3193, https://arxiv.org/abs/1210.3193. Relevant material: general moment generating functions and Corollary 3.
- J. Anderson, N. Goyal and L. Rademacher, *Efficient Learning of Simplices*, preprint 2012-11-09, arXiv:1211.2227, https://arxiv.org/abs/1211.2227. Relevant material: simplex third moments and Theorem 8.
