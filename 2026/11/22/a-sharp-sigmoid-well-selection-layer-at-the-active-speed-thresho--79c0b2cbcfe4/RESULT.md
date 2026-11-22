# A sharp sigmoid well-selection layer at the active speed threshold

## Finding

A particle driven by a two-state, directionally biased velocity-jump process in the piecewise-linear double well \(U(x)=b\bigl||x|-a\bigr|\) exhibits a singular but completely classified well-selection crossover as its propulsion speed \(v\) approaches the force magnitude \(b\) from above. For fixed \(a,b,r>0\), write \(v=b+\varepsilon\) and assign the orientation-switching rates
\[
\alpha_+=r-\frac{\theta\varepsilon}{2a},\qquad
\alpha_-=r+\frac{\theta\varepsilon}{2a},\qquad \theta\in\mathbb R,
\]
where \(+\) switches to \(-\) at rate \(\alpha_+\) and \(-\) switches to \(+\) at rate \(\alpha_-\). For every sufficiently small \(\varepsilon>0\), the process has a unique stationary probability law. For stationary position \(X_\varepsilon\), put \(H_\varepsilon=\operatorname{sgn}X_\varepsilon\in\{-1,+1\}\) and \(Y_\varepsilon=(X_\varepsilon-aH_\varepsilon)/\varepsilon\). Then, in total variation,
\[
 (H_\varepsilon,Y_\varepsilon)\ \Longrightarrow\ (H,Y),\quad
 \mathbb P(H=+1)=\frac{1}{1+e^{-\theta}},\quad
 \mathbb P(Y\in dy)=\frac r2 e^{-r|y|}\,dy,
\]
with \(H\) and \(Y\) independent. Furthermore, the well weight has the uniform-on-compact-\(\theta\) first correction
\[
\mathbb P(X_\varepsilon>0)=s(\theta)+\frac{\theta\varepsilon}{2b}s(\theta)(1-s(\theta))+O_{a,b,r,\Theta}(\varepsilon^2),\qquad s(\theta)=(1+e^{-\theta})^{-1},\quad |\theta|\le\Theta.
\]
The internal orientation \(S_\varepsilon\in\{-1,+1\}\) satisfies the *exact* identity
\[
\mathbb P\bigl(S_\varepsilon\ne\operatorname{sgn}Y_\varepsilon\bigr)=\frac{\varepsilon}{2(b+\varepsilon)}.
\]
Consequently \(S_\varepsilon=\operatorname{sgn}Y\) in the joint limit. The crossover scale is sharp: if \(\alpha_\pm\to r\) and \(a(\alpha_--\alpha_+)/\varepsilon\to+\infty\), respectively \(-\infty\), the right-well probability tends to \(1\), respectively \(0\). The symmetric limit equals \(1/2\).

## Assumptions and scope

The state \((X_t,S_t)\in\mathbb R\times\{-1,+1\}\) follows the piecewise-deterministic process
\[
\dot X_t=-U'(X_t)+v S_t,\quad U(x)=b\bigl||x|-a\bigr|,\quad a,b>0,\quad v>b.
\]
At isolated nonsmooth points choose either adjacent drift value; trajectories cross them in finite time and the choice is irrelevant almost surely. The independent orientation chain switches \(+\to-\) at \(\alpha_+>0\), \(-\to+\) at \(\alpha_->0\). There is no independent Brownian thermal diffusion in this theorem. All stationary probabilities refer to the unique invariant law under the strict confinement criterion below.

For general positive rates and \(v>b\), define
\[
\varepsilon=v-b,\quad c=v+b,\qquad
L=\frac{\alpha_-}{\varepsilon}-\frac{\alpha_+}{c},\quad
R=\frac{\alpha_+}{\varepsilon}-\frac{\alpha_-}{c}.
\]
A finite invariant law exists exactly if \(L,R>0\), equivalently
\[
 v|\alpha_--\alpha_+|<b(\alpha_++\alpha_-).
\]
This general existence and density statement is an explicitly derived application of an already established two-velocity stationary-current formula, not itself asserted to be novel.

