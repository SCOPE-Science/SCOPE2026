# Exact graphic-matroid shattering for fixed-block same-cluster queries

## Finding
Let \(n\ge2\), \(2\le q\le n\), and let \(H\) be any finite simple graph with labeled vertex set \([n]\), whose edges are the allowable pair queries. Let \(\mathcal C_{n,q}(H)\) be the Boolean concept class induced on \(E(H)\) by **all partitions of \([n]\) into exactly \(q\) nonempty, unlabeled blocks**: an edge \(uv\) receives label one exactly when its endpoints lie in the same block.

**Theorem (complete shattering and trace criteria).** Every support \(S\subseteq E(H)\) is shattered by \(\mathcal C_{n,q}(H)\) if and only if \(([n],S)\) is a forest and \(|S|\le n-q\). Hence its shattering complex is exactly the rank-\(\min\{n-q,n-c(H)\}\) truncation of the graphic matroid of \(H\), and
\[
\operatorname{VCdim}(\mathcal C_{n,q}(H))=\min\{n-q,\,n-c(H)\},
\]
where \(c(H)\) is the number of connected components of \(H\), including isolated vertices.

More generally, for any pair of disjoint edge sets \(P,N\subseteq E(H)\) requiring labels one and zero, respectively, contract all edges of \(P\) in the spanning graph on \([n]\). Let \(c_P\) be the number of resulting vertices and let \(Q_{P,N}\) be the graph on these vertices with edges induced by \(N\). If an edge of \(N\) becomes a loop, define \(\chi(Q_{P,N})=\infty\). The requested trace is realizable **if and only if**
\[
\chi(Q_{P,N})\le q\le c_P.
\]
Thus, for the fixed value \(q=3\), deciding feasibility of a *specified signed trace* is NP-complete in general, although deciding whether the entire support is shattered takes only a forest test and a cardinality comparison.

The complete shattering polynomial is the rank truncation of the ordinary forest polynomial:
\[
\Phi_{H,q}(z)=\sum_{j=0}^{n-q} f_j(H)z^j
=\bigl[z^{\le n-q}\bigr]\,z^{n-c(H)}T_H(1+z^{-1},1),
\]
where \(f_j(H)\) counts \(j\)-edge forests in \(H\), \(T_H\) is the Tutte polynomial, and \([z^{\le r}]\) retains only degrees at most \(r\). All inclusion-maximal shattered supports have exactly \(\min\{n-q,n-c(H)\}\) edges. In the complete-query case \(H=K_n\), the number of inclusion-maximal supports equals
\[
\frac{n!}{q!}[u^n]\left(\sum_{j\ge1}\frac{j^{j-2}}{j!}u^j\right)^q,
\]
where the singleton-tree term at \(j=1\) is interpreted as \(1\).

## Assumptions and scope
The theorem concerns ordinary undirected, simple pair queries with no loops or duplicates. The partition blocks are all nonempty and have **exactly** \(q\) blocks; their names are immaterial. No optimization objective or distribution is imposed on the clustering. For \(q=1\), the concept class consists of a single constant function, so only the empty support is shattered; this boundary case is outside the stated forest characterization. For \(q=n\), only the discrete partition exists, and the formula gives VC dimension zero. The trace criterion itself also holds for \(q=1\).

## Proof
**Arbitrary traces.** Contracting the required-positive edges \(P\) forces every resulting component to be monochromatic: its members must belong to a single block. If a negative edge has endpoints in the same positive component, the demand is contradictory. Otherwise, negative edges impose only the rule that adjacent positive components must receive different block names. A partition into exactly \(q\) blocks thus induces a proper coloring of \(Q_{P,N}\) using exactly \(q\) nonempty color classes, proving necessity of \(\chi(Q_{P,N})\le q\le c_P\). Conversely, if these inequalities hold, choose any proper coloring with \(\chi(Q_{P,N})\) colors; repeatedly split a nonempty color class into two until exactly \(q\) colors are used. This is possible because there are \(c_P\) vertices. Lifting the colors to the original vertices produces a required partition, proving sufficiency. This proves the trace criterion even if \(P\) has cycles.

**Shattering necessity.** If \(S\) contains a cycle, put label one on all but one cycle edge and label zero on that last edge. Transitivity of equality makes this labeling impossible. Thus a shattered \(S\) must be a forest. The all-positive labeling contracts the \(|S|\) edges of this forest and leaves exactly \(n-|S|\) positive components. At least \(q\) components are needed for exactly \(q\) nonempty blocks. Hence \(|S|\le n-q\).

