# Sharp weak-cutoff carrying threshold for localized ecological trait distributions

## Finding

In a cutoff reaction–diffusion model with competition for a globally shared resource, let \(\kappa_{\max}(\varepsilon,D)\) be the largest global-competition coefficient for which a finite-mass, positive, even, single-peaked stationary trait distribution exists. If the cutoff \(\varepsilon\downarrow0\) and the trait-diffusion coefficient \(D>0\) is fixed, then

\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\sqrt D\,\kappa_{\max}(\varepsilon,D)=\frac15\left(\frac35\right)^{3/2}=\frac{3\sqrt{15}}{125}.}
\]

For **every** maximizing choice of the effective global mortality \(r_\varepsilon=\kappa_{\max}M_\varepsilon\), \(r_\varepsilon\to3/5\) and the pulse height satisfies \(\max_x\phi_\varepsilon(x)/\varepsilon\to\sqrt{5/2}\). In the coordinate \(y=x/\sqrt D\), the normalized maximizing profile \(\phi_\varepsilon(\sqrt D\,y)/\varepsilon\) tends locally uniformly to

\[
u_*(y)=\begin{cases}
\sqrt{5/2}\cos(\sqrt{2/5}\,y),& |y|\le a_*,\\
\exp[-\sqrt{3/5}(|y|-a_*)],& |y|\ge a_*,
\end{cases}\quad
 a_*=\sqrt{5/2}\arcsin\sqrt{3/5}.
\]

At every sufficiently small cutoff there is at least one positive stationary pulse when \(\kappa=\kappa_{\max}\), at least two distinct pulses for each \(0<\kappa<\kappa_{\max}\), and none in the specified class for \(\kappa>\kappa_{\max}\). These assertions do **not** claim uniqueness of the maximizing pulse or its dynamical stability at finite cutoff.

## Assumptions and scope

Fix \(D>0\), \(0<\varepsilon<1/\sqrt3\), and \(\kappa>0\). The ecological trait density solves

\[
\partial_t\phi=D\partial_{xx}\phi+\phi\Theta(\phi-\varepsilon)-\phi^2-\kappa M(t)\phi,
\qquad M(t)=\int_{\mathbb R}\phi(x,t)\,dx.
\]

The cutoff is a sharp reproduction switch (the value assigned to the Heaviside function exactly at its threshold does not alter the continuous stationary matching). The theorem concerns nonzero, positive, symmetric, decreasing-on-the-positive-half-line, finite-mass stationary pulses, with continuously differentiable profiles and piecewise twice differentiable profiles, which vanish at spatial infinity. Translation of a pulse does not create a different shape. Write \(r=\kappa M\) and \(b=1-r\). The source's mechanical-potential existence condition is \(0<r<r_c(\varepsilon)=1-3^{1/3}\varepsilon^{2/3}\). Its turning-point peak \(A=A_\varepsilon(r)\in(\varepsilon,b)\) is the smaller positive root of

\[
\varepsilon^2=bA^2-\frac23 A^3.
\]

No independent statement about a discrete-individual stochastic system is made.

## Proof

