# A parity-sensitive weak-link law for irreversible dimers on clique barbells

## Finding

Let \(B_{a,b}\) be two disjoint complete graphs \(K_a\) and \(K_b\), with one designated vertex in each joined by a single bridge. For any integers \(a,b\geq2\), independently attempt irreversible dimer deposition on each internal edge at Poisson rate \(1\) and on the bridge at rate \(\lambda>0\); an attempted edge is occupied exactly when both its endpoints are vacant. Write \(P_{a,b}(\lambda)\) for the probability that the bridge is occupied at jamming.

**Exact finite law.** If \(K_n(t)\) is the number of unmatched vertices at time \(t\) for the same isolated deposition process on \(K_n\), then
\[
q_n(t)=\frac{\mathbb E K_n(t)}{n},\qquad
P_{a,b}(\lambda)=\lambda\int_0^\infty e^{-\lambda t}q_a(t)q_b(t)\,dt.
\]
This is an exact integral of finite sums of exponentials and hence a rational function of each positive rational \(\lambda\). An explicit finite rational recursion is provided in the proof.

**Weak-bridge parity singularity.** For every fixed \(a,b\geq2\),
\[
\lim_{\lambda\downarrow0}P_{a,b}(\lambda)=
\frac{\mathbf1_{\{a\text{ odd}\}}\mathbf1_{\{b\text{ odd}\}}}{ab}.
\]
Thus an arbitrarily weak positive bridge retains a nonzero probability of irreversible occupancy precisely when both cliques have odd order, even though removing the bridge altogether makes that occupancy impossible.

**Unequal-community logarithmic law and rate crossover.** Fix \(\rho\in(0,\infty)\) and let \(a\to\infty\), \(b/a\to\rho\). For every fixed \(\lambda>0\),
\[
\lim aP_{a,b}(\lambda)=\lambda h(\rho),\qquad
h(\rho)=\begin{cases}\dfrac{\log\rho}{\rho-1},&\rho\neq1,\\1,&\rho=1.\end{cases}
\]
At the competing rate scale \(\lambda=ca\), for every fixed \(c>0\),
\[
\lim P_{a,b}(ca)=c\int_0^\infty\frac{e^{-cs}}{(1+s)(1+\rho s)}\,ds.
\]
The crossover limit tends to zero as \(c\downarrow0\) and to one as \(c\to\infty\).

**Exact jammed-size law.** Let \(N\) be the number of accepted dimers. Put
\[
N_0=\lfloor a/2\rfloor+\lfloor b/2\rfloor,\qquad
N_1=1+\lfloor(a-1)/2\rfloor+\lfloor(b-1)/2\rfloor.
\]
Then \(N=N_1\) when the bridge is occupied and \(N=N_0\) otherwise. Hence the entire distribution of \(N\) is determined by \(P_{a,b}(\lambda)\). For two even-order cliques the bridge reduces the total deposition count by one; for two odd-order cliques it increases the count by one; for mixed parity it leaves the count unchanged.

## Assumptions and scope

All cliques are simple and labeled. Each internal edge has an independent unit-rate Poisson process of attempted dimer placement; the sole bridge has independent rate \(\lambda>0\). Accepted dimers cover both endpoints permanently. There is no desorption, diffusion, interaction beyond hard-core exclusion, or finite-time stopping rule. The asserted probabilities concern the eventual jammed matching. Integer orders satisfy \(a,b\geq2\), and the two-community limits allow arbitrary sequences of integers with \(b/a\to\rho\in(0,\infty)\).

## Proof

**1. Isolation-and-clock coupling.** Run independent deposition processes on the two isolated cliques while independently running a rate-\(\lambda\) exponential clock for the bridge. Up to the bridge clock, the combined process is identical to deposition on the barbell. The bridge is accepted exactly if both designated endpoints have not been covered by their isolated clique processes before its clock. In an isolated clique, exchangeability conditional on \(K_n(t)=k\) makes the probability that a fixed endpoint is vacant equal to \(k/n\). Independence of the two isolated cliques therefore gives the displayed Laplace integral.

