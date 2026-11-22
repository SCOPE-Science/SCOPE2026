# Friendship-base type spectra and a sharp edge-star condensation hierarchy

## Finding
Let \(\mathbb H_4\) denote the countable homogeneous universal \(K_4\)-free graph. For an integer \(m\ge1\), individually name an induced *friendship graph* \(F_m=K_1\vee(mK_2)\), whose hub is joined to the two endpoints of each of \(m\) disjoint petal edges. For any fixed integer \(r\ge2\), uniformly sample a complete type of an ordered, pairwise distinct \(r\)-tuple of vertices outside the named parameters. Let \(H\) be its labelled induced graph on the new coordinates.

**Exact all-arity transfer.** For each labelled \(K_4\)-free graph \(H\) on \([r]\), define \(q_H(C)\) for \(C\subseteq[r]\) as the number of ordered pairs \((U,V)\) of subsets of \([r]\) satisfying the following finite conditions:

1. Each of \(H[C]\), \(H[U]\), and \(H[V]\) is triangle-free.
2. \(C\cap U\cap V=\varnothing\).
3. Each of \(H[C\cap U]\), \(H[C\cap V]\), and \(H[U\cap V]\) is edgeless.

Then the number \(N_H(m)\) of these complete types with induced graph exactly \(H\) is
\[
\boxed{N_H(m)=\sum_{C\subseteq[r]}q_H(C)^m.}
\]
These terms are nonnegative, and \(q_H(C)<q_H(\varnothing)\) for every nonempty \(C\) whenever the latter is positive. Therefore \(N_H(m)\sim q_H(\varnothing)^m\) for fixed \(r,H\).

**Sharp hierarchy of rare-edge concentration.** For every fixed \(r\ge2\) and \(1\le k\le r-1\), put
\[
\rho_k=\frac34+\frac14\left(\frac34\right)^k.
\]
Let \(L_{r,1}=\binom r2\), and for \(2\le k\le r-1\) let \(L_{r,k}=r\binom{r-1}{k}\). For the uniform distribution over complete ordered injective \(r\)-tuple types, as the number \(m\) of petals tends to infinity,
\[
\boxed{\Pr_m(|E(H)|\ge k)\sim L_{r,k}\,\rho_k^m.}
\]
Moreover, conditional on \(|E(H)|\ge k\), the induced graph \(H\) is asymptotically almost surely exactly a \(k\)-edge star together with \(r-k-1\) isolated vertices. For \(k=1\) this means one edge; for \(k\ge2\) it means all \(k\) edges incident to a common tuple vertex. The conditional concentration statement is for each *fixed* \(r,k\), not for thresholds growing with \(m\).

As a finite check, the number of nonedge ordered-pair types is \((4^m+3^m)^2\), and the number of edge ordered-pair types is \(15^m+2\cdot12^m+7^m\). This pair case is illustrative rather than asserted as a new two-type classification.

## Assumptions and scope
The graph language has one undirected, irreflexive adjacency relation. The named parameter graph \(F_m\) is induced, all its vertices are fixed individually, and no two different petal pairs have cross-edges. All tuple coordinates are pairwise distinct and distinct from every parameter. Complete types are full first-order types over the named finite base; by homogeneity and the finite-extension property, their classification coincides with the finite induced adjacency diagrams that are \(K_4\)-free. Internal tuple graphs \(H\) carrying \(K_4\) contribute zero and are omitted.

The limit holds for fixed finite arity \(r\) and fixed integer edge threshold \(k\), as \(m\to\infty\). The uniform measure is on the finite set of **logical types**, not on independently sampled vertices from the infinite structure. The statement makes no claim about arbitrary parameter graphs, tuple repetitions, or growing tuple arity.

