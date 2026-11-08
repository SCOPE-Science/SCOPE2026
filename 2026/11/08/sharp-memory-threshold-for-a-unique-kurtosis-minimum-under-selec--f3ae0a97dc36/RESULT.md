# Sharp memory threshold for a unique kurtosis minimum under selective Brownian resetting

## Finding

For a coupled Brownian probe and a viscoelastic bath, with rate-\(r\) resetting of **only the probe**, stationary excess kurtosis exhibits a sharp memory-driven bifurcation. The critical bath parameter \(g_c\) is the unique positive root of
\[
22g_c^4+25g_c^3-15g_c-6=0,\qquad g_c=0.745958198386253\ldots.
\]
For every \(0<g<g_c\), the stationary excess kurtosis \(\kappa(g,r)\) has exactly one critical point for \(r>0\), a strict global minimum at \(r_*(g)\). It decreases up to this point and increases thereafter. For every \(g\geq g_c\), it increases strictly at every positive resetting rate. The minimizing rate has sharp asymptotics
\[
r_*(g)=g^{-1}-\frac56+O(g)\quad(g\downarrow0),
\qquad r_*(g)=C(g_c-g)+O((g_c-g)^2)\quad(g\uparrow g_c),
\]
where
\[
C=\frac{88g_c^3+75g_c^2-15}{g_c(60g_c^3+55g_c^2-5g_c-16)}
=2.3701769457648\ldots.
\]
For every fixed \(r>0\), excess kurtosis is strictly decreasing as the bath parameter \(g>0\) increases, even though its dependence on resetting rate can be nonmonotone. Meanwhile, the stationary probe variance is always strictly decreasing in \(r\). Thus resetting can reduce typical fluctuations while initially suppressing the excess-kurtosis shape parameter before the eventual return to the Brownian-resetting value \(3\).

## Assumptions and scope

Take independent standard Brownian motions \(W\) and \(B\) and the dimensionless stochastic differential equations between resets
\[
\mathrm dX_t=(Q_t-X_t)\,\mathrm dt+\sqrt2\,\mathrm dW_t,
\qquad
\mathrm dQ_t=g^{-1}(X_t-Q_t)\,\mathrm dt+\sqrt{2/g}\,\mathrm dB_t,
\]
for fixed \(g>0\). At independent rate-\(r\) Poisson times, with \(r>0\), set \(X\) to zero instantaneously while leaving \(Q\) unchanged. The dimensionless time and noise convention are as displayed; no simultaneous bath reset is permitted. The unique stationary law of this jump diffusion is denoted by \(\pi_{g,r}\), with
\[
M_{ij}=\int x^i q^j\,\pi_{g,r}(\mathrm dx,\mathrm dq),\qquad
\kappa(g,r)=\frac{M_{40}}{M_{20}^2}-3.
\]
All statements are for finite \(g,r>0\), with indicated one-sided limits only. At \(r=0\), the translation mode has no invariant probability distribution, so \(r=0\) is excluded from the steady-state claim. Here \(g\) is the dimensionless ratio of bath-to-probe friction timescales, not a resetting rate.

For existence and moment finiteness, inspect the embedded chain at the successive reset times. Starting with \(X=0\), the deterministic transfer of \(Q\) over a waiting time \(T>0\) is multiplication by
\[
a(T)=\frac{g+e^{-(1+1/g)T}}{g+1},\qquad 0<a(T)<1.
\]
The random Brownian increment is independent of the previous reset state, centered Gaussian conditional on \(T\), and has finite moments of every order when \(T\) is exponential. Therefore the random affine recursion admits a unique stationary law with moments of all orders: \(\mathbb E a(T)^k<1\) for each positive integer \(k\). The finite-mean regenerative clock in the extended state then gives the unique continuous-time stationary law. These arguments also justify all polynomial generator expectations below.

## Proof