**2. Exact finite recurrence.** Let \(R_{i,j}\) denote bridge-occupation probability when both bridge endpoints and respectively \(i,j\) other vertices remain vacant in the two cliques. The only currently usable edges are the bridge (rate \(\lambda\)), \(i+j\) internal edges incident to a bridge endpoint (whose acceptance permanently prevents bridge occupation), and \(\binom{i}{2}+\binom{j}{2}\) edges between other vacant vertices. Conditioning on the first accepted edge yields
\[
R_{i,j}=\frac{\lambda+\binom{i}{2}R_{i-2,j}+\binom{j}{2}R_{i,j-2}}{\lambda+\binom{i+1}{2}+\binom{j+1}{2}},\qquad P_{a,b}(\lambda)=R_{a-1,b-1},
\]
where terms whose first subscript is negative are omitted and \(R_{0,0}=1\). This uniquely defines every finite probability using smaller nonnegative indices. The pure-death chain \(K_n(t)\) jumps \(k\to k-2\) at rate \(\binom{k}{2}\), so its transition probabilities are finite linear combinations of exponentials and the Laplace formula is computable exactly.

Equivalently, there is a fully finite partial-fraction expression without time integration. Define \(\mathcal K_n=\{n,n-2,\ldots,n\bmod2\}\), \(r_k=\binom{k}{2}\), and coefficients \(c^{(n)}_{k,j}\) by \(c^{(n)}_{n,n}=1\) and, descending in \(k\) by two, for \(j>k\),
\[
c^{(n)}_{k,j}=\frac{r_{k+2}c^{(n)}_{k+2,j}}{r_k-r_j},\qquad
c^{(n)}_{k,k}=-\sum_{j>k}c^{(n)}_{k,j}.
\]
Put \(w_{n,j}=n^{-1}\sum_{k\in\mathcal K_n}k c^{(n)}_{k,j}\). The pure-death forward equations give \(q_n(t)=\sum_{j\in\mathcal K_n}w_{n,j}e^{-r_jt}\) and therefore
\[
P_{a,b}(\lambda)=\sum_{i\in\mathcal K_a}\sum_{j\in\mathcal K_b}\frac{\lambda w_{a,i}w_{b,j}}{\lambda+r_i+r_j}.
\]
These explicit finite rational coefficients are a second computational route, independent of direct graph-state enumeration. At \(\lambda=1\), for example, \(P_{2,2}=1/3\), \(P_{3,3}=2/7\), \(P_{4,4}=5/26\), and \(P_{3,4}=79/350\).

**3. Weak-bridge boundary.** At infinite time, a greedy matching of an isolated clique leaves precisely \(n\bmod2\) unmatched vertices. Its single residual vertex, if it exists, is uniform by symmetry. Consequently \(\lim_{t\to\infty}q_n(t)=\mathbf1_{\{n\text{ odd}\}}/n\). As \(\lambda\downarrow0\), a rate-\(\lambda\) exponential clock diverges in probability, so bounded convergence in the clock mixture gives the stated parity limit. At \(\lambda=0\), no bridge attempts take place; the one-sided limit need not agree with this separate process.

**4. Jammed size.** Condition on whether the bridge is eventually accepted. Without it, both isolated cliques must become maximal matchings and therefore contain exactly \(\lfloor a/2\rfloor\) and \(\lfloor b/2\rfloor\) dimers. With it, one vertex on each side is committed to the bridge and all remaining vertices in each clique are eventually paired as completely as their parity permits. This gives \(N_0,N_1\). It remains true if the bridge is accepted after some internal dimers have already been placed.

