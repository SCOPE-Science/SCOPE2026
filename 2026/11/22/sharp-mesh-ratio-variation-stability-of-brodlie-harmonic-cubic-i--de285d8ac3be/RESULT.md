# Sharp mesh-ratio variation stability of Brodlie harmonic cubic interpolation

## Finding
On a fixed, locally finite, strictly increasing bi-infinite real knot grid, let \(\mathcal H\) be the \(C^1\) piecewise-cubic interpolant using the nonuniform Brodlie–Fritsch–Butland *weighted harmonic mean* of the two adjacent secant slopes at each knot. For real nodal data with summable adjacent increments, it preserves each input's total variation exactly, yet its **sharp two-input variation Lipschitz coefficient** is
\[
\boxed{K(\boldsymbol h)=1+\frac8{27}\sup_{j\in\mathbb Z}\left[\Phi\!\left(\frac{h_{j-1}}{h_j}\right)+\Phi\!\left(\frac{h_{j+1}}{h_j}\right)\right],\qquad \Phi(r)=\frac{3r(1+r)}{1+2r}.}
\]
Here the value \(+\infty\) is allowed. The interpolant is globally two-input Lipschitz in variation **if and only if** the adjacent mesh-length ratios are uniformly bounded. On a uniform grid \(K=59/27\). The sharp value is a supremum approached by arbitrarily shallow interior steps surrounded by steeper neighbors, not attained by any distinct pair when \(K<\infty\). The cell-local contribution for three consecutive lengths \((2,1,3)\) is exactly \(377/105\), distinct from the corresponding nonuniform Steffen-limiter contribution \(107/27\).

