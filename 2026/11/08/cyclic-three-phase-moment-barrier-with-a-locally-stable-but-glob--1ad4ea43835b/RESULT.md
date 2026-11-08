# Cyclic three-phase moment barrier with a locally stable but globally suboptimal equal-rate design

## Finding
Let an absorption-time computation use three exponential holding stages followed by a Bernoulli return to the first stage. The normalized fourth raw-moment ratio always obeys the exact three-stage Erlang floor, but equal holding times can be strictly locally optimal and simultaneously inferior to a heterogeneous design at the same return probability.

Precisely, let \(a_1,a_2,a_3>0\), let \(0\le p<1\), and write \(T\) for the time to absorption in the model defined below. Set \(\mu_j=\mathbb E[T^j]\) and \(R=\mu_2\mu_4/\mu_3^2\). Then
\[
R\ge\frac65,
\]
with equality if and only if \(p=0\) and \(a_1=a_2=a_3\). For each fixed \(p<1\), the equal-time design is a strict local minimizer of \(R\) among positive triples modulo common scale.

Define \(p_*\) to be the unique root in \((0,1)\) of
\[
p^4+48p^3+148p^2+16p-60=0.
\]
It satisfies \(0.5425<p_*<0.5426\). For **each** \(p\in(p_*,1)\), there are strictly positive heterogeneous holding times with smaller \(R\) than the equal-time design at the same \(p\). For example, at \(p=5/8\),
\[
R(1,1,1;p)-R(1,1,1/16;p)
=\frac{8340}{345550921}>0.
\]
The root \(p_*\) is the crossover for the two *specified* equal-time and vanishing-third-holding-time benchmark profiles; it is **not** claimed to be the global onset of nonuniform optimality.

## Assumptions and scope
The continuous-time chain starts in transient state 1. In transient state \(i\), it waits an independent exponential time of mean \(a_i>0\), then moves from 1 to 2, from 2 to 3, and from 3 to 1 with probability \(p\), or is absorbed with probability \(1-p\). Every visit draws an independent holding time and return coin. Thus its generator on transient states is
\[
Q=\begin{pmatrix}
-1/a_1&1/a_1&0\\
0&-1/a_2&1/a_2\\
p/a_3&0&-1/a_3
\end{pmatrix},
\]
and the missing row sum in state 3 is the absorption rate \((1-p)/a_3\). This is the directed three-phase feedback family within the phase-type representations used in positivity and absolute-monotonicity studies of Runge--Kutta schemes. The result is a moment-geometry statement for this specific family, not a theorem about arbitrary three-state generators or numerical methods of arbitrary order.

All claims concern exact arithmetic and finite strictly positive holding times, except for the explicitly labelled limiting comparison \(a_3\downarrow0\). The normalized ratio is invariant under scaling all \(a_i\) by the same positive constant.

## Proof
**1. The exact four-moment formula.** The number of complete circuits is geometric, with \(\Pr(K=k)=(1-p)p^{k-1}\) for \(k\ge1\). Each circuit comprises three independent exponential times. Therefore, in a neighborhood of zero,
\[
\mathbb E[e^{zT}]
=\frac{1-p}{(1-a_1z)(1-a_2z)(1-a_3z)-p}.
\]
Put \(e_1=a_1+a_2+a_3\), \(e_2=a_1a_2+a_1a_3+a_2a_3\), \(e_3=a_1a_2a_3\), \(r=1-p\), and \(t=1/r\). Coefficient extraction gives
\[
\begin{aligned}
\frac{\mu_2}{2!}&=t^2e_1^2-te_2,\\
\frac{\mu_3}{3!}&=t^3e_1^3-2t^2e_1e_2+te_3,\\
\frac{\mu_4}{4!}&=t^4e_1^4-3t^3e_1^2e_2+t^2(e_2^2+2e_1e_3).
\end{aligned}
\]
Set \(x=e_2/e_1^2\), \(y=e_3/e_1^3\), and \(q=t-1=p/(1-p)\). By the elementary symmetric mean inequalities, \(0<x\le1/3\) and \(0<y\le1/27\). With
\[
A=t-x,\quad B=t^2-2tx+y,\quad C=t^3-3t^2x+t(x^2+2y),
\]
we obtain \(R=(4/3)AC/B^2\), where \(B>0\) because \(\mu_3>0\). Thus \(R\ge6/5\) is equivalent to \(10AC-9B^2\ge0\).

**2. A positive polynomial for every feedback probability.** Direct expansion yields
\[
10AC-9B^2=P_0+qP_1+q^2P_2+q^3P_3+q^4,
\]
where
\[
\begin{aligned}
P_0&=1-4x+4x^2-10x^3+2y+16xy-9y^2,\\
P_1&=2\big(2-6x+4x^2-5x^3+(8x+2)y\big),\\
P_2&=2\big(3-6x+2x^2+y\big),\\
P_3&=4(1-x).
\end{aligned}
\]
For \(0<x\le1/3\), the polynomial \(2-6x+4x^2-5x^3\) is decreasing and at \(x=1/3\) equals \(7/27>0\). Consequently, \(P_1>0\), \(P_2>0\), and \(P_3>0\).

