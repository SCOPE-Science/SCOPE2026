# All-time grounded heat-trace ordering on cocktail-party networks

## Finding

Fix integers \(m\ge2\) and \(1\le k<2m\). In the unit-conductance *cocktail-party graph* \(G_m=K_{2m}\setminus M_m\), label the \(m\) deleted matching pairs as the natural two-vertex parts. For any set \(S\) of \(k\) perfectly grounded leaders, put \(U=V(G_m)\setminus S\) and \(A_S(\mu)=L_{UU}+\mu I\), where \(L\) is the combinatorial graph Laplacian and \(\mu\ge0\).

**All-time strict hierarchy theorem.** Let \(r(S)\) be the number of deleted-matching pairs lying *entirely among followers* \(U\). For every \(t>0\) and every \(\mu\ge0\), the grounded heat-trace objective
\[
H_{t,\mu}(S)=\operatorname{tr}\!\left(e^{-tA_S(\mu)}\right)
\]
is **strictly decreasing in \(r(S)\)** among all \(k\)-leader sets. Any two sets with the same \(r(S)\) have equal heat traces for every time. Consequently, the unique optimal placement type, simultaneously for *all positive times*, consists of \(\lfloor k/2\rfloor\) completely grounded missing-edge pairs and—when \(k\) is odd—one vertex from an additional pair. There are exactly \(\binom m{k/2}\) optimum sets for even \(k\), and \(2(m-r)\binom mr\) optimum sets for odd \(k=2r+1\). Every other placement is strictly worse at *every* positive time.

For each real \(p>0\) and \(\mu\ge0\), exactly the same sets minimize \(\operatorname{tr}(A_S(\mu)^{-p})\). They also uniquely minimize \(\mathcal E_T(S)=\int_0^T\operatorname{tr}(e^{-2tA_S(\mu)})\,dt\) for every finite \(T>0\). These are corollaries of the strict pointwise heat-trace comparison, rather than separate assumptions.

The optimal spectrum is explicit. Put \(h=2m-k\), \(a=2m-1+\mu\), and \(q=\lfloor h/2\rfloor\). If \(h=1\), its only eigenvalue is \(a-1\). If \(h=2q\), its eigenvalues are \(a-1\) (multiplicity \(q\)), \(a+1\) (multiplicity \(q-1\)), and \(a+1-h\) (multiplicity one). If \(h=2q+1\ge3\), its eigenvalues are \(a-1\) (multiplicity \(q\)), \(a+1\) (multiplicity \(q-1\)), and \(a-q\pm\sqrt{q^2+1}\). The complete optimum value for every time, positive inverse order, and finite horizon is therefore obtained by substituting this finite eigenvalue list into the corresponding spectral sum.

## Assumptions and scope

The graph is simple, undirected, unweighted, and connected. The deleted edges form a fixed perfect matching; no other edge is deleted. Only the leader *locations* vary, and each leader is perfectly pinned. The number of followers \(h\) is fixed, and the grounded matrix is the principal submatrix of the *original* Laplacian, retaining its original degree diagonal. The term \(\mu I\) is uniform positive-semidefinite screening, not an adjustment to the graph's edges. Since \(k\ge1\), every grounded Laplacian is positive definite even when \(\mu=0\). At time zero, the heat traces all equal \(h\); the strict claim is only for \(t>0\). Every statement concerns finite graphs and finite positive horizons; no optimality claim is made for different graph families or different noise models.

## Proof

**1. A complete description of the leader-placement orbits.** Let \(r\) be the number of deleted matching pairs entirely in \(U\), and let \(s\) be the number of further pairs contributing exactly one follower. Then \(h=2r+s\) and \(\max\{0,h-m\}\le r\le\lfloor h/2\rfloor\). Because pair permutations and within-pair swaps are automorphisms, all choices with the same \((r,s)\) are equivalent. No other orbit invariant is needed. The number of sets in that orbit is \(\binom mr\binom{m-r}s2^s\).

