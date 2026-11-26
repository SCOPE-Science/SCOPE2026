# A sharp velocity–reset threshold for which initial search phase wins at a fixed target distance

## Finding

Consider a one-dimensional searcher switching between diffusion (the only phase that can detect a target) and undetecting ballistic relocations. Complete Poisson resets return the particle to its original location and its selected initial phase. There is a **sharp and complete classification** of which starting phase minimizes mean detection time at any prescribed distance. If \(v^2\le D(r+\beta)\), diffusion is strictly better at every distance; if \(v^2>D(r+\beta)\), exactly one positive distance changes the preference, from diffusion nearby to ballistic initialization farther away. The threshold is explicit and does not depend on an approximation or numerical phase diagram.

## Assumptions and scope

Fix finite \(D,v,\alpha,\beta,r>0\). The searcher is on \(\mathbb R\), begins at distance \(x\ge0\) from an absorbing target at the origin, and can detect it only while diffusing with generator \(D\partial_{xx}\). It leaves the diffusive mode at rate \(\alpha\), choosing velocity \(+v\) or \(-v\) with equal probabilities, and each ballistic mode returns to diffusion at rate \(\beta\). Independent Poisson resets of rate \(r\) instantaneously restore both position and the specified initial mode; ballistic initialization means an independent fair choice of direction at every renewal. Let \(T_D(x;r)\) and \(T_B(x;r)\) be the corresponding finite mean detection times, including time in all phases. The boundary point \(x=0\) is included for algebraic completeness: diffusive initialization then detects immediately, but ballistic initialization need not.

Put \(\lambda=r+\beta\), \(R=r\lambda/v^2\). Define \(0<\mu_-<\mu_+\) by the two positive roots \(\mu_-^2,\mu_+^2\) of

\[
P(t)=Dv^2t^2-[(r+\alpha)v^2+D\lambda^2]t+r\lambda(r+\alpha+\beta).
\]

If \(v^2>D\lambda\), set

\[
x_* = \frac{1}{\mu_+-\mu_-}\log\!\left[\frac{\mu_-(\mu_+^2-R)}{\mu_+(\mu_-^2-R)}\right].
\]

The complete comparison is:

\[
\begin{array}{ll}
v^2\le D\lambda &: T_D(x;r)<T_B(x;r)\quad\text{for every }x\ge0,\\
v^2>D\lambda &: T_D(x;r)<T_B(x;r)\ (0\le x<x_*),\\
& T_D(x_*;r)=T_B(x_*;r),\\
& T_D(x;r)>T_B(x;r)\ (x>x_*).
\end{array}
\]

## Proof

**Step 1: distinct real decay rates.** One has \(P(0)=r\lambda(r+\alpha+\beta)>0\) and

\[
P(\lambda^2/v^2)=-\alpha\beta\lambda<0.
\]

Since \(Dv^2>0\), the roots are simple, positive and satisfy \(0<\mu_-^2<\lambda^2/v^2<\mu_+^2\). Define \(H_\pm=\lambda^2/(v^2\mu_\pm)-\mu_\pm\). Then \(H_->0>H_+\), and \(\Delta=H_--H_+>0\).

**Step 2: transform of one resetting-free detection excursion.** At discount \(s=r\), the spatial Fourier transform of the diffusive-state resolvent with a diffusive start is

\[
\mathcal G_D(k)=\left[r+\alpha+Dk^2-\frac{\alpha\beta\lambda}{\lambda^2+v^2k^2}\right]^{-1}.
\]

For a fair ballistic start, the corresponding diffusive-state resolvent is \(\mathcal G_B(k)=\beta\lambda\,\mathcal G_D(k)/(\lambda^2+v^2k^2)\). A first-detection decomposition at the origin (detection occurs only in the diffusive phase) gives \(F_D=\mathcal G_D(x)/\mathcal G_D(0)\) and \(F_B=\mathcal G_B(x)/\mathcal G_D(0)\), where \(F_i(r,x)=\mathbb E[e^{-r\tau_i}]\) for the **unreset** detection time \(\tau_i\). Partial fractions in \(k^2\) and inverse Fourier transformation give

\[
F_D=\frac{H_-e^{-\mu_-x}-H_+e^{-\mu_+x}}{\Delta},\qquad
F_B=\frac{\beta\lambda}{v^2\mu_-\mu_+}\frac{\mu_+e^{-\mu_-x}-\mu_-e^{-\mu_+x}}{\Delta}.
\]

The second coefficient simplifies using the characteristic polynomial, giving the exact comparison

