# Exact low-variable logical separation of diameter-two Moore graphs

## Finding
Let \(\mathcal M\) be the family of finite simple undirected Moore graphs of diameter two and degree \(d\ge2\), regarded in the language consisting only of equality and adjacency. Write \(\equiv_{\mathrm{FO}^{k}}\) for equivalence under all counting-free first-order sentences using at most \(k\) distinct variable names, with no restriction on quantifier depth.

**Theorem.** For any \(G,H\in\mathcal M\) of degrees \(d,e\ge2\):

1. \(G\equiv_{\mathrm{FO}^{2}}H\).
2. \(G\equiv_{\mathrm{FO}^{3}}H\) if and only if \((d=2\Leftrightarrow e=2)\).
3. If \(d=3\) and \(e\ge4\), the least variable width of a first-order sentence distinguishing \(G\) from \(H\) is exactly four.

In particular, for the three unconditionally existing diameter-two Moore graphs—the five-cycle, Petersen graph, and Hoffman–Singleton graph—the exact pairwise minimum distinguishing widths are, respectively, three for five-cycle versus Petersen, three for five-cycle versus Hoffman–Singleton, and four for Petersen versus Hoffman–Singleton. The statements involving degree greater than seven are conditional on the existence of a Moore graph of that degree; no assertion that a degree-57 Moore graph exists is made.

## Assumptions and scope
A diameter-two Moore graph of degree \(d\) is a finite simple graph attaining the diameter-two Moore bound. Consequently it is \(d\)-regular of order \(d^2+1\), with no triangles or four-cycles. Equivalently, for distinct vertices, adjacent pairs have zero common neighbors and nonadjacent pairs have exactly one common neighbor. The only possible degrees are \(2,3,7\) and, conditionally, \(57\); the degree-two case is the five-cycle.

All equivalences are in the **pure undirected adjacency language without counting quantifiers**. Graphs need not have the same number of vertices. There is no bound on quantifier rank. All logical claims are about whole graphs, not rooted or expanded graphs.

## Proof
**Two variables.** In the ordinary two-pebble game, after one pebble is lifted, at most one stationary vertex remains. Every vertex in every member of \(\mathcal M\) has both a distinct neighbor (there are \(d\)) and a distinct nonneighbor (there are \(d(d-1)\)). The responder can therefore match equality or non-equality and adjacency or nonadjacency in every round. This permanent strategy proves assertion 1.

**Three variables.** Suppose two distinct stationary vertices are \(x,y\). For a fresh vertex distinct from both, the numbers of witnesses with adjacency pattern to \((x,y)\), in the order \((00,01,10,11)\), are
\[
\begin{array}{c|cccc}
&00&01&10&11\\\hline
x\sim y&(d-1)^2&d-1&d-1&0\\
x\not\sim y&d(d-2)&d-1&d-1&1.
\end{array}
\]
For adjacent pairs, each vertex has \(d-1\) neighbors other than the opposite endpoint, and those two neighborhoods are disjoint. For nonadjacent pairs, the unique common neighbor gives the \(11\) entry and leaves \(d-1\) exclusive neighbors per endpoint. Subtraction from \(d^2+1\) gives the \(00\) entries. When the stationary pebbles coincide or fewer pebbles remain, the two-variable argument applies.

For every \(d\ge3\), the *supports* (positive-versus-zero patterns) of both rows are independent of \(d\). A responder can match every legal third-pebble choice while retaining the adjacency and equality pattern of the stationary pair. After any subsequent move the same argument applies afresh, giving a winning strategy at every finite length and hence equivalence at unrestricted quantifier depth.

When \(d=2\), the nonadjacent-pair \(00\) entry vanishes. The graph is the five-cycle, with no independent triple. For \(d\ge3\), any three neighbors of a common vertex form an independent triple, since the graph has no triangles. Thus the three-variable sentence asserting the existence of three pairwise distinct, pairwise nonadjacent vertices separates exactly the degree-two member. This establishes assertion 2.