**2. Strict single-step improvement at *every* time.** Suppose \(s\ge2\). Select followers \(u\) and \(v\) that are singletons of two different missing-edge pairs. The missing-edge mate \(u'\) of \(u\) is currently grounded. Replace \(v\) by \(u'\) among the followers. This keeps \(h\) fixed, increases \(r\) by one, and decreases \(s\) by two. Identify the new follower coordinates with the old coordinates by using the former coordinate of \(v\) for \(u'\). In the induced follower graph, the *only* changed adjacency is the previously present edge \(uv\), which becomes absent. All grounded diagonals remain \(2m-2+\mu\). Hence the new and old grounded matrices satisfy
\[
A_1=A_0+E_{uv}+E_{vu}.
\]
Consider \(A_\theta=A_0+\theta(E_{uv}+E_{vu})\) for \(0\le\theta\le1\). Both endpoints are positive definite grounded matrices, hence so is every convex combination \(A_\theta\). The off-diagonal entries of \(-A_\theta\) are nonnegative. For every \(0\le\theta<1\), its \((u,v)\) entry equals \(1-\theta>0\). The standard nonnegative power series for a shifted Metzler matrix therefore yields
\[
\big(e^{-tA_\theta}\big)_{uv}>0\qquad(t>0,\ 0\le\theta<1).
\]
The trace derivative of the matrix exponential is
\[
\frac{d}{d\theta}\operatorname{tr}(e^{-tA_\theta})
=-t\operatorname{tr}((E_{uv}+E_{vu})e^{-tA_\theta})
=-2t\big(e^{-tA_\theta}\big)_{uv}<0.
\]
Thus \(H_{t,\mu}\) decreases strictly under every such operation for *each* \(t>0\). Importantly, this is an off-diagonal, positive-semigroup comparison, not an unsupported Loewner comparison: \(E_{uv}+E_{vu}\) is indefinite.

**3. Strict hierarchy and all equality cases.** Every feasible \(r<\lfloor h/2\rfloor\) has \(s=h-2r\ge2\), so step 2 applies. Repeating until \(s\le1\) gives a strict chain for every time, with \(r\) increasing by one each step. Since all sets at any fixed \(r\) are automorphic, this gives the claimed *total strict ordering* of all orbits, not only the minimum. At the end, followers comprise as many full missing pairs as possible and at most one singleton. Complementing gives the stated completely grounded leader pairs and the exact counts from step 1. No other placements tie.

**4. Finite-horizon and all inverse orders.** Each grounded matrix is positive definite. For any \(p>0\), spectral calculus and the Euler gamma integral give
\[
\operatorname{tr}(A_S(\mu)^{-p})=\frac1{\Gamma(p)}\int_0^\infty t^{p-1}H_{t,\mu}(S)\,dt.
\]
The integral is finite, and the integrand is *strictly* smaller for the optimal orbit than for every other orbit at every \(t>0\). It therefore yields the same strict ranking for all \(p>0\). Integrating the positive-time comparison over \((0,T)\), with the change of variable \(t\mapsto2t\), proves the finite-horizon statement. More generally, any finite nonzero nonnegative time-weighted integral of \(H_{t,\mu}\), with positive weight at positive times, has the same strict optimizer.

**5. Exact spectral reproducibility.** With \(a=2m-1+\mu\), the full grounded matrix is \(aI-\mathbf1\mathbf1^{\mathsf T}+M_U\), where \(M_U\) exchanges the ends of the \(r\) complete missing-edge pairs and vanishes on the \(s\) singleton followers. For \(r\ge1\), its \(r\) antisymmetric within-pair modes have eigenvalue \(a-1\); its \(r-1\) pair-symmetric difference modes have eigenvalue \(a+1\); and, when \(s\ge1\), its \(s-1\) singleton-difference modes have eigenvalue \(a\). For \(r,s\ge1\), the remaining two-dimensional part is
\[
\begin{pmatrix}
a+1-2r & -\sqrt{2rs}\\
-\sqrt{2rs} & a-s
\end{pmatrix}.
\]
When \(s=0\) its remaining eigenvalue is \(a+1-2r\); when \(r=0\), the spectrum is \(a-h\) once and \(a\) with multiplicity \(h-1\). Taking \(r=\lfloor h/2\rfloor\), so \(s=0\) or \(1\), gives exactly the optimal spectra in the Finding. These formulas include all multiplicities and remain positive because the matrices are grounded positive definite. This finishes the proof.

## Verification

The included `verify.py` checks the claimed optimal spectra against numerical grounded-matrix diagonalizations for \(2\le m\le9\), every allowable budget, and screening values \(\mu\in\{0,0.3,7\}\). It enumerates all follower-pair composition orbits at several positive times and inverse spectral orders, and separately enumerates *every* leader subset for \(2\le m\le6\), verifying strict optimizer equality classification and multiplicities. An integer symbolic characteristic-polynomial computation checks all optimal spectra for \(2\le m\le6\). Its recorded run passed 7,401 assertions, broken down as 240 spectra, 960 inverse-order orbit checks, 720 heat-orbit checks, 5,446 subset checks and 35 exact characteristic-polynomial identities. These finite checks test computations and edge cases; the quantified theorem for all integers and all positive times is established by the proof, not by extrapolation. The checker requires Python 3, NumPy and SymPy.

## Relationship to prior work

The noise-free grounded-inverse trace objective occurs in the 2013 work of Lin, Fardad and Jovanović. The previously published *Exhaustive-community optimal leaders on balanced multipartite networks* proves the grouping conclusion for \(\operatorname{tr}(L_{UU}^{-1})\) on the larger family of balanced complete multipartite graphs; its \(n=2\) specialization (for \(m\ge3\)) is precisely the **first inverse-power, unscreened special case here**. The four-vertex case \(m=2\) is a cycle and is also covered by established cycle-based first-inverse methods. Neither that specialization nor its leader-count classification is claimed as new. The contribution here is the strictly stronger, *pointwise-in-time* hierarchy of **every placement orbit** for the heat semigroup, which gives simultaneous finite-horizon, screened and every-positive-inverse-order optimality. Knowing one inverse-trace inequality alone does not establish this heat-trace dominance. The earlier manuscript's full stated theorem and its rational Schur-complement proof were checked for this implication; no pointwise heat-order statement appeared. The path/cycle and general joint-centrality studies cited below concern other graph families or the first inverse moment, and do not provide the strict all-time hierarchy on this network. Searches for the corresponding heat-trace, transient-coherence, pair-completion, spectral-order and matching-complement formulations found no directly covering statement in inspected accessible sources.

## Limitations

This is an exact mathematical theorem under the stated complete-minus-matching, fixed-degree grounded-Laplacian, perfect-leader assumptions. It does not address arbitrary graphs, nonsymmetric transition kernels, variable degrees, arbitrary edge weights, imperfect leaders or optimizers for a different norm such as worst-case spectral radius. The theorem does not imply a Loewner ordering of grounded matrices. Finite tests are supplementary rather than independent verification of the infinite-domain argument. Primary-literature searches and comparisons cannot exclude every unindexed or differently formulated prior publication; independent audit has not been performed.

## References

1. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, initially public February 3, 2013, https://arxiv.org/abs/1302.0450.
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, initially public July 7, 2014, https://arxiv.org/abs/1407.1569.
3. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, initially public December 20, 2014, https://arxiv.org/abs/1412.6595.
4. *Exhaustive-community optimal leaders on balanced multipartite networks*, complete published RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exhaustive-community-optimal-leaders-on-balanced-multipartite-ne--fb8c09cd8e4e.
