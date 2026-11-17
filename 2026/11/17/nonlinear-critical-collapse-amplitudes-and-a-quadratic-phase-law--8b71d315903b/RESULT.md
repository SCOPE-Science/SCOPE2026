# Nonlinear critical-collapse amplitudes and a quadratic phase law in two-player maxima dynamics

## Finding

Consider the critical-resource (\(\alpha=2\)) map of maxima
\[
\Phi(x,y)=\left(
\frac{\max\{2x(1-y),1-x\}}{2x(1-y)+1-x},
\frac{\max\{2y(1-x),1-y\}}{2y(1-x)+1-y}
\right),\qquad (x,y)\in[1/2,1)^2.
\]
For any initial point with \(x_0>y_0\), put
\[
a_t=\log\frac{x_t}{1-x_t},\qquad b_t=\log\frac{y_t}{1-y_t},\qquad \rho=\frac34.
\]
There exist a finite integer \(N\ge0\) and a nonzero vector \(W=(U,V)\) with \(U>0\) and \(0\le V\le U/2\), depending on the initial point, such that
\[
\binom{a_{N+2n}}{b_{N+2n}}
=\rho^n\binom U V
+\rho^{2n}\frac16\binom{3U^2-4UV+8V^2}{V(4U+V)}
+O(\rho^{3n}), \tag{1}
\]
and
\[
\binom{a_{N+2n+1}}{b_{N+2n+1}}
=\rho^n\begin{pmatrix}1&-1/2\\1/2&-1\end{pmatrix}
\binom U V+O(\rho^{2n}). \tag{2}
\]
The errors are vector errors as \(n\to\infty\), with constants allowed to depend on the initial point. For \(y_0>x_0\), interchange the two coordinates. Consequently, writing \(G_t=\max\{x_t,y_t\}\), every off-diagonal initial point satisfies the **rigorous sharp rate**
\[
\lim_{t\to\infty}\frac{G_{t+2}-1/2}{G_t-1/2}=\frac34. \tag{3}
\]
Moreover the even-phase ratio \(b_{N+2n}/a_{N+2n}\) tends to \(V/U\), while the odd-phase ratio tends to \((U/2-V)/(U-V/2)\): the decay carries an initial-condition-dependent two-phase direction.

On the diagonal \(x_0=y_0\in(1/2,1)\), there is \(A>0\) such that
\[
a_n=b_n=2^{-n}A+\tfrac12 4^{-n}A^2+O(8^{-n}),\qquad
\lim_{n\to\infty}\frac{G_{n+2}-1/2}{G_n-1/2}=\frac14. \tag{4}
\]
Thus symmetric and asymmetric initial maxima have distinct *exact* critical two-step rates.

## Assumptions and scope

The dynamics is the continuous reduced maxima map \(\Phi\) at exactly \(\alpha=2\). The closed-left state space \([1/2,1)^2\) is invariant. At boundary maxima \(1/2\) the reduced map remains unambiguous, but no uniqueness of a position-labelled full-system update at a tied maximum is asserted. The fixed point \((1/2,1/2)\) is excluded from the ratios in (3)--(4). In (1)--(2), \(N\) can be any time after entry into the explicitly described invariant cone. No assertion of a uniform \(N\) or uniform error constant as the initial state approaches the diagonal is made.

## Proof

