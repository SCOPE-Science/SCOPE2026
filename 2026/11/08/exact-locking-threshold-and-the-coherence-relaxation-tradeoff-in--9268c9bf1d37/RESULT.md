# Exact locking threshold and the coherence–relaxation tradeoff in a detuning-weighted Kuramoto triad

## Finding
Consider the three-node Kuramoto system with intrinsic frequencies \((-\omega,0,\omega)\), \(\omega>0\), and symmetric coupling strengths proportional to the \(p\)-th power of frequency separation, where \(p\ge0\). Normalize the nonnegative coupling weights by their average per-node budget \(B>0\):
\[
\dot\theta_i=\Omega_i+\sum_{j\ne i}K_{ij}\sin(\theta_j-\theta_i),\qquad
\frac13\sum_{i,j}K_{ij}=B,
\]
\[
K_{12}=K_{23}=a=\frac{3B}{2(2+z)},\qquad K_{13}=b=za,\qquad z=2^p.
\]
Set \(K_{ii}=0\). All phase-locked equilibria below are identified modulo a common rotation, and **linearly attracting** means that both eigenvalues transverse to the common-rotation direction have strictly negative real part.

Define
\[
c_z=\frac{\sqrt{1+32z^2}-1}{8z},\quad
\alpha_z=\arccos c_z,\quad
B_c(p)=\frac{2\omega(z+2)}{3[\sin\alpha_z+z\sin(2\alpha_z)]}.
\]
There exists exactly one linearly attracting phase-locked equilibrium if and only if \(B>B_c(p)\). It is represented uniquely by \((\theta_1,\theta_2,\theta_3)=(-\varphi,0,\varphi)\), where \(0<\varphi<\alpha_z\) is the unique solution of
\[
\omega=\frac{3B}{2(z+2)}[\sin\varphi+z\sin(2\varphi)].
\]
At equality, the symmetric branch has a nonhyperbolic fold; below the threshold no linearly attracting locked equilibrium exists.

The threshold \(B_c(p)\) is strictly decreasing for \(p\ge0\), and
\[
B_c(p)>\frac{2\omega}{3}\quad\text{for every finite }p,\qquad
\lim_{p\to\infty} B_c(p)=\frac{2\omega}{3}.
\]
For each fixed \(B>2\omega/3\), the attracting branch exists for all sufficiently large \(p\); its phase spread \(\varphi(p)\) decreases strictly, and its Kuramoto coherence \(R(p)=(1+2\cos\varphi(p))/3\) increases strictly.

This coherence gain comes with a sharp dynamical cost. Put
\[
s=\frac{2\omega}{3B}\in(0,1),\quad
\varphi_\infty=\frac12\arcsin s,\quad
\delta=\frac{2s-\sin\varphi_\infty}{2\cos(2\varphi_\infty)}>0,\quad
R_\infty=\frac{1+2\cos\varphi_\infty}{3}.
\]
If \(\gamma(p)\) is the smaller of the two positive transverse exponential decay rates, then as \(p\to\infty\), with \(B,\omega\) fixed,
\[
\boxed{R_\infty-R(p)=\frac23\sin\varphi_\infty\,\delta\,2^{-p}+O(2^{-2p}),}
\]
\[
\boxed{\gamma(p)=\frac{9B}{2}\cos\varphi_\infty\,2^{-p}+O(2^{-2p}).}
\]
Thus arbitrarily selective allocation improves local locked-state phase coherence but makes the slowest transverse relaxation time grow proportionally to \(2^p\). At the formal limit \(p=\infty\), the middle oscillator decouples, so the limiting locked configuration is not hyperbolically attracting as a full three-node state.

## Assumptions and scope
The oscillators have exactly equally spaced mean-zero intrinsic frequencies, pairwise positive symmetric weights for every finite \(p\), and fixed per-node budget as defined above. The statements concern phase-locked equilibria and their local transverse linearization, **not** global convergence from arbitrary initial phases or ensemble-average synchronization in the many-oscillator limit. Only \(p\ge0\), \(B>0\), \(\omega>0\) are considered. The limit \(p\to\infty\) is taken at fixed \(B,\omega\).