## Assumptions and scope
Let \((x_j)_{j\in\mathbb Z}\) be strictly increasing, with \(x_j\to\pm\infty\) as \(j\to\pm\infty\), and positive lengths \(h_j=x_{j+1}-x_j\). For real data \(y=(y_j)\), put
\[
\delta_j(y)=\frac{y_{j+1}-y_j}{h_j},\quad V_d(y)=\sum_{j\in\mathbb Z}h_j|\delta_j(y)|<\infty.
\]
At knot \(j\), write \(\ell=h_{j-1}\), \(r=h_j\), \(a=\delta_{j-1}\), \(b=\delta_j\), and set
\[
m_j=\begin{cases}
\displaystyle\frac{3(\ell+r)ab}{(2r+\ell)b+(r+2\ell)a},&ab>0,\\[4pt]
0,&ab\le0.
\end{cases}
\]
This is the Brodlie weighted harmonic mean, with the conventional signed extension for decreasing data. On \([x_j,x_{j+1}]\), with \(u=(x-x_j)/h_j\), the interpolant is
\[
(\mathcal Hy)(x)=y_j+h_j\left[\delta_j S(u)+m_j A(u)+m_{j+1}B(u)\right],
\]
where \(S(u)=3u^2-2u^3\), \(A(u)=u(1-u)^2\), and \(B(u)=u^3-u^2\). Continuous variation means \(V_c(f)=\int_{\mathbb R}|f'(x)|\,dx\). The quotient used to define \(K\) is \(\sup_{V_d(y-z)>0}V_c(\mathcal Hy-\mathcal Hz)/V_d(y-z)\). Knots are the same for both inputs. No finite-interval PCHIP endpoint-derivative formula is asserted.

## Proof
**1. Exact cell geometry.** On the normalized cell,
\[
S'=6u(1-u),\quad A'=1-4u+3u^2,\quad B'=-2u+3u^2.
\]
For any \(0\le a,b\le3\), the polynomial \(S'+aA'+bB'\) is nonnegative on \([0,1]\). Indeed, dependence on \((a,b)\) is affine, and at the four corners \((0,0),(3,0),(0,3),(3,3)\) its values are, respectively, \(6u(1-u)\), \(3(1-u)^2\), \(3u^2\), and \(3(2u-1)^2\). Its integral is one. Also \(A\) and \(B\) vanish at both ends, and have signed extrema \(4/27\) and \(-4/27\), so
\[
\int_0^1|A'(u)|\,du=\int_0^1|B'(u)|\,du=\frac8{27}.
\]
**2. Single-input variation.** The selected knot derivative has the sign of each nonzero adjacent secant and satisfies \(|m_j|\le3\min(|\delta_{j-1}|,|\delta_j|)\). When a cell secant is zero, both its endpoint derivatives vanish. The cell polynomial is therefore monotone between its nodal values by step 1, and its variation is \(h_j|\delta_j|\). Summing yields \(V_c(\mathcal Hy)=V_d(y)\).

**3. Sharp incremental bound.** For fixed neighboring lengths \(\ell,r>0\), the weighted harmonic selector is locally Lipschitz in both secants. On a same-sign quadrant its partial derivatives are nonnegative. For the *right* secant \(b\), the derivative is
\[
\partial_b m=\frac{3(\ell+r)(r+2\ell)a^2}{[(2r+\ell)b+(r+2\ell)a]^2}\le\frac{3(\ell+r)}{r+2\ell},
\]
and for the *left* secant \(a\), the derivative is bounded by \(3(\ell+r)/(2r+\ell)\); in other sign quadrants the partial derivatives vanish. The selector is absolutely continuous along any single-coordinate line, and these bounds hold almost everywhere. Both bounds are strictly less than three. They are sharp only as the varied secant tends to zero against a nonzero same-sign neighbor.

Hold all secants fixed except \(\delta_j\), and differentiate the interpolant against that secant at almost every admissible point. Denote the responses at knots \(j\) and \(j+1\) by \(a_j,b_j\in[0,3]\). Apart from constant translations, its derivative on the three affected cells \(j-1,j,j+1\), in their respective unit coordinates, is the scalar response \(a_jB'\), \(S'+a_jA'+b_jB'\), \(b_jA'\), respectively. Hence its *exact* continuous variation per unit change in \(\delta_j\) is
\[
h_j+\frac8{27}\left(h_{j-1}a_j+h_{j+1}b_j\right)
\le h_j\left[1+\frac8{27}\left\{\Phi\!\left(\frac{h_{j-1}}{h_j}\right)+\Phi\!\left(\frac{h_{j+1}}{h_j}\right)\right\}\right].
\]
The equality before the inequality uses **the actual monotonicity of the central response**, rather than a triangle inequality on its three Hermite basis terms.

For finitely many changed secants, vary them successively along their connecting line segments, integrate the almost-everywhere directional bounds, and apply the variation triangle inequality. To handle infinitely many changed secants, truncate to a finite set, anchoring one nodal value; the differences of secants are absolutely summable after multiplication by \(h_j\). The resulting interpolants converge locally modulo additive constants, and lower semicontinuity of variation gives the asserted global upper bound when the displayed supremum is finite. The same finite-column argument remains valid without the finiteness assumption.

**4. Sharpness.** Fix \(j\). Take data with \(\delta_{j-1}=\delta_{j+1}=1\), \(\delta_j=0\), and all other secants zero; then change only \(\delta_j\) to \(\varepsilon>0\), keeping a nodal anchor fixed. The input-difference variation is \(h_j\varepsilon\). The two newly nonzero knot slopes divided by \(\varepsilon\) converge to
\[
\frac{3(h_{j-1}+h_j)}{h_j+2h_{j-1}},\qquad
\frac{3(h_j+h_{j+1})}{h_j+2h_{j+1}}.
\]
The central difference cell is monotone and has variation \(h_j\varepsilon\); the two adjacent difference cells have variations \((8/27)h_{j-1}m_j\) and \((8/27)h_{j+1}m_{j+1}\). Dividing by \(h_j\varepsilon\) and taking \(\varepsilon\downarrow0\) gives exactly the bracketed local coefficient. Now take the supremum over \(j\), establishing equality for both finite and infinite \(K\). The strictness of the derivative bounds on every nonzero finite secant perturbation also shows that no two distinct finite-variation inputs attain a finite sharp \(K\).

**5. Mesh-regularity equivalence.** The function \(\Phi\) is positive, continuous, increasing, and satisfies \(\Phi(r)/r\to3/2\) as \(r\to\infty\). Thus the displayed supremum is finite exactly when both adjacent-length ratios are uniformly bounded. For \(h_j\equiv h\), \(\Phi(1)=2\), giving \(59/27\). For ratios \(2\) and \(3\), \(\Phi(2)=18/5\), \(\Phi(3)=36/7\), giving local factor \(377/105\).

## Verification
The standalone `verify_pchip.py` reconstructs the harmonic slopes and integrates the absolute value of each cubic derivative exactly up to ordinary floating-point evaluation of its at-most-two critical points. It checks individual-input preservation and the claimed upper bound for 3,080 seeded random data/positive-mesh pairs over sizes 2–12, plus five near-flat sharpness witnesses and the analytical Hermite basis variation constants. Run with `python3 verify_pchip.py`; only the Python standard library is needed. The bi-infinite theorem and strict nonattainment are proved analytically, not inferred from finite experiments.

## Relationship to prior work
Fritsch and Butland (1984), equations (4)–(5), specify exactly the nonuniform harmonic-mean slope and show the one-input monotonicity criterion; their full text does not give a two-input total-variation coefficient or sharp mesh-ratio law. Aràndiga (2013) studies order and monotonicity on nonuniform meshes; its accessible abstract does not establish a sharp perturbation norm, but the full article was not retrieved and remains a priority risk. Aràndiga and Yáñez (2019), equations (8)–(10), review the same weighted mean and its approximation order, not a two-input variation norm. A published uniform-grid harmonic-mean variation result establishes \(59/27\) for identical cell lengths, and a separate nonuniform Steffen-limiter theorem gives \(1+(16/27)\sup_j(h_{j-1}+h_{j+1})/h_j\). Neither result implies the displayed Brodlie mesh-specific coefficient: the uniform theorem omits variable lengths and the Steffen rule is a different nonlinear mean with different derivatives. The present theorem identifies a sharp stability law for the actual nonuniform Brodlie selector; it does not claim novelty for the harmonic-mean formula itself.

## Limitations
The theorem concerns real-valued data on a *fixed* bi-infinite knot grid, with this exact interior weighted harmonic rule. It does not cover finite-interval PCHIP's one-sided endpoint-derivative prescriptions, simultaneous perturbations of the knots, vector-valued data, or other harmonic-mean variants. On severely irregular grids, single-input total variation is still preserved even though no finite uniform two-input variation Lipschitz coefficient exists. Historical priority remains qualified by the inaccessible full 2013 paper and possible unindexed equivalents. Independent audit has not been conducted.

## References
1. F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM J. Sci. Stat. Comput. 5 (1984), 300–304, https://doi.org/10.1137/0905021. Accessible full text: https://anthonylloyd.github.io/public/interp/pchip/A_method_for_constructing_local_monotone_picewise_cubic_interpolants_fritsch1984.pdf .
2. F. Aràndiga, *On the Order of Nonuniform Monotone Cubic Hermite Interpolants*, SIAM J. Numer. Anal. 51 (2013), 2613–2633, https://doi.org/10.1137/12088495X; first day-verified online appearance 2013-09-12.
3. F. Aràndiga and D. F. Yáñez, *Third-order accurate monotone cubic Hermite interpolants*, Applied Mathematics Letters 94 (2019), 73–79, https://doi.org/10.1016/j.aml.2019.02.012; lawful author repository full text https://roderic.uv.es/rest/api/core/bitstreams/f9c9df53-3ff1-431d-91f5-af262fbb116b/content .
4. F. Dubois, *Nonlinear Interpolation and Total Variation Diminishing Schemes*, arXiv:1006.3921 (first posted June 20, 2010), https://arxiv.org/abs/1006.3921.
5. *Sharp two-input bounded-variation stability of harmonic-mean cubic Hermite interpolation*, published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-two-input-bounded-variation-stability-of-harmonic-mean-cub--479993d5519d .
6. *Sharp mesh-ratio control of two-input variation for nonuniform Steffen cubic Hermite interpolation*, published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-mesh-ratio-control-of-two-input-variation-for-nonuniform-s--c024605d3664 .