**Step 1: exact stationary moments.** For \(i,j\geq0\), the stationary jump-diffusion generator applied to \(x^i q^j\) yields
\[
\begin{split}
0={}&-(i+j/g+r\mathbf1_{i>0})M_{ij}
+iM_{i-1,j+1}+(j/g)M_{i+1,j-1}\\
&+i(i-1)M_{i-2,j}+[j(j-1)/g]M_{i,j-2},
\end{split}
\]
with terms of negative index omitted and \(M_{00}=1\). Let
\[
U=g(r+1)+1,\quad V=g(r+2)+1,\quad W=g(r+2)+2,
\]
\[
H=g^3(r^3+6r^2+9r+3)+g^2(5r^2+13r+9)+g(7r+9)+3,
\]
\[
J=g^3(r^3+9r^2+26r+24)+g^2(6r^2+31r+36)+g(11r+24)+6.
\]
Solving the full degree-two and degree-four linear systems gives
\[
M_{20}=\frac{2U}{rV},\qquad M_{40}=\frac{24WH}{r^2VJ},\qquad
\kappa(g,r)=\frac{6WVH}{U^2J}-3.
\]
All the displayed denominator factors are strictly positive throughout the domain. Moreover,
\[
\partial_r M_{20}=-\frac{2(g^2r^2+2g^2r+2g^2+2gr+3g+1)}{r^2[gr+2g+1]^2}<0.
\]

**Step 2: classify every stationary point in resetting rate.** Exact differentiation and cancellation show
\[
\partial_r\kappa=\frac{6g^2 P_g(r)}{U^3J^2},\qquad P_g(r)=\sum_{j=0}^{7}p_j(g)r^j,
\]
where the complete coefficient certificate is
\[
\begin{aligned}
p_0={}&6(g+1)^2(2g+1)(22g^4+25g^3-15g-6),\\
p_1={}&6g(g+1)^2(2g+1)(60g^3+55g^2-5g-16),\\
p_2={}&g^2(g+1)(906g^4+1856g^3+1134g^2+105g-61),\\
p_3={}&g^3(682g^4+1744g^3+1542g^2+523g+49),\\
p_4={}&g^4(324g^3+647g^2+415g+86),\\
p_5={}&g^5(94g^2+131g+46),\\
p_6={}&g^6(15g+11),\qquad p_7=g^7.
\end{aligned}
\]
Each of the three nontrivial sign-controlling polynomials in \(p_2,p_1,p_0\), respectively, has **exactly one positive root** by Descartes' rule of signs. Direct exact-rational signs bracket these roots, in increasing order, by
\[
(1/10,1/5),\qquad (2/5,1/2),\qquad (7/10,3/4).
\]
The third root is \(g_c\). For \(0<g<g_c\), the coefficient signs of \(P_g\), when ordered from the constant term upward, undergo precisely one negative-to-positive change. Its constant term is negative and leading coefficient is positive. Descartes' rule applied to \(P_g\) thus yields **exactly one** positive real root, counted with multiplicity. The derivative switches from negative to positive there, proving unique strict global minimality. For \(g\geq g_c\), all nonconstant coefficients are positive and the constant coefficient is nonnegative, hence \(\partial_r\kappa>0\) for every \(r>0\). No other critical points exist.

**Step 3: strict bath-parameter dependence.** Another exact differentiation gives
\[
-\partial_g\kappa=\frac{6g\,S_g(r)}{U^3J^2},
\]
where \(S_g(r)=\sum_{j=0}^7 s_j(g)r^j\) has the following **entire** coefficient certificate:
\[
\begin{aligned}
s_0={}&72(g+1)^4(2g+1)^2,\\
s_1={}&6(g+1)(144g^5+540g^4+713g^3+430g^2+119g+12),\\
s_2={}&2g(g+1)(616g^4+1926g^3+1962g^2+835g+132),\\
s_3={}&g^2(1052g^4+3476g^3+4083g^2+2051g+386),\\
s_4={}&g^3(554g^3+1360g^2+1085g+288),\\
s_5={}&g^4(173g^2+283g+116),\\
s_6={}&g^5(29g+24),\qquad s_7=2g^6.
\end{aligned}
\]
These have strictly positive values for all \(g>0\); therefore \(\partial_g\kappa<0\) at every \(g,r>0\). The boundary values are
\[
\lim_{g\downarrow0}\kappa(g,r)=3,
\qquad \lim_{g\to\infty}\kappa(g,r)
=\frac{3r(r^3+7r^2+15r+11)}{(r+1)^2(r+3)(r+4)},
\]
where the latter is less than \(3\), as its gap equals
\[
\frac{6(r^3+6r^2+10r+6)}{(r+1)^2(r+3)(r+4)}>0.
\]
Thus kurtosis is an injective monotone memory observable at any fixed positive resetting rate.

