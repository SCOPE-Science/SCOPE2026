# Quadratic-observable slowdown hidden by optimal affine relaxation in a Gaussian sampler

## Finding

There is an exact and systematic gap between first- and second-degree convergence in a natural Gaussian version of reflected proximal sampling. For every \(0<\mu<L\) and \(\kappa=L/\mu>1\), calibrate the exact conditional mirror/refresh algorithm below to minimize its worst-case **affine** spectral radius over Hessian eigenvalues in \([\mu,L]\):

\[
\eta_*=(\mu L)^{-1/2},\qquad
\rho_* = \frac{4\kappa^{1/4}}{(1+\kappa^{1/4})^2},\qquad
q=\frac{\kappa^{1/4}-1}{\kappa^{1/4}+1}.
\]

The classical Gaussian affine/SOR analysis yields the sharp first-degree factor \(q\); that affine calibration is **not** claimed novel here. For either endpoint eigendirection \(\lambda\in\{\mu,L\}\), however, the homogeneous transition of the three covariance-error components \((\Delta\mathbb E X^2,\Delta\mathbb E[XY],\Delta\mathbb E Y^2)\) has characteristic polynomial

\[
\begin{split}
P_{t,\rho}(z)={}&z^3+[1-\rho+(3\rho-4)t^2]z^2\\
&+[\rho-1+(\rho-1)(\rho-4)t^2]z-(1-\rho)^2,
\end{split}
\]

where \(t=(1-\eta\lambda)/(1+\eta\lambda)\). **At the affine-optimal parameters**, \(t^2=4q^2/(1+q^2)^2\) and \(\rho=1-q^2\). Exact substitution gives

\[
P_{t,\rho}(q)=-\frac{4q^4(1-q)^3}{(1+q^2)^2}<0,
\qquad
P_{t,\rho}(1)=\frac{(1-q^2)^3}{1+q^2}>0.
\]

Consequently the second-degree transition has a real eigenvalue in \((q,1)\), and its spectral radius \(r_2\) satisfies the **strict universal gap** \(q<r_2<1\) for every \(\kappa>1\). This is observable in the *position variance*, not merely an artificial mixed-state polynomial: for a legitimate centered Gaussian initial law whose stationary joint covariance is perturbed by a positive multiple of the identity on an endpoint mode,

\[
\lim_{n\to\infty}\big(\mathbb E[X_{n,\lambda}^2]-\lambda^{-1}\big)^{1/n}=r_2>q.
\]

The quantity inside the root is positive for all \(n\). Thus a sharp optimization of expected affine observables can provably understate the geometric relaxation factor of quadratic observables. In contrast, a fixed-coefficient Gaussian autoregression propagates covariance by a tensor square of its mean matrix; the **shared Bernoulli switching** in this kernel breaks that implication. The assertion concerns only this exact ideal algorithm and its specified affine-optimal tuning, not all samplers or full-distribution mixing.

## Assumptions and scope

Take \(H\in\mathcal H_{\mu,L}\), the Gaussian target \(\pi_H=\mathcal N(0,H^{-1})\), and \(\eta>0\). The augmented stationary law is

\[
\Pi_\eta(dx,dy)\ \propto\ \exp[-x^\mathsf T Hx/2-\|y-x\|^2/(2\eta)]\,dx\,dy.
\]

Write \(A_\eta=(I+\eta H)^{-1}\) and \(C_\eta=(H+\eta^{-1}I)^{-1}\). Conditionally on \(Y=y\), the target law of \(X\) is \(q_y=\mathcal N(A_\eta y,C_\eta)\). The ideal sampler acts on a state \((X,Y)\) as follows, with a fresh independent Bernoulli decision each update:

1. Set \(Y^+=2X-Y\).
2. With probability \(\rho\), draw \(X^+\sim q_{Y^+}\) independently (conditional refresh).
3. With probability \(1-\rho\), set \(X^+=2A_\eta Y^+-X\) (conditional mirror).

This deterministic conditional mirror is a **specified new ideal Gaussian specialization**, not either of the kinetic conditional implementations of the motivating paper. The first-degree operator on centered affine observables supplies the calibration, but the main new assertion concerns the exact degree-two *covariance-error operator* and the actual position-variance relaxation from Gaussian initial laws. It is **not** a theorem on full \(L^2\) mixing, total variation, or the oracle cost of conditional Gaussian draws.

For fixed \((\eta,\rho)\), define \(r(H,\eta,\rho)\) as the spectral radius of the \(2d\)-by-\(2d\) matrix carrying \((\mathbb EX,\mathbb EY)\) to \((\mathbb EX^+,\mathbb EY^+)\); this equals the first-degree Markov-operator spectral radius. The minimax supremum ranges over all \(H\) with eigenvalues inside the **inclusive** interval, and includes the endpoints. All computations are in exact real arithmetic. The endpoint case \(\kappa=1\) is included.

