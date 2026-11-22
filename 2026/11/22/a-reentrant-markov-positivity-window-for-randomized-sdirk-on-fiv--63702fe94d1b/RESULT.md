# A reentrant Markov-positivity window for randomized SDIRK on five birth states

## Finding

**Theorem (exact one-step stochasticity law).** Let \(B_n\) be the row generator of the homogeneous unit-rate absorbing pure-birth chain on \(n\ge2\) states: \((B_n)_{i,i}=-1\) and \((B_n)_{i,i+1}=1\) for \(1\le i<n\), and its final row is zero. Apply to \(p'=pB_n\) the two-stage singly diagonally implicit Runge--Kutta method with
\[
 A_x=\begin{pmatrix}x&0\\1-2x&x\end{pmatrix},\qquad b=(1/2,1/2)^\mathsf T,\qquad X\sim\mathrm{Uniform}[1/2,1],
\]
with one common draw \(X\) in both stages. Write \(M_n(h,X)\) for the one-step *row* transition matrix at step \(h\ge0\). Its row sums are always one.

For all \(n=2,3,4\), all \(x\in[1/2,1]\), and all \(0\le h\le2\), the matrix \(M_n(h,x)\) is entrywise nonnegative. Five states are the first in this absorbing-birth family for which a positive fraction of tableau draws give a negative transition entry at **arbitrarily small positive** steps. For \(n=5\), the entire positivity probability is exactly
\[
\Pr\bigl(M_5(h,X)\ge0\bigr)=
\begin{cases}
1,&h=0,\\
\dfrac{4-3h-\sqrt{h^2-40h+16}}{4h},&0<h<1/3,\\
1,&1/3\le h\le2,\\
\dfrac2h-\sqrt{\dfrac{2(h-2)}h},&2<h<1+\sqrt3,\\
0,&h\ge1+\sqrt3.
\end{cases}
\]
Here \(M\ge0\) means *every* matrix entry is nonnegative. In particular, **all** tableau choices are stochastic precisely for \(h\in\{0\}\cup[1/3,2]\); the success probability tends to \(1/2\), rather than one, as \(h\downarrow0\). Moreover, the ensemble-mean transition matrix itself is nonstochastic for all sufficiently small \(h>0\), since
\[
\mathbb E\bigl[(M_5(h,X))_{1,5}\bigr]=-\frac{h^4}{16}+O(h^5).
\]

## Assumptions and scope

Indices are one-based; the final state is absorbing, and the generator has unit transition rates. The step \(h\) is dimensionless (rate times physical time). The probabilities concern a *single completed one-step matrix*; a negative entry does not require every starting distribution to become negative. The random stage parameter is continuous-uniform on \([1/2,1]\), independent between successive steps if repeated, although only one step is analyzed here. The completed method is applied in exact arithmetic, without truncating the two implicit solves. The stability function is evaluated by rational functional calculus on \(B_n\).

## Proof

**1. Exact scalar function.** Solving the two stage equations gives, for a scalar argument \(z\),
\[
R(z;x)=\frac{2+(2-4x)z+(2x^2-4x+1)z^2}{2(1-xz)^2},
\]
so that for decay \(z=-h\),
\[
r_0:=R(-h;x)=\frac{2+(4x-2)h+(2x^2-4x+1)h^2}{2(1+hx)^2}.
\]
The tableau is well-defined for every \(h\ge0\) because \(1+hx>0\). Since \(R(0;x)=1\) and \(B_n\mathbf1=0\), the update is exactly row-sum preserving.

**2. Finite birth-chain functional calculus.** The transient block is \(-I+S\), with \(S\) the nilpotent forward shift. Analytic functional calculus gives the transient-to-transient entry at forward distance \(j\) as \(r_j=h^j\partial_z^jR(-h;x)/j!\). The three nontrivial distances needed for at most five states are
\[
\begin{aligned}
r_1&=\frac{h[1+h(3x-1)]}{(1+hx)^3},\\
r_2&=\frac{h^2[1+h(6x^2-2x)]}{2(1+hx)^4},\\
r_3&=\frac{h^3x[1-x+hx(3x-1)]}{(1+hx)^5}.
\end{aligned}
\]
Every displayed entry is nonnegative for \(h\ge0\), \(1/2\le x\le1\). The probability of absorption from a state with \(k\) forward jumps available is \(a_k=1-\sum_{j=0}^{k-1}r_j\). Direct common-denominator algebra gives
\[
\begin{aligned}
a_1&=\frac{h[2+h(4x-1)]}{2(1+hx)^2},\\
a_2&=\frac{h^2[1+hx(4x-1)]}{2(1+hx)^3},\\
a_3&=\frac{h^3x[2(1-x)+hx(4x-1)]}{2(1+hx)^4},\\
a_4&=\frac{h^4x^2[3-4x+hx(4x-1)]}{2(1+hx)^5}.
\end{aligned}
\]
The first three absorption entries are nonnegative for every \(h\ge0\). Consequently, **for five states and every positive step, the only possible negative entries are a transient diagonal \(r_0\) and the opposite-corner entry \(a_4=(M_5)_{1,5}\)**. With at most four states, \(a_4\) never occurs.

**3. Exact opposite-corner transition.** The sign of \(a_4\) for \(h>0\) is the sign of \(F_h(x)=3-4x+hx(4x-1)\). For \(1/2\le x\le3/4\), this is nonnegative for all \(h\ge0\). For \(3/4<x\le1\), it is negative exactly when
\[
0<h<\frac{4x-3}{x(4x-1)}.
\]
The right endpoint increases over \([3/4,1]\), and its maximum is \(1/3\). This can also be seen directly from \(x(4x-1)-3(4x-3)=(x-1)(4x-9)\ge0\) on that interval. Hence \(a_4\ge0\) for all parameters as soon as \(h\ge1/3\), whereas at every \(0<h<1/3\), it is negative exactly for \(x>\alpha(h)\), where
\[
\alpha(h)=\frac{h+4-\sqrt{h^2-40h+16}}{8h}\in(3/4,1).
\]
The root is unique in \([1/2,1]\): \(F_h\) is strictly decreasing there for \(0<h<1/3\), with \(F_h(1/2)>0\) and \(F_h(1)<0\). Uniformity of \(X\) gives the first nontrivial probability branch \(2(\alpha(h)-1/2)\).

**4. Exact diagonal transition.** The numerator of \(r_0\), regarded as a quadratic in \(x\), has discriminant \(8h^3(h-2)\). For \(0<h\le2\), it is nonnegative throughout \([1/2,1]\) (equivalently, the derivative in \(x\) is nonnegative there and its value at \(1/2\) is \(2-h^2/2\ge0\)). For \(h>2\), its smaller zero is below \(1/2\) and the larger zero is
\[
\beta(h)=1-\frac1h+\sqrt{\frac{h-2}{2h}}.
\]
Thus \(r_0\ge0\) precisely when \(X\ge\beta(h)\); a nonempty admissible set remains only for \(2<h<1+\sqrt3\). Its uniform probability is \(2(1-\beta(h))=2/h-\sqrt{2(h-2)/h}\). For \(h\ge1+\sqrt3\), the probability is zero (endpoint equality is a null event). Combining this with Step 3 proves the complete five-branch law and the noninterval all-draw safe set.

**5. Small-step phase and expected failure.** For every fixed \(x>3/4\), the opposite-corner expansion is
\[
a_4(h,x)=\frac{x^2(3-4x)}2h^4+O(h^5)<0
\]
for all sufficiently small positive \(h\). At the same time, \(\alpha(h)\to3/4\) as \(h\downarrow0\), giving the limiting success probability \(2(3/4-1/2)=1/2\). The expansion is uniform in \(x\in[1/2,1]\) by the positive denominators. Since the uniform density on this interval is two,
\[
\mathbb E\left[\frac{X^2(3-4X)}2\right]
=\int_{1/2}^1x^2(3-4x)\,dx=-\frac1{16}.
\]
This proves negativity of the mean opposite-corner entry for sufficiently small \(h>0\). The step at \(h=0\) is exactly the identity and therefore nonnegative, proving the discontinuity in positivity probability at zero. The minimal-state assertion follows from Step 2 and the \(r_0\ge0\) bound on \([0,2]\).

## Verification

The accompanying `verify.py` is a self-contained Python 3 standard-library checker. It builds the full matrix by exact rational stage solves (not from the closed formulas), independently builds the claimed coefficient matrices, compares all entries for two through five states across rational step and parameter grids, checks row sums and signs, and numerically cross-checks the four nonzero probability branches using 4,000 midpoint bins per case. A fresh package extraction passed 5,495 checks. These finite checks supplement but do not substitute for the algebraic argument above; the theorem covers continuous parameter ranges and all positive step sizes.

## Relationship to prior work

Eisenmann, Jans, Kruse and Podhaisky (2026, arXiv:2607.18928) introduce precisely this randomized tableau and prove its algebraic and scalar A-stability and convergence. Those stability properties and the scalar stability function are prior facts. They do not state the five-state Markov-positive probability or its small-step discontinuity.

The published *Sharp sign-loss probability and Poisson critical window for randomized SDIRK* analyzes the **same** tableau but only a scalar decay multiplier. Its negative-multiplier probability is exactly the high-step branch here, so that branch is not presented as a standalone novelty claim. It cannot imply the fourth-order, off-diagonal Markov obstruction at steps \(h<1/3\), where scalar multipliers stay positive. The published *A sharp one-third balance frontier for positivity of randomized SDIRK Markov steps* analyzes the **same** tableau on irreducible two-state generators, whose stochasticity condition is a single spectral-multiplier inequality. The present five-state birth generator has a nilpotent transient block and requires a fourth derivative of the multiplier; its low-step transition law is not a corollary of the two-state formula.

Published pure-birth chain positivity analyses for implicit Taylor, Radau IIA and other rational Runge--Kutta maps demonstrate related reentrant phenomena with **different** stability functions and thresholds. Lóczi and Ketcheson (2013/2014) analyze absolute-monotonicity radii of whole rational-function classes, which constrain worst-case uniform positivity guarantees but do not give this particular stage-randomized five-state probability law. Horváth's classical positivity-step theory concerns general RK methods; an explicit equivalent formula in older specialist literature remains a historical-priority risk.

## Limitations

The complete probability law applies only to the specified unit-rate **five-state absorbing birth chain** and the specified unmodified two-stage tableau with a common uniform draw. The four-or-fewer-state immunity assertion is only for this birth-chain family and steps up to two; it is not a statement about every finite Markov generator. The theorem does not assert positivity of internal stages, nor imply that the randomized method fails norm, A-, B-, or mean-square stability. A negative matrix entry need not make every numerical trajectory negative. The negative ensemble-mean entry is a small-step asymptotic, not a sign formula for all time steps. No claim of independent verification or exhaustive historical priority is made.

## References

1. M. Eisenmann, M. Jans, R. Kruse, H. Podhaisky, *Error Bound and Stability Analysis for a Randomized Singly Diagonally Implicit Runge--Kutta Method*, arXiv:2607.18928v1 (first public 2026-07-21), https://arxiv.org/abs/2607.18928.
2. *A sharp one-third balance frontier for positivity of randomized SDIRK Markov steps*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-one-third-balance-frontier-for-positivity-of-randomized--873db862d3d5.
3. *Sharp sign-loss probability and Poisson critical window for randomized SDIRK*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-sign-loss-probability-and-poisson-critical-window-for-rand--119cb032c3ba.
4. *Sharp five-state positivity onset and topology-dependent recovery for the implicit Taylor method*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-five-state-positivity-onset-and-topology-dependent-recover--b9cdeb14effb.
5. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, LMS J. Comput. Math. 17 (2014), arXiv:1303.6651, https://arxiv.org/abs/1303.6651.
6. Z. Horváth, *Positivity of Runge--Kutta and diagonally split Runge--Kutta methods*, Applied Numerical Mathematics 28 (1998), 309--326, https://doi.org/10.1016/S0168-9274(98)00050-6.
