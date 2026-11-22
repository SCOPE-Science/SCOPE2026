# Universal Poisson–Gaussian separation and residual anticorrelation in dilute subdivided hard-core gases

## Finding

**Theorem (one-subdivision hard-core gas).** Let \(G_n\) be any sequence of finite simple graphs with vertex set \([n]\), edge count \(m_n\), and degrees \(d_{n,v}\). Replace every edge of \(G_n\) by a two-edge path, writing \(S(G_n)\) for the resulting incidence/subdivision graph. Give **every** original and subdivision vertex the same hard-core activity \(z_n=c/n\), where \(c>0\) is fixed. Let \(A_n\) be the random set of occupied original vertices, \(K_n=|A_n|\), and \(Y_n\) the number of occupied subdivision vertices.

For every \(n\ge1\), define \(w_{n,v}=z_n(1+z_n)^{-d_{n,v}}\) and let \(Q_n\) be the product Bernoulli law with occupancy probabilities \(q_{n,v}=w_{n,v}/(1+w_{n,v})\). Then the **entire labeled original-vertex occupancy vector** obeys the graph-uniform total-variation bound
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(A_n),Q_n\bigr)
 \le \frac{c^3}{2n}\exp\!\bigl(c e^{c/2}\bigr).
\]
This bound is nonasymptotic and needs no regularity or density assumptions on the host graphs.

Suppose additionally that the empirical measure of rescaled degrees converges weakly on \([0,1]\):
\[
 \mu_n=\frac1n\sum_{v=1}^n\delta_{d_{n,v}/n}\Longrightarrow\mu,
 \qquad \beta=\frac12\int_0^1 t\,\mu(dt)>0.
\]
Put \(\lambda(c)=c\int_0^1 e^{-ct}\,\mu(dt)\) and \(p_n=z_n/(1+z_n)\). Then the degree-marked original occupation point process \(\sum_{v\in A_n}\delta_{d_{n,v}/n}\) converges weakly to a Poisson random measure with intensity \(c e^{-ct}\mu(dt)\). In particular, \(K_n\) converges to \(\operatorname{Poisson}(\lambda(c))\). Independently of that limiting Poisson measure,
\[
 \frac{Y_n-m_np_n}{\sqrt{m_np_n(1-p_n)}}\Longrightarrow N(0,1).
\]
The grand partition functions satisfy the finite-order correction
\[
 \frac{Z_{S(G_n)}(c/n)}{(1+c/n)^{m_n}}\longrightarrow e^{\lambda(c)},
\]
and the **unnormalized** cross-population covariance retains the finite nonzero limit
\[
 \operatorname{Cov}(K_n,Y_n)\longrightarrow
 -c^2\int_0^1 t e^{-ct}\,\mu(dt).
\]

For an asymptotically \(\rho n\)-regular sequence with \(\rho>0\), the rare-original mean is \(\lambda(c)=ce^{-\rho c}\), uniquely maximized at \(c=1/\rho\), with height \(1/(e\rho)\), even though the mean occupied subdivision population is of order \(n\). Thus the original-vertex response is reentrant in the inverse-size activity window. The covariance limit becomes \(-\rho c^2e^{-\rho c}\).

## Assumptions and scope

Graphs are labeled, finite, simple and otherwise arbitrary, including disconnected graphs. The graph \(S(G)\) has the original vertices of \(G\) plus one new vertex for each edge; the only edges join a new vertex to its two original endpoints. A hard-core configuration is an independent vertex set, weighted by \(z^{\text{number of occupied sites}}\). All limits have fixed \(c>0\), \(n\to\infty\); the limits are not uniform when \(c\) grows with \(n\). The Gaussian assertion requires \(\beta>0\), equivalent to quadratic-order edge count. The total-variation bound and the partition reduction do not require that assumption. The marked-Poisson convergence is weak convergence of finite point measures, not total variation on a continuum of degree marks. \(N(0,1)\) denotes a standard normal random variable.

## Proof

