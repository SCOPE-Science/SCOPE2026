# Global someone-knows spectra: rectangular visibility, exact fibers, and the matching boundary

## Finding

Let \(k\geq2\) be finite, let \(X_1,\ldots,X_k\) be finite nonempty sets, and let \(T\subseteq\prod_i X_i\) be nonempty. Assume each \(X_i=\pi_i(T)\). On this finite multi-agent \(\mathsf{S5}\) frame, agent \(i\) identifies worlds with the same \(i\)-th coordinate. For an event \(U\subseteq T\), define the **global someone-knows observation**
\[
\mathsf S_T(U)=\{w\in T:\exists i\ \forall v\in T\,(v_i=w_i\Longrightarrow v\in U)\}.
\]
Write \(H=T\setminus U\), with \(\pi_i(\varnothing)=\varnothing\), and define \(c_T(H)=T\cap\prod_i\pi_i(H)\) (the product is empty when a factor is empty).

**Theorem (complete observation and visibility spectrum).**

1. For every such \(T\) and every \(U\subseteq T\),
\[
\mathsf S_T(U)=T\setminus c_T(T\setminus U).
\]
The map \(c_T\) is a closure operator, so the someone-knows operation is an idempotent interior operator. Put \(\mathcal L_T=\{c_T(H):H\subseteq T\}\), ordered by inclusion, with Möbius function \(\mu\). Every observation is exactly \(T\setminus C\) for one \(C\in\mathcal L_T\), and its exact valuation fiber has cardinality
\[
\#\{U:\mathsf S_T(U)=T\setminus C\}
=\sum_{D\in\mathcal L_T\, :\,D\subseteq C}\mu(D,C)2^{|D|}.
\]
2. If \(T=\prod_i X_i\) is a full product and \(n_i=|X_i|\), the number of distinct global observations is
\[
1+\prod_{i=1}^k(2^{n_i}-1).
\]
Besides the unique observation \(T\), the observations are precisely \(T\setminus\prod_i B_i\), where each \(B_i\subseteq X_i\) is nonempty. The number of events \(U\) yielding one such observation, with \(b_i=|B_i|\), is
\[
F(b_1,\ldots,b_k)=\sum_{j_1=0}^{b_1}\cdots\sum_{j_k=0}^{b_k}(-1)^{\sum_i j_i}\left(\prod_i\binom{b_i}{j_i}\right)2^{\prod_i(b_i-j_i)}.
\]
3. On the full product, put \(N=\prod_i n_i\) and \(M=\max_i n_i\). Among events completely invisible to every agent everywhere (\(\mathsf S_T(U)=\varnothing\)), the largest cardinality is \(N-M\). If \(j\) is any coordinate with \(n_j=M\), the number of events attaining this bound equals
\[
\prod_{i\ne j}n_i!\,\left\{\begin{matrix}M\\n_i\end{matrix}\right\},
\]
where the braces are Stirling numbers of the second kind. For a \(2\times2\times3\) full product, the maximum invisible-event size is \(9\), attained by exactly \(36\) events.
4. For a general, possibly correlated \(T\), completely invisible events correspond exactly to **edge covers** of the \(k\)-partite \(k\)-uniform incidence hypergraph whose edges are the worlds of \(T\) and whose vertex parts are the observed coordinate values \(X_i\). For \(k=2\), if \(\nu\) is the maximum matching size in that bipartite graph, the maximum invisible-event size is \(|T|-(|X_1|+|X_2|-\nu)\). For \(k=3\), deciding from \((T,q)\) whether there is an invisible event with \(|T\setminus U|\le q\) is NP-complete; equivalently, maximizing invisible truth sets in explicit correlated three-agent structures is NP-hard.

The matching and three-dimensional matching facts used in part 4 are classical. The finding is the combined finite-modal observation/fiber/optimization characterization, not a claim to those standard combinatorial theorems.

## Assumptions and scope