## Proof

**Stationarity.** The outer map \((x,y)\mapsto(x,2x-y)\) preserves \(\Pi_\eta\), because \(Y-X\mid X\) is a centered Gaussian. For fixed \(y\), \(x\mapsto2A_\eta y-x\) is a reflection about the mean of \(q_y\) and preserves \(q_y\); independent conditional refresh preserves it as well. Therefore the mixed inner kernel and its composition with the outer reflection preserve \(\Pi_\eta\). The exact-invariance principle is already present in the motivating paper and is not claimed as new.

**First-degree transfer.** For any eigenvalue \(\lambda>0\), put \(a=(1+\eta\lambda)^{-1}\), \(t=2a-1=(1-\eta\lambda)/(1+\eta\lambda)\). Taking conditional expectations of the two branches and then projecting onto that eigenvector gives the scalar two-state matrix

\[
T_{\lambda,\eta,\rho}=
\begin{pmatrix}
4a-1-\rho(2a-1)&-a(2-\rho)\\
2&-1
\end{pmatrix},
\qquad
\det(zI-T_{\lambda,\eta,\rho})
=z^2-t(2-\rho)z+(1-\rho).
\]

The matrices for different eigenvalues form a direct sum after orthogonal diagonalization of \(H\), so \(r(H,\eta,\rho)\) is the maximum modulus of these quadratic roots over \(\lambda\in\operatorname{spec}(H)\). Set

\[
s(\eta)=\max\left\{\left|\frac{1-\eta\mu}{1+\eta\mu}\right|,\left|\frac{1-\eta L}{1+\eta L}\right|\right\}<1.
\]

The function \(\lambda\mapsto|(1-\eta\lambda)/(1+\eta\lambda)|\) is maximized over \([\mu,L]\) at an endpoint. For fixed \(\rho\), the larger root modulus of the displayed polynomial is nondecreasing in \(|t|\): in its complex-root region it equals \(\sqrt{1-\rho}\); in the real-root region it equals

\[
\frac{|t|(2-\rho)+\sqrt{t^2(2-\rho)^2-4(1-\rho)}}2.
\]

Thus the worst matrix has a mode with \(|t|=s(\eta)\), and minimizing \(r\) for fixed \(\eta\) is the scalar task of minimizing the root modulus of \(z^2-s(2-\rho)z+1-\rho\).

**Exact refresh optimum.** Let \(v=\sqrt{1-\rho}\in[0,1]\), and for \(s\in(0,1)\) put

\[
q(s)=\frac{s}{1+\sqrt{1-s^2}},
\qquad s=\frac{2q(s)}{1+q(s)^2}.
\]

At \(v=q(s)\), the polynomial is \((z-q(s))^2\), so the maximum root modulus is \(q(s)\). If \(v>q(s)\), the product of its two roots is \(v^2\), forcing the maximum modulus to be at least \(v>q(s)\). If \(v<q(s)\), evaluating the polynomial at \(z=q(s)\) gives

\[
q(s)^2-s(1+v^2)q(s)+v^2
=\frac{(1-q(s)^2)(v^2-q(s)^2)}{1+q(s)^2}<0.
\]

Hence a positive real root exceeds \(q(s)\). This proves the **unique** fixed-\(\eta\) minimizer \(\rho=1-q(s(\eta))^2\). At \(s=0\), the eigenvalues both vanish only for \(v=0\), again giving the unique optimum \(\rho=1\).

**Exact augmentation optimum.** The function \(q(s)\) is strictly increasing on \([0,1)\). The function \(s(\eta)\) is uniquely minimized when the two endpoint absolute fractions are equal. Solving

\[
\frac{1-\eta\mu}{1+\eta\mu}=\frac{\eta L-1}{\eta L+1}
\]

in the region \(1/L\le\eta\le1/\mu\) yields \(\eta_*=(\mu L)^{-1/2}\). Let \(k=\kappa^{1/4}\). Then \(s_*=(k^2-1)/(k^2+1)\), \(q(s_*)=(k-1)/(k+1)\), and \(\rho_*=1-q(s_*)^2=4k/(k+1)^2\). For every intermediate \(\lambda\), \(|t|<s_*\), so the polynomial has nonreal conjugate roots with product \(q_*^2\); at both endpoints its roots coalesce. Therefore every eigendirection has modulus \(q_*\). This also establishes global uniqueness for \(\kappa>1\); for \(\kappa=1\) the optimizer is uniquely \((\eta,\rho)=(\mu^{-1},1)\).