**1. Exact conditional reduction.** For \(A\subseteq[n]\), write \(e_n(A)\) for the number of host edges internal to \(A\), and \(I_n(A)=\sum_{v\in A}d_{n,v}-e_n(A)\) for the number of host edges incident to \(A\). The original vertices are mutually nonadjacent in \(S(G_n)\). Once their occupied subset is \(A\), exactly \(m_n-I_n(A)\) subdivision sites remain available, with no edges among them. Thus their conditional joint law is independent Bernoulli with success probability \(p_n\), and
\[
 Z_{S(G_n)}(z)=\sum_{A\subseteq[n]}z^{|A|}(1+z)^{m_n-I_n(A)}
 =(1+z)^{m_n}\sum_{A\subseteq[n]}\Bigl(\prod_{v\in A}z(1+z)^{-d_{n,v}}\Bigr)(1+z)^{e_n(A)}.
\]
In particular, the original occupation law is a tilt of \(Q_n\) by \(F_n(A)=(1+z_n)^{e_n(A)}\):
\[
 \mathbb P(A_n=A)=Q_n(A)\frac{F_n(A)}{\mathbb E_{Q_n}F_n}.
\]

**2. Quantitative independence.** Let \(K=|A|\) under \(Q_n\). Since \(e_n(A)\le\min\{\binom K2,nK/2\}\),
\[
 0\le F_n(A)-1\le z_ne_n(A)F_n(A)
 \le\frac{c}{2n}K(K-1)e^{cK/2}.
\]
Each independent Bernoulli parameter of \(Q_n\) is at most \(c/n\). Expanding \(K(K-1)\) into ordered pairs and bounding the remaining Bernoulli exponential moments gives
\[
 \mathbb E_{Q_n}[K(K-1)e^{cK/2}]
 \le c^2\exp\!\bigl(c e^{c/2}\bigr).
\]
For any \(F\ge1\), the total-variation distance between \(Q\) and its \(F\)-tilt is at most \(\mathbb E_Q(F-1)\), by the triangle inequality and \(\mathbb E_QF\ge1\). Substituting proves the displayed bound. The same exponential-moment estimate yields uniformly bounded moments of every fixed order for \(K_n\).

**3. Marked Poisson and partition correction.** Uniformly over vertices, \(nq_{n,v}=c\exp(-c d_{n,v}/n)+O_c(1/n)\), and \(\sum_vq_{n,v}^2\le c^2/n\). Independent Bernoulli points under \(Q_n\) therefore have the same limiting Laplace functional as a Poisson random measure of intensity \(ce^{-ct}\mu(dt)\). Step 2 transfers this law to \(A_n\). Further,
\[
 \frac{Z_{S(G_n)}(z_n)}{(1+z_n)^{m_n}}
 =\prod_{v=1}^n(1+w_{n,v})\,\mathbb E_{Q_n}F_n.
\]
Here \(\mathbb E_{Q_n}F_n=1+O_c(n^{-1})\), \(\sum_vw_{n,v}^2=O_c(n^{-1})\), and \(\sum_vw_{n,v}\to\lambda(c)\). Taking logarithms proves the partition limit.

**4. Gaussian bulk and independence.** Conditional on \(A_n=A\),
\[
 Y_n\sim\operatorname{Binomial}(m_n-I_n(A),p_n).
\]
The Poisson convergence and uniform exponential moments imply \(K_n=O_{\mathbb P}(1)\); since \(I_n(A_n)\le nK_n\), the conditional midpoint count differs from a binomial with \(m_n\) trials by at most \(O_{\mathbb P}(n)\) available trials. Its conditional mean shifts by at most \(p_n nK_n=O_{\mathbb P}(1)\) and its variance has relative error \(O_{\mathbb P}(1/n)\). As \(m_np_n\sim\beta cn\to\infty\), the binomial central limit theorem applies uniformly on each event \(K_n\le L\), for fixed \(L\). Sending \(L\to\infty\) establishes the joint independent normal/marked-Poisson limit.

