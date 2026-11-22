# The first screened wheel with a hub-to-rim two-landmark transition

## Finding

Let \(W_{m+1}=K_1\vee C_m\) be the simple unweighted wheel with \(m\ge3\) rim vertices and hub \(h\). For every screening strength \(\mu>0\), put \(A_\mu=\mu I+L(W_{m+1})\) and \(K_\mu=A_\mu^{-1}\). Given two distinct noiseless landmarks \(S\), minimize the residual-trace Nyström error
\[
E_\mu(S)=\operatorname{tr}\!\left(K_\mu-K_{\mu,:,S}(K_{\mu,S,S})^{-1}K_{\mu,S,:}\right).
\]
The full result is as follows.

1. For \(m=3\), all six pairs tie at every \(\mu>0\).
2. For \(4\le m\le6\), the *only* minimizers, for every \(\mu>0\), are pairs of rim vertices at maximum cyclic separation \(\lfloor m/2\rfloor\). The respective numbers of optimal pairs are \(2,5,3\).
3. For \(m=7\), define
\[
\begin{aligned}
P(x)={}&2x^{10}+57x^9+712x^8+5106x^7+23107x^6+68172x^5\\
&+130255x^4+153158x^3+95916x^2+17226x-6931.
\end{aligned}
\]
There is exactly one positive zero \(\alpha=0.175354708826\ldots\) of \(P\). For \(0<\mu<\alpha\), the seven hub–rim pairs are exactly the minimizers. At \(\mu=\alpha\), those seven pairs and the seven rim–rim pairs at cyclic separation three, fourteen sets altogether, are precisely the minimizers. For \(\mu>\alpha\), precisely the seven maximally separated rim pairs minimize the error.
4. For every \(m\ge7\), there are positive constants \(\varepsilon_m\) and \(M_m\) such that every optimal pair contains the hub for \(0<\mu<\varepsilon_m\), whereas no optimal pair contains the hub for \(\mu>M_m\). The assertion for arbitrary \(m\) is an existence statement; it neither asserts a unique crossover nor classifies the intermediate screening range when \(m\ge8\).

Thus the wheel with seven rim vertices is the smallest wheel whose globally optimal *two-point* selection switches from a hub-containing pair to a hub-avoiding pair as uniform positive screening varies. The exact boundary and all tie cases are determined at that first occurrence.

## Assumptions and scope

The rim is a simple cycle of size \(m\), the spoke and rim conductances all equal one, the screening \(\mu\) is uniform and strictly positive, and exactly two distinct vertices are observed without observation noise. The error is an unscaled covariance residual trace; it is also an inverse-trace criterion for the unobserved precision block. Nothing is claimed for unequal conductances, more than two landmarks, alternative matrix functions, or noisy observations.

For a pair \(S\), let \(U=V(W_{m+1})\setminus S\), and set \(p_S(x)=\det(xI+L(W_{m+1})_{UU})\). This principal submatrix notation means that the full original vertex degrees are retained before taking the submatrix. It has size \(m-1\).

## Proof

