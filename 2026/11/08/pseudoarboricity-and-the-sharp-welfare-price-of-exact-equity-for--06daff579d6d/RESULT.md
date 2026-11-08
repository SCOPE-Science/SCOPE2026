# Pseudoarboricity and the sharp welfare price of exact equity for two-sparse binary allocations

## Finding

Let \(n\ge3\) and \(D\ge2\) be integers. In a complete allocation of indivisible goods among \(n\) agents with additive binary valuations, assume that every agent approves exactly \(D\) goods and every good is approved by either one or two agents. Write \(G\) for the loopless multigraph whose edges are the goods approved by two agents; singleton-approved goods are not edges. For nonempty \(S\subseteq N\), let \(e_G(S)\) count edges with both endpoints in \(S\), with multiplicity, and put

\[
\lambda(G)=\left\lceil\max_{\varnothing\ne S\subseteq N}\frac{e_G(S)}{|S|}\right\rceil,
\qquad t_*=D-\lambda(G).
\]

**Exact-equity theorem.** The largest common realized utility in any exactly equitable (EQ) complete allocation is exactly \(t_*\). An EQ allocation achieving this optimum also satisfies envy-freeness up to one good (EF1), and can be found by integral bipartite matching. Thus the maximum utilitarian welfare subject to EQ equals that subject to simultaneous EQ and EF1, namely \(nt_*\). In particular, \(t_*\ge\lfloor D/2\rfloor\ge1\).

**Sharp welfare-price spectrum.** Let \(m\) be the number of goods (every good has a positive-value recipient). Unrestricted maximum utilitarian welfare is \(m\). For fixed \(n,D\) and fixed \(\lambda=\lambda(G)\), the maximal possible price of imposing simultaneous EQ and EF1 is

\[
\sup_{\lambda(G)=\lambda}\frac{m}{n(D-\lambda)}=
\begin{cases}
1,&\lambda=0,\\
\displaystyle\frac{nD-2\lambda+1}{n(D-\lambda)},&1\le\lambda\le\lceil D/2\rceil.
\end{cases}
\]

Every displayed supremum is attained. Maximizing over all permitted profiles gives the **sharp** fixed-\((n,D)\) price

\[
\boxed{\frac{nD-2\lceil D/2\rceil+1}{n\lfloor D/2\rfloor}}.
\]

The two-support restriction allows arbitrary non-laminar approval intersections, arbitrary edge multiplicities, and any number of agents.

## Assumptions and scope

A good \(g\) has approval set \(T_g=\{i:v_i(\{g\})=1\}\), with \(1\le|T_g|\le2\). Every \(i\) has \(\sum_gv_i(\{g\})=D\). An allocation is an exhaustive partition \((A_i)_{i\in N}\) of the labeled goods. Write \(u_i=v_i(A_i)\). EQ means all \(u_i\) are equal. EF1 means that, for each distinct \(i,j\), either \(v_i(A_i)\ge v_i(A_j)\) or there is a good \(g\in A_j\) for which \(v_i(A_i)\ge v_i(A_j\setminus\{g\})\). Zero-valued transfers are allowed; Pareto efficiency and non-wastefulness are **not** assumed. All bounds are for integer \(n\ge3,D\ge2\) and are not statements for arbitrary valuations or for support size three.

## Proof

**1. Exact level from generalized Hall.** Let \(N(S)=\{g:T_g\cap S\ne\varnothing\}\). To give every agent at least \(t\) *different approved* goods, create \(t\) copies of each agent and match each copy to an approved good. Hall's theorem (or an integral unit-capacity flow) shows this is possible exactly when \(|N(S)|\ge t|S|\) for every nonempty \(S\subseteq N\). Necessity is immediate because goods cannot be assigned twice. Conversely, after matching all \(nt\) copies, give each unmatched good to an agent outside \(T_g\). Such an agent exists because \(n\ge3\) and \(|T_g|\le2\). Therefore all realized utilities are **exactly** \(t\), not merely at least \(t\). Hence

\[
t_*=\min_{\varnothing\ne S\subseteq N}\left\lfloor\frac{|N(S)|}{|S|}\right\rfloor.
\]

Each approved good touching \(S\) is counted once in \(|N(S)|\), whereas the sum of approvals over agents in \(S\) counts exactly one extra occurrence for every double-approved good internal to \(S\). Consequently

\[
|N(S)|=D|S|-e_G(S),\qquad
\left\lfloor\frac{|N(S)|}{|S|}\right\rfloor
=D-\left\lceil\frac{e_G(S)}{|S|}\right\rceil.
\]

Minimizing yields \(t_*=D-\lambda(G)\). Since the degree of every vertex in \(G\) is at most \(D\), \(2e_G(S)\le D|S|\), so \(\lambda(G)\le\lceil D/2\rceil\), establishing \(t_*\ge\lfloor D/2\rfloor\).

**2. EF1 at no extra welfare loss.** In any exactly equitable allocation with utility \(t\), agent \(i\) values \(D\) goods in total and receives \(t\) of them. Thus, for any \(j\ne i\),

\[
v_i(A_j)\le D-t.
\]

