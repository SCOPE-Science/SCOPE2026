# Poisson crowd-out for complete envy-free allocations with fixed-size complementary demands

## Finding

**Theorem (Poisson law for the optimal envy-free welfare).** Fix an integer \(r\ge2\). For each \(m\ge r\), let \(n=n_m\ge m\) agents independently choose a uniformly random \(r\)-element subset \(D_i\) of \([m]\). Each good has one indivisible copy, each agent receives a (possibly empty) bundle, every good must be assigned, payments are disallowed, and \(v_i(A)=\mathbf1\{D_i\subseteq A\}\). Let \(W_m\) be the maximum welfare over all complete envy-free allocations. Put \(M=\binom mr\).

If \(n/M-\log M-\log\log M\to t\in\mathbb R\), then
\[
W_m\xrightarrow{d}\operatorname{Poisson}(e^{-t}),\qquad
\mathbb EW_m\to e^{-t},\qquad
\Pr(W_m=0)\to \exp(-e^{-t}).
\]
In the one-sided windows \(n/M=\log M+\log\log M+t_m\), \(|t_m|=o(\log M)\), positive welfare has probability tending to one if \(t_m\to-\infty\) and to zero if \(t_m\to+\infty\).

The bridge from occupancy to fair-allocation welfare is quantitative. Let \(S_m\) be the number of request types occurring exactly once and \(C_m\) the number of intersecting unordered pairs among those uniquely requested \(r\)-sets. For every finite admissible \((m,n,r)\),
\[
S_m-C_m\le W_m\le S_m,\quad
 d_{\rm TV}(\mathcal L(W_m),\mathcal L(S_m))\le \Pr(W_m\ne S_m)\le \mathbb EC_m,
\]
where
\[
\mathbb EC_m=\frac{M}{2}\left(M-1-\binom{m-r}{r}\right)
\frac{n(n-1)}{M^2}\left(1-\frac2M\right)^{n-2}.
\]
In the stated fixed-\(t\) critical window this bound is \(O_r(1/m)\). In particular the Poisson limit describes the *optimal fair welfare*, not just the number of singly occupied bins. For finite \((m,n,r)\) the zero-welfare event is exactly \(\{S_m=0\}\), and hence
\[
\Pr(W_m=0)=\sum_{j=0}^{\min(M,n)}(-1)^j\binom Mj
 \frac{(n)_{\underline j}}{M^j}\left(1-\frac jM\right)^{n-j}.
\]

The deterministic structural fact used below is the identity \(W=\nu(H)\), where \(H\) is the hypergraph of uniquely requested \(r\)-sets and \(\nu(H)\) is its disjoint-edge packing number. **This identity and the consequent matching-versus-set-packing computational boundary are not presented as independent novelty:** the zero-payment specialization of the known single-minded envy-free auction characterization already supplies its core winner/loser condition. The distinct contribution asserted here is the application to the full stochastic optimum, especially the quantitative hyperedge-intersection transfer. The occupancy-window law itself is classical in the double-Dixie-cup/coupon-collection setting.

## Precise definitions and finite bridge

A complete allocation is an ordered partition \((A_1,\dots,A_n)\) of \([m]\) (empty parts allowed). It is envy-free if \(v_i(A_i)\ge v_i(A_j)\) for all \(i,j\). Let \(H\) have an edge \(D\) exactly if one agent demands \(D\). Any satisfied agent with a duplicate request would cause envy for the other identical requester, so satisfied demand sets are unique. They are disjoint by unit supply; hence \(W\le\nu(H)\).

Conversely, for any \(k\)-edge packing in \(H\), allocate each selected \(r\)-set to its unique requester, then allocate each of the remaining \(m-rk\) goods as a singleton to a distinct unselected agent. This is feasible because \(n-k\ge m-rk\) follows from \(n\ge m\) and \(r\ge2\). Give the rest empty bundles. Every selected agent is satisfied; no losing agent desires another single-item bundle (\(r\ge2\)) or one of the selected bundles (each has a different unique requester and the same size \(r\)). This is complete and envy-free with welfare \(k\), establishing \(W=\nu(H)\). This elementary parking argument reconciles the classical no-payment single-minded winner condition with *complete* allocation.

If \(S\) edges of \(H\) are occupied exactly once, delete from their family at most one edge for each intersecting pair. The remaining edges form a packing of size at least \(S-C\). Thus \(S-C\le W\le S\), and \(W=0\) if and only if \(S=0\). A coupling of \(W,S\) on the same demand profile gives the total-variation and expectation-gap bounds in the finding.

## Occupancy calculations and asymptotic proof

For any fixed \(j\le \min(M,n)\), the chance that each of \(j\) prescribed types appears exactly once among \(n\) independent uniform requests is
\[
 p_j=\frac{(n)_{\underline j}}{M^j}\left(1-\frac jM\right)^{n-j}.
\]
Consequently \(\mathbb E(S)_{\underline j}=(M)_{\underline j}p_j\); inclusion-exclusion over singleton-type events yields the stated exact \(\Pr(S=0)\). For fixed \(j\), \(n/M=\log M+\log\log M+t+o(1)\) implies \(n/M^2\to0\) and
\[
\mathbb E(S)_{\underline j}
 =\left[M(n/M)e^{-n/M}\right]^j(1+o(1))\longrightarrow e^{-jt}.
\]
The Poisson factorial-moment criterion gives \(S\Rightarrow\operatorname{Poisson}(e^{-t})\) and its mean converges by the \(j=1\) identity.

