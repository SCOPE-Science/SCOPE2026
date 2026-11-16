# A sharp Lu Qi-Keng transition for Euclidean-distance-weighted bidisk kernels

## Finding
For every integer \(m\ge0\), let \(A^2_m(\mathbb D^2)\) be the holomorphic Hilbert space with norm induced by the product of normalized planar area measures, weighted by the \(m\)-th power of the **Euclidean distance to the boundary of the bidisk**. Write its reproducing kernel as \(K_m(z,\zeta)\). Then
\[
K_m(z,\zeta)\ne0\quad\text{for all }z,\zeta\in\mathbb D^2
\quad\Longleftrightarrow\quad m\in\{0,1\}.
\]
For each \(m\ge1\), the restriction to **equal cross-products** \(z_1\overline{\zeta_1}=z_2\overline{\zeta_2}=x\) has an explicit numerator polynomial \(P_m(x)\), every zero of which is real, strictly negative and simple. Consecutive polynomials have strictly interlacing negative zeros, allowing either equal or one-greater degree; in particular their rightmost zeros move strictly toward zero. The first interior-kernel zero occurs at \(m=2\): its equal-product coordinate is
\[
x_2=\frac{-11+2\sqrt{19}}{3}\in(-1,0).
\]
This is an integer-exponent classification; no conclusion is claimed for nonintegral powers.

## Assumptions and scope
Use \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), normalized planar area \(dA/\pi\), and
\[
\delta(z_1,z_2)=\operatorname{dist}_{\mathbb C^2}((z_1,z_2),\partial\mathbb D^2)
=\min\{1-|z_1|,1-|z_2|\}.
\]
The Hilbert norm is \(\|f\|_m^2=\int_{\mathbb D^2}|f(z)|^2\delta(z)^m\,dA(z_1)dA(z_2)/\pi^2\). The boundary of this domain has corners; the weight is not a tensor product of one-variable weights. For \(m\in\mathbb N_0\), all monomials are integrable and form a complete orthogonal basis. All zeros discussed are zeros of the off-diagonal reproducing kernel, not of its strictly positive diagonal \(K_m(z,z)\).

## Proof
**1. Exact moments and kernel.** Independent angular integration and layer cake give, for \(j,k\ge0\) and \(m\ge1\),
\[
\begin{aligned}
\|z_1^jz_2^k\|_m^2
&=4\int_0^1\int_0^1 r^{2j+1}s^{2k+1}\min(1-r,1-s)^m\,dr\,ds\\
&=\frac{m}{(j+1)(k+1)}\int_0^1u^{m-1}(1-u)^{2j+2k+4}\,du\\
&=\frac{m!(2j+2k+4)!}{(j+1)(k+1)(2j+2k+m+4)!}.
\end{aligned}
\]
The final formula is also valid for \(m=0\). If \(u=z_1\overline{\zeta_1}\), \(v=z_2\overline{\zeta_2}\), then
\[
K_m(u,v)=\frac1{m!}\sum_{j,k\ge0}(j+1)(k+1)(2j+2k+5)_m\,u^jv^k,
\]
where \((a)_m=\prod_{q=0}^{m-1}(a+q)\), with \((a)_0=1\). All series converge normally on compact subsets of the bidisk. Set \(G_m=m!K_m\). Coefficient comparison yields
\[
G_0(u,v)=\frac1{(1-u)^2(1-v)^2},\qquad
G_{m+1}=(2u\partial_u+2v\partial_v+m+5)G_m.
\]

**2. Sharp zero-free portion.** The unweighted kernel is the zero-free product \(K_0=G_0\). Direct differentiation gives
\[
K_1(u,v)=\frac{5-u-v-3uv}{(1-u)^3(1-v)^3}.
\]
If its numerator vanished for \(|u|,|v|<1\), then \((1+3u)v=5-u\). But
\[
|5-u|^2-|1+3u|^2
=8(3-2\operatorname{Re}u-|u|^2)>0\quad(|u|<1),
\]
whereas \(|v|<1\); contradiction, including the case \(1+3u=0\). Hence \(m=1\) is zero-free.