Whenever \(t\ge\lfloor D/2\rfloor\), \(D-t\le t+1\). If \(i\) envies \(j\), this inequality says \(v_i(A_j)=t+1\); there must be a positively valued good in \(A_j\), whose removal reduces that value to \(t\). The allocation is EF1. In particular, every EQ allocation at the maximal common level \(t_*\) is EF1. Its welfare is \(nt_*\), and no EQ allocation can have greater welfare by step 1.

**3. Conditional welfare envelope.** Write \(m_2=e_G(N)\) for the number of double-approved goods. Double counting approval incidences gives \(nD=m+m_2\). Fix \(\lambda(G)=\lambda\ge1\). Some nonempty \(S\) satisfies \(e_G(S)>(\lambda-1)|S|\). Since \(G\) is loopless, this \(S\) has \(|S|\ge2\); integrality then gives

\[
m_2\ge e_G(S)\ge (\lambda-1)|S|+1\ge2\lambda-1.
\]

It follows that \(m\le nD-(2\lambda-1)\). The bound is attained as follows: choose two agents sharing exactly \(b=2\lambda-1\) goods, add \(D-b\) singleton-approved goods for each of the two, and add \(D\) singleton-approved goods for each remaining agent. This is valid because \(b\le D\) whenever \(\lambda\le\lceil D/2\rceil\). The multigraph is just two vertices joined by \(b\) parallel edges, hence \(\lambda(G)=\lceil b/2\rceil=\lambda\). It has \(m=nD-b\) goods, proving equality in the price formula. If \(\lambda=0\), no good is double approved, and both welfare optima equal \(m=nD\).

**4. Global sharp price.** For \(\lambda\ge1\), the envelope can be written

\[
\frac{nD-2\lambda+1}{n(D-\lambda)}
=\frac2n+\frac{(n-2)D+1}{n(D-\lambda)}.
\]

It is strictly increasing in the integer \(\lambda\) for \(n\ge3\). Therefore the maximum occurs at \(\lambda=\lceil D/2\rceil\), producing the boxed formula. The construction in step 3 attains it. This completes the proof.

## Verification

Run `python3 verify.py` using Python 3 and no third-party dependencies. It checks the Hall/graph-density formula, constructs the exact-EQ allocation via an independent augmenting-path matcher, verifies utilities and literal EF1 inequalities, and evaluates the sharp price envelopes for all unlabeled multiplicity patterns at \((n,D)=(3,2),(3,3),(3,4),(4,2),(4,3)\), totaling 346 profiles. It also independently brute-forces complete assignments on 51 sampled profiles, tests the extremal family, and checks every feasible density layer for additional sample sizes. All tests passed in the supplied run. The infinite claims follow from the proof, **not** from finite enumeration.

## Relationship to prior work

Hosseini, Pathak, Xia and Zhang (2026, arXiv:2608.26410, first public August 26, 2026) study EF1 and EQ1 compatibility and report a seven-agent guarantee for general normalized binary goods and an arbitrary-agent guarantee under laminar approvals. Here the domain is instead bounded *per-good approval support*, allowing non-laminar patterns at unbounded agent count, and the stronger target is exact EQ plus EF1 with optimal EQ welfare and an exact price formula. This statement is not implied by the reported seven-agent result or the laminar restriction. The primary paper's complete text was not accessible for full appendix comparison, which remains an originality risk.

Bhaskar, Misra, Sethia and Vaish (2023, arXiv:2307.06726) analyze the price of **EQ1** for binary valuations and generalized welfare metrics; the theorem here concerns **exact EQ**, simultaneous EF1, a two-sparse approval domain, and its sharp density-resolved welfare price. The graph parameter \(\lambda(G)\) is the classical pseudoarboricity, already characterized by density and minimum-maximum-indegree orientations; this graph identity itself is **not claimed as novel** (see Blumenstock, 2016). The mathematical contribution proposed here is the fair-division compatibility and extremal welfare classification obtained from that invariant.

## Limitations

The construction deliberately allows some goods to be allocated to nonapprovers, so the guarantee is not Pareto efficiency, nonwastefulness, or the stronger all-goods version of EFX. The \(D=1\) case is excluded: with two agents sharing their sole approved good and all remaining agents each approving a private good, maximum exact-EQ welfare is zero. The two-support condition and equal approved degree are essential to the stated guarantee; no assertion is made for goods approved by three or more agents. The novelty conclusion is provisional in light of inaccessible full text of the most closely related 2026 source and possible unindexed equivalents. There is no independent scientific validation.

## References

1. H. Hosseini, S. Pathak, L. Xia, C. Zhang, *Simultaneous Envy and Equitability Guarantees*, arXiv:2608.26410 (2026), https://arxiv.org/abs/2608.26410 ; public result table: https://thelatestinai.com/papers/2608.26410 .
2. U. Bhaskar, N. Misra, A. Sethia, R. Vaish, *The Price of Equity with Binary Valuations and Few Agent Types*, arXiv:2307.06726 (2023), https://www.alphaxiv.org/abs/2307.06726 .
3. M. Blumenstock, *Fast Algorithms for Pseudoarboricity*, ALENEX (2016), https://doi.org/10.1137/1.9781611974317.10 .
4. P. Hall, *On Representatives of Subsets*, J. London Math. Soc. (1935). Generalized Hall matching follows by replacing each demanded agent with copies.
