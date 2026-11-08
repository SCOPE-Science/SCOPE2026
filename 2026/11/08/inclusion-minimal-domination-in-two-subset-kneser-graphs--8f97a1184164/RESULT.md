# Inclusion-minimal domination in two-subset Kneser graphs

## Finding

For every integer \(n\ge4\), the inclusion-minimal ordinary dominating vertex sets of the Kneser graph \(KG(n,2)\) correspond, under the edge interpretation of its vertices, to exactly five root-graph families: a triangle, a complete star on all \(n\) root vertices, a five-cycle, a matching of three edges, or a proper double star with exactly two leaves at each center. Unused root labels are allowed except in the complete-star family. Every listed configuration fitting on \(n\) labels is inclusion-minimal, and no others occur.

Consequently, the polynomial enumerating inclusion-minimal dominating sets by their cardinality is
\[
M_n(z)=\left(\binom n3+15\binom n6\right)z^3+\left(12\binom n5+90\binom n6\right)z^5+nz^{n-1},
\]
with binomial coefficients interpreted as zero when their lower argument exceeds \(n\). If two displayed exponents coincide, their coefficients add. In particular, the number of inclusion-minimal dominating sets is
\[
M_n(1)=n+\binom n3+12\binom n5+105\binom n6.
\]
For \(n=4,5,6,7\), the respective polynomials are \(8z^3\), \(10z^3+5z^4+12z^5\), \(35z^3+168z^5\), and \(140z^3+882z^5+7z^6\). The upper domination number is \(3\) when \(n=4\) and \(\max\{5,n-1\}\) when \(n\ge5\). All inclusion-minimal dominating sets have the same size only for \(n=4\). From \(n\ge9\) the possible sizes are exactly \(\{3,5,n-1\}\), leaving arbitrarily long gaps.

## Assumptions and scope

The graph \(KG(n,2)\) has one vertex for every unordered two-element subset of \([n]=\{1,\ldots,n\}\), and two such vertices are adjacent if and only if their subsets are disjoint. A vertex set \(S\) is (ordinary) dominating if every vertex outside \(S\) has a neighbor in \(S\); it is inclusion-minimal if no proper subset of \(S\) is dominating. A selected Kneser vertex \(\{u,v\}\) is treated as an edge \(uv\) of an auxiliary simple graph \(H\) on all \(n\) root labels, possibly with isolated root vertices. The vertex-cover number \(\tau(H)\) is the least number of root vertices meeting all selected edges. Classification is by the edge sets themselves, not by root-label isomorphism alone.

The five families are specified without ambiguity: (i) the three edges of a triangle on any three root labels; (ii) all \(n-1\) edges incident to one root label; (iii) the five edges of a simple cycle on five root labels; (iv) three pairwise vertex-disjoint edges; (v) a tree with adjacent centers \(u,v\), exactly two other neighbors of \(u\), exactly two other neighbors of \(v\), and four distinct leaves. The last family has six root labels and five edges.

## Proof

**Step 1: a vertex-cover criterion.** An unselected Kneser vertex \(\{u,v\}\) is undominated precisely when every selected edge of \(H\) meets \(\{u,v\}\); equivalently, \(\{u,v\}\) is a two-vertex cover of \(H\) but \(uv\notin E(H)\). Thus
\[
S\text{ dominates }KG(n,2)\iff
\text{every two-vertex cover of }H\text{ is an edge of }H.
\]
This criterion automatically holds whenever \(\tau(H)\ge3\). Deleting edges from \(H\) corresponds to deleting vertices from \(S\), and domination is monotone under adding selected vertices. Hence it suffices to test every one-edge deletion to prove inclusion-minimality.

**Step 2: configurations of cover number at most two.** A graph \(H\) with \(\tau(H)=0\) selects no Kneser vertices, so it is not dominating. If \(\tau(H)=1\), every selected edge meets some root vertex \(u\). For each other root vertex \(v\), the pair \(\{u,v\}\) is a cover, so the criterion forces \(uv\in E(H)\). Thus \(H\) is the complete star, which is minimal: deleting any star edge \(uv\) makes the now-unselected pair \(uv\) an undominated vertex.

