# Sharp divergence between mean-outbreak and threshold-risk vaccination on paths

## Finding

For every integer \(n\ge 2\), every outbreak threshold \(h\ge 2\), and every independent bond-transmission probability \(0<p<1\), consider perfect vaccination of exactly one vertex of the path \(P_n\). A single initial infection is then drawn uniformly from the \(n-1\) unvaccinated vertices. Let \(M_v(p)\) be the expected total number infected and \(T_{v,h}(p)\) the probability that at least \(h\) vertices become infected when vertex \(v\) is vaccinated.

The mean-outbreak minimizers are exactly the one or two central vertices:
\[
\operatorname*{arg\,min}_{1\le v\le n}M_v(p)
=\left\{\left\lfloor\frac{n+1}{2}\right\rfloor,\left\lceil\frac{n+1}{2}\right\rceil\right\}.
\]
The threshold-risk minimizers, in contrast, are
\[
\operatorname*{arg\,min}_{1\le v\le n}T_{v,h}(p)=
\begin{cases}
\{v\in\mathbb Z:\max(1,n-h+1)\le v\le\min(n,h)\},& n\le 2h-1,\\
\{h,n-h+1\},& n\ge 2h.
\end{cases}
\]
All indicated minimizers are exact, including ties. Therefore the two objectives admit a common optimal vaccinated vertex **if and only if** \(n\le 2h\). When \(n\ge 2h+1\), their optimal sets are disjoint for every \(0<p<1\), and the exact excess threshold risk of vaccinating any mean-optimal vertex is
\[
T_{v_{\mathrm{mean}},h}(p)-\min_vT_{v,h}(p)
=\frac{(h-1)p^h}{n-1}>0.
\]

This identifies the sharp conflict cutoff \(n=2h+1\) simultaneously for every threshold \(h\ge2\). For example, when \(h=3\), the first disagreement occurs on \(P_7\): the mean-optimal vertex is \(4\), while threshold-risk-optimal vertices are \(3\) and \(5\) (one-based indexing), independently of \(p\).

## Assumptions and scope

The network is a finite, simple, undirected unweighted path with vertices \(1,\ldots,n\), where \(n\ge2\). Vaccination perfectly removes the chosen vertex and its incident contacts before introduction of disease. Each remaining undirected edge is independently open with a common probability \(p\in(0,1)\). The infected set is the open connected component of one uniformly sampled unvaccinated vertex. The threshold \(h\) is any integer at least two, including thresholds exceeding the number of unvaccinated vertices (in which case the tail probability is zero). Protection resources permit one vertex deletion only; expected outbreak and threshold risk are optimized separately.

This is an independent-undirected-bond outbreak model. Its distribution is not asserted to coincide with arbitrary continuous-time SIR models whose contact transmissions are correlated through shared infectious periods. The threshold concerns the absolute number of infections, not a growing fraction of population size.

## Proof

**1. Counting vertices in long open components.** Let \(F_m^{(h)}(p)\) denote the expected number of vertices belonging to open components containing at least \(h\) vertices after independently retaining the edges of a path on \(m\ge0\) vertices. When \(m<h\), clearly \(F_m^{(h)}=0\).

For an arbitrary *deterministic* configuration of open path edges, each component of length \(\ell\ge h\) contains exactly \(\ell-h+1\) consecutive subpaths on \(h\) vertices and \(\ell-h\) consecutive subpaths on \(h+1\) vertices. Consequently
\[
h(\ell-h+1)-(h-1)(\ell-h)=\ell.
\]
A component shorter than \(h\) contributes zero on both sides. Summing over all open components therefore gives the configurationwise identity
\[
\#\{\text{vertices in components of order at least }h\}
=hN_h-(h-1)N_{h+1},
\]
where \(N_j\) counts open consecutive subpaths on \(j\) vertices. This identity is exact for every binary edge configuration.

Each of the \(m-h+1\) candidate \(h\)-vertex subpaths is open with probability \(p^{h-1}\), and each of the \(m-h\) candidate \(h+1\)-vertex subpaths is open with probability \(p^h\). Taking expectations, for \(m\ge h\),
\[
F_m^{(h)}(p)=h(m-h+1)p^{h-1}-(h-1)(m-h)p^h.
\]
Equivalently, define
\[
A_h=p^{h-1}[h-(h-1)p]>0,\qquad
B_h=h(h-1)p^{h-1}(1-p)>0.
\]
Then \(F_m^{(h)}=A_hm-B_h\) for \(m\ge h\), while \(F_m^{(h)}=0\) for \(m<h\). In particular the increase \(F_{m+1}^{(h)}-F_m^{(h)}=A_h>0\) holds when \(m\ge h\).

**2. Exact threshold-risk optimization.** Vaccinating vertex \(v\) creates paths of lengths \(a=v-1\) and \(b=n-v\), with \(a+b=N=n-1\). Uniform seeding gives
\[
T_{v,h}(p)=\frac{F_a^{(h)}(p)+F_b^{(h)}(p)}{N}.
\]
If \(N\le2h-2\), both component lengths can be made less than \(h\). Such and only such positions have zero risk, because any component of size at least \(h\) contains a possible open \(h\)-block with positive probability for \(p>0\). The first displayed minimizer set follows.

If \(N\ge2h-1\), at least one side has size at least \(h\). Among splits where the other side has size \(s<h\), the objective numerator equals \(F_{N-s}^{(h)}=A_h(N-s)-B_h\), strictly decreasing in \(s\). Its minimum in this class is achieved precisely at \(s=h-1\), yielding \(v=h\) or \(v=n-h+1\).

