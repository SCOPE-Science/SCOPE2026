# A sharp reversal-branch threshold and false long-time limits for positivity-preserving SAV-BE

## Finding

The positive-root, quadratic-reformulated scalar auxiliary variable backward-Euler (SAV-BE) scheme can have a strictly positive auxiliary variable at every finite step and a strictly decreasing modified energy, yet converge in its physical state to a *nonstationary* point of a strongly convex quadratic gradient flow. The failure persists throughout an interval of **strictly positive** auxiliary-energy shifts.

For the one-dimensional equation \(\dot\phi=-a\phi\), with \(a>0\), initialize \(\phi_0>0\), \(r_0=\sqrt{a\phi_0^2/2+C}\), and take the SAV-BE scheme specified below. In the exactly solvable, unshifted case \(C=0\), define \(t=a\tau\), \(q=(1+2t)^{-1/2}\) and

\[
t_*=\frac{11+3\sqrt{17}}4,\qquad
\Lambda(t)=\frac{2q^2+3q-1}{2q}.
\]

For every \(t\ge t_*\), the trajectory is well-defined at every finite step, \(\phi_n<0\) for every \(n\ge1\), \(r_n=\sqrt{a/2}\,\phi_0q^n>0\), and \(\lim_{n\to\infty}\phi_n=\phi_0\Lambda(t)\). The limit vanishes exactly at \(t=t_*\) and is strictly negative for \(t>t_*\). The threshold is sharp **for permanent residence on the first reversed-sign branch**: if \(1+\sqrt2<t<t_*\), a continuation that stays negative at all subsequent steps is impossible. This says nothing about every later branch after that first crossing.

More importantly, without the unshifted case's removable singularity restriction, the same long-time pathology holds with \(a=1\), \(\phi_0=1\), \(\tau=100\), and **every** \(0<C\le1/2\):

\[
\phi_n<-4\quad(n\ge1),\qquad
r_n>0,\qquad
r_n<10^{-n},\qquad
\phi_n\nearrow\phi_\infty<-4\quad(n\ge1).
\]

The physical energy \(E(\phi)=\phi^2/2\) therefore satisfies \(\lim_{n\to\infty}E(\phi_n)>8\), although \(E(\phi_0)=1/2\) and the modified energy \(\widetilde E_n=r_n^2-C\) decreases to \(-C\). Thus unconditional auxiliary positivity and modified-energy dissipation do not imply long-time fidelity to the unique equilibrium \(\phi=0\), even on a strongly convex quadratic.

## Assumptions and scope

Use the *unmodified* positive-root scheme (3.2) of Huang–Liu–Wang–Yan, not the original sign-indefinite SAV discretization and not a relaxed or corrected variant. Set the scalar mobility to \(\mathcal G=1\), the implicit quadratic operator to \(\mathcal L=0\), the explicit energy to \(\mathcal E_{\mathcal N}(\phi)=a\phi^2/2\), and its derivative to \(\mathcal N(\phi)=a\phi\), with \(a>0\). For \(C>0\), the defining square root is globally strictly positive; hence all standing positivity assumptions are met.

Write \(S_n=\sqrt{a\phi_n^2/2+C}\). The discrete system for each integer \(n\ge0\) and fixed \(\tau>0\) is

\[
\phi_{n+1}-\phi_n=-\tau a\frac{r_{n+1}}{S_n}\phi_n,\qquad
r_{n+1}^2-r_n^2=a\frac{r_{n+1}}{S_n}\phi_n(\phi_{n+1}-\phi_n),
\]

and always selects the unique positive root for \(r_{n+1}\). The case \(C=0\) is analyzed only along the strictly nonzero iterates identified in the theorem: \(S_n=0\) at \(\phi_n=0\), so that boundary case is not a globally defined numerical map. The robust result for \(C>0\) does not have this issue.

## Proof

**1. Scalar reduction and modified energy.** Substitute the first update into the second to get

\[
r_{n+1}^2\left(1+\tau a^2\frac{\phi_n^2}{S_n^2}\right)=r_n^2.
\]

Because the bracket is positive and \(r_0>0\), the unique positive root and state update are

\[
r_{n+1}=\frac{r_n}{\sqrt{1+\tau a^2\phi_n^2/S_n^2}},\qquad
\phi_{n+1}=\phi_n-\tau a\frac{r_{n+1}}{S_n}\phi_n.
\]

At every step with \(\phi_n\ne0\), one has \(0<r_{n+1}<r_n\); thus \(\widetilde E_n=r_n^2-C\) strictly decreases. The exact differential equation, by contrast, has solution \(\phi(t)=\phi_0e^{-at}\to0\).

**2. Sharp unshifted reversal branch.** With \(C=0\) and \(\phi_n\ne0\), \(S_n=\sqrt{a/2}\,|\phi_n|\), so the first recurrence gives \(r_n=\sqrt{a/2}\,\phi_0q^n\) and the second becomes

\[
\phi_{n+1}=\phi_n-t\phi_0q^{n+1}\operatorname{sgn}(\phi_n).
\]

The first step changes sign exactly if \(tq>1\), equivalent to \(t>1+\sqrt2\). As long as the resulting branch remains negative, subsequent increments are positive, and summing their geometric series yields, for every \(n\ge1\),

\[
\frac{\phi_n}{\phi_0}=1-tq+\frac{tq^2(1-q^{n-1})}{1-q},\qquad
\frac{\phi_\infty}{\phi_0}=1-tq+\frac{tq^2}{1-q}
=\frac{2q^2+3q-1}{2q}.
\]

