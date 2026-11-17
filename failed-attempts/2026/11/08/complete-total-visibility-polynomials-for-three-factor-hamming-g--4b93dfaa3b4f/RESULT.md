# Complete total-visibility polynomials for three-factor Hamming graphs with a binary factor

## Finding
For integers \(b,n\ge 3\), put \(G_{b,n}=K_2\square K_b\square K_n\), where \(\square\) is the Cartesian graph product. A set \(X\subseteq V(G_{b,n})\) is *total mutual-visible* if for every pair of vertices \(u,v\) there exists a shortest \(u,v\)-path with no internal vertex in \(X\). Let the *total-visibility polynomial* count all such labelled subsets:
\[
\mathcal V_t(G_{b,n};z)=\sum_{X\text{ total mutual-visible}}z^{|X|}.
\]
Define
\[
\begin{aligned}
U_b(z)&=(1+2z)^b-2(1+z)^b+1,\\
Q_n(z)&=(1+z)^{n-1}-1-(n-1)z,\\
R_n(z)&=(1+2z)^n-2(1+z)^n+1
          -2nz((1+z)^{n-1}-1)+n(n-1)z^2.
\end{aligned}
\]
**Theorem.** For every \(b,n\ge3\),
\[
\boxed{\begin{aligned}
\mathcal V_t(G_{b,n};z)={}&1+n\left[2((1+z)^b-1)+bz^2\right]\\
&+2b\left[(1+z)^n-1-nz\right]
+n(n-1)U_b(z)\\
&+2bn\left[(1+z)^{b-1}-1\right]Q_n(z)
+b(b-1)R_n(z).
\end{aligned}}
\]
All coefficients count *individual vertex subsets*, without identification under graph automorphisms. Moreover, the number of maximum-cardinality total mutual-visibility sets is exactly \(2bn\). Their cardinality is \(b+n-2\), which was previously established; the full coefficient distribution and maximum-set multiplicity for \(b,n\ge3\) are the contributions here. The polynomial identity also remains algebraically correct when \(b=2\) or \(n=2\); those boundary specializations are consistency checks, not part of the originality claim.

## Assumptions and scope
All graphs are finite, simple, undirected, and labelled. The graph \(G_{b,n}\) has vertices \((x,y,c)\) with \(x\in\{0,1\}\), \(y\in[b]\), and \(c\in[n]\). Vertices are adjacent exactly when their coordinates differ in precisely one position; the shortest-path distance is the number of unequal coordinates. The new assertion assumes \(b,n\ge3\); binary boundary cases are discussed solely for verification and overlap. Empty and singleton subsets are included in the polynomial. No assertion concerns other Hamming dimensions or graphs without a binary factor.

