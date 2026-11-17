# A missing bipartite edge creates a circle in the Alexander dual of a three-cut complex

## Finding

Let \(a,b\geq3\) be integers and let \(G\) arise by deleting one cross-edge from the complete bipartite graph \(K_{a,b}\). Write \(\Delta_3(G)\) for its **ordinary** three-cut complex: the simplicial complex whose facets are the complements of three-element vertex sets inducing disconnected graphs. Write \(K=\Delta_3(G)^\vee\) for the combinatorial Alexander dual on all \(a+b\) vertices. Define
\[
R(a,b)=\binom{a-1}{2}\binom{b-1}{2}-(a-2)(b-2).
\]
Then the following integral homotopy equivalence holds for every permitted pair:
\[
\boxed{|K|\simeq S^1\vee\bigvee^{R(a,b)}S^3.}
\]
The convention for a wedge of zero spheres is a point. In particular, at \(a=b=3\), the dual is a circle. For all other permitted pairs, it contains both a circle and at least one three-sphere in this homotopy decomposition.

Consequently, the **integral reduced homology** of the original cut complex is
\[
\boxed{
\widetilde H_i(\Delta_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{R(a,b)},&i=a+b-6,\\
\mathbb Z,&i=a+b-4,\\
0,&\text{otherwise.}
\end{cases}}
\]
These two degrees are distinct. For every \((a,b)\ne(3,3)\) with \(a,b\ge3\), the pure complex \(\Delta_3(G)\), of dimension \(a+b-4\), is therefore not shellable. No homotopy wedge decomposition of \(\Delta_3(G)\) itself is asserted.

## Assumptions and scope

All graphs are finite, simple, and undirected. The two bipartition classes have \(a\) and \(b\) vertices, and the single missing edge has endpoints \(u\) and \(v\) in opposite classes. The combinatorial Alexander dual of a complex \(L\) on a fixed ground set \(V\) is \(L^\vee=\{\sigma\subseteq V:V\setminus\sigma\notin L\}\). This is not the *total* three-cut complex, whose facets come only from independent triples.

For every \(s\ge2\), denote by \(E_s\) the complete graph as a one-dimensional simplicial complex on \(s\) vertices, equivalently the one-skeleton of an \((s-1)\)-simplex. It has integral first homology of rank \(c_s=\binom{s-1}{2}\); at \(s=2\), this group vanishes because \(E_2\) is a single edge.

## Proof

**1. Disconnected triples.** In \(K_{a,b}\), an induced three-vertex graph is disconnected precisely when all three vertices belong to one shore. Upon removing \(uv\), the only additional disconnected triples are \(\{u,v,w\}\) for \(w\in V\setminus\{u,v\}\). Indeed, every such triple has exactly one cross-edge and therefore an isolated vertex; every other triple with vertices on both shores still has at least two cross-edges. There are exactly \(\binom a3+\binom b3+a+b-2\) disconnected triples in the deleted-edge graph.

**2. The Alexander dual.** By definition of a cut complex, a subset belongs to its Alexander dual exactly when it contains no disconnected triple. Thus the dual of the intact complete bipartite graph is the simplicial join \(K_0=E_a*E_b\): a face may contain at most two vertices from each shore. Removing \(uv\) deletes from \(K_0\) every face of size at least three that contains both \(u\) and \(v\), but retains the one-simplex \(uv\). Writing
\[
D=\{\sigma\in K_0:\{u,v\}\not\subseteq\sigma\},
\]
we have the *exact equality of complexes* \(K=D\cup\{uv\}\), with no two-simplex incident on the newly adjoined edge.

**3. A union of joins.** Define \(A=E_{a-1}*E_b\) and \(B=E_a*E_{b-1}\), where the reduced factors omit \(u\) and \(v\), respectively. Then \(D=A\cup B\), while \(I=A\cap B=E_{a-1}*E_{b-1}\). Each factor \(E_s\) is connected for \(s\ge2\); the simplicial join of two connected complexes is two-connected. Therefore \(A\), \(B\), and \(I\) are all two-connected complexes of dimension at most three. Their third integral homology groups, by the reduced homology of joins, are respectively
\[
H_3(A)=\mathbb Z^{c_{a-1}c_b},\qquad
H_3(B)=\mathbb Z^{c_ac_{b-1}},\qquad
H_3(I)=\mathbb Z^{c_{a-1}c_{b-1}}.
\]
All other reduced integral homology of these three spaces vanishes.

**4. The nonstandard Mayer--Vietoris map is injective.** Inclusion \(I\hookrightarrow A\) induces on third homology the tensor product of the identity on \(H_1(E_{a-1};\mathbb Z)\) with the inclusion \(H_1(E_{b-1};\mathbb Z)\to H_1(E_b;\mathbb Z)\). The latter is injective: for a graph regarded as a one-dimensional CW complex, \(H_1\) consists of integral one-cycles with zero boundaries, and inclusion into a larger graph cannot kill a nonzero one-cycle because there are no two-cells. These free abelian cycle lattices are pure and admit compatible bases, so tensoring preserves injectivity. Consequently the first coordinate of the Mayer--Vietoris map
\[
H_3(I)\longrightarrow H_3(A)\oplus H_3(B)
\]
is injective, including the degenerate rank-zero cases. This is the critical step: exactness alone without this injectivity would not establish the claimed integral ranks.

**5. Homotopy type of \(D\).** The Mayer--Vietoris sequence, the preceding injection, and the vanishing of lower homology show that \(D\) has no reduced homology except in degree three, where it is free of rank
\[
\begin{aligned}
 c_{a-1}c_b+c_ac_{b-1}-c_{a-1}c_{b-1}
 &=c_ac_b-(c_a-c_{a-1})(c_b-c_{b-1})\\
 &=\binom{a-1}{2}\binom{b-1}{2}-(a-2)(b-2)=R(a,b).
\end{aligned}
\]
Van Kampen gives \(\pi_1(D)=0\), since both pieces and their intersection are simply connected. Also \(H_2(D)=0\), so the Hurewicz theorem implies \(\pi_2(D)=0\). The three-dimensional CW complex \(D\) is therefore two-connected with free top homology. Representatives of an integral basis of \(H_3(D)\) determine a map \(\bigvee^{R(a,b)}S^3\to D\) that is an isomorphism on all integral homology groups; the Hurewicz and homological Whitehead theorems make it a homotopy equivalence. When \(R(a,b)=0\), the same argument gives contractibility.

**6. The surviving edge creates the circle.** Both endpoints \(u,v\) belong to the connected complex \(D\). The realization of \(K=D\cup uv\) is obtained by attaching one closed interval along its two distinct endpoints, with no higher cells introduced. For any path-connected CW complex, this attachment is homotopy equivalent to wedging on \(S^1\). Hence \(|K|\simeq|D|\vee S^1\), proving the dual homotopy theorem.

**7. Integral cut homology.** With \(N=a+b\), combinatorial Alexander duality gives \(\widetilde H_i(\Delta_3(G);\mathbb Z)\cong\widetilde H^{N-i-3}(K;\mathbb Z)\). The free cohomology of \(S^1\vee\bigvee^{R(a,b)}S^3\) occurs in degrees one and three, with ranks one and \(R(a,b)\). This gives the displayed integral homology formula. Each disconnected triple has a complementary facet of size \(N-3\), hence the cut complex is pure of dimension \(N-4\). When \(R(a,b)>0\), its nonzero homology in lower degree \(N-6\) contradicts the homology concentration required of a nonempty pure shellable complex. Finally, \(R(a,b)\ge0\), and direct factorization using \(c_s=(s-1)(s-2)/2\) shows equality only at \(a=b=3\) within the stated range.

## Verification

The standalone standard-library program `verify.py` enumerates all disconnected triples directly from the deficient bipartite graph; constructs both the cut complex and its Alexander dual independently; checks exact equality with the proposed edge-deletion decomposition; and computes simplicial homology using signed boundary matrices reduced modulo two distinct primes. It checks \((a,b)=(3,3),(3,4),(4,4),(4,5),(5,5),(5,6)\). The program prints `COMPLETE_BIPARTITE_EDGE_DEFECT_THREE_CUT_PASS` on success; its recorded output is `verification_output.txt`.

For example, at \((a,b)=(4,4)\), the dual has 106 faces (including the empty face), with first Betti number one and third Betti number five; the original cut complex has reduced Betti ranks five in degree two and one in degree four. The finite checks are corroboration, not a proof for infinitely many shore sizes. The proof above is symbolic and integral.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue, Theorem 7.4 of *Topology of Cut Complexes of Graphs*, determine the homotopy type of the ordinary three-cut complex of the **intact** complete bipartite graph: a wedge of \(\binom{a-1}{2}\binom{b-1}{2}\) spheres in degree \(a+b-6\). Their hypotheses do not cover one deleted cross-edge. The present theorem determines the precise loss of \((a-2)(b-2)\) of those generators and the appearance of an additional class in top degree \(a+b-4\), by computing the full Alexander-dual homotopy type.

Shen, Song, Yu, Zhou and Zhuang, *Realizations and Uniqueness of Cut Complexes of Graphs* (first publicly posted December 15, 2025), Proposition 3.3, determine **whether** an edge deletion changes the ordinary three-cut complex (the criterion uses twin endpoints). Their proposition contains no homology or homotopy classification for the modified complex; the present result quantifies a concrete, natural edge-deletion change.

Carnero Bravo's *Total cut complexes and their duals* treats total cut complexes, including complete multipartite graphs, not the present ordinary cut complex of the non-complete-multipartite deleted-edge graph. Published results for crown graphs with a whole perfect matching removed likewise concern a different deletion regime and do not imply the one-edge formula. Searches for equivalent formulations under disconnected-triple avoidance, Alexander duality, and edge-deleted bicliques found no covering statement; search absence is not evidence of global uniqueness.

## Limitations

The result assumes both shores have at least three vertices and **exactly one** cross-edge is removed. It proves an integral homotopy decomposition only for the *Alexander dual*, and an integral homology classification (not a homotopy classification) for the original cut complex. The finite experiments do not establish universal claims on their own. No statement is made about multiple-edge deletions, higher cut thresholds, or integral homology representations under graph automorphisms. Unindexed prior literature might contain an equivalent theorem.

## References

1. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes of Graphs*, SIAM Journal on Discrete Mathematics 38 (2024). arXiv:2304.13675, especially Theorem 7.4. https://arxiv.org/abs/2304.13675
2. Yufeng Shen, Zhiyu Song, Fenglin Yu, Leopold Wuhan Zhou, and Jingqi Zhuang, *Realizations and Uniqueness of Cut Complexes of Graphs*, arXiv:2512.12933, initially posted 2025-12-15, especially Section 3, Proposition 3.3. https://arxiv.org/abs/2512.12933
3. Andrés Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, initially posted 2026-02-24, especially its complete-multipartite treatment. https://arxiv.org/abs/2602.21427
4. Combinatorial Alexander duality, reduced join homology, Mayer--Vietoris, van Kampen, Hurewicz and Whitehead theorems, as standard statements in algebraic topology.
