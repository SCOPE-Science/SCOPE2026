# Polar fourth moments reveal nematic ordering in a planar triadic balance model

## Finding
Let \(\theta_1,\ldots,\theta_N\in[0,2\pi)\) be distributed according to the canonical equilibrium law for the planar triadic Hamiltonian below. The polar vector \(P_N=N^{-1/2}\sum_j e^{i\theta_j}\) has exactly temperature-independent covariance, but its fourth moment detects nematic order:
\[
\mathbb E|P_N|^2=1,\qquad
\mathbb E|P_N|^4=2-\frac2N+\mathbb E|m_N|^2,
\qquad m_N=\frac1N\sum_j e^{2i\theta_j}.
\]
Thus the excess radial fourth moment (with the finite-size independent-spin correction removed) equals the nematic squared magnetization *exactly at every* \(N\ge3\).

Write \(c=J/(4k_BT)\), and define \(\rho(c)=0\) for \(c\le2\); for \(c>2\) let \(\rho(c)\in(0,1)\) be the unique solution of \(\rho=I_1(c\rho)/I_0(c\rho)\). For every fixed \(c>0\), the polar vector \(P_N\) converges weakly in \(\mathbb R^2\), with characteristic function
\[
\Phi_c(t)=\exp\!\left(-\frac{|t|^2}4\right)
I_0\!\left(\frac{\rho(c)|t|^2}4\right),\qquad t\in\mathbb R^2.
\]
Here \(I_0,I_1\) are modified Bessel functions. The limit is an ordinary centered isotropic Gaussian exactly for \(c\le2\), while for \(c>2\) it is a non-Gaussian uniform mixture of centered anisotropic Gaussians with eigenvalues \((1+\rho)/2\) and \((1-\rho)/2\). In particular the limiting one-coordinate *excess kurtosis* is \(3\rho(c)^2/2\), whereas its variance remains \(1/2\).

At \(c=2\) (equivalently \(k_BT_c=J/8\)),
\[
\sqrt N\!\left(\mathbb E|P_N|^4-2+\frac2N\right)
\longrightarrow\frac2{\sqrt\pi},
\]
and, uniformly for \(t\) in compact sets,
\[
\mathbb E e^{it\cdot P_N}=
\exp\!\left(-\frac{|t|^2}4\right)
\left[1+\frac{|t|^4}{32\sqrt{\pi N}}+O_t(N^{-1})\right].
\]
This is a critical polar non-Gaussian correction even though the limiting polar law at criticality is Gaussian.

## Assumptions and scope
For integer \(N\ge3\), fixed coupling \(J>0\), and inverse thermal energy \(\beta=(k_BT)^{-1}>0\), the canonical probability measure has density proportional to \(e^{-\beta H_N}\) relative to independent uniform angular measure, where
\[
H_N=-\frac{J}{N^2}\sum_{1\le i<j<k\le N}
\cos(\theta_i-\theta_j)\cos(\theta_j-\theta_k)\cos(\theta_k-\theta_i).
\]
Both the thermodynamic law and the characteristic-function expansion hold with fixed \(c=\beta J/4\) as \(N\to\infty\). The result concerns the zero-external-field canonical ensemble, including angular and gauge fluctuations; it is not a symmetry-broken-state statement. The critical correction uses the exact finite-\(N\) Hamiltonian, not a replacement of its \(N-2\) factor by \(N\).

## Proof
**1. Exact change of variables and conditional signs.** The elementary identity
\[
\cos(a)\cos(b)\cos(a+b)=\frac14\big(1+\cos(2a)+\cos(2b)+\cos(2(a+b))\big)
\]
reduces the triadic energy, up to an angle-independent constant, to
\[
H_N=-\frac{J(N-2)}{4N^2}\sum_{i<j}\cos(2\theta_i-2\theta_j)+\text{constant}.
\]
Set \(\phi_j=2\theta_j\bmod 2\pi\). Conditional on \(\phi_1,\ldots,\phi_N\), the preimage angles satisfy \(e^{i\theta_j}=\varepsilon_j b_j\), with \(b_j=e^{i\phi_j/2}\) and independent fair signs \(\varepsilon_j\in\{-1,+1\}\). This is because the equilibrium density is constant on each of the \(2^N\) fibers of the doubled-angle map.

Conditional on the doubled angles, \(P_N=N^{-1/2}\sum_j\varepsilon_j b_j\). Expanding the Rademacher moments and using \(|b_j|=1\) yields
\[
\mathbb E_\varepsilon|P_N|^2=1,\quad
\mathbb E_\varepsilon(P_N^2)=\frac1N\sum_jb_j^2=m_N,\quad
\mathbb E_\varepsilon|P_N|^4=2-\frac2N+|m_N|^2.
\]
Rotation invariance implies \(\mathbb E m_N=0\). Averaging gives the exact finite-size identities.

**2. Nematic mean-field concentration.** With \(S_N=\sum_j e^{i\phi_j}\) and \(c_N=c(N-2)/N\), the doubled angles have Gibbs weight \(\exp(c_N|S_N|^2/(2N))\), up to a constant. Gaussian decoupling expresses their joint law as a mixture: introduce a planar field \(h\) with density proportional to
\[
\exp\!\left[N\left(\log I_0(|h|)-\frac{|h|^2}{2c_N}\right)\right]dh,
\]
and, conditional on \(h\), draw the \(\phi_j\) independently from density \(\exp(h\cdot(\cos\phi,\sin\phi))/(2\pi I_0(|h|))\). Its mean vector has magnitude \(I_1(|h|)/I_0(|h|)\), along the field direction.

