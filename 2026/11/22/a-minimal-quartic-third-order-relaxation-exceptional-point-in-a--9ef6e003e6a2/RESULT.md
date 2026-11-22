# A minimal quartic third-order relaxation exceptional point in a harmonically trapped active Brownian particle

## Finding

The fourth positional polynomial of a harmonically trapped active Brownian particle has a third-order, rather than merely a second-order, defective relaxation mode at the equality of trap and angular relaxation rates. This is **the first possible positional moment degree** with a term quadratic in time multiplying an exponential. At the positive-rate resonance \(D_r=\kappa\), its conditional relaxation contains the exactly determined term
\[
\frac{v^4}{2\kappa^2}t^2e^{-4\kappa t}\cos(2\Theta_0).
\]
Here the word *contains* specifies a coefficient in an exact finite exponential-polynomial expansion, not the entire conditional expectation. This coefficient is independent of translational thermal diffusivity. The relevant invariant nine-dimensional polynomial sector has a **single size-three Jordan block** at eigenvalue \(-4\kappa\).

## Assumptions and scope

For \(\kappa,v,D_r>0\) and \(D\ge0\), let independent standard Brownian motions \(W,B\) drive
\[
dX_t=(-\kappa X_t+v\cos\Theta_t)dt+\sqrt{2D}\,dW_t,\qquad
d\Theta_t=\sqrt{2D_r}\,dB_t\pmod{2\pi}.
\]
The initial state \((X_0,\Theta_0)\) may be arbitrary and deterministic. Take \(D_r=\kappa\). Define \(s=D/\kappa\) and monic scaled probabilists' Hermite polynomials \(H_j(x)=s^{j/2}\operatorname{He}_j(x/\sqrt s)\) for \(D>0\), extended continuously at \(s=0\) as \(H_j(x)=x^j\). Thus \(H'_j=jH_{j-1}\), \((D\partial_x^2-\kappa x\partial_x)H_j=-j\kappa H_j\), and \(H_4=x^4-6sx^2+3s^2\). A relaxation *mode* here is a term in the finite-dimensional backward-generator evolution of polynomial--angular observables; no claim about completeness of the full spatial/angular function-space spectrum is made.

## Proof

**1. An invariant finite-dimensional sector.** The backward generator is
\[
\mathcal L=(-\kappa x+v\cos\theta)\partial_x+D\partial_x^2+D_r\partial_\theta^2.
\]
For all \(j\ge0\), \(m\ge0\),
\[
\mathcal L[H_j\cos(m\theta)]=-(j\kappa+m^2D_r)H_j\cos(m\theta)+
\begin{cases}
jvH_{j-1}\cos\theta,&m=0,\
\frac{jv}{2}H_{j-1}[\cos((m-1)\theta)+\cos((m+1)\theta)],&m\ge1.
\end{cases}
\]
When \(j=0\) the last term is zero. For a positional polynomial of degree at most \(N\), the reachable invariant space is spanned by \(H_j\cos(m\theta)\) with \(0\le j\le N\), \(0\le m\le N-j\) and \(m\equiv N-j\pmod2\) for a leading \(H_N\). Descending in \(j\) makes the matrix triangular with diagonal entries \(-j\kappa-m^2D_r\).

**2. Quartic resonance and exact Jordan order.** The reachable basis from \(H_4\), in descending position degree, consists of
\[
(4,0),(3,1),(2,0),(2,2),(1,1),(1,3),(0,0),(0,2),(0,4),
\]
where \((j,m)\) means \(H_j\cos(m\theta)\). At \(D_r=\kappa\), exactly \((4,0),(3,1),(0,2)\) share eigenvalue \(-4\kappa\), giving algebraic multiplicity three. The exact generator matrix, built from the formula above, has rank eight after adding \(4\kappa I\), so its geometric multiplicity at that eigenvalue is one. Therefore the entire algebraic eigenspace is one size-three Jordan block. The rank statement is independently checkable by exact elimination in the standalone verifier; the next step gives a direct nonzero cubic-resolvent-pole certificate, which also proves the asserted block size together with algebraic multiplicity three.