If both sides are at least \(h\), necessarily \(N\ge2h\), and the risk numerator equals \(A_hN-2B_h\). Relative to the optimal one-small-side numerator \(A_h(N-h+1)-B_h\), this is larger by
\[
(A_hN-2B_h)-[A_h(N-h+1)-B_h]
=(h-1)A_h-B_h=(h-1)p^h>0.
\]
This establishes the second minimizer set and its strictness. It also gives the exact excess-risk formula whenever both sides of a centrally positioned vaccination have at least \(h\) vertices.

**3. Exact expected-outbreak optimization.** On an open component \(C\), the sum of infection counts over all seeds in \(C\) is \(|C|^2\). Since \(|C|^2=|C|+2\binom{|C|}{2}\), the expected outbreak for a retained path of length \(m\) is determined by expected connected vertex pairs. Any fixed pair of distance \(d\) on a path is connected if and only if all \(d\) intervening edges are open, which has probability \(p^d\). Therefore the expected number of connected unordered pairs on \(P_m\) is
\[
H_m(p)=\sum_{d=1}^{m-1}(m-d)p^d\quad(m\ge1),\qquad H_0=0.
\]
For vaccinated vertex \(v\),
\[
M_v(p)=1+\frac{2}{n-1}[H_{v-1}(p)+H_{n-v}(p)].
\]
For all \(m\ge0\), the first discrete increment satisfies \(H_{m+1}-H_m=\sum_{d=1}^{m}p^d\), whose successive increments increase strictly for \(p>0\). Consequently shifting one vertex from a longer component to a shorter one strictly lowers \(H_a+H_b\) whenever their sizes differ by at least two. Precisely the balanced splits \(\lvert a-b\rvert\le1\) minimize the mean. These correspond exactly to the stated central vertex or central pair.

**4. Sharp cutoff and gap.** For \(n\le2h-1\), a mean-optimal balanced deletion leaves both components shorter than \(h\), so also minimizes threshold risk. At \(n=2h\), both central deletions are the two risk-optimal positions. For \(n\ge2h+1\), a balanced deletion leaves *both* components of size at least \(h\), whereas a threshold-risk optimum must leave one component of size exactly \(h-1\); the optimal sets are therefore disjoint. Dividing the positive numerator difference in Step 2 by \(n-1\) proves the claimed exact gap. This completes all cases, including equality boundaries and arbitrary integers \(n,h\) in the stated domain.

## Verification

Run `python3 verify_path_tail.py` with Python 3 (standard library only). The standalone checker exhaustively confirms the deterministic run-count identity for 16,376 edge-configuration/threshold pairs, the expected component formula by 252 exact-rational enumerations, the pair-connectivity formula by 36 exact-rational enumerations, and both minimizer classifications in 1,089 exact-rational parameter instances. It also verifies the sharp \(n=7,h=3,p=1/2\) boundary and its risk gap \(1/24\). These finite tests are checks, not the proof of the all-order result; that proof is Steps 1–4 above.

At \(n=7,h=3,p=1/2\), vaccinating the center yields mean \(11/6\) and risk \(1/4\); vaccinating vertex \(3\) or \(5\) yields mean \(15/8\) and risk \(5/24\). Thus each objective is strictly better at its own respective choice.

## Relationship to prior work

Miller's 2008 network-epidemic analysis explicitly distinguishes epidemic probability from epidemic size and treats random initial infection, but studies transmissibility-heterogeneity bounds rather than exact one-vaccination minimizers on finite paths. Altarelli et al. (first public arXiv version September 11, 2013) study targeted immunization using marginal infection and expected-burden objectives, not the all-threshold path tail-minimizer classification. Holme (2017) analyzes exact expected-outbreak-based vaccination and other node-importance objectives on small graphs; the threshold-event objective and arbitrary path order are not part of its reported classification. These scientific comparisons are differences in mathematical statements, not assertions that mere title or keyword mismatch proves historical novelty.

The exact run-count identity is elementary and is not represented as new in isolation. The contribution claimed here is its application to a *complete* all-order/all-threshold intervention classification and a sharp incompatibility boundary for two motivated objectives. A search of relevant scholarly formulations and available mathematical research records found no directly subsuming result, but hidden equivalents and uninspected sources remain possible.

## Limitations

The risk event counts at least a fixed absolute number of cases, including very small thresholds; for large paths this is not synonymous with a major population-level epidemic. In particular, the absolute gap decreases like \(1/(n-1)\) at fixed \(h,p\). The model uses independent undirected open edges, a uniformly random seed after protection, identical vaccine efficacy, and just one deletion. It does not cover heterogeneous rates, correlated directed transmissions, multiple vaccinees, dynamic recovery models with nonindependent edges, or stochastic seeding before vaccination. Independently established historical priority and external scientific validation have not been performed.

## References

- Joel C. Miller, *Bounding the Size and Probability of Epidemics on Networks*, first public arXiv version March 6, 2008, https://arxiv.org/abs/0803.0999.
- F. Altarelli, A. Braunstein, L. Dall'Asta, J. R. Wakeling and R. Zecchina, *Containing epidemic outbreaks by message-passing techniques*, first public arXiv version September 11, 2013, https://arxiv.org/abs/1309.2805; published in Physical Review X 4 (2014), 021024.
- Petter Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, Physical Review E 96 (2017), 062305, https://doi.org/10.1103/PhysRevE.96.062305.
