# The exact speed-limited error-pair region for an amplitude-damped qubit inversion

## Finding

**Theorem (complete two-input error region and sharp asymmetry bound).** Fix a drive-speed cap \(\Omega>0\) and a pulse duration \(T\ge\pi/\Omega\). Consider every admissible ideal unitary qubit control whose Bloch generator is \(H(t)=\frac12\mathbf h(t)\cdot\boldsymbol\sigma\), with piecewise-continuous \(\mathbf h\) and \(\lVert\mathbf h(t)\rVert\le\Omega\) almost everywhere, that perfectly inverts the computational basis at time \(T\). Subject both antipodal inputs to the same laboratory-frame amplitude-damping channel with jump \(\sqrt\gamma|0\rangle\langle1|\). Define the first-order ideal-target state infidelities by

\[
K_\pm=\lim_{\gamma\downarrow0}\frac{1-F_\pm(\gamma)}{\gamma},
\]

where \(F_+\) corresponds to input \(|0\rangle\) and \(F_-\) to input \(|1\rangle\); each target is the noiseless final state for its input. Put

\[
C=\frac{3\pi}{2\Omega},\qquad \Delta=T-\frac\pi\Omega.
\]

At the minimum time \(\Delta=0\), the entire attainable pair set consists of the single point \(K_+=K_-=C/4\). At every strictly longer time \(\Delta>0\), define dimensionless coordinates

\[
u=\frac{4K_--C}{\Delta},\qquad v=\frac{4K_+-C}{\Delta}.
\]

The **complete attainable set** of normalized error pairs is exactly

\[
\boxed{\quad 2+\frac{(u-v)^2}{8}\le u+v\le4.\quad}
\]

Both inequalities are inclusive. Every admissible pair is implemented by a maximum-speed meridian half-turn, with at most two nonnegative dwelling intervals inserted at specified latitudes. In particular, the sharp two-input directional ratio satisfies

\[
\boxed{\quad\frac{K_-}{K_+}\le1+\frac8{3\pi}(\Omega T-\pi).\quad}
\]

At \(\Delta>0\) equality in this orientation requires, at the level of the Bloch path's time-occupation measure, a maximum-speed meridian crossing with all excess duration spent at the north pole before crossing; this is attainable. Reversing the roles of the two inputs gives the reversed ratio bound. This theorem describes leading weak-damping slopes at fixed \(T\), not finite-\(\gamma\) fidelities or bounds optimized over different baths.

## Assumptions and scope

The noiseless evolution is \(\dot U=-iH(t)U\) in units \(\hbar=1\), with arbitrary piecewise-continuous three-axis Hamiltonian coefficients under the **Euclidean Bloch angular-speed** cap \(\lVert\mathbf h\rVert\le\Omega\). The noise is a time-independent, zero-temperature, single-jump GKSL dissipator \(\mathcal D_\gamma(\rho)=\gamma(\sigma_-\rho\sigma_+-\{\sigma_+\sigma_-,\rho\}/2)\) with \(\sigma_-=|0\rangle\langle1|\). This is not an optimization over a variable dissipator, and no detuning, additional dissipator, leakage level, or control-derivative limit is allowed. A perfect inversion means the noiseless propagator exchanges the two basis rays; phases of these two rays need not be specified. No such control exists for \(T<\pi/\Omega\).

The Bloch paths from the two inputs are antipodal: if \(\mathbf r(t)\) starts at the north pole and ends at the south pole, the other is \(-\mathbf r(t)\). Thus the result applies to arbitrary nonmeridional paths and arbitrarily many control reversals, not just the constructed meridian controls.

## Proof

**Step 1: first-order dissipative cost.** For any noiseless pure-state projector \(P(t)=|\psi(t)\rangle\langle\psi(t)|\), a first-order interaction-frame expansion of the Lindblad equation gives

\[
\lim_{\gamma\downarrow0}\frac{1-F(\gamma)}\gamma
=\int_0^T\left(\langle\sigma_+\sigma_-\rangle_{P(t)}-|\langle\sigma_-\rangle_{P(t)}|^2\right)dt.
\]

