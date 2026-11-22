# Unequal two-site resetting: an exact stationary mode diagram in a harmonic diffusion

## Finding

Let \(X\) solve \(dX=-\kappa X\,dt+\sqrt{2D}\,dW\) between independent rate-\(r\) Poisson resets. At every reset set \(X=b\) with probability \(p\), and \(X=-b\) otherwise. Assume \(r,\kappa,D,b>0\), \(0<p<1\). Put \(\alpha=r/\kappa\), \(a=b\sqrt{\kappa/D}\), and \(y=x\sqrt{\kappa/D}\). Define, for \(\alpha>0\),
\[
\Psi_\alpha(z)=e^{-z^2/2}\int_0^\infty t^{\alpha-1}e^{-t^2/2-zt}\,dt,\qquad H_\alpha(z)=-\Psi_\alpha'(z).
\]
The stationary density has no strict local maxima outside the two reset sites and their intervening interval, and its complete mode classification is as follows.

When \(\alpha>1\), set
\[
q_*(\alpha,a)=\frac{H_\alpha(-a)}{H_\alpha(-a)+H_\alpha(a)}\in(1/2,1).
\]
There are exactly two strict modes, located at \(-a,+a\), if and only if \(1-q_*<p<q_*\). Otherwise there is exactly one strict mode at the more heavily reset site: \(+a\) when \(p\ge q_*\), and \(-a\) when \(p\le1-q_*\). The two-mode bias tolerance \(q_*\) strictly increases with separation \(a\).

When \(0<\alpha<1\), there exists a unique \(a_c(\alpha)>0\) satisfying \(H_\alpha(-a_c)=0\). For \(a\ge a_c\), there is exactly one strict mode in \((-a,a)\), for every \(p\in(0,1)\). For \(0<a<a_c\), set
\[
s_*(\alpha,a)=\frac{H_\alpha(-a)}{H_\alpha(-a)+H_\alpha(a)}\in(0,1/2).
\]
The unique mode is at \(-a\) if \(p\le s_*\), at \(+a\) if \(p\ge1-s_*\), and strictly inside \((-a,a)\) if \(s_*<p<1-s_*\). At either equality the mode remains unique at the indicated reset site.

At \(\alpha=1\) there is an exactly flat modal interval \([-a,a]\) if \(p=1/2\), a previously established symmetric-case phenomenon; otherwise the unique mode is the more heavily reset site. The new classification concerns the complete unequal-weight mode thresholds and the separation boundary.

## Assumptions and scope

All statements are for the unique stationary law of the one-dimensional linear Ornstein–Uhlenbeck diffusion with independently sampled, instantaneous, two-atom reset targets. The mode statements refer to maxima of the continuous stationary Lebesgue density (not atoms). All parameter ranges above are strict except as explicitly stated, and \(p=0,1\), \(r=0\), and noiseless diffusion are excluded. Exactly one or two modes occur, apart from the critical plateau.

## Proof

