# A logarithmic importation window and random infection exponents at the critical SIS threshold

## Finding
For each integer \(n\ge2\), consider a continuous-time susceptible–infected–susceptible (SIS) process on the complete graph on \(n\) vertices. Each infected vertex recovers at rate one; an uninfected vertex is infected by each infected neighbor at rate \(1/n\) and has an additional independent spontaneous infection rate \(\alpha_n/n\), where \(\alpha_n>0\). Let \(K_n\) be the number infected under its unique stationary law, and set
\[
Y_n=\frac{\log(1+K_n)}{\log n}.
\]
If \(\alpha_n\log n\to c\in[0,\infty)\), then \(Y_n\) converges in distribution to the random variable with cumulative distribution function
\[
F_c(y)=\begin{cases}
0,&y<0,\\
e^{c(y-1/2)},&0\le y<1/2,\\
1,&y\ge1/2.
\end{cases}
\]
In particular, \(\Pr(K_n=0)\to e^{-c/2}\). For \(c>0\), the limit has an atom of mass \(e^{-c/2}\) at zero and continuous density \(c e^{c(y-1/2)}\) on \((0,1/2)\). For \(c=0\), it is the point mass at zero. In the complementary vanishing-importation regime \(\alpha_n\to0\) and \(\alpha_n\log n\to\infty\), one has \(Y_n\to1/2\) in probability.

The exact finite-population stationary law, included to make the theorem reproducible, is
\[
\Pr(K_n=k)=\frac{1}{Z_n}\binom nk\frac{(\alpha_n)_k}{n^k},\qquad
Z_n=\sum_{j=0}^{n}\binom nj\frac{(\alpha_n)_j}{n^j},\qquad 0\le k\le n,
\]
where \((a)_0=1\) and \((a)_k=\prod_{j=0}^{k-1}(a+j)\) for positive \(k\). This finite formula itself is a known instance of the stationary birth–death law; the finding is the singular logarithmic-source asymptotic and its complete limiting distribution.

## Assumptions and scope
All contact and spontaneous-infection clocks and recovery clocks are independent exponential clocks. The number of vertices tends to infinity through integers. Recovery is rate one, pairwise contact rate is \(1/n\), and per-vertex importation is \(\alpha_n/n\). The system is considered at its stationary distribution, not at a finite observation time. For the finite-\(c\) assertion only \(\alpha_n>0\) and \(\alpha_n\log n\to c\) are assumed; for the last assertion additionally \(\alpha_n\to0\). All logarithms are natural. The choice \(\alpha_n=c/\log n\) for fixed \(c>0\) is the sharp nondegenerate importation window.

## Proof
**Stationary weights.** If \(k\) sites are infected, the count process has birth rate \(b_k=(n-k)(k+\alpha_n)/n\) for \(k<n\) and death rate \(d_k=k\) for \(k>0\). Positive birth and death rates yield irreducibility. Detailed balance gives \(\pi_{k+1}/\pi_k=b_k/d_{k+1}\), proving the displayed finite stationary law. Write \(a=\alpha_n\),
\[
q_{n,k}=\frac{(a)_k}{k!},\qquad R_{n,k}=\prod_{j=0}^{k-1}\left(1-\frac jn\right),\qquad Z_n=\sum_{k=0}^{n}q_{n,k}R_{n,k}.
\]
Notice \(0\le R_{n,k}\le1\), and for \(k=o(\sqrt n)\), \(R_{n,k}=1-o(1)\) uniformly over such initial ranges. The useful *exact* rising-factorial summation identity is
\[
\sum_{k=0}^{m}q_{n,k}=\frac{(a+1)_m}{m!}=\frac{\Gamma(m+a+1)}{\Gamma(1+a)\Gamma(m+1)}.
\tag{1}
\]
It follows by induction: the difference between the right sides at indices \(m\) and \(m-1\) is \((a)_m/m!\). If \(a\to0\), \(m\to\infty\), and \(a\log m\to v\in[0,\infty)\), the right side tends to \(e^v\), using the standard uniform gamma-ratio estimate \(\Gamma(m+a+1)/\Gamma(m+1)=m^a(1+O(a/m))\) for \(0<a\le1\).

