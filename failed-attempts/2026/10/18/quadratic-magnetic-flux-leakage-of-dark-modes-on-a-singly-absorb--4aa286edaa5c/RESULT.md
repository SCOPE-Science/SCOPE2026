# Quadratic magnetic-flux leakage of dark modes on a singly absorbing quantum ring

## Finding
For every integer \(N\ge3\), hopping magnitude \(J>0\), and loss strength \(\gamma>0\), consider a cyclic tight-binding Hamiltonian with Peierls flux \(\phi\), supplemented by the purely absorbing site potential \(-i\gamma |0\rangle\langle0|\). Every symmetry-protected dark eigenvalue at a zero- or half-quantum flux has a *purely imaginary* quadratic shift under a small flux detuning. Explicitly, if \(\phi_*\in\{0,\pi\}\) and \(q\in(0,\pi)\) satisfies \(Nq\equiv\phi_*\pmod{2\pi}\), then a unique analytic eigenvalue branch satisfies

\[
\lambda_q(\phi_*+\delta)
=2J\cos q-i\frac{2J^2\sin^2 q}{\gamma N}\,\delta^2+O(\delta^4)
\qquad(\delta\to0).
\]

In particular, the real part of this eigenvalue changes only at fourth order, and its leading decay linewidth depends on the hopping, trap strength, ring size, and unperturbed mode through the displayed elementary expression. Away from fluxes congruent to \(0\) or \(\pi\) modulo \(2\pi\), every eigenvalue has strictly negative imaginary part: the same ring has no exact dark mode.

## Assumptions and scope
Work in the single-particle vector space \(\mathbb C^N\) with orthonormal site vectors \(\{|j\rangle:j\in\mathbb Z/N\mathbb Z\}\). Fix \(N\ge3\), \(J>0\), and \(\gamma>0\). Set

\[
(H_\phi\psi)_j=J e^{i\phi/N}\psi_{j+1}+J e^{-i\phi/N}\psi_{j-1},
\qquad K_\phi=H_\phi-i\gamma|0\rangle\langle0|.
\]

The physical total flux \(\phi\) is dimensionless and taken modulo \(2\pi\). The expansion is at *fixed* \(N,J,\gamma,q\); it is not uniform as \(\gamma\to0\), \(N\to\infty\), or \(q\to0,\pi\). An eigenvalue is called dark when it is real, equivalently when its right eigenvector vanishes on site \(0\). The imaginary part uses the convention \(e^{-itK_\phi}\) for forward no-jump time evolution. The leading probability-decay rate of the corresponding eigenmode is therefore \(4J^2\sin^2(q)\,\delta^2/(\gamma N)+O(\delta^4)\).

## Proof
**1. Exact secular identity.** Write \(x=z/(2J)\) and let \(T_N\) denote the ordinary Chebyshev polynomial of the first kind, defined by \(T_N(\cos\theta)=\cos(N\theta)\). Plane-wave diagonalization gives the characteristic polynomial of the lossless ring,

\[
P_\phi(z)=\det(zI-H_\phi)=2J^N\big[T_N(z/(2J))-\cos\phi\big].
\]

The equality follows from the plane-wave energies \(2J\cos((2\pi\ell+\phi)/N)\), for \(0\le\ell<N\), and matching leading coefficients. The determinant lemma for the rank-one absorbing potential yields

\[
\det(zI-K_\phi)=P_\phi(z)+i\gamma\,\operatorname{cof}_{00}(zI-H_\phi).
\]