The renewal-resolvent formula is \(f(y)=\alpha\int_0^\infty e^{-\alpha t}\,[pG_t(y\mid a)+(1-p)G_t(y\mid-a)]\,dt\), where \(G_t\) is the Ornstein–Uhlenbeck transition density with unit mean-reversion and unit generator diffusion. It proves existence, uniqueness, positivity, continuity and unit normalization. Equivalently,
\[
f''+(yf)'-\alpha f+\alpha[p\delta_a+(1-p)\delta_{-a}]=0.
\]
A decaying homogeneous solution is \(\Psi_\alpha(y)\) at \(+\infty\) and \(\Psi_\alpha(-y)\) at \(-\infty\). Matching continuity and the derivative jumps \(f'(a+)-f'(a-)=-\alpha p\), \(f'(-a+)-f'(-a-)=-\alpha(1-p)\), yields, writing \(K=\alpha/[H_\alpha(-a)+\Psi_\alpha(-a)H_\alpha(a)/\Psi_\alpha(a)]>0\),
\[
 f(y)=K\begin{cases}
\big[p+(1-p)\Psi_\alpha(-a)/\Psi_\alpha(a)\big]\Psi_\alpha(-y),&y<-a,\\
p\Psi_\alpha(-y)+(1-p)\Psi_\alpha(y),&-a\le y\le a,\\
\big[1-p+p\Psi_\alpha(-a)/\Psi_\alpha(a)\big]\Psi_\alpha(y),&y>a.
\end{cases}
\]
Positivity of \(K\) also follows from the positive renewal density and the inner representation. On the exterior intervals, \(f\) increases toward \(-a\) and decreases away from \(+a\), since \(H_\alpha(z)>0\) for \(z>0\). On the inner interval, \(f''=(\alpha-1)f-yf'\); hence at a critical point, \(f''=(\alpha-1)f\). Every inner critical point is thus a strict minimum for \(\alpha>1\), a strict maximum for \(\alpha<1\), and there can be at most one (two successive critical points with the same strict extremum type are impossible). The one-sided slopes are
\[
f'(-a+)=K[pH_\alpha(a)-(1-p)H_\alpha(-a)],\qquad
f'(a-)=K[pH_\alpha(-a)-(1-p)H_\alpha(a)].
\]
For \(\alpha>1\), integration by parts gives \(H_\alpha(z)=(\alpha-1)e^{-z^2/2}\int_0^\infty t^{\alpha-2}e^{-t^2/2-zt}\,dt>0\). In particular \(H_\alpha(-a)>H_\alpha(a)\), and their ratio grows strictly with \(a\): the ratio of the two positive integrals has logarithmic derivative equal to the sum of two positive exponentially tilted means of \(t\). The slope signs yield the two-mode and one-mode regimes, including equality.

For \(0<\alpha<1\), the positive function \(\Psi_\alpha\) has \(\Psi_\alpha'(-\infty)>0\) (from \(\Psi_\alpha(-a)\sim\sqrt{2\pi}a^{\alpha-1}\)) and \(\Psi_\alpha'(0)<0\). At every zero of its derivative, \(\Psi_\alpha''=(\alpha-1)\Psi_\alpha<0\), so it has exactly one such zero. Consequently \(H_\alpha(-a)\) changes once from positive to negative. Moreover \(H_\alpha(a)>H_\alpha(-a)\): applying the same critical-point argument to the even sum \(\Psi_\alpha(a)+\Psi_\alpha(-a)\), whose second derivative at zero is negative, shows that its derivative remains negative for \(a>0\). The slope conditions then prove the subcritical regimes, with no unlisted extrema. For \(\alpha=1\), \(H_1(z)=e^{-z^2/2}\), making the inner derivative constant in sign or identically zero, completing the classification.

## Verification

`CHECK.py` implements the stated piecewise resolvent independently from numerical optimization: it evaluates the special-function solutions via parabolic-cylinder functions, compares stationarity and normalization, verifies derivative jumps and critical boundaries, and tests the mode classification on distinct parameter values. With `scipy>=1.11`, run `python CHECK.py`; its run passed 516 deterministic assertions. Numerical checks supplement the all-parameter analytic proof.

## Relationship to prior work

Olsen (2023) derives general moment identities for random-target stochastic resetting, including Ornstein–Uhlenbeck cases, but does not give this asymmetric two-target stationary-mode classification. The published symmetric two-site results listed below already establish the balanced \(p=1/2\) universal transition and plateau. Those findings do not imply the two distinct unequal-weight frontiers \(q_*(\alpha,a)\) and \(s_*(\alpha,a)\), nor the sharp subcritical separation \(a_c(\alpha)\). The exact one-site or symmetric-limit assertions are not claimed as new.

## Limitations

The analysis does not cover nonlinear confinement, non-Gaussian driving, random reset clocks, or more than two reset sites. The proof is analytic; the numerical checker is not an infinite-domain certificate. Literature priority has not been independently validated, and equivalent results in unindexed literature remain possible.

## References

- Kristian Stølevik Olsen, *Steady-state moments under resetting to a distribution* (2023), arXiv:2310.04840, https://arxiv.org/abs/2310.04840 (first public October 7, 2023).
- Trajanovski and collaborators, *Ornstein–Uhlenbeck process and generalizations: ... resetting* (2023), arXiv:2301.12304, https://arxiv.org/abs/2301.12304.
- *A separation-independent modality transition for two-site Ornstein–Uhlenbeck resetting*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-separation-independent-modality-transition-for-two-site-ornste--f8cae881c577 (symmetric reset weights).
- *Separation-independent modal transition for harmonically confined diffusion under symmetric resetting*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-separation-independent-modal-transition-for-harmonically-confine--a6b2a5417eeb (symmetric reset weights).
