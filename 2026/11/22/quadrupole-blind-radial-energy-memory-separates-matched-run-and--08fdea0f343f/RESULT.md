# Quadrupole-blind radial-energy memory separates matched run-and-tumble and active Brownian traps

## Finding
For an athermal three-dimensional swimmer in an isotropic harmonic trap, the complete *normalized* stationary two-time autocovariance of radial squared displacement depends on only the dipolar angular relaxation rate, whereas its amplitude detects the independent quadrupolar relaxation rate. Thus two canonical orientation protocols matched to have exactly the same orientation autocorrelation can also have identical normalized energy autocorrelation at every time while exhibiting sharply different energy fluctuations.

Write \(\alpha=\gamma/\kappa>0\), \(\theta=\beta/\kappa>0\), and \(Q_t=\kappa^2|R_t|^2/v^2\), with \(\beta\) the quadrupolar angular relaxation eigenvalue. For every physically admissible process in the scope below, stationarity gives
\[
\mathbb E Q=\frac1{1+\alpha},\qquad
\mathbb E Q^2=\frac{18+5\theta}{3(1+\alpha)(3+\alpha)(2+\theta)},
\]
\[
V(\alpha,\theta):=\operatorname{Var} Q=
\frac{2(\alpha\theta+6\alpha-2\theta)}{3(1+\alpha)^2(3+\alpha)(2+\theta)}.
\]
For \(\tau=\kappa t\ge0\), the exact normalized stationary covariance is
\[
\frac{\operatorname{Cov}(Q_0,Q_t)}{\operatorname{Var}Q}=H_\alpha(\tau)=
\begin{cases}
\dfrac{(1+\alpha)e^{-2\tau}-2e^{-(1+\alpha)\tau}}{\alpha-1},&\alpha\ne1,\\
(1+2\tau)e^{-2\tau},&\alpha=1.
\end{cases}
\]
This curve is independent of the quadrupolar relaxation eigenvalue. Its right-hand curvature \(H_\alpha''(0)=-2(1+\alpha)\) identifies \(\alpha\) if the trap relaxation rate is known. Given \(\alpha\), one stationary fourth radial moment identifies the quadrupolar rate: setting \(S=3(1+\alpha)(3+\alpha)\mathbb E Q^2\), one has \(5<S<9\) and \(\theta=(18-2S)/(S-5)\). The formal derivative of the variance at fixed \(\alpha\) is \(-8/[3(1+\alpha)(3+\alpha)(2+\theta)^2]<0\); admissibility of a pair of angular eigenvalues is determined by its underlying Markov generator, not by arbitrary choices of positive numbers.

At matched first-harmonic relaxation \(\gamma\), complete isotropic run-and-tumble redraws at rate \(\gamma\) have \(\beta=\gamma\), while active Brownian rotational diffusion with diffusivity \(D_R=\gamma/2\) has \(\beta=3\gamma\). Their stationary radial-energy means and their normalized autocovariances coincide, but
\[
\frac{V_{\mathrm{RTP}}}{V_{\mathrm{ABP}}}=
\frac{(\alpha+4)(3\alpha+2)}{3\alpha(\alpha+2)}>1,
\qquad
V_{\mathrm{RTP}}-V_{\mathrm{ABP}}=
\frac{16\alpha}{3(1+\alpha)(2+\alpha)(3+\alpha)(3\alpha+2)}>0.
\]
The ratio diverges like \(4/(3\alpha)\) as \(\alpha\downarrow0\), and tends to \(1\) as \(\alpha\to\infty\). These statements concern equal-time and two-time **radial-energy** fluctuations, not equality of spatial distributions or unnormalized covariances.

