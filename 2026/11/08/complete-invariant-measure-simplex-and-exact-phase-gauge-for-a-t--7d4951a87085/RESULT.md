# Complete invariant-measure simplex and exact phase gauge for a three-dimensional polynomial flow

## Finding
Let \(\mu>0\) and \(e\in\mathbb R\). With \(w=x+iy\), \(s=|w|^2\), and
\[
B(s,z)=(s-5)\left(\frac{20}{21}-s\right)-\frac{400}{21}z^2,
\qquad D(s,z)=z+\frac{s}{10},
\]
consider the real polynomial flow
\[
\dot w=\bigl[\mu B(s,z)+i(1+eD(s,z))\bigr]w,
\qquad \dot z=-D(s,z).
\]
This is the Castañeda–Rebollo-Perdomo family from arXiv:2610.09176v1, with the same equation also considered for real \(e\).

**Theorem.** Every forward solution exists globally and is bounded. For every
\[
0<\mu\leq\frac{588}{6575},\qquad e\in\mathbb R,
\]
there are precisely three ergodic invariant Borel probability measures for the continuous-time flow on \(\mathbb R^3\): the point mass \(\delta_0\) at the origin, normalized time measure \(\sigma_1\) on the circle \(\{|w|=1,z=-1/10\}\), and normalized time measure \(\sigma_2\) on \(\{|w|=2,z=-2/5\}\). In particular, **every** invariant Borel probability measure is uniquely
\[
\alpha_0\delta_0+\alpha_1\sigma_1+\alpha_2\sigma_2,
\qquad \alpha_j\geq0,\quad\sum_{j=0}^{2}\alpha_j=1.
\]
Every forward trajectory approaches exactly one of these three periodic or stationary sets. If \(w(0)\ne0\) and its meridional limit is \((r_j,z_j)\), \(j\in\{1,2\}\), its **exact asymptotic phase** is
\[
\lim_{t\to\infty}\left|w(t)-r_j\exp\left(i\left[t+\arg w(0)+e(z(0)-z_j)\right]\right)\right|=0.
\]
For arbitrary real \(e,e'\) the global real-analytic, volume-preserving diffeomorphism
\[
H_{e,e'}(w,z)=\left(e^{i(e-e')z}w,z\right)
\]
conjugates the vector fields with parameters \(e\) and \(e'\), with **no time reparametrization**. All claims hold without assuming pointwise Hurwitz Jacobians. Consequently every such invariant probability has zero measure-theoretic entropy for the time-one map, and the time-one map has zero topological entropy on **every compact forward-invariant subset**. Also, the time average of each bounded continuous observable along any forward trajectory converges to its integral against the corresponding one of the three ergodic measures.

The special published parameter pair \((\mu,e)=(1/1000,1/10)\) belongs to this class and has a globally Hurwitz Jacobian by the cited source.

## Assumptions and scope
The flow is autonomous and polynomial in the three real Cartesian state variables; \(\mu>0\), while \(e\) may be any real number. A Borel probability \(\nu\) is invariant when \((\Phi_t)_*\nu=\nu\) for all \(t\ge0\). The probability simplex refers to the continuous-time dynamics, not to arbitrary discrete numerical samples. The measure \(\sigma_j\) is normalized arclength on its circular orbit, equivalently the uniform time distribution because angular speed on either circle is exactly one.

The global convergence and three-measure classification require \(0<\mu\le588/6575\). Forward boundedness and analytic conjugacy require only \(\mu>0\). We make no claims that all backward solutions are complete or that the Jacobian-Hurwitz property itself is conjugacy invariant.

## Proof
**1. Global boundedness.** For \(r=|w|\), the meridional system is
\[
\dot r=-\frac{\mu r}{21}\left[(r^2-5)(21r^2-20)+400z^2\right],\qquad
\dot z=-z-\frac{r^2}{10}.
\]
For \(r^2\ge5\), the bracket is nonnegative. Therefore \(0\le r(t)\le R:=\max\{r(0),\sqrt5\}\) as long as a solution exists. Variation of constants gives
\[
z(t)=e^{-t}z(0)-\frac1{10}\int_0^t e^{-(t-u)}r(u)^2\,du,
\]
so \(|z(t)|\le|z(0)|+R^2/10\). The angular velocity \(1+e(z+r^2/10)\) is then also bounded. Standard ODE continuation proves forward completeness in Cartesian coordinates. Both \(r=0\) and \(r>0\) are forward invariant.

**2. Every meridional orbit converges to one equilibrium.** In the half-plane \(r\ge0\), the only equilibria are \(q_0=(0,0)\), \(q_1=(1,-1/10)\), and \(q_2=(2,-2/5)\): for \(r>0\), the equation \(z=-r^2/10\) reduces the other equilibrium equation to \(25(r^2-1)(r^2-4)=0\). At \(q_0\), the meridional eigenvalues are \(-100\mu/21\) and \(-1\). At \(q_1\), the Jacobian determinant is \(-50\mu/7<0\), so it is a hyperbolic saddle. At \(q_2\), the Jacobian trace is \(-1-344\mu/21<0\) and determinant \(200\mu/7>0\), so it is a sink.

The meridional divergence is exactly
\[
-1-\mu\left[5\left(r^2-\frac{25}{14}\right)^2+\frac{400}{21}z^2-\frac{6575}{588}\right]\le0.
\]
It is strictly negative everywhere when \(\mu<588/6575\), and at equality it vanishes only at one isolated point. Hence its integral over any nonempty bounded open planar region is strictly negative. The divergence theorem rules out periodic Jordan loops and homoclinic loops of the meridional vector field: a loop formed from trajectories has zero boundary flux, contradicting the negative interior divergence integral. The two sinks cannot participate in a nontrivial heteroclinic cycle. In a bounded planar flow with finitely many equilibria, Poincaré–Bendixson then implies that every forward \(\omega\)-limit set here is a singleton equilibrium. Explicitly, an \(\omega\)-limit set containing a sink forces convergence to that sink; an \(\omega\)-limit set without equilibria would be a periodic orbit; and any nontrivial set containing only the remaining saddle as an equilibrium would require a homoclinic graphic, already excluded. A trajectory initially on \(r=0\) tends to \(q_0\) directly. Thus every \((r(t),z(t))\) converges to exactly one \(q_j\).

**3. Phase and conjugacy.** Since \(\dot z=-(z+r^2/10)\), for \(w\ne0\) one has the exact identity
\[
\frac{d}{dt}\bigl(\arg w(t)+ez(t)\bigr)=1.
\]
Equivalently \(u=e^{iez}w\) satisfies \(\dot u=(\mu B(|u|^2,z)+i)u\) with the unchanged \(z\) equation. This identity is valid globally in Cartesian coordinates, including the invariant axis by continuity of \(H_{e,0}\). The inverse is \(H_{0,e}\); its real Jacobian has block form with a planar rotation on the diagonal and last diagonal entry one, so \(\det DH_{e,e'}=1\). This proves real-analytic volume-preserving time conjugacy. If \((r(t),z(t))\to(r_j,z_j)\), the integrated phase identity gives the stated asymptotic formula without an asymptotic phase integral or an unknown offset.

**4. Classification of invariant probabilities.** Every finite invariant Borel probability has almost every point recurrent by the Poincaré recurrence theorem, applied to the measure-preserving time-one map (forward completeness is established above). A point whose \((r,z)\) is not an equilibrium cannot be recurrent: by Step 2 its meridional coordinate converges to a distinct equilibrium and eventually leaves a neighborhood of its initial coordinate. The only recurrent points therefore lie at the origin or on the two circular orbits. Every invariant probability is supported on their disjoint union. Continuous-time translation around each circle is the full rotation action, so normalized angular Lebesgue measure is its unique invariant probability. The origin supports only its point mass. Restriction and normalization on each of the three disjoint invariant sets gives the unique convex decomposition. Each of the three component measures is ergodic; no other ergodic measures exist. Each component time-one map is either a fixed point or a circle rotation, of zero measure-theoretic entropy. Thus all invariant probabilities have zero time-one entropy by ergodic decomposition. The variational principle applied to any compact forward-invariant subset gives zero topological entropy there. Finally, the asymptotic phase identity implies that the long-time average of a bounded continuous observable along a trajectory approaching a circle equals its uniform circular average; a trajectory approaching the origin has time average equal to its value at zero.

## Verification
Run `python3 verify.py` with Python 3, SymPy, NumPy and SciPy. The checker independently derives the Cartesian Jacobian at a representative point of the inner circle, its exact cubic characteristic polynomial and a sharp local Routh–Hurwitz threshold; verifies the meridional divergence, equilibrium factorization and stability determinants symbolically; checks cancellation of the angular gauge term at 80 parameter-state evaluations; and compares 36 pairs of numerically integrated conjugate trajectories. It prints `VERIFY_OK` on success. These finite checks are not the proofs of global boundedness, convergence, the invariant-measure classification or historical priority.

## Relationship to prior work
Castañeda and Rebollo-Perdomo (arXiv:2610.09176v1, first posted 2026-10-06) prove the globally Hurwitz property at one concrete parameter pair, identify the origin and two periodic circles, and establish the negativity of the reduced planar divergence and absence of other periodic orbits. Their Section 4 gives a numerical phase portrait and describes a separatrix between the basins. These facts, and the general planar reduction itself, are **not claimed as new**. The result here adds an analytic, all-initial-state convergence argument sufficient for the **complete invariant-probability simplex**, including the absence of nonperiodic ergodic stationary laws, and the explicit time-preserving gauge and asymptotic-phase formula for the entire real angular parameter range. The measure classification does not follow merely from the source's count of periodic orbits: aperiodic recurrent invariant measures would not be excluded by that count alone. The new trapping-and-limit-set argument supplies the missing exclusion. The source's numerical basin discussion anticipates part of the global dynamical picture, so this is an extension of that specific model, not a claim that the general Poincaré–Bendixson method is new.

## Limitations
No assertion is made for \(\mu>588/6575\) about the possible existence of other recurrent dynamics. The result is specific to the displayed rotationally symmetric polynomial family; global convergence does not imply that there are no nonstationary complete heteroclinic trajectories or other compact invariant **sets** containing their closures. The analytic conjugacy is not polynomial in general. Standard planar limit-set and recurrence theorems are used in the proof; the published paper's separate global Jacobian-Hurwitz certification is cited rather than independently re-proved. Historical priority has been checked against accessible sources but not exhaustively established. Independent scientific validation has not been performed.

## References
1. Á. Castañeda and S. Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1 (first posted 2026-10-06), https://arxiv.org/html/2610.09176.
2. Classical Poincaré–Bendixson, Bendixson–Dulac and Poincaré recurrence theorems, used in their standard planar-flow and measure-preserving formulations.
