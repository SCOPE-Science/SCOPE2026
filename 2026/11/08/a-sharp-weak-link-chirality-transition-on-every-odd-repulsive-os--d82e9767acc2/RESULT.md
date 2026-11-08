# A sharp weak-link chirality transition on every odd repulsive oscillator ring

## Finding

Let \(n\ge5\) be odd, put \(k=n-1\), and consider \(n\) phases on a ring with repulsive nearest-neighbor cosine potential
\[
V_w(\theta)=\sum_{i=0}^{n-2}\cos(\theta_{i+1}-\theta_i)+w\cos(\theta_0-\theta_{n-1}),\qquad w>0.
\]
Phases are considered modulo a common rotation and modulo \(2\pi\). The **entire set of global minimizers** undergoes a sharp transition at \(w_c=1/k\):

1. If \(0<w\le1/k\), there is exactly one minimizing phase class. The \(k\) unit-weight bonds have phase difference \(\pi\), and the weak bond has difference \(0\), modulo \(2\pi\). The minimum energy is \(E_n(w)=-k+w\).
2. If \(w>1/k\), there are exactly two minimizing phase classes, exchanged by reflection (chirality). They are specified by a unique \(\delta\in(0,\pi/k)\) satisfying
   \[
   \frac{\sin\delta}{\sin(k\delta)}=w.
   \]
   On each unit-weight edge the successive phase difference is \(\pi+\delta\) for one class and \(\pi-\delta\) for the other, and the closing edge has the corresponding difference \(-k\delta\) or \(+k\delta\) modulo \(2\pi\). Their common minimum energy is
   \[
   E_n(w)=-k\cos\delta+w\cos(k\delta).
   \]
The magnitude of the stationary bond current is \(J(w)=\sin\delta\) above the transition and \(J(w)=0\) below it. As \(w\downarrow1/k\) from above,
\[
J(w)=\sqrt{\frac{6k}{k^2-1}}\,\sqrt{w-1/k}+O_k((w-1/k)^{3/2}),
\]
and the energy changes relative to the continued unfrustrated configuration by
\[
(-k+w)-E_n(w)=\frac{3k^3}{2(k^2-1)}(w-1/k)^2+O_k((w-1/k)^3).
\]
At the threshold the minimizing energy has a *strict quartic*, rather than quadratic, restoring term along its only degenerate direction. Away from the threshold each minimizing phase class is a hyperbolic attracting fixed point of the corresponding explicit-Euler repulsive gradient phase map for sufficiently small positive step size. At the threshold no hyperbolicity is claimed.

## Assumptions and scope

The vertex set is a simple ring of odd size \(n\ge5\); each of the first \(n-1\) edges has coupling weight one, and precisely the closing edge has positive coupling weight \(w\). There are no prescribed external frequencies, delays or phase shifts. The energy is a smooth function on the quotient torus of phase configurations modulo diagonal rotation. The repulsive discrete Huygens update is \(\theta^+=\theta-h\nabla V_w(\theta)\pmod{2\pi}\), with \(h>0\). Results concerning *global minimizers* hold at every positive \(w\) without imposing a step size; stability of the update is asserted only for sufficiently small \(h\) away from the threshold. No claim is made about every nonglobal equilibrium, basin sizes, or almost-everywhere convergence.

## Proof

**Step 1: reduce the frustrated ring to an exact simplex problem.** Write the \(n\) directed edge differences as \(d_i\in\mathbb R/(2\pi\mathbb Z)\), with \(\sum_i d_i=0\pmod{2\pi}\). Because \(n\) is odd, choose preferred-opposition errors \(e_i\in[-\pi,\pi]\) defined by \(d_i=\pi+e_i\pmod{2\pi}\). The closure condition is
\[
\sum_i e_i=\pi\pmod{2\pi},\qquad V_w=-\sum_{i=1}^{k}\cos e_i-w\cos e_{k+1}.
\]
Hence \(\sum_i|e_i|\ge\pi\). Since cosine is strictly decreasing on \([0,\pi]\), one can replace the absolute values by numbers \(0\le t_i\le|e_i|\) with \(\sum_i t_i=\pi\), without increasing energy. The new positive errors satisfy ring closure and are realizable by phases. If any positive magnitude was strictly reduced, energy strictly decreases, since all edge weights are positive. At a true global minimum, therefore, \(\sum_i|e_i|=\pi\), and closure forces all nonzero errors to have the same sign (apart from the identification of \(\pi\) and \(-\pi\)). It suffices to maximize
\[
\sum_{i=1}^k\cos t_i+w\cos u,
\qquad t_i\ge0,\ u\ge0,\quad \sum_{i=1}^kt_i+u=\pi.
\]

**Step 2: rigorously equalize the strong-bond errors.** Fix \(S=\sum_i t_i=\pi-u\le\pi\). For any two strong errors \(a,b\ge0\),
\[
\cos a+\cos b=2\cos\!\left(\frac{a+b}{2}\right)\cos\!\left(\frac{a-b}{2}\right)
\le2\cos\!\left(\frac{a+b}{2}\right),
\]
because \(a+b\le\pi\). Repeated pairwise averaging forces an optimum with all \(t_i=S/k\). The maximizing tuple is unique for \(k\ge4\): averaging is strict for unequal entries whenever their sum is less than \(\pi\); the sole exceptional pair sum \(\pi\) forces all remaining entries to vanish, and averaging either nonzero entry with a zero then gives strict improvement. Therefore all strong edges have common error \(\delta\in[0,\pi/k]\), while the weak error is \(u=\pi-k\delta\). The global minimization is **exactly** the one-variable maximization
\[
B_w(\delta)=k\cos\delta-w\cos(k\delta),\quad 0\le\delta\le\pi/k,\qquad E_n(w)=-\max B_w.
\]