The increasing branch stays strictly negative for every finite \(n\ge1\) if and only if its limiting value is nonpositive: at equality, it approaches zero strictly from below. Since \(q\) decreases with \(t\), this is equivalent to \(0<q\le(\sqrt{17}-3)/4\), or \(t\ge(11+3\sqrt{17})/4\). For \(1+\sqrt2<t<t_*\), the negative-branch formula would eventually become positive, proving that the first reversed-sign branch cannot last indefinitely. This proves both the exact limit and the stated sharpness, without asserting a classification of later sign flips.

**3. Uniform robust example with a strictly positive shift.** Put \(a=\phi_0=1\), \(\tau=100\), \(0<C\le1/2\). Here \(S_0^2=1/2+C\in(1/2,1]\) and \(r_0=S_0\le1\). Directly,

\[
\phi_1=1-\frac{100}{\sqrt{1+100/S_0^2}}<1-\frac{100}{15}=-\frac{17}{3},
\]

using \(1+100/S_0^2\le201<225\). Suppose the iterates have remained \(\phi_j<-4\) up to some step. Then \(S_j^2=\phi_j^2/2+C\le\phi_j^2\), giving

\[
0<r_{j+1}\le\frac{r_j}{\sqrt{101}}<\frac{r_j}{10},\qquad
0<\phi_{j+1}-\phi_j
=100r_{j+1}\frac{|\phi_j|}{S_j}
\le100\sqrt2\,r_{j+1}<150r_{j+1}.
\]

The same decay bound holds for the first auxiliary update, because \(S_0^2\le1\). Therefore \(r_j<10^{-j}\) for all \(j\ge1\) as long as the induction holds. The total movement *after* the first reversed step is consequently bounded by

\[
\sum_{j=2}^\infty(\phi_j-\phi_{j-1})
<150\sum_{j=2}^\infty10^{-j}=\frac53.
\]

Hence every partial sum satisfies \(\phi_n<-17/3+5/3=-4\), closing the induction. The sequence \(\phi_n\) is increasing from \(n=1\), bounded above by \(-4\), and has a limit below \(-4\) by the uniform strict bound; \(r_n\to0\) geometrically. Finally \(\phi_\infty^2/2>8\), while \(\widetilde E_n=r_n^2-C\downarrow-C\). All inequalities are analytic and hold for infinitely many steps, not merely checked samples.

## Verification

The accompanying `verify.py` independently implements the two scalar update equations with high-precision decimal arithmetic. It checks the closed-form recurrence and limit at and above the unshifted branch threshold, tests the exact update residuals and the strict bounds for representative positive shifts, and verifies the key rational inequalities used in the induction. Running `python verify.py` prints `VERIFY_OK`. These finite calculations are supplemental; the infinite-time statements follow from the preceding proof and explicit geometric-series bounds.

## Relationship to prior work

Huang, Liu, Wang and Yan (2026), equations (3.2)–(3.8), introduced precisely the positive-root quadratic-reformulated SAV-BE scheme and proved positivity and dissipation of a **modified** energy. Their analysis does not supply this exact long-time scalar reversal threshold or the strictly-positive-shift nonstationary limit. This result neither disputes their actual positivity/modified-energy theorems nor applies to their separately defined SAV-CN method.

The earlier weighted-SAV work of Huang, Jiang, Yang and Yuan (2024), especially sections 1–3, already explains that modified energy need not track physical energy and describes large-step physical-energy instability. It uses a different discrete auxiliary equation, involving \(2r_{n+1}(r_{n+1}-r_n)\), rather than the exact square difference used here. General statements about energy mismatch do not imply the present exact threshold or all-step positive-shift construction.

Related work on scalar-tracking and pullback-corrected SAV schemes discusses energy-state discrepancies and modified algorithms. Its abstract does not establish a covering result for the specifically defined 2026 positive-root scheme. No claim of exhaustive historical priority is made.

## Limitations

The sharp phase boundary is for the persistent *first reversed-sign branch* in the \(C=0\) scalar limit, not a complete classification of all stepsizes or subsequent crossings. Because \(C=0\) gives a zero radicand at \(\phi=0\), the source's globally positive-radicand hypothesis is supplied rigorously by the separate \(0<C\le1/2\) construction. The robust positive-shift example fixes \(a=\phi_0=1\), \(\tau=100\); no optimal timestep cutoff is claimed there. The result does not address higher-dimensional nonlinear models, corrected SAV variants, or small-step convergence rates. Finite checker runs are not substitutes for the all-step proof. Independent validation has not been performed.

## References

1. Q.-A. Huang, Z.-H. Liu, Y.-W. Wang, L.-N. Yan, *Positivity-preserving scalar auxiliary variable schemes for gradient flows via a quadratic reformulation*, arXiv:2610.01063v1 (October 1, 2026). https://arxiv.org/html/2610.01063v1
2. Q.-A. Huang, W. Jiang, J. Z. Yang, C. Yuan, *A weighted scalar auxiliary variable method for solving gradient flows: bridging the nonlinear energy-based and Lagrange multiplier approaches*, arXiv:2411.17403v1 (November 26, 2024). https://arxiv.org/html/2411.17403v1
3. S. Zhang, J. Shen, *Scalar-Tracking SAV Schemes with Pullback Corrections for Gradient Flows*, arXiv:2606.18551 (June 17, 2026). https://arxiv.org/abs/2606.18551
