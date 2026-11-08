# Exact Littlestone dimension of acyclic orientations of \(K_{2,b}\)

## Finding

Let \(b\ge1\). Represent an acyclic orientation of the complete bipartite graph \(K_{2,b}\) by its \(2\times b\) binary edge-direction matrix, and let each of its \(2b\) individual entries be an allowable binary query. The exact Littlestone dimension of this finite concept class is
\[
\operatorname{Ldim}(\mathcal A_b)=\left\lceil\frac{3b}{2}\right\rceil.
\]
Its VC dimension, previously known via the forest characterization of shattered edge sets, is \(b+1\), so the exact adaptive–static gap is \(\lceil b/2\rceil-1\) and is unbounded even though the underlying graphs have treewidth at most two.

More generally, let \(F(u,a,c)\) be the online dimension of the conditional two-sign version space described below. For all nonnegative integers \(u,a,c\),
\[
F(u,a,c)=\max\left\{u+a,\ u+c,\ \left\lceil\frac{3u+a+c}{2}\right\rceil\right\}.
\]
This conditional formula is the stronger claim from which the main theorem follows by taking \(u=b\) and \(a=c=0\).

## Assumptions and scope

The graph has two distinguished left vertices and \(b\) distinctly labelled right vertices. Each column of the orientation matrix is one of four types, named \(00\), \(01\), \(10\), \(11\), with entry one meaning the corresponding edge is oriented from its left endpoint toward its right endpoint. Call \(00\) and \(11\) *neutral* and call \(01\) and \(10\) the two *opposite mixed* types. An orientation is acyclic if and only if it does not simultaneously have a column of type \(01\) and one of type \(10\): any directed cycle on a graph with just two left vertices has length four, and such a four-cycle uses precisely the two opposite mixed columns.

For a finite, nonempty binary concept family \(\mathcal H\), \(\operatorname{Ldim}(\mathcal H)\) is the maximum depth of a complete binary mistake tree with edge-entry queries at internal nodes and a consistent hypothesis at every leaf. Equivalently, singleton families have rank zero, and for any family with more than one hypothesis the rank is the maximum over nonconstant queries of one plus the minimum rank of the two nonempty answer classes.

Before any mixed type has been fixed by prior answers, every unresolved column is either unqueried (\(u\) columns), queried in exactly one of its two entries (a neutral-or-\(01\) pair for \(a\) columns or a neutral-or-\(10\) pair for \(c\) columns), or fully fixed to a neutral type (ignored). The conditional class \(\mathcal H(u,a,c)\) consists of exactly those full columns consistent with this information and the global ban on opposite mixed types. The locations of columns and the choice of their neutral types do not affect its online rank. We set \(F(u,a,c)=\operatorname{Ldim}(\mathcal H(u,a,c))\).

## Proof

**1. Product classes after a sign is forced.** If an observed answer forces a \(01\) column, then every other column must belong to \(\{00,01,11\}\). Among the remaining columns, each formerly unqueried one has three nested allowed two-bit strings, each of the other \(a\) half-queried columns has two options, and each of the \(c\) opposite-type half-queried columns becomes fixed neutral. These coordinates are independent. Such a product with \(v\) ternary nested columns and \(w\) binary half columns has Littlestone rank \(v+w\). For the lower bound, query each column once at an entry with two possible answers, obtaining a full tree of depth \(v+w\). For the upper bound, each query in a ternary column has one branch that fixes that column completely, and any query in a binary half column fixes it in both branches. An induction over \(v+w\) bounds the smaller successor rank by \(v+w-1\). Hence the dimension is exactly \(v+w\). The analogous conclusion holds if a \(10\) column is forced.

**2. Exact conditional recursion.** Define \(F(0,0,0)=0\). At an unqueried column, either edge query creates a half-queried neutral-or-\(01\) column in one answer branch and a half-queried neutral-or-\(10\) column in the other. Thus its candidate depth is
\[
1+\min\{F(u-1,a+1,c),F(u-1,a,c+1)\}\quad(u>0).
\]
A query at one of the \(a\) half-queried \(01\)-eligible columns either fixes it neutral (leaving \(F(u,a-1,c)\)) or fixes its mixed type, reducing the latter branch to a product of rank \(u+a-1\). The candidate depth is therefore
\[
1+\min\{F(u,a-1,c),u+a-1\}\quad(a>0).
\]
Similarly the candidate for a \(10\)-eligible half column is
\[
1+\min\{F(u,a,c-1),u+c-1\}\quad(c>0).
\]
There are no other nonconstant edge queries. This gives a well-founded recursion because every query removes one unqueried entry. With the induction formula below, the first branch rank in a half-column query is at least \(u+a-1\) or \(u+c-1\), respectively, so those candidate depths simplify exactly to \(u+a\) and \(u+c\).

