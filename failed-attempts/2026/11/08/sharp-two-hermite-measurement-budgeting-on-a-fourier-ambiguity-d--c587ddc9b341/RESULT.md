# Sharp two-Hermite measurement budgeting on a Fourier-ambiguity disk

## Finding

There is an exact transition in the best allocation of a fixed total measurement budget between the normalized Gaussian and first Hermite short-time Fourier transform (STFT) windows. For every real \(T>0\), define
\[
\Gamma(T)=\max_{0\le w\le1}\ \min_{0\le s\le T}
 e^{-s}\bigl((1-w)+w(1-s)^2\bigr).
\]
This is the sharp least squared singular value of the two-channel pointwise ambiguity-recovery map, uniformly over the phase-space disk \(\pi(x^2+\xi^2)\le T\), when \(w\) of the total squared-channel measurement budget is assigned to the first Hermite window.

The complete optimizer classification is:

* If \(0<T<2\), the unique optimizer is \(w=0\), and \(\Gamma(T)=e^{-T}\).
* If \(T=2\), the complete optimizer set is \(0\le w\le1/2\), and \(\Gamma(2)=e^{-2}\).
* If \(T>2\), there is a unique optimal weight \(w_T\in(1/2,1)\). Let \(a_T\in(1,2)\) be the unique solution of
  \[
  2(a_T-1)e^{T-a_T}=T(T-2)+4a_T-a_T^2-2.
  \]
  Then
  \[
  w_T=\frac1{4a_T-a_T^2-2},\qquad
  \Gamma(T)=\frac{2(a_T-1)e^{-a_T}}{4a_T-a_T^2-2}
  =e^{-T}\bigl(1+w_T T(T-2)\bigr).
  \]
  The two worst-case radii are \(s=a_T\) and \(s=T\). The optimal squared margin exceeds the Gaussian-only margin strictly for every \(T>2\).

As \(T\to\infty\), the optimal budget and margin obey
\[
1-w_T\sim (T-1)^2 e^{1-T},\qquad
\Gamma(T)\sim (T-1)^2e^{-T}.
\]
In particular the improvement factor in squared margin over the Gaussian-only design grows quadratically in \(T\). At \(T=4\), \(w_T\approx0.6440631953\) and \(\Gamma(T)\approx0.1126870701\), against \(e^{-4}\approx0.0183156389\) for the Gaussian alone.

## Assumptions and scope

Use the unitary-frequency normalization
\[
V_g f(x,\xi)=\int_{\mathbb R} f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt,
\quad
\mathcal A f(x,\xi)=\int_{\mathbb R}f(t+x/2)\overline{f(t-x/2)}e^{-2\pi i\xi t}\,dt.
\]
The two real, unit-\(L^2\) windows are \(h_0(t)=2^{1/4}e^{-\pi t^2}\) and \(h_1(t)=2\sqrt\pi\,t h_0(t)\). For \(f\in L^2(\mathbb R)\), the two transformed squared-spectrogram channels are
\[
D_j(x,\xi)=\mathcal F_{\mathbb R^2}(|V_{h_j}f|^2)(\xi,-x)
=\mathcal A f(x,\xi)\,\overline{\mathcal A h_j(x,\xi)},\quad j\in\{0,1\}.
\]
For weight \(w\), assign channels scalar multipliers \(\sqrt{1-w}\) and \(\sqrt w\). The total squared weight is one. At a fixed phase-space point, the (unconstrained complex-error) least-squares inverse from this two-vector to the scalar \(\mathcal A f\) has exact operator norm
\[
\left((1-w)|\mathcal A h_0|^2+w|\mathcal A h_1|^2\right)^{-1/2}.
\]
Here “sharp” refers only to this pointwise inverse for arbitrary additive perturbations of the transformed intensity channels; it does not assert uniformly stable recovery of arbitrary original signals.

## Proof

**Window ambiguity factors.** Completing the square in the Gaussian integral, and using the Gaussian second moment for \(h_1\), gives
\[
\mathcal A h_0(x,\xi)=e^{-s/2},\qquad
\mathcal A h_1(x,\xi)=(1-s)e^{-s/2},\qquad
s=\pi(x^2+\xi^2).
\]
The identity \(D_j=\mathcal A f\overline{\mathcal A h_j}\) makes the two-channel forward operator a column vector. Its sole nonzero singular value squared is
\[
F_w(s)=e^{-s}\bigl[1+w(s^2-2s)\bigr].
\]
Cauchy–Schwarz proves that the pointwise weighted pseudoinverse has norm \(F_w(s)^{-1/2}\), and equality holds for an error vector parallel to the column. Hence maximizing the worst-case margin over the disk is exactly the stated optimization.