\[
\Delta(F_B-F_D)=A e^{-\mu_-x}+B e^{-\mu_+x},\qquad
A=\frac{\mu_-^2-R}{\mu_-},\qquad B=\frac{R-\mu_+^2}{\mu_+}<0.
\]

At \(x=0\) the right side equals \((\mu_--\mu_+)\bigl(1+R/(\mu_-\mu_+)\bigr)<0\). In particular diffusion wins at the target.

**Step 3: determine the sign of the slow coefficient.** The exact identity

\[
P(R)=r\lambda\beta\left(1-\frac{D\lambda}{v^2}\right)
\]

has a decisive sign. Since \(0<R<\lambda^2/v^2<\mu_+^2\), the upward quadratic implies \(A>0\) if and only if \(v^2>D\lambda\); otherwise \(A\le0\). When \(A\le0\), both terms in the comparison are nonpositive, and the \(B\) term is strictly negative. When \(A>0\), the sign of the difference is the sign of \(A+B e^{-(\mu_+-\mu_-)x}\), a strictly increasing function of \(x\), negative at zero and tending to \(A>0\). It therefore has exactly one zero, necessarily positive; solving gives the displayed \(x_*\).

**Step 4: convert to reset mean first-detection times.** Renewal at each complete Poisson reset yields

\[
T_i(x;r)=\frac{1-F_i(r,x)}{rF_i(r,x)}\quad (i=D,B).
\]

For \(x>0\), both transforms are strictly between zero and one. The displayed expression is strictly decreasing in \(F_i\), so the sign of \(T_D-T_B\) is opposite the sign of \(F_D-F_B\). Together with Step 3 this proves the complete classification. At \(x=0\), diffusion detects immediately, preserving the strict inequality.

## Verification

The accompanying `CHECK.py` independently evaluates resolvent Fourier integrals by oscillatory quadrature and compares them with both explicit transforms. It checks the polynomial identity at rational parameter points and the unique-crossing signs across 240 randomized positive parameter sets, and reports 845 passing diagnostic assertions. This finite verification is supplementary; the proof of uniqueness and of the all-parameter inequalities is analytic.

For example, \(D=\alpha=\beta=r=1\) and \(v=\sqrt5\) satisfy \(v^2>D(r+\beta)\). Then \(\mu_-\approx0.7267875971\), \(\mu_+\approx1.5072424452\), and \(x_*\approx2.5004560358\).

To reproduce, use Python 3 with NumPy and SciPy and run `python CHECK.py` in the directory containing that file. Its numerical tests use fixed seeded random parameters.

## Relationship to prior work

Flaquer-Galmés, Campos and Méndez, *Intermittent random walks under stochastic resetting* (arXiv:2401.16849, first publicly posted January 30, 2024; Physical Review E 109, 034103, 2024), derive the intermittent model, the two initial-mode first-passage transforms and Poisson-renewal mean times. Those ingredients are **not new here**. Their parameter studies optimize the reset and switching rates separately for each starting mode and describe distinct numerical optimization regions. The contribution proved here is the exact, all-positive-parameter **direct preference comparison between initial modes**, its unique positive crossing, and the necessary-and-sufficient speed boundary \(v^2=D(r+\beta)\) independent of \(\alpha\). This is a theorem-level consequence of their formulas; potential implicit or equivalent coverage in other literature remains an originality risk.

The broader intermittent-search context is reviewed by Bénichou, Loverdo, Moreau and Voituriez, *Intermittent search strategies*, Reviews of Modern Physics 83, 81 (2011). Related research on persistent two-level resetting clocks addresses different switching mechanisms rather than the blind-ballistic initial-mode comparison.

## Limitations

The claim concerns fixed positive parameters, one stationary target on the unbounded line, equal ballistic directions at initialization, ballistic blindness, and complete independent Poisson resets that reproduce the initial phase. It does not compare initial states after reoptimizing reset or switching rates, finite resetting durations, random target distributions, finite sensing radii, or asymmetric relocation velocities. Algebraic derivability from published transform formulas is explicitly acknowledged; independent literature validation and experimental tests have not been performed.

## References

1. R. Flaquer-Galmés, D. Campos, and V. Méndez, *Intermittent random walks under stochastic resetting*, arXiv:2401.16849 (first public version January 30, 2024), https://arxiv.org/abs/2401.16849; *Phys. Rev. E* **109**, 034103 (2024), https://doi.org/10.1103/PhysRevE.109.034103.
2. O. Bénichou, C. Loverdo, M. Moreau, and R. Voituriez, *Intermittent search strategies*, *Rev. Mod. Phys.* **83**, 81 (2011), https://doi.org/10.1103/RevModPhys.83.81.