For completeness, the strict decrease of \(I_1(r)/(r I_0(r))\) for \(r>0\) follows by writing it as one-half the expectation of \(1/(K+1)\) under weights proportional to \((r^2/4)^k/(k!)^2\). This family is strictly increasing in likelihood ratio as \(r\) grows, and \(1/(k+1)\) is strictly decreasing. The ratio decreases from \(1/2\) to zero. Consequently the radial field free energy has its unique maximum at the origin when \(c\le2\), and a unique positive maximizing radius \(r_*\) when \(c>2\). In the latter case \(r_*=c\rho(c)\) and the maximizing direction is uniform. Laplace concentration and the conditional law of large numbers show that \(m_N\) converges in distribution to zero if \(c\le2\), and to \(\rho(c)e^{iU}\) if \(c>2\), with \(U\) uniform on \([0,2\pi)\).

**3. The polar mixture limit.** Conditioned on \(\phi\), the Rademacher characteristic function is
\[
\mathbb E_\varepsilon e^{it\cdot P_N}=
\prod_{j=1}^N\cos\!\left(\frac{t\cdot b_j}{\sqrt N}\right),
\]
where each complex \(b_j\) is identified with its real planar vector. The Taylor formula for \(\log\cos\), uniformly for fixed bounded \(t\), yields
\[
\prod_j\cos\!\left(\frac{t\cdot b_j}{\sqrt N}\right)
=\exp\!\left[-\frac{|t|^2}4-
\frac14\operatorname{Re}\!\left((t_1-it_2)^2m_N\right)
+O_t(N^{-1})\right].
\]
Since the angle of \(m_N\) is uniform by rotational invariance, averaging its conditional exponent gives \(e^{-|t|^2/4}I_0(|t|^2|m_N|/4)+O_t(N^{-1})\). The concentration in Step 2 and bounded continuity of the Bessel factor establish \(\Phi_c\). In the ordered case \(I_0(z)>1\) for \(z>0\), proving non-Gaussianity; direct Gaussian covariance averaging gives eigenvalues \((1\pm\rho)/2\). The exact fourth-moment identity and \(|m_N|\le1\) justify moment convergence and the one-coordinate kurtosis formula.

**4. Critical amplitude.** At \(c=2\), the auxiliary field \(h=N^{-1/4}u\) has radial limiting density proportional to \(u\exp(-u^4/64)\,du\), because \(\log I_0(r)=r^2/4-r^4/64+O(r^6)\) and \(c_N=2(N-2)/N\). The conditional doubled-spin mean equals \(h/2+O(|h|^3)\), while the conditional sample-mean noise is \(O_{L^2}(N^{-1/2})\). Quartic radial Laplace bounds give the moment expansion
\[
\mathbb E|m_N|^2=\frac2{\sqrt{\pi N}}+O(N^{-1}),
\qquad \mathbb E|m_N|^4=O(N^{-1}).
\]
Indeed the limiting radial second moment for \(u\) is \(8/\sqrt\pi\). Substitution in the exact fourth-moment formula gives the critical fourth-moment amplitude. Finally \(I_0(z)=1+z^2/4+O(z^4)\), combined with Step 3 and the two nematic moment bounds, gives the stated compact-uniform characteristic-function correction.

## Verification
Run the standalone script `verify_polar_nematic.py` with Python, NumPy and SciPy. It enumerates every sign vector for thirty finite-angle instances, checking the exact conditional second and fourth moments. Independent one-dimensional Gaussian-decoupling quadrature for four sizes approaches the predicted critical amplitude \(2/\sqrt\pi\); four angular integrations verify the Bessel characteristic function. The checks support algebra and normalization, but are not substitutes for the limiting proof. The reported tests executed successfully from the packaged script.

## Relationship to prior work
Arab Mohammadi, Kargaran, Hosseiny, Jafari and Saberi (2026) established the exact triadic-to-doubled-angle Curie–Weiss XY mapping, the gauge symmetry, the nematic transition, and the critical \(N^{-1/4}\) nematic law. Those are inputs, not new claims. The present result instead concerns the *undoubled polar sum*: its exact fourth-moment identity, full Gaussian-mixture law across temperatures, and first critical correction. Lacoste and Gaspard (2014) study rotational fluctuation relations and nematic tensor order more generally, not this polar scalar moment or its critical amplitude. A general Gaussian-mixture or Rademacher-chaos treatment might imply portions indirectly; publication-priority overlap remains a risk.

## Limitations
No external field, quenched gauge breaking, dynamics, finite-size rate away from criticality, or experimental noise model is treated. The critical \(O_t(N^{-1})\) remainder is at fixed \(t\) (uniform on compact sets), not globally uniform over arbitrary growing Fourier scales. The physical nematic finite-size law and critical temperature are established antecedents. Priority is asserted only for the exact polar-fluctuation statement after targeted literature checks, not for universal originality of its individual ingredients. Independent validation has not been performed.

## References
1. S. Arab Mohammadi, A. Kargaran, A. Hosseiny, R. Jafari and A. A. Saberi, *When Does Triadic Balance Reduce to Pairwise Order?* (2026), arXiv:2611.02117, https://arxiv.org/abs/2611.02117 (first public version 2026-11-01).
2. D. Lacoste and P. Gaspard, *Isometric Fluctuation Relations for Equilibrium States with Broken Symmetry*, Physical Review Letters **113**, 240602 (2014), https://doi.org/10.1103/PhysRevLett.113.240602.
