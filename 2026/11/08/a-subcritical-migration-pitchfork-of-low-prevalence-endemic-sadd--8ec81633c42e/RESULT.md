# A subcritical migration pitchfork of low-prevalence endemic saddles in two identical patches

## Finding

In the deterministic two-patch susceptible–infected–temporarily recovered epidemic model with nonlinear reinfection and the explicitly specified positive rates below, the synchronized *lower endemic equilibrium* undergoes a nondegenerate, **subcritical patch-exchange pitchfork** at
\[
d_*=\frac{\sqrt{26689}-143}{240}=0.084865347761646\ldots.
\]
There is an open neighborhood of this equilibrium and a number \(\varepsilon>0\) such that, for \(d\in(d_*-\varepsilon,d_*)\), precisely two additional positive, asymmetric endemic equilibria occur there, exchanged by swapping the patches; for \(d\in[d_*,d_*+\varepsilon)\), no additional equilibrium occurs there. This is a *local* count, not a global equilibrium classification. Both asymmetric branches have exactly one unstable linear eigenvalue in the full six-dimensional system. The synchronized lower endemic equilibrium has two unstable eigenvalues just below \(d_*\), one just above \(d_*\), and one zero eigenvalue at \(d_*\).

Writing the leading amplitude of the infected-state difference as \(t\), the branch is described by
\[
\begin{aligned}
(I_1,R_1)&=z_-+t e+t^2h+O(t^3),\\
(I_2,R_2)&=z_--t e+t^2h+O(t^3),\\
d(t)&=d_*+\frac{\eta}{2}t^2+O(t^4),
\end{aligned}
\]
where \(e_1=1\), \(z_-=(1/30,1/70)\), and
\[
\eta=-\frac{166845}{52}+\frac{26656035\sqrt{26689}}{1387828}
=-70.7519352159\ldots<0.
\]
In particular, the equilibrium infection imbalance has the square-root law
\[
|I_1-I_2|=2\sqrt{\frac{2(d_*-d)}{-\eta}}+O((d_*-d)^{3/2}).
\]

## Assumptions and scope

The six population compartments at patch \(j\in\{1,2\}\) are susceptible \(S_j\), infected \(I_j\), and temporarily recovered \(R_j\). Let \(N_j=S_j+I_j+R_j\), and let \(k=3-j\). At states with \(N_j>0\), consider the deterministic flow
\[
\begin{aligned}
\dot S_j&=1-\frac32\frac{I_j}{N_j}S_j-S_j+d(S_k-S_j),\\
\dot I_j&=\frac32\frac{I_j}{N_j}S_j-2I_j+40\frac{I_j}{N_j}R_j+d(I_k-I_j),\\
\dot R_j&=I_j-40\frac{I_j}{N_j}R_j-R_j+d(R_k-R_j).
\end{aligned}
\]
This is the equal-patch parameter specialization \(\Lambda_j=\mu_j=\gamma_j=1\), \(\beta_j=3/2\), \(\rho_j=40\), and symmetric migration \(\delta_{12}=\delta_{21}=d>0\) of the deterministic equations in the cited two-patch literature. The isolated-patch invasion number is \(\mathcal R_0=3/4\). Claims refer to equilibria sufficiently close to the stated positive synchronized equilibrium and to their local linear stability, not to global attractors, stochastic extinction, or epidemiological parameter calibration. All coordinates represent nonnegative normalized populations.

## Proof

**1. Demographic reduction.** Summing the compartment equations gives
\[
\dot N_j=1-N_j+d(N_k-N_j).
\]
Its only equilibrium is \((N_1,N_2)=(1,1)\), with eigenvalues \(-1\) and \(-1-2d\). The plane \(N_1=N_2=1\) is invariant. Every equilibrium of the six-dimensional model is on this plane; the two demographic eigenvalues remain negative independently of the infection Jacobian. On this plane, eliminate \(S_j=1-I_j-R_j\), put \(z_j=(I_j,R_j)^T\), and obtain
\[
\dot z_1=F(z_1)+d(z_2-z_1),\qquad
\dot z_2=F(z_2)+d(z_1-z_2),
\]
where
\[
F(x,r)=\begin{pmatrix}x(-\frac12-\frac32x+\frac{77}{2}r)\\x-r-40xr\end{pmatrix}.
\]
The homogeneous equilibria of the single-patch reaction law are \((0,0)\), \(z_-=(1/30,1/70)\), and \(z_+=(1/4,1/44)\). At \(z_-\) the reaction Jacobian is
\[
A=DF(z_-)=\begin{pmatrix}-\frac1{20}&\frac{77}{60}\\\frac37&-\frac73\end{pmatrix},\quad
\operatorname{tr}A=-\frac{143}{60},\quad\det A=-\frac{13}{30}.
\]
Its eigenvalues are \(\lambda_\pm=(-143\pm\sqrt{26689})/120\), with \(\lambda_+>0>\lambda_-\).

**2. Spectral crossing.** At \((z_-,z_-)\), the in-phase and out-of-phase perturbations decouple into \(A\) and \(A-2d\operatorname{Id}\). The latter has eigenvalue zero precisely when \(d=\lambda_+/2=d_*\); its other eigenvalue is negative. The in-phase sector has one positive and one negative eigenvalue at every \(d\). Thus exactly one simple, antisymmetric zero eigenvalue crosses as \(d\) varies, with negative derivative \(-2\), while no other eigenvalue is zero.

