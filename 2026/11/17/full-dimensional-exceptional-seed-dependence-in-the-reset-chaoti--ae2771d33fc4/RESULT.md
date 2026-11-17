# Full-dimensional exceptional seed dependence in the reset chaotic logistic map

## Finding

Let \(f(x)=4x(1-x)\). Independently at each integer time, a state is replaced with its *initial seed* \(x\) with probability \(r\), or advanced under \(f\) with probability \(1-r\). For a fixed reset history, differentiate the resulting state at time \(n\) with respect to the seed \(x\), keeping the history fixed. Let \(A_n(x,r)\) be the expectation of the absolute value of this derivative over reset histories.

**Theorem.** On the interior seed interval \(0<x<1\):

1. For every \(r\in[1/2,1)\) and every seed, the limit \(\lim_{n\to\infty}n^{-1}\log A_n(x,r)=0\) exists.
2. There exists one set \(E\subset(0,1)\), independent of \(r\), that is dense, Lebesgue-null, and of Hausdorff dimension exactly \(1\), such that **for every** \(x\in E\) and **every** \(0<r<1/2\), the limit \(\lim_{n\to\infty}n^{-1}\log A_n(x,r)\) **does not exist**. More precisely, its upper limit is \(\log(2(1-r))\), and its lower limit is strictly smaller.
3. Outside a Lebesgue-null set of seeds, simultaneously for all \(0<r<1/2\), the limit exists and equals \(\log(2(1-r))\).

The result concerns *annealed absolute derivative growth*, not the almost-sure derivative exponent for a single reset history. It identifies an explicit seed-dependence boundary of a standard resetting-growth formula.

## Assumptions and scope