**3. Explicit cubic pole and conditional-moment coefficient.** Let \(z\) be a resolvent parameter and write \(R(z)=(zI-\mathcal L)^{-1}\) on that invariant space. The transition \((4,0)\to(3,1)\) has coefficient \(4v\). From \((3,1)\) to \((0,2)\) there are precisely three four-step paths, with intermediate pairs \(((2,0),(1,1))\), \(((2,2),(1,1))\) and \(((2,2),(1,3))\). Their contributions to the coefficient of \((z+4\kappa)^{-3}\), after multiplying the four transition rates and evaluating the two nonresonant denominators at \(z=-4\kappa\), are respectively
\[
\frac{3v^4}{2\kappa^2},\qquad -\frac{3v^4}{4\kappa^2},\qquad \frac{v^4}{4\kappa^2}.
\]
Thus their sum is nonzero and
\[
\lim_{z\to-4\kappa}(z+4\kappa)^3R(z)_{(0,2),(4,0)}=\frac{v^4}{\kappa^2}.
\]
Since the inverse Laplace transform of \((z+4\kappa)^{-3}\) is \(\tfrac12t^2e^{-4\kappa t}\), the conditional expectation \(\mathbb E[H_4(X_t)\mid X_0=x,\Theta_0=\theta]\) has the claimed coefficient \(v^4/(2\kappa^2)\) multiplying \(t^2e^{-4\kappa t}\cos(2\theta)\), for all \(t\ge0\). This is an exact spectral-decomposition coefficient and does not require stationary initialization.

**4. Sharp minimality in positional degree.** In the reachable triangular sectors from \(H_1,H_2,H_3\), every diagonal eigenvalue has algebraic multiplicity at most two at \(D_r=\kappa\): there are no three distinct pairs \((j,m)\) with \(j+m^2\) equal. Consequently no Jordan block larger than two can occur in these sectors. Every lower-degree positional polynomial is a linear combination of those observables, so none can produce a term proportional to \(t^2e^{\lambda t}\). Quartic order is therefore minimal.

## Verification

Run `python3 verify_ep.py` using Python and SymPy. The executable independently constructs the exact moment generator, tests eigenvalue algebraic and geometric multiplicities, computes the cubic resolvent-pole coefficient, checks the three-path rational identity, compares degrees one through three and verifies two independent rational rescalings of \(\kappa\) and \(v\). The script passes. The exact generator identity, path sum and multiplicity argument above provide the all-positive-parameter proof; finite symbolic cases supplement rather than replace it.

## Relationship to prior work

Caraglio and Franosch (arXiv:2210.04205, first posted 2022-10-09) construct the exact evolution of an active Brownian particle in a harmonic well using a triangular polynomial-mode representation and provide the general spectral eigenvalues; these are **not** claimed here as new. Their general propagator can in principle be specialized to coincident relaxation rates. The assessed contribution is the exact minimal-degree, **third-order defective** resonant block and its explicitly nonzero quartic conditional-moment coefficient. Nakul and Gopalakrishnan (arXiv:2209.09184) treat the stationary harmonic active Brownian problem, not the same finite-degree temporal Jordan classification. Related published studies of exceptional polynomial moments for two-state biased run-and-tumble models involve a different, finite orientation sector and size-two blocks. Nontrivial implication by a general formula remains a priority risk; independent literature verification is outstanding.

## Limitations

Only the specified ideal active Brownian diffusion in a harmonic trap, at \(D_r=\kappa\), and polynomial--Fourier observables are analyzed. The result is about the exact finite invariant observable sector, not a complete spectral theorem on the full generator domain. It does not claim uniqueness of the resonance over all parameter ratios or universality under nonlinear confinement, non-Markovian angle noise, or noisy finite-window measurements. The published triangular propagator may already imply the block by specialization; explicit originality assessment is qualified pending independent priority review.

## References

1. M. Caraglio and T. Franosch, *Analytic Solution of an Active Brownian Particle in a Harmonic Well*, arXiv:2210.04205 (first posted 2022-10-09), https://arxiv.org/abs/2210.04205.
2. J. Nakul and M. Gopalakrishnan, *Stationary states of an active Brownian particle in a harmonic trap*, arXiv:2209.09184 (2022), https://arxiv.org/abs/2209.09184.
