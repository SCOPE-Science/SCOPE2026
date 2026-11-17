# Sharp two-input bounded-variation stability of harmonic-mean cubic Hermite interpolation

## Finding
Let \(y=(y_j)_{j\in\mathbb Z}\) be any real sequence of finite discrete total variation
\[
V_d(y)=\sum_{j\in\mathbb Z}|y_{j+1}-y_j|<\infty.
\]
Define the uniform-grid harmonic-mean cubic Hermite interpolant \(\mathcal H y\) in the next section. Then
\[
\operatorname{Var}_{\mathbb R}(\mathcal H y)=V_d(y)
\]
for every such \(y\), but the **sharp two-input variation Lipschitz factor** is
\[
\boxed{\sup_{V_d(y-z)>0}\frac{\operatorname{Var}_{\mathbb R}(\mathcal H y-\mathcal H z)}{V_d(y-z)}=\frac{59}{27}.}
\]
The supremum is approached by pairs whose difference is a single discrete jump, positioned in an almost-flat data interval between two unit rising intervals. In particular, individual shape/variation preservation does **not** imply nonexpansive perturbation sensitivity in total variation.

## Assumptions and scope
The index set is the entire integer line, the knot locations are exactly the integers, the data and all variations are real, and \(V_d(y),V_d(z)<\infty\). For \(s_j=y_{j+1}-y_j\), put
\[
H(a,b)=\begin{cases}\dfrac{2ab}{a+b},&ab>0,\\0,&ab\le0,\end{cases}
\qquad m_j=H(s_{j-1},s_j).
\]
Here \(H\) is the signed harmonic-mean selector, well defined also for negative arguments. Write
\[
S(t)=3t^2-2t^3,\quad A(t)=t(1-t)^2,\quad B(t)=t^3-t^2,
\qquad 0\le t\le1.
\]
The interpolant on each unit cell is exactly
\[
(\mathcal Hy)(j+t)=y_j+s_jS(t)+m_jA(t)+m_{j+1}B(t).
\]
It is globally continuously differentiable at the knots. Continuous total variation is the sum of the absolute derivative integrals over the cells. No finite-endpoint derivative rule is assumed: this is the full-line interior-slope harmonic-mean method, which coincides with the usual uniform-grid weighted harmonic mean in the original PCHIP interior construction. Constant translations of data translate the interpolant by the same constant.

