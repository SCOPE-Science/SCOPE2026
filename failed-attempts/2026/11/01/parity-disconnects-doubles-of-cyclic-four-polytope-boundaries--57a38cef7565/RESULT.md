# Parity disconnects doubles of cyclic four-polytope boundaries

## Finding
For every integer \(n\ge 5\), let \(C(n,4)\) be the cyclic four-dimensional convex polytope on moment-curve vertices labeled \(0,1,\ldots,n-1\) in increasing parameter order, and let \(X_n=\partial C(n,4)\) be its boundary simplicial complex. Let \(D_2(X_n)\) be the double of Lesh–Schreiner–Wahl: vertices are two-element faces of \(X_n\), and two such vertices span an edge if their union is a four-element face of \(X_n\).

If \(n\) is odd, then the double is connected and
\[
|D_2(X_n)|\simeq \bigvee^{\,n(n-4)+1}S^1.
\]
If \(n\) is even, then it has exactly two connected components. The component indexed by pairs of vertices with **equal** parity and the component indexed by pairs with **opposite** parity have homotopy types, respectively,
\[
\bigvee^{\,n(n-4)/4+1}S^1
\quad\text{and}\quad
\bigvee^{\,3n(n-4)/4+1}S^1.
\]
In particular, for even \(n\), the reduced zeroth integral homology is \(\mathbb Z\), carried trivially by cyclic rotation and reflection of the moment-curve labeling; for odd \(n\), it vanishes. All higher reduced homology except degree one vanishes, and the displayed degree-one groups are free abelian. The even case gives an infinite family of triangulated three-spheres whose doubles are disconnected.

## Assumptions and scope
The cyclic four-polytope is the convex hull of \((t,t^2,t^3,t^4)\) at any \(n\) distinct increasing real parameters. Its boundary is a triangulated three-sphere. All indices in combinatorial arguments are taken modulo \(n\), and a **cycle edge** means \(\{i,i+1\}\) in the fixed cyclic order. The double is the *ordinary abstract simplicial complex* of Definition 2.1 in the first reference, not the geometric double along a manifold boundary. The homotopy equivalences are ordinary, not asserted equivariant. The endpoint convention \(n\ge5\) includes the boundary of the four-simplex at \(n=5\).

## Proof
**1. Four-faces.** Cyclic four-polytopes are two-neighborly: every two-element vertex set is an edge. By Gale's evenness criterion, their facets are precisely the four-sets that can be partitioned into two vertex-disjoint cycle edges of \(C_n\). For completeness, among vertices omitted from a prospective facet the number of selected vertices between consecutive omitted vertices must be even. Since exactly four are selected, this means that the selected vertices occur as two adjacent pairs in the cyclic order; the pair crossing the last-to-first vertex is allowed. Conversely such two adjacent pairs satisfy the evenness test. For \(n=5\), the test has only one omitted vertex and every four-set is a facet; each is still the union of two disjoint cycle edges. The partition into two disjoint cycle edges is unique for \(n\ge5\): the induced subgraph of the simple cycle on four vertices is a union of paths, and a union of paths has at most one perfect matching. Thus the number of facets is the number of unordered disjoint pairs of cycle edges,
\[
F_n=\frac{n(n-3)}2.
\]

**2. Doubling graph.** As \(X_n\) has dimension three, its double has no simplices of dimension at least two. It is the graph \(H_n\) on all \(\binom n2\) unordered pairs \(\{i,j\}\). The vertices \(\{i,j\}\) and \(\{k,l\}\) are adjacent exactly when their four endpoints are distinct and their union is two disjoint cycle edges. Every facet yields its three perfect matchings, hence exactly three distinct graph edges. Conversely an edge determines its four endpoints and thus its facet, so there is no overcount. Therefore
\[
V(H_n)=\frac{n(n-1)}2,\qquad E(H_n)=\frac{3n(n-3)}2.
\]

**3. Connectedness and the parity obstruction.** Put \(a_i=\{i,i+1\}\). Two such vertices are adjacent in \(H_n\) when their cycle edges are disjoint. For every \(n\ge5\), \(a_i\) and \(a_{i+1}\) are joined by the two-edge path through \(a_{i+3}\). Thus all cycle-edge vertices lie in a single component. For any pair \(\{i,j\}\), choose a cyclic arc from \(i\) to \(j\) of odd length \(d\). If \(d=1\), this is already a cycle-edge vertex. If \(d\ge3\), then
\[
\{i,j\}\sim\{i+1,j-1\}
\]
is an edge in \(H_n\), since the union is the facet made from the two disjoint cycle edges \(\{i,i+1\}\) and \(\{j-1,j\}\). The chosen arc shortens by two. Repeating reaches a cycle-edge vertex. When \(n\) is odd, one of the two arcs between any pair has odd length, so \(H_n\) is connected. When \(n\) is even, the same argument joins every pair with opposite-parity endpoints to the cycle-edge component.

