# Exact online shattering of acyclic orientations of triangular books

## Finding

Let \(B_b\), for any integer \(b\geq0\), be the graph consisting of one edge joining two anchor vertices, together with \(b\) additional vertices each adjacent to both anchors and to no other additional vertex. Thus \(B_b=K_2\vee\overline{K_b}\). Let \(\mathcal A(B_b)\) be the class of all acyclic orientations, viewed as binary hypotheses on the edge set: a query reveals the direction of one specified edge. Then

\[
\operatorname{Ldim}(\mathcal A(B_b))=1+\left\lfloor\frac{3b}{2}\right\rfloor.
\]

The formula is a specialization of a complete conditional-state theorem. For nonnegative integers \(u,a,c\), let \(\mathcal F(u,a,c)\) have one binary selector \(e\), \(u\) two-bit columns, \(a\) one-bit columns of the first type, and \(c\) one-bit columns of the second type. For \(e=0\), each full column ranges independently over \(\{00,10,11\}\), each first-type column over \(\{0,1\}\), and each second-type column is fixed to \(0\). For \(e=1\), full columns range over \(\{00,01,11\}\), first-type columns are fixed to \(0\), and second-type columns range over \(\{0,1\}\). The selector itself is always queried as a distinct binary coordinate. Then, with all three parameters quantified over nonnegative integers,

\[
\operatorname{Ldim}(\mathcal F(u,a,c))=
\max\!\left\{u+a,\;u+c,\;1+\left\lfloor\frac{3u+a+c}{2}\right\rfloor\right\}.
\]

For every \(b\ge0\), the same graph family has \(\operatorname{VCdim}(\mathcal A(B_b))=b+1\). Thus the online-minus-static gap is \(\lfloor b/2\rfloor\), growing without bound on a family of chordal graphs of clique number at most three. As a contextual comparison, the previously established online rank for \(K_{2,b}\) is \(\lceil3b/2\rceil\); adding the edge between its two degree-\(b\) vertices changes the online dimension by one exactly when \(b\) is even, while its VC dimension remains \(b+1\).

## Assumptions and scope

All graphs are finite and simple, all orientations assign one of the two directions to every edge, and only acyclic orientations are hypotheses. Littlestone dimension is the maximum depth of a complete binary mistake tree with an edge query at each internal node, having a consistent orientation on every root-to-leaf path. A singleton hypothesis class has Littlestone dimension zero. The empty list of pages, \(b=0\), is allowed; its graph is a single edge and has online rank one.

The selector encoding is as follows. The binary selector records the direction of the shared anchor edge. For one selector value, the two directions on a page belong to the three allowed patterns \(00\), \(10\), and \(11\); for the other selector value, the allowed patterns are \(00\), \(01\), and \(11\). These are precisely the orientations of a triangle avoiding a directed three-cycle. Since every simple cycle in \(B_b\) is made up of triangles sharing the anchor edge or of four-cycles using two pages, the triangle constraints also exclude directed four-cycles: a directed four-cycle would exhibit both forbidden mixed page patterns, which no common selector permits. Equivalently, the graph is chordal, so a shortest directed cycle in an orientation must be a directed triangle. The \(b\) pages are conditionally independent once the selector is fixed; hence \(\mathcal A(B_b)\) is the class \(\mathcal F(b,0,0)\).

## Proof

Write \(F(u,a,c)=\operatorname{Ldim}(\mathcal F(u,a,c))\) and define

\[
p=u+a,\qquad q=u+c,\qquad h=1+\left\lfloor\frac{3u+a+c}{2}\right\rfloor,\qquad G(u,a,c)=\max\{p,q,h\}.
\]

For any nonempty finite hypothesis class, the defining complete-tree recurrence says its online rank is the maximum, over coordinates for which both labels occur, of one plus the minimum of the two restricted ranks. The relevant restrictions can be listed exactly here. A selector query yields independent product classes of ranks \(u+a=p\) and \(u+c=q\), because a full three-pattern two-bit column has online rank one, a free one-bit column has rank one, and online ranks of products on disjoint coordinates add. (For clarity, product additivity follows by concatenating complete mistake trees for the lower bound; for the upper bound, a query in one factor has a branch whose factor rank decreases, and induction on the number of hypotheses bounds the product rank by the sum.) Therefore a selector query contributes \(1+\min(p,q)\).

If \(u>0\), querying either bit of one full column yields, up to a separate inversion of the remaining bit, the two conditional classes \(\mathcal F(u-1,a+1,c)\) and \(\mathcal F(u-1,a,c+1)\). Hence the full-column option contributes

\[
1+\min\{F(u-1,a+1,c),F(u-1,a,c+1)\}.
\]

If \(a>0\), querying a first-type bit has a positive branch in which the selector is forced to zero and exactly \(u+a-1\) independent binary learning decisions remain; the other branch has class \(\mathcal F(u,a-1,c)\). Thus this option is \(1+\min\{p-1,F(u,a-1,c)\}\). A second-type bit analogously contributes \(1+\min\{q-1,F(u,a,c-1)\}\) when \(c>0\). These are all possible queries.

We prove \(F=G\) by induction on \(u+a+c\). For \(u=0\), a selector query supplies rank \(1+\min(a,c)\); fixing the selector and taking the class of free first- or second-type bits supplies ranks \(a\) and \(c\). A first-type query has rank at most \(a\) by the displayed recurrence, and a second-type query at most \(c\). The induction therefore gives

