# A single-polynomial covariogram on every ray of a cross-polytope

## Finding

Let \(d\ge1\), let \(B_1^d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\), and let \(v\in\mathbb R^d\setminus\{0\}\). Define the directional covariogram
\[
g_v(t)=\operatorname{vol}_d\bigl(B_1^d\cap(B_1^d+tv)\bigr),\qquad t\ge0.
\]
Then on the **entire** overlap interval \(0\le t\le2/\|v\|_1\), the function \(g_v\) agrees with a **single real polynomial of degree at most \(d\)**; it has no interior polynomial knots. The overlap is zero beyond that interval. The polynomial can be constructed by the explicit finite formula below, without integrating or solving a polytope-volume problem at each translation. The same statement holds for coordinate directions and non-generic rays by continuity.

For a direction with positive coordinates, write \([d]=\{1,\ldots,d\}\), \(L=\sum_i v_i\), \(U=1-Lt/2\), and, for \(I\subseteq[d]\), \(r\ge1\), and real \(c\), put
\[
 W_{I,r}(c)=\frac{r!}{(|I|+r)!}\sum_{H\subseteq I}(-1)^{|H|}\left(\sum_{i\in I\setminus H}v_i-c\right)_+^{|I|+r},\qquad x_+=\max(x,0).
\]
The all-ray polynomial is
\[
\boxed{\displaystyle
g_v(t)=\frac{2^d}{d!}
-2\sum_{\varnothing\ne E\subseteq[d]}\frac1{|E|!}\sum_{P\subseteq E}
\sum_{\substack{1\le r\le|E|\\r\ \mathrm{odd}}}
\binom{|E|}{r}\,t^{d-|E|+r}\left(1-\frac{Lt}{2}\right)^{|E|-r}
W_{[d]\setminus E,r}\left(\frac L2-\sum_{i\in P}v_i\right).}
\]
Every positive part in this display depends **only on the fixed direction**, never on \(t\); therefore it is genuinely one polynomial. The degree is at most \(d\) in each summand. For arbitrary signs, replace \(v_i\) by \(|v_i|\); for zero coordinates use the continuous limit of this coefficient formula.

For positive directions and \(d\ge2\), the overlap has the additional sharp endpoint behavior
\[
 g_v(t)=L\left(\frac2L\right)^{d-1}f_v(L/2)\left(\frac2L-t\right)
+O\left(\left(\frac2L-t\right)^2\right),
\]
where
\[
 f_v(s)=\frac1{(d-1)!}\sum_{H\subseteq[d]}(-1)^{|H|}\left(s-\sum_{i\in H}v_i\right)_+^{d-1}>0\quad\text{at }s=L/2.
\]
(The endpoint may have higher-order contact when some direction coordinates vanish.)

## Assumptions and scope

Volumes are ordinary \(d\)-dimensional Lebesgue volumes; the cross-polytope is the unit \(\ell_1\)-ball, not an arbitrary affine image unless the translation is transformed accordingly. Directions and translation parameters are real; the result is exact for every \(d\ge1\) and every nonzero direction. The formula's direct proof first assumes all \(v_i>0\). Independent sign changes preserve the body, and continuity of intersection volumes and of the finite formula extends it to zero coordinates. The first derivative assertion at support applies to directions with **all coordinates nonzero** and \(d\ge2\). No analogous simple-contact claim is made along coordinate hyperplanes.

## Proof

