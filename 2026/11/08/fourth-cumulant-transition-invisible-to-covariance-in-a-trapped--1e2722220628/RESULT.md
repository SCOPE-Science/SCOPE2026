# Fourth-cumulant transition invisible to covariance in a trapped Markov-speed run-and-tumble particle

## Finding
For a one-dimensional particle with harmonic relaxation, independent thermal diffusion, and a direction that is independently redrawn at each Poisson tumble, suppose its two possible propulsion *speeds* retain tunable one-step memory. The entire stationary active-velocity autocovariance, and hence the stationary position variance, are independent of speed memory. Nevertheless the stationary position fourth cumulant is strictly increasing with the speed-memory parameter and can cross zero exactly once.

Precisely, use the definitions below and write
\[
s_0=\frac{a^2+b^2}{2},\qquad c=\left(\frac{b^2-a^2}{b^2+a^2}\right)^2,\qquad \alpha=\frac{\gamma}{\mu}.
\]
Then, for every \(\mu,\gamma>0\), \(a,b>0\) with \(a\ne b\), \(D\ge0\), and \(-1\le\rho<1\), the unique stationary position law satisfies
\[
\operatorname{Var}(X)=\frac{s_0}{\mu(\mu+\gamma)}+\frac D\mu,
\qquad
\kappa_4(X)=\frac{6s_0^2}{\mu^4(\alpha+1)^2(\alpha+3)}\left(\frac{c(\alpha+1)}{2+\alpha(1-\rho)}-1\right).
\]
Its propulsion autocovariance is \(\operatorname{Cov}(V_t,V_{t+u})=s_0e^{-\gamma|u|}\). These two second-order observables are constant along the entire memory family, but \(\kappa_4(X)\) increases strictly with \(\rho\). A sign change within \(-1\le\rho<1\) exists if and only if \(c(\alpha+1)>2\), and then its unique threshold is
\[
\rho_c=1-\frac{c(\alpha+1)-2}{\alpha}=\frac{\alpha+2-c(\alpha+1)}{\alpha}\in(0,1).
\]
The fourth cumulant is negative below \(\rho_c\), zero at \(\rho_c\), and positive above it. If \(c(\alpha+1)\le2\), it is strictly negative for every allowed \(\rho\). Thus fixed covariance and fixed variance do not determine even the *sign* of the trapped stationary fourth cumulant.