For \(\tau(H)=2\), choose a two-vertex cover \(\{u,v\}\). Domination forces \(uv\in E(H)\). Every other selected edge meets \(u\) or \(v\). Write \(A=N_H(u)\setminus\{v\}\) and \(B=N_H(v)\setminus\{u\}\), with both nonempty (otherwise the cover number is one). If \(|A|=1\), say \(A=\{a\}\), then \(\{v,a\}\) also covers \(H\), so domination forces \(va\in E(H)\). Hence the three edges \(uv,ua,va\) form a triangle, already a dominating set. Inclusion-minimality forces \(H\) to be exactly that triangle. The case \(|B|=1\) is symmetric.

If both \(|A|\) and \(|B|\) are at least two, \(\{u,v\}\) is the unique two-vertex cover of \(H\), and \(H\) is dominating. Deleting a leaf edge cannot destroy domination when its incident center still has at least two other external neighbors; thus inclusion-minimality forces \(|A|=|B|=2\). If \(A\cap B\ne\varnothing\), delete from the \(u\)-side the edge to a leaf outside the intersection (if necessary, exchange the two centers). The resulting graph has exactly the two covers \(\{u,v\}\) and \(\{v,a\}\), where \(a\in A\cap B\), both selected edges; it remains dominating, contradicting minimality. In detail, when \(A\ne B\), choose a leaf of \(A\setminus B\); when \(A=B\), choose either leaf, leaving the other common leaf. Therefore \(A\cap B=\varnothing\), and \(H\) is the stated proper double star. Conversely, deleting its center edge exposes the now-unselected cover \(\{u,v\}\), and deleting any leaf edge exposes the nonselected cover formed by the opposite center and the remaining leaf on the deleted edge's side. Every deletion therefore destroys domination.

**Step 3: cover number at least three.** Suppose an inclusion-minimal dominating \(H\) has \(\tau(H)\ge3\). For every selected edge \(e\), its deletion is non-dominating and therefore admits an unselected two-vertex cover \(B_e\) of \(H-e\). Since \(H\) has no cover of size two, \(B_e\) is disjoint from the endpoints \(A_e\) of \(e\), while \(B_e\) meets the endpoints of every other selected edge. In particular, \(\tau(H-e)\le2\), so \(\tau(H)=3\).

The following four-element set-pair argument bounds the number of edges of \(H\). For each edge \(e\), independently consider the event that, in a uniformly random ordering of all relevant root labels, both members of \(A_e\) appear before both members of \(B_e\). Its probability is \(1/\binom42=1/6\). Two different events cannot both occur: choose a label in \(A_e\cap B_f\) and another in \(A_f\cap B_e\); the two events would require the same two labels to occur in opposite relative orders. The events are pairwise disjoint, whence \(|E(H)|/6\le1\). Every such graph therefore has at most six edges, independently of \(n\).

**Step 4: exhaustive finite classification after the uniform bound.** An isolate-free simple graph with \(m\) edges is obtained from an isolate-free graph with \(m-1\) edges by adding an edge joining (a) two previously present nonadjacent vertices, (b) a present vertex to a new vertex, or (c) two new vertices: delete any edge and then discard the isolated vertices to see this inductively. Starting with the empty graph, generating these three extension types and identifying graphs by exact adjacency-preserving isomorphism gives respectively \(1,2,5,11,26,68\) classes with \(m=1,\ldots,6\) edges. The complete self-contained generator and verifier are supplied in `verify_minimal_kg2.py`; it performs an exhaustive backtracking isomorphism test, enumerates every vertex cover of size at most three, and checks the criticality condition for each class.

Exactly four of these classes have cover number three and drop to cover number at most two after every edge deletion: \(3K_2\), \(K_3\sqcup K_2\), \(C_5\), and \(K_4\). The middle graph \(K_3\sqcup K_2\) is not inclusion-minimal dominating, because deleting its isolated-edge component leaves the dominating triangle. The graph \(K_4\) is not inclusion-minimal dominating, because deleting any edge leaves a graph whose only two-vertex cover is the selected opposite edge. By contrast, deleting any edge from \(3K_2\) exposes an unselected transversal of the two remaining disjoint edges, and deleting any edge from \(C_5\) exposes an unselected two-vertex cover of the resulting five-vertex path. These two classes are therefore exactly the inclusion-minimal dominating cases with cover number three.