**1. Midpoint coordinates and a finite partition.** By sign symmetry assume \(v_i>0\). Translate the two balls to centers \(\pm s\), with \(s_i=tv_i/2\), and set \(U=1-\sum_i s_i\). The two defining inequalities are equivalent to
\[
\sum_{i=1}^d\max(|y_i|,s_i)+\left|\sum_{i=1}^d\operatorname{clip}(y_i,[-s_i,s_i])\right|\le1,
\]
because \(|y_i\pm s_i|=\max(|y_i|,s_i)\pm\operatorname{clip}(y_i,[-s_i,s_i])\). In each partition let \(E\) index the coordinates outside \([-s_i,s_i]\), let \(P\subseteq E\) index the positive outside coordinates, and let \(I=[d]\setminus E\). For outside coordinates write \(|y_i|=s_i+w_i\), with \(w_i\ge0\); for inside coordinates write \(z_i=y_i+s_i\in[0,tv_i]\). The inequality becomes
\[
\sum_{i\in E}w_i+\left|\sum_{i\in I}z_i-a\right|\le U,
\qquad a=t\left(\frac L2-\sum_{i\in P}v_i\right).
\]
For \(k=|E|\ge1\), integrating the nonnegative outside variables gives \((U-|\sum z_i-a|)_+^k/k!\). For \(k=0\), the same expression is interpreted as the indicator of \(|\sum z_i-a|<U\), up to null sets.

**2. The truncated-power identity and box moments.** For \(k\ge0\), \(U\ge0\), and almost every real \(x\),
\[
 (U-|x|)_+^k=(x+U)_+^k-2\sum_{\substack{1\le r\le k\\r\ \mathrm{odd}}}\binom{k}{r}U^{k-r}(x)_+^r-(-1)^k(x-U)_+^k.
\]
When \(k=0\), take \(x_+^0=\mathbf 1_{x>0}\). This identity follows by checking the three intervals \(x<-U\), \(-U<x<0\), and \(0<x<U\), with cancellation for \(x>U\). The elementary box-moment formula is
\[
 T_{I,r}(a;t):=\int_{\prod_{i\in I}[0,tv_i]}(\sum_{i\in I}z_i-a)_+^r\,dz
=\frac{r!}{(|I|+r)!}\sum_{H\subseteq I}(-1)^{|H|}
\left(t\sum_{i\in I\setminus H}v_i-a\right)_+^{|I|+r}.
\]
It is inclusion-exclusion applied to the standard simplex volume integral. The boundary cases \(|I|=0\) and \(r=0\) use point mass and the indicator convention, respectively.

**3. Global cancellation of both outer truncated powers.** Sum over every \(E\subseteq[d]\), \(P\subseteq E\), and \(H\subseteq I\). The first outer term \(T_{I,k}(a-U;t)/k!\) reduces to
\[
 \frac1{d!}\sum_{E,P,H}(-1)^{|H|}
 \left(1-t\sum_{i\in(E\setminus P)\cup H}v_i\right)_+^d.
\]
Fix a subset \(J\) appearing in the displayed inner sum. Each coordinate in \(J\) may be a negative outside coordinate (weight \(+1\)) or an inside coordinate belonging to \(H\) (weight \(-1\)); these choices cancel. Each coordinate not in \(J\) has two positive choices. Only \(J=\varnothing\) survives, contributing exactly \(2^d/d!\).

Likewise, after including the coefficient \((-1)^k\), the last outer term \(T_{I,k}(a+U;t)/k!\) has arguments
\[
\left(t\sum_{i\in P\cup(I\setminus H)}v_i-1\right)_+^d.
\]
For each coordinate included in this sum, its positive-outside and inside-not-in-\(H\) contributions cancel because of the exterior parity factor. Only the empty included subset might survive, and its positive-part value is \((-1)_+^d=0\). Thus **the entire last term vanishes**.

**4. The remaining polynomial.** For each odd \(r\), the middle box moment has the homogeneous form
\[
T_{I,r}(a;t)=t^{|I|+r}W_{I,r}\left(\frac L2-\sum_{i\in P}v_i\right).
\]
Substituting it into the global partition sum gives exactly the boxed formula in the finding. All remaining positive parts are constants for the chosen \(v\). Each monomial factor has total degree \((d-k+r)+(k-r)=d\), though cancellations can lower the final degree. This proves one polynomial on \(0\le t\le2/L\). If \(tL>2\), the triangle inequality forces the two balls to have empty intersection. Continuity proves both the support endpoint and the extension to zero coordinates.

