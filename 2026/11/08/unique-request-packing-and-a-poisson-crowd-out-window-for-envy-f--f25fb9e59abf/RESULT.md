# Unique-request packing and a Poisson crowd-out window for envy-free complementary allocations

## Finding

**Theorem (unique-request packing, computational boundary, and stochastic crowd-out).** Let \(m\ge r\ge2\) and \(n\ge m\) be integers. There are \(m\) distinct indivisible goods, exactly one copy of each, and \(n\) agents. Agent \(i\) demands exactly an \(r\)-element set \(D_i\) and has binary perfect-complements utility \(v_i(B)=\mathbf 1\{D_i\subseteq B\}\). Every good must be allocated to one agent, with no money. Write \(W\) for the maximum utilitarian welfare among **complete envy-free allocations**. Let \(H\) be the \(r\)-uniform hypergraph on the goods whose edges are precisely those demand sets reported by *exactly one* agent; let \(\nu(H)\) be its maximum pairwise-disjoint edge-packing size. Then

\[
W=\nu(H).
\]

Thus the optimum and an attaining complete envy-free allocation are computable in polynomial time for \(r=2\) via ordinary graph matching. For each fixed \(r\ge3\), the corresponding welfare-threshold decision problem is NP-complete even under these unit-supply, equal-request-size, many-agent assumptions.

If the \(n\) demand sets are independently uniform among the \(M=\binom mr\) possible sets, then for every finite \(m,n,r\) with \(n\ge m\), \(W=0\) precisely when no demand set is requested exactly once. In particular,

\[
\Pr(W=0)=\sum_{j=0}^{\min(M,n)}(-1)^j\binom Mj\frac{(n)_{\underline j}}{M^j}\left(1-\frac jM\right)^{n-j}.
\]

Fix an integer \(r\ge2\) and a real \(t\). If \(m\to\infty\) and integers \(n=n_m\) satisfy

\[
\frac nM-\log M-\log\log M\longrightarrow t,\qquad M=\binom mr,
\]

then the optimum welfare obeys the **full Poisson limit**

\[
W\ \xrightarrow{d}\ \operatorname{Poisson}(e^{-t}),\qquad
\mathbb EW\longrightarrow e^{-t},\qquad
\Pr(W=0)\longrightarrow \exp(-e^{-t}).
\]

This is a sharp threshold: with \(n/M=\log M+\log\log M+t_m\) and \(|t_m|=o(\log M)\), the probability of positive envy-free welfare tends to one if \(t_m\to-\infty\), and to zero if \(t_m\to+\infty\). Thus adding demanders eventually **eliminates** all positive envy-free welfare in the crowded regime, independently of every fixed complement size \(r\ge2\).

## Assumptions and scope

A complete allocation is an ordered partition \((A_1,\ldots,A_n)\) of the \(m\) labeled goods, with empty bundles permitted. Envy-freeness means \(v_i(A_i)\ge v_i(A_j)\) for every pair of agents \(i,j\). Welfare is \(\sum_i v_i(A_i)\), so each fully satisfied agent contributes exactly one. A good outside an agent's requested set has zero marginal value for that agent. The agents have no monetary payments, and there is one copy of each good. The large-agent hypothesis \(n\ge m\) permits unused goods to be parked separately without completing another demand. In the random model, only agents' demand sets are random; the mechanism may optimize after observing the entire profile.

Demand vectors with zero components for goods outside \(D_i\) are explicitly permitted here. This is a restricted zero-demand variant of indivisible Leontief preferences, not the positive-demand-for-every-good domain of the initiating paper. The stochastic result concerns the *maximum over envy-free allocations*, not a prescribed online mechanism or a uniformly drawn allocation.

## Proof

**1. Every satisfied demand is unique.** If two agents require the same set \(D\), at most one can receive all goods of \(D\), because there is only one copy of each. Were one of them satisfied, the other would receive utility zero but would value the first one's bundle at one, violating envy-freeness. Therefore nobody with a repeated demand set can be satisfied in an envy-free allocation.

**2. Satisfied sets form a packing.** For distinct satisfied agents, their requested sets must be contained in their disjoint allocated bundles and hence are pairwise disjoint. By Step 1 they are all edges of \(H\). Therefore every complete envy-free allocation has welfare at most \(\nu(H)\).

