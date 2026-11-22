# Sharp three-site stability and a mesh–power boundary layer for generalized Floater–Hormann interpolation

## Finding
Let \(\gamma\geq1\) be any integer. For the degree-one generalized Floater–Hormann interpolation operator on three ordered sites, the middle site uniquely minimizing the \(\ell^\infty\)-data-to-\(L^\infty\)-function Lebesgue norm is the midpoint. The exact minimal norm and the sharp overshoot of bounded monotone data are
\[
\boxed{\min_{0<a<1}\Lambda_\gamma(a)=1+2\delta_\gamma,\qquad
\delta_\gamma=\frac{1-t_\gamma}{1+t_\gamma}\frac{t_\gamma^\gamma}{1+t_\gamma^\gamma},}
\]
where \(t_\gamma\in(0,1)\) is the unique solution of
\[
\boxed{\gamma(1-t_\gamma^2)=2t_\gamma(1+t_\gamma^\gamma).}
\]
The sites have been affinely normalized to \(0,a,1\). For every \(a\), the largest negative excursion below \(0\) and positive excursion above \(1\), over all nondecreasing nodal triples in \([0,1]\), are bounded by \((\Lambda_\gamma(a)-1)/2\), and this bound is attained by a one-jump triple. At the optimal midpoint grid, both signs attain the defect \(\delta_\gamma\).

The exact constants start with \(\Lambda_1^{\min}=5/4\), and \(\Lambda_2^{\min}=1.134884497736\ldots\). They strictly decrease as \(\gamma\) increases, with the sharp law
\[
\boxed{\lim_{\gamma\to\infty}\gamma(\Lambda_\gamma^{\min}-1)=W(e^{-1})=0.278464542761\ldots,}
\]
where \(W\) is the positive real Lambert function, defined by \(W(z)e^{W(z)}=z\).

The limiting geometry is singular. For any fixed off-center \(a\in(0,1)\),
\[
\boxed{\lim_{\gamma\to\infty}\Lambda_\gamma(a)=\frac1{\min\{a,1-a\}}-1.}
\]
For a moving site \(a_\gamma=1/2+\beta/\gamma\), with any fixed real \(\beta\), the complete inner transition is
\[
\boxed{\lim_{\gamma\to\infty}\gamma\bigl(\Lambda_\gamma(a_\gamma)-1\bigr)
=W\bigl(e^{4|\beta|-1}\bigr).}
\]
Consequently an increased blending power suppresses amplification at the exactly balanced grid, but an off-center site retained at fixed displacement has a nontrivial limiting amplification.

## Assumptions and scope
The input is a real triple \(y=(y_0,y_1,y_2)\) at nodes \(0<a<1\), with interpolation degree \(d=1\) and the generalized blending exponent \(\gamma\in\{1,2,\ldots\}\). Denote by \(p_0\) the line interpolating \((0,y_0),(a,y_1)\), and by \(p_1\) the line interpolating \((a,y_1),(1,y_2)\). The generalized Floater–Hormann rule is
\[
R_\gamma[y](x)=\frac{\lambda_0(x)p_0(x)+\lambda_1(x)p_1(x)}{\lambda_0(x)+\lambda_1(x)},\quad
\lambda_0(x)=\frac1{[x(x-a)]^\gamma},\quad
\lambda_1(x)=\frac{(-1)^\gamma}{[(x-a)(x-1)]^\gamma},
\]
with continuous values at the nodes. The Lebesgue norm is
\[
\Lambda_\gamma(a)=\sup_{y\ne0}\frac{\|R_\gamma[y]\|_{L^\infty[0,1]}}{\max_j|y_j|}.
\]
Its value and all results are invariant under translating and positively rescaling the three abscissae. No restriction to monotone input is made in defining the Lebesgue norm; monotonicity is used only for the equivalent one-sided range-defect statement. Only three distinct sites and a fixed first-degree blend are considered.