**Step 3: the unique phase transition.** Differentiation yields
\[
B_w'(\delta)=k\bigl[-\sin\delta+w\sin(k\delta)\bigr].
\]
On \((0,\pi/k)\), \(R_k(\delta)=\sin(k\delta)/\sin\delta\) decreases strictly from \(k\) to zero. Indeed its logarithmic derivative has sign that of \((k\delta)\cot(k\delta)-\delta\cot\delta\), and \(t\cot t\) decreases strictly on \((0,\pi)\) (its derivative is \((\sin t\cos t-t)/\sin^2t<0\)). Thus if \(w\le1/k\), \(B_w'\) is negative at every interior point, so its unique maximum is \(\delta=0\). If \(w>1/k\), the derivative changes sign exactly once, from positive to negative, at the unique stated \(\delta\). The two signs of the preferred-opposition errors yield exactly two distinct phase classes, exchanged by reflection. At \(\delta=0\) the two signs describe the same class.

**Step 4: sharp critical expansion and local stability.** Taylor expansion gives
\[
\frac{\sin\delta}{\sin(k\delta)}
=\frac1k\left(1+\frac{k^2-1}{6}\delta^2+O_k(\delta^4)\right).
\]
It follows that \(\delta^2=6k(w-1/k)/(k^2-1)+O_k((w-1/k)^2)\), giving the displayed current law. Expanding \(B_w\) at the threshold also gives
\[
B_{1/k}(\delta)=k-1/k-\frac{k(k^2-1)}{24}\delta^4+O_k(\delta^6).
\]
Substituting the critical displacement in \(B_w\) proves the energy-gap coefficient \(3k^3/[2(k^2-1)]\).

For \(w<1/k\), the constrained Hessian of the **maximized** objective at its unique maximizer, in the \(k\) independent strong-edge error coordinates, is \(-I+w\mathbf1\mathbf1^T\); it is negative definite. For \(w>1/k\), the constrained Hessian is \(-\cos\delta\,I+w\cos(k\delta)\mathbf1\mathbf1^T\), with negative eigenvalues \(-\cos\delta\) on the \(k-1\)-dimensional transverse subspace and \(-\cos\delta+kw\cos(k\delta)<0\) on the common-error direction, the latter inequality following from the strict downward derivative crossing in Step 3. Thus both minima are strictly Hessian-positive on the phase quotient. The gradient Euler map has multipliers \(1-h\lambda_j\) at such a minimum, where \(\lambda_j>0\) are quotient Hessian eigenvalues; taking \(0<h<2/\max_j\lambda_j\) makes each minimum a hyperbolic local sink. At \(w=1/k\) the one-dimensional Hessian degeneracy and positive quartic restoring term follow from the expansion above; the map is not claimed hyperbolic there.

## Verification

The standalone script `verify.py` reconstructs the full phase energy from vertex phases, independently optimizes it over many random starts, and compares its values with the one-variable analytical prediction for odd ring sizes \(3,5,7,9\). It exercised 36 parameter choices and 1,080 independent random-start optimization attempts; every converged result stayed above the derived exact energy to numerical tolerance. The size-three case is **only a consistency check** and is not part of the claimed new range. The script does not prove global optimality; that is established by Steps 1–3. The threshold and expansions are derived analytically, not inferred from these finite computations.

## Relationship to prior work

Buescu and Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings* (arXiv:2610.19953v1, October 14, 2026), studies equal-weight rings and the long-time dynamics of their phase maps. The present classification concerns a **single variable edge weight on every odd ring of length at least five**; the uniform case \(w=1\) is just one parameter point, not sufficient to determine the sharp nonuniform transition. Buescu, D'Aniello and Oliveira, *Morse–Smale dynamics in discrete Huygens networks* (arXiv:2610.10993v1, October 7, 2026), provides a different graph-dependent dynamical stability treatment. Zhao and Zhou, *Critical Points, Stability, and Basins of Attraction of Three Kuramoto Oscillators with Isosceles Triangle Network* (arXiv:2407.11314, July 2024), treats three oscillators; no three-oscillator classification is asserted as new here. Earlier studies of quantum antiferromagnetic rings with one defective bond concern discrete spin and total-spin quantum numbers, rather than the classical planar phase-energy classification of this theorem. Historical priority beyond the inspected material is not claimed.

## Limitations

This is an exact theorem on global energy minima and their small-step linear stability, **not** a classification of all equilibria or basins. It assumes equal positive repulsive strengths on all but one edge, a single positive exceptional strength, odd size at least five, identical oscillator frequencies, and sinusoidal nearest-neighbor interactions. The result is insensitive to the Euler step except for the stated local-stability consequence. It does not establish any global convergence rate or Morse–Smale property. Exact coincidence with older work on classical defective XY rings remains a historical-priority risk, because certain plausibly related full texts were not accessible for comparison.

## References

1. J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1, October 14, 2026, https://arxiv.org/abs/2610.19953.
2. J. Buescu, E. D'Aniello, and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, October 7, 2026, https://arxiv.org/abs/2610.10993.
3. X. Zhao and X. Zhou, *Critical Points, Stability, and Basins of Attraction of Three Kuramoto Oscillators with Isosceles Triangle Network*, arXiv:2407.11314, July 16, 2024, https://arxiv.org/abs/2407.11314.
4. G. Kamieniarz, W. Florek, and M. Antkowiak, *Universal sequence of ground states validating the classification of frustration in antiferromagnetic rings with a single bond defect*, Phys. Rev. B 92, 140411(R) (2015), https://doi.org/10.1103/PhysRevB.92.140411.
