# A reset-rate threshold for singular static response at an unstable double-well equilibrium

## Finding
For a deterministically evolving particle in a quartic double-well, independent Poisson resetting exactly to its unstable equilibrium produces a sharp transition in its **stationary response to a weak constant field**. Set \(x_s=\sqrt{a/b}\), \(h=A/(a x_s)\), and \(\rho=r/a\). Let \(m(h,\rho)=\mathbb E[X]/x_s\) denote the normalized stationary mean. For each fixed \(\rho>0\), as \(h\downarrow0\),
\[
m(h,\rho)\sim
\begin{cases}
\frac12 B\bigl(\frac{1-\rho}{2},1+\frac{\rho}{2}\bigr)h^\rho,&0<\rho<1,\\
h\log(1/h),&\rho=1,\\
\frac{h}{\rho-1},&\rho>1.
\end{cases}
\]
Thus the right static susceptibility is infinite for \(0<r\le a\) but equals \(1/(r/a-1)\) in normalized units for \(r>a\). There is a sharp continuous critical crossover. For every fixed \(\lambda\in\mathbb R\), with \(L=\log(1/h)\) and \(\rho_h=1+\lambda/L\),
\[
\lim_{h\downarrow0}\frac{m(h,\rho_h)}{hL}=
F(\lambda):=\begin{cases}(1-e^{-\lambda})/\lambda,&\lambda\ne0,\\1,&\lambda=0.\end{cases}
\]
The crossover is also locally uniform for \(\lambda\) in compact real intervals. For negative \(h\), the stationary mean is odd in \(h\). All statements concern exact point resetting and **autonomous, noise-free inter-reset dynamics**, not finite-frequency signal resonance.

## Assumptions and scope
Let \(a,b,r>0\). Between the jump times of an independent homogeneous Poisson process of rate \(r\), solve
\[
\dot X(t)=aX(t)-bX(t)^3+A,
\]
with every jump setting \(X=0\), including an initial post-reset state \(X(0)=0\). The external field \(A\) is constant, not periodic, and there is no independent Brownian forcing. The stationary regime is the unique renewal stationary law associated with an exponential reset age. Write \(s=at\), \(y=X/x_s\), \(h=A/(a x_s)\), and \(\rho=r/a\), so that \(dy/ds=h+y-y^3\). For the results above \(h\) approaches zero at fixed \(\rho\) or in the stated moving-rate window. At exactly \(h=0\), resetting to the unstable equilibrium leaves the trajectory identically zero.

## Proof
**1. Renewal formula.** By odd symmetry it suffices to take \(h>0\). Let \(y_+(h)>1\) be the largest positive root of \(h+y-y^3=0\). The solution \(y_h(s)\) starting at zero is strictly increasing and tends to \(y_+(h)\). Its first hitting time of a level \(0<z<y_+(h)\) is
\[
\tau_h(z)=\int_0^z\frac{du}{h+u-u^3}.
\]
The stationary reset age \(S\) is exponential of rate \(\rho\); by Fubini's tail formula for the bounded nonnegative variable \(y_h(S)\),
\[
m(h,\rho)=\rho\int_0^\infty e^{-\rho s}y_h(s)\,ds
=\int_0^{y_+(h)}\exp[-\rho\tau_h(z)]\,dz.\tag{1}
\]
This identity fixes both the normalization and all endpoint effects.

**2. Universal short-distance comparison.** As \(h+y-y^3\le h+y\) on the positive path,
\[
\tau_h(y)\ge\log(1+y/h),\qquad
0\le e^{-\rho\tau_h(y)}\le(1+y/h)^{-\rho}.\tag{2}
\]
For any fixed \(0<\eta<1\), write
\[
\tau_h(y)=\log(1+y/h)+R_h(y),\quad
R_h(y)=\int_0^y\frac{u^3}{(h+u-u^3)(h+u)}\,du.
\]
For \(0\le y\le\eta\), using \(h+u-u^3\ge(1-\eta^2)(h+u)\),
\[
0\le R_h(y)\le\frac{\eta^2}{2(1-\eta^2)}.\tag{3}
\]
For every fixed \(0<y<1\), dominated convergence for the remainder gives
\[
R_h(y)\longrightarrow-\tfrac12\log(1-y^2),\qquad
h^{-\rho}e^{-\rho\tau_h(y)}\longrightarrow y^{-\rho}(1-y^2)^{\rho/2}.\tag{4}
\]
The stable endpoint obeys \(y_+(h)=1+O(h)\) and is bounded uniformly for small \(h\).

**3. Subcritical reset rates.** For \(0<\rho<1\), the majorant in (2) yields \(h^{-\rho}e^{-\rho\tau_h(y)}\le y^{-\rho}\) for \(y\in(0,1)\). The short extension from \(1\) to \(y_+(h)\) contributes at most \(O(h)=o(h^\rho)\). Applying dominated convergence to (1) and (4) gives
\[
\lim_{h\downarrow0}\frac{m(h,\rho)}{h^\rho}
=\int_0^1y^{-\rho}(1-y^2)^{\rho/2}\,dy
=\tfrac12B\bigl((1-\rho)/2,1+\rho/2\bigr).
\]
The beta integral is positive and finite precisely for \(0<\rho<1\).

