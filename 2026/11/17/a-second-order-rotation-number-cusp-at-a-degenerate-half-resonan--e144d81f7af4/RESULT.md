# A second-order rotation-number cusp at a degenerate half-resonance tongue edge

## Finding
Fix real \(a>0\) and \(c\). For sufficiently small \(|\varepsilon|\), the analytic lift
\[
F_\varepsilon(x)=x+\frac12+\varepsilon\bigl[a(1+\cos(4\pi x))+c\sin(2\pi x)\bigr]
\]
is an orientation-preserving circle diffeomorphism. Let \(\rho(\varepsilon)\) be its lifted rotation number. The first-order two-step drift is nonnegative but vanishes at two points, so the ordinary strict-transversality formula does not apply. Nevertheless the following sharp alternative holds.

For \(0<|c|<4a\),
\[
\boxed{\rho(\varepsilon)=\frac12+\operatorname{sgn}(\varepsilon)\frac{\pi|c|}{2}\sqrt{16a^2-c^2}\,\varepsilon^2+o(\varepsilon^2).}
\]
In particular \(\rho'(0)=0\), but the two one-sided quadratic difference quotients have equal nonzero magnitude and opposite signs, so \(\rho\) is not twice differentiable at zero. For \(c=0\) or \(|c|>4a\), \(\rho(\varepsilon)=1/2\) throughout some open neighborhood of zero. No assertion is made at the critical ratios \(|c|=4a\).

## Assumptions and scope
The real parameters \(a>0\) and \(c\) are fixed while \(\varepsilon\to0\) from either side. The displayed map is a real lift with \(F_\varepsilon(x+1)=F_\varepsilon(x)+1\). Since \(F_\varepsilon'(x)=1+\varepsilon v'(x)\), with \(v(x)=a(1+\cos4\pi x)+c\sin2\pi x\), it is orientation preserving for sufficiently small \(|\varepsilon|\). The rotation number is \(\rho(F)=\lim_{n\to\infty}(F^n(x)-x)/n\), independent of \(x\). The asymptotics are pointwise in fixed \(a,c\), not uniform when \(|c|\) approaches \(0\) or \(4a\). The result is a local statement for this concrete two-harmonic path through the rigid half-rotation, not a global description of its full mode-locking parameter set.

## Proof
**1. Exact return and two singular locations.** Put \(H_\varepsilon(x)=F_\varepsilon^2(x)-1=x+D_\varepsilon(x)\). Taylor expansion, uniform in \(x\) including spatial derivatives, yields
\[
D_\varepsilon(x)=\varepsilon\left[v(x)+v(x+\tfrac12)\right]+\varepsilon^2v'(x+\tfrac12)v(x)+\frac{\varepsilon^3}{2}v''(x+\tfrac12)v(x)^2+O(\varepsilon^4).
\]
The first bracket is \(2a(1+\cos4\pi x)\), which is nonnegative and has precisely the two quadratic zeros \(r_+=1/4\) and \(r_-=3/4\) modulo one.

**2. Uniform cubic jets at the bottlenecks.** Set \(x=r_\pm+\varepsilon u\) with \(u\) bounded. Direct expansion gives
\[
D_\varepsilon(r_++\varepsilon u)=\varepsilon^3P_+(u)+O_u(\varepsilon^4),\qquad
D_\varepsilon(r_-+\varepsilon u)=\varepsilon^3P_-(u)+O_u(\varepsilon^4),
\]
where
\[
\begin{aligned}
P_+(u)&=16\pi^2 a u^2+4\pi^2c(4a+c)u+2\pi^2c^2(4a+c),\\
P_-(u)&=16\pi^2 a u^2+4\pi^2c(c-4a)u+2\pi^2c^2(4a-c).
\end{aligned}
\]
Both have quadratic coefficient \(A=16\pi^2a\) and the same completed-square minimum
\[
K=\frac{\pi^2c^2(16a^2-c^2)}{4a}.
\]
Indeed each is \(A(u-u_\pm)^2+K\) for a real center \(u_\pm\).

**3. The sharp locking-versus-drift threshold.** Suppose \(0<|c|<4a\), so \(K>0\). Taylor expansion around either zero, keeping the relative terms in \(t=x-r_\pm\) and \(\varepsilon\), shows that \(D_\varepsilon(x)/\varepsilon\) equals a positive definite quadratic form
\[
A t^2+B_\pm\varepsilon t+C_\pm\varepsilon^2+O((|t|+|\varepsilon|)^3).
\]
Its definiteness follows from \(A>0\) and \(K=C_\pm-B_\pm^2/(4A)>0\). On sufficiently small fixed neighborhoods of the two zeros, this implies
\[
\frac{|D_\varepsilon(x)|}{|\varepsilon|}\ge k_0\left[(x-r_\pm)^2+\varepsilon^2\right]
\]
for some \(k_0>0\) independent of sufficiently small nonzero \(\varepsilon\). On the complement, the positive first-order bracket bounds \(D_\varepsilon/\varepsilon\) away from zero. Consequently \(D_\varepsilon\) has the strict sign of \(\varepsilon\) everywhere: the return has no fixed point.

If \(|c|>4a\), then \(K<0\). At each \(r_\pm+\varepsilon u_\pm\), the sign of \(D_\varepsilon\) is opposite to that of \(\varepsilon\) for sufficiently small nonzero \(\varepsilon\). Away from these locations it has the sign of \(\varepsilon\). The intermediate value theorem supplies a fixed point of \(H_\varepsilon\), i.e. a point satisfying \(F_\varepsilon^2(x)=x+1\). The standard periodic-point criterion for orientation-preserving lifts gives \(\rho(F_\varepsilon)=1/2\). At \(c=0\), the two points \(1/4\) and \(3/4\) are an exact period-two orbit for all sufficiently small \(\varepsilon\), proving the remaining locking assertion.

**4. Bottleneck passage time.** In the drifting case set
\[
I_\varepsilon=\int_0^1\frac{dx}{|D_\varepsilon(x)|}.
\]
On the complement of fixed neighborhoods of the zeros, the integral is \(O(|\varepsilon|^{-1})\). In each zero neighborhood, substitute \(x=r_\pm+\varepsilon u\). The lower bound in step 3 dominates the rescaled integrand by \(C/(1+u^2)\), and the cubic jets permit dominated convergence. Thus
\[
\lim_{\varepsilon\to0}|\varepsilon|^2I_\varepsilon
=\int_{-\infty}^{\infty}\frac{du}{P_+(u)}+
\int_{-\infty}^{\infty}\frac{du}{P_-(u)}
=\frac{2\pi}{\sqrt{AK}}.
\]
The last equality is the elementary integral for a positive quadratic with leading coefficient \(A\) and minimum \(K\).

**5. Passage time equals rotation rate at leading order.** Uniformly on the circle, \(\|D_\varepsilon'\|_\infty=O(|\varepsilon|)\). Along one iterate of the near-identity lift \(H_\varepsilon\), the integral of \(1/|D_\varepsilon|\) over the traversed interval is \(1+O(|\varepsilon|)\), uniformly in the starting point. To see this, the mean-value bound \(|D_\varepsilon(t)-D_\varepsilon(x)|\le\|D_\varepsilon'\|_\infty|t-x|\) applies on an interval whose length is exactly \(|D_\varepsilon(x)|\). Summing over an arbitrarily long orbit, and using the period-one translation property of the integrand, proves
\[
\rho(H_\varepsilon)=\frac{\operatorname{sgn}(\varepsilon)}{I_\varepsilon}(1+O(|\varepsilon|)).
\]
The lifted rotation identity \(\rho(H_\varepsilon)=2\rho(F_\varepsilon)-1\) now gives
\[
\rho(F_\varepsilon)-\frac12=\operatorname{sgn}(\varepsilon)
\frac{\sqrt{AK}}{4\pi}\varepsilon^2+o(\varepsilon^2)
=\operatorname{sgn}(\varepsilon)\frac{\pi|c|}{2}\sqrt{16a^2-c^2}\,\varepsilon^2+o(\varepsilon^2),
\]
which proves the theorem. The nonzero coefficient gives the stated failure of a two-sided second derivative.

## Verification
The supplemental `CHECK.py` recomputes both bottleneck polynomials and their completed-square minima with exact symbolic algebra, and verifies the drift/sign regimes and predicted coefficient with sampled parameters. These computations are supplementary: the proof of every asymptotic statement is the uniform Taylor expansion, sign argument, dominated-convergence calculation, and discrete passage-time estimate above. Reproduction requires Python 3 and SymPy: run `python CHECK.py` in the directory containing that script.

## Relationship to prior work
Glendinning [1] analyzes rational rotation perturbations and specifically the two-harmonic map \(x+\alpha+\beta\sin(2\pi x)+\gamma\cos(4\pi x)\). His Theorem 1.3 requires strict positivity or a sign change in the first-order resonant average; Section 6 explicitly treats half-rotation in the strictly positive case. The present path lies exactly on the excluded equality boundary, where the first-order average has a quadratic zero, and determines both a second-order drift coefficient and the sharp nonresonant-harmonic cutoff that selects locking. Parkhe [2] proves differentiability under a strict monotonicity hypothesis; it does not determine the present second-order cusp. Mugnaine, Sales, Szezech and Viana [3] introduce and study the same two-harmonic sine-circle map in a nontwist context, but their numerical bifurcation diagrams and their reported saddle-node curves do not give the explicit singular half-rotation asymptotic here. Previously published explicit half-tongue width formulas for the **single-harmonic** sine map and quadratic complementary-harmonic tongue laws at denominators at least three concern different parameter domains and do not imply this equality-boundary result.

## Limitations
The threshold assertions leave the boundary \(|c|=4a\) unresolved. No uniform estimate is claimed for parameter paths tending to that boundary, nor for coupling outside the small-\(|\varepsilon|\) diffeomorphism regime. The result identifies the local lifted rotation number and a locking threshold; it does not characterize mode-locking tongues throughout parameter space. Although the named full-text comparisons did not disclose the same explicit formula, classical parabolic circle-map normal forms may contain an equivalent specialization not located in the inspected literature. Historical priority and independent mathematical validation remain open.

## References
[1] P. Glendinning, “Scaling of the rotation number for perturbations of rational rotations,” arXiv:2506.19508v1, first publicly posted 2025-06-24; *Chaos* **35** (2025), 093146, DOI: 10.1063/5.0290311. Open accepted manuscript: https://pure.manchester.ac.uk/ws/portalfiles/portal/1620599874/Glendinning_Scalingv1.pdf.

[2] K. Parkhe, “One-parameter families of circle diffeomorphisms with strictly monotone rotation number,” arXiv:1109.3214 (2011); full preprint at https://arxiv.org/pdf/1109.3214.

[3] M. Mugnaine, M. R. Sales, J. D. Szezech Jr. and R. L. Viana, “Dynamics, multistability, and crisis analysis of a sine-circle nontwist map,” *Physical Review E* **106** (2022), 034203, DOI: 10.1103/PhysRevE.106.034203. Open author-hosted manuscript: https://fisica.ufpr.br/viana/artigos/2022/PhysRevE.106.034203.pdf.

[4] “Quadratic Arnold-tongue onset from complementary Fourier harmonics,” public mathematical research record, 2026-11-01, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-quadratic-arnold-tongue-onset-from-complementary-fourier-harmoni--721f62609418/RESULT.md.

[5] “Exact half-resonance tongue width and strict normalized narrowing in the sine circle map,” public mathematical research record, 2026-10-18, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-exact-half-resonance-tongue-width-and-strict-normalized-narrowin--29dcfa7c1806/RESULT.md.