**All-refresh benchmark and exact two-step endpoint.** With \(\rho=1\), the roots are \(0,t\); balancing endpoints produces the minimum \(s_*=(\sqrt\kappa-1)/(\sqrt\kappa+1)\). When \(\kappa=1\), take \(\eta=\mu^{-1}\). In any coordinate, \(a=1/2\) and the refresh noise has variance \(\eta/2\). Starting from arbitrary deterministic \((x_0,y_0)\), after the first update \(x_1=y_1/2+\xi_1\), after the second \(y_2=2\xi_1\), \(x_2=\xi_1+\xi_2\), with independent \(\xi_1,\xi_2\sim\mathcal N(0,\eta I/2)\). Thus \(x_2\sim\mathcal N(0,\eta I)\), \(y_2\mid x_2\sim\mathcal N(x_2,\eta I)\), exactly \(\Pi_\eta\), independent of the starting state.

**Quadratic-error transfer and strict spectral gap.** Let \(M_0\) and \(M_1\) denote the deterministic coefficient matrices of the mirror and refresh branches in one Hessian mode, respectively:

\[
M_0=\begin{pmatrix}4a-1&-2a\\2&-1\end{pmatrix},\qquad
M_1=\begin{pmatrix}2a&-a\\2&-1\end{pmatrix}.
\]

The refresh branch adds independent zero-mean Gaussian noise only to the position coordinate. Subtracting the stationary covariance cancels this additive covariance; hence the covariance defect evolves **exactly** under the positive linear map

\[
\mathcal L(E)=(1-\rho)M_0EM_0^\mathsf T+\rho M_1EM_1^\mathsf T
\]

for any symmetric \(2\times2\) matrix \(E\). Relative to \(E\leftrightarrow(E_{11},E_{12},E_{22})\), the elementary lift of \(M=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) is

\[
\operatorname{Sym}^2(M)=\begin{pmatrix}a^2&2ab&b^2\\ac&ad+bc&bd\\c^2&2cd&d^2\end{pmatrix}.
\]

Expanding \((1-\rho)\operatorname{Sym}^2(M_0)+\rho\operatorname{Sym}^2(M_1)\) yields precisely the displayed cubic \(P_{t,\rho}\). For \(\lambda\in\{\mu,L\}\), the affine-optimal tuning has \(t=\pm2q/(1+q^2)\), and the two exact polynomial signs in the finding follow by substitution. By continuity there is a real eigenvalue strictly between \(q\) and \(1\), so \(r_2>q\).

**Upper stability bound.** Let \(\Sigma\succ0\) be the stationary covariance of the scalar joint Gaussian and let \(v=(\lambda+\eta^{-1})^{-1}>0\). The reflection branch has \(M_0\Sigma M_0^\mathsf T=\Sigma\); the refresh branch has \(M_1\Sigma M_1^\mathsf T=\Sigma-v e_1e_1^\mathsf T\). Therefore, setting \(E=v e_1e_1^\mathsf T\),

\[
\mathcal L^2(\Sigma)=\Sigma-\rho\{E+\mathcal L(E)\}\prec\Sigma.
\]

The final strict matrix inequality holds because \(E+\mathcal L(E)\succ0\): its quadratic form is the sum of \(v w_1^2\) and the strictly positive weighted squares of \(w^\mathsf TM_0e_1\) and \(w^\mathsf TM_1e_1\), which are nonzero for \(w=(0,w_2)\ne0\), since each matrix has lower-left entry \(2\). Since \(\mathcal L\) is positive on positive-semidefinite matrices, \(\mathcal L^2(\Sigma)\preceq(1-\delta)\Sigma\) for some \(\delta>0\), forcing \(r_2^2\le1-\delta<1\) by comparison on the cone (which spans symmetric matrices).

**Actual position-variance visibility.** The positive map \(\mathcal L\) satisfies \(\|\mathcal L^n\|_{\mathrm{op}\to\mathrm{op}}=\|\mathcal L^n(I)\|_{\mathrm{op}}\) on real symmetric matrices: if \(\|D\|_{\mathrm{op}}\le1\), then \(-I\preceq D\preceq I\), hence \(-\mathcal L^n(I)\preceq\mathcal L^n(D)\preceq\mathcal L^n(I)\). The Gelfand formula therefore gives \(\|\mathcal L^n(I)\|_{\mathrm{op}}^{1/n}\to r_2\). Moreover,

\[
[\mathcal L(F)]_{11}=\operatorname{tr}\left(F G\right),\quad
G=(1-\rho)(M_0^\mathsf Te_1)(M_0^\mathsf Te_1)^\mathsf T+
\rho(M_1^\mathsf Te_1)(M_1^\mathsf Te_1)^\mathsf T.
\]