**Critical-window normalization.** Assume \(a\log n\to c<\infty\), hence \(a\to0\). Fix \(0<\delta<1/2\), and put \(m_-=\lfloor n^{1/2-\delta}\rfloor\), \(m_+=\lceil n^{1/2+\delta}\rceil\). Since \(\log R_{n,k}\ge-2k^2/n\) for \(k\le m_-\) and sufficiently large \(n\), the initial sum is bounded below by \((1-o(1))\sum_{k=0}^{m_-}q_{n,k}\to e^{c(1/2-\delta)}\). For the upper bound, split at \(m_+\). Since \(a\le1\), \(q_{n,k}\le1\), while
\[
R_{n,k}\le \exp\left(-\frac{k(k-1)}{2n}\right),
\]
the tail beyond \(m_+\) is at most \(n\exp[-(m_+^2-m_+)/(2n)]=o(1)\). The remaining sum is at most \(\sum_{k=0}^{m_+}q_{n,k}\to e^{c(1/2+\delta)}\). Send \(\delta\downarrow0\) to obtain
\[
Z_n\longrightarrow e^{c/2}.
\tag{2}
\]
For every fixed \(0<y<1/2\), \(R_{n,k}=1-o(1)\) uniformly for \(k\le\lfloor n^y\rfloor\), and (1) gives
\[
\sum_{k=0}^{\lfloor n^y\rfloor}q_{n,k}R_{n,k}\longrightarrow e^{cy}.
\tag{3}
\]
At \(y=0\), the stationary zero-state probability is \(1/Z_n\to e^{-c/2}\). Thus (2) and (3) yield the claimed cumulative distribution below \(1/2\). Above \(1/2\), the Gaussian tail bound above proves the limiting cumulative distribution equals one. To check there is no extra atom *at* \(1/2\), note for \(a\le1\) that \(q_{n,k}\le C a k^{a-1}\); summing \(q_{n,k}e^{-k(k-1)/(2n)}\) over \(k>\sqrt n\) gives \(O(a n^{a/2})=o(1)\) in the finite-\(c\) regime. Hence \(F_c(1/2)=1\), and convergence in distribution follows.

**More slowly vanishing importation.** Suppose \(a\to0\) while \(a\log n\to\infty\). For \(y<1/2\), choose \(\delta>0\) with \(y<1/2-\delta\). Then (1) bounds the cumulative numerator by \(n^{ay}(1+o(1))/\Gamma(1+a)\), whereas the initial-range lower bound on \(Z_n\) is \((1-o(1))n^{a(1/2-\delta)}/\Gamma(1+a)\). Their ratio tends to zero. For \(y>1/2\), the above Gaussian tail at \(n^y\) tends to zero; since \(Z_n\ge1\), its stationary probability tends to zero. Therefore \(Y_n\to1/2\) in probability.

## Verification
`VERIFY.py` uses only the Python standard library. It checks the finite stationary count law by independently summing explicit full-configuration weights, and checks detailed balance on every individual single-site infection/recovery edge for \(2\le n\le7\), at three rational importation strengths. It also verifies the exact rising-factorial partial-sum identity and compares finite critical-window probabilities with the limiting formula. The finite calculations are not offered as proof of the infinite-population limit; the proof is the analytic argument above. Run: `python VERIFY.py`.

## Relationship to prior work
Van Mieghem and Cator (2012) obtained the finite complete-graph stationary \(\varepsilon\)-SIS birth–death law, equivalent to the finite formula above after setting their \(\beta=1/n\), \(\delta=1\), and \(\varepsilon=\alpha_n/n\); that formula is explicitly acknowledged and not claimed as new. Cator and Van Mieghem (2013) gave exact complete-graph results for a different, extinction-preventing modified SIS process. Van Mieghem (2020) studied small spontaneous infection and a finite-size prevalence threshold. The specific simultaneous asymptotic \(\alpha_n\log n\to c\) and the limiting distribution of the *logarithmic infection-size exponent*, including its zero atom, were not established in the inspected material. The theorem does not claim the stationarity formula, the general birth–death method, or the existence of the SIS critical point as original.

## Limitations
This is a theorem for the exact finite complete-graph process in equilibrium; it is not an epidemic extinction-time estimate, transient scaling law, result for heterogeneous networks, or prevalence transition at fixed nonzero immigration. It identifies a singular stationary window and does not quantify the convergence rate. Prior exact formulas are stronger at every fixed size, but no equivalent logarithmic-size scaling statement was located in the inspected literature; historical priority should remain open to further specialist review.

## References
- P. Van Mieghem and E. Cator, “Epidemics in networks with nodal self-infection and the epidemic threshold,” *Physical Review E* **86**, 016116 (2012), first verified public release 2012-07-30, https://doi.org/10.1103/PhysRevE.86.016116.
- E. Cator and P. Van Mieghem, “Susceptible-infected-susceptible epidemics on the complete graph and the star graph: Exact analysis,” *Physical Review E* **87**, 012811 (2013), https://doi.org/10.1103/PhysRevE.87.012811, accessible full text https://www.nas.ewi.tudelft.nl/people/Piet/papers/PhysRevE2012_SIS_Complete_graph_and_star.pdf.
- P. Van Mieghem, “Explosive phase transition in susceptible-infected-susceptible epidemics with arbitrary small but nonzero self-infection rate,” *Physical Review E* **101**, 032303 (2020), https://doi.org/10.1103/PhysRevE.101.032303, accessible full text https://pure.tudelft.nl/ws/portalfiles/portal/72096045/PhysRevE.101.032303.pdf.