**3. Every packing can be realized envy-freely.** Choose \(k\) disjoint unique-request edges of \(H\). Give each of these \(r\)-item sets, unchanged, to its unique requesting agent. Distribute each of the remaining \(m-rk\) goods as a singleton bundle to a different one of the other \(n-k\) agents, and give the remaining agents empty bundles. This is possible since \(n-k\ge m-rk\), a consequence of \(n\ge m\) and \(r\ge2\). All \(k\) selected agents get utility one and cannot envy anyone. Every unselected agent's own bundle is a singleton or empty and hence has utility zero. No other agent's bundle fulfills this agent's demand: each selected bundle is an \(r\)-set with a *unique* requester, and every other nonempty bundle is a singleton of size strictly less than \(r\). Thus no agent envies any other. The allocation is complete and has welfare \(k\). Taking \(k=\nu(H)\) proves \(W=\nu(H)\).

**4. Algorithmic boundary.** For \(r=2\), \(H\) is a simple undirected graph and \(\nu(H)\) is its maximum matching cardinality, computable by Edmonds' polynomial-time matching algorithm. To prove hardness for \(r=3\), begin with a 3-dimensional matching instance consisting of distinct triples on a ground set of size \(m_0\). Make one requester for each triple. Add three new dummy goods and \(L\) dummy requesters all demanding exactly these same three goods, with \(L\ge\max(2,m_0+3-|E|)\). The dummy request occurs at least twice, so the unique-demand hypergraph consists exactly of the original triples; moreover \(n=|E|+L\ge m_0+3=m\). Step 3 makes optimum envy-free welfare equal to the original maximum 3-dimensional matching size. The construction is polynomial. For every fixed \(r>3\), give each original triple \(r-3\) fresh private goods to create an \(r\)-set; the packing optimum is unchanged. Then pad with at least two dummy requesters for one new disjoint \(r\)-set, choosing the dummy count large enough that \(n\ge m\). The decision problem is in NP because completeness, welfare and all pairwise envy inequalities are directly checkable in polynomial time. This establishes NP-completeness for every fixed \(r\ge3\).

**5. Exact singleton counting.** In the uniform random model, let \(S\) be the number of demand sets sampled exactly once, or equivalently the number of edges of \(H\). Step 3 implies \(W=0\) if and only if \(S=0\). For \(0\le j\le\min(M,n)\), the probability that each of \(j\) specified distinct sets is requested exactly once equals

\[
\frac{(n)_{\underline j}}{M^j}\left(1-\frac jM\right)^{n-j},
\]

where \((a)_{\underline j}=a(a-1)\cdots(a-j+1)\) and \((a)_{\underline0}=1\). Inclusion-exclusion over singleton-occupancy events gives the finite formula displayed in the finding.

**6. Poisson singleton law.** The factorial moments are

\[
\mathbb E(S)_{\underline j}=(M)_{\underline j}\frac{(n)_{\underline j}}{M^j}\left(1-\frac jM\right)^{n-j}.
\]

For fixed \(j\) and \(n/M=\log M+\log\log M+t+o(1)\), taking logarithms and using \(n/M^2=o(1)\) gives

\[
\mathbb E(S)_{\underline j}
=\left[M\frac nM e^{-n/M}\right]^j(1+o(1))\longrightarrow e^{-jt}.
\]

The factorial-moment characterization of the Poisson law therefore proves \(S\xrightarrow{d}\operatorname{Poisson}(e^{-t})\), as well as \(\mathbb ES\to e^{-t}\).

**7. Singleton sets are asymptotically disjoint.** Let \(C\) count unordered pairs of intersecting edges in \(H\). The number of unordered intersecting pairs among all possible \(r\)-sets is

\[
\frac M2\left(M-1-\binom{m-r}{r}\right),
\]

with the convention that a binomial coefficient is zero when its top entry is smaller than its bottom entry. Consequently,

\[
\mathbb EC=
\frac M2\left(M-1-\binom{m-r}{r}\right)
\frac{n(n-1)}{M^2}\left(1-\frac2M\right)^{n-2}.
\]

For fixed \(r\), the fraction of intersecting pairs of random distinct \(r\)-sets is \(O(1/m)\). The exact two-singleton probability is \(O(1/M^2)\) in the critical window. Hence \(\mathbb EC=O(1/m)\to0\). Deleting at most one selected edge per intersecting pair produces a packing, so \(S-C\le W\le S\). Therefore \(\Pr(W\ne S)\le\mathbb EC\to0\) and \(0\le\mathbb ES-\mathbb EW\le\mathbb EC\to0\). Combining with Step 6 proves the Poisson distribution and mean limits for \(W\), and hence its zero-welfare probability.