\[
F(0,a,c)=\max\{a,c,1+\min(a,c)\}=\max\!\left\{a,c,1+\left\lfloor\frac{a+c}{2}\right\rfloor\right\}=G(0,a,c).
\]

This also covers the base \(F(0,0,0)=1\), since the selector distinguishes two hypotheses.

For \(u>0\), apply the induction hypothesis to the two full-column branches. Their ranks are, respectively,

\[
G(u-1,a+1,c)=\max\{p,q-1,h-1\},\qquad
G(u-1,a,c+1)=\max\{p-1,q,h-1\}.
\]

Assume without loss of generality \(p\ge q\). The first displayed maximum is \(\max\{p,h-1\}\); it is at least the second. The full-column query therefore attains

\[
1+\max\{p-1,q,h-1\}=\max\{p,q+1,h\}=\max\{p,q,h\}=G(u,a,c),
\]

where \(h\ge q+1\) follows from \(u\ge1\) and \(p\ge q\). The case \(q\ge p\) is symmetric. A selector query contributes at most \(G\), since \(h\ge1+\min(p,q)\). A first-type query contributes at most \(p\le G\), and a second-type query at most \(q\le G\). Thus no query gives greater rank, completing the induction and the conditional-state theorem. Substitution \((u,a,c)=(b,0,0)\) proves the displayed book-graph formula.

For completeness, the static VC calculation does not depend on the online recurrence. A queried edge set \(S\) is shattered by acyclic orientations of any graph if and only if the graph induced by its edges is a forest. Every orientation of a forest is acyclic and can be extended to an acyclic orientation of the whole graph by choosing a topological order and orienting every remaining edge forward. Conversely, a queried cycle can be given a directed cyclic pattern, which no acyclic orientation realizes. Since the connected graph \(B_b\) has \(b+2\) vertices, its maximum forest contains \(b+1\) edges. Hence its VC dimension is exactly \(b+1\), and subtracting proves the claimed gap.

## Verification

The standalone standard-library checker at `verification/check.py` independently enumerates all binary orientations and detects directed cycles for \(0\le b\le6\). It compares the resulting hypothesis families to the two-pattern selector representation and recomputes Littlestone ranks directly from the complete-tree recurrence. It also checks the proposed conditional-state formula on all checked triples of total size at most six, confirms the forest shattering characterization through four pages, and verifies the closed-form recursion on 64,000 further parameter triples. Running `python3 verification/check.py` produced:

`BOOK_ORIENTATION_ONLINE_PASS b=0..6 conditional_states=84 recurrence_triples=64000`

These finite checks do not prove the unrestricted statement; the induction above supplies the all-parameter proof.

## Relationship to prior work

Kozma and Moran (2012/2013) characterize ordinary shattering for acyclic graph orientations and derive its forest-based VC dimension. That static statement is acknowledged and is not claimed to be new here. Pikhurko (2009) studies the worst-case number of membership questions needed to **identify** an unknown acyclic orientation; that decision-tree search objective differs from the largest depth of a complete adversarial mistake tree, and its stated bounds do not imply the online rank here. Cardinal, Hoang, Merino, Mička and Mütze (2022) study Gray-code generation and reorientation lattices of chordal-graph orientations. Their simplicial-vertex insertion construction explains a known enumeration of the present hypothesis family, but is not an exact Littlestone-rank calculation. Dong et al. (2018) relate counts of acyclic orientations to chromatic coefficients, not to online shattering ranks.

A separate prior exact rank for orientations of \(K_{2,b}\) concerns a different query domain lacking the common-edge selector. Its formula is used only as a comparison. The new result is the exact rank of the chordal triangular book and the stronger three-parameter conditional recurrence. Literature searches have not supplied a claim covering these conclusions, but historical priority under a different name for the orientation mistake-tree parameter remains a limitation.

## Limitations

The theorem concerns binary edge-direction queries and acyclic orientations of the stated graph family only. It does not compute identification decision-tree complexity or the rank for arbitrary chordal graphs. Complete-tree optimality is established by an induction on abstract residual classes; it does not provide a polynomial-size explicit tree for large input (such trees have exponentially many leaves). The literature comparison is based on accessible published texts and database queries, not an exhaustive proof of novelty. Independent mathematical review remains unperformed.

## References

1. J. Cardinal, H. P. Hoang, A. Merino, O. Mička, and T. Mütze, *Combinatorial generation via permutation languages. V. Acyclic orientations*, arXiv:2212.03915v1, first publicly posted 2022-12-07; SIAM Journal on Discrete Mathematics 37 (2023), 1509–1547. https://arxiv.org/abs/2212.03915
2. O. Pikhurko, *Finding an Unknown Acyclic Orientation of a Given Graph*, arXiv:0904.1229v1 (2009). https://arxiv.org/abs/0904.1229
3. L. Kozma and S. Moran, *Shattering, Graph Orientations, and Connectivity*, arXiv:1211.1319v1 (2012); Electronic Journal of Combinatorics 20(3) (2013), P44. https://arxiv.org/abs/1211.1319
4. F. Dong, J. Ge, H. Gong, B. Ning, Z. Ouyang, and E. G. Tay, *Proving a conjecture on chromatic polynomials by counting the number of acyclic orientations*, arXiv:1803.08658v1 (2018). https://arxiv.org/abs/1803.08658