**4. Supercritical rates.** For \(\rho>1\), substitute \(y=hv\) in (1). At every fixed \(v\ge0\), \(\tau_h(hv)\to\log(1+v)\). Inequality (2) supplies the integrable majorant \((1+v)^{-\rho}\). Extension by zero for \(v>y_+(h)/h\) permits dominated convergence on \([0,\infty)\):
\[
\lim_{h\downarrow0}\frac{m(h,\rho)}h
=\int_0^\infty(1+v)^{-\rho}\,dv=\frac1{\rho-1}.
\]

**5. Critical window.** Let \(L=\log(1/h)\) and \(\rho_h=1+\lambda/L\). Split (1) at any fixed \(0<\eta<1\). The region \([\eta,y_+(h)]\) contributes \(O_{\eta,\lambda}(h^{\rho_h})=O_{\eta,\lambda}(h)\), by (2). On \([0,\eta]\), (3) squeezes the contribution between \(e^{-\rho_h\eta^2/[2(1-\eta^2)]}J_h\) and \(J_h\), where
\[
J_h=\int_0^\eta(1+y/h)^{-\rho_h}\,dy
=h\,\frac{1-(1+\eta/h)^{-\lambda/L}}{\lambda/L}
\]
with its continuous logarithmic interpretation at \(\lambda=0\). Since \(\log(1+\eta/h)/L\to1\), \(J_h/(hL)\to F(\lambda)\). Divide the squeeze by \(hL\), take \(h\downarrow0\), then \(\eta\downarrow0\): both bounds tend to \(F(\lambda)\). The estimates and the limit for \(J_h\) are uniform for \(\lambda\) in compact sets, proving local uniformity. The \(\rho=1\) asymptotic is the \(\lambda=0\) case.

**6. Negative field and susceptibility.** Uniqueness of the ODE solution gives \(y_{-h}(s)=-y_h(s)\), hence \(m(-h,\rho)=-m(h,\rho)\). All positive-side coefficients are nonzero. Therefore \(m(h,\rho)/h\to\infty\) when \(\rho\le1\), and \(\to(\rho-1)^{-1}\) when \(\rho>1\). Since \(m(0,\rho)=0\), these are the right difference-quotient susceptibilities.

## Verification
The self-contained `checker.py` integrates the deterministic flow together with the exponentially weighted stationary mean, and compares positive-mean ordering, the three weak-field coefficients, and three critical-window values. Its execution passed 31 finite numerical/asymptotic consistency checks. These checks test normalization and constants; the proof of all infinite limits is analytic, through (1)–(4). Run with `python checker.py` using Python 3, SciPy and the standard library. No random numbers or external data are used.

## Relationship to prior work
Wang et al. (2026) introduce the same cubic bistable dynamics and Poisson resetting for **periodically driven** weak-signal amplification. Their exact periodic renewal framework (including supplemental Sec. S1) and logarithmic reset-to-well phase-selection time are prior work. This result analyzes the distinct autonomous \(\omega=0\) field limit at fixed positive reset rate, proves a rate-indexed static response law with an exact beta-function amplitude, and derives a moving-rate crossover. A coarse-grained late well-selection time does not determine this exact stationary mean, which includes the entire path before arrival in a well. The general exponential-age renewal formula is standard and not claimed as new.

The reset-process spectral framework of Rose et al. (2018) and Evans and Sunil's (2024) lecture notes provide broader background, not the stated nonlinear static-response classification. Targeted literature and indexed-result searches did not identify a mathematically covering statement, but an implicit formulation or result elsewhere cannot be excluded.

## Limitations
There is no thermal noise between resets and no spatial dispersion of the reset point. The crossover is a weak-*static*-field result; it is not a finite-frequency gain theorem. Its constant depends on cubic saturation, while the leading exponents and critical location reflect the local unstable linearization. We do not assert experimental observability in a noisy device, nor publication priority without independent review. The critical susceptibility diverges as a difference quotient; no finite derivative at the origin is asserted there.

## References
1. W. Wang, K. Li, J. Zhu, A. G. Cherstvy, R. Metzler, and Y. Xu, *Weak-Signal Amplification through Stochastic Resetting*, arXiv:2611.01991v1, first submitted 2026-11-01. https://arxiv.org/html/2611.01991v1
2. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Phys. Rev. E 98, 022129 (2018), arXiv:1806.01298. https://arxiv.org/abs/1806.01298
3. M. R. Evans and J. C. Sunil, *Stochastic Resetting and Large Deviations*, arXiv:2412.16374v1, first submitted 2024-12-20. https://arxiv.org/abs/2412.16374