## Assumptions and scope
Let \(N_t\) be a rate-\(\gamma\) Poisson process and let the pair of marks \((S_t,Z_t)\in\{-1,1\}^2\) be constant between its events. At an event, draw the new heading \(S'\) uniformly from \(\{-1,1\}\), independently of all preceding data. Conditional on the old speed label \(Z=z\), draw the new label according to
\[
\Pr(Z'=z'\mid Z=z)=\frac{1+\rho zz'}{2},\qquad z,z'\in\{-1,1\},\quad -1\le\rho<1.
\]
Conditionally, \(S'\) and \(Z'\) are independent. The speed is \(R(-1)=a\), \(R(1)=b\), with \(a,b>0\) and \(a\ne b\), and \(V_t=S_tR(Z_t)\). For a Brownian motion \(B\) independent of the Poisson process and marks, consider
\[
dX_t=(-\mu X_t+V_t)\,dt+\sqrt{2D}\,dB_t,\qquad \mu,\gamma>0,\quad D\ge0.
\]
Both signs and both speed labels have stationary probability \(1/2\), independently. At \(\rho=-1\), every tumble switches speed; the continuous-time four-state chain is still irreducible. At \(\rho=1\), speed never changes and the stationary law is not uniquely selected by dynamics; that endpoint is excluded from the asserted uniqueness and transition theorem. Cumulants are centered, with \(\kappa_4(X)=\mathbb E[(X-\mathbb EX)^4]-3\operatorname{Var}(X)^2\). The result is stationary, one-dimensional, and non-inertial; it does not classify the full position density or higher cumulants.

## Proof
**Stationary state and second-order invisibility.** The finite-state process \((S,Z)\) has the unique invariant uniform distribution on four marks for \(\rho<1\). Bounded propulsion and \(\mu>0\) give a unique stationary stochastic convolution
\[
X_t=\int_{-\infty}^t e^{-\mu(t-u)}V_u\,du
+\sqrt{2D}\int_{-\infty}^t e^{-\mu(t-u)}\,dB_u.
\]
The second term is a centered independent Gaussian with variance \(D/\mu\). The first is centered and bounded. If there is no tumble between two instants separated by \(|u|\), the heading persists and \(V_tV_{t+u}=R(Z_t)^2\). If at least one tumble occurs, the newly redrawn heading is independent and centered, so that conditional product has expectation zero. Therefore \(\mathbb E[V_tV_{t+u}]=s_0e^{-\gamma|u|}\), independently of \(\rho\). Integrating against the two harmonic kernels, or using the moment equations below, yields the asserted variance.

**Finite closed moment system.** Write \(s_1=(b^2-a^2)/2\), so \(R^2=s_0+s_1Z\) and \(\mathbb E R^4=s_0^2+s_1^2\). Initially set \(D=0\). For the stationary joint generator, jumps kill every observable containing one heading factor \(S\), while they send \(Z\) to conditional mean \(\rho Z\). Thus, on the respective polynomial observables, the exact stationary generator identities give
\[
Y:=\mathbb E[XSR]=\frac{s_0}{\mu+\gamma},\quad
Y_Z:=\mathbb E[XSRZ]=\frac{s_1}{\mu+\gamma},\quad
M:=\mathbb E[X^2]=\frac{Y}{\mu},
\]
\[
F:=\mathbb E[X^2Z]=\frac{2s_1}{(\mu+\gamma)[2\mu+\gamma(1-\rho)]},\qquad
C:=\mathbb E[XSR^3]=\frac{s_0^2+s_1^2}{\mu+\gamma},
\]
\[
Q:=\mathbb E[X^2R^2]
=\frac{2C+\gamma(s_0M+\rho s_1F)}{2\mu+\gamma},
\qquad
H:=\mathbb E[X^3SR]=\frac{3Q}{3\mu+\gamma},
\qquad
\mathbb E[X^4]=\frac{H}{\mu}.
\]
These relations follow successively from the generator acting on \(XSR\), \(XSRZ\), \(X^2\), \(X^2Z\), \(XSR^3\), \(X^2R^2\), \(X^3SR\), and \(X^4\), respectively. For instance, a tumble transforms \(R^2\) into conditional mean \(s_0+\rho s_1Z\), explaining the otherwise invisible speed-memory term in \(Q\). Reflection symmetry gives \(\mathbb EX=\mathbb EX^3=0\).

Insert the displayed rational values into \(\mathbb E[X^4]-3M^2\) and simplify. The result is precisely the boxed fourth-cumulant expression stated under Finding. Restoring \(D\ge0\), the independent thermal Ornstein--Uhlenbeck term adds variance \(D/\mu\) but has zero fourth cumulant, so the formula for \(\kappa_4\) remains unchanged.

**Sharp transition.** Because \(a\ne b\), \(0<c<1\). The sole \(\rho\)-dependent factor \(c(\alpha+1)/[2+\alpha(1-\rho)]\) has strictly positive derivative \(c\alpha(\alpha+1)/[2+\alpha(1-\rho)]^2\). At \(\rho=0\), this factor is \(c(\alpha+1)/(2+\alpha)<1\); for \(\rho<0\) it is smaller still. As \(\rho\uparrow1\), the factor tends to \(c(\alpha+1)/2\). Hence it passes through one exactly when \(c(\alpha+1)>2\), at the unique stated \(\rho_c\). If equality holds, the limiting cumulant reaches zero only at the excluded nonergodic endpoint, never for \(\rho<1\). These statements establish all strict sign and boundary assertions.

**Exact witness.** Take \(\mu=1\), \(\gamma=4\), \(a=1\), \(b=3\) and any \(D\ge0\). Then \(s_0=5\), \(c=16/25\), and the sign-changing speed-memory threshold is \(\rho_c=7/10\). In particular, the fourth cumulant at \(\rho=9/10\) is exactly \(2/7>0\), while at \(\rho=0\) it is strictly negative. Throughout, \(\operatorname{Var}(X)=1+D\) and \(\mathbb E[V_tV_{t+u}]=5e^{-4|u|}\).

## Verification
The included standalone `verify.py` constructs the full four-state jump transition matrix, solves the stationary polynomial-moment equations up to degree four over exact rational arithmetic, and independently checks both moment identities against the closed formulas. It passed 1,347 exact assertions over combinations of two trap strengths, three tumble rates, two choices of first speed, two choices of second speed, seven memory settings, and two thermal noise settings, as well as the explicit rational threshold witness. The test contains a formal \(\rho=1\) limit beyond the claimed ergodic domain; this is only an algebraic consistency test and not evidence of uniqueness there. Executing `python verify.py` requires SymPy. The proof above, not the finite parameter grid, establishes the unrestricted parameter assertions.

## Relationship to prior work
Guéneau, Majumdar and Schehr (2026) give an exact stationary distribution and all moments for a generalized harmonically trapped particle whose velocity is freshly and **independently** sampled at every tumble; their finite-velocity mixture and Dirichlet representation cover our \(\rho=0\) marginal-velocity instance, not temporal dependence between successive speed labels. Their Appendix B analyzes moments under that independent-redraw assumption. The present transition requires retaining a nontrivial speed-label Markov eigenmode, which is absent from that independent representation. Frydel (2023), Sun, Ye and Podgornik (2024/2025), Sun, Ye and Chen (2026), and Sevilla and Meléndez Mora (2026) analyze trapped particles with fixed propulsion magnitude, finite tumble duration or thermal convolution; none of their inspected model equations includes a speed-label transition kernel with nonzero \(\rho\). Their moment/generator methods are relevant antecedents, and the independent-Gaussian-convolution observation is not claimed as new.

The contribution is only the exact separation between equal two-time propulsion statistics and memory-sensitive fourth stationary cumulants, including its sharp, realizable sign boundary for this specific minimal Markov-speed model. General finite-state generator moment calculation is a standard method and is not claimed as novel.

## Limitations
The four-state speed-memory model is a controlled theoretical extension, not a measured biological mechanism. The transition requires sufficient speed heterogeneity and a sufficiently large tumble-to-relaxation ratio, and its limiting \(\rho=1\) process is nonergodic. Fixed covariance does not mean equality of full stationary distributions or higher-order correlations. The fourth-cumulant sign does not by itself determine unimodality or entropy production. Earlier work on general Markov-modulated colored noise could potentially subsume the computation; no priority or independent validation is certified here.

## References
1. M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (first public 2026-02-09), https://arxiv.org/abs/2602.08436.
2. D. Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, arXiv:2309.12537 (2023), https://arxiv.org/abs/2309.12537.
3. A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578 (2024), https://arxiv.org/abs/2409.00578.
4. A. Sun, F. Ye, J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961 (2026), https://arxiv.org/abs/2610.24961.
5. F. J. Sevilla, J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781 (2026), https://arxiv.org/abs/2608.21781.
6. *Dynamics and escape of active particles in a harmonic trap*, Physical Review Research 2, 013003 (2020), https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.013003 (background on non-Gaussian forces with matched autocorrelation).