**5. Residual covariance and reentrance.** The conditional mean of \(Y_n\) is \(p_n(m_n-I_n(A_n))\), so
\[
 \operatorname{Cov}(K_n,Y_n)
 =-np_n\operatorname{Cov}\!\left(K_n,\sum_{v\in A_n}\frac{d_{n,v}}n\right)
 +p_n\operatorname{Cov}(K_n,e_n(A_n)).
\]
The second term tends to zero because \(e_n(A_n)\le K_n^2/2\), \(p_n\to0\), and the occupation counts have uniform high moments. The first covariance converges to the covariance of total count and sum of marks of the Poisson random measure, namely \(c\int t e^{-ct}\mu(dt)\). Since \(np_n\to c\), the claimed finite negative limit follows. For \(\mu=\delta_\rho\), differentiation of \(ce^{-\rho c}\) gives the unique stated maximum, and convergence of expectations follows from uniform moments. This is an asymptotic activity-window assertion, not a claim of a unique extremum at each finite \(n\).

## Verification

The independent Python 3 checker `verify_subdivision_gas.py` builds the subdivided incidence graph explicitly, enumerates its independent sets without using the conditional formula, and compares exact rational partition weights for host complete graphs, cycles and stars of orders three through five. It separately checks the algebraic conditional reduction for every original subset and the explicit total-variation inequality over host sizes three through eight and three rational fugacity scales. It reports `ALL_NEW_CHECKS_PASSED 590` when successful. Further independent analytic checks of the complete-host family at orders 15, 30, 60, 120 and 240 show mean original occupation and cross covariance approaching \(e^{-1}\) and \(-e^{-1}\), respectively, for \(c=1\). These finite checks are corroboration only; Steps 1–5 give the infinite-graph-sequence proof.

## Relationship to prior work

Scott and Sokal [1] develop the hard-core partition function and general repulsive-gas identities; their definition and polynomial framework encompass the present model, but the inspected definitions, general identities, and Section 3 examples do not give the subdivision-conditioned low-activity Poisson–Gaussian law or the residual cross-population covariance. Barbour and Brown [2] establish general Stein–Chen point-process approximations and analyze a continuous hard-core gas on a geometric torus. Those general tools are related to the Poisson part, but their specific result neither identifies the effective degree-profile intensity of an edge-subdivision model nor computes its independent Gaussian midpoint fluctuations. A previously documented exact polynomial for independent *dominating* sets of subdivided complete bipartite graphs [3] uses the same subdivision operation but counts only maximal independent sets, so it cannot supply the full hard-core Gibbs law or its dilute scaling without additional work. No publication-priority guarantee is inferred from unsuccessful searches.

## Limitations

The statement is about the equilibrium grand-canonical hard-core measure, not Kawasaki/Glauber dynamics, irreversible deposition, or interacting quantum particles. There is no thermodynamic-limit phase-transition claim. The normal limit requires quadratic-order host edge density and excludes the zero-density case. The explicit total-variation constant is uniform but not claimed sharp. The independence is at Gaussian scale: the raw count covariance can have a nonzero limit. Bibliographic overlap may exist in unindexed work or as a specialization of an uninspected general theorem; priority remains provisional, and independent review has not been carried out.

## References

[1] A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, arXiv:cond-mat/0309352, initially public 2003-09-15; https://arxiv.org/abs/cond-mat/0309352. Accessible manuscript: https://people.maths.ox.ac.uk/scott/Papers/lovasz.pdf.

[2] A. D. Barbour and T. C. Brown, *Stein's method and point process approximation*, Stochastic Processes and their Applications **43** (1992), 9–31; https://user.math.uzh.ch/barbour/pub/Barbour/BBrown_PointProcess.pdf. In particular Theorems 1.1 and 2.4 and the continuous torus example.

[3] *Independent domination of subdivided bicliques: exact polynomials and multiplication-table gaps*, research record, 2026-11-02; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-independent-domination-of-subdivided-bicliques-exact-polynomials--d94ae62f6ccd. Distinct independent-domination rather than Gibbs-occupation observable.
