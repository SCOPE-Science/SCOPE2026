# A quarantine atom and unequal complete-transmission exponents on an epidemic star

## Finding

**Theorem (matched single-contact dynamics, different epidemic extremes).** Fix an integer \(k\ge2\) and positive constants \(a,b,\lambda,\mu\). A single infectious hub in a \(k\)-leaf star recovers after an independent \(\operatorname{Exp}(\mu)\) time; each leaf is initially susceptible and has no other infectious contact. There are two contact mechanisms:

* **Shared-hub switching (NI):** the hub alternates independently of disease between inactive and active, at off-to-on rate \(a\) and on-to-off rate \(b\); every leaf is permanently available.
* **Independent-link switching (LI):** each hub–leaf link alternates independently with exactly the same two-state transition rates; the hub is permanently available.

All switching clocks start in their stationary distribution and continue independently of infection and recovery. Transmission on an active contact occurs at rate \(\lambda\) per susceptible leaf, and no other transmission is possible. Write \(X_k\), respectively \(Y_k\), for the number of leaves infected before hub recovery in NI and LI. Each individual edge has the **same entire temporal availability law** under both mechanisms, and \(\mathbb E X_k=\mathbb E Y_k\), but the joint extremes differ sharply.

Set
\[
\pi=\frac a{a+b},\quad d=\frac{b\mu}{(a+b)(a+\mu)},\quad w=1-d,
\quad r=\frac{\mu(a+b+\mu)}{a+\mu}.
\]
Define
\[
\rho=\frac{a+b+\lambda-\sqrt{(a+b+\lambda)^2-4a\lambda}}2,
\quad R=\frac{a+b+\lambda+\sqrt{(a+b+\lambda)^2-4a\lambda}}2,
\quad c=\frac{R-\lambda\pi}{R-\rho}.
\]
All parameters \(d,w,\rho,R,c\) satisfy \(0<d,w,c<1\) and \(0<\rho<R\). Then
\[
\begin{aligned}
\Pr(X_k=0)&=d+\frac{wr}{r+k\lambda}\longrightarrow d>0,\\
\Pr(Y_k=0)&\sim\frac{\mu}{\lambda\pi}\,k^{-1},\\
\Pr(X_k=k)&=w\frac{\Gamma(1+r/\lambda)\Gamma(k+1)}{\Gamma(k+1+r/\lambda)}
\sim w\Gamma(1+r/\lambda)k^{-r/\lambda},\\
\Pr(Y_k=k)&\sim c^{-\mu/\rho}\Gamma(1+\mu/\rho)k^{-\mu/\rho}.
\end{aligned}
\]
The two complete-transmission exponents are **strictly separated**:
\[
\frac r\lambda<\frac\mu\rho.
\]
Consequently, \(\Pr(X_k=k)/\Pr(Y_k=k)\) diverges polynomially as \(k\to\infty\), although expected transmissions agree. For every finite \(k\ge2\), NI has strictly greater probabilities of both no secondary infections and all \(k\) secondary infections; its offspring count dominates LI in convex order. The latter generic convex-order effect is **not claimed as original**; the stated exact atom and unequal power-law exponents are the contribution here.

## Assumptions and scope

This is the full stochastic finite-star **SIR final-size law seeded at the hub**, not an SIS lifetime or an epidemic threshold. Infection of a leaf has no effect on the contact clocks or hub recovery, and leaves cannot infect each other. We compare *hub-only* quarantine with independent switching of its links; this isolates the common-source contact mechanism from the more general all-node switching model. The theorem assumes strictly positive switching, recovery and transmission rates and stationary initial activity. Nothing is claimed for non-exponential holding times, a nonstationary initialization, multiple infectious seeds or an arbitrary graph. For the limit, \(k\to\infty\) with the four positive rates held fixed.

## Proof