## Assumptions and scope
Fix \(\kappa,v>0\). A three-dimensional trajectory satisfies \(dR_t/dt=-\kappa R_t+v n_t\) with no translational thermal noise. The orientation \(n_t\) is an autonomous stationary, isotropic, ergodic Markov process on the unit sphere \(S^2\), with generator \(\mathcal L_n\) acting as
\[
\mathcal L_n n_i=-\gamma n_i,\qquad
\mathcal L_n(n_i n_j-\delta_{ij}/3)=-\beta(n_i n_j-\delta_{ij}/3),\qquad \gamma,\beta>0.
\]
The eigenvalue conditions apply to all coordinate indices. The two specified physical models satisfy them. Write dimensionless time \(\tau=\kappa t\), dimensionless position \(Y=\kappa R/v\), and \(P=Y\cdot n\), \(Q=|Y|^2\). A stationary version exists by the convergent pathwise convolution \(Y_\tau=\int_{-\infty}^{\tau}e^{-(\tau-s)}n_s\,ds\), and satisfies \(|Y|\le1\). Its finite moments and all derivatives used below are therefore legitimate. We assume \(\operatorname{Var}Q>0\), which holds for both canonical models at every positive rate. The theorem does not assert that all pairs of positive eigenvalues are realizable as orientation processes.

## Proof
First, in dimensionless time, the joint backward generator is \(\mathcal L=(-Y+n)\cdot\nabla_Y+\mathcal L_n\). The unit-sphere and first-harmonic identities give
\[
\mathcal L Q=-2Q+2P,\quad
\mathcal L P=-(1+\alpha)P+1.
\]
Averaging in stationarity yields \(\mathbb E Q=\mathbb E P=(1+\alpha)^{-1}\).

Second, set \(F=\mathbb E Q^2\), \(A=\mathbb E(QP)\), and \(B=\mathbb E P^2\). Because \(n_i n_j=\delta_{ij}/3+(n_i n_j-\delta_{ij}/3)\), the quadrupolar eigenvalue enters the closed identities
\[
\mathcal L Q^2=-4Q^2+4QP,
\]
\[
\mathcal L(QP)=-(3+\alpha)QP+Q+2P^2,
\]
\[
\mathcal L P^2=-(2+\theta)P^2+2P+\frac\theta3 Q.
\]
Consequently \(A=F\), \((3+\alpha)F=\mathbb E Q+2B\), and \((2+\theta)B=(2+\theta/3)\mathbb E Q\). Substitution gives the stated \(F\), \(V\), and the rational inverse for \(\theta\). The variance derivative follows by differentiation. The derivative comparison is within the set of realizable processes.

Third, for nonnegative lag \(\tau\), let \(C(\tau)=\operatorname{Cov}(Q_0,Q_\tau)\) and \(D(\tau)=\operatorname{Cov}(Q_0,P_\tau)\). From the same two generator equations, \(D'(\tau)=-(1+\alpha)D(\tau)\) and \(C'(\tau)=-2C(\tau)+2D(\tau)\). The stationary identity \(A=F\), together with \(\mathbb E Q=\mathbb E P\), yields \(D(0)=C(0)=V\). Thus \(D(\tau)=Ve^{-(1+\alpha)\tau}\). Solving the forced linear equation for \(C\) proves \(C/V=H_\alpha\), including the continuous resonant limit \(\alpha=1\). Differentiating at the origin yields \(H_\alpha''(0)=-2(1+\alpha)\), and therefore the inverse relation for \(\alpha\).

Fourth, uniform-redraw run-and-tumble orientation obeys \(\mathcal L_n f=\gamma(\overline f-f)\) and therefore has first- and second-harmonic eigenvalues both equal to \(\gamma\). The spherical active Brownian orientation obeys \(\mathcal L_n=D_R\Delta_{S^2}\), whose degree-one and degree-two spherical-harmonic eigenvalues are \(2D_R\) and \(6D_R\). Choosing \(D_R=\gamma/2\) matches the dipolar rate and sets \(\theta=3\alpha\), compared with \(\theta=\alpha\) for RTP. Substituting these rates into the variance formula gives
\[
V_{\mathrm{RTP}}=\frac{2\alpha(\alpha+4)}{3(1+\alpha)^2(2+\alpha)(3+\alpha)},\qquad
V_{\mathrm{ABP}}=\frac{2\alpha^2}{(1+\alpha)^2(3+\alpha)(3\alpha+2)}.
\]
The positive ratio and gap, and their asymptotic limits, follow by factoring these rational expressions. This completes the all-lag comparison.