**3. Equal-cross-product polynomials.** Let \(x=u=v\). Since
\(\sum_{j=0}^{N}(j+1)(N-j+1)=\binom{N+3}{3}\), the restricted kernel is
\[
K_m(x,x)=\sum_{N\ge0}\binom{N+3}{3}
\frac{(2N+5)_m}{m!}x^N
=\frac{P_m(x)}{(1-x)^{m+4}}.
\]
Here \(K_m(x,x)\) denotes substitution of **cross-products** \(u=v=x\), not evaluation of the positive diagonal of the Bergman kernel. From the differential recurrence,
\[
P_0=1,\qquad
(m+1)P_{m+1}(x)=2x(1-x)P_m'(x)+[(m+5)+(m+3)x]P_m(x).
\tag{1}
\]
In particular \(P_1=5+3x\), \(P_2=15+22x+3x^2\). If \(P_m=\sum_{j=0}^{d_m}a_jx^j\), then the coefficient \(b_j\) of \(x^j\) in the next polynomial satisfies
\[
(m+1)b_j=(2j+m+5)a_j+(m+5-2j)a_{j-1},
\]
with out-of-range coefficients zero. Directly, \(d_0=0\), \(d_1=1\), and \(d_m=\lfloor(m+3)/2\rfloor\) for \(m\ge2\). An induction on the above coefficient relation proves every coefficient of \(P_m\) is strictly positive: for \(j\le d_m\), \(m+5-2j\ge2\) when \(m\ge2\); the new leading coefficient has sign \(m+3-2d_m\) and vanishes exactly when the asserted degree does not grow. The base polynomials are explicit.

**4. Strict real-rootedness and interlacing.** The assertion holds for \(P_1\), whose sole zero is \(-5/3\). Assume \(P_m\) has \(d_m\) simple negative roots \(r_1<\cdots<r_{d_m}<0\) and positive leading coefficient. Equation (1) gives
\[
P_{m+1}(r_i)=\frac{2r_i(1-r_i)}{m+1}P_m'(r_i).
\]
The factor before the derivative is negative, and the signs of \(P_m'(r_i)\) alternate. Thus there is one new root between each consecutive pair. At the rightmost root, \(P_m'(r_{d_m})>0\), so \(P_{m+1}(r_{d_m})<0\), whereas \(P_{m+1}(0)>0\); a further root belongs to \((r_{d_m},0)\). If \(d_{m+1}=d_m+1\), positive leading coefficient makes the sign at negative infinity opposite to the sign at \(r_1\), giving an extra root to the left. This accounts for the full degree in both cases. All roots are distinct, negative, and interlace strictly, and the rightmost root moves strictly right.

**5. Actual off-diagonal kernel zeros.** The rightmost zero of \(P_2\) is \(x_2=(-11+2\sqrt{19})/3\in(-1,0)\). By strict rightmost-root interlacing, each \(P_m\), \(m\ge2\), has a root \(x_m\in(x_2,0)\subset(-1,0)\). Take the bidisk points \(z=(\sqrt{-x_m},\sqrt{-x_m})\) and \(\zeta=(-\sqrt{-x_m},-\sqrt{-x_m})\). Then both cross-products equal \(x_m\), and \(K_m(z,\zeta)=0\), since the denominator is nonzero. This completes the classification.

## Verification
The included `CHECK.py` independently constructs \(P_m\) by exact rational coefficient arithmetic, tests the moment-series identity over finite index ranges and the first-order bivariate kernel, and checks finite instances of root separation. These are reproducibility checks, **not** a substitute for the preceding all-integer proof. Run `python3 CHECK.py` with standard Python 3; no third-party packages are required.

## Relationship to prior work
Marinescu and Xing (first public September 21, 2026) study parameter dependence of the same Euclidean boundary-distance family on **smoothly bounded** pseudoconvex domains. Their full text explicitly assumes \(C^2\) boundary for the singular distance-power theorem and does not give this bidisk Lu Qi-Keng classification. Fu and Deng provide the general monomial-moment representation for torus-invariant weighted Reinhardt spaces, which underlies but does not imply the present zero-set result. Perälä studies zeros for radial weighted kernels in **one complex variable**. Related published Euclidean-distance classifications for the unit disk and complex ball differ geometrically: the bidisk's distance is a coupled minimum, and its kernel is not a product. The novelty assessment is limited to inspected sources; an equivalent treatment under other terminology remains a publication-priority risk.

## Limitations
Only nonnegative **integer** exponents are classified. The argument does not classify nonintegral powers or the entire two-complex-variable zero variety when \(m\ge2\), nor does it characterize every zero away from equal cross-products. External independent mathematical verification and exhaustive literature-priority confirmation have not been performed.

## References
- G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258 (first submitted September 21, 2026), https://arxiv.org/abs/2609.24258.
- Q. Fu and G. Deng, *The weighted reproducing kernels of the Reinhardt domain*, arXiv:2209.09394 (2022), https://arxiv.org/abs/2209.09394.
- A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976 (2017), https://arxiv.org/abs/1703.05976.
- H. P. Boas, S. Fu and E. J. Straube, *The Bergman kernel function: explicit formulas and zeroes*, arXiv:math/9706202 (1997), https://arxiv.org/abs/math/9706202.
