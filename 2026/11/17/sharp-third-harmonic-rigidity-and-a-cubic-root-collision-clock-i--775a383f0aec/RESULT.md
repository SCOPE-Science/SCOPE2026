# Sharp third-harmonic rigidity and a cubic-root collision clock in a three-phase network

## Finding
Consider three identical phases with complete, equal-strength pair interactions of the form \(G_r(s)=-\cos s+r\cos(3s)\). For every \(-1/3\le r\le1/9\), the relative-phase torus contains exactly three equilibria: synchrony and two opposite splay states. The two collision-free regions are each completely filled by nested nonstationary periodic relative-phase orbits surrounding one splay center. The three pair-collision circles are the entire boundary of these two period annuli; on each open collision arc every solution runs asymptotically into synchrony. The splay linear frequencies are both exactly \(3g/2\), independent of \(r\).

At \(-1/3\le r<1/9\), a trajectory approaching synchrony on a collision arc has a lifted angular gap \(d(t)\in(-2\pi,0)\), and obeys \(\lim_{t\to\infty}gt\,|d(t)|=2/(1-9r)\). Exactly at \(r=1/9\), the critical clock changes to \(\lim_{t\to\infty}gt\,|d(t)|^3=1\). The endpoint is sharp for this three-equilibrium portrait: for every \(1/9<r<1\), six additional pair-cluster relative equilibria appear, two on each collision circle.

## Assumptions and scope
Let \(g>0\), \(\Omega\in\mathbb R\), \(r\in[-1/3,1/9]\), and let \(\theta_j\in\mathbb R/(2\pi\mathbb Z)\) solve the smooth autonomous equations
\[
\dot\theta_j=\Omega+g\sum_{k\ne j}G_r(\theta_k-\theta_j),\qquad G_r(s)=-\cos s+r\cos(3s),\quad j=1,2,3.
\]
Define \(x=\theta_2-\theta_1\), \(y=\theta_3-\theta_1\) modulo \(2\pi\), and rescale time by \(\tau=gt\). A *relative* periodic orbit means periodicity of \((x,y)\); the original three phases need not close after a period. The three collision circles are \(x=0\), \(y=0\), \(x=y\) on the relative torus.

The critical clock is for a nonstationary trajectory on any of these collision circles approaching synchrony in forward time. On \(x=0\), use the lift \(d=y\in(-2\pi,0)\); the other collision arcs are related by permutation symmetry. The extension statement for \(r>1/9\) is restricted to \(1/9<r<1\) and does not assert a complete phase portrait there.

## Proof
**1. Hamiltonian reduction and equilibrium census.** The relative equations are
\[
x'=G_r(y-x)-G_r(y),\qquad y'=G_r(y-x)-G_r(x).
\]
Set \(Q_r(s)=-\sin s+(r/3)\sin(3s)\). Then
\[
\mathcal H_r(x,y)=Q_r(y-x)-Q_r(y)+Q_r(x)
\]
satisfies \(x'=\partial_y\mathcal H_r\), \(y'=-\partial_x\mathcal H_r\). This Hamiltonian first-integral structure for arbitrary even three-phase interactions is **previously known**, not asserted as a new general theorem.

Using \(u=\cos s\), write \(G_r(s)=F_r(u)\), where
\[
F_r(u)=4ru^3-(1+3r)u,\qquad F'_r(u)=12ru^2-(1+3r).
\]
For \(-1/3\le r\le1/9\), this derivative is nonpositive on \([-1,1]\) and vanishes only at isolated points; therefore \(F_r\) is strictly decreasing. An equilibrium satisfies \(G_r(x)=G_r(y)=G_r(y-x)\), hence \(\cos x=\cos y=\cos(y-x)\). If \(y=x\), then \(\cos x=1\), giving synchrony. Otherwise \(y=-x\) modulo \(2\pi\) and \(\cos(2x)=\cos x\), yielding precisely \(x=2\pi/3\), \(y=4\pi/3\), and the reflected state. Thus there are exactly three relative equilibria.