For even \(n\), a facet has two even and two odd endpoints, since it consists of disjoint edges of an even cycle. Its three pairings consist of two pairings into opposite-parity pairs and one pairing into same-parity pairs. Hence no graph edge joins the opposite-parity and same-parity vertex sets. Every same-parity pair has an even cyclic arc. Moving both ends inwards along that arc, as above, reduces its length by two until the pair is \(b_i=\{i,i+2\}\) for some \(i\). For each \(i\), the consecutive short chords \(b_i,b_{i+1}\) are adjacent because their union consists of cycle edges \(\{i,i+1\}\) and \(\{i+2,i+3\}\). Thus all same-parity pairs form one connected component. Exactly two components occur.

**4. Exact circle ranks.** Every finite connected graph is homotopy equivalent to a wedge of \(E-V+1\) circles. For odd \(n\), Step 2 yields \(3n(n-3)/2-n(n-1)/2+1=n(n-4)+1\). For even \(n\), write \(m=n/2\). There are \(m^2=n^2/4\) opposite-parity vertices and \(2\binom m2=n(n-2)/4\) same-parity vertices. Each of the \(F_n\) facets contributes two graph edges in the former component and one in the latter, by Step 3. Thus their respective circle ranks are
\[
2F_n-\frac{n^2}{4}+1=\frac{3n(n-4)}4+1,
\qquad
F_n-\frac{n(n-2)}4+1=\frac{n(n-4)}4+1.
\]
Cyclic rotation and reflection preserve the equal-parity versus opposite-parity relation for even \(n\), so neither component is exchanged. The claimed reduced zeroth-homology action follows. This completes the proof.

## Verification
The included standalone `verify.py` independently tests the four-facet lists in three ways: exact signs of the degree-four moment-curve supporting polynomial, Gale evenness, and unions of two disjoint edges of a cyclic graph. It then constructs every vertex and edge of the doubled graph, computes exact connected components by union–find, and checks component vertex counts, edge counts, and the stated integral first-Betti ranks for every \(5\le n\le24\) and \(n=28,29,30,31,32\). No floating-point calculations or external dependencies are used. These finite tests corroborate, but do not replace, the argument for every \(n\ge5\). Run with `python3 verify.py`.

## Relationship to prior work
Lesh–Schreiner–Wahl introduce the double and prove a general weak Cohen–Macaulay connectivity bound. Applied to a triangulated three-sphere with doubling parameter two, their bound guarantees only the nonempty-connectivity level; it neither identifies connected components nor circle ranks. The even family here shows that a uniform connectedness conclusion is impossible even for cyclic-polytopal three-spheres. Their matching-complex identification applies to the **full simplex**. For the initial case \(n=5\), doubling its boundary coincides with doubling that full simplex (the familiar matching complex of \(K_5\)); this initial case is not claimed as new. For every \(n\ge6\), the cyclic-polytope boundary is a genuine restriction and has a different doubling graph, with the parity transition established here. Classical Gale evenness and neighborliness supply the facet classification used in the proof, but do not themselves state the double's homotopy type. No claim is made that these earlier tools are new.

## Limitations
The conclusion is restricted to cyclic four-polytope boundaries with \(n\ge5\), and does not classify doubles of other three-spheres, higher-dimensional cyclic polytopes, or higher-tupling complexes. An arbitrary finite connected graph has a circle-wedge homotopy type; the content here is the exact parity-dependent component decomposition and ranks for this canonical infinite family. The result asserts an ordinary homotopy classification and an action on reduced degree-zero homology, not full equivariant homotopy or a degree-one representation formula. Independent review has not been performed.

## References
1. K. Lesh, B. Schreiner and N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436, first posted 12 June 2025, Definition 2.1 and Theorem A (and revised manuscript, 27 October 2026). https://arxiv.org/abs/2506.10436
2. G. M. Ziegler, *Lectures on Polytopes*, Graduate Texts in Mathematics 152, Springer (1995), Theorem 0.7 (Gale's evenness criterion). See also the accessible exposition *15 Basic Properties of Convex Polytopes*, section on cyclic polytopes: https://paperzz.com/doc/9459585/15-basic-properties-of-convex-polytopes