## Proof
**Positive blending representation.** Cancellation of the common factor \((x-a)^\gamma\) gives
\[
R_\gamma[y](x)=(1-w_\gamma(x))p_0(x)+w_\gamma(x)p_1(x),\qquad
w_\gamma(x)=\frac{x^\gamma}{x^\gamma+(1-x)^\gamma}.
\]
This identity holds on \([0,1]\) by continuous extension, for both parities of the integer \(\gamma\). Thus the cardinal coefficients of \(y_0,y_1,y_2\) are
\[
\ell_0=(1-w_\gamma)(1-x/a),\quad
\ell_1=(1-w_\gamma)x/a+w_\gamma(1-(x-a)/(1-a)),\quad
\ell_2=w_\gamma(x-a)/(1-a).
\]
They sum to one. For \(0<x<a\), exactly \(\ell_2\) is negative; for \(a<x<1\), exactly \(\ell_0\) is negative. The other coefficients are nonnegative. Therefore
\[
\Lambda_\gamma(a)=1+2\max\{H_\gamma(a),H_\gamma(1-a)\},
\quad H_\gamma(a)=\max_{0\le x\le a}\frac{(a-x)w_\gamma(x)}{1-a}.
\tag{1}
\]
For bounded nondecreasing nodal data \(0\le y_0\le y_1\le y_2\le1\), the extremal left-cell negative value is obtained by \((0,0,1)\), and the extremal right-cell excess above one is obtained by \((0,1,1)\). These follow either by the displayed signs or by checking the four vertices \((0,0,0),(0,0,1),(0,1,1),(1,1,1)\) of the monotone-data polytope. Hence the sharp monotone range defect equals \((\Lambda_\gamma(a)-1)/2\), not just an upper bound.

**Unique cell maximum and unique optimal grid.** On \((0,a)\), differentiation gives the sign of \(H\)'s objective as that of \(K_\gamma(x;a)-1\), where
\[
K_\gamma(x;a)=\frac{\gamma(a-x)}{x(1-x)}\cdot\frac1{1+(x/(1-x))^\gamma}.
\]
The factor \((a-x)/(x(1-x))\) strictly decreases because its logarithmic derivative is
\[
-\frac1{a-x}-\frac1x+\frac1{1-x}<0
\]
for \(x<a<1\). The final factor also strictly decreases; \(K_\gamma\) falls from infinity to zero. Consequently the objective has exactly one interior maximum. Independently, \(H_\gamma(a)\) is strictly increasing as a function of \(a\): for every fixed \(x<a\), the factor \((a-x)/(1-a)\) increases strictly, and increasing \(a\) enlarges the admissible interval. By reflection, \(H_\gamma(1-a)\) decreases strictly. Equation (1) therefore has its unique global minimum at \(a=1/2\).

**Exact midpoint constant.** At \(a=1/2\), put \(t=x/(1-x)\) for \(0<x<1/2\). Then
\[
H_\gamma(1/2)=\max_{0<t<1}\frac{1-t}{1+t}\frac{t^\gamma}{1+t^\gamma}.
\]
The logarithmic derivative vanishes exactly when \(\gamma(1-t^2)=2t(1+t^\gamma)\). The left-hand side strictly decreases from \(\gamma\) to zero, while the right-hand side strictly increases from zero to four, yielding a unique root and the first boxed formula. Since \(t^\gamma/(1+t^\gamma)\) strictly decreases with \(\gamma\) for each \(0<t<1\), the unique attained maximum \(\delta_\gamma\) strictly decreases in \(\gamma\). Substituting \(\gamma=1\) gives \(t_1=1/3\) and \(\delta_1=1/8\).

**Sharp centered high-power law.** The root equation first forces \(t_\gamma\to1\). Put \(u_\gamma=\gamma(1-t_\gamma)\). The same equation gives a positive lower bound and an upper bound on \(u_\gamma\) (indeed \(1+o(1)\le u_\gamma\le2+o(1)\)). Along any convergent subsequence, \(t_\gamma^\gamma\to e^{-u}\), so the root equation implies \(u=1+e^{-u}\). Its unique solution is \(u=1+W(e^{-1})\). Thus
\[
\gamma\delta_\gamma\longrightarrow
\frac{u}{2}\frac{e^{-u}}{1+e^{-u}}=\frac12W(e^{-1}),
\]
proving the asserted scaling of the optimal Lebesgue norm.

**Fixed off-center grid.** Suppose \(a<1/2\). In \(H_\gamma(a)\), the weight \(w_\gamma\) tends uniformly to zero on \([0,a]\), hence \(H_\gamma(a)\to0\). In \(H_\gamma(1-a)\), the weight tends to the indicator of \(x>1/2\), and its weighted objective has maximum tending to \((1/2-a)/a\): for a lower bound evaluate at \(x=1/2+\varepsilon\), and for an upper bound split the domain into \(x\le1/2-\varepsilon\) (uniform exponentially small weight) and \(x>1/2-\varepsilon\) (at most \((1/2-a+\varepsilon)/a\)); then let \(\varepsilon\downarrow0\). Equation (1) yields \(\Lambda_\gamma(a)\to1/a-1\). Reflection covers \(a>1/2\), and the centered limit covers equality.