**2. Complete global level-set topology.** The collision circles are invariant by phase-permutation symmetry and meet only at synchrony. Their complement consists of the two open triangular disks \(T_+=\{0<x<y<2\pi\}\) and \(T_-=\{0<y<x<2\pi\}\). The Hamiltonian vanishes identically on their boundaries. It takes values \(-3\sqrt3/2\) and \(+3\sqrt3/2\) respectively at the two splay states: the third-harmonic sine vanishes at each splay angle. The Jacobian at either center has trace zero and determinant \(9/4\) in \(\tau\)-time, so both are strict nondegenerate extrema with linear frequency \(3/2\). No other critical points exist. Consequently each triangular disk has no interior level-set topology change away from its unique center: by the Morse lemma near the center and regular-level isotopy on compact sublevels, every intermediate level is one smooth simple closed curve. Each such curve carries a nonzero autonomous flow and is a relative periodic orbit. These curves fill each triangular disk. On a collision arc the scalar field has a constant nonzero sign away from synchrony, so the entire boundary is made of asymptotic collision trajectories.

**3. Exact collision asymptotics.** On \(x=0\), the gap \(d\in(-2\pi,0)\) evolves according to
\[
d'=G_r(d)-G_r(0)=F_r(\cos d)-F_r(1)>0.
\]
For \(r<1/9\), Taylor expansion gives \(d'=(1-9r)d^2/2+O(d^4)\). Since \(d\nearrow0\), integrating the derivative of \(|d|^{-1}\) gives the first asserted limit. At \(r=1/9\) there is the exact factorization
\[
G_{1/9}(d)-G_{1/9}(0)=\frac49(\cos d-1)^2(\cos d+2)=\frac{d^4}{3}+O(d^6).
\]
Hence \(\frac{d}{d\tau}|d|^{-3}=1+o(1)\), proving \(\tau|d|^3\to1\).

**4. Sharpness.** For \(1/9<r<1\), the identity
\[
G_r(d)-G_r(0)=(\cos d-1)\{4r(\cos^2d+\cos d)+r-1\}
\]
produces, besides synchrony, exactly two distinct roots on each pair-collision circle at
\[
\cos d=\frac{-1+r^{-1/2}}2\in(0,1).
\]
They give six distinct additional pair-cluster relative equilibria, proving that the stated three-equilibrium global portrait cannot extend to any larger \(r\)-interval beyond its upper endpoint.

## Verification
The standalone script `verify.py` uses symbolic identities for the Hamiltonian derivatives, the cubic-factorization and quartic-factorization, the splay Jacobian and its eigenvalue product, the collision boundaries, and the Taylor coefficients. Independent numerical integrations for five parameter values preserve the Hamiltonian on two representative collision-free orbits, and eight scalar quadrature tests corroborate the first-order and critical collision clocks. Run with `python verify.py` and standard Python packages `sympy`, `numpy`, `scipy`. The infinity-time claims follow from the analytical argument, not numerical iteration.

## Relationship to prior work
Qie, Pedersen, Song, Liu, and Shilnikov (2026) give a three-cell delayed inhibitory-network phase reduction, motivating the three-phase interaction model and phase-shift viewpoint; the particular two-harmonic interaction here is an **idealized specialization**, not a measured interaction in their neuronal model. A sinusoidal interaction with a quarter-cycle phase shift gives the even fundamental harmonic; the third harmonic tests a finite correction to that idealization.

Ashwin, Bick, and Burylko (2016, §4.1) already prove that every three-oscillator system with even pair coupling admits a first integral and discuss its periodic-level-set geometry. That result is credited fully. The present specific claim is the uniform **complete** equilibrium/period-annulus classification on a sharp third-harmonic parameter interval, together with the exact collision exponent switch and leading coefficient. The fundamental-harmonic case \(r=0\), including its conservative periodic annuli and separatrix behavior, is also already studied; it is a special case, not the novelty basis.

## Limitations
No conclusion about stable attraction of the splay states is asserted: the family is conservative in relative phases, so its closed orbits are neutrally stable. The theorem concerns a finite three-phase surrogate, **not** the original delayed FitzHugh–Nagumo differential-delay system or its fitted phase-response function. The claim does not classify \(r<-1/3\) or the complete global dynamics when \(r>1/9\), and it does not establish historical priority beyond the inspected published sources. Relative periodicity need not imply periodic original phases.

## References
1. X. Qie, M. G. Pedersen, J. Song, S. Liu, A. L. Shilnikov, “Delay-induced multirhythmicity in a 3-cell inhibitory network,” arXiv:2611.06836v1, first posted 2026-11-04. https://arxiv.org/html/2611.06836v1
2. P. Ashwin, C. Bick, O. Burylko, “Identical Phase Oscillator Networks: Bifurcations, Symmetry and Reversibility for Generalized Coupling,” *Frontiers in Applied Mathematics and Statistics* **2** (2016), article 7, §4.1. https://doi.org/10.3389/fams.2016.00007