**Exact logarithmic form.** Set \(\kappa(s)=\log((1+e^s)/2)\) for \(s\ge0\). It satisfies \(\kappa(0)=0\), \(0<\kappa(s)<s\) when \(s>0\), and \(1/2\le\kappa'(s)<1\). The log-odds conjugate of \(\Phi\) is exactly
\[
(a,b)\longmapsto\bigl(|a-\kappa(b)|,\ |b-\kappa(a)|\bigr). \tag{5}
\]
Suppose \(a>b\ge0\). The first modulus is positive because \(a> b\ge\kappa(b)\). If \(b\ge\kappa(a)\), the difference of the new coordinates equals \((a-b)+(\kappa(a)-\kappa(b))>0\); if \(b\le\kappa(a)\), it equals \((a+b)-(\kappa(a)+\kappa(b))>0\). Hence strict order persists, and the larger log-odds satisfies \(a_{t+1}=a_t-\kappa(b_t)\le a_t\).

**Global approach and finite cone entry.** The decreasing nonnegative sequence \(a_t\) has a limit \(a_\infty\). Summing \(\kappa(b_t)=a_t-a_{t+1}\) gives \(\kappa(b_t)\to0\), so \(b_t\to0\). Equation (5) then forces \(b_{t+1}\to\kappa(a_\infty)\). Thus \(a_\infty=0\), and both coordinates tend to zero. Define the closed cone-like region
\[
\mathcal S=\{(a,b):a>b\ge0,\ b\le\kappa(a)\}.
\]
Whenever \(b>\kappa(a)\), the gap \(a-b\) increases strictly in one step, by \(\kappa(a)-\kappa(b)>0\). If this held forever, the gap would remain at least its initial positive value despite \(a_t\to0\), impossible. Hence the orbit enters \(\mathcal S\) after finitely many steps. Inside it, (5) is the smooth map
\[
T(a,b)=(a-\kappa(b),\kappa(a)-b). \tag{6}
\]
This region is forward invariant: writing \((a',b')=T(a,b)\), the \(1\)-Lipschitz property of \(\kappa\) and \(\kappa(b)\le b\) give
\[
\kappa(a')=\kappa(a-\kappa(b))\ge\kappa(a)-\kappa(b)\ge\kappa(a)-b=b'.
\]
Strict order also continues by the previous argument.

**Two-step analytic normal form.** Taylor expansion yields
\[
\kappa(s)=\frac{s}{2}+\frac{s^2}{8}+O(s^4),\qquad
T(z)=Lz+q(z)+O(\|z\|^4),
\]
where \(z=(a,b)^{\mathsf T}\),
\[
L=\begin{pmatrix}1&-1/2\\1/2&-1\end{pmatrix},\qquad
q(a,b)=\frac18\binom{-b^2}{a^2}.
\]
Direct multiplication gives \(L^2=\rho I\). Therefore
\[
T^2(z)=\rho z+Q(z)+O(\|z\|^3),
\quad Q=Lq+q\circ L=-\frac1{32}\binom{3a^2-4ab+8b^2}{4ab+b^2}. \tag{7}
\]
In particular, after cone entry and for sufficiently small iterates, the two-step norms \(r_n=\|z_{N+2n}\|\) satisfy
\[
(\rho-Cr_n)r_n\le r_{n+1}\le(\rho+Cr_n)r_n.
\]
Since \(r_n\to0\), choose \(q_0\) with \(\rho<q_0<\sqrt\rho\). Eventually \(r_{n+1}\le q_0r_n\), implying \(\sum_n r_n<\infty\). The normalized vectors \(w_n=\rho^{-n}z_{N+2n}\) converge because
\[
\|w_{n+1}-w_n\|\le C\rho^{-n-1}r_n^2
\]
is summable. Their limit \(W\) is nonzero: the lower two-step estimate makes the product of normalized radial factors bounded below by the positive infinite product \(\prod_{n\ge n_0}(1-Cr_n/\rho)\). Invariance of \(\mathcal S\) implies \(0\le V\le U/2\), and nonzero \(W\) then forces \(U>0\).

The convergence first gives \(z_{N+2n}=\rho^nW+O(\rho^{2n})\), since the normalized vectors are bounded and the quadratic tails sum as a geometric series. Substituting this estimate into (7), summing the normalized telescoping differences from \(n\) to infinity, and retaining the homogeneous quadratic term yields
\[
W-w_n=\frac{\rho^{n-1}}{1-\rho}Q(W)+O(\rho^{2n}).
\]
Multiplication by \(\rho^n\) gives (1), because \(-Q(W)/(\rho(1-\rho))\) is precisely the quadratic vector displayed there. Substitution in (6) gives (2). Since \(U>0\) and \(U-V/2>0\), the maximal coordinate is asymptotically positive in both parities. The logistic relation \(x-1/2=a/4+O(a^3)\) gives (3) and the stated ratios.

**Diagonal.** For \(a=b>0\), the exact scalar recurrence is \(a'=a-\kappa(a)\). It decreases to zero and has expansion \(a'=a/2-a^2/8+O(a^4)\). The same normalized-product/telescoping argument, now with multiplier \(1/2\), produces \(A=\lim 2^na_n>0\) and \(a_n=2^{-n}A+(A^2/2)4^{-n}+O(8^{-n})\), proving (4).

## Verification

Run `python3 verify.py` using Python 3 with its standard library. The checker verifies the rational polynomial identities \(L^2=\rho I\), \(Q=Lq+q\circ L\), and the coefficient relation for the second-order term; it additionally tests strict order, eventual cone entry, and two-step rates for specified finite trajectories (including near-diagonal cases). A separate high-precision numerical calculation for initial maxima \((0.81,0.66)\) produced the limiting even-phase log-odds vector approximately \((0.84485526,0.26648559)\), and observed quadratic scaled-error coefficients approach the exact predicted functions \((0.30148180,0.16193026)\). Numerical checks are supporting evidence; the proof above supplies all-time and continuum-of-input conclusions.

## Relationship to prior work

Satur's 2026 analysis introduces this map, proves global collapse at \(\alpha=2\), and in Section 5.2 calculates the **piecewise-linear leading-order** two-step factor \(3/4\), with an explicit statement that rigorous nonlinear rate control is still needed. Equations (1)--(4) establish that nonlinear control for every off-diagonal orbit and give a nonzero asymptotic vector plus its universal second-order correction; they do not claim discovery of the leading-order factor. Simpson's stability theory for maps on switching manifolds provides general stability context, but its exponential-stability criteria are not the asymptotic vector and quadratic coefficient for the present two-switching-manifold model.

## Limitations

This concerns exactly the critical parameter, not \(\alpha\ne2\). The limiting vector depends on the initial state and need not have an elementary closed form. Global convergence at the critical parameter and the linearized factor are known from the source; the additions are the rigorous all-orbit nonlinear asymptotic phase, explicit second-order term, and sharp diagonal/off-diagonal dichotomy. The reduced map can be continued at ties even when the original position-labelled interpretation becomes ambiguous. No robustness under perturbations or uniformity near the invariant diagonal is claimed. Independent external validation and historical-priority adjudication have not been performed.

## References

1. O. R. Satur, *From oscillations to symmetry breaking in a two-dimensional piecewise-smooth dynamical system*, arXiv:2611.13318v1, first posted 2026-11-09, especially Eq. (1), Theorem 2 and Section 5.2. https://arxiv.org/abs/2611.13318
2. D. J. W. Simpson, *The stability of fixed points on switching manifolds of piecewise-smooth continuous maps*, arXiv:1612.02932v1 (2016), especially Sections 1 and 3. https://arxiv.org/abs/1612.02932