The frame is a **finite nonempty explicitly represented set of joint local states** \(T\), with coordinates giving the actual observational equivalence classes. The proposition varies freely over all \(2^{|T|}\) Boolean valuations. No independence of the local coordinates is assumed unless the full-product hypothesis is stated. Every coordinate value in \(X_i\) must occur in at least one world; this removes irrelevant isolated vertices. Complete invisibility is a statement about the global truth set of \(\bigvee_{i=1}^k K_i p\), not about whether one particular pointed state satisfies it, and not about distributed knowledge. The complexity statement fixes three agents, and the explicit list of worlds is part of the input.

## Proof

**Step 1: the semantic closure identity.** Write \(H=T\setminus U\). An agent \(i\) knows the proposition at \(w\) iff no false world has coordinate \(w_i\), i.e. iff \(w_i\notin\pi_i(H)\). Consequently no agent knows at \(w\) iff \(w\in T\cap\prod_i\pi_i(H)\). This proves the first identity for empty and nonempty \(H\). The operator \(c_T\) is extensive: each \(h\in H\) has all its coordinates in the corresponding projection. It is monotone by projection monotonicity. Also \(\pi_i(c_T(H))=\pi_i(H)\), since \(H\subseteq c_T(H)\) and \(c_T(H)\subseteq\{w:w_i\in\pi_i(H)\}\). Therefore it is idempotent. Taking complements shows \(\mathsf S_T\) is an idempotent, deflationary, monotone interior operator. Its image is the complements of \(c_T\)-closed sets.

For a closed \(C\), let \(f(C)=|\{H:c_T(H)=C\}|\). A set \(H\) satisfies \(c_T(H)\subseteq C\) exactly when \(H\subseteq C\), by extensiveness in one direction and monotonicity plus \(c_T(C)=C\) in the other. Thus \(2^{|C|}=\sum_{D\in\mathcal L_T,D\subseteq C}f(D)\). Möbius inversion on this finite poset proves the fiber formula. The map \(U\mapsto H\) is a bijection, so counts agree.

**Step 2: full-product output and fiber counts.** If \(T=\prod_i X_i\), then each nonempty closure is exactly the box \(\prod_i B_i\), and every such box is itself closed (its projection in coordinate \(i\) is precisely \(B_i\)). Distinct nonempty boxes have distinct coordinate projections. There is one empty closure, giving \(1+\prod_i(2^{n_i}-1)\) images. To have \(c_T(H)=\prod_i B_i\), we must choose \(H\subseteq\prod_i B_i\) such that each coordinate projection is surjective onto \(B_i\). For every tuple of forbidden coordinate-value subsets \(J_i\subseteq B_i\), there are exactly \(2^{\prod_i(b_i-|J_i|)}\) choices of \(H\) avoiding all values in all \(J_i\). Inclusion-exclusion over all forbidden values gives \(F\). The empty closure comes only from \(H=\varnothing\), so its fiber is \(1\).

**Step 3: sharp invisibility bound and multiplicity.** Invisibility means \(c_T(H)=T\). On a full product, this is equivalent to surjectivity of every projection \(\pi_i(H)=X_i\). Hence \(|H|\ge M=\max_i n_i\). Conversely label the elements of each \(X_i\) by residues and choose \(M\) worlds indexed by \(t=0,\ldots,M-1\), with coordinate \(i\) equal to the label \(t\bmod n_i\). They are distinct in a coordinate \(j\) with \(n_j=M\), and every projection is surjective, achieving \(|H|=M\). For any optimal \(H\), each of the \(M\) values of coordinate \(j\) occurs in exactly one world, so \(H\) is the graph over \(X_j\) of independent surjections \(f_i:X_j\twoheadrightarrow X_i\) for \(i\ne j\). The number of surjections from an \(M\)-element set onto an \(n_i\)-element set is \(n_i!\left\{\begin{smallmatrix}M\\n_i\end{smallmatrix}\right\}\). Multiplying gives the count, valid even when several coordinates tie for the largest size.

**Step 4: correlated-team complexity.** A subset \(H\subseteq T\) projects onto all \(X_i\) iff every observed coordinate value lies in an edge corresponding to some member of \(H\). This is exactly an edge cover of the incidence hypergraph. In two parts there are no isolated vertices by assumption. A minimum edge cover of a bipartite graph with \(r=|X_1|+|X_2|\) vertices has size \(r-\nu\): a maximum matching of size \(\nu\) extends to an edge cover using one edge for each unmatched vertex, giving \(r-\nu\); conversely an inclusion-minimal edge cover induces a disjoint union of stars, each of which contributes one edge to a matching, proving the reverse bound. Computing a maximum bipartite matching is polynomial.