**1. Exact stationary mass.** The energy integral of the stationary ODE reads \(D(\phi')^2/2+U(\phi)=0\), where

\[
U(v)=\begin{cases}
-rv^2/2-v^3/3,&0\le v<\varepsilon,\\
bv^2/2-v^3/3-\varepsilon^2/2,&v\ge\varepsilon.
\end{cases}
\]

Integrating \(M=2\int_0^\infty\phi(x)\,dx\) on the decreasing half-pulse gives exactly

\[
\frac{M_\varepsilon(r,D)}{2\sqrt D}
=\int_0^\varepsilon\frac{dv}{\sqrt{r+2v/3}}
+\int_\varepsilon^{A_\varepsilon(r)}\frac{v\,dv}
{\sqrt{\varepsilon^2-(1-r)v^2+2v^3/3}}.
\tag{1}
\]

Each \(0<r<r_c\) gives one symmetric pulse up to translation, with corresponding \(\kappa_\varepsilon(r,D)=r/M_\varepsilon(r,D)\). The mass diverges logarithmically as \(r\uparrow r_c\), where the turning point merges with the potential maximum. Conversely, \(\kappa_\varepsilon\to0\) as \(r\downarrow0\), since the mass is bounded away from zero. Therefore this positive continuous curve vanishes at both ends and attains an interior maximum. Every competition strength strictly between zero and the maximum occurs on each side of a maximizing point, hence yields at least two distinct stationary pulses. The spatial change \(x=\sqrt D\,y\) gives the exact diffusivity identity \(\kappa_{\max}(\varepsilon,D)=D^{-1/2}\kappa_{\max}(\varepsilon,1)\).

**2. The mass limit for fixed effective mortality.** Fix \(r\in(0,1)\) and take \(\varepsilon\downarrow0\). The turning equation implies \(A_\varepsilon(r)/\varepsilon\to 1/\sqrt{1-r}\). The first integral in (1), divided by \(\varepsilon\), tends to \(1/\sqrt r\). In the second set \(v=\varepsilon z\). Then, using an endpoint-square-root substitution to control the integrable turning-point singularity, its quotient by \(\varepsilon\) tends to

\[
\int_1^{1/\sqrt{1-r}}\frac{z\,dz}{\sqrt{1-(1-r)z^2}}=\frac{\sqrt r}{1-r}.
\]

These limits are uniform on every compact subset of \((0,1)\), because the smaller turning point is simple there. Thus

\[
\frac{M_\varepsilon(r,D)}{2\varepsilon\sqrt D}\longrightarrow\frac1{\sqrt r(1-r)},\qquad
\varepsilon\sqrt D\,\kappa_\varepsilon(r,D)\longrightarrow F(r)=\frac12 r^{3/2}(1-r),
\tag{2}
\]

uniformly on compact subintervals of \((0,1)\).

**3. Exclusion of escaping maximizers.** The first integral of (1) supplies the global lower bound

\[
M_\varepsilon(r,D)\ge \frac{2\varepsilon\sqrt D}{\sqrt{r+2\varepsilon/3}},
\qquad \varepsilon\sqrt D\,\kappa_\varepsilon(r,D)\le\frac r2\sqrt{r+2\varepsilon/3}.
\tag{3}
\]

This controls maximizing sequences with \(r\to0\). On the other side, throughout the pulse the stationary equation gives \(\phi''\ge-(1-r)A/D\): below the threshold the curvature is nonnegative, and above it \(\phi''=\phi(\phi-(1-r))/D\ge-(1-r)A/D\). Integrating twice from the peak yields \(\phi(x)\ge A/2\) for \(|x|\le\sqrt{D/(1-r)}\). From \(\varepsilon^2=A^2[(1-r)-2A/3]\le(1-r)A^2\), it follows that

\[
M_\varepsilon(r,D)\ge A\sqrt{D/(1-r)}\ge\frac{\varepsilon\sqrt D}{1-r},\qquad
\varepsilon\sqrt D\,\kappa_\varepsilon(r,D)\le r(1-r).
\tag{4}
\]

Hence maximizing sequences cannot have \(r\to1\). Since the fixed trial choice \(r=3/5\) gives \(F(3/5)>0\), (3)–(4) force every maximizing sequence into a compact subinterval of \((0,1)\). Compact uniform convergence in (2) and the unique strict global maximizer of \(F\), determined by \(F'(r)=\tfrac14\sqrt r(3-5r)\), imply \(r_\varepsilon\to3/5\). Substitution into (2) proves the boxed limiting carrying threshold.

**4. Height and shape.** The peak equation and convergence of \(r_\varepsilon\) give \(A_\varepsilon/\varepsilon\to\sqrt{5/2}\). With \(u_\varepsilon(y)=\phi_\varepsilon(\sqrt D\,y)/\varepsilon\), the stationary equation becomes

\[
u_\varepsilon''+u_\varepsilon\Theta(u_\varepsilon-1)-r_\varepsilon u_\varepsilon-\varepsilon u_\varepsilon^2=0.
\]

On the interval above the threshold, continuous ODE dependence gives the limiting solution \(u=\sqrt{5/2}\cos(\sqrt{2/5}\,y)\). Its first crossing of one is at \(a_*=\sqrt{5/2}\arcsin\sqrt{3/5}\), with derivative \(-\sqrt{3/5}\). Below the threshold, the limiting decaying solution of \(u''-(3/5)u=0\) is exactly the stated exponential. Integrability and the transversality of the crossing give locally uniform convergence across the matching point, and evenness gives the negative half-line.

## Verification

The standalone `verify.py` checks the turning-point root, computes both integrals in (1) by a nonsingular substitution, tests the exact \(D^{-1/2}\) scaling, and compares the small-cutoff optimum and fixed-\(r\) mass with the proved constants. Numerical maximization is **not** used to prove global optimality. For \(D=1\), at \(\varepsilon=10^{-5}\) the numerical maximizer is approximately \(r=0.5999891\) and \(\varepsilon\kappa\approx0.0929494\), versus the proved limit \(0.0929516003\). The analytic endpoint inequalities (3)–(4) complete the maximizer argument beyond the finite computations.

## Relationship to prior work

Kessler and Shnerb (2026), Sec. II and Appendix B, construct the same localized pulse family and the self-consistency curve \(\kappa=r/M\), observe a finite-cutoff fold numerically, and analyze broad, near-Maxwell-point pulses with height of order \(\varepsilon^{2/3}\) at **fixed** competition strength. Those facts are premises here, not new claims. The present result instead determines the **global maximum** of permissible competition in the singular weak-cutoff limit, its exact leading coefficient, the selected effective mortality \(3/5\), and the limiting threshold-scale cosine/exponential profile. That regime has pulse height of order \(\varepsilon\), distinct from the source's broad fixed-\(\kappa\) branch. Maruvka and Shnerb (2007) consider moving invasion fronts with finite-range nonlocal competition rather than a globally self-consistent stationary capacity fold. The possibility of other mathematically equivalent earlier formulations remains a priority risk.

## Limitations

This is an asymptotic result for a sharp-threshold deterministic one-dimensional trait-space equation; no error rate in \(\varepsilon\) is proved. Finite-cutoff uniqueness/nondegeneracy of the competition maximizer, stability, long-time selection, stochastic survival, and arbitrary nonsymmetric/multipeak solutions are not asserted. The original paper already establishes the existence and mechanical energy parameterization of the pulse family. The literature comparison is bounded; scientific priority has not been independently audited.

## References

1. D. A. Kessler and N. M. Shnerb, *Diversification under Global Competition: A Cutoff-Induced Localization Mechanism*, arXiv:2611.16887v1, first submitted 2026-11-12, https://arxiv.org/html/2611.16887v1 (Secs. II, Appendices A and B).
2. Y. E. Maruvka and N. M. Shnerb, *Nonlocal competition and front propagation in branching-coalescence systems*, Physical Review E **75**, 042901 (2007), https://doi.org/10.1103/PhysRevE.75.042901.