With \(z(t)=r_z(t)\), the instantaneous excited-state population is \(p=(1-z)/2\), and purity gives \(|\langle\sigma_-\rangle|^2=p(1-p)\). Their difference equals \(p^2=(1-z)^2/4\). For the antipodal path the sign of \(z\) reverses, yielding the two exact coefficients

\[
4K_+=\int_0^T(1-z(t))^2dt,\qquad
4K_-=\int_0^T(1+z(t))^2dt.
\]

The first-order expansion follows for bounded, piecewise-continuous controls by the Dyson integral; its remainder is \(O(\gamma^2)\) for any fixed finite \(T\).

**Step 2: a nonnegative residual residence measure.** Let \(\theta(t)=\arccos z(t)\in[0,\pi]\). This polar angle is the spherical geodesic distance from the north pole and is an absolutely continuous function of time. Its metric derivative satisfies \(|\dot\theta|\le\lVert\dot{\mathbf r}\rVert\le\Omega\) almost everywhere, and \(\theta(0)=0\), \(\theta(T)=\pi\). For every bounded Borel function \(f\ge0\), the one-dimensional area formula and passage through all intermediate latitudes imply

\[
\int_0^T f(\theta(t))\,dt
\ge\frac1\Omega\int_0^T f(\theta(t))|\dot\theta(t)|dt
\ge\frac1\Omega\int_0^\pi f(s)ds.
\]