**5. The endpoint coefficient (nonzero coordinate directions).** Let \(t_*=2/L\), and \(U=L(t_*-t)/2\). For \(E=\varnothing\), the remaining box condition is \(|\sum_i z_i-tL/2|\le U\); its volume is \(2U t^{d-1}f_v(L/2)+O(U^2)\), by the locally polynomial distribution of a sum of independent box coordinates. For every \(E\ne\varnothing\), at least one positive exterior variable and the central slab have simultaneous vanishing widths; its contribution is \(O(U^2)\) for \(d\ge2\), since each \(v_i>0\). Hence the quoted slope follows. The value \(f_v(L/2)>0\) because \(L/2\) is interior to the sum-of-boxes support and all side lengths are positive. A coordinate-zero translation can instead have a higher-order endpoint zero, so this hypothesis is essential.

## Verification

The standalone `verification/verify.py` uses exact rational arithmetic, independently evaluating the uncanceled partition sum and the finite-polynomial expression at 21 rational parameters on each of eight direction vectors in dimensions one through five. It also checks normalization at the origin and vanishing at the support endpoint. The optional `--hull` mode evaluates polytope volumes independently via `scipy.spatial.HalfspaceIntersection` and `ConvexHull` in dimensions two through four, away from degenerate endpoints. The actual package extracted and run with `--hull` returned `CROSSPOLYTOPE_RADIAL_POLYNOMIAL_OK 216`.

Examples include
\[
 g_{(1,1)}(t)=2(1-t)\quad(0\le t\le1),
\]
\[
 g_{(1,1,1)}(t)=\frac{(3t-4)(3t-2)}6\quad(0\le t\le2/3),
\]
and
\[
 g_{(1,2,3)}(t)=\frac{2(3t-1)(3t^2+3t-2)}3\quad(0\le t\le1/3).
\]
The all-dimensional mathematical proof does not depend on these finite tests.

## Relationship to prior work

Ramesh and Weiss (2026) study exact and high-precision volume computations for intersections of convex semialgebraic bodies and illustrate them with translated \(\ell_p\)-balls, including \(\ell_4\) examples. The present claim is a distinct structural phenomenon for congruent \(\ell_1\)-balls: a **single** polynomial on every radial overlap segment. Ando and Kijima (2016; later journal version 2020) establish hardness and deterministic approximation methods for intersections of general cross-polytopes, rather than this explicit same-shape all-ray cancellation law. Known covariogram theory gives general geometric relationships but does not by itself provide this formula. An arithmetically exact polynomial for orthotopes is not a cross-polytope formula. This comparison is based on inspected available primary text, relevant indexed research records, and statement/implication comparisons, not on keyword absence alone. Historical priority cannot be certified by a bounded literature search.

## Limitations

This establishes a polynomial along each fixed ray, **not** one multivariate polynomial in all translation coordinates; the polynomial coefficients may change when the direction crosses a subset-sum chamber. It does not solve the general intersection of two independently scaled, rotated or unequal cross-polytopes. The explicit finite sum may have exponential computational size. The simple endpoint slope requires nonzero coordinates. Independent mathematical review and definitive historical-priority verification have not been performed.

## References

1. L. Ramesh and N. Weiss, *Exact Volumes of Semi-Algebraic Convex Bodies*, arXiv:2602.04707 (first public 2026-02-04), https://arxiv.org/abs/2602.04707.
2. E. Ando and S. Kijima, *An FPTAS for the Volume of a \(\mathcal V\)-Polytope—It Is Hard to Compute the Volume of the Intersection of Two Cross-polytopes*, arXiv:1607.06173 (2016), https://arxiv.org/abs/1607.06173; journal version *Theoretical Computer Science* 833 (2020), 87–106.
3. G. Bianchi, *The covariogram and Fourier–Laplace transform in \(\mathbb C^n\)*, *Proceedings of the London Mathematical Society* 113 (2016), 1–23, https://doi.org/10.1112/plms/pdw020.
