# Comparison shattering for linear extensions of finite posets

## Finding
Let \(P=(X,<_{P})\) be an arbitrary finite strict poset with \(|X|=n\). Let \(\mathcal L(P)\) be the binary concept class consisting of every linear extension of \(P\), queried by an unordered distinct pair \(\{a,b\}\subset X\), with answer \(1\) meaning \(a\) precedes \(b\) under a fixed canonical ordering of each queried pair. A support \(S\subseteq\binom X2\) is shattered by \(\mathcal L(P)\) if and only if the following conditions hold simultaneously:

1. The undirected query graph \(F=(X,S)\) is a forest, including its isolated vertices.
2. Every connected component of \(F\) is an antichain of \(P\).
3. The directed multigraph \(Q\), with one vertex per component of \(F\) and an arc \(C\to D\) whenever \(C\ne D\) and there exist \(c\in C,d\in D\) with \(c<_{P}d\), is acyclic.

Consequently, writing \(h(P)\) for the maximum number of elements in a chain (and \(h(\varnothing)=0\)), the exact VC dimension is
\[
\operatorname{VCdim}(\mathcal L(P))=n-h(P).
\]
This holds for every finite poset, including an empty or total poset. In particular, although counting linear extensions remains \(\#\mathrm P\)-complete even for height-two posets, the VC dimension in this comparison model is computable from a precedence DAG by a longest-path dynamic program in \(O(n+m)\) time, where \(m\) is the number of input arcs.

## Assumptions and scope
A linear extension is a strict total order containing each relation of \(P\). A comparison support is a set of *distinct* unordered pairs; its answer vector records their relative order in an extension. Shattering requires all \(2^{|S|}\) answer vectors, with no distribution or independence assumption. The graph \(F\) includes all elements of \(X\) even if they do not appear in queries. An antichain contains no comparable distinct elements. In the quotient test all strict comparabilities of \(P\) between components are used, not merely covering relations; reachability yields the same quotient after transitive closure. The theorem is about VC dimension, not Littlestone dimension or the cost of identifying a linear extension adaptively.

## Proof
**Step 1, forest obstruction.** If \(F\) has a cycle, orient the comparisons on its edges cyclically and assign any answers to other queries. No strict total order can realize the cyclic comparisons. Hence a shattered support is a forest.

**Step 2, antichain obstruction.** Suppose \(F\) is a forest and some component contains \(a<_{P}b\). The unique \(F\)-path from \(b\) to \(a\) can be oriented as \(b\prec\cdots\prec a\). This answer pattern contradicts the fixed poset relation \(a<_{P}b\). Thus every component must be a \(P\)-antichain.

**Step 3, quotient obstruction.** Assume the first two conditions, but that \(Q\) contains a directed simple cycle of components \(C_0\to C_1\to\cdots\to C_{r-1}\to C_0\). For each quotient arc choose witnesses \(x_i\in C_i\), \(y_{i+1}\in C_{i+1}\) with \(x_i<_{P}y_{i+1}\), indices modulo \(r\). In each tree \(F[C_i]\), orient its unique path from the incoming vertex \(y_i\) to the outgoing vertex \(x_i\), allowing a zero-length path. Orient all unused query edges arbitrarily. The resulting directed comparisons plus the poset relations contain the directed closed walk \(x_0\to y_1\leadsto x_1\to\cdots\to y_0\leadsto x_0\). It is a directed cycle and has no linear extension, so \(S\) is not shattered.

**Step 4, sufficiency.** Suppose all three conditions hold. Give the edges of \(F\) any orientations, representing an arbitrary desired answer vector. Each oriented tree is acyclic. The union of these orientations with the fixed poset arcs has no directed cycle: any directed cycle entirely within one component contradicts the forest property (the poset has no internal strict relation by condition 2); a cycle meeting more than one component projects to a directed closed walk in \(Q\), contradicting condition 3. Every finite acyclic directed graph has a topological order. Its order is a linear extension of \(P\) realizing this answer vector. Thus all vectors occur.

**Step 5, dimension upper bound.** Let \(S\) be shattered. A forest with \(c\) components (including isolated vertices) has \(|S|=n-c\) edges. Since each component is an antichain, the \(h(P)\) elements of any longest chain occupy distinct components. Hence \(c\ge h(P)\), giving \(|S|\le n-h(P)\).

**Step 6, dimension lower bound.** For each \(x\in X\), set \(\rho(x)\) equal to the maximum number of elements of a chain ending at \(x\). The nonempty rank levels \(L_i=\{x:\rho(x)=i\}\), for \(1\le i\le h(P)\), partition \(X\) into antichains; \(x<_{P}y\) implies \(\rho(x)<\rho(y)\). Place an arbitrary spanning tree of comparison edges inside each \(L_i\), with isolated vertices for singleton levels. Their disjoint union \(F\) has \(\sum_i(|L_i|-1)=n-h(P)\) edges, and the quotient arcs always point from a lower rank to a higher rank, so it meets all three conditions. The support is shattered by Step 4 and meets the upper bound. For the empty poset the empty support gives equality.

## Verification
The bundled standalone program `verify_poset_comparisons.py` independently enumerates every labeled poset on up to four vertices, all possible query supports, and all compatible total orders to compare trace shattering directly against the three graph conditions and the dimension formula. It also checks every support for 75 deterministically sampled five-element posets, and verifies a forest whose quotient has a directed two-cycle is not shattered. Running `python3 verify_poset_comparisons.py` prints:

`POSET_COMPARISON_SHATTER_PASS all_posets_n_le_4=242 sampled_n5=75 tested_pairs=90975 posets_n5=4231`

The unrestricted claim is proved above; these finite tests are additional reproducibility checks, not an infinite-domain certificate.

## Relationship to prior work
For the antichain poset \(P\), the criterion reduces to the known assertion that the shattered pair-query supports of all permutations are exactly the forests; the new theorem handles every nontrivial fixed precedence relation and the additional component-level obstruction. Mirsky's rank-layer antichain decomposition is classical, but its role as an exact VC-dimension formula for pairwise comparison traces, together with the complete support criterion, is distinct from counting linear extensions. Dittmer and Pak (2018) establish \(\#\mathrm P\)-completeness of counting linear extensions for several restricted poset classes. Peters and Procaccia (2021) study average-case active preference elicitation with pairwise queries. Feng, Geneson, Lee, and Slettnes (2022) study bandit mistake bounds for inversion-comparison learning of permutations; their Section 5.2 does not characterize shattered fixed-poset supports. Duan, Ouyang, and Wang (2024 preprint; 2026 journal) study different compatibility set systems whose instances are whole posets or total orders, not individual pair queries under a fixed poset. None of these inspected results states or implies the three-condition characterization or \(n-h(P)\) formula for the specified class.

## Limitations
No assertion is made about adaptive Littlestone dimension, noisy or probabilistic preferences, querying entire partial orders, or the enumeration of all shattered supports for a general poset. The quotient requires transitive order information; starting from a DAG one may instead check reachability as needed. The literature comparison cannot exclude prior publication under an unsearched name, and this result has not undergone independent mathematical validation.

## References
1. S. Dittmer and I. Pak, *Counting linear extensions of restricted posets*, arXiv:1802.06312, first submitted 17 February 2018. https://arxiv.org/abs/1802.06312.
2. D. Peters and A. D. Procaccia, *Preference Elicitation as Average-Case Sorting*, AAAI 2021, 5647–5655, published 18 May 2021. https://dominik-peters.de/publications/sort-elicit.pdf; doi:10.1609/aaai.v35i6.16709.
3. B. Duan, M. Ouyang, and Z. Wang, *VC-dimensions Between Partially Ordered Sets and Totally Ordered Sets*, arXiv:2412.06402, first submitted 9 December 2024; *Order* 43 (2026), article 9. https://arxiv.org/html/2412.06402v3.
4. R. Feng, J. Geneson, A. Lee, and E. Slettnes, *Sharp bounds on the price of bandit feedback for several models of mistake-bounded online learning*, arXiv:2209.01366, first submitted 3 September 2022, Section 5.2. https://arxiv.org/html/2209.01366v1.
5. L. Mirsky, *A dual of Dilworth's decomposition theorem*, *American Mathematical Monthly* 78 (1971), 876–877 (classical antichain rank decomposition; not a claim of novelty).