Together with Step 2, this proves both necessity and sufficiency of the five families for all \(n\ge4\). The finite census is exhaustive because of the proved six-edge bound; direct enumerations at small \(n\) are corroborations rather than an extrapolation to all \(n\).

**Step 5: enumeration and consequences.** Labeled triangles contribute \(\binom n3\) sets; complete stars contribute \(n\); labeled five-cycles contribute \((5-1)!/2=12\) per five root labels; three-edge matchings contribute \(6!/(2^3 3!)=15\) per six labels. For double stars choose the two centers in \(\binom62=15\) ways and the two leaves attached to the smaller-labeled center in \(\binom42=6\) ways, giving \(90\) structures on six labels. The five families are disjoint, proving the polynomial. The minimum size is three; the upper domination number, possible sizes, and gap assertion follow by comparing the three allowed exponents \(3\), \(5\), and \(n-1\), including the small orders separately.

## Verification

Run `python3 verify_minimal_kg2.py` using the supplied standard-library-only source file. Its two independent finite checks are (1) exhaustive isolate-free graph-type generation through six edges, confirming the four cover-critical types and the two ordinary-domination-minimal types in Step 4; and (2) direct Kneser-graph adjacency and dominating-set enumeration for every vertex subset at orders \(4,5,6,7\), confirming the five-family classification and all coefficients. The direct check visits \(2{,}131{,}004\) nonempty vertex subsets and finds respectively \(8,27,203,1029\) minimal dominating sets. The checks are not a substitute for Steps 1–3, which justify why the finite census settles all orders.

## Relationship to prior work

Ivančo and Zelinka (1993) proved the ordinary domination number \(\gamma(KG(n,2))=3\) and characterized dominating triples for orders at least five. Cornet and Torres (first public preprint August 29, 2023) considered multiple domination and gave a root-incidence characterization of \(k\)-tuple domination on \(KG(n,2)\), focusing on minimum cardinalities and \(k\ge2\). The five-family **inclusion-minimal ordinary** classification, all-cardinality minimal-set polynomial, and unbounded gaps are not implied merely by their minimum-cardinality results. The general minimal-dominating-set enumeration literature supplies algorithms and bounds rather than the present explicit two-subset Kneser formula. Related complete classifications of minimal *total* or *paired* dominating sets do not imply ordinary minimal domination: for example, triangles and complete stars are ordinary dominating sets but not total dominating sets when the corresponding Kneser vertices have no selected neighbors.

## Limitations

This is a mathematical proof and self-review, not independent validation. All explicit computation is finite, with the universal conclusion justified by the six-edge lemma and a complete finite isomorphism-class census. Publication-priority uncertainty remains because searches and inspected works cannot rule out an equivalent result under different terminology or in unindexed sources. No formula for every (not necessarily minimal) dominating set is claimed, nor is a generalization to \(KG(n,r)\) for \(r>2\) established.

## References

- M. G. Cornet and P. Torres, *\(k\)-tuple domination on Kneser graphs*, arXiv:2308.15603, first public version August 29, 2023, https://arxiv.org/abs/2308.15603 .
- J. Ivančo and B. Zelinka, *Domination in Kneser graphs*, Mathematica Bohemica 118 (1993), 147–152, https://dml.cz/handle/10338.dmlcz/126050 .
- I. Gorodezky, *Dominating sets in Kneser graphs*, University of Waterloo master's thesis, 2007, https://uwspace.uwaterloo.ca/items/162bbbfc-6952-4188-8d4a-e403b81807c4 .
- M. M. Kanté, V. Limouzy, A. Mary, and L. Nourine, *On the enumeration of minimal dominating sets and related notions*, SIAM J. Discrete Math. 28 (2014), 1916–1929, https://doi.org/10.1137/120862612 .
