# A Poisson bulk and an exponentially tilted simplex in multi-hub zero-range condensation

## Finding
Fix an integer \(r\ge3\), nonnegative integers \(h_1,\ldots,h_r\), and \(\rho>0\). For each \(n\ge1\), start with the complete bipartite graph \(K_{r,n}\), whose \(r\)-vertex part is labeled \(a_1,\ldots,a_r\). Attach \(h_i\) new pendant vertices to \(a_i\), and put \(M_n\ge1\) indistinguishable particles on the resulting graph, with \(M_n/n\to\rho\). In the continuous-time zero-range process, each nonempty site emits one particle at total rate one, sending it to a uniformly chosen neighbor. Let \(U_{i,n}\) be the stationary occupation of hub \(a_i\), and let \(S_n\) count the particles on the original \(n\)-vertex part (not on the hubs or the added pendants). Then
\[
\left(S_n,\frac{U_{1,n}}{M_n},\ldots,\frac{U_{r,n}}{M_n}\right)
\ \Longrightarrow\ (P,X_1,\ldots,X_r),
\]
where \(P\sim\operatorname{Poisson}(r)\), independent of \(X\), and \(X\) has density
\[
f_{\rho,h}(x)=\frac{\exp\bigl(\rho\sum_{i=1}^r h_i x_i\bigr)}{\displaystyle\int_{\Delta_{r-1}}\exp\bigl(\rho\sum_{i=1}^r h_i y_i\bigr)\,dy},\qquad x\in\Delta_{r-1},
\]
with respect to \((r-1)\)-dimensional coordinate Lebesgue measure on \(\Delta_{r-1}=\{x_i\ge0,\ \sum_{i=1}^r x_i=1\}\). The total number of particles on all added pendant vertices converges to zero in probability. If the \(h_i\) are equal, \(X\) is uniform on the simplex, or \(\operatorname{Dirichlet}(1,\ldots,1)\). If just one pendant is attached to \(a_1\), the limit of its occupied fraction has density proportional to \(e^{\rho x}(1-x)^{r-2}\) on \([0,1]\). Thus a single added edge, with all original hub degrees equal to \(n\), produces a nonvanishing macroscopic redistribution among the hubs.

## Assumptions and scope
The graph is finite, simple, connected, and undirected. Particles have unlimited nonnegative integer occupation and their total number \(M_n\ge1\) is fixed for each \(n\). Empty sites have zero departure rate. Each nonempty site has a unit total departure rate, **not** a unit rate per particle; the destination is uniformly distributed over its neighbors. All parameters \(r\), \(h_i\), and \(\rho\) are fixed while \(n\to\infty\), and \(M_n/n\to\rho>0\). This is a stationary distribution theorem, not a theorem about relaxation times or the dynamics of condensate formation. In particular \(r\ge3\) is part of the assertion.

## Proof
**1. Exact stationary weights.** If \(d_v\) is the degree of a vertex and \(m_v\) its particle count, write
\[
\pi(m)=Z_{n,M}^{-1}\prod_v d_v^{m_v},\quad \sum_v m_v=M.
\]
For adjacent vertices \(v,w\), if \(m_v>0\), the forward jump has rate \(1/d_v\). The reverse state differs in weight by \(d_w/d_v\), and its reverse jump has rate \(1/d_w\), giving detailed balance. Connectedness makes this stationary law unique. The \(r\) hub degrees are \(n+h_i\), each of the \(n\) original opposite-part vertices has degree \(r\), and each of the \(H=\sum_i h_i\) pendants has degree one. Consequently
\[
Z_{n,M}=[z^M]\prod_{i=1}^{r}\frac1{1-(n+h_i)z}\cdot\frac1{(1-rz)^n(1-z)^H}.
\]
This identity is valid for every \(n\) and \(M\).

**2. Concentration of the outside mass.** Let \(L_n\) denote pendant occupation. Write
\[
T_n(t)=\sum_{u_1+\cdots+u_r=t}\prod_{i=1}^r(1+h_i/n)^{u_i},\qquad t\ge0.
\]
For \(s+\ell\le M\), the unnormalized joint mass of \((S_n,L_n)=(s,\ell)\), divided by \(n^M\), equals
\[
\binom{n+s-1}{s}\left(\frac rn\right)^s\binom{H+\ell-1}{\ell}n^{-\ell}\,T_n(M-s-\ell),
\]
where if \(H=0\), only \(\ell=0\) is allowed and its binomial factor is one. The function \(T_n(t)\) is nondecreasing in \(t\): adding one particle to a hub takes every composition of \(t\) injectively to a composition of \(t+1\), increasing or preserving its weight. As shown in Step 3, \(T_n(M-s-\ell)/T_n(M)\to1\) for each fixed \(s,\ell\). Also
\[
\binom{n+s-1}{s}(r/n)^s\to\frac{r^s}{s!}.
\]
For all \(s\le M\), when \(M/n\le\rho+1\), this term is bounded by \((r(\rho+2))^s/s!\), and \(\sum_{\ell\ge0}\binom{H+\ell-1}{\ell}n^{-\ell}=(1-1/n)^{-H}\) for \(n>1\). These bounds permit dominated convergence of the full partition sum divided by \(n^M T_n(M)\): it tends to \(e^r\). It follows that \(S_n\Rightarrow\operatorname{Poisson}(r)\), while \(\Pr(L_n>0)\to0\). In particular \(\sum_i U_{i,n}/M_n\to1\) in probability.

