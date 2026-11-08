# Eight vertices are sharp for transmissibility-dependent optimal single-edge epidemic interdiction on trees

## Finding

**Theorem.** Consider a finite simple tree \(T\) on \(n\ge 2\) vertices. Exactly one of its edges is permanently blocked before an outbreak. Subsequently one initial infected vertex is selected uniformly from all \(n\) original vertices, and every other edge independently transmits with probability \(p\in(0,1)\). Infection eventually reaches precisely the open-edge component of the seed. The objective is to minimize expected final outbreak size, with the seed law remaining uniform on all original vertices after intervention.

For every tree with \(2\le n\le7\), **there exists an edge that is optimal for every** \(p\in(0,1)\). This is sharp: in the eight-vertex tree with edge set

\[
\{01,12,23,04,05,36,37\},
\]

where \(01\) means the edge between vertices \(0\) and \(1\), the optimal edge changes with transmission probability. For \(0<p<1/2\), the *two near-hub bridge edges* \(01\) and \(23\) are jointly optimal; for \(p=1/2\), edges \(01,12,23\) tie; for \(1/2<p<1\), only the *central bridge edge* \(12\) is optimal. The other four (pendant) edges are never optimal for \(0<p<1\).

Consequently eight is the minimum tree order admitting a transmission-dependent change in the optimal single-edge block under this precise expected-size criterion. This is not a statement about vertex vaccination, fixed-seed interventions, multiedge blocking, cycles, or non-tree networks.

## Assumptions and scope

The epidemic is a one-seed Reed–Frost or equivalently independent bond-percolation final-size model. Each edge transmits independently, with a single common probability \(p\). The blocked edge is determined before, and without knowledge of, the uniformly drawn seed. The blocked edge has zero residual transmission probability; all unblocked edges have unchanged transmission probability. Every vertex is counted in expected final outbreak size, including a seed isolated by the block.

Let \(S_T(p)\) denote mean total infections without blocking, and \(S_{T-e}(p)\) mean total infections when \(e\) is blocked. The benefit of blocking \(e\) is \(G_e(p)=S_T(p)-S_{T-e}(p)\). An optimal edge maximizes \(G_e(p)\), equivalently minimizes \(S_{T-e}(p)\).

## Proof

**1. Exact objective.** In any forest \(H\) on \(n\) vertices, a uniformly selected seed reaches another vertex \(v\) exactly when every edge along their unique path is open. Thus

\[
 S_H(p)=1+\frac{2}{n}\sum_{\{u,v\}:\,u\leftrightarrow v\text{ in }H} p^{d_H(u,v)}.
\]

If deleting tree edge \(e\) partitions the original tree into \(U_e,V_e\), the only erased pair-connectivities are those crossing this cut. Therefore

\[
 G_e(p)=\frac2n F_e(p),\qquad
 F_e(p)=\sum_{u\in U_e}\sum_{v\in V_e}p^{d_T(u,v)}.
\]

In particular \(F_e\) is an integer-coefficient polynomial of degree at most \(n-1\), with no constant term. The exact mean-size objective is therefore reduced to comparison of finitely many explicitly computable polynomial pairs.

**2. Universal cutoff for orders at most seven.** All labeled trees of order \(n\ge2\) correspond bijectively to the \(n^{n-2}\) Prüfer words of length \(n-2\), including the unique empty word for \(n=2\). The standalone `verify.py` enumerates every word and reconstructs its tree. It enumerates each edge cut, computes the exact integer coefficients of \(F_e(p)\) by unique-path distances, and selects an edge \(e_*\) maximizing the exact value \(F_e(1/2)\) (ties are resolved by the deterministic list order, which is mathematically immaterial).

For every other edge \(f\), write \(D(p)=F_{e_*}(p)-F_f(p)=\sum_{i=0}^{d}a_i p^i\), with \(d=n-1\). Its degree-\(d\) Bernstein coefficients are exactly

\[
 b_j=\sum_{i=0}^{j}a_i\frac{\binom ji}{\binom di},\quad j=0,\ldots,d,
\]

so the identity

\[
 D(p)=\sum_{j=0}^{d}\binom dj b_j p^j(1-p)^{d-j}
\]

shows that all nonnegative \(b_j\) imply \(D(p)\ge0\) for every \(0\le p\le1\). The checker uses Python integer arithmetic and `fractions.Fraction`, not floating-point approximations, to confirm **every one of these coefficients is nonnegative for every competing edge of every labeled tree of orders two through seven**. Counts by order are \(1,3,16,125,1296,16807\), totaling \(18{,}248\) labeled trees. Since the Prüfer bijection is exhaustive and edge-by-edge comparisons cover all interventions, this is a finite exhaustive proof rather than sampling the continuum \(p\in(0,1)\).