We prove \(P_0\ge0\) directly. Its derivative in \(y\) is \(2+16x-18y>0\) on the permitted domain. If \(x\le1/4\), then
\[
P_0\ge 1-4x+4x^2-10x^3\ge3/32>0,
\]
because the displayed cubic is decreasing on \([0,1/4]\). If \(1/4\le x\le1/3\), Schur's three-variable inequality \(e_1^3+9e_3\ge4e_1e_2\) yields \(y\ge(4x-1)/9\), and hence
\[
P_0\ge P_0\!\left(x,\frac{4x-1}{9}\right)
=\frac23(1-3x)(5x^2-3x+1)\ge0.
\]
The final quadratic is strictly positive for real \(x\). Equality in this argument requires \(x=1/3\), forcing \(a_1=a_2=a_3\), and also \(q=0\) because all remaining polynomial coefficients are positive. This proves the universal floor and its equality characterization.

**3. Equal holding times are locally optimal.** Homogeneity permits fixing \(a_1+a_2+a_3=3\), and symmetry makes the Hessian at \((1,1,1)\) a scalar on the two-dimensional mean-zero perturbation plane. Its value is determined by \((a_1,a_2,a_3)=(1+u,1-u,1)\). Exact differentiation gives
\[
R(1+u,1-u,1;p)
=R(1,1,1;p)
+\frac{4(1-p)^3(50-10p-13p^2)}{(p^2+16p+10)^3}u^2+O(u^4).
\]
The quadratic coefficient is strictly positive for \(0\le p<1\). Thus the equal-time triple is a strict local minimum, modulo common rescaling, for every such \(p\).

**4. Exact comparison with the two-fast-stage boundary.** Direct substitution gives
\[
R_{\mathrm{eq}}(p)=\frac{12(p+2)(5p^2+17p+5)}{(p^2+16p+10)^2},\quad
R_{\mathrm{bd}}(p)=\lim_{\varepsilon\downarrow0}R(1,1,\varepsilon;p)=\frac{(p+3)(p^2+10p+5)}{12(p+1)^2}.
\]
Their difference factors as
\[
R_{\mathrm{eq}}(p)-R_{\mathrm{bd}}(p)
=\frac{(1-p)^3(p^4+48p^3+148p^2+16p-60)}{12(p+1)^2(p^2+16p+10)^2}.
\]
The polynomial in the numerator is strictly increasing on \([0,1]\), negative at zero and positive at one; therefore it has precisely the asserted interior root. Above that root, continuity at \(\varepsilon=0\) supplies a strictly positive finite \(\varepsilon\) with \(R(1,1,\varepsilon;p)<R_{\mathrm{eq}}(p)\). The stated rational witness follows by exact substitution, completing the proof.

## Verification
Run `python verify.py` using SymPy. The standalone program checks the generating-polynomial coefficients, the exact Schur-bound substitution, both benchmark formulas, the quartic crossover factorization, its rational root bracket, the local Hessian coefficient, and the rational finite-parameter witness. It also performs 30 exact-rational supplementary sample checks. These samples are not used as a proof for the quantified family: the algebraic arguments above establish the universal statements.

## Relationship to prior work
Weng, Yu, and Zhu (2026) relate Runge--Kutta absolute-monotonicity conditions to phase-type absorption times. Their Theorem 4.4 proves a higher-moment ratio bound for *acyclic* phase-type representations; they explicitly leave the corresponding general cyclic higher-order bound open. This result proves the fourth raw-moment ratio bound for the directed three-phase feedback family, including positive feedback, and exposes a local-versus-global distinction under rate heterogeneity. It does not resolve the unrestricted cyclic problem.

The earlier Aldous--Shepp least-variance theorem concerns the second raw-moment ratio; He, Horváth, Horváth, and Telek (2019) obtain stochastic and individual moment bounds using dominant eigenvalues, not the stated nonlinear fourth-moment ratio and rate-design comparison. Previous equal-holding-time feedback calculations give the symmetric benchmark curve, but cannot imply the heterogeneous strict comparison.

## Limitations
The crossover root is **only** the exact crossing of two specified benchmark profiles, not an asserted global optimization transition. The boundary profile has a zero holding time and is used only as a limit; the proof and rational witness provide finite positive realizations. The moment inequality is established for a single directed three-stage feedback cycle, not arbitrary cyclic PH distributions, other starting distributions, or unconstrained Runge--Kutta tableaux. The local minimum concerns rate perturbations at fixed feedback probability and is not a global minimum for all such probabilities. Historical-priority uncertainty remains for more general distribution inequalities and nonlocal optimization results.

## References
1. Z. Weng, H. Yu, and Q. Zhu, *Phase-type representations for Strong Stability Preserving Runge--Kutta methods*, arXiv:2610.37425v1 (first public version 2026-10-27), https://arxiv.org/html/2610.37425.
2. Q.-M. He, G. Horváth, I. Horváth, and M. Telek, *Moment bounds of PH distributions with infinite or finite support based on the steepest increase property*, Advances in Applied Probability 51 (2019), 168--183, https://doi.org/10.1017/apr.2019.7.
3. D. Aldous and L. Shepp, *The least variable phase type distribution is Erlang*, Communications in Statistics: Stochastic Models 3 (1987), 467--473, https://doi.org/10.1080/15326348708807067.