## Proof
**1. Exhaustion of possible attracting locks.** Write \(u=\theta_2-\theta_1\) and \(v=\theta_3-\theta_2\), modulo \(2\pi\). Because the intrinsic frequencies sum to zero, the common locked frequency is zero. The outer equilibrium equations give
\[
\omega=a\sin u+b\sin(u+v)=a\sin v+b\sin(u+v).
\]
As \(a>0\), every equilibrium satisfies \(\sin u=\sin v\). Hence either \(v=u\) or \(v=\pi-u\), modulo \(2\pi\). In the second case, \(u+v=\pi\): the two nearest-neighbor linearized edge weights are \(a\cos u\) and \(-a\cos u\), and the outer edge weight is \(-b\). The trace of the symmetric, linearized *positive* graph Laplacian is therefore \(-2b<0\). Since its common-rotation eigenvalue is zero, a negative transverse eigenvalue exists; this case cannot be linearly attracting.

In the symmetric case, rotate the equilibrium to \((-\varphi,0,\varphi)\). The exact equilibrium equation is \(\omega=a\sin\varphi+b\sin2\varphi\), and the two transverse Jacobian eigenvalues are
\[
-3a\cos\varphi,\qquad -(a\cos\varphi+2b\cos2\varphi).
\]
Both are negative only if \(\cos\varphi>0\) and the derivative of \(a\sin\varphi+b\sin2\varphi\) is positive. With \(\omega>0\), the first restriction forces \(\varphi\in(0,\pi/2)\) modulo \(2\pi\). On that interval the torque \(F(\varphi)=a\sin\varphi+b\sin2\varphi\) has \(F''(\varphi)=-a\sin\varphi-4b\sin2\varphi<0\), and \(F'(0)>0>F'(\pi/2)\). Hence it has exactly one interior maximum, its increasing branch contains precisely one solution when \(\omega<F_{\max}\), and this is the unique linearly attracting lock. At \(\omega=F_{\max}\) its second transverse eigenvalue is zero.