**1. Shared contact and stopped active occupation.** Let \(T\sim\operatorname{Exp}(\mu)\) be hub recovery and \(A_T=\int_0^T\mathbf1_{\{H_t=\mathrm{on}\}}dt\). The probability the hub begins off and recovers before activating is exactly \(d=\frac b{a+b}\frac\mu{a+\mu}\). Starting on, first-step conditioning on a competing recovery, deactivation and Laplace-killing clock yields the Laplace transform \(r/(r+s)\) for \(A_T\), where \(r=\mu+b\mu/(a+\mu)\). Starting off, either recovery precedes activation, or the process restarts on; therefore
\[
\mathbb E e^{-s A_T}=d+w\frac r{r+s},\qquad s\ge0.
\]
Thus \(A_T\) has an atom of mass \(d\) at zero and, with mass \(w\), has exponential density \(r e^{-r u}\,du\) on \(u>0\). Conditional on \(A_T=u\), infection events on the \(k\) leaves are independent, each with probability \(1-e^{-\lambda u}\). Hence
\[
\Pr(X_k=k)=w\int_0^\infty r e^{-r u}(1-e^{-\lambda u})^k du
=w\frac r\lambda B(r/\lambda,k+1),
\]
which is the gamma expression in the theorem. Similarly \(\Pr(X_k=0)=\mathbb E e^{-k\lambda A_T}=d+wr/(r+k\lambda)\). Gamma-ratio asymptotics prove its complete-transmission exponent and prefactor.