**3. Hub simplex law and independence.** For any fixed \(s,\ell\), set \(t=M_n-s-\ell\). Uniformly for \(u_1+\cdots+u_r=t\), with \(x_i=u_i/t\),
\[
\prod_i(1+h_i/n)^{u_i}=\exp\left(\frac tn\sum_i h_ix_i+O_{r,h}(t/n^2)\right).
\]
Since \(t/n\to\rho\), the lattice of weak compositions of \(t\) gives Riemann sums on the simplex, hence for every continuous \(g\),
\[
\frac{\sum_{\sum u_i=t}g(u/t)\prod_i(1+h_i/n)^{u_i}}{T_n(t)}
\longrightarrow\frac{\int_{\Delta_{r-1}}g(x)e^{\rho\sum_i h_ix_i}\,dx}{\int_{\Delta_{r-1}}e^{\rho\sum_i h_ix_i}\,dx}.
\]
In particular \(T_n(t)/t^{r-1}\) converges to the strictly positive denominator, yielding the ratio used in Step 2. The same limiting conditional law holds for each fixed \(s,\ell\), and \(t/M_n\to1\). Summing first over bounded \(s\), then using the Poisson tail and \(\Pr(L_n>0)\to0\), proves joint convergence and independence.

**4. Explicit one-edge effect.** With \(h=(1,0,\ldots,0)\), integration over the other \(r-1\) coordinates gives
\[
\Pr(X_1\in dx)=\frac{e^{\rho x}(1-x)^{r-2}}{\int_0^1 e^{\rho t}(1-t)^{r-2}\,dt}\,dx,\qquad0<x<1.
\]
Without the pendant, the marginal density is \((r-1)(1-x)^{r-2}\). These are different for every \(\rho>0\). For example, when \(r=3\) and \(\rho=1\),
\[
\mathbb E X_1=\frac{3-e}{e-2}>\frac13,
\]
whereas the symmetric graph gives mean \(1/3\).

## Verification
The accompanying standard-library program `verify.py` independently enumerates labeled configurations and computes the reduced coefficient sums, checks detailed balance on every relevant directed edge move in multiple small systems, and checks exact finite partition distributions against the predicted Poisson and tilted-simplex limits at \(n=20,40,80,160,320\). It reports 2169 successful finite assertions and numerical-bound comparisons. These calculations test the algebra but **do not replace** the infinite-size proof, which is Steps 1–4.

Run `python verify.py` with Python 3 and no third-party dependencies.

## Relationship to prior work
The degree-weighted canonical stationary measure is foundational and appears already in Noh–Shim–Lee (2004), equations (1)–(4), as well as Bogacz–Burda–Janke–Waclaw (2007), equations (1)–(3), and Waclaw–Bogacz–Burda–Janke (2007), Section II. Noh et al. discuss scale-free networks with a unique largest hub, not the present multiple tied leading degrees and their joint canonical fluctuation law. Those works investigate homogeneous systems, star-like geometries, and one anomalously large-degree site; the new assertion is the simultaneous multi-hub \(r\)-simplex law, an independent finite Poisson outside population, and the nonvanishing effect of finitely many pendant edges. Schwarzkopf–Evans–Mukamel (2008) studies multiple condensates driven by *nonmonotonic occupancy-dependent hopping rates* on a ring rather than fixed high-degree hubs with constant hopping. Mailler–Mörters–Ueltschi (2015) treats random weak site disorder and regularly varying interaction weights with unique-site condensates, not the deterministic \(r\)-hub constant-rate critical degree splitting. A separately examined two-defect directed-ring calculation obtains a one-dimensional exponential sharing law with a Gaussian macroscopic-background fluctuation; it does not imply the \(r\ge3\) simplex with an independently Poisson microscopic bulk. The generic factorization formula is common prior knowledge and not claimed as new.

## Limitations
There is no new general stationary-measure formula; the contribution is a specific all-\(r\) scaling law and critical finite-graph perturbation phenomenon. The law holds only for fixed \(r\ge3\), fixed pendant counts, constant occupied-site departure rate, and particle counts linear in \(n\). It gives neither a relaxation/mixing rate nor a dynamic condensation time. Historical uniqueness is not independently certified, and further literature not indexed by the cited databases may contain analogous finite-degeneracy limits. The two-hub case is provided only as background intuition, not the new principal assertion.

## References
1. L. Bogacz, Z. Burda, W. Janke, B. Waclaw, *Balls-in-boxes condensation on networks*, arXiv:cond-mat/0701553 (first public 2007-01-23), https://arxiv.org/abs/cond-mat/0701553.
2. B. Waclaw, L. Bogacz, Z. Burda, W. Janke, *Condensation in zero-range processes on inhomogeneous networks*, arXiv:cond-mat/0703243 (first public 2007-03-09), https://arxiv.org/abs/cond-mat/0703243.
3. Y. Schwarzkopf, M. R. Evans, D. Mukamel, *Zero-Range Processes with Multiple Condensates: Statics and Dynamics*, arXiv:0801.4501 (first public 2008-01-29), https://arxiv.org/abs/0801.4501.
4. C. Mailler, P. Mörters, D. Ueltschi, *Condensation and symmetry-breaking in the zero-range process with weak site disorder*, arXiv:1509.07672 (first public 2015-09-25), https://arxiv.org/abs/1509.07672.
5. J. D. Noh, G. M. Shim, H. Lee, *Complete Condensation in a Zero Range Process on Scale-Free Networks*, arXiv:cond-mat/0409120 (first public 2004-09-06), https://arxiv.org/abs/cond-mat/0409120.