**2. Exact boundary and monotonicity.** The maximum solves
\[
0=\cos\alpha_z+2z\cos2\alpha_z
=4z\cos^2\alpha_z+\cos\alpha_z-2z,
\]
which has the stated unique positive cosine root. Substituting this maximizing angle gives the displayed \(B_c(p)\). Let \(G(z,\varphi)=[\sin\varphi+z\sin2\varphi]/(z+2)\). Its partial derivative at a fixed phase is
\[
\partial_z G(z,\varphi)=\frac{\sin\varphi(4\cos\varphi-1)}{(z+2)^2}.
\]
The maximum angle satisfies \(\cos\alpha_z\ge\cos\alpha_1=(\sqrt{33}-1)/8>1/4\) for \(z\ge1\): indeed implicit differentiation of \(4zc_z^2+c_z-2z=0\) gives \(c'_z=(2-4c_z^2)/(1+8zc_z)>0\), since \(c_z<1/\sqrt2\). Consequently, the maximal \(G\) grows strictly with \(z\), proving \(B_c\) strictly decreases in \(p\). On the attracting branch \(0<\varphi<\alpha_z\), so \(\partial_zG>0\) while \(\partial_\varphi G>0\). Implicit differentiation at fixed \(B,\omega\) gives \(d\varphi/dz<0\) and hence \(dR/dz>0\).

Because \(\sin\varphi+z\sin2\varphi\le1+z<2+z\), every finite-\(p\) threshold exceeds \(2\omega/3\). The maximum of \(\sin2\varphi\) over \([0,\pi/2]\) equals one, giving \(B_c(p)\to2\omega/3\).

**3. Singular relaxation and coherence asymptotics.** Fix \(B>2\omega/3\), set \(\epsilon=z^{-1}=2^{-p}\), and divide the locking equation by \(z\):
\[
s=\frac{\sin2\varphi+\epsilon\sin\varphi}{1+2\epsilon},
\qquad s=\frac{2\omega}{3B}.
\]
The limiting stable root is \(\varphi_\infty=\tfrac12\arcsin s\in(0,\pi/4)\). Its nonzero derivative \(2\cos2\varphi_\infty\) allows the implicit function theorem. Expanding gives
\[
\varphi(p)=\varphi_\infty+\delta\epsilon+O(\epsilon^2),\qquad
\delta=\frac{2s-\sin\varphi_\infty}{2\cos2\varphi_\infty}>0.
\]
Taylor expansion of \(R=(1+2\cos\varphi)/3\) produces its claimed strict positive first-order deficit. The two *positive* transverse decay rates are exactly
\[
\gamma_1=3a\cos\varphi,\qquad
\gamma_2=a\cos\varphi+2b\cos2\varphi.
\]
Since \(a=(3B/2)\epsilon/(1+2\epsilon)\), \(b=(3B/2)/(1+2\epsilon)\), their asymptotics are
\[
\gamma_1=\frac{9B}{2}\cos\varphi_\infty\,\epsilon+O(\epsilon^2),\qquad
\gamma_2=3B\cos2\varphi_\infty+O(\epsilon).
\]
The latter limit is strictly positive; therefore \(\gamma=\min(\gamma_1,\gamma_2)=\gamma_1\) for large \(p\), completing the proof.

## Verification
The standalone finite numerical checker `verify.py` constructs normalized weights, solves the attracting branch by scalar bracketing, computes the full three-by-three Kuramoto Jacobian directly, compares its spectrum to both explicit transverse eigenvalues, checks monotonicity and the limiting coefficients, and tests example parameters. Run `python verify.py` with Python 3, NumPy and SciPy. A successful local execution printed `VERIFY_OK checks=423 asymptotic_cases=15 full_jacobian_and_phase=52`. These tests support numerical consistency but do not replace any proof above.

## Relationship to prior work
Pando et al., *Enhanced synchronization with proportional coupling in Kuramoto oscillator networks under a fixed coupling budget* (arXiv:2603.29648v1; extended v2), motivate the exact power-law detuning family and establish nonmonotone, typically finite optimum exponents from simulations and continuum self-consistency for many oscillators. The present three-oscillator statement demonstrates a mathematically sharp different finite-size regime: the locked-state coherence is strictly monotone in the exponent while its local relaxation collapses at the limiting allocation.

The broad total-budget lower bound \(B\ge\sum_i|\Omega_i|/3=2\omega/3\) is **not** claimed as new: Mikaberidze and Taylor's *Emergent Topology of Optimal Networks for Synchrony* develops that general necessary bound. The new conclusion concerns the exact finite-exponent branch, exclusion of competing attracting nonsymmetric equilibria, and the two explicit, competing \(2^{-p}\) asymptotic laws. Tanaka and Aoyagi's work optimizes weighted networks but does not give this prescribed power-family singular stability boundary. The convex-geometric finite-Kuramoto framework of Garijo et al. treats uniformly weighted complete graphs; Wang et al. establish an approximate uniform-coupling finite-size criterion. These and classical three-oscillator equilibrium algebra do not imply the exact unequal-edge, prescribed-power-family asymptotic stability law.

## Limitations
The conclusions apply only to a symmetric three-oscillator system with equally spaced frequencies and power-law edge weights under the stated budget. Other frequency triples, signed weights, larger networks, noisy dynamics, global basins, and bifurcations of drifting trajectories are not addressed. A zero transverse eigenvalue at the limiting allocation does not imply nonlinear instability of every trajectory; it means that an isolated hyperbolically attracting full-phase equilibrium is absent. The quoted finite checks are not a proof. Historical originality is assessed against the cited accessible literature and remains subject to independent scholarly confirmation.

## References
1. A. Pando et al., *Enhanced synchronization with proportional coupling in Kuramoto oscillator networks under a fixed coupling budget*, arXiv:2603.29648, first version March 31, 2026, https://arxiv.org/html/2603.29648.
2. G. Mikaberidze and D. Taylor, *Emergent Topology of Optimal Networks for Synchrony*, arXiv:2509.18279, https://arxiv.org/html/2509.18279.
3. T. Tanaka and T. Aoyagi, *Optimal weighted networks of phase oscillators for synchronization*, Physical Review E 78 (2008), 046210, https://doi.org/10.1103/PhysRevE.78.046210; author PDF https://tanaka-takuma-lab.github.io/site/ttakuma2008b.pdf.
4. C. Xu et al., *Synchronization of phase oscillators with frequency-weighted coupling*, Scientific Reports 6 (2016), 21926, https://www.nature.com/articles/srep21926.
5. X. Xin, T. Kikkawa and Y. Liu, *Analytical solutions of equilibrium points of the standard Kuramoto model: 3 and 4 oscillators*, 2016 American Control Conference, https://doi.org/10.1109/ACC.2016.7525284.
6. A. Garijo, S. Gómez and A. Arenas, *A convex-geometric framework for fully phase-locked states in the finite Kuramoto model*, arXiv:2604.14772, https://arxiv.org/pdf/2604.14772.
7. C. Wang, N. Rubido, C. Grebogi and M. S. Baptista, *Approximate solution for frequency synchronization in a finite-size Kuramoto model*, Physical Review E 92 (2015), 062808, https://doi.org/10.1103/PhysRevE.92.062808.