## Proof
**1. Local forbidden-clique conditions and factorization.** Fix the induced tuple graph \(H\). Let \(C\subseteq[r]\) index new vertices adjacent to the old hub. For petal \(j\), let \(U_j,V_j\subseteq[r]\) index new vertices adjacent to its two endpoints. A forbidden four-clique in the combined diagram must be one of: four new vertices; the hub together with three new vertices; one petal endpoint together with three new vertices; the hub and one petal endpoint together with two new vertices; both endpoints of one petal together with two new vertices; or the old hub and both endpoints of one petal together with one new vertex. These cases are respectively excluded by \(H\) being \(K_4\)-free, the three triangle-free tests, the three edgeless-intersection tests, and the triple-empty test in the definition of \(q_H\). No four-clique can meet distinct petal edges because there are no cross-petal old edges. Thus \(C\) is global but the \(m\) petal choices are independent, giving exactly \(q_H(C)^m\) diagrams for each \(C\); summing gives the transfer identity. Each permitted diagram determines one complete type by universality and ultrahomogeneity of \(\mathbb H_4\).

For \(C\ne\varnothing\), the allowed \((U,V)\) pairs form a subset of those allowed at \(C=\varnothing\). If \(c\in C\), the choice \(U=V=\{c\}\), allowed at \(C=\varnothing\) for every \(H\), fails \(C\cap U\cap V=\varnothing\). Therefore \(q_H(C)<q_H(\varnothing)\). In particular \(q_H(\varnothing)\ge1\), proving \(N_H(m)\sim q_H(\varnothing)^m\).

**2. A weighted independent-set envelope.** At \(C=\varnothing\), membership of a coordinate in \(U,V\) has four states: neither, first only, second only, or both. The edgelessness of \(H[U\cap V]\) requires the coordinates in the both-state to form an independent set. Dropping only the additional triangle-free requirements on \(H[U]\) and \(H[V]\) gives the upper bound
\[
q_H(\varnothing)\le\Psi_r(H):=\sum_{I\subseteq[r]\text{ independent in }H}3^{r-|I|}.
\]
Equality holds whenever \(H\) is triangle-free, since then every induced subgraph \(H[U],H[V]\) is triangle-free. In particular equality holds for an edgeless graph and for every star.

**3. Weighted extremality of small stars.** For any simple graph \(H\) with at least \(k\) edges, where \(1\le k\le r-1\), choose an arbitrary \(k\)-edge subgraph \(G\) on the same vertices. Deleting edges only increases the count of independent sets of each cardinality, so \(\Psi_r(H)\le\Psi_r(G)\), strictly if any edge was deleted: the two endpoints of a deleted edge themselves form an independent set in the resulting subgraph. Applying the graph form of the Kruskal–Katona clique theorem to the complement \(\overline G\), which has \(\binom r2-k\) edges, shows that a colex initial segment simultaneously maximizes the number of cliques of every size. For \(k\le r-1\), this colex graph is the complement of a \(k\)-edge star with \(r-k-1\) isolated vertices. Hence its clique-count coefficients, equivalently the independent-set coefficients of the star, dominate those of \(G\). All weights \(3^{r-j}\) are strictly positive, so
\[
\Psi_r(H)\le\Psi_r(S_{r,k})=4^{r-k-1}(3\cdot4^k+3^k)=4^r\rho_k.
\]
For \(k\ge2\), equality forces the \(k\)-edge graph to have an independent set of size \(r-1\), as the star does. This requires all its edges to share one vertex; hence it must itself be a \(k\)-edge star. For \(k=1\), every one-edge graph is such a star. Adding any additional edge strictly reduces the weighted independent-set count. Consequently every graph with at least \(k\) edges that is not isomorphic to \(S_{r,k}\) has \(q_H(\varnothing)<4^r\rho_k\), while each copy of the star, being triangle-free, has exactly \(q_H(\varnothing)=4^r\rho_k\).