**3. Exact odd/even reduction.** Write \(u=(z_1+z_2)/2\), \(v=(z_1-z_2)/2\). Define a symmetric bilinear mapping
\[
Q((x,r),(y,s))=\begin{pmatrix}-\frac32xy+\frac{77}{4}(xs+ry)\\-20(xs+ry)\end{pmatrix}.
\]
Because \(F\) is quadratic, its two-patch equations become *exactly*
\[
\dot u=F(u)+Q(v,v),\qquad
\dot v=(DF(u)-2d\operatorname{Id})v.
\]
Patch exchange acts as \(v\mapsto-v\). Take the right and left eigenvectors of \(A\) associated with \(\lambda_+\), normalized by \(e_1=1\) and \(\ell e=1\):
\[
e=\begin{pmatrix}1\\(\sqrt{26689}-137)/154\end{pmatrix},\qquad
\ell=\begin{pmatrix}\frac12+\frac{137\sqrt{26689}}{53378}&\frac{77\sqrt{26689}}{26689}\end{pmatrix}.
\]
As \(\det A\ne0\), the mean equation \(F(u)+Q(v,v)=0\) uniquely determines \(u\) as a smooth even function of \(v\) near \((z_-,0)\). The simple eigenvalue of \(DF(u)-2d\operatorname{Id}\) permits a one-dimensional odd Lyapunov–Schmidt reduction of the difference equation. Parameterize the difference by \(v=t e+O(t^3)\) (its first coordinate is \(t\)), and obtain
\[
u=z_-+t^2h+O(t^4),\qquad h=-A^{-1}Q(e,e).
\]
The order-\(t^3\) solvability condition in the difference equation reads
\[
\eta=\ell\,[2Q(h,e)],\qquad 2(d-d_*)=\eta t^2+O(t^4).
\]
The exact calculation yields the \(\eta\) displayed in the Finding. To prove its sign without decimals, use \(\sqrt{26689}<164\):
\[
\eta<-\frac{166845}{52}+\frac{26656035\cdot164}{1387828}
=-\frac{81336465}{1387828}<0.
\]
The nonzero \(\eta\), together with the transverse parameter derivative \(-2\), proves the asserted unique local pitchfork (precisely two exchange-related branches for \(d<d_*\) and none above). Local positivity follows from \(z_->0\) and \(1-(z_-)_1-(z_-)_2=20/21>0\). Inverting the quadratic amplitude law proves the asserted infection difference.

**4. Stability along the asymmetric branches.** The scalar eigenvalue in the antisymmetric center direction has the reduced expansion \(-2(d-d_*)+\eta t^2+O(t^4)\) in the equilibrium equation. Its derivative along a nontrivial branch is \(2\eta t^2+O(t^4)<0\). One positive in-phase eigenvalue tends to \(\lambda_+>0\); the remaining three infection-sector eigenvalues tend to strictly negative numbers. Two further demographic eigenvalues are negative. Therefore each nearby asymmetric equilibrium has exactly one unstable eigenvalue. At the synchronized state the sign of \(\lambda_+-2d\) supplies the stated exchange of the unstable dimension. At \(d=d_*\), the critical state is nonhyperbolic; no assertion of its nonlinear asymptotic stability is required.

## Verification

Run `python verify.py` with SymPy. It symbolically verifies the two one-patch endemic points, the exact Jacobian, eigenvector normalizations, polarization identities, critical spectral factorization, cubic solvability coefficient and strict negative sign, and positivity of the reference state. Additional numerical root solves near \(d_*\) yield two exchanged positive branches and Jacobian spectra with one unstable eigenvalue, but these numerical checks are diagnostics; the infinite local-branch and stability conclusions follow from the analytical reductions above.

## Relationship to prior work

Calvo, Hernández, Porter, and Sánchez (2019), *A two-patch epidemic model with nonlinear reinfection*, introduce the two-patch nonlinear reinfection framework and show numerically that several feasible endemic equilibria and multiple attractors can coexist, including their Example 4.7. This note does **not** claim novelty for multiple equilibria, bistability, or migration effects in general. Calvo and coauthors (2024), *Stochastic two-patch epidemic model with nonlinear recidivism*, provide the explicit deterministic balance equations used here before developing stochastic approximations. Knipl, Pilarczyk, and Röst (2015), *Rich bifurcation structure in a two-patch vaccination model*, analyze different vaccinated-population reactions and demonstrate broader two-patch bifurcation complexity; those general phenomena do not determine the critical value or the cubic coefficient of the nonlinear reinfection mechanism here. The new local statement gives an exact threshold, an exact orientation coefficient, and a Morse-index classification for a specific lower endemic state of the reinfection model.

## Limitations

The theorem concerns one explicit rational choice of biological rates and a neighborhood of one synchronized lower endemic state. It neither counts all positive equilibria at a given migration rate nor establishes global attraction, persistence, or intervention outcomes. The two emergent asymmetric equilibria are saddles, not new stable endemic attractors. No stochastic distributional statement follows from the deterministic analysis. The mathematical originality assessment is based on the accessible cited material and search, not on a guarantee against unindexed equivalent prior results.

## References

1. J. G. Calvo, A. Hernández, M. A. Porter, F. Sánchez, *A two-patch epidemic model with nonlinear reinfection*, arXiv:1907.08887, first posted 2019-07-21. https://arxiv.org/abs/1907.08887
2. J. G. Calvo, M. I. Simoy, J. P. Aparicio, J. E. Chacón, F. Sánchez, *Stochastic two-patch epidemic model with nonlinear recidivism*, arXiv:2405.10998v1, first posted 2024-05-16; especially Section 2, equations (2.1)–(2.3). https://arxiv.org/html/2405.10998v1
3. D. Knipl, P. Pilarczyk, G. Röst, *Rich bifurcation structure in a two-patch vaccination model*, 2015. https://discovery.ucl.ac.uk/id/eprint/1473750/1/99393.pdf
