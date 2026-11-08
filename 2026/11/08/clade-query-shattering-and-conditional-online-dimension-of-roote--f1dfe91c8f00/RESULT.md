# Clade-query shattering and conditional online dimension of rooted phylogenetic trees

## Finding

Let \(X\) be a fixed labeled set of \(n\ge 2\) taxa and let \(\mathcal Q_X=\{A\subsetneq X:|A|\ge 2\}\). For every rooted binary phylogenetic tree \(T\) on \(X\), write \(\mathcal C(T)\subseteq\mathcal Q_X\) for its nontrivial proper clusters (the descendant leaf sets of nonroot internal vertices). The concept class \(\mathscr B_X\) consists of their indicator functions on \(\mathcal Q_X\). For a compatible family \(H\subseteq\mathcal Q_X\) of confirmed positive cluster queries, set \(\mathscr B_X(H)=\{\mathcal C(T):H\subseteq\mathcal C(T)\}\).

**New structural theorem (extending the previously established unconditional scalar capacities).** A query support \(S\subseteq\mathcal Q_X\setminus H\) is shattered by \(\mathscr B_X(H)\) if and only if \(H\cup S\) is **laminar**: for any two members, their intersection is empty or equals one of them. Consequently, for every such \(H\),

\[
\operatorname{VCdim}(\mathscr B_X(H))
=\operatorname{Ldim}(\mathscr B_X(H))=n-2-|H|.
\]

These equalities and the shattering criterion also hold if all rooted phylogenetic trees without unary internal vertices are permitted, instead of only binary trees.

For \(H=\varnothing\), write \(\Phi_n(z)=\sum_S z^{|S|}\), summed over shattered query supports. For every \(n\ge2\),

\[
\Phi_n(z)=\sum_{k=0}^{n-2}\left\{\!\!\begin{matrix}n+k\\k+1\end{matrix}\!\!\right\}_{\ge2}z^k,
\]

where \(\left\{\!\!\begin{smallmatrix}m\\j\end{smallmatrix}\!\!\right\}_{\ge2}\) counts partitions of an \(m\)-element set into \(j\) blocks, each of size at least two. In particular,

\[
\begin{aligned}
\Phi_3(z)&=1+3z,\\
\Phi_4(z)&=1+10z+15z^2,\\
\Phi_5(z)&=1+25z+105z^2+105z^3,\\
\Phi_6(z)&=1+56z+490z^2+1260z^3+945z^4.
\end{aligned}
\]

The coefficient formula enumerates a classical family of laminar hierarchies. The previously established unconditional equality of VC and Littlestone dimensions is **not** claimed as new. The new substance is the complete characterization of every shattered query support, its full face count, and its sharpened exact online dimension after any prescribed compatible family of confirmed positive clades.

## Assumptions and scope

Trees are rooted, nonplane, and leaf-labeled by \(X\). Binary means every internal node has exactly two children; in the nonbinary variant every internal node has at least two. No branch lengths are involved. Singleton clusters and \(X\) are excluded from the query universe because their answers would always be positive. Both the VC and Littlestone dimensions are computed for binary **membership answers to proposed clusters**, not rooted-triplet or quartet answers and not the number of queries required to identify the entire tree. \(H\) is an arbitrary laminar family of nontrivial proper clusters. All assertions are uniform in \(n\) and \(H\).

A family of queries is shattered if each Boolean labeling occurs as its restriction in at least one concept. Littlestone dimension is the largest depth of a complete adaptively labeled binary query tree all of whose paths are realizable.

## Proof

**1. An avoidance lemma.** Let \(Y\) be a set of \(d\ge2\) atoms, and let \(N\) be any laminar family of proper subsets of \(Y\), each with at least two elements. There exists a rooted binary tree on \(Y\) having none of the members of \(N\) as nontrivial clusters. Induct on \(d\). For \(d=2\) there are no such forbidden sets. For \(d\ge3\), since the two-element members of a laminar family are disjoint, they number at most \(\lfloor d/2\rfloor\). Thus some pair \(\{a,b\}\) does not belong to \(N\). Contract that pair to a new atom \(c\); discard members of \(N\) containing exactly one of \(a,b\), and transport each other member by the contraction. The transported family is laminar and has only proper subsets of size at least two. Apply induction to the contracted atoms and expand \(c\) to the cherry \(\{a,b\}\). The chosen cherry is not forbidden; every forbidden set containing exactly one of its leaves cannot be a cluster, while any remaining forbidden set would yield a forbidden cluster after contraction. This proves the lemma.

**2. Conditional shattering.** Necessity follows from the fact that the cluster family of every rooted tree is laminar, by assigning positive answers simultaneously to all queries in \(S\).

For sufficiency, assume \(H\cup S\) laminar, and fix an arbitrary labeling of \(S\). Let \(P\) consist of \(H\) and the positively labeled queries of \(S\). Adjoin the root cluster \(X\) and all singleton clusters. The resulting hierarchy defines a rooted, possibly multifurcating tree whose internal clusters include exactly \(P\) together with \(X\). For each negatively labeled query \(A\), let \(B\) be its smallest containing cluster in \(P\cup\{X\}\). Compatibility with \(P\) implies that \(A\) is the union of at least two but not all children of \(B\): otherwise it would lie inside a smaller positive node, or equal a singleton or member of \(P\). Negative queries assigned to the same \(B\) form a laminar family of proper, nonsingleton subsets of its children. Apply the avoidance lemma independently at each multifurcating node of the positive hierarchy to obtain binary refinements avoiding all these negative unions. The resulting binary tree preserves every member of \(P\) and contains no negative query. Since the labeling was arbitrary, \(S\) is shattered.