**2. Independent links and a spectral survival kernel.** Condition on the *shared* recovery time \(T=t\). On one link, the no-transmission probability is
\[
u(t)=\begin{pmatrix}1-\pi&\pi\end{pmatrix}
\exp\!\left[t\begin{pmatrix}-a&a\\b&-b-\lambda\end{pmatrix}\right]
\begin{pmatrix}1\\1\end{pmatrix}.
\]
The killed two-state generator has eigenvalues \(-\rho,-R\). Initial value \(\nu(0)=1\) and derivative \(\nu'(0)=-\lambda\pi\) give
\[
\nu(t)=c e^{-\rho t}+(1-c)e^{-Rt}.
\]
For the characteristic polynomial \(q(x)=x^2-(a+b+\lambda)x+a\lambda\), one computes \(q(\lambda\pi)=-\lambda^2ab/(a+b)^2<0\). Thus \(\rho<\lambda\pi<R\), proving \(0<c<1\) and \(\rho>0\). Conditioning on recovery time and independent link clocks,
\[
\Pr(Y_k=k)=\int_0^\infty\mu e^{-\mu t}(1-\nu(t))^k dt,\qquad
\Pr(Y_k=0)=\int_0^\infty\mu e^{-\mu t}\nu(t)^k dt.
\]
For all-infected probability set \(z=kc e^{-\rho t}\), so \(t=\rho^{-1}\log(kc/z)\). After factoring \((kc)^{-\mu/\rho}\), the remaining integrand converges to \((\mu/\rho) z^{\mu/\rho-1}e^{-z}\). It is bounded by the same gamma-integrable function because \(\nu(t)\ge c e^{-\rho t}=z/k\) and \((1-\nu(t))^k\le e^{-z}\). Dominated convergence yields the prefactor \(c^{-\mu/\rho}\Gamma(1+\mu/\rho)\). For no-infection probability, \(\nu(t)=1-\lambda\pi t+O(t^2)\) as \(t\downarrow0\) and \(\nu(t)<1\) for \(t>0\). Splitting at any small fixed time and substituting \(z=kt\) gives \(k\Pr(Y_k=0)\to\mu/(\lambda\pi)\), with an exponentially small remaining integral.

**3. Strict exponent separation.** From the characteristic-polynomial calculation,
\[
\rho<\lambda\pi=\frac{\lambda a}{a+b}<\frac{\lambda(a+\mu)}{a+b+\mu}=\frac{\lambda\mu}{r}.
\]
The second strict inequality uses \(b\mu>0\). Rearranging the last inequality proves \(r/\lambda<\mu/\rho\). The complete-transmission ratio therefore diverges with power \(\mu/\rho-r/\lambda>0\).

**4. Identical marginals, strict finite extremes.** At each time the hub contact indicator in NI and any single link in LI has the same stationary two-state Markov law, hence the marginal leaf-infection probability is the same. Explicitly \(\Pr(\text{given leaf infected})=w\lambda/(r+\lambda)\), so the offspring means equal \(kw\lambda/(r+\lambda)\). For fixed \(t>0\), let \(Q_t=1-e^{-\lambda A_t}\) be the random one-leaf infection probability generated by one stationary switching path up to time \(t\). NI gives a binomial mixture \(\operatorname{Bin}(k,Q_t)\) conditional on \(T=t\); LI gives \(\operatorname{Bin}(k,\mathbb E Q_t)\). For any convex function on integer offspring counts, its binomial expectation is convex in the success parameter: its second derivative is \(k(k-1)\) times the expectation of the nonnegative second difference of that function under \(\operatorname{Bin}(k-2,p)\). Jensen's inequality thus gives convex order. Applying it to the strictly convex functions \(p^k\) and \((1-p)^k\) gives strict all/none inequalities for \(k\ge2\), because \(Q_t\) is nondegenerate for every \(t>0\). Integrate over the common recovery law.

## Verification

A standalone script `check.py` independently builds exact-rational absorbing continuous-time chains for the NI and LI processes at \(a=b=\lambda=\mu=1\), and compares their hitting probabilities with the derived formulas for \(2\le k\le5\), and for three additional non-symmetric positive-rate parameter vectors at \(k=3\). For example, at \(k=2\), NI has \(\Pr(X_2=2)=6/35\) and \(\Pr(X_2=0)=4/7\), whereas LI has \(\Pr(Y_2=2)=59/440\) and \(\Pr(Y_2=0)=47/88\). At these rates \(d=1/4\), \(r/\lambda=3/2\), \(\rho=(3-\sqrt5)/2\), and \(\mu/\rho=(3+\sqrt5)/2\). Numerical quadrature for degrees \(20,100,500,2000\) confirms the stated large-degree constants. All exact-rational and numerical tests passed. The infinity statements are proved analytically; no finite sample is used as an infinite proof. Run `python check.py` with Python 3, SymPy, NumPy and SciPy installed.

## Relationship to prior work

Moraes and Ferreira, arXiv:2610.00429v1 (30 September 2026), compare node and link intermittency in SIS/SIR spreading and study thresholds and star SIS lifetimes. Their model motivates the distinction; their reported results do not state the killed-hub occupation atom, exact all-leaf SIR probability or separated all-leaf exponents here. The present hub-only intervention is a transparent restriction, not identical to switching every node in their simulations. Giordano, Martinucci and Paraggio (2026) analyze the two-state switched Poisson process at deterministic times and long-time Gaussian limits; the matrix-exponential step is standard, and that work does not present this epidemic-specific independent-link versus common-hub all-leaf comparison or its degree-dependent exponent contrast. The standard binomial-mixture convex-order conclusion is already covered in broader epidemic heterogeneity results and is used here only as context, not as the novelty claim. The distinct asymptotic exponents and residual zero-offspring atom are the proposed new contributions. Hilton and Hall (2023) treat beta-Poisson mixtures and zero-inflated secondary-case counts, so a beta mixture or an excess-zero effect alone is not novel; they do not study this exactly matched stationary-contact switching comparison or its two all-neighbor power exponents. A related 2019 SIR edge-dropping paper distinguishes individual edge removal from common recovery but does not analyze reversible intermittent source contacts under matched edge dynamics. All literature priority statements are bounded by the accessible sources described in the review.

## Limitations

The comparison is at the one-generation outbreak of a fixed infectious hub; it does not establish that node intermittency universally increases population-level epidemic risk or changes an infinite-network SIS threshold. Its hub-only switching is a deliberate special case, and its large-degree limits keep rates fixed. Generic covariance/convex-order facts are not new. Primary historical completeness and mathematical independence have not been established by an external reviewer.

## References

1. J. T. Moraes and S. C. Ferreira, *Intermittent quarantine suppresses epidemic spreading beyond simple contact reduction*, arXiv:2610.00429v1, first public 2026-09-30. https://arxiv.org/html/2610.00429v1
2. N. Giordano, B. Martinucci and P. Paraggio, *Explicit distributions and time-changed dynamics of the two-state Markov modulated Poisson process*, Methodology and Computing in Applied Probability **28**, article 88 (2026). https://doi.org/10.1007/s11009-026-10327-1
3. F. Ball, T. Britton, K. Y. Leung and D. Sirl, *A stochastic SIR network epidemic model with preventive dropping of edges*, Journal of Mathematical Biology **78** (2019), 1875–1951. https://doi.org/10.1007/s00285-019-01329-4
4. J. Hilton and I. Hall, *A beta-Poisson model for infectious disease transmission*, medRxiv (2023). https://doi.org/10.1101/2023.03.24.23287701
5. A. Koher, H. H. K. Lentz, J. P. Gleeson and P. Hövel, *Contact-Based Model for Epidemic Spreading on Temporal Networks*, Physical Review X **9**, 031017 (2019). https://doi.org/10.1103/PhysRevX.9.031017
