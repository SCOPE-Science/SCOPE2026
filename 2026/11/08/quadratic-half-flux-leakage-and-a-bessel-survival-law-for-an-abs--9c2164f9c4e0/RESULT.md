# Quadratic half-flux leakage and a Bessel survival law for an absorbing quantum ring

## Finding
For every fixed even integer \(n\ge4\), hopping amplitude \(J>0\), and trap rate \(\gamma>0\), let \(H_{n,\phi}\) and \(S_{n,\delta}(\tau)\) be as defined below. For \(k=0,\ldots,n/2-1\), put \(\theta_k=(2k+1)\pi/n\). The eigenvalues that are dark at half flux have the exact second-order expansions
\[
z_k(\pi+\delta)=2J\cos\theta_k-i\frac{4J^2}{\gamma n}\sin^2\theta_k\,\delta^2+O_{n,J,\gamma}(\delta^4).
\]
Consequently, with a particle initially at the vertex opposite the trap and physical time \(t=\gamma n\tau/(8J^2\delta^2)\), for every fixed \(\tau\ge0\),
\[
\lim_{\delta\to0}S_{n,\delta}(\tau)=F_n(\tau)=\frac2n\sum_{k=0}^{n/2-1}e^{-\tau\sin^2\theta_k}.
\]
The convergence is uniform for \(\tau\) in any compact subset of \([0,\infty)\). Taking a **subsequent**, not simultaneous, even-ring limit gives
\[
\lim_{n\to\infty,\ n\text{ even}}\lim_{\delta\to0}S_{n,\delta}(\tau)
=\frac1\pi\int_0^\pi e^{-\tau\sin^2\theta}\,d\theta
=e^{-\tau/2}I_0(\tau/2),
\]
with \(I_0(x)=\pi^{-1}\int_0^\pi e^{x\cos u}\,du\). The limiting curve has tail \(e^{-\tau/2}I_0(\tau/2)\sim(\pi\tau)^{-1/2}\) as \(\tau\to\infty\).

The exact static dark-state classification and ultimate-capture probabilities at zero and half flux are **not** new claims. This finding concerns the quadratic *time-dependent* leakage scale and the finite-ring/Bessel crossover.

## Assumptions and scope
Use the single-particle Hilbert space \(\mathbb C^n\) with site basis \(\{|j\rangle:j\in\mathbb Z/n\mathbb Z\}\). Define the dissipative no-click generator
\[
H_{n,\phi}=J\sum_{j\bmod n}\left(e^{i\phi/n}|j+1\rangle\langle j|+e^{-i\phi/n}|j\rangle\langle j+1|\right)-\frac{i\gamma}{2}|0\rangle\langle0|.
\]
The flux \(\phi\) is a dimensionless total Peierls phase; \(\hbar=1\). An initially normalized state \(|n/2\rangle\) has no-absorption probability
\[
S_{n,\delta}(\tau)=\big\|e^{-it H_{n,\pi+\delta}}|n/2\rangle\big\|^2,
\quad t=\frac{\gamma n}{8J^2\delta^2}\tau.
\]
All limits first fix \(n,J,\gamma\) and vary real nonzero \(\delta\to0\); only afterward is \(n\) allowed to increase through even integers. The error term in the eigenvalue formula is for each fixed \(n,J,\gamma,k\) and not uniform over changing ring size. No environment, other traps, dephasing, interactions, or stroboscopic detection are included.