**8. The one-sided threshold.** If \(n/M=\log M+\log\log M+t_m\) with \(|t_m|=o(\log M)\), then \(\mathbb ES\sim e^{-t_m}\). If \(t_m\to+\infty\), Markov's inequality gives \(\Pr(W>0)\le\mathbb ES\to0\). If \(t_m\to-\infty\), the exact first two factorial moments in Step 6 imply \(\mathbb E(S)_{\underline2}/(\mathbb ES)^2\to1\), so \(\operatorname{Var}(S)/(\mathbb ES)^2\to0\); Chebyshev's inequality gives \(\Pr(S=0)\to0\). Since \(W>0\) exactly when \(S>0\), this proves the claimed sharp transition.

## Verification

The standalone file `verification/checker.py` implements two independently constructed finite procedures: complete enumeration of all allocations followed by literal envy and welfare tests, and exact maximum packing of the uniquely occurring requests. Their answers agree on 10,862 demand profiles, including exhaustive profiles for \((m,r,n)=(4,2,5)\) and \((4,3,5)\), plus seeded larger cases. A separate direct occupancy enumeration agrees with the inclusion-exclusion and falling-factorial moment identities for six finite parameter pairs. Execute `python3 verification/checker.py` from the extracted package directory. This finite verification does not establish NP-hardness or any infinite-limit theorem; those follow from Steps 1–8.

## Relationship to prior work

Inamdar, Jain and Pandey (2026) introduce welfare maximization for complete envy-free indivisible Leontief allocations and prove general intractability together with polynomial algorithms for identical demands and single-good instances. Their publicly available introduction and contribution summary do not state the unique-demand packing identity, the fixed complement-cardinality complexity boundary, or the stochastic welfare collapse. Importantly, the present claim allows zero demand outside a set of \(r\) goods, whereas that paper's main positive-demand regime differs; a secondary overview explicitly flags zero-demand generalization as a further direction. This is a domain distinction, not a novelty proof.

The polynomial matching theorem of Edmonds, the classical NP-completeness of 3-dimensional matching, and elementary occupancy factorial moments are used as established components. The new claim is their exact, envy-freeness-preserving connection under complete allocation and the resulting welfare distribution. The ``envy-free matching'' of Aigner-Horev and Segal-Halevi concerns one-object assignments in a bipartite agent-item graph; it is not the packing of complementary \(r\)-item demands considered here. Search-based novelty checks are nonexhaustive.

## Limitations

The equality requires equal request cardinality at least two, unit supply, complete allocation, binary perfect complements, and at least as many agents as goods. It does not claim that arbitrary Leontief instances, positive-demand-for-all-goods instances, or arbitrary multiplicities of goods are polynomial-time solvable. The Poisson law holds for fixed \(r\) and independent uniform request sets at the specified logarithmic occupancy window; dependence, nonuniform demands, growing \(r\), and prescribed online allocation mechanisms are not covered. Full primary-text access for the initiating 2026 preprint was unavailable beyond its summary/introduction material during this comparison; unindexed or inaccessible coverage remains a publication-priority risk.

## References

1. T. Inamdar, P. Jain, and P. Pandey, *Envy-Free Allocation of Indivisible Goods under Leontief Preferences*, arXiv:2609.28308, first submitted 23 September 2026. https://arxiv.org/abs/2609.28308
2. E. Aigner-Horev and E. Segal-Halevi, *Envy-free Matchings in Bipartite Graphs and their Applications to Fair Division*, arXiv:1901.09527 (2019). https://arxiv.org/abs/1901.09527
3. J. Edmonds, *Paths, Trees, and Flowers*, Canadian Journal of Mathematics 17 (1965), 449–467. https://doi.org/10.4153/CJM-1965-045-4
4. R. M. Karp, *Reducibility Among Combinatorial Problems*, in *Complexity of Computer Computations* (1972), 85–103. https://doi.org/10.1007/978-1-4684-2001-2_9
5. M. Cygan, *Improved Approximation for 3-Dimensional Matching via Bounded Pathwidth Local Search*, arXiv:1304.1424 (2013); background on 3-set packing hardness. https://arxiv.org/abs/1304.1424
6. A. D. Barbour and A. V. Gnedin, *Small Counts in the Infinite Occupancy Scheme*, arXiv:0809.4387 (2008); related occupancy-count literature. https://arxiv.org/abs/0809.4387