**3. Conditional dimensions.** A laminar family of proper nontrivial subsets of an \(n\)-element set has at most \(n-2\) members: add root and singleton nodes and count internal vertices of a rooted tree with no unary nodes. Every such family extends to exactly \(n-2\) nontrivial clusters of a binary refinement. Hence step 2 gives \(\operatorname{VCdim}(\mathscr B_X(H))=n-2-|H|\).

For the adaptive upper bound, follow the all-positive path of any completely shattered binary query tree for \(\mathscr B_X(H)\). Every query on that path must be distinct and not in \(H\), since each node has two feasible continuation branches, and a repeated query or confirmed positive cannot branch. All queries along the path, together with \(H\), occur in one binary phylogenetic tree. Such a tree has exactly \(n-2\) proper nontrivial clusters. Therefore the path length is at most \(n-2-|H|\). Since VC dimension never exceeds Littlestone dimension, equality holds. For the nonbinary class the same upper bound holds because nonbinary trees have at most \(n-2\) such clusters; the binary subclass supplies the same lower bound and shattering witnesses.

**4. Complete face counts.** A laminar family of proper nontrivial subsets on \(n\) labels is precisely a rooted nonplane phylogenetic hierarchy with these subsets as its marked nonroot internal nodes. Such internal nodes have at least two children. Let \(h(u)=e^u-1-u\), and let \(U(x,z)\) be the exponential generating series of nonroot subtrees, with a weight \(z\) for every internal node:

\[
U=x+z h(U),\qquad
\sum_{n\ge1}\Phi_n(z)\frac{x^n}{n!}=x+h(U).
\]

For \(n\ge2\), formal Lagrange inversion in \(z\) gives

\[
[z^k]h(U)=\frac1{(k+1)!}\left(\frac{d}{dx}\right)^k h(x)^{k+1},
\]

and hence

\[
[z^k]\Phi_n(z)=\frac{(n+k)!}{(k+1)!}[x^{n+k}](e^x-1-x)^{k+1}
=\left\{\!\!\begin{matrix}n+k\\k+1\end{matrix}\!\!\right\}_{\ge2}.
\]

The final equality uses the standard exponential generating function for partitions into blocks of size at least two.

## Verification

`python3 verify_clades.py` uses only the Python standard library. It recursively lists all distinct binary rooted tree cluster sets for \(2\le n\le6\), then enumerates every subset of every resulting cluster set. It verifies that all \(3019\) resulting laminar supports are actually shattered and independently matches each coefficient to a restricted-Stirling recurrence. It also recomputes the Littlestone recurrence for all positive histories through four taxa and for those with at least two confirmed proper clusters on five taxa, totaling \(241\) conditional instances. The emitted marker is `PHYLO_CLADE_SHATTER_PASS`. Finite checks validate small instances and do not replace the unrestricted induction.

## Relationship to prior work

The classical association between phylogenetic trees and laminar hierarchies is not new. Huber, Moulton and Wu study closed sets and hierarchies in phylogenetic networks; Francis and Jarvis study algebraic encodings of rooted binary and nonbinary phylogenetic trees and enumerate tree-related structures; Moulton, Spillner and Wicke treat cluster and split systems in phylogenetic diversity indices. Classical nonbinary hierarchy counting underlies the coefficient expression. Those results are not asserted to be new here. The unconditional scalar VC and Littlestone dimensions for clade membership in binary and unresolved rooted trees were established in earlier research and are **background, not a new claim of priority**. The new claims are the precise characterization and enumeration of the entire shattering complex, and exact conditional capacity for arbitrary compatible positive clade histories. The equality of the binary and unresolved **full shattering complexes**, rather than just scalar dimensions, is additional. Tree-reconstruction questions based on triplets or quartet displays have different query semantics.

## Limitations

No claim is made about the number of queries needed for exact identification of one tree, noisy labels, hidden taxa, or branch-length reconstruction. Negative observations can shrink the residual online dimension by more than this formula; the theorem computes the exact dimension conditioned on **positive** observations alone. The unconditional scalar dimensions and the counting coefficients as abstract hierarchy counts are already known, and neither is claimed as an original isolated result. The new claims concern their exact query-shattering and conditional-online interpretations. Historical priority for the particular learning-theoretic reformulation under alternative terminology remains a risk. The finite verifier checks only stated small ranges, and independent external validation has not been performed.

## References

1. K. T. Huber, V. Moulton, T. Wu, *Hierarchies from Lowest Stable Ancestors in Nonbinary Phylogenetic Networks*, Journal of Classification 36 (2019), 200–231, DOI: 10.1007/s00357-018-9279-5. Public repository deposit dated 20 October 2017. https://ueaeprints.uea.ac.uk/id/eprint/65193/
2. A. Francis, P. D. Jarvis, *Brauer and partition diagram models for phylogenetic trees and forests*, Proceedings of the Royal Society A 478 (2022), 20220044, DOI: 10.1098/rspa.2022.0044. https://pmc.ncbi.nlm.nih.gov/articles/PMC9185836/
3. V. Moulton, A. Spillner, K. Wicke, *Phylogenetic Diversity Indices from an Affine and Projective Viewpoint*, Bulletin of Mathematical Biology 86 (2024), article 103, arXiv:2403.15842, DOI: 10.1007/s11538-024-01332-x. https://arxiv.org/abs/2403.15842
4. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone’s Dimension via (Unbalanced) Biclique*, ITCS 2023, DOI: 10.4230/LIPIcs.ITCS.2023.85. https://doi.org/10.4230/LIPIcs.ITCS.2023.85