## Proof

**1. Exact law and existence.** Let \(p_+(x),p_-(x)\) be orientation-resolved stationary densities and write \(f(x)=-U'(x)\in\{+b,-b\}\) away from \(\{-a,0,a\}\). Their total stationary current is spatially constant. Any integrable invariant density on the full line has zero current, hence
\[
(v+f)p_+=(v-f)p_-=:q(x),\quad
 p_+=\frac{v-f}{2v}P,\quad p_-=\frac{v+f}{2v}P,
\]
where \(P=p_++p_-\). The positive orientation equation then yields
\[
q'(x)=\left(\frac{\alpha_-}{v-f(x)}-\frac{\alpha_+}{v+f(x)}\right)q(x).
\]
The two velocities are uniformly nonzero and their fluxes are continuous across each force discontinuity. Thus \(q\), and therefore \(P\), is continuous and piecewise exponential. Defining \(C>0\) by normalization gives
\[
P(x)=C\begin{cases}
e^{Ra+L(x+a)},&x<-a,\\
e^{-Rx},&-a\le x<0,\\
e^{Lx},&0\le x<a,\\
e^{La-R(x-a)},&x\ge a,
\end{cases}
\]
with
\[
 C^{-1}=\frac{e^{Ra}}L+\frac{e^{Ra}-1}R+\frac{e^{La}-1}L+\frac{e^{La}}R.
\]
It integrates exactly to one iff both tail exponents \(L,R\) are strictly positive. If either is nonpositive, no integrable stationary solution exists. When both are positive, the displayed positive invariant law and accessibility of all open position intervals through alternating velocities imply its uniqueness (standard irreducibility and stationary-measure uniqueness for this one-dimensional switching flow). The equivalence to the velocity-bias inequality follows by multiplying the two strict tail conditions by \(\varepsilon c\) and using \(c+\varepsilon=2v\) and \(c-\varepsilon=2b\).

**2. Exact well mass and sigmoid expansion.** Integration over the two half-lines gives
\[
M_+=C\left[e^{La}\left(\frac1L+\frac1R\right)-\frac1L\right],\quad
M_-=C\left[e^{Ra}\left(\frac1L+\frac1R\right)-\frac1R\right].
\]
Set \(A=L^{-1}+R^{-1}\). For \(\alpha_\pm=r\mp\theta\varepsilon/(2a)\), both \(L,R=r/\varepsilon+O(1)\) uniformly for \(|\theta|\le\Theta\). Consequently, by dividing numerator and denominator by \(A(e^{La}+e^{Ra})\),
\[
M_+=s\bigl(a(L-R)\bigr)+O_{a,b,r,\Theta}\bigl(e^{-c_0/\varepsilon}\bigr)
\]
for some \(c_0>0\) and every sufficiently small \(\varepsilon\). Direct subtraction gives the *exact* relation \(a(L-R)=\theta(1+\varepsilon/(2b+\varepsilon))\). Taylor's theorem on compact \(\theta\)-sets proves the displayed correction and an \(O(\varepsilon^2)\) remainder. If \(\alpha_\pm\to r\) and \(a(\alpha_--\alpha_+)/\varepsilon\to\pm\infty\), the same exact mass formula and \(\min(L,R)a\to\infty\) imply the sharp polarized limits.

**3. Local displacement and orientation.** On \(X>0\), set \(x=a+\varepsilon y\); its unnormalized density equals \(C\varepsilon e^{La}e^{L\varepsilon y}\) for \(-a/\varepsilon<y<0\), and \(C\varepsilon e^{La}e^{-R\varepsilon y}\) for \(y>0\). The analogous density on \(X<0\) uses the common factors \(e^{Ra}\) and exponents \(L\varepsilon\) for \(y<0\), \(R\varepsilon\) for \(y>0\). Since \(\varepsilon L,\varepsilon R\to r\), each conditional law of \(Y_\varepsilon\) converges in total variation, by direct exponential-tail integration, to the common symmetric Laplace density \(r e^{-r|y|}/2\). Combining with the well-mass limit proves independence of \(H\) and \(Y\) in the joint total-variation limit. For every regular \(x\), the zero-current fractions show that \(p_+/P=\varepsilon/(2v)\) on segments with \(f=+b\), and \(p_-/P=\varepsilon/(2v)\) where \(f=-b\). These are precisely the events in which the orientation disagrees with the sign of displacement from the closest well center; integrating gives the exact mismatch probability.

## Verification

The standalone `check.py` script performs direct quadrature of all four density segments, compares the exact well mass against numerical integrals, checks the stationary orientation flux and local master equation, and tests the sigmoid boundary-layer convergence for multiple positive parameter choices. It uses ordinary floating-point tests only as cross-checks; the theorem is proved by the preceding exact identities and analytic limits. Invoke `python check.py` with Python 3, SciPy and NumPy available. No finite numerical test is used to infer the infinite-parameter limit.

## Relationship to prior work

Singh and Aghion (2026) introduced and solved the heat-coupled symmetric-rate run-and-tumble dynamics in this precise piecewise-linear double well. Their stationary solutions, escape times and symmetry assumptions are credited. Jain and Chatterjee (2024), particularly their Eq. (7) and Appendix A, supplied a general zero-current stationary density formula for two-state switching particles with position-dependent velocities and switching rates. Substituting the present piecewise velocities into that formula already produces our exact finite-parameter stationary density: that substitution is not a novelty claim. Dhar and coauthors (2018/2019) studied single-well confining potentials and the zero-noise linear-force threshold, and Ratanov (2025) considered smooth bistable telegraph dynamics in a distinct low-velocity, disjoint-attractor regime.

The specific assessed conclusion is the simultaneous *near-critical propulsion and weak orientation-bias* scaling: the sharp universal sigmoid occupation weights, their first correction, independent two-sided exponential intrawell fluctuations, and orientation locking. The cited full texts do not state that combined singular-window theorem. A generic exact finite-parameter density does permit its derivation; this is the closest potentially dominating antecedent and a genuine priority risk rather than evidence of independent novelty certification.

## Limitations

The result concerns a piecewise-linear double-well drift, no thermal diffusion, constant orientation-switching rates and \(v>b\). At \(v\le b\), deterministic barriers may separate invariant regions, so the theorem does not claim uniqueness or the same limit there. It neither gives mixing-time asymptotics nor asserts that observing the invariant distribution alone reveals kinetic transition rates. The critical window is a singular joint limit, not spontaneous symmetry breaking at a fixed positive \(\varepsilon\). The new asymptotic might be an implicit unreported corollary of broader stationary formulas; published equivalence has not been excluded absolutely.

## References

1. R. K. Singh and E. Aghion, *Spatial density, first passage times, and entropy of run and tumble particles in a bistable potential*, arXiv:2610.08029 (publicly submitted 2026-10-06), https://arxiv.org/abs/2610.08029.
2. K. Jain and S. Chatterjee, *Run-and-tumble particle with saturating rates*, arXiv:2405.13521 (publicly submitted 2024-05-22), Eq. (7) and Appendix A, https://arxiv.org/abs/2405.13521.
3. A. Dhar, A. Kundu, S. N. Majumdar, S. Sabhapandit and G. Schehr, *Run-and-tumble particle in one-dimensional confining potential*, arXiv:1811.03808, https://arxiv.org/abs/1811.03808.
4. N. Ratanov, *Metastability for telegraph processes in a double-well potential*, arXiv:2509.17383 (publicly submitted 2025-09-22), https://arxiv.org/abs/2509.17383.
