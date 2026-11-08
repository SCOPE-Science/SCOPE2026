# A sharp off-axis third-cumulant transition for orientationally reset active Brownian motion

## Finding
Consider an active Brownian particle in the plane whose orientation is reset to the positive horizontal axis at rate \(r>0\). Let \(d>0\) be rotational diffusivity, \(v>0\) propulsion speed, and \(D\geq0\) independent translational diffusivity. For a unit measurement direction \(n=(\cos\phi,\sin\phi)\), define the stationary-asymptotic third cumulant rate
\[
K_3(\phi)=\lim_{t\to\infty}\frac{1}{t}\operatorname{cum}_3\bigl(n\cdot(R_t-R_0)\bigr).
\]
This limit exists and equals
\[
K_3(\phi)=-A\cos^3\phi-3B\cos\phi\sin^2\phi,
\]
where the strictly positive amplitudes are
\[
A=\frac{12d^3rv^3(67d^2+191dr+52r^2)}{(d+r)^5(4d+r)^2(9d+r)},\qquad
B=\frac{12d^2rv^3(23d+7r)}{(d+r)^3(4d+r)^2(9d+r)}.
\]
The mixed rate \(\lim_{t\to\infty}t^{-1}\operatorname{cum}(X_t,Y_t,Y_t)=-B\) is nonzero, though the purely transverse third rate vanishes. In every direction with \(\cos\phi>0\), the third rate is strictly negative, and its sign reverses for \(\cos\phi<0\).

Write \(q=r/d\). There is a unique positive root
\[
q_*=1.94554336387280\ldots\quad\text{of}\quad14q^3+22q^2-85q-21=0.
\]
For \(0<q\le q_*\), the absolute third cumulant rate is uniquely maximized, up to sign reversal of the measurement axis, by the reset axis. For \(q>q_*\), the maximizers are instead the two reflected oblique unoriented lines making angles \(\pm\phi_*\) with the resetting direction, where
\[
\cos^2\phi_*=\frac{B}{3B-A},\qquad0<\phi_*<\frac{\pi}{2}.
\]
As \(q\to\infty\), these angles tend to \(\arccos(1/\sqrt3)\). The transition and angle are independent of \(v\) and \(D\). This optimizes the *unstandardized third cumulant per unit time*, not standardized finite-time skewness.

## Assumptions and scope
The orientation \(\Theta_t\) lives on \(\mathbb R/(2\pi\mathbb Z)\) and obeys Brownian angular diffusion of generator \(d\partial_\theta^2\) between independent Poisson resets to \(\Theta=0\) at rate \(r\). The planar displacement satisfies
\[
dR_t=v(\cos\Theta_t,\sin\Theta_t)\,dt+\sqrt{2D}\,dW_t,
\]
where \(W_t\) is independent standard planar Brownian motion. All claimed limits hold from any fixed starting angle, and in particular from the unique stationary angular law. No translational-position resetting, chirality, angular drift or distribution of reset angles is included. The time variable tends to infinity before the dimensionless limits \(q\downarrow0\) or \(q\uparrow\infty\).

## Proof
The angular generator on observables is
\[
Lf=d f''+r\{f(0)-f(\theta)\}.
\]
Its invariant expectation \(\langle\cdot\rangle\) satisfies \(m_j=\langle\cos(j\Theta)\rangle=r/(r+j^2d)\) and \(\langle\sin(j\Theta)\rangle=0\). With \(h_j=\cos(j\theta)-m_j\) and \(s_j=\sin(j\theta)\), one has \(-Lh_j=(r+j^2d)h_j\), \(-Ls_j=(r+j^2d)s_j\). Thus the centered Poisson resolvent \(G=(-L)^{-1}\) satisfies
\[
Gh_j=\frac{h_j}{r+j^2d},\qquad Gs_j=\frac{s_j}{r+j^2d}.
\]
The angular process is exponentially mixing and the bounded tilted generator \(L+k v f\) has an analytic simple leading eigenvalue near \(k=0\), for \(f(\theta)=\cos\phi\cos\theta+\sin\phi\sin\theta\). Centering \(h=f-\langle f\rangle\), third-order eigenvalue perturbation gives
\[
K_3(\phi)=6v^3\langle h\,G(h\,Gh)\rangle.
\]
Here \(G\) subtracts the stationary mean of any argument; constants play no role in the pairing with \(h\). The independent translational Brownian term adds only \(Dk^2\) to the tilted eigenvalue, contributing no cubic derivative.