**3. Sharp eight-vertex witness.** In the stated eight-vertex tree, direct application of the cut-distance formula yields three distinct edge scores: for either near-hub edge, for the central edge, and for any pendant edge, respectively,

\[
\begin{aligned}
 F_h(p)&=p+3p^2+3p^3+4p^4+4p^5,\\
 F_m(p)&=p+2p^2+5p^3+4p^4+4p^5,\\
 F_\ell(p)&=p+2p^2+p^3+p^4+2p^5.
\end{aligned}
\]

The exact differences are

\[
\begin{aligned}
 F_h(p)-F_m(p)&=p^2(1-2p),\\
 F_h(p)-F_\ell(p)&=p^2(1+2p+3p^2+2p^3),\\
 F_m(p)-F_\ell(p)&=p^3(4+3p+2p^2).
\end{aligned}
\]

The latter two differences are strictly positive throughout \(p\in(0,1)\), while the first changes sign only at \(p=1/2\). This proves the complete optimal-edge classification, including the ties at the threshold, and establishes the sharp lower bound on tree order.

## Verification

Run `python3 verify.py` with Python 3.8 or later; the script uses only Python's standard library. It checks all \(18{,}248\) labeled trees at orders two through seven, **all** competing edges, and the exact Bernstein sign certificates without discretizing transmission probabilities. It prints the seven exact edge-distance polynomial coefficient vectors for the witness and checks their symbolic identities. As a separate independent calculation, it enumerates all bond-open/bond-closed configurations on the six unblocked witness edges at probabilities \(1/4\), \(1/2\), and \(3/4\), computes expected component size directly from connected components, and compares all intervention differences with the polynomial formula using exact rational arithmetic. The finite tests support the explicitly stated model only, and do not claim coverage of larger trees or arbitrary graphs.

## Relationship to prior work

Marcelino and Kaiser (2009) motivate suppressing epidemic spread by targeted removal of travel-network edges, with empirical networks and outbreak simulations, rather than a universal all-transmissibility optimal-edge classification for trees. Enns, Mounzer, and Brandeau (2011) study optimal link removal by separating known infected from susceptible populations using graph partitioning; their zero/one reachability objective with designated initial infections does not give the uniform unknown-seed, probability-weighted comparison here. Kenah and Miller (2011) develop epidemic percolation networks and final-size/out-component correspondences that support the general modeling framework, without the specific minimal-order intervention result. Marcelino and Kaiser (2012) analyze airline flight cancellations and epidemic delay, again a different network, source, and criterion. Sharkey and collaborators (2012 preprint) establish exact epidemic equations on trees for Markovian dynamics; they do not compare one-edge deletion across every transmission probability.

The present theorem is a finite special-case exact optimization classification. It does **not** assert that the general percolation representation or polynomial evaluation is new. The related literature on reliability importance and edge interdiction might contain an unlocated equivalent optimality result; historical priority therefore requires independent assessment.

## Limitations

The 7-vertex universal property is verified through a complete **finite exact computation**, not a short structural pen-and-paper classification. The cutoff cannot be extended beyond seven because of the explicit eight-vertex counterexample. No optimality statement is made for graphs with cycles, interventions that target a node, more than one deleted edge, a nonuniform or pre-known outbreak seed, edge-specific transmission probabilities, changing the seed distribution after deletion, or epidemics where independent bond transmission is not a valid final-size model. The illustrative distinction is mathematical, not a recommendation about actual epidemic-control decisions. Independent historical-priority audit and independent mathematical audit have not been performed.

## References

1. J. Marcelino and M. Kaiser, "Reducing influenza spreading over the airline network," *PLoS Currents* (first public 2009-08-21), doi:10.1371/currents.rrn1005. https://pubmed.ncbi.nlm.nih.gov/20020673/
2. E. A. Enns, J. J. Mounzer, and M. L. Brandeau, "Optimal Link Removal for Epidemic Mitigation: A Two-Way Partitioning Approach," *Mathematical Biosciences* (first public 2011-11-16), doi:10.1016/j.mbs.2011.11.006. https://pmc.ncbi.nlm.nih.gov/articles/PMC3434711/
3. E. Kenah and J. C. Miller, "Epidemic Percolation Networks, Epidemic Outcomes, and Interventions," (first public 2011-02-21), doi:10.1155/2011/543520. https://onlinelibrary.wiley.com/doi/full/10.1155/2011/543520
4. J. Marcelino and M. Kaiser, "Critical paths in a metapopulation model of H1N1: Efficiently delaying influenza spreading through flight cancellation," *PLoS Currents* (2012-04-23), doi:10.1371/4f8c9a2e1fca8. https://pmc.ncbi.nlm.nih.gov/articles/PMC3392097/
5. K. J. Sharkey et al., "Exact equations for SIR epidemics on tree graphs," preprint publicly dated 2012-12-10, https://arxiv.org/abs/1212.2172
