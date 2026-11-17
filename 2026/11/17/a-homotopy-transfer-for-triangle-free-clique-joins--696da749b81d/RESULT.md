# A homotopy transfer for triangle-free clique joins

## Finding

Let \(H\) be any finite, nonempty, simple triangle-free graph, let \(s\ge 2\) be an integer, and let \(G=K_s\vee H\) denote the graph join. The three-clique-free complex \(\mathsf{CF}_3(G)\) contains precisely those vertex subsets inducing no triangle. Then the **integral homotopy type** is

\[
\mathsf{CF}_3(K_s\vee H)\ \simeq\
\left(\bigvee^{\binom{s}{2}}S^1\right)\ \vee\
\left(\bigvee_{i=1}^{s}\Sigma |\operatorname{Ind}(H)|\right).
\]

Here \(\operatorname{Ind}(H)\) is the ordinary independence complex, \(|\cdot|\) denotes geometric realization, \(\Sigma\) is the **unreduced** suspension, and the empty wedge of circles is interpreted as a point. The suspension is unreduced, so the formula also applies when the independence complex is disconnected. The displayed splitting is non-equivariant.

Equivalently, for each integer \(d\ge 1\), the integral reduced homology satisfies

\[
\widetilde H_d(\mathsf{CF}_3(K_s\vee H);\mathbb Z)
\cong\
\begin{cases}
\mathbb Z^{\binom{s}{2}}\oplus \widetilde H_0(\operatorname{Ind}(H);\mathbb Z)^{\oplus s}, &d=1,\\
\widetilde H_{d-1}(\operatorname{Ind}(H);\mathbb Z)^{\oplus s}, &d\ge2.
\end{cases}
\]

For a concrete connected, nonchordal input, \(H=C_6\) has \(\operatorname{Ind}(C_6)\simeq S^1\vee S^1\), and therefore
\[
\mathsf{CF}_3(K_3\vee C_6)\simeq
\bigvee^3S^1\vee\bigvee^6S^2.
\]

## Assumptions and scope

All graphs are finite and simple, with their vertex sets disjoint before forming the graph join. The graph \(H\) has **at least one vertex** and no triangles. It may contain isolated vertices, edges, even or odd cycles of length at least four, and disconnected components. The central complete graph has \(s\ge2\) vertices; no connectivity or purity hypothesis is needed. Homotopy equivalences are those of ordinary topological spaces underlying finite simplicial complexes.

## Proof

Write \(U=V(H)\), \(C=\{c_1,\ldots,c_s\}\), and \(B=\operatorname{Ind}(H)\). Set \(A=2^U\), the full simplex on \(U\). Since \(H\) is triangle-free, a set containing only vertices of \(U\) is always a face of the three-clique-free complex, so its induced subcomplex is exactly \(A\). Because \(U\ne\varnothing\), \(|A|\) is nonempty and contractible.

The only triangles in \(K_s\vee H\) have either (i) three vertices in \(C\), (ii) two vertices in \(C\) and one in \(U\), or (iii) one vertex in \(C\) and an edge of \(H\). There are no triangles fully in \(U\). Therefore a face has either no central vertex and an arbitrary subset of \(U\), exactly one central vertex \(c_i\) and an independent subset of \(U\), or exactly two central vertices and **no** vertex of \(U\). No face contains three central vertices. Consequently there is an **equality of simplicial subcomplexes**

\[
X:=\mathsf{CF}_3(K_s\vee H)
=A\ \cup\ K_s^{(1)}\ \cup\ \bigcup_{i=1}^{s}(c_i*B).
\]

Here \(K_s^{(1)}\) is the one-dimensional simplex skeleton on \(C\); each \(c_i*B\) is the simplicial cone with apex \(c_i\), and each cone meets \(A\) along its entire base \(B\).

As \(A\subseteq X\) is a nonempty contractible CW subcomplex, the quotient \(|X|\to |X|/|A|\) is a homotopy equivalence: the inclusion is a cofibration, the quotient induces isomorphisms of homotopy groups by the cofibration long exact sequence, and Whitehead's theorem applies to finite CW complexes. Equivalently, collapsing a contractible subcomplex of a finite CW complex is a homotopy equivalence.