**Shattering sufficiency.** Suppose that \(S\) is a forest and \(|S|\le n-q\), and choose arbitrary disjoint \(P,N\) partitioning \(S\) into positive and negative required edges. Contracting \(P\) in the forest cannot create a loop or cycle in the negative graph \(Q_{P,N}\). Thus \(\chi(Q_{P,N})\le2\le q\). Also \(c_P=n-|P|\ge n-|S|\ge q\). The already proved trace criterion realizes every assignment on \(S\); therefore \(S\) is shattered.

**Matroid and enumeration consequences.** The independent sets of the graphic matroid of \(H\) are precisely its forests. Restricting these to size at most \(n-q\) is matroid rank truncation, so the maximum rank is \(\min\{n-q,n-c(H)\}\) and all maximal independent sets have that size. For the Tutte identity, use the subset expansion at \(y=1\): only forests contribute, giving \(\sum_j f_j(H)z^j=z^{n-c(H)}T_H(1+z^{-1},1)\). For \(K_n\), maximal supports are spanning forests with exactly \(q\) components. The exponential formula for sets of labeled trees, together with Cayley's count \(j^{j-2}\) for a labeled tree of order \(j\ge2\), gives the displayed coefficient extraction.

**Complexity contrast.** For \(q=3\), let \(P=\varnothing\), and let \(N\) be the edges of an arbitrary graph \(J\) on \(n\ge3\) vertices. Then \(c_P=n\) and \(Q_{P,N}=J\). The all-negative trace is feasible exactly when \(J\) is three-colorable. Standard graph three-colorability is NP-complete, and a three-block partition is a polynomially checkable certificate. Conversely, the shattering characterization permits linear-time testing in \(n+|S|\), using a depth-first forest test and \(|S|\le n-q\).

## Verification
The standalone stdlib Python file `verify.py` independently enumerates all unlabeled set partitions using restricted-growth strings, computes their edge-label masks, and checks all supports against the forest-cardinality characterization for complete pair domains through \(n=5\). It also checks a deterministic sample at \(n=6\), verifies matroid basis exchange for the complete domains through \(n=5\), and cross-checks the arbitrary-trace contraction/coloring criterion against explicit partition search on complete domains through \(n=4\), plus a deterministic sample for \(n=5\). Execute from this directory using `python3 verify.py`. The expected terminal marker is `FIXED_BLOCK_PARTITION_SHATTERING_PASS 9916 partition-support cases`. These finite tests corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work
Same-cluster queries are used by Ailon, Bhattacharya, and Jaiswal (2017), by Kushagra, Ben-David, and Ilyas (2018), and by Saha and Subramanian (2019). The 2018 work explicitly represents a clustering as a binary function on pairs and formulates VC-dimension-dependent sample guarantees; Section 5.1 gives general bounds on VC dimension for finite clustering families and hierarchical clustering, not this fixed-block all-support description. The other cited papers concern approximation and oracle query complexity, not the shattering complex of all exactly-\(q\)-block partitions. Forests, graphic-matroid truncation, Cayley tree counts, Tutte polynomials, and the NP-completeness of three-colorability are standard prior mathematics; none is claimed as new. The contribution is their exact identification with every shattered pair support for the fixed-block hypothesis class and the resulting discrepancy between universal support testing and arbitrary trace feasibility.

## Limitations
This is a mathematical capacity theorem, not an optimal adaptive-query algorithm or an improved approximation theorem for correlation clustering. The graph \(H\) specifies which pair queries are available, not constraints on which partitions are valid. Requiring geometric clusters, connected clusters, prescribed block sizes, or weighted objectives changes the hypothesis class and may invalidate the forest condition. Prior independent discovery under an alternative graph-coloring or clustering terminology remains possible. The finite verification covers only stated test instances; the proof establishes the unrestricted result.

## References
1. N. Ailon, A. Bhattacharya, R. Jaiswal, *Approximate Correlation Clustering Using Same-Cluster Queries*, arXiv:1712.06865, first version 19 December 2017, https://arxiv.org/abs/1712.06865.
2. S. Kushagra, S. Ben-David, I. Ilyas, *Semi-supervised clustering for de-duplication*, arXiv:1810.04361, first version 10 October 2018, https://arxiv.org/abs/1810.04361, especially Sections 2 and 5.1 and Appendix C.1.
3. B. Saha, S. Subramanian, *Correlation Clustering with Same-Cluster Queries Bounded by Optimal Cost*, ESA 2019, DOI 10.4230/LIPIcs.ESA.2019.81, https://doi.org/10.4230/LIPIcs.ESA.2019.81.