**A four-variable separator.** Let \(I(x,y,z)\) abbreviate that \(x,y,z\) are distinct and pairwise nonadjacent. Consider the sentence
\[
\begin{split}
\Phi:=\exists x\,\exists y\,\exists z\;\bigl(&I(x,y,z)\ \land\\
&\exists w\,[E(w,x)\land E(w,y)\land E(w,z)]\ \land\\
&\forall w\,[w=x\lor w=y\lor w=z\lor E(w,x)\lor E(w,y)\lor E(w,z)]\bigr).
\end{split}
\]
The same fourth variable \(w\) is reused in two disjoint quantifier scopes; \(\Phi\) belongs to \(\mathrm{FO}^{4}\). For any independent triple \(x,y,z\) having a common neighbor \(t\), the common neighbor of each pair is uniquely \(t\). Therefore, apart from \(t\), the three neighborhoods are pairwise disjoint and each contributes \(d-1\) points. The number of vertices outside the triple adjacent to none of its members equals
\[
(d^2+1)-3-\bigl(1+3(d-1)\bigr)=d(d-3).
\]
A centered independent triple exists for every \(d\ge3\): take three neighbors of any vertex. If \(d=3\), the displayed number is zero, so \(\Phi\) holds. If \(d\ge4\), it is positive for *every* centered independent triple, so \(\Phi\) fails. Assertion 2 gives the matching three-variable non-separation, proving the sharp width in assertion 3.

No argument requires a hypothetical degree-57 graph to exist; it uses only the defining Moore conditions whenever such a graph is supplied.

## Verification
The standalone standard-library program `verify.py` builds the five-cycle, the Petersen graph from disjoint two-subsets of a five-point set, and the Hoffman–Singleton graph using ten pentagons/pentagrams and the modular cross-edge rule. It independently checks regularity, order, and all pairwise common-neighbor conditions, exhausts every unordered stationary pair and all four nonalgebraic adjacency patterns, and exhausts every centered independent triple for the exact \(d(d-3)\) anti-neighbor count. Run `python3 verify.py` from the directory containing the program. The recorded replay appears in `verification_output.txt`.

On the five-cycle, Petersen, and Hoffman–Singleton graphs the program checks, respectively, \(10\), \(45\), and \(1225\) distinct unordered stationary pairs, and \(0\), \(10\), and \(1750\) centered independent triples. All asserted identities pass. The proof for every possible degree and all quantifier depths is mathematical, not an inference from these three finite computations.

## Relationship to prior work
Hoffman and Singleton (1960) established the diameter-two Moore degree possibilities and the graph-theoretic adjacency identities used here. Grohe and Otto (2012) describe the ordinary finite-variable logic/pebble-game correspondence and its distinction from counting logic. Neither examined portion directly states this classification of Moore graphs by counting-free two- and three-variable theories, or this particular four-variable separation. The contribution is the exact specialization and sharp logical boundary, not a new existence theorem for Moore graphs or a new general pebble-game theorem.

For contrast, counting quantifiers with two variable names can distinguish the different Moore degrees immediately, by counting neighbors. The counting-free three-variable indistinguishability across degrees three and seven therefore cannot be inferred from counting-logic equivalence.

## Limitations
The theorem classifies the two-variable and three-variable theories of diameter-two Moore graphs and provides the sharp four-variable separation of degree three from higher degrees. It does **not** classify all four-variable equivalence classes among degrees seven and fifty-seven, settle existence of the degree-57 graph, apply to arbitrary strongly regular graphs, or apply to a counting or enriched language. The originality comparison is not an exhaustive historical-priority guarantee; a general theorem in finite-model-theoretic literature may imply the specialization. Independent mathematical audit has not been performed.

## References
1. A. J. Hoffman and R. R. Singleton, *On Moore Graphs with Diameters 2 and 3*, IBM Journal of Research and Development **4** (1960), 497–504, DOI: 10.1147/RD.45.0497.
2. Martin Grohe and Martin Otto, *Pebble Games and Linear Equations*, CSL 2012, 289–304, DOI: 10.4230/LIPIcs.CSL.2012.289; arXiv:1204.1990 (first posted 2012-04-09).