After collapsing \(A\) to a point \(p\), each cone \(c_i*B\) with base \(B\) identified with \(p\) becomes the **unreduced suspension** of \(|B|\), with tips \(p\) and \(c_i\). The distinct suspended copies meet only at \(p\); the edges of \(K_s^{(1)}\) join their other tips. Choose one vertex \(u\in U\), so \(\{u\}\in B\). In each suspension the image of the edge \(\{c_i,u\}\) is an embedded edge \(e_i\) between \(p\) and \(c_i\). Their union \(T=\bigcup_{i=1}^s e_i\) is a contractible star tree, a CW subcomplex.

Collapse \(T\) to a point. This is another homotopy equivalence, because \(T\) is a contractible cofibration subcomplex. Within each suspension, collapsing its chosen tip-to-tip edge preserves the suspension's homotopy type (it is a contractible subcomplex). The \(\binom{s}{2}\) original central edges now each have both endpoints at the common point and their interiors distinct, giving precisely \(\binom{s}{2}\) independent circles. There are no remaining identifications between distinct suspensions away from the common basepoint. The resulting quotient is exactly the displayed wedge, proving the assertion for every permitted \(H\) and \(s\).

The homology formulas follow from the reduced suspension isomorphism, reduced homology of a wedge, and integral homology of circles; no torsion-freeness assumption on \(\operatorname{Ind}(H)\) is required.

For the example \(H=C_6\), the only independent triples are the two alternating triples, giving two disjoint filled triangles; the remaining independent pairs provide three edges between them. Collapsing each filled triangle to one point produces two vertices joined by three edges, a graph with the homotopy type \(S^1\vee S^1\). Substitution at \(s=3\) yields the stated \(3\)-circle and \(6\)-sphere wedge.

## Verification

The standalone `verify_clique_join.py` enumerates **every labelled triangle-free graph on one through five vertices** (\(1+2+7+41+388=439\) graphs), both central clique sizes \(s=2,3\), and coefficients in \(\mathbf F_2\) and \(\mathbf F_3\). It reconstructs forbidden triangles directly from join edges, computes the complete augmented simplicial boundary complexes, and compares all reduced Betti numbers to the formula computed independently from the graph's independence complex. It also tests cycles \(C_6\) and \(C_7\) at both central clique sizes and both primes. The checker reports **1,764 passed field-level comparisons**, covering 119,588 enumerated simplices across repeated instances. Run `python3 verify_clique_join.py` with Python 3.8 or later. The recorded reproducible output is included separately as `verification_output.txt`.

These finite homology checks are not substituted for the unrestricted homotopy proof; they do not establish homotopy equivalence themselves.

## Relationship to prior work

Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (public preprint dated 2026-02-10, arXiv:2602.09623v1), defined the same clique-free complexes and proved diamond-free chordal shellability and clique-attachment preservation statements. Those results concern a different graph operation or shellability rather than homotopy of \(K_s\vee H\). They do not state the independence-complex transfer formula, and nonchordal inputs such as \(H=C_6\) lie outside their chordal criterion.

Known complete split-graph computations occur as the special case where \(H\) has no edges and its independence complex is contractible. Those cases do not imply the asserted formula when \(\operatorname{Ind}(H)\) has nontrivial topology. Another publicly indexed result concerning clique joins suspends **Lovász neighborhood complexes**; that is a different simplicial construction and does not give the stated clique-free equivalence. A finite search cannot exclude all unpublished, unindexed, or implicit equivalent statements.

## Limitations

The graph \(H\) must be nonempty and triangle-free. If it is empty, the proof's first contractible simplex is absent and the circle multiplicity changes. If \(H\) contains triangles, its deletion-side clique-free complex is no longer the full simplex, so this splitting need not hold. The result asserts a nonequivariant homotopy equivalence, not an equivariant splitting, shellability, a new classification of independence complexes, or an independent mathematical audit. It permits torsion from the independence complex and does not decide that torsion separately.

## References

- R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first posted 2026-02-10. https://arxiv.org/abs/2602.09623
- Public comparable result: *Clique-joins suspend Lovász neighborhood complexes*, scientific record at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clique-joins-suspend-lov-sz-neighborhood-complexes--46728c3e0714 (different simplicial functor; title and indexed summary examined, not full text).