**5. Macroscopic limit and logarithm.** On the accelerated time scale \(s=nt\), the fraction \(K_n(s/n)/n\) has jumps of size \(2/n\), drift \(-x^2+O(1/n)\), and quadratic variation \(O(1/n)\) on every bounded interval. Martingale concentration and Gronwall's inequality give convergence in probability, uniformly on bounded \(s\)-intervals, to the solution \(x'(s)=-x(s)^2\), \(x(0)=1\): namely \(x(s)=(1+s)^{-1}\). Since fractions lie in \([0,1]\), also \(q_n(s/n)\to(1+s)^{-1}\).

To justify passage under the rescaled integral, write \(u_n(t)=\mathbb E K_n(t)\). Since \(u_n'(t)=-\mathbb E[K_n(t)(K_n(t)-1)]\le u_n(t)-u_n(t)^2\), scalar comparison gives
\[
q_n(t)\le\frac{1}{n-(n-1)e^{-t}}.
\]
For \(b/a\) bounded above and below, this bounds \(q_a(s/a)q_b(s/a)\) by \(C(1+s)^{-2}\) on \(0\le s\le a\); the integral over \(s>a\), weighted by \(e^{-\lambda s/a}\), is \(O(1/a)\) for fixed \(\lambda>0\). Dominated convergence on the first range and this tail estimate yield
\[
\lim\frac{aP_{a,b}(\lambda)}{\lambda}
=\int_0^\infty\frac{ds}{(1+s)(1+\rho s)}
=h(\rho).
\]
For \(\lambda=ca\), direct substitution gives a bounded integrand dominated by \(ce^{-cs}\), proving the stated crossover. The limit as \(c\downarrow0\) follows from integrability of the rational kernel, and the limit as \(c\to\infty\) follows from concentration of the exponential density at \(s=0\).

## Verification

The standalone script `verify_direct.py` independently enumerates all available edges in every reachable unmatched-vertex configuration, computes the bridge event and entire jammed-size law, and compares these against the reduced recurrence using exact rational arithmetic. It passes 72 tests across unequal clique sizes and three bridge rates. The separate script `verify_laplace.py` constructs the isolated-clique pure-death exponential decomposition, integrates two independent survival functions exactly, and confirms 588 rational identities against the recurrence. It also checks the odd-clique terminal survival coefficients and prints asymptotic numerical comparisons. Run each script with Python 3; no third-party packages are required. These finite tests support, but do not replace, the all-order proof and asymptotic argument above.

## Relationship to prior work

Pippenger (1989) studied graph random sequential adsorption and included edge blocking; Dyer and Frieze (1991) studied randomized greedy matching on graphs. The stochastic mechanism here is an instance of their general subjects, and the edge-by-edge conditioning principle is not claimed as new. Cadilhe, Araújo and Privman (2006) review dimer and monomer deposition on patterned substrates and include exact Bethe-lattice equations, not the present finite dense two-clique bridge model. The specific finite bridge probability, weak-positive-rate parity discontinuity, unequal-clique logarithmic asymptotic, rate crossover and resulting size law are the claimed contribution. Full text of the historical 1989 and 1991 works was unavailable in the present literature comparison; priority with respect to uninspected specialized results remains a limitation.

## Limitations

The claims concern irreversible edge dimer deposition under exponential Poisson attempts, not equilibrium monomer-dimer models, arbitrary vertex-arrival greedy matching, or adsorption with diffusion. The logarithmic limit assumes both clique sizes diverge with a strictly positive finite ratio; it is not asserted for highly unequal scales. The crossover holds at \(\lambda=ca\) with fixed \(c>0\). Exact rational verification covers only finite test instances; it is not a proof of the limits. Historical novelty is provisional pending full-text checks of inaccessible older literature and independent scientific validation.

## References

1. A. Cadilhe, N. A. M. Araújo and V. Privman, *Random Sequential Adsorption: From Continuum to Lattice and Pre-Patterned Substrates*, arXiv:cond-mat/0611413 (first posted 2006-11-15), https://arxiv.org/abs/cond-mat/0611413.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics **2** (1989), 393–401, https://doi.org/10.1137/0402034.
3. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms **2** (1991), 29–45, https://doi.org/10.1002/rsa.3240020104.
