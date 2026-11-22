# Quadratic radial forcing is the unique least-dissipative nonconservative optical-trap profile

## Finding

Consider the stationary three-coordinate overdamped diffusion defined below. Among **all nonconstant smooth centered radial axial forces of polynomial growth and specified stationary force variance** \(V>0\), the quadratic profile \(f(x,y)=c(x^2+y^2-2)\) uniquely minimizes the total stationary entropy-production rate, up to the sign of \(c\). In the normalization used here, its sharp value is
\[
\boxed{\Sigma_{\min}=\frac{2V}{\eta(\eta+2)}.}
\]
Moreover, if \(\Pi_2 f\) denotes the orthogonal projection of \(f\) onto the centered quadratic radial mode, there is an **exact sharp stability gap**
\[
\boxed{\Sigma(f)-\frac{2V}{\eta(\eta+2)}\ge
\frac{2}{(\eta+2)(\eta+4)}\lVert f-\Pi_2 f\rVert_{L^2(\gamma_2)}^2.}
\]
Equality in this stability bound occurs exactly when \(f\) contains only radial Laguerre modes of degrees two and four (the quadratic-only case is included). An upper bound \(\Sigma(f)<V/\eta\) is optimal but is never attained by any nonzero admissible radial force; normalized Laguerre profiles of increasing degree approach it. These statements hold for every \(\eta>0\), without a small-force expansion.

## Assumptions and scope

Time is in units of the transverse Ornstein–Uhlenbeck relaxation time; the transverse equilibrium covariance is the identity. Let \(W^1,W^2,W^3\) be independent standard Brownian motions, and set
\[
\begin{aligned}
dX_t&=-X_t\,dt+\sqrt2\,dW^1_t,\\
dY_t&=-Y_t\,dt+\sqrt2\,dW^2_t,\\
dZ_t&=(-\eta Z_t+f(X_t,Y_t))\,dt+\sqrt{2\eta}\,dW^3_t,
\qquad \eta>0.
\end{aligned}
\]
The nonconservative axial drive is any centered radial \(C^\infty\) function whose derivatives have polynomial growth \(f(x,y)=F(s)\), where \(s=(x^2+y^2)/2\) and \(\int_0^\infty F(s)e^{-s}\,ds=0\). Its force budget is
\[
V=\int_0^\infty F(s)^2e^{-s}\,ds=\mathbb E[f(X_0,Y_0)^2]>0.
\]
The constant axial force component is irrelevant: it only shifts \(Z\) and contributes no stationary heat. The positional equilibrium reference is the Gaussian \(\gamma_2=N(0,I_2)\). All three coordinates are even under physical time reversal. Entropy production \(\Sigma\) means the stationary path-space forward/reversed relative-entropy rate, equivalently the integrated quadratic stationary probability-current functional, in units of Boltzmann's constant per unit dimensionless time. The diffusion matrix is \(\operatorname{diag}(1,1,\eta)\).

This model contains the quadratic radiation-pressure term of Mangeat, Guérin and Dean, arXiv:2110.04362, after translation of the axial coordinate and normalization of the force coefficient. The larger radial-force class is an idealized mathematical profile-design family, not a claim of optical realizability at arbitrarily large radial excursions.

## Proof

**1. Existence and stationary heat identity.** The independent transverse processes have their unique stationary \(N(0,I_2)\) law. The axial equation has the unique stationary representation
\[
Z_t=\int_0^\infty e^{-\eta u} f(X_{t-u},Y_{t-u})\,du
+\sqrt{2\eta}\int_{-\infty}^t e^{-\eta(t-s)}\,dW^3_s.
\]
The polynomial-growth force has finite Gaussian moments of every order, so the representation is well-defined and yields the unique attracting stationary distribution. Its uniformly elliptic diffusion has smooth stationary densities. The drift is the sum of the gradient-equilibrium drift \((-X,-Y,-\eta Z)\) and the extra force \((0,0,f)\). By the stationary Stratonovich heat/current identity, the gradient part contributes the stationary mean time derivative of \((X^2+Y^2+Z^2)/2\), which is zero. The force term contributes
\[
\Sigma=\frac1\eta\mathbb E[f(X_t,Y_t)\circ\dot Z_t]
=\frac1\eta\{V-\eta\mathbb E[f(X_t,Y_t)Z_t]\}.
\]
The second equality follows from the axial stochastic equation: the independent axial noise has zero cross-variation with the continuous function of the two transverse coordinates. This is the **full** stationary entropy-production rate, not a partial housekeeping-flux proxy.

**2. Radial spectral decomposition.** Put \(S_t=(X_t^2+Y_t^2)/2\). It has invariant density \(e^{-s}\mathbf1_{s>0}\) and generator
\[
(\mathcal L_S g)(s)=2s g''(s)+2(1-s)g'(s).
\]
The standard Laguerre polynomials \(L_m\), normalized by \(\int_0^\infty e^{-s}L_m(s)L_n(s)\,ds=\delta_{mn}\), satisfy \(\mathcal L_S L_m=-2mL_m\). Write the complete orthogonal expansion \(F(s)=\sum_{m\ge1}a_mL_m(s)\) in \(L^2(e^{-s}ds)\); centering excludes \(m=0\). The series converges in \(L^2\), and the semigroup, stationary convolution, and entropy quadratic form are bounded on this space, permitting termwise passage from finite sums. Stationarity and reversibility of \(S\) give
\[
\mathbb E[F(S_t)F(S_0)]=\sum_{m\ge1}a_m^2e^{-2m|t|},\qquad
V=\sum_{m\ge1}a_m^2.
\]
Substituting the stationary axial convolution into Step 1 yields the exact diagonal identity
\[
\boxed{\Sigma(F)=\frac1\eta\sum_{m\ge1}\frac{2m}{\eta+2m}a_m^2.}
\]
The independent axial noise drops out of the force--axial covariance; its variance still fixes the thermodynamic normalization \(1/\eta\).