The two first rows of \(M_0,M_1\) are linearly independent (their determinant is \(a>0\)), and \(0<\rho<1\), so \(G\succ0\). Hence for any \(F\succeq0\), \([\mathcal L(F)]_{11}\ge c\operatorname{tr}F\ge c\|F\|_{\mathrm{op}}\) for some \(c>0\). Applying this to \(F=\mathcal L^n(I)\) gives

\[
c\|\mathcal L^n(I)\|_{\mathrm{op}}\le [\mathcal L^{n+1}(I)]_{11}\le\|\mathcal L^{n+1}(I)\|_{\mathrm{op}},
\]

so the positive position-variance defect has exact root-asymptotic factor \(r_2\). Choose a centered initial Gaussian with covariance \(\Sigma+\varepsilon I\), \(\varepsilon>0\), in that endpoint mode (the other Hessian modes may start stationary). Its covariance defect is \(\varepsilon\mathcal L^n(I)\), proving the asserted legitimate-start variance law. The shared switching does not invalidate this unconditional second-moment recursion; it is precisely the reason the lift is a *mixture of tensor squares* rather than the tensor square of the mixed mean map.

## Verification

The standalone `verify.py` checks the exact rational covariance-lift cubic and its endpoint signs, together with stationary branch identities, first-degree calibration and bounded numerical roots. These finite tests corroborate, but cannot substitute for, the covariance-cone and strict-sign proof. For \(\mu=1,L=16\), first-degree calibration gives \(q=1/3\) whereas the endpoint quadratic spectral factor is approximately \(0.4098522657>1/3\). For \(\mu=1,L=256\), the respective factors are \(0.6\) and approximately \(0.687357688\).

## Relationship to prior work

Yuan, Guo and Chen (2026), §3.1, supply the ideal reflected-proximal algorithm and exact-invariance principle. Their specific accelerated kernels use kinetic conditional dynamics; the conditional mirror examined here is a new ideal specialization. Classical Adler/Neal Gaussian overrelaxation and Young's SOR spectral theory already explain the optimal **first-degree** critical-damping formula; neither that formula nor Gaussian stationarity is claimed novel. Roberts–Sahu (1997) derive rates for Gaussian Gibbs schemes but explicitly exclude stochastic overrelaxation from their analysis. Fox–Parker (2015) derive Gaussian Gibbs/matrix-splitting convergence and polynomial acceleration: for fixed linear-Gaussian transitions covariance relaxes by tensorized mean propagation. Here an independent Bernoulli selector alternates *two distinct deterministic coefficient matrices*, so the covariance transition is their weighted symmetric-square lifts, **not** the lift of their weighted mean. This logically blocks direct inference from those classical affine spectral results. Wolff (1992) gives prior Gaussian microcanonical/heat-bath hybrid overrelaxation, but its fixed-number sweep design and accessible abstract do not establish the present exact cubic sign obstruction. Older hybrid-MCMC literature remains a historical-priority risk.

## Limitations

The result concerns the exact ideal Gaussian conditional-mirror/refresh process with a *single shared Bernoulli choice per iteration*, and its specifically affine-optimal parameters. The strict slower quadratic mode is a spectral and position-variance statement, not a total-variation, \(L^2\), integrated-autocorrelation-time or practical sampling-cost theorem. No all-parameters minimax optimum for quadratic observables is claimed. The equality at \(\kappa=1\) is excluded because then the affine-optimal chain refreshes every time and samples the entire joint Gaussian in two updates. Historical priority in broader hybrid-overrelaxation literature has not been exhaustively settled.

## References

1. B. Yuan, W. Guo, and Y. Chen, *Reflected Proximal Dynamics for Accelerated High-Accuracy Log-Concave Sampling*, arXiv:2610.16248v1 (first public 2026-10-12), https://arxiv.org/html/2610.16248v1.
2. G. O. Roberts and S. K. Sahu, *Updating Schemes, Correlation Structure, Blocking and Parameterization for the Gibbs Sampler*, J. R. Stat. Soc. B 59 (1997), 291–317, https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/RobertsSahuJRSSB1997.pdf.
3. C. Fox and A. Parker, *Accelerated Gibbs sampling of normal distributions using matrix splittings and polynomials*, arXiv:1505.03512v1 (2015), https://arxiv.org/pdf/1505.03512.
4. R. M. Neal, *Suppressing Random Walks in Markov Chain Monte Carlo Using Ordered Overrelaxation*, technical report 9508 (1995), https://glizen.com/radfordneal/over.abstract.html.
5. S. L. Adler, *Overrelaxation algorithms for lattice field theories*, Phys. Rev. D 37 (1988), 458–471, https://doi.org/10.1103/PhysRevD.37.458.
6. U. Wolff, *Dynamics of hybrid overrelaxation in the Gaussian model*, Phys. Lett. B 288 (1992), 166–170, https://inspirehep.net/literature/333936.