For three parts, membership in NP follows by checking a proposed \(H\) of size at most \(q\). To prove hardness, reduce *three-dimensional matching*: given disjoint sets \(X_1,X_2,X_3\), each of cardinality \(q\), and a set of permitted triples \(T\), ask whether \(q\) pairwise disjoint triples cover all \(3q\) values. If some value occurs in no permitted triple, output a fixed negative edge-cover instance instead; this standard preprocessing is polynomial and preserves yes/no. Otherwise \(\pi_i(T)=X_i\). An edge cover with at most \(q\) triples must have exactly \(q\), and since it covers \(3q\) vertices it is a perfect three-dimensional matching. The converse holds immediately. This is a many-one polynomial reduction from the classical NP-complete problem. All claims hold on the stated finite explicit input model.

## Verification

The standalone standard-library Python script `check.py` executes **direct** coordinate-equivalence modal truth evaluation rather than merely reusing the algebraic formula. It compares that direct evaluation with the closure identity for every nonempty subteam of four small coordinate products (\(2\times2\), \(2\times3\), \(3\times3\), \(2\times2\times2\)): 844 distinct teams and 27,050 truth-set valuations. It independently reconstructs fibers by the closed-set recurrence. It checks all events on full products of sizes \((1,2),(2,2),(2,3),(3,3),(2,2,2),(2,2,3)\), including exact outputs, fiber counts, sharp false-state thresholds and optimal multiplicities. Executed with Python 3, it reports `ALL_CHECKS_PASSED`. The NP-completeness proof is symbolic and uses the established hardness of three-dimensional matching; these finite tests do not establish that hardness or the general theorem.

## Relationship to prior work

Ding and Yang, *A General Theory of Propositional Modal Bundled Modalities* (arXiv:2603.26268, first public March 27, 2026), §5.1, define the someone-knows disjunction and derive axiomatics and representation/completeness results for \(\mathsf{S5}\). Their paper is the primary semantic source; its inspected full text does not contain the global finite-product projection-box output spectrum, fibers or the graph/hypergraph optimization boundary here. Ding, Liu and Wang, *Someone knows that local reasoning on hypergraphs is a weakly aggregative modal logic* (2023), give a directly relevant hypergraph perspective and modal-logical axiomatization, but the complete text was not accessible during this comparison, so potential conceptual or quantitative overlap remains unresolved. Classical finite closure-system Möbius inversion, edge-cover/matching duality, surjection counts and NP-completeness of three-dimensional matching are established background and are not asserted to be newly discovered here.

## Limitations

The counts and full-product optimum rely on unconstrained Boolean valuations; restrictions on admissible valuations could change every fiber. The explicit formula for arbitrary correlated teams involves the closed-set poset and may be exponential to compute. The polynomial versus NP-complete distinction concerns the *explicit finite input*, not arbitrary succinctly represented models. A relevant older full paper about epistemic hypergraphs was not fully accessible, and equivalent formulations in older closure-system or database projection literature could take priority; absence from checked sources is not proof of historical uniqueness. Independent auditing and priority certification are not asserted.

## References

1. Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268v1 (first public 2026-03-27), revised arXiv:2603.26268v2; EPTCS 447 (2026), pp. 299–320, DOI: 10.4204/EPTCS.447.17. Open full text: https://arxiv.org/html/2603.26268v2 .
2. Yifeng Ding, Jixin Liu and Yanjing Wang, *Someone knows that local reasoning on hypergraphs is a weakly aggregative modal logic*, Synthese 201 (2023), DOI: 10.1007/s11229-022-04032-y. Complete text not inspected.
3. Classical results used: Möbius inversion on finite posets; Stirling numbers and surjections; minimum bipartite edge covers via maximum matching; NP-completeness of three-dimensional matching. These are cited as established mathematical tools, not independent novel claims.