All diagonal cofactors of \(zI-H_\phi\) agree by cyclic translation symmetry. Their sum is the derivative of its determinant. Thus \(\operatorname{cof}_{00}(zI-H_\phi)=P_\phi'(z)/N\), first where the resolvent exists and then everywhere by polynomial continuation. Consequently the *exact all-flux characteristic polynomial* is

\[
\boxed{\det(zI-K_\phi)=2J^N\left[T_N(x)-\cos\phi+\frac{i\gamma}{2JN}T_N'(x)\right],\quad x=z/(2J).}
\]

**2. Simplicity of each protected dark eigenvalue.** Let \(\phi_*\in\{0,\pi\}\), \(s=\cos\phi_*\in\{+1,-1\}\), and choose \(q\in(0,\pi)\) with \(Nq\equiv\phi_*\pmod{2\pi}\). Set \(x_0=\cos q\) and \(z_0=2Jx_0\). Then \(T_N(x_0)=s\) and \(T_N'(x_0)=N\sin(Nq)/\sin q=0\). The Chebyshev differential equation

\[
(1-x^2)T_N''(x)-xT_N'(x)+N^2T_N(x)=0
\]

implies \(T_N''(x_0)=-N^2s/(1-x_0^2)\ne0\). If \(F(x,\phi)=T_N(x)-\cos\phi+i\gamma T_N'(x)/(2JN)\), then

\[
F_x(x_0,\phi_*)=-\frac{i\gamma Ns}{2J(1-x_0^2)}\ne0.
\]

Hence \(z_0\) is a simple eigenvalue of \(K_{\phi_*}\), even though it comes from a two-fold degenerate eigenvalue of \(H_{\phi_*}\), and the analytic implicit-function theorem supplies a unique local eigenvalue branch.

**3. Quadratic flux coefficient.** Since \(\cos(\phi_*+\delta)=s\cos\delta\), the characteristic equation has an even dependence on \(\delta\). Uniqueness of the analytic eigenvalue branch makes that branch even as well. Writing \(x(\delta)=x_0+c\delta^2+O(\delta^4)\) and expanding \(F(x(\delta),\phi_*+\delta)=0\) gives

\[
0=\frac{s}{2}\delta^2-\frac{i\gamma Ns}{2J(1-x_0^2)}c\,\delta^2+O(\delta^4).
\]

Therefore \(c=-iJ(1-x_0^2)/(\gamma N)\). Multiplication by \(2J\) and \(1-x_0^2=\sin^2 q\) gives exactly the claimed expansion. The leading coefficient is strictly negative imaginary because \(J,\gamma>0\) and \(q\in(0,\pi)\). It has no real part.

**4. No dark eigenvalues at generic flux.** For any right eigenpair \(K_\phi\psi=z\psi\), dissipativity gives

\[
\operatorname{Im}z\,\|\psi\|^2=-\gamma|\psi_0|^2.
\]

A real eigenvalue therefore requires a lossless-ring eigenvector with \(\psi_0=0\). When \(\phi\not\equiv0,\pi\pmod{2\pi}\), the free-ring plane-wave energies are all nondegenerate (cosine-pair degeneracy would require \(2\phi\equiv0\pmod{2\pi}\)), and every plane wave has nonzero amplitude at every site. Hence no real eigenvalue exists at those fluxes. At \(\phi_*\), every interior member of a degenerate plane-wave pair has precisely one combination vanishing at site \(0\); these are the eigenvalues treated in steps 2–3. Any nondegenerate band-edge mode is not dark.

## Verification
The standalone `VERIFY.py` constructs the non-Hermitian matrix from individual hoppings, independently computes its determinant and numerical eigenvalues, and compares them with the Chebyshev formula and the leading linewidth. It passed **33 nontrivial characteristic-determinant evaluations** for ring lengths \(3\le N\le13\), with relative errors at most \(1.33\times10^{-15}\), and **195 small-flux eigenvalue checks** for \(3\le N\le12\), three loss/hopping pairs, and both protected fluxes. The maximum tested relative linewidth-coefficient discrepancy was \(5.33\times10^{-5}\) at detuning \(0.006\) radians, consistent with the proved fourth-order remainder. These finite calculations check the implementation and arithmetic; the all-size theorem follows from the analytic determinant and implicit-function argument, not from enumeration.

To reproduce: install Python 3 and NumPy, place `VERIFY.py` alongside this file, and execute `python VERIFY.py`. The check uses no network resources or unpublished inputs.

## Relationship to prior work
Krapivsky, Luck, and Mallick [1] explicitly analyze loss-avoiding quantum modes and long-time survival on a *zero-flux* finite ring, including multiple absorbing sites. Existence of the zero-flux dark subspace is therefore prior work, not a discovery claimed here. The distinguishing assertion is the universal complex-eigenvalue response to a *small magnetic flux*: the exact second-order imaginary coefficient, absence of a second-order real shift, and the fourth-order remainder for every ring size and every protected mode. The zero-flux mode formula by itself neither states nor supplies this flux derivative.

Longhi [2] studies non-Hermitian *continuum* rings and flux-dependent Bloch spectra for general complex potentials. Gou and collaborators [3] demonstrate a dissipative flux-threaded *three-site scattering element coupled to leads*, emphasizing nonreciprocal transport rather than isolated finite-ring dark-mode linewidths. Burke, Wiersig, and Haque [4] investigate a single imaginary scattering defect on an *open chain without a magnetic flux*. The inspected models overlap physically but do not give the all-size rank-one Chebyshev identity or the protected eigenvalue's purely imaginary quadratic flux shift. These comparisons support originality within the examined literature; they are not a claim that all possible sources have been excluded.

## Limitations
This is a one-particle no-jump spectral result. It does **not** compute a full many-body Liouvillian gap or an exact finite-detuning survival law; the spectral branch need not control the globally slowest mode for every choice of parameters. The asymptotic remainder is local in detuning for each fixed positive loss rate and finite system, and no uniform estimate as parameters vary is asserted. This work has undergone self-review; independent audit and broader priority verification have not been performed.

## References
[1] P. L. Krapivsky, J. M. Luck and K. Mallick, *Survival of classical and quantum particles in the presence of traps*, Journal of Statistical Physics 154 (2014), arXiv:1311.6298v2, Section 4.2–5. https://arxiv.org/abs/1311.6298

[2] S. Longhi, *Non-Hermitian quantum rings*, Physical Review A 88, 062112 (2013), arXiv:1312.4693v1, Sections I–II. https://arxiv.org/abs/1312.4693

[3] W. Gou et al., *Tunable non-reciprocal quantum transport through a dissipative Aharonov-Bohm ring in ultracold atoms*, Physical Review Letters 124, 070402 (2020), arXiv:2001.01859v1 (first public 2020-01-07). https://arxiv.org/abs/2001.01859

[4] P. C. Burke, J. Wiersig and M. Haque, *Non-Hermitian scattering on a tight-binding lattice*, Physical Review A 102, 012212 (2020), arXiv:1910.07439v2, Sections I–II. https://arxiv.org/abs/1910.07439