## Verification
The self-contained \(\texttt{check.py}\) reconstructs the five generator-moment balance equations, verifies their symbolic solution and strict comparison identities, checks the closed covariance ODE, resonance and inverse formulas, and tests positive exact-rational rate choices. Its independent simulated paths implement Poisson uniform reorientation and rotational Brownian orientation on the sphere at matched first-mode rate, measuring the stationary radial-energy mean, variance and lag correlation. The run passed 38 assertions. The simulations independently corroborate the exact mathematics and are not offered as proof.

At \(\alpha=1\), the predicted means are \(1/2\), the RTP and ABP variances are respectively \(5/72\) and \(1/40\), and their common normalized covariance at lag \(0.96\) is \(2.92e^{-1.92}\). One fixed-seed run produced RTP mean \(0.498169\), variance \(0.067504\), normalized lag correlation \(0.424642\); ABP mean \(0.501599\), variance \(0.024448\), normalized lag correlation \(0.438807\). The common predicted normalized lag correlation is approximately \(0.428092\). Small simulation discrepancies arise from finite sampling and time discretization.

## Relationship to prior work
Frydel [1] develops an exact stationary moment recurrence for trapped run-and-tumble particles, including the isotropic three-dimensional trap. Chaudhuri and Dhar [2] develop a general time-dependent moment hierarchy and calculate stationary fourth moments for confined active Brownian particles. Thus the separate stationary moments and the general idea of a moment hierarchy are established, not new claims. Caraglio and Franosch [4] give a full two-dimensional active-Brownian trap propagator, including ordinary positional correlations but not this three-dimensional radial-energy RTP–ABP identity. Solon, Cates and Tailleur [3] compare the two propulsion models and document distinct confined position profiles, including matched-effective-equilibrium limits. The present claim is the **single all-lag, mode-selective radial-energy covariance theorem**, its exact RTP–ABP amplitude separation at matched dipolar persistence, and the resulting two-mode inverse interpretation. Merely combining known one-point formulas does not yield the stated normalized all-lag identity without the stationary mixed-moment closure.

## Limitations
The proof treats noninteracting three-dimensional athermal swimmers under isotropic linear confinement. It does not assert that full stationary radial distributions, higher-time joint distributions, or fourth-order two-time laws coincide. It assumes angular stationarity, isotropy and the stated first two harmonic eigenrelations; arbitrary positive \((\gamma,\beta)\) pairs need not correspond to a valid angular Markov process. The general moment equations can be viewed as consequences of existing moment-hierarchy methods, so literature priority for related implicit formulations remains uncertain. There is no independent validation beyond the stated analytic argument and computational cross-checks.

## References
[1] D. Frydel, “Run-and-tumble oscillator: moment analysis of stationary distributions,” arXiv:2309.12537v1 (first posted 2023-09-21), especially Sections IV, VI and Appendix D. https://arxiv.org/html/2309.12537v1

[2] D. Chaudhuri and A. Dhar, “Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition,” arXiv:2005.14234 (first posted 2020-05-28), especially Sections 3.1 and 3.3–3.4. https://arxiv.org/abs/2005.14234

[3] A. P. Solon, M. E. Cates and J. Tailleur, “Active brownian particles and run-and-tumble particles: A comparative study,” *European Physical Journal Special Topics* **224** (2015), 1231–1262, DOI: 10.1140/epjst/e2015-02457-0, especially Section 2.4. https://www.lptmc.jussieu.fr/files/solon/papers/SolonEPJST2015.pdf

[4] M. Caraglio and T. Franosch, “Analytic Solution of an Active Brownian Particle in a Harmonic Well,” *Physical Review Letters* **129**, 158001 (2022), arXiv:2210.04205 (first posted 2022-10-09), especially the exact two-dimensional propagator and ordinary positional autocorrelation. https://arxiv.org/abs/2210.04205