## Proof
**1. Elementary cubic geometry.** Differentiating the three basis functions gives
\[
S'(t)=6t(1-t),\quad A'(t)=1-4t+3t^2,\quad B'(t)=-2t+3t^2.
\]
For each \(0\le u,v\le2\), the polynomial \(Q_{u,v}=S'+uA'+vB'\) is nonnegative throughout \([0,1]\). Indeed it depends affinely on \((u,v)\) and its values at the four corners of the rectangle \([0,2]^2\) are
\[
6t(1-t),\quad2(1-t),\quad2t,\quad2(1-3t+3t^2),
\]
all nonnegative on that interval. Thus
\[
\operatorname{Var}_{[0,1]}(S+uA+vB)=1.
\]
Moreover \(A\) is nonnegative with maximum \(4/27\) at \(1/3\), and \(B\) is nonpositive with minimum \(-4/27\) at \(2/3\). Both vanish at endpoints, so
\[
\operatorname{Var}(uB)=\frac{8u}{27},\quad
\operatorname{Var}(vA)=\frac{8v}{27}\qquad(u,v\ge0).
\]

**2. Preservation of each signal's variation.** If \(s_j\ne0\), the harmonic selector gives \(m_j/s_j,m_{j+1}/s_j\in[0,2]\); if \(s_j=0\), both endpoint slopes are zero. By step 1, each Hermite cell is monotone between its sampled endpoint values. Its variation is precisely \(|s_j|\). Summing over all integer cells proves the first identity, including when there are infinitely many nonzero increments.

**3. One-increment perturbation bound.** Holding all increments but \(s_k\) fixed, changing \(s_k\) translates every sample to the right of the edge \((k,k+1)\) by that change. The function \(a\mapsto H(a,b)\) is continuous and locally absolutely continuous, with derivative either zero or
\[
\frac{\partial H(a,b)}{\partial a}=\frac{2b^2}{(a+b)^2}\in[0,2]
\]
at differentiability points; the other partial derivative has the analogous formula. Along a unit positive perturbation of \(s_k\), let \(u=\partial m_k/\partial s_k\) and \(v=\partial m_{k+1}/\partial s_k\). Almost everywhere \(u,v\in[0,2]\). Up to translations in the argument and adding constants, the directional response is precisely
\[
\begin{array}{ll}
-u\,t^2(1-t),&[k-1,k],\\
S(t)+uA(t)+vB(t),&[k,k+1],\\
1+vA(t),&[k+1,k+2],
\end{array}
\]
and is zero to the far left and one to the far right. The three cells join continuously. Step 1 computes its total variation **exactly** as
\[
1+\frac{8(u+v)}{27}\le1+\frac{32}{27}=\frac{59}{27}.
\]
The same bound holds for negative perturbations after taking absolute values. Integrating along a finite change of \(s_k\) and applying the triangle inequality for variation proves the bound for each single-increment modification.

**4. Arbitrary pairs.** Differences of increment sequences lie in \(\ell^1(\mathbb Z)\). First telescope finitely many incremental modifications, changing the increments of \(z\) into those of \(y\), and apply step 3. For the general case change only finitely many increments, initially anchoring the value at the zeroth knot; as the finite set expands to all integers, these modified data converge at each fixed knot to the target data up to one global additive constant. The interpolation depends continuously on finitely many local samples, so the interpolants converge pointwise on each compact cell to the target interpolant up to the same constant. Total variation is lower semicontinuous under such pointwise convergence, and the omitted \(\ell^1\) increment differences have vanishing total mass. This gives
\[
\operatorname{Var}(\mathcal Hy-\mathcal Hz)
\le\frac{59}{27}\sum_k|s_k(y)-s_k(z)|
=\frac{59}{27}V_d(y-z).
\]

**5. Sharpness.** Define \(y\) by \(s_{-1}=s_1=1\), \(s_0=0\), and all other increments zero. Obtain \(z\) by changing only the middle increment to \(\varepsilon>0\), keeping the left-side value fixed. Then
\[
V_d(z-y)=\varepsilon,\qquad
m_0(z)=m_1(z)=\frac{2\varepsilon}{1+\varepsilon},\quad m_0(y)=m_1(y)=0.
\]
The central difference cell is monotone and varies by \(\varepsilon\); its two neighboring cells each contribute \(8m_0(z)/27\). Therefore the ratio is **exactly**
\[
\frac{\operatorname{Var}(\mathcal Hz-\mathcal Hy)}{V_d(z-y)}
=1+\frac{32}{27(1+\varepsilon)}\longrightarrow\frac{59}{27}
\quad(\varepsilon\downarrow0).
\]
This gives the matching lower bound and completes the proof. The limiting pair describes a supremum; attainment by a distinct finite perturbation is not asserted.

## Verification
The independent-of-sampling analytical proof above supplies the infinite-dimensional assertion. The included `verify.py` uses exact rational calculations for the cubic-corner identities, side extrema, and near-plateau witness ratios, then tests random finite sequences by integrating the absolute derivative of each cubic difference through its critical points. The random tests are corroboration, not a substitute for steps 1–5. Run with `python3 verify.py`; only the Python standard library is needed.

## Relationship to prior work
Fritsch and Butland (1984), pages 300–304, give the harmonic-mean interior-slope selector and prove local monotonicity for their interpolation methods. In particular their formula (2), and formula (5) on a uniform mesh, yield precisely the selector analyzed here. Their theorem and examples address **each interpolated signal** rather than the variation of the **difference of two different interpolants**, so their statement does not imply the value \(59/27\). Edelman and Micchelli (1987) classify admissible slopes for monotone/convex interpolation; this concerns the shape of a single interpolant and likewise does not determine a sharp nonlinear two-input variation modulus. Aràndiga and Yáñez (2019) examine accuracy and monotonicity of harmonic-mean variants; their inspected statements do not give the claimed variation-Lipschitz factor. A prior result about a median or another nonlinear filter cannot imply this constant without a separate reduction, and none was identified. Priority beyond the accessed literature is not certified.

## Limitations
The sharp number applies to the signed harmonic-mean interior-slope selector on the full equally spaced integer line, not to arbitrary finite-boundary PCHIP endpoint rules, nonuniform grids, other slope-limiter formulas, or multivariate interpolation. It is a supremal perturbation gain, not a claim of exact finite-pair attainment. This is a self-review, not independent validation. The original printed 1984 paper specifies a month but no day; the explicitly verified online-publication date of the lead source is July 14, 2006, and should not be confused with the print issue date.

## References
1. F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM J. Sci. Stat. Comput. **5** (1984), 300–304, DOI: https://doi.org/10.1137/0905021. Accessible full text: https://anthonylloyd.github.io/public/interp/pchip/A_method_for_constructing_local_monotone_picewise_cubic_interpolants_fritsch1984.pdf.
2. A. Edelman and C. A. Micchelli, *Admissible Slopes for Monotone and Convex Interpolation*, Numer. Math. **51** (1987), 441–458. Author-hosted version: https://math.mit.edu/~edelman/publications/admissible_slopes.pdf.
3. F. Aràndiga and D. F. Yáñez, *Third-order accurate monotone cubic Hermite interpolants*, Appl. Math. Lett. **94** (2019), 73–79, DOI: https://doi.org/10.1016/j.aml.2019.02.012; university repository: https://roderic.uv.es/rest/api/core/bitstreams/f9c9df53-3ff1-431d-91f5-af262fbb116b/content.