**Moving-mesh boundary layer.** Fix \(\beta\in\mathbb R\), set \(a_\gamma=1/2+\beta/\gamma\) and \(x=1/2+z/\gamma\). On the left cell the objective in (1), multiplied by \(\gamma\), tends at each fixed \(z<\beta\) to
\[
F_\beta(z)=\frac{2(\beta-z)}{1+e^{-4z}}.
\]
The convergence of maxima follows by compact convergence plus uniform tail bounds: as \(z\to-\infty\), the weight is bounded by \(e^{4z}\), whereas the prefactor grows at most linearly; at \(z\uparrow\beta\), the prefactor vanishes. Every maximizer remains in a fixed compact subset of \(( -\infty,\beta)\). The unique maximum of \(F_\beta\) satisfies
\[
4(\beta-z)=1+e^{4z}.
\]
Writing \(v=e^{4z}\) gives \(ve^v=e^{4\beta-1}\), so
\[
\max_{z<\beta}F_\beta(z)=\tfrac12W(e^{4\beta-1}).
\]
The reflected cell has the same limit with \(\beta\) replaced by \(-\beta\). Since the real principal \(W\) is strictly increasing, (1) gives
\[
\lim_{\gamma\to\infty}\gamma(\Lambda_\gamma(a_\gamma)-1)
=W(e^{4|\beta|-1}).
\]
This concludes all quantifiers and boundary regimes.

## Verification
Run `python3 checker.py` with Python 3; it uses only the standard library. The program reconstructs the generalized signed local blending formula with exact `Fraction` arithmetic for positive integer exponents, checks representative cardinal identities, sign and partition-of-unity identities, unique central-node minimax comparisons and known exact constants, and evaluates fixed-mesh and moving-mesh limits. It prints its explicit test count and numerical constants. All continuous/global statements, strict uniqueness claims, and infinite-power limits are proved analytically above; finite tests are only corroborative.

## Relationship to prior work
Themistoclakis and Van Barel introduced the generalized Floater–Hormann blending exponent in arXiv:2307.05345 (first public July 11, 2023), established no-real-pole interpolation, and derived general Lebesgue estimates. Their 2024 open-access sequel treats error bounds for arbitrary node distributions. Neither inspected full-text analysis identifies the exact minimal three-site Lebesgue norm, its sharp monotone-data range defect, the globally optimal interior-node placement, or the noncommuting mesh–power limits. Their general mesh-ratio estimate is not a sharp statement of any of these quantities.

The original Floater–Hormann degree-one rule at \(\gamma=1\) is a polynomial for three nodes, so its classical midpoint-node Lebesgue constant is background, not the claimed novelty. A published four-node degree-one classical Floater–Hormann monotone-range computation (different exponent and data cardinality) and a three-site Shepard total-variation theorem (positive Shepard weights, different operator and seminorm) provide adjacent but not implication-dominating statements. An exact three-knot natural-cubic positivity defect has a similar one-negative-cardinal mechanism but a different spline basis and does not imply the present power-dependent constants or limits.

## Limitations
The result concerns the smallest nontrivial degree-one generalized blend only. It does not establish corresponding stability for longer node sets or higher blending degrees; in particular, \(\gamma\to\infty\) here changes the scheme with the exponent, not the approximation accuracy of a refined many-node sequence. The sharp numerical facts are exact-arithmetic properties of the interpolation operator, not bounds on floating-point implementation error. Historical priority remains provisional because the broader rational shape-preserving literature may contain an equivalent result under a different interpolation-operator name.

## References
1. W. Themistoclakis and M. Van Barel, *A generalization of Floater–Hormann interpolants*, arXiv:2307.05345, first publicly submitted July 11, 2023, https://arxiv.org/abs/2307.05345 (full HTML text inspected).
2. W. Themistoclakis and M. Van Barel, *A note on generalized Floater–Hormann interpolation at arbitrary distributions of nodes*, published online September 17, 2024, DOI: 10.1007/s11075-024-01933-6, https://link.springer.com/article/10.1007/s11075-024-01933-6 (full open-access HTML inspected).
3. M. S. Floater and K. Hormann, *Barycentric Rational Interpolation with No Poles and High Rates of Approximation*, Numerische Mathematik 107 (2007), 315–331, DOI: 10.1007/s00211-007-0093-y (original construction).
4. *Sharp monotone range defect of four-point degree-one Floater–Hormann interpolation*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-monotone-range-defect-of-four-point-degree-one-floater-hor--588356639a12 (full result read).
5. *Sharp bounded-variation stability of three-site Shepard interpolation and its mesh–power boundary layer*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-bounded-variation-stability-of-three-site-shepard-interpol--a6803f77c76f (full result read).