Among \(M\) possible \(r\)-edges, exactly \(\frac M2(M-1-\binom{m-r}{r})\) unordered pairs intersect. Multiplying by \(p_2\) gives the exact \(\mathbb EC\) formula. For fixed \(r\), \([M-1-\binom{m-r}{r}]/M=O_r(1/m)\); in the critical window \(p_2=O(M^{-2})\), uniformly for fixed \(t\). Therefore \(\mathbb EC=O_r(1/m)\to0\). The coupling bound transfers the entire distribution and expectation from \(S\) to \(W\), proving the three limits.

For \(t_m\to+\infty\) with \(|t_m|=o(\log M)\), the exact first moment obeys \(\mathbb ES\sim e^{-t_m}\to0\), and \(\Pr(W>0)=\Pr(S>0)\le\mathbb ES\to0\). For \(t_m\to-\infty\), the first and second factorial-moment formulas give \(\mathbb ES\sim e^{-t_m}\to\infty\) and \(\mathbb E(S)_{\underline2}/(\mathbb ES)^2\to1\). Thus \(\operatorname{Var}(S)/(\mathbb ES)^2\to0\) and \(\Pr(W=0)=\Pr(S=0)\to0\).

## Classical algorithmic consequences (not originality claims)

For a fixed realized profile, \(r=2\) reduces the welfare maximization problem to ordinary maximum graph matching after deleting repeated request types. At any fixed \(r\ge3\), the corresponding decision problem is NP-complete by reducing 3-dimensional matching to the unique-demand hypergraph: request each original triple once, pad with a duplicated dummy request on fresh goods to ensure \(n\ge m\), and for \(r>3\) pad original triples with private goods. Exact welfare equality preserves the maximum packing size; membership in NP is immediate by checking allocations and envy. These are direct uses of classical graph matching and set-packing results, not novel complexity-theoretic reductions.

## Verification and scope

A separately implemented finite verification explicitly enumerated all complete assignments and checked all envy inequalities on 1,661 demand profiles for small \((m,r,n)\), recovering the packing identity in each case. Four exact finite occupancy calculations independently matched the zero-welfare formula and expected singleton count. Such finite tests do not prove the unrestricted theorem. The analytic steps above provide the general argument. The package's original `verification/checker.py` and external-verification channels are preserved unchanged.

The conclusion needs equal fixed request cardinality \(r\ge2\), one copy of each good, no payments, full allocation, \(n\ge m\), and independent uniform request types; it does not address positive Leontief demand for every good, nonuniform or dependent profiles, variable \(r\), or online allocations. The Poisson law is an exact asymptotic statement for the optimal fair welfare, *not* a new coupon-collector Poisson theorem in isolation.

## Relationship to prior mathematics and priority limitations

Fiat and Wingarten (2009), *Envy, Multi Envy, and Revenue Maximization*, Section 4.1, Observation 5, characterize winners and losers for single-minded envy-free auction allocations under prices. Setting all prices to zero and fixing equal positive valuations and request sizes forces any satisfied demand to be uniquely requested; unit supply requires disjoint winners. With enough agents to park leftover goods, the deterministic packing identity follows. The current proof states the parking implication explicitly, but does not claim historical priority for the identity or for graph matching/NP-completeness.

The double-Dixie-cup result of Newman–Shepp and the fixed-multiplicity coupon-collector limit law of Erdős–Rényi establish the classical \(M\log M+M\log\log M\) occupancy window. The above result additionally compares the maximum size of an envy-free packing of uniquely occupied *overlapping* \(r\)-sets to that classical count and controls the difference. No checked source was found establishing this exact welfare comparison in the specified full-allocation model. A stronger unindexed random-hypergraph matching theorem or single-minded allocation result could still imply it; novelty is therefore best-of-knowledge, not independently certified.

Inamdar, Jain and Pandey (2026), *Envy-Free Allocation of Indivisible Goods under Leontief Preferences*, address general Leontief envy-freeness and welfare optimization, principally with strictly positive demands across goods. Its abstract/introduction and stated results were checked, but full primary text could not be retrieved in this audit (despite lawful retrieval attempts). Noncoverage is asserted only for the material inspected; the omitted sections remain a concrete priority risk. Aigner-Horev and Segal-Halevi's bipartite envy-free matchings assign one object per agent, not complementary bundles. The verified classical results and this remaining source-access risk must accompany any later publication claim.

## References

1. A. Fiat and A. Wingarten, *Envy, Multi Envy, and Revenue Maximization* (2009), arXiv:0909.4569, especially Observation 5. https://arxiv.org/abs/0909.4569
2. D. J. Newman and L. Shepp, *The Double Dixie Cup Problem*, American Mathematical Monthly 67 (1960), 58–61.
3. P. Erdős and A. Rényi, *On a classical problem of probability theory*, Magyar Tud. Akad. Mat. Kutató Int. Közl. 6 (1961), 215–220.
4. T. Inamdar, P. Jain and P. Pandey, *Envy-Free Allocation of Indivisible Goods under Leontief Preferences*, arXiv:2609.28308 (2026). https://arxiv.org/abs/2609.28308
5. E. Aigner-Horev and E. Segal-Halevi, *Envy-free Matchings in Bipartite Graphs and their Applications to Fair Division*, arXiv:1901.09527 (2019). https://arxiv.org/abs/1901.09527
6. J. Edmonds, *Paths, Trees, and Flowers*, Canadian Journal of Mathematics 17 (1965), 449–467. https://doi.org/10.4153/CJM-1965-045-4
7. R. M. Karp, *Reducibility Among Combinatorial Problems*, in *Complexity of Computer Computations* (1972), 85–103.