**1. Exact conditional-precision reduction.** The block inverse identity for a positive-definite precision matrix says
\[
K_{UU}-K_{US}K_{SS}^{-1}K_{SU}=(A_{UU})^{-1}.
\]
Therefore \(E_x(S)=\operatorname{tr}((xI+L_{UU})^{-1})=p'_S(x)/p_S(x)\), the final identity following from Jacobi's determinant derivative. Because the wheel is connected and \(S\ne\varnothing\), every grounded Laplacian \(L_{UU}\) is positive definite. Hence \(p_S(x)>0\) for \(x\ge0\).

Dihedral symmetry reduces the possibilities to \(H=\{h,v_1\}\) and \(R_d=\{v_1,v_{1+d}\}\), \(1\le d\le\lfloor m/2\rfloor\). Here rim indices are cyclic. For any two types \(X,Y\),
\[
E_x(X)-E_x(Y)=\frac{Q_{X,Y}(x)}{p_X(x)p_Y(x)},\quad Q_{X,Y}=p'_Xp_Y-p_Xp'_Y.
\]
The sign is therefore decided by an integer polynomial.

**2. Complete exact small-wheel comparison.** The determinant polynomials \(p_H,p_{R_d}\), as integer coefficient arrays in ascending powers, and the analogous arrays for every comparison numerator \(Q_{H,R_{\lfloor m/2\rfloor}}\) and \(Q_{R_d,R_{\lfloor m/2\rfloor}}\), are given completely in `certificates.json`. The independent standard-library program `verify_screened_wheel.py` obtains these coefficients anew from integer grounded-matrix determinants and checks all arrays, rather than relying on stored comparison outputs. Every coefficient in every nonzero comparison numerator for \(4\le m\le6\) is strictly positive. The same holds for rim separations smaller than three when \(m=7\). This proves the exact global classifications for \(m\le6\) and reduces the \(m=7\) problem to comparing \(H\) with \(R_3\). The case \(m=3\) is the complete graph \(K_4\), so every pair is equivalent.

For clarity, the two \(m=7\) grounded determinant polynomials factor as
\[
\begin{aligned}
p_H(x)={}&(x^3+8x^2+19x+13)(x^3+10x^2+31x+29),\\
p_{R_3}(x)={}&(x+3)(x+4)(x^4+15x^3+70x^2+116x+58).
\end{aligned}
\]
Exact multiplication and differentiation yield \(Q_{H,R_3}(x)=2P(x)\). Since the coefficients of every positive power of \(x\) in \(P\) are strictly positive while the constant term is \(-6931\), the polynomial is strictly increasing on \([0,\infty)\), starts negative, and tends to positive infinity. It therefore has exactly one positive zero. Exact rational evaluation places it in
\[
\frac{1753547088}{10^{10}}<\alpha<\frac{1753547089}{10^{10}}.
\]
The sign of \(Q\) and the strict positivity of all other rim-versus-\(R_3\) numerators establish all three regimes and all equality sets. In particular the threshold is not inferred from floating-point sampling.

**3. Why the hub wins for small screening on every larger wheel.** We give a self-contained strict unscreened comparison, which also appears as a special wheel leader-selection result in the cited literature. At \(x=0\) define \(T_\ell\) to be the \(\ell\)-vertex tridiagonal matrix with diagonal three and neighboring entries minus one, and put
\[
h_\ell=\operatorname{tr}(T_\ell^{-1}),\quad
f_\ell={\bf1}^{\mathsf T}T_\ell^{-1}{\bf1},\quad
g_\ell=\lVert T_\ell^{-1}{\bf1}\rVert^2
\]
with all three zero at \(\ell=0\). Grounding a hub–rim pair leaves a single path, hence \(E_0(H)=h_{m-1}\). Grounding \(R_d\) leaves two rim paths of lengths \(a=d-1\), \(b=m-d-1\), and one hub. A Schur complement gives
\[
E_0(R_d)=h_a+h_b+\frac{1+g_a+g_b}{m-f_a-f_b}.\tag{1}
\]
The denominator is strictly positive by grounded positive definiteness.

For \(m=7,8\), exact rational evaluation of (1) yields respectively
\[
\begin{array}{c|c|c}
m&E_0(H)&(E_0(R_1),\ldots,E_0(R_{\lfloor m/2\rfloor}))\\\hline
7&954/377&(383/116,885/319,31/12)\\
8&2939/987&(4927/1218,1451/420,425/132,221/70).
\end{array}
\]
Both rows have the hub–rim value strictly below every rim–rim value. These exact checks also follow by substituting zero into the determinants in the independent verifier.

For \(m\ge9\), write \(r=(3+\sqrt5)/2\). Standard inversion of \(T_\ell\), obtained by solving the recurrence with zero endpoint values, gives
\[
(T_\ell^{-1})_{ii}=\frac{(1-r^{-2i})(1-r^{-2(\ell+1-i)})}{\sqrt5(1-r^{-2(\ell+1)})},\qquad
(T_\ell^{-1}{\bf1})_i=1-\frac{r^i+r^{\ell+1-i}}{r^{\ell+1}+1}.
\]
Summing these formulas yields, for all \(\ell\ge0\),
\[
\frac{\ell-2/(r^2-1)}{\sqrt5}\le h_\ell\le\frac\ell{\sqrt5},\qquad
f_\ell\ge\ell-\frac{2}{r-1}.
\]
In (1) this gives \(m-f_a-f_b\le2\sqrt5\), \(f_a+f_b\ge m-2\sqrt5>0\); by Cauchy–Schwarz \(g_a+g_b\ge(f_a+f_b)^2/(m-2)\). Consequently
\[
E_0(R_d)-E_0(H)\ge
\frac{1+(m-2\sqrt5)^2/(m-2)}{2\sqrt5}
-\frac{1+4/(r^2-1)}{\sqrt5}>0.
\]
The last expression is increasing for real \(m\ge9\), and at \(m=9\) equals \((61\sqrt5-132)/35>0\). Thus the hub–rim type strictly beats *all* rim pairs for every \(m\ge7\) at zero screening. By continuity and finitely many pair orbits, the same strict preference persists on a nonempty positive interval \((0,\varepsilon_m)\).

**4. High screening reverses the preference.** For each fixed \(m\), the convergent large-\(x\) matrix expansion gives
\[
E_x(S)=\frac{m-1}{x}-\frac{\operatorname{tr}L_{UU}}{x^2}+O_m(x^{-3}).
\]
The wheel degree sum is \(4m\). Deleting a hub and rim vertex removes degrees \(m+3\), whereas deleting two rim vertices removes degree sum six. Hence for every rim pair \(R_d\),
\[
E_x(H)-E_x(R_d)=\frac{m-3}{x^2}+O_m(x^{-3})>0
\]
for sufficiently large \(x\) when \(m>3\). There are finitely many pair orbits; one threshold \(M_m\) therefore works simultaneously for all of them. This completes the all-size existence assertion and, together with Step 2, the minimal-wheel characterization.

## Verification

Run `python3 verify_screened_wheel.py` with Python 3.9 or later. It requires no third-party libraries. It reconstructs all orbit determinants by integer fraction-free elimination and exact Newton interpolation, checks the complete integer polynomial certificate and sharp root isolator, tests the determinant-derivative identity against exact rational inversions, and exhaustively identifies optimal two-subsets for \(3\le m\le7\) at six positive rational screening strengths. The all-\(m\) statements are proved analytically in Steps 3–4; the finite checker is not presented as an infinite exhaustive certificate.

## Relationship to prior work

Lin, Fardad and Jovanović (2013) introduced general inverse-trace leader-selection formulations and optimization relaxations. Fitch and Leonard (2014) derived graph-based joint-centrality formulas and exact path/cycle leader examples. Belabbas and Wolfe (2009) developed the Nyström landmark-error framework. A separate published exact zero-screening wheel result already classifies the \(\mu=0\) case, including the seven-rim threshold. The present theorem does *not* claim that result as new: it proves a distinct strictly positive screening phase transition, determines its first exact transition polynomial and all critical equality cases, and establishes hub avoidance in the strongly screened regime. General evaluation formulas do not imply the above screening-dependent all-pair optimality classifications without the explicit comparisons.

## Limitations

Only seven-rim screening has a proven unique crossing in this work. For \(m\ge8\), the existence of a hub-to-rim reversal does not prove there is just one crossing or that the optimal rim separation is always maximal. The result is specific to unit-conductance wheels, uniform positive screening and two noiseless landmarks. The originality comparison is based on the identified inspected sources, not an exhaustive priority guarantee. Independent mathematical validation has not been carried out.

## References

1. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450v1, first publicly posted 2013-02-03. https://arxiv.org/abs/1302.0450
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569v1, first publicly posted 2014-07-07. https://arxiv.org/abs/1407.1569
3. M.-A. Belabbas and P. J. Wolfe, *On Landmark Selection and Sampling in High-Dimensional Data Analysis*, arXiv:0906.4582v1, first publicly posted 2009-06-24. https://arxiv.org/abs/0906.4582
4. *Sharp hub-leader transition for two noise-free leaders on wheel graphs*, public mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-hub-leader-transition-for-two-noise-free-leaders-on-wheel--8f7b91d540d5
