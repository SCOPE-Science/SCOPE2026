# Exact finite-step risk for binary random Lie order and a three-state trace obstruction

## Finding

Let \(A=\left(\begin{smallmatrix}-a&a\\b&-b\end{smallmatrix}\right)\) and \(B=\left(\begin{smallmatrix}-c&c\\d&-d\end{smallmatrix}\right)\) be conservative two-state Markov generators in the row convention. Write \(s=a+b>0\), \(t=c+d>0\), \(u=e^{-sh}\), \(v=e^{-th}\), \(r=uv\), \(\pi_A=b/s\), and \(\pi_B=d/t\), for \(h>0\). Set
\[
q=\frac{\frac{s}{s+t}(1-r)-v(1-u)}{(1-u)(1-v)},\qquad
\Delta=(1-u)(1-v)(\pi_A-\pi_B).
\]
Use the full-length reverse order \(e^{hB}e^{hA}\) with probability \(q\), and \(e^{hA}e^{hB}\) otherwise, independently at each step. The single-step mean calibration is a corollary of the exact positive three-factor split [1], as explained below. Here the quantitative claim is the **exact finite-step mean-square error** from any deterministic initial probability row \(p_0\), for each integer \(n\ge1\):
\[
\mathbb E\|P_n-p_0 e^{nh(A+B)}\|_2^2
=2q(1-q)\Delta^2\frac{1-r^{2n}}{1-r^2}.
\]
For fixed \(T=nh>0\) and noncommuting generators, the risk is
\[
\frac{s^2t^2(\pi_A-\pi_B)^2}{4(s+t)}(1-e^{-2(s+t)T})h^3+o(h^3).
\]

There is also a **three-state affine obstruction at every positive step**. For
\[
A_3=\begin{pmatrix}-1&1&0\\1&-1&0\\0&0&0\end{pmatrix},\qquad
B_3=\begin{pmatrix}0&0&0\\0&-1&1\\0&0&0\end{pmatrix},
\]
no affine combination, even with arbitrary real coefficients summing to one, of the two full-length orders equals \(e^{h(A_3+B_3)}\) at any \(h>0\). By zero-block embedding the universal two-order exactness property fails in every dimension at least three.

## Assumptions and scope

All individual rates are nonnegative; one-way generators are allowed. If either generator is zero, both orders are exact and there is no random error. The formulas concern the Euclidean error of the random propagated probability vector, not exactness of a realized trajectory or simulation of a continuous-time Markov sample path. Both subflows are evaluated exactly. The independence assumption is across successive steps; the dimension-three example does not disallow exact fitting for special higher-dimensional pairs.

## Proof

**Calibration and its relation to the three-factor split.** For a row \((x,1-x)\), the first coordinate evolves under the individual flows as \(ux+(1-u)\pi_A\) and \(vx+(1-v)\pi_B\). Both full-length orders have slope \(r\). Their first-coordinate offsets are \(v(1-u)\pi_A+(1-v)\pi_B\) and \((1-u)\pi_A+u(1-v)\pi_B\), respectively. They differ by \(\Delta\).

In the row convention, [1] gives the exact split \(e^{(1-\vartheta)hA}e^{hB}e^{\vartheta hA}\) with \(0<\vartheta<1\) and \(e^{-s\vartheta h}=t(1-r)/((s+t)(1-v))\). Its scalar slope is \(r\), its coefficient of \(\pi_B\) is \(e^{-s\vartheta h}(1-v)\), and the two stationary weights add to \(1-r\). Consequently it is the affine interpolation of the two endpoint orders with reverse weight \((1-e^{-s\vartheta h})/(1-u)\), which is exactly the displayed \(q\) and belongs to \((0,1)\). Equality on all probability inputs gives equality of the full matrices. The weight is unique if \(\pi_A\ne\pi_B\), since the two orders differ; if \(\pi_A=\pi_B\), both orders are exact. In particular, the one-step mean is the joint semigroup, and fresh independence gives the exact mean at every step.