**Critical-point structure.** Direct differentiation yields
\[
F_w'(s)=e^{-s}\bigl[-1+w(-s^2+4s-2)\bigr].
\]
The quadratic in brackets never exceeds \(-1+2w\). For \(w\le1/2\), the function is nonincreasing on \([0,\infty)\), with a single stationary tangent at \((w,s)=(1/2,2)\); the minimum over the disk is \(F_w(T)\). For \(w>1/2\), there are exactly two critical radii
\[
s_-(w)=2-\sqrt{2-1/w}\in[1,2),\qquad
s_+(w)=2+\sqrt{2-1/w}\in(2,3],
\]
which are, respectively, a strict local minimum and maximum. Because \(F_w(0)=1\) is the global maximum of the pointwise ambiguity energy, the disk minimum for \(T>2\) is
\[
\min\{F_w(s_-(w)),F_w(T)\}.
\]
For \(T\le2\), the boundary value \(F_w(T)\) immediately gives the asserted optimizer when \(T<2\). At \(T=2\), \(F_w(2)=e^{-2}\) independently of \(w\); monotonicity establishes equality for \(w\le1/2\), whereas the strict local minimum at \(s_-(w)<2\) makes the margin smaller for \(w>1/2\).

**Unique balance for larger disks.** Fix \(T>2\). On \([0,1/2]\), the minimum \(F_w(T)=e^{-T}[1+wT(T-2)]\) strictly increases with \(w\). On \((1/2,1)\), this boundary value continues to increase, while the interior local-minimum value \(F_w(s_-(w))\) strictly decreases. Indeed, by stationarity its derivative with respect to \(w\) is \(e^{-s_-}s_-(s_--2)<0\). At \(w=1/2\), the interior value \(e^{-2}\) is strictly greater than \(F_{1/2}(T)\). At \(w=1\), the interior value vanishes while \(F_1(T)=e^{-T}(T-1)^2>0\). There is therefore exactly one crossing; the minimum of the increasing and decreasing branches is uniquely maximized there.

Set \(a=s_-(w)\). The critical-point equation rearranges to \(w=(4a-a^2-2)^{-1}\), and then
\[
F_w(a)=\frac{2(a-1)e^{-a}}{4a-a^2-2},\qquad
F_w(T)=\frac{e^{-T}[4a-a^2-2+T(T-2)]}{4a-a^2-2}.
\]
Equating them gives the stated transcendental equation, with a unique solution in \((1,2)\) by the preceding crossing argument.

**Large-disk limit.** Write \(a_T=1+\delta_T\). The balance equation becomes
\[
2\delta_T e^{T-1-\delta_T}=(T-1)^2+2\delta_T-\delta_T^2.
\]
Since its left-hand side grows exponentially at fixed positive \(\delta_T\), necessarily \(\delta_T\to0\); rearrangement then gives \(2\delta_T\sim (T-1)^2e^{1-T}\). Because \(4a_T-a_T^2-2=1+2\delta_T-\delta_T^2\), the asserted weight and margin asymptotics follow.

## Verification

Run `python CHECK.py` with Python, NumPy, SciPy and SymPy. It independently evaluates the Gaussian ambiguity integrals by quadrature, checks the derivative and balance reductions symbolically, compares the analytic maximin with scalar numerical optimization over a range of disk radii, verifies the \(T=4\) values, and tests the large-disk asymptotics. The expected output is `ALL_SHARP_HERMITE_MINIMAX_CHECKS_PASSED`. The unrestricted proof above, rather than these samples, establishes the results for every \(T>0\).

## Relationship to prior work

Bertolini, de Dios Pont, Pineau, Ramos and Taylor (2026) prove local \(L^2\) STFT phase-retrieval stability for Gaussian and Hermite windows at appropriate signals. Their local signal-space result does not give a sharp **two-channel pointwise ambiguity-inversion budget** on a prescribed disk.

Alaifari and Yang (first posted October 2024) introduce multi-window STFT reconstruction and investigate joint Hermite ambiguity coverage. Their formulas include \(\mathcal A h_n=e^{-s/2}L_n(s)\); their partition-based coverage algorithm and stability estimates do not state the complete optimal allocation or the radius-dependent transition above. This known Laguerre identity is used as an ingredient, not claimed as a new formula.

## Limitations

The result concerns the fixed pair of unit-normalized Hermite windows of orders zero and one, fixed channel weights, and radial disks. The noise amplifier refers to the pointwise linear inversion of Fourier-transformed **squared** spectrogram channels with arbitrary complex additive errors. It does not bound the nonlinear recovery of \(f\) from physically realizable magnitude noise, nor claim optimality among other window choices, signal-dependent weights, or noncircular domains. Priority relative to other weight-design work outside the inspected literature remains open to external review.

## References

1. S. Bertolini, J. de Dios Pont, B. Pineau, J. P. G. Ramos and M. A. Taylor, *\(L^2\)-Stability for STFT phase retrieval*, arXiv:2605.20527, first posted 2026-05-19. https://arxiv.org/abs/2605.20527
2. R. Alaifari and Y. Yang, *Multi-window approaches for direct and stable STFT phase retrieval*, arXiv:2410.05486, first posted 2024-10-07; journal version SIAM J. Appl. Math. 85 (2025), 2376–2398. https://arxiv.org/abs/2410.05486
3. D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507, first posted 2026-05-29. https://arxiv.org/abs/2605.31507