**3. Exhaustive minimization.** For every \(\eta>0\), the weights \(w_m=2m/(\eta+2m)\) are strictly increasing in positive integer \(m\). Thus
\[
\Sigma(F)\ge\frac{w_1}{\eta}\sum_{m\ge1}a_m^2
=\frac{2V}{\eta(\eta+2)}.
\]
Equality forces \(a_m=0\) for every \(m\ge2\). Since \(L_1(s)=1-s\), this is precisely \(f=c(x^2+y^2-2)\) with the sign of \(c\) arbitrary and \(4c^2=V\). No other nonzero admissible centered radial force attains the minimum.

**4. Sharp gap, equality, and upper extremum.** For \(m\ge2\), strict monotonicity implies \(w_m-w_1\ge w_2-w_1=2\eta/((\eta+2)(\eta+4))\). Therefore
\[
\Sigma(F)-\Sigma_{\min}\ge\frac{2}{(\eta+2)(\eta+4)}\sum_{m\ge2}a_m^2.
\]
The sum is exactly \(\lVert f-\Pi_2f\rVert^2_{L^2(\gamma_2)}\). Equality holds only if all \(a_m=0\) for \(m\ge3\), and is attained by every nonzero mixture of \(L_1\) and \(L_2\) (including pure \(L_2\)). Finally \(0<w_m<1\) for each \(m\), giving \(\Sigma(F)<V/\eta\). The normalized pure \(L_M\) family has \(\Sigma(F_M)=V\,2M/[\eta(\eta+2M)]\to V/\eta\), proving sharp nonattainment of the upper bound.

## Verification

`checker.py` implements two independent exact-rational computations. One uses the Laguerre spectral identity above. The other applies the **stationary generator directly** to the raw polynomial moments \(\mathbb E[ZS^k]\), using
\[
(\eta+2k)\mathbb E[ZS^k]=2k^2\mathbb E[ZS^{k-1}]+\mathbb E[F(S)S^k],\quad \mathbb E[S^k]=k!,
\]
then computes \(\Sigma=(\mathbb E[F(S)^2]-\eta\mathbb E[ZF(S)])/\eta\). For five rational values of \(\eta\), pure modes through order six and mixed modes through order five, both methods agree exactly. The checker also tests the global bound, sharp gap equality, and upper-bound approach, totaling 189 exact rational assertions. Run `python3 checker.py` in the same directory. The proof above supplies the full smooth radial-class conclusion through the bounded spectral multiplier and monotone-weight argument; finitely many assertions do not replace it.

## Relationship to prior work

Mangeat, Guérin and Dean (arXiv:2110.04362, first version 2021-10-08) derived the stationary optical-trap distribution and circulation for the **specific quadratic** transverse forcing; that concrete force law and the stationary representation are prior art. Mangeat and collaborators (arXiv:1812.09188, first version 2018-12-21) studied nonlinear optical-scattering-induced currents and position/force cross-spectra, including an exact time-reversal-breaking spectral signal. The standard stochastic-thermodynamic path-ratio identity predates both (Seifert, 2005). The result here is a **shape optimization over smooth centered radial forcing laws of polynomial growth at fixed variance**, together with the exhaustive equality class and sharp quantitative stability gap; neither compared optical-trap treatment classifies that variational problem. The spectral calculation uses known Laguerre diagonalization and stationary heat identities as tools, rather than claiming their discovery.

## Limitations

The thermodynamic claim assumes all coordinates are observed and are even under time reversal, equal bath thermal normalization as displayed, additive independent Brownian noises, transverse isotropic Gaussian confinement, and axial linear relaxation. It does not cover inertial particles, nonlinear axial restoring forces, anisotropic transverse traps, arbitrary time-dependent control, or physical constraints on optical-beam intensity. The fixed-variance comparison permits oscillatory sign-changing polynomial and other sign-changing radial force profiles at large radius; the upper-bound sequence is mathematical and should not be interpreted as an experimentally realizable optical beam. No finite-data entropy-production estimator or empirical precision bound is provided. The standard spectral functional and general stochastic-thermodynamic identities make implicit prior coverage possible; independent publication-priority review has not been performed.

## References

1. M. Mangeat, T. Guérin, D. S. Dean, *Steady state of overdamped particles in the non-conservative force field of a simple non-linear model of optical trap*, arXiv:2110.04362v1 (2021-10-08), https://arxiv.org/abs/2110.04362.
2. M. Mangeat, Y. Amarouchene, Y. Louyer, T. Guérin, D. S. Dean, *The role of non-conservative scattering forces and damping on Brownian particles in optical traps*, arXiv:1812.09188v1 (2018-12-21), https://arxiv.org/abs/1812.09188.
3. U. Seifert, *Entropy Production along a Stochastic Trajectory and an Integral Fluctuation Theorem*, Phys. Rev. Lett. 95, 040602 (2005), https://doi.org/10.1103/PhysRevLett.95.040602.
4. R. J. Martin, I. J. Ford, *Stochastic entropy production in diffusive systems*, J. Phys. A 53, 255001 (2020), https://doi.org/10.1088/1751-8121/ab78d0.