For the horizontal component, write \(a_1=r+d\), \(a_2=r+4d\), and
\[
V_1=\frac{1+m_2}{2}-m_1^2,\qquad C_{12}=\frac{m_1+m_3}{2}-m_1m_2.
\]
The identity \(h_1^2-V_1=\tfrac12h_2-2m_1h_1\) yields
\[
K_{xxx}=\frac{6v^3}{a_1}\left(\frac{C_{12}}{2a_2}-\frac{2m_1V_1}{a_1}\right)=-A.
\]
For the mixed term use \(s_1^2-\langle s_1^2\rangle=-\tfrac12h_2\) and \(h_1s_1=\tfrac12s_2-m_1s_1\). Differentiating the tilted eigenvalue once in the horizontal tilt and twice in the transverse tilt gives the sum of the three placements of \(h_1\):
\[
K_{xyy}=2v^3\left[-\frac{C_{12}}{2a_1a_2}+\frac{2}{a_1}\left(\frac{m_1-m_3}{4a_2}-\frac{m_1(1-m_2)}{2a_1}\right)\right]=-B.
\]
Reflection \(\theta\mapsto-\theta\) kills the tensor components with an odd number of transverse factors, leaving only \(K_{xxx}\) and the three permutations of \(K_{xyy}\). Substituting the explicit \(m_1,m_2,m_3\) and factoring produces the displayed positive \(A,B\).

For \(c=|\cos\phi|\in[0,1]\), the magnitude of the cubic rate is
\[
F(c)=A c^3+3B c(1-c^2),\qquad F'(c)=3B+3(A-3B)c^2.
\]
If \(A\ge2B\), \(F\) is strictly increasing before \(c=1\) and the unique maximum is axial. If \(A<2B\), \(F'\) has its unique zero \(c^2=B/(3B-A)\) in \((0,1)\), giving the two reflected oblique lines. The threshold reduces to
\[
\frac{A}{B}-2=-\frac{14q^3+22q^2-85q-21}{(1+q)^2(23+7q)}.
\]
The cubic is negative at zero, positive at infinity, and has exactly one positive zero by Descartes' sign rule; therefore the stated cases exhaust all \(r,d>0\). Finally \(A/B\to0\) as \(q\to\infty\), hence \(c^2\to1/3\).

## Verification
Execute `python CHECK.py` with Python 3, `sympy`, and `mpmath`. The checker tests both Poisson-resolvent cubic identities symbolically, the angular threshold polynomial, its positive root, 15 high-precision third-derivative evaluations from a separate Fourier tilted-generator eigenvalue calculation, and five angular-maximizer cases. The extracted code passed all 25 assertions. The harmonic truncation is used only to check cubic derivatives, whose perturbation series reaches angular harmonics at most three; the analytical proof above, not the numerical finite differences, establishes the global claim.

## Relationship to prior work
Baouche, Franosch, Meiners and Kurzthaler (arXiv:2405.06769v1, 10 May 2024) give the orientational-reset ABP model, the full intermediate scattering function and marginal third moments, finding negative longitudinal skewness at intermediate times. Their formulas in principle determine the mixed tensor after differentiation; the new statement is the explicit *long-time mixed third cumulant* together with a sharp global off-axis maximizing-direction phase transition. Kumar, Sadekar and Basu (arXiv:2008.03294v1, 7 August 2020) analyze orientation-only resetting and marginal first and second moments. Neither inspected treatment states the mixed cubic-rate factorization or the angular transition. This is a structural extraction from an exactly solvable model, not a claim of a new stochastic process or independent characteristic function.

## Limitations
The result concerns long-time third cumulant *rates* and their unstandardized angular magnitudes, not finite-time skewness maxima, standardized coskewness, first-passage statistics, or large-deviation tails. The exact intermediate scattering function in the cited source implicitly fixes all cumulants, so priority for derived specializations remains a publication risk. The theorem applies only to deterministic reset orientation and Poisson reset times; it makes no claim of universal behavior for other protocols. No independent audit has been performed.

## References
1. Y. Baouche, T. Franosch, M. Meiners, C. Kurzthaler, "Active Brownian particle under stochastic orientational resetting," arXiv:2405.06769v1 (10 May 2024), https://arxiv.org/html/2405.06769v1 .
2. V. Kumar, O. Sadekar, U. Basu, "Active Brownian Motion in two-dimensions under Stochastic Resetting," arXiv:2008.03294v1 (7 August 2020), https://arxiv.org/html/2008.03294v1 .