Consequently the pushforward of time under \(\theta\), denoted \(\theta_\#(dt)\), dominates the measure \(ds/\Omega\) on \([0,\pi]\). The difference \(\nu=\theta_\#(dt)-ds/\Omega\) is a positive Borel measure of total mass exactly \(\Delta=T-\pi/\Omega\). Since \(\int_0^\pi(1\pm\cos s)^2ds=3\pi/2\), the costs decompose *exactly* as

\[
4K_-=C+\int_0^\pi(1+\cos s)^2\,d\nu(s),\qquad
4K_+=C+\int_0^\pi(1-\cos s)^2\,d\nu(s).
\]

When \(\Delta=0\), the remainder measure is zero and the claimed singleton follows, including the rigid normalized value at the quantum speed limit.

**Step 3: the necessary sharp region.** For \(\Delta>0\), push forward the probability measure \(\nu/\Delta\) under \(x=\cos s\), obtaining a random variable \(X\in[-1,1]\). Set \(h=\mathbb E X\), \(q=\mathbb E X^2\). Then

\[
u=\mathbb E(1+X)^2=1+2h+q,\qquad
v=\mathbb E(1-X)^2=1-2h+q,
\]

and hence \(h=(u-v)/4\), \(q=(u+v)/2-1\). The exact two-moment restrictions \(h^2\le q\le1\) yield the displayed parabolic lower boundary and horizontal upper boundary. They also force \(|u-v|\le4\) and nonnegative normalized errors.

**Step 4: constructive sufficiency of every point.** Conversely take any real \((u,v)\) satisfying both inequalities. Define \(h=(u-v)/4\) and \(q=(u+v)/2-1\); these obey \(-1\le h\le1\) and \(h^2\le q\le1\). For \(h>-1\) define

\[
b=\frac{q+h}{1+h}\in[h,1],\qquad
\alpha=\frac{b-h}{b+1}\in[0,1].
\]

The two-point probability law \(\Pr(X=-1)=\alpha\), \(\Pr(X=b)=1-\alpha\) has \(\mathbb E X=h\) and \(\mathbb E X^2=q\), as seen by direct substitution. At \(h=-1\) take \(X=-1\) almost surely. Now rotate along one meridian from north to south at angular speed exactly \(\Omega\), inserting a nonnegative dwell of length \((1-\alpha)\Delta\) at \(\theta=\arccos b\), and another of length \(\alpha\Delta\) at the south pole. The angular-speed bound and ideal endpoint inversion hold, the travel time is exactly \(\pi/\Omega\), and the residual occupation is precisely the prescribed two-atom measure. The construction realizes the requested \((u,v)\). In the endpoint case \(h=-1\), use only the south-pole dwell. Thus the moment restrictions are also sufficient, with no hidden regularity or reachability constraints.

**Step 5: ratio optimum and equality.** By the positive residual measure, \(4K_+\ge C\); because \((1+X)^2\le4\), \(4K_-\le C+4\Delta\). Dividing strictly positive bounds proves

\[
\frac{K_-}{K_+}\le\frac{C+4\Delta}{C}
=1+\frac{8\Omega\Delta}{3\pi}.
\]

For positive \(\Delta\), equality forces the residual measure to be supported entirely at \(X=1\), i.e. the north pole. In addition, equality in the speed-limited measure comparison precludes extra latitudinal traversals; the remaining path is a length-minimizing meridian crossed at maximum speed. Conversely north-pole dwelling followed by the maximum-speed meridian gives equality. The reversed ratio is obtained by exchanging north and south. This completes the proof.

## Verification

The accompanying standalone `checks/check.py` uses Python's standard library. Execute `python3 checks/check.py` to test the moment-to-two-dwell inversion, random speed-limited nonmonotone meridian paths, both sharp ratio endpoints, and weak-rate GKSL Bloch-equation integration for three piecewise-constant pulse schedules. The delivered checker passed **4,445** numerical and algebraic assertions. The general result is established by Steps 1–5 above; finite checks do not certify arbitrary trajectories.

For reproducibility, the exact meridian integral in the checker is

\[
\int_a^b(1\pm\cos s)^2ds
=\frac32(b-a)+\frac14(\sin 2b-\sin 2a)\pm2(\sin b-\sin a),\qquad a\le b,
\]

and reversing path orientation only changes the integration order, not its positive time contribution.

## Relationship to prior work

Patra, *Directional gate-error asymmetry and universal selectivity bounds in non-unital open quantum systems* (arXiv:2611.18755v1, first public 11 November 2026), establishes the general first-order pure-state jump-variance law, trajectory moment decomposition, optimization over GKSL baths for a fixed path, and explicitly analyzes **wait–flip–wait pole schedules** (Section 7.2 and Appendix F). Those results are fundamental premises here and are not presented as discoveries. The present theorem fixes the amplitude-damping dissipator and a global Hamiltonian-speed/duration budget, proves the complete joint reachable region for *all* admissible inversion paths, and constructs every feasible point from at most two dwells. The source's pole-dwell family realizes part of the region, including the ratio-extremizing schedule, but its reported bounds are neither an all-trajectory occupation-measure converse nor a classification of the entire two-error set.

Lin, Sels and Wang, *Time-optimal control of a dissipative qubit*, Phys. Rev. A **101** (2020), 022320, treats bounded-control minimum-time state transfer in Lindblad dynamics via Pontryagin analysis. Its optimization target and restricted control setting differ from the complete weak-damping, two-initial-state attainable error region at prescribed duration. The general quantum-speed-limit principle and classical one-dimensional occupation/moment inequalities are used as mathematical ingredients, not claimed as novel.

## Limitations

The finding concerns exactly one two-level Markovian amplitude-damping jump and first derivatives of state fidelity at zero noise. It does not bound finite-damping fidelities uniformly in pulse duration, nor allow thermal excitation, dephasing, state-dependent loss, detuning limitations, bandwidth or slew-rate constraints, composite higher-dimensional gates, or a variable bath. The construction permits instant changes of the control amplitude at dwell endpoints (piecewise-continuous control). Experimental calibration under a stricter hardware control set may yield a proper subset of the stated region. The general first-order moment identity and special pole-dwell examples were already available in the initiating source; publication priority for the new full-region converse and precise global fixed-bath statement requires independent literature assessment.

## References

1. A. Patra, *Directional gate-error asymmetry and universal selectivity bounds in non-unital open quantum systems*, arXiv:2611.18755v1 (11 November 2026), https://arxiv.org/abs/2611.18755 ; Sections 2–3, 7.2 and Appendix F.
2. C. Lin, D. Sels, and Y. Wang, *Time-optimal control of a dissipative qubit*, Phys. Rev. A **101**, 022320 (2020), https://doi.org/10.1103/PhysRevA.101.022320 ; full-text https://www.merl.com/publications/docs/TR2020-023.pdf.