**Risk.** Write \(e_j\) for the difference between the random and exact first-state masses at step \(j\). Each random update uses the same slope \(r\), so \(e_{j+1}=r e_j+\xi_j\) with \(e_0=0\), where the \(\xi_j\) are independent centered variables with variance \(q(1-q)\Delta^2\). Iteration and the vanishing of cross covariances give \(\mathbb E e_n^2=q(1-q)\Delta^2\sum_{j=0}^{n-1}r^{2j}\). The probability-vector error is \((e_n,-e_n)\), yielding the claimed factor of two and the geometric denominator. For the small-step law, one may use
\[
q=\frac{s}{s+t}\frac{1}{1-e^{-sh}}-\frac{t}{s+t}\frac{1}{e^{th}-1}
=\tfrac12+\tfrac{s-t}{12}h+O(h^3).
\]
Also \(\Delta=st(\pi_A-\pi_B)h^2+O(h^3)\), \(1-r^2\sim2(s+t)h\), and \(r^{2n}=e^{-2(s+t)T}\). These yield the stated coefficient.

**Obstruction.** The last state of the displayed three-state pair is absorbing. On the transient block the generators are \(\widetilde A=\left(\begin{smallmatrix}-1&1\\1&-1\end{smallmatrix}\right)\) and \(\widetilde B=\operatorname{diag}(0,-1)\). By cyclicity the two orders have equal transient trace. The common trace is \(2e^{-3h/2}\cosh(h)\cosh(h/2)\); the exact transient trace is \(2e^{-3h/2}\cosh(\sqrt5h/2)\), since the traceless part of \(\widetilde A+\widetilde B\) squares to \((5/4)I\). The function \(z\mapsto\cosh(h\sqrt z)\) is strictly convex on \([0,\infty)\) by its power series for \(h>0\). At the midpoint of \(9/4\) and \(1/4\), strict Jensen gives
\[
\cosh(\sqrt5h/2)<\tfrac12(\cosh(3h/2)+\cosh(h/2))=\cosh(h)\cosh(h/2).
\]
The absorbing state adds one to each trace, and an affine combination retains the split trace. Thus no such combination is exact. Adding further absorbing states preserves the obstruction.

## Verification and relationship to prior work

The accompanying standard-library `verify.py` compares the binary transition matrices, enumerates all order sequences up to eight steps for selected pairs, and evaluates the trace inequality on a finite grid. These are checks of constants and implementations, not substitutes for the analytic risk and strict trace-gap arguments.

The binary exact-mean identity itself is covered by the three-factor result [1] through the interpolation above. Mean-exact selection of one rescaled subgenerator [2] is a different random experiment. Fair random-order splitting [3] already gives the \(h^{3/2}\) trajectory-error scale for general matrices; neither that scale nor abstract independent-innovation variance summation is claimed as new. The finite-step expression here gives the size of the residual fluctuations of calibrated full-length orders, including the dependence on rates and horizon even though the mean is exact. The explicit all-step obstruction concerns the same class of two-order schemes, without requiring the coefficients to be probabilities. The strict trace comparison is also consistent with the Golden–Thompson inequality on the symmetric transient blocks. Priority beyond the cited comparisons is not asserted.

## References

1. [An exact positive three-factor split for two-state Markov generators](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-an-exact-positive-three-factor-split-for-two-state-markov-genera--9b0eeef7eade/RESULT.md), Finding and Proof §2.
2. [Unique mean-exact calibration and a Cantor stationary law for randomized two-state generator splitting](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-unique-mean-exact-calibration-and-a-cantor-stationary-law-for-ra--543ac65eaf32/RESULT.md).
3. [A sharp Gaussian trajectory-error law for random-order Lie splitting](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-a-sharp-gaussian-trajectory-error-law-for-random-order-lie-split--38d8d8425ab3/RESULT.md).