**4. Extraction of the asymptotic law.** The edgeless tuple graph has local count \(q_{\emptyset}(C)=4^{r-|C|}3^{|C|}\), so its type count is exactly
\[
N_{\emptyset}(m)=(4^m+3^m)^r\sim 4^{rm}.
\]
The extremal bound at \(k=1\) shows every nonempty internal graph has strictly smaller exponential base than \(4^r\), so the total number of types is \(4^{rm}(1+o(1))\). For \(k\ge2\), there are exactly \(r\binom{r-1}{k}\) labelled \(k\)-edge stars on \([r]\), while for \(k=1\) there are \(\binom r2\) one-edge graphs. Each contributes asymptotically \((4^r\rho_k)^m\) types. All other graphs with at least \(k\) edges contribute exponentially less, and only finitely many labelled graphs occur for fixed \(r\). Dividing their total by \(4^{rm}(1+o(1))\) proves the sharp probability equivalent and conditional star concentration.

**5. Exact pair count.** For \(r=2\) and an edgeless internal graph, \(q(C)=4^{2-|C|}3^{|C|}\), giving \((4^m+3^m)^2\). For a single internal edge, the four choices \(C=\varnothing,\{1\},\{2\},\{1,2\}\) yield respectively \(q(C)=15,12,12,7\), and hence \(15^m+2\cdot12^m+7^m\).

## Verification
The accompanying standalone `check_windmill.py` performs direct enumeration of adjacency diagrams, testing the full combined graph for forbidden four-cliques independently of the transfer criterion. It compares 88 complete diagram cases, covering tuple arities up to four and one to three petals, and checks 432 independent-set extremal inequalities over all graphs of the tested orders up to five tuple vertices. It also verifies the exact pair channels. Execute `python3 check_windmill.py` with Python's standard library; `verification-output.txt` records the successful replay. These finite tests corroborate the all-arity proof but cannot establish its unbounded claims.

## Relationship to prior work
Henson's 1971 construction supplies universality and ultrahomogeneity of the countable \(K_4\)-free graph. Conant (arXiv:1401.1570v1) describes finite relation types and their consistency in Henson graphs, particularly in Proposition 3.4, but investigates dividing/forking rather than this type distribution. Classical Kruskal–Katona theory supplies the required coefficientwise extremal inequality for independent-set polynomials, not the logical type transfer or conditional concentration result.

Previous finite-parameter Henson one-type enumeration and pair-feasibility principles account for the unary and illustrative pair formulas; these are not claimed as a new two-type result. Another explicitly relevant previous higher-arity result enumerates tuple types over **disjoint maximal parameter cliques** and finds leading edgeless, single-edge and two-edge-path layers. Its parameter base has no common hub, and its stated leading-base result does not entail the full hierarchy of \(k\)-edge-star concentration for every fixed threshold \(k\le r-1\) over the friendship parameter family. Direct searches of the identified mathematical literature and indexed records did not establish an equivalent all-threshold statement for this family. Completeness of historical priority is not certified.

## Limitations
The transfer is a finite algorithmic expression rather than a minimal closed exponential expansion for every internal graph. The concentration theorem requires fixed \(r,k\), and its error is not claimed uniform when they vary. Logical types have equal weight; random realizations in a sampled finite graph need not. All statements assume the graph language and the induced friendship parameter base. Earlier unindexed enumerations or equivalent extremal probabilistic formulations are a remaining historical-priority risk.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* **38** (1971), 69–83, Theorem 2.3. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-s.pdf
2. G. Conant, “Forking and dividing in Henson graphs,” arXiv:1401.1570v1, first posted 2014-01-08, Section 3 and Proposition 3.4. https://arxiv.org/html/1401.1570v1
3. H. Huang, N. Linial, H. Naves, Y. Peled and B. Sudakov, “On the densities of cliques and independent sets in graphs,” arXiv:1211.4532 (2012); background on the classical Kruskal–Katona extremal clique theorem. https://arxiv.org/abs/1211.4532
4. “Exact triple-type spectrum and rare-edge clustering over disjoint maximal cliques in Henson graphs,” published mathematical record, 2026, sections Finding and Proof. https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-triple-type-spectrum-and-rare-edge-clustering-over-disjoin--85936f11eaf8/RESULT.md