**Step 4: sharp endpoint laws.** As \(g\downarrow0\), set \(z=gr\). The exact polynomial has the uniform coefficientwise expansion
\[
P_g(z/g)=(z-1)(z+1)^2(z+2)^2(z+3)^2+g\,Q(z)+O(g^2),
\]
for a polynomial \(Q\), with \(-Q(1)/P_0'(1)=-5/6\). Because the limiting positive root \(z=1\) is simple, the implicit-function theorem and uniqueness in Step 2 give \(z_*(g)=1-5g/6+O(g^2)\), hence the stated \(r_*(g)\) expansion. Near \(g_c\), \(P_{g_c}(0)=0\) and its \(r\)-coefficient is strictly positive; the implicit-function theorem gives
\[
r_*(g)=-\frac{\partial_g P_g(0)|_{g_c}}{\partial_r P_{g_c}(0)}(g-g_c)
+O((g-g_c)^2),
\]
which simplifies to the stated positive \(C\). As \(r\to\infty\), \(\kappa(g,r)\to3\); as \(r\downarrow0\), the one-sided limit is \(3(2g+1)/(2g^2+2g+1)\). These limits complete the global comparisons.

## Verification

`verify.py` regenerates the degree-two and degree-four moment linear systems, recomputes all eight rate-derivative coefficients, checks the exact positive-root sign structure and rational root brackets, verifies every coefficient of the bath derivative, verifies boundary limits and both optimizer asymptotics, and solves forty separate exact-rational moment systems. Run from this package using `python -m pip install -r requirements.txt` followed by `python verify.py`. The executable is a reproducible exact symbolic consistency check, not a substitute for the mathematical argument above. All statements involving a continuum of parameters follow from the displayed algebraic sign proof and Descartes' rule, not a finite parameter sweep.

## Relationship to prior work

Santra and Das (first publicly posted March 17, 2026) introduced the same probe-only resetting model and computed the stationary excess-kurtosis expression, its limiting regimes and a parameter-plane visualization. Those formulas and the selective-resetting mechanism are prior work, not claimed new. The present result is the global **one-critical-point versus no-critical-point** classification in resetting frequency, the exact quartic boundary, strict monotone dependence on bath memory, and the endpoint laws for the unique minimizing frequency. These do not appear as stated classifications in the inspected modeling, instantaneous-resetting, kurtosis-appendix and concluding sections. Algebraic specialization of the original exact moment formula is closely related, so a prior unnoticed optimization or an implication hidden in other literature remains a publication-priority risk.

Earlier viscoelastic-resetting work (arXiv:2412.09260) includes protocols that renew the memory variable at a reset; those renewal conditions do not imply the selective-resetting result by direct substitution. Classical memoryless Brownian resetting is recovered here as the limit \(g\downarrow0\); its constant excess kurtosis is not a reentrant-minimum theorem. General polynomial sign tools and moment-generator equations are standard; the claim is their exact combined classification for this nonrenewal physical model, not invention of those tools.

## Limitations

The theorem assumes linear Gaussian two-coordinate dynamics, equal dimensionless thermal-noise normalization as displayed, probe-only instantaneous Poisson resets to zero, positive finite parameters, and a stationary observation. It does not cover noninstantaneous return, nonlinear memory, general viscoelastic kernels, first-passage optimization or experimental feedback costs. The quartic threshold has no claim of universality outside this model. The steady state at zero reset rate does not exist; only one-sided limits are asserted there. An independent scientific audit has not been performed, and related but unlocated treatments of this exact stationary-kurtosis extremum may affect publication priority.

## References

1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1 (first public date 2026-03-17), https://arxiv.org/abs/2603.17027 ; published in *New Journal of Physics* **28**, 074601 (2026), DOI:10.1088/1367-2630/ae868c.
2. *Viscoelastic stochastic resetting with memory renewal*, arXiv:2412.09260 (2024), https://arxiv.org/abs/2412.09260 (compare resetting conventions only).