At each step, reset events are independent Bernoulli variables of parameter \(r\). A reset sends the evolving point to the same initial value \(x\), hence its derivative with respect to that seed is \(1\). Write \(q=1-r\) and \(D_m(x)=|(f^m)'(x)|\), with \(D_0=1\). The last-reset decomposition gives the exact finite-time identity

\[
A_n(x,r)=r\sum_{m=0}^{n-1}q^mD_m(x)+q^nD_n(x),\qquad n\ge1.
\]

This identity is present in the motivating literature; it is not a new contribution. We restrict the theorem to \(0<x<1\) and \(0<r<1\), except that the first assertion allows the upper endpoint interval \(r\in[1/2,1)\). No claim of universal behavior at \(x=0,1\) is made.

## Proof

**Exact conjugacy and renewal growth.** Write \(x=h(t)=\sin^2(\pi t)\), uniquely for \(0<t<1/2\). Since \(f\circ h(t)=h(2t)\), differentiation gives, for all integers \(m\ge0\),

\[
D_m(h(t))=\frac{2^m|\sin(2^{m+1}\pi t)|}{\sin(2\pi t)}.
\]

Put \(b_m(t)=|\sin(2^{m+1}\pi t)|\), \(c(t)=\sin(2\pi t)>0\), and \(R=2(1-r)\). The renewal identity becomes the **exact**, nonasymptotic expression

\[
c(t)A_n(h(t),r)=r\sum_{m=0}^{n-1}R^m b_m(t)+R^n b_n(t).\tag{1}
\]

For \(r\ge1/2\), \(R\le1\). The right-hand side is at most \(rn+1\) and at least \(r c(t)\), since the original expression contains the term \(rD_0=r\). Thus \(r\le A_n\le(rn+1)/c(t)\), proving assertion 1.

For \(0<r<1/2\), \(R>1\). From \(b_m\le1\), equation (1) gives \(A_n\le C_{r,t}R^n\). On the other hand,

\[
A_n(h(t),r)\ge\frac{R^n b_n(t)}{c(t)}.\tag{2}
\]

**Full-measure universal rate.** The map \(t\mapsto\{2^m t\}\) preserves uniform Lebesgue measure on \((0,1/2)\) for each \(m\ge1\). Consequently, for every \(\varepsilon>0\),

\[
\operatorname{Leb}\bigl\{t\in(0,1/2):b_m(t)<e^{-\varepsilon m}\bigr\}=O(e^{-\varepsilon m}).
\]

The first Borel–Cantelli lemma, applied to a countable sequence of positive \(\varepsilon\) approaching zero, yields \(\liminf_{m\to\infty}m^{-1}\log b_m(t)\ge0\) for almost every \(t\). Because \(b_m\le1\), this limit is exactly zero. Using (2) and the exponential upper bound establishes assertion 3 **simultaneously in every** \(0<r<1/2\). The map \(h\) is Lipschitz, so the corresponding exceptional set in \(x\)-space is also null.

**Sparse zero-block Cantor sets.** Fix \(\alpha>0\). Select an integer \(k_1\ge16\), then recursively set

\[
L_j=\lceil\alpha k_j\rceil,\qquad k_{j+1}=(k_j+L_j+3)^2.
\]

In a binary expansion \(t=0.t_1t_2\ldots\), force the digits at positions \(k_j+1,\ldots,k_j+L_j\) to be zero, and the next three digits to be \(010\). All remaining digits are free. Also fix the initial prefix \(001\), so \(t\in[1/8,1/4]\). Call the resulting compact set \(C_\alpha\). The infinitely many prescribed \(1\)-digits make every expansion unambiguous. For each \(t\in C_\alpha\), define \(n_j=k_j+\lfloor L_j/2\rfloor\) and \(N_j=k_j+L_j\).

At the end of each zero block, the next binary digits are \(010\), which entails \(\{2^{N_j}t\}\in[1/4,3/8]\), and hence

\[
b_{N_j}(t)\ge1/\sqrt2.
\]

It follows from (2) and the global upper bound that

\[
\limsup_{n\to\infty}\frac{\log A_n(h(t),r)}n=\log R.\tag{3}
\]

For \(k_j\le m\le n_j\), the remaining zero digits imply \(0\le\{2^m t\}\le2^{-(k_j+L_j-m)}\), and thus

\[
b_m(t)\le 2\pi\,2^{m-k_j-L_j}.
\]

Split the sum in (1) at \(m=k_j\). Its earlier terms are bounded by \(rR^{k_j}/(R-1)\). The terms from \(k_j\) to \(n_j\), including the final term, are bounded by

\[
C_r R^{k_j}2^{-L_j}(2R)^{\lfloor L_j/2\rfloor}
\le C_r R^{k_j}(R/2)^{L_j/2}\le C_rR^{k_j},
\]

because \(R/2=1-r<1\). Therefore \(A_{n_j}(h(t),r)\le C_{r,t}R^{k_j}\), with \(C_{r,t}\) independent of \(j\), and

\[
\liminf_{n\to\infty}\frac{\log A_n(h(t),r)}n
\le \frac{\log R}{1+\alpha/2}<\log R.\tag{4}
\]

Equations (3)–(4) prove failure of the growth-rate limit for every \(r\in(0,1/2)\) on the **same** \(C_\alpha\).

**Exact dimension and density.** Let \(F(N)\) count the free digits among the first \(N\) binary places. Since \(k_{j+1}/(k_j+L_j)\to\infty\), preceding forced blocks have asymptotically negligible length, and the smallest asymptotic free-digit fraction occurs at the ends of the current blocks. Consequently

\[
\liminf_{N\to\infty}\frac{F(N)}N=\frac1{1+\alpha}.
\]

At depth \(N\) there are exactly \(2^{F(N)}\) admissible dyadic cylinders. Covering at depths \(N=k_j+L_j\) gives the Hausdorff-dimension upper bound \(1/(1+\alpha)\). Conversely, putting unbiased independent digits in every free place gives a measure of mass \(2^{-F(N)}\) on each admissible depth-\(N\) cylinder. For every \(s<1/(1+\alpha)\), this mass is eventually at most \(2^{-sN}\), and an interval of length comparable to \(2^{-N}\) meets at most two such cylinders. The mass-distribution principle proves the reverse bound. Thus

\[
\dim_H C_\alpha=\frac1{1+\alpha}.
\]

The function \(h(t)=\sin^2(\pi t)\) is bi-Lipschitz on \([1/8,1/4]\). Hence the corresponding seed set has the same dimension. Allowing *any* fixed finite binary prefix instead of \(001\) produces a copy in every open subinterval of \((0,1/2)\): simply start \(k_1\) beyond the prefix, and all asymptotic estimates are unchanged. Finally take the countable union of these prefix copies over \(\alpha=1/j\), \(j\ge1\), and over finite binary prefixes. Every constituent has dimension strictly below \(1\), hence is Lebesgue-null; their union \(E\) is dense and has \(\dim_H E=\sup_j j/(j+1)=1\). Its image under the increasing homeomorphism \(h\) is dense in \((0,1)\), null by the Lipschitz property, and still full-dimensional (a fixed-prefix copy lies in some compact subinterval where \(h\) is bi-Lipschitz). This proves assertion 2 and the theorem.

## Verification

The standalone `CHECK.py` recomputes the conjugacy-derivative identity, enumerates every reset history through eight steps to verify the renewal formula directly, checks the prescribed binary-block sine inequalities on a finite constructed example, and confirms the predicted finite-scale growth dips and recoveries. It reports `OK 72 analytic-identity, enumerated-history and finite-block checks` in the specified local environment. The infinite-time and dimension conclusions rest on the analytic arguments above, **not** on these finite checks.

## Relationship to prior work

Aron and Kulkarni (2024 preprint, published 2025) give the exact renewal formula and its typical chaotic prediction \(\max\{0,\log(2(1-r))\}\). The theorem here is **not** a new derivation of that prediction. It distinguishes its almost-everywhere validity from full seed-wise validity and shows that the exceptional collection is dense and of full Hausdorff dimension, uniformly across the entire subcritical resetting regime. The original analysis assumes a well-defined seed-independent deterministic chaotic exponent; the constructed seeds need not satisfy that assumption, so this is a rigorously identified boundary of applicability, not a claim that its conditional derivation is false. The follow-up work on Lyapunov spectra under resetting also studies regular scrambling regimes but does not establish this seed-exception dimension theorem.

Barreira–Schmeling (2000) and Gelfert–Rams (2007/2009) study full-dimensional sets irregular for ordinary pointwise Lyapunov/Birkhoff exponents. Those observables use \(n^{-1}\log D_n\) or Birkhoff averages. The present observable is \(n^{-1}\log[r\sum_{m<n}(1-r)^mD_m+(1-r)^nD_n]\), a **positive renewal-weighted sum of past derivatives**: nonconvergence of the underlying deterministic exponent by itself does not imply nonconvergence of this smoothed maximum. The zero-block and recovery estimates are therefore essential additional comparisons.

## Limitations

This concerns one logistic map at parameter four, Bernoulli resets to the same initial seed, and the *expected absolute seed derivative*. It does not classify the whole exceptional set, establish a universal dimension spectrum for individual upper/lower rates, or extend directly to coupling, noise in the reset site, or the pathwise random derivative Lyapunov exponent. Interior seeds are essential: endpoint seeds can have different derivative growth. The historical-priority conclusion is based on the accessible sources and searched records, not on a complete mathematical-literature census; general nonadditive multifractal theory could conceivably imply a related result after further specialization.

## References

1. C. Aron and M. Kulkarni, *Control of spatiotemporal chaos by stochastic resetting*, arXiv:2412.21043v1 (first posted 2024-12-30), later *Physical Review E* **112**, 014220 (2025), https://arxiv.org/html/2412.21043v1 ; https://doi.org/10.1103/zlm4-zrnx .
2. C. Aron and M. Kulkarni, *Localization of information driven by stochastic resetting*, arXiv:2510.07394 (first posted 2025-10-08), https://arxiv.org/html/2510.07394 .
3. L. Barreira and J. Schmeling, *Sets of “non-typical” points have full topological entropy and full Hausdorff dimension*, *Israel Journal of Mathematics* **116** (2000), 29–70, https://doi.org/10.1007/BF02773211 .
4. K. Gelfert and M. Rams, *The Lyapunov spectrum of some parabolic systems*, arXiv:0709.2832 (2007), *Ergodic Theory and Dynamical Systems* **29** (2009), 919–940, https://arxiv.org/abs/0709.2832 .