**3. Solve the recursion for all parameters.** Put
\[
P=u+a,\qquad Q=u+c,\qquad R=\left\lceil\frac{3u+a+c}{2}\right\rceil.
\]
We prove by induction on the number \(2u+a+c\) of unresolved edge entries that \(F(u,a,c)=\max\{P,Q,R\}\). When \(u=0\), half-column queries have possible depths \(a\) and \(c\), giving \(F(0,a,c)=\max\{a,c\}\); since \(R\le\max\{a,c\}\), this is the formula. This includes the all-fixed base case.

Suppose \(u>0\). By induction, the two child ranks after querying an unseen column are
\[
\max\{P,Q-1,R-1\}\quad\text{and}\quad\max\{P-1,Q,R-1\}.
\]
If \(R>\max\{P,Q\}\), both children have rank \(R-1\), so the unseen-column query has depth \(R\), while each available half-column query has depth at most \(\max\{P,Q\}<R\).

Otherwise \(R\le\max\{P,Q\}\). We cannot have \(P=Q\): that would mean \(a=c\), and then \(R=a+\lceil3u/2\rceil>a+u=P\), because \(u>0\). Assume \(P>Q\), with the other case symmetric. Then \(a>c\), so \(a>0\) and a half-column query achieves depth \(P\). The unseen-column query has depth at most \(P\), since its second child has rank at most \(P-1\) (use \(Q\le P-1\) and \(R\le P\)); any other half-column query also has depth at most \(P\). Thus \(F=P\). This completes the induction and proves the all-parameter formula.

**4. Dimension and static comparison.** Initially all \(b\) columns are unqueried, so \(F(b,0,0)=\lceil3b/2\rceil\). For any undirected graph, a set of edge-direction queries is VC-shattered by all acyclic orientations exactly when it is a forest: every orientation of a forest is acyclic and extends by topological sorting, while a cycle can be cyclically directed to block one labeling. This is the established characterization of Kozma–Moran. The largest forest of the connected graph \(K_{2,b}\) has \(b+1\) edges, proving the stated known VC dimension and gap.

## Verification

The standalone, dependency-free script `verify_online_rank.py` independently enumerates all two-row orientation matrices for \(1\le b\le7\), tests each finite Littlestone dimension using the defining mistake-tree recursion on all reachable version spaces, and checks it against the exact formula. For \(1\le b\le5\), it also enumerates all edge-query supports to check the VC dimension and directly compares the forbidden-column characterization to directed-cycle detection in the graph. It also checks all 6,560 consistent partial-query assignments on up to four columns against the appropriate forced-sign or uncommitted conditional formula. Finally, it checks the three-parameter recurrence against its claimed closed form on 1,584 finite parameter triples. Its successful output is recorded in `VERIFICATION.md`. The exhaustive enumeration covers a finite parameter range only; the unrestricted result is proved above.

## Relationship to prior work

Kozma and Moran (2013) established that the edge sets shattered by all acyclic orientations of any graph are exactly forests, giving the VC-dimension comparison; their result is not claimed as new. Cameron, Glass, Rekvényi, and Schumacher (first publicly posted in 2014) identified complete-bipartite acyclic orientations with lonesum matrices and gave the count \(2\cdot3^b-2^b\) for \(K_{2,b}\). Blagoev's 2018 preprint studies enumeration of complete multipartite acyclic orientations. West (1995) independently studied the attainable numbers of reversible edges in individual acyclic orientations of the same graphs. These sources address static shattering, edge reversibility, or hypothesis counts, neither of which specifies the Littlestone rank of adaptive edge-membership queries. For example, at \(b=4\) the counting upper bound is \(\lfloor\log_2(146)\rfloor=7\), while the exact rank proved here is six. The new contribution is the adaptive rank and the full conditional-state classification, not the previously established orientation encoding, enumeration, or forest VC theorem.

## Limitations

This is a theorem for exactly two vertices in one bipartition class and individual edge-direction queries. It does not assert corresponding formulas for arbitrary complete bipartite graphs, other query models, or general lonesum-matrix restrictions. Numerical computations do not establish uniqueness or novelty against inaccessible literature. Priority under different online-learning or matrix terminology is a residual historical risk. No independently performed mathematical audit is asserted.

## References

1. L. Kozma and S. Moran, *Shattering, Graph Orientations, and Connectivity*, Electronic Journal of Combinatorics 20(3), P44 (2013), DOI:10.37236/3326. [Full text](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p44/pdf/).
2. P. J. Cameron, C. A. Glass, K. Rekvényi, and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, first posted 2014-12-11, arXiv:1412.3685. [Full text](https://arxiv.org/abs/1412.3685).
3. D. B. West, *Acyclic orientations of complete bipartite graphs*, Discrete Mathematics 138 (1995), 393–396, DOI:10.1016/0012-365X(94)00222-5. [Full text](https://dwest.web.illinois.edu/pubs/aobip.pdf).
4. V. Blagoev, *On the Number of Acyclic Orientations of Complete \(k\)-Partite Graphs*, first posted 2018-08-08, arXiv:1808.02787. [Full text](https://arxiv.org/abs/1808.02787).