## Proof
**1. Exact secular equation.** Write \(H_{n,\phi}=H_{0,\phi}-i\gamma |0\rangle\langle0|/2\), with \(H_{0,\phi}\) Hermitian, and set \(x=z/(2J)\). The free ring has Fourier energies \(2J\cos((2\pi r+\phi)/n)\), so its characteristic polynomial is \(2J^n[T_n(x)-\cos\phi]\), where \(T_n\) and \(U_{n-1}\) are Chebyshev polynomials. Translation symmetry gives the diagonal free resolvent \(\langle0|(z-H_{0,\phi})^{-1}|0\rangle=\tfrac1n\partial_z\log\det(z-H_{0,\phi})\). Since \(T_n'(x)=nU_{n-1}(x)\), the matrix-determinant lemma yields the polynomial identity
\[
\det(z-H_{n,\phi})=2J^n\left[T_n(x)-\cos\phi+\frac{i\gamma}{4J}U_{n-1}(x)\right].\tag{1}
\]
The identity extends through free-spectrum points by polynomial continuity.

**2. Simple formerly dark eigenvalues.** At \(\phi=\pi\), the \(n/2\) vectors
\[
v_k(j)=\sqrt{\frac2n}\,e^{i\pi j/n}\sin(\theta_k j),\qquad \theta_k=\frac{(2k+1)\pi}{n},
\]
are orthonormal, vanish at site zero, and satisfy \(H_{n,\pi}v_k=E_kv_k\) with \(E_k=2J\cos\theta_k\). Their eigenvalues are distinct. In (1), \(T_n(\cos\theta_k)=-1\) and \(U_{n-1}(\cos\theta_k)=0\), whereas
\[
\left.\partial_zU_{n-1}\left(\frac z{2J}\right)\right|_{z=E_k}=\frac{n}{2J\sin^2\theta_k}>0.
\]
Thus each \(E_k\) is a **simple** zero of the full characteristic polynomial despite its being doubly degenerate in the loss-free ring. Also \(\cos(\pi+\delta)=-1+\delta^2/2+O(\delta^4)\). The implicit-function theorem applied to (1) proves the announced analytic even-power eigenvalue expansion, including its negative imaginary coefficient.

**3. Disappearance of every other component on the stretched time scale.** For an eigenvector \(w\) of \(H_{n,\phi}\),
\[
\operatorname{Im}z=-\frac{\gamma|w(0)|^2}{2\|w\|^2}.
\]
A real eigenvalue therefore requires a free-ring eigenvector with zero amplitude at the trap. At exactly half flux the dark eigenspace is spanned by the \(v_k\). The remaining eigenvalues all have strictly negative imaginary parts; with fixed \(n\) they stay uniformly below the real axis for sufficiently small \(|\delta|\). Their evolution, including possible finite Jordan blocks, vanishes at times of order \(\delta^{-2}\). The isolated simple dark spectral projectors vary continuously with \(\delta\). At \(\delta=0\) their right/left eigenvectors coincide with the orthonormal \(v_k\), so their mutual inner products differ from orthogonality by \(O(\delta)\). The initial antipodal vector lies entirely in their span, because \(|v_k(n/2)|^2=2/n\) and these \(n/2\) weights sum to one. The bright component of the same initial vector is \(O(\delta)\), and norm cross terms involving distinct slow modes are also \(O(\delta)\), uniformly for bounded rescaled \(\tau\). Therefore the survival probability converges to the sum of the slow-mode squared amplitudes; the negative imaginary part in step 2 gives \(\exp(-\tau\sin^2\theta_k)\). This proves the finite-ring formula and compact-\(\tau\) uniformity.

For \(\delta\ne0\) sufficiently small, all eigenvalues have negative imaginary part: the Hermitian magnetic ring has simple eigenvalues for flux not congruent to zero or \(\pi\) modulo \(2\pi\), and each Fourier eigenvector has nonzero trap amplitude. Thus eventual capture is certain at any such fixed detuning, despite the long nearly protected transient.

**4. Subsequent continuum limit.** The \(\theta_k\) are midpoints of a uniform partition of \([0,\pi]\), and \(F_n(\tau)\) is its midpoint Riemann sum for \(\pi^{-1}\int_0^\pi e^{-\tau\sin^2\theta}\,d\theta\). Writing \(\sin^2\theta=(1-\cos2\theta)/2\) gives the displayed modified-Bessel representation. Laplace asymptotics near the two minima of \(\sin^2\theta\) at the integral endpoints (or standard asymptotics of \(I_0\)) give \((\pi\tau)^{-1/2}\) for large \(\tau\).

## Verification
The accompanying `verify_flux.py` computes the complex non-Hermitian site matrix independently from (1), verifies its determinant against (1), compares slow complex-eigenvalue widths with the stated quadratic coefficient, and directly propagates the no-click state at rescaled times. It also checks finite-ring midpoint sums against the modified Bessel function and its leading large-time form. The extracted standalone program passed 77 numerical checks, using Python 3, NumPy and SciPy. Numerical checks support but do not replace the exact determinant, perturbation, spectral-separation and Riemann-sum proofs above.

## Relationship to prior work
The zero-field ring with one trap, its dark odd sector, and its ordinary bright-sector relaxation were studied by Krapivsky, Luck and Mallick, *Survival of classical and quantum particles in the presence of traps* (arXiv:1311.6298, first posted 2013-11-25), especially section 4 and its equation (4.23). Their analysis of unthreaded rings does not give the half-flux detuning expansion or the rescaled Bessel curve. Emary, *Dark states in the magnetotransport through triple quantum dots* (arXiv:0705.2934, first posted 2007-05-21), proves magnetic-field lifting of a dark current blockade in a three-dot source/drain system, including a quadratic field response; it does not imply the all-even-ring slow spectral family or the sequential Bessel survival law. Le *et al.*, *How to suppress dark states in quantum networks and bio-engineered structures* (2018), study dark subspaces and absorption control, but not the present mode-resolved flux-detuning law. The known static half-flux protection and eventual-survival classification are explicitly excluded from the new result.

## Limitations
The Bessel curve is a **sequential** \(\delta\to0\), then \(n\to\infty\) limit for fixed positive \(J,\gamma\), not a proven joint limit. The algebraic tail belongs to the resulting limiting curve; every individual fixed-size \(F_n\) instead has an exponential tail. Spectral error constants need not be uniform in \(n\). The result concerns conditional no-click survival, not a normalized postselected state, a many-particle system, or finite-temperature transport. Historical-priority claims are limited by the examined sources, and independent verification has not been performed.

## References
- C. Emary, *Dark states in the magnetotransport through triple quantum dots*, arXiv:0705.2934 (2007-05-21), https://arxiv.org/html/0705.2934v1.
- P. L. Krapivsky, J. M. Luck, K. Mallick, *Survival of classical and quantum particles in the presence of traps*, arXiv:1311.6298 (2013-11-25), https://arxiv.org/abs/1311.6298, especially sections 4–5.
- T. P. Le et al., *How to suppress dark states in quantum networks and bio-engineered structures*, J. Phys. A 51 (2018) 365306, https://discovery.ucl.ac.uk/id/eprint/10063626/.
- E. Bach et al., *One-dimensional quantum walks with absorbing boundaries*, arXiv:quant-ph/0207008 (2002), https://arxiv.org/abs/quant-ph/0207008; a distinct discrete-time walk model.