## Proof
**Distance-two criterion.** For every Hamming graph \(H\), a vertex set \(X\) is total mutual-visible if and only if no two points of \(X\) are at distance exactly two (Bujtás--Klavžar--Tian, Theorem 6). For completeness, suppose \(p,q\in X\) differ in exactly two coordinates. The other two corners of their Cartesian square have exactly two shortest paths between them, with internal points \(p\) and \(q\); neither path avoids \(X\). Conversely, if no pair of selected points is at distance two, prove the visibility condition by induction on the distance \(t\) of arbitrary endpoints \(u,v\). It is immediate for \(t\le1\). For \(t\ge2\), the \(t\) neighbors of \(v\) within the interval from \(u\) to \(v\) are pairwise at distance two. Hence at most one lies in \(X\). Choose an unselected neighbor \(v'\); the induction hypothesis supplies a shortest \(u,v'\)-path with no selected internal points. Appending \(v'v\) gives the desired path.

**Structural classification.** For each \(c\in[n]\), let \(L_c\) be the layer with third coordinate \(c\), and call it active when \(X\cap L_c\ne\varnothing\). Within one layer, two selected vertices may not differ in both the binary and \([b]\)-coordinates. Thus a nonempty layer section is either an arbitrary nonempty subset of one horizontal row \(\{x\}\times[b]\times\{c\}\), or one vertical pair \(\{(0,y,c),(1,y,c)\}\). The row cases do not overlap, and the vertical pairs are separate.

If at least two layers are active, no layer can contain a vertical pair: a point in another layer would have distance two from at least one endpoint of the pair. Therefore each active layer consists of a nonempty set \(\{x\}\times Y_c\times\{c\}\) for a single binary coordinate \(x\) and \(\varnothing\ne Y_c\subseteq[b]\). For two distinct active layers with the **same** binary coordinate, their \([b]\)-sets must both be the same singleton: otherwise a cross-layer pair differs in exactly the second and third coordinates. For active layers with **opposite** binary coordinates, their \([b]\)-sets must be disjoint: otherwise a cross-layer pair differs in exactly the first and third coordinates. These conditions are also sufficient, since all other cross-layer pairs differ in one or three coordinates.

It follows that with at least two active layers, either (i) every active layer has the same binary coordinate and the same singleton \([b]\)-coordinate, or (ii) both binary coordinates occur, each binary group containing either one layer with an arbitrary nonempty \([b]\)-set or at least two layers with the same singleton, and the \([b]\)-sets used by the two groups are disjoint. This is a bijective classification, not merely a necessary condition.

**Enumeration.** The empty set contributes \(1\). Exactly one active layer contributes
\[
n\left[2((1+z)^b-1)+bz^2\right],
\]
because there are two horizontal rows and \(b\) vertical pairs per layer. When at least two layers are active but only one binary coordinate occurs, choose that coordinate and one of \(b\) possible singleton \([b]\)-coordinates; the contribution is
\[
2b\left[(1+z)^n-1-nz\right].
\]

Suppose both binary coordinates occur. Let \(A,B\) be the respective disjoint nonempty sets of active layers. If \(|A|=|B|=1\), the two distinct layer positions are chosen in \(n(n-1)\) ways. The weighted number of ordered pairs of disjoint nonempty \([b]\)-subsets is \(U_b(z)\), giving \(n(n-1)U_b(z)\).

If exactly one of \(|A|,|B|\) equals one, the repeated group uses a fixed singleton \([b]\)-coordinate and at least two of the other \(n-1\) layers; the single group uses a nonempty subset of the remaining \(b-1\) coordinates. Interchanging the two binary groups yields
\[
2bn\left[(1+z)^{b-1}-1\right]
\left[(1+z)^{n-1}-1-(n-1)z\right].
\]
If \(|A|,|B|\ge2\), the two groups use two distinct singleton \([b]\)-coordinates, with \(b(b-1)\) ordered choices. The weighted number of ordered disjoint subsets \(A,B\subseteq[n]\) of sizes at least two is \(R_n(z)\): begin with \((1+2z)^n\), exclude empty groups by inclusion-exclusion, then exclude singleton groups by another inclusion-exclusion. This gives \(b(b-1)R_n(z)\). The five nonempty cases are pairwise disjoint and exhaustive; summing them proves the polynomial.

**Extremal multiplicity.** If \(b,n\ge3\), the polynomial has degree \(b+n-2\). Only the case with exactly one active layer in one binary group and at least two in the other attains this degree: its leading coefficient is \(2bn\). This recovers the previously known extremal cardinality \(b+n-2\) while refining it by a count of all optimizers. The algebraic specialization \(b=2\) gives \(2(1+2z)^n-1+4nz^2\), already covered as a binary--binary-factor boundary case; it is not presented as new.

## Verification
A standalone standard-library Python program `verify.py` constructs the three-coordinate Hamming graph directly, enumerates the independent sets of its exact-distance-two conflict graph by recursive backtracking, and compares every coefficient with an independent algebraic evaluation of the stated formula. It checks \((b,n)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4),(3,5),(5,3),(4,5),(5,4),(2,6)\), including both boundary dimensions and coordinate interchange. Separately, for the \(8\)-vertex and \(12\)-vertex cases it tests every one of \(2^8+2^{12}=4352\) vertex subsets against the literal definition, finding shortest paths that avoid selected internal vertices. The program also checks all three extremal-multiplicity regimes. Execute `python3 verify.py` with Python 3.9 or later. These finite checks corroborate, but do not replace, the all-parameter proof.

For illustration, \(\mathcal V_t(G_{3,3};z)=1+18z+81z^2+84z^3+18z^4\), while \(\mathcal V_t(G_{3,4};z)=1+24z+144z^2+248z^3+162z^4+24z^5\).

## Relationship to prior work
Bujtás, Klavžar, and Tian's *Total mutual-visibility in Hamming graphs* proves the exact-distance-two criterion (their Theorem 6) and the maximum total-visibility number of every three-factor Hamming graph (their Theorems 1 and 9). Those results **cover the feasibility criterion and the extremal cardinality**, not the all-size coefficients or the maximum-set multiplicities for \(b,n\ge3\) computed here. The present argument uses the established criterion as an input and independently derives the disjoint case decomposition and its enumeration.

Bujtás, Klavžar, and Tian later introduced the total-visibility polynomial, established its general properties, and determined examples including complete bipartite graphs. The inspected complete article does not state a polynomial for \(K_2\square K_b\square K_n\). Kuziak and Rodríguez-Velázquez's earlier total-visibility product results provide bounds and scalar examples, but not this enumeration. The formula may also be regarded as the independence polynomial of the exact-distance-two graph on this Hamming space. No directly covering expression was located under either viewpoint. The absence of a located formula is not a proof of publication priority.

## Limitations
This is a mathematical proof and deterministic finite computational corroboration, not an independent mathematical audit. The novelty comparison is limited to inspected accessible primary works, mathematical-record searches, and accessible previous claims; equivalent Hamming-code or distance-two conflict-graph enumeration may exist under different terminology. It is not claimed that the original exact-distance-two characterization, the maximum cardinality, or the already covered \(K_2\square K_2\square K_n\) boundary are new. No claims are made about arbitrary numbers of factors or the full classification of inclusion-maximal sets by cardinality.

## References
1. C. Bujtás, S. Klavžar, and J. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168, first submitted 11 July 2023; subsequently Opuscula Math. 45 (2025), 63--78. https://arxiv.org/abs/2307.05168
2. C. Bujtás, S. Klavžar, and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, first submitted 4 December 2024; subsequently Aequationes Math. 99 (2025), 1883--1901. https://arxiv.org/abs/2412.03066
3. D. Kuziak and J. A. Rodríguez-Velázquez, *Total mutual-visibility in graphs with emphasis on lexicographic and Cartesian products*, Bull. Malays. Math. Sci. Soc. 46 (2023), article 197. https://doi.org/10.1007/s40840-023-01590-3
