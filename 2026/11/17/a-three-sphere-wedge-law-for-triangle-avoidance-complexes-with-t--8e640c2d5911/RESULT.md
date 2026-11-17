# A three-sphere-wedge law for triangle-avoidance complexes with two cross-part matching defects

## Finding
Let \(A,B,C\) be nonempty disjoint vertex sets with \(|A|=a\), \(|B|=b\), \(|C|=c\). Fix integers \(p,q\ge 1\) satisfying \(p\le a\), \(p+q\le b\), and \(q\le c\). Start with the complete tripartite graph on \(A\sqcup B\sqcup C\). Delete edges \(a_i b_i\) for \(1\le i\le p\) and \(b'_j c_j\) for \(1\le j\le q\), where all displayed vertices within each part are distinct, and \(\{b_i\}\cap\{b'_j\}=\varnothing\). Call the resulting graph \(G\).

Write \(\mathsf{CF}_3(G)\) for the simplicial complex of subsets of vertices spanning no triangle. Then **for every such choice**, including the endpoint sizes and all unmatched vertices,
\[
\boxed{|\mathsf{CF}_3(G)|\simeq\bigvee^{(p-1)(q-1)}S^3.}
\]
A zero-fold wedge denotes a contractible space. In particular the first noncontractible example has \(p=q=2\) and is homotopy equivalent to \(S^3\), while \(p=1\) or \(q=1\) gives contractibility. All reduced integral homology is zero outside degree three, where it is free of rank \((p-1)(q-1)\).

## Assumptions and scope
All graphs are finite, simple, undirected. The three vertex parts are independent before and after deletions; every edge joining different parts is present except the two explicitly specified matchings. The two matchings meet the middle part \(B\) in disjoint sets. This disjointness is essential to the face decomposition below. A simplex on a vertex set \(W\) is written \(\Delta(W)\). All homotopy types concern geometric realizations and integral topology.

The theorem is an infinite-family homotopy classification, not an assertion about ordinary matching complexes, graph three-cut complexes, or graph joins. Its sphere count depends on the two matching sizes but not on the three shore sizes once the feasibility inequalities hold.

## Proof
**1. Classify all faces.** Put
\[
X_0=\Delta(A\cup B)\cup\Delta(A\cup C)\cup\Delta(B\cup C).
\]
Every set contained in two of the three parts is triangle-free. The three simplices have contractible nonempty pairwise intersections \(\Delta(A)\), \(\Delta(B)\), \(\Delta(C)\), and empty triple intersection. The simplicial nerve lemma therefore gives \(|X_0|\simeq S^1\).

Define the defect simplices
\[
P_i=\Delta(\{a_i,b_i\}\cup C),\qquad Q_j=\Delta(A\cup\{b'_j,c_j\}),\qquad T_{ij}=\Delta(\{a_i,b_i,b'_j,c_j\}).
\]
We claim that the full triangle-avoidance complex \(X\) satisfies
\[
X=X_0\cup\bigcup_{i=1}^pP_i\cup\bigcup_{j=1}^qQ_j\cup\bigcup_{i=1}^p\bigcup_{j=1}^qT_{ij}.\tag{1}
\]
Indeed, a face meeting all three parts has a nonempty selected set in \(B\). Any selected middle vertex not among the \(b_i,b'_j\) creates a triangle with any selected vertex of \(A\) and of \(C\). If a selected middle vertex is \(b_i\), all selected \(A\)-vertices must equal \(a_i\); two distinct middle vertices of the first type cannot both occur. If a selected middle vertex is \(b'_j\), all selected \(C\)-vertices must equal \(c_j\); two distinct middle vertices of the second type cannot both occur. Thus the selected middle vertices consist of just one \(b_i\), just one \(b'_j\), or one of each. The respective possibilities are faces of \(P_i\), \(Q_j\), and \(T_{ij}\). Conversely, each listed simplex is triangle-free, proving (1).

**2. The two-cell stage.** Set \(Y=X_0\cup_i P_i\cup_j Q_j\). The intersections \(P_i\cap X_0=L_i\) are unions of the three simplices
\[
\Delta(\{a_i,b_i\}),\quad\Delta(\{a_i\}\cup C),\quad\Delta(\{b_i\}\cup C).
\]
These three simplices form a circular nerve, so \(|L_i|\simeq S^1\). Similarly, \(Q_j\cap X_0=L'_j\) is the union of
\[
\Delta(A\cup\{b'_j\}),\quad\Delta(A\cup\{c_j\}),\quad\Delta(\{b'_j,c_j\}),
\]
and \(|L'_j|\simeq S^1\). Under the inclusions into \(X_0\), both circles map with degree \(+1\) after consistent choices of orientation: the three vertices of their nerves correspond, in order, to the \(AB\), \(AC\), and \(BC\) two-part simplices of \(X_0\). This is also verified by the oriented boundary of any triangle with one vertex in each part.

For different defect simplices, \(P_i\cap P_{i'}=\Delta(C)\), \(Q_j\cap Q_{j'}=\Delta(A)\), and \(P_i\cap Q_j=\Delta(\{a_i,c_j\})\), all already inside \(X_0\). Therefore
\[
Y/X_0\cong\bigvee_i(P_i/L_i)\vee\bigvee_j(Q_j/L'_j).
\]
Since every \(P_i,Q_j\) is contractible and every attaching circle is homotopy equivalent to \(S^1\), the only nonzero reduced relative group is
\[
H_2(Y,X_0;\mathbb Z)\cong\mathbb Z^{p+q}.
\]
Let \(e_i\) and \(f_j\) be the classes represented by respectively oriented triangles \([a_i,b_i,c_j]\) and \([a_i,b'_j,c_j]\); their classes do not depend on the auxiliary index. The connecting map to \(H_1(X_0;\mathbb Z)\cong\mathbb Z\) is
\[
\partial_2(e_i)=1,\qquad\partial_2(f_j)=1.
\]
It is surjective. Thus \(H_2(Y;\mathbb Z)\) injects into \(\mathbb Z^{p+q}\) with image \(\ker\partial_2\cong\mathbb Z^{p+q-1}\); all higher reduced homology groups of \(Y\) vanish. Van Kampen applied to any one contractible \(P_i\) (or \(Q_j\)) kills the generator of \(\pi_1(X_0)\), so \(Y\) is simply connected.

**3. The three-cell stage.** Each tetrahedron \(T_{ij}\) meets \(Y\) in its *entire boundary*: the four triangular facets lie, respectively, in \(X_0\), \(Q_j\), \(P_i\), \(X_0\). Any intersection between distinct tetrahedra is also contained in \(Y\). Therefore
\[
X/Y\cong\bigvee_{i,j}(T_{ij}/\partial T_{ij})\cong\bigvee^{pq}S^3,
\quad H_3(X,Y;\mathbb Z)\cong\mathbb Z^{pq},
\]
with all other reduced relative homology zero. Orient each tetrahedron as \([a_i,b_i,b'_j,c_j]\). Its signed boundary is
\[
[b_i,b'_j,c_j]-[a_i,b'_j,c_j]+[a_i,b_i,c_j]-[a_i,b_i,b'_j].
\]
The first and last triangular faces are in \(X_0\). Hence the image of its connecting class in \(H_2(Y,X_0)\) is exactly \(e_i-f_j\). The vectors \(e_i-f_j\) are the integral edge-incidence columns of the complete bipartite graph with vertex classes of sizes \(p\) and \(q\). They span **the entire** sum-zero lattice \(\ker\partial_2\): every two \(e_i\)'s and every two \(f_j\)'s differ by combinations of these columns, and a spanning-tree submatrix has determinant \(\pm1\). This proves surjectivity onto \(H_2(Y)\) integrally, without any torsion or index ambiguity.

The long exact sequence for \((X,Y)\) gives
\[
\widetilde H_i(X;\mathbb Z)=0\quad(i\ne3),\qquad
H_3(X;\mathbb Z)=\ker\big(\mathbb Z^{pq}\to\mathbb Z^{p+q-1}\big)
\cong\mathbb Z^{pq-p-q+1}.
\]
Since attaching cells of dimension at least three cannot change the fundamental group, \(X\) is simply connected. The vanishing of \(H_2(X)\) makes it 2-connected by the Hurewicz theorem. Representatives of a basis of \(H_3(X)\) then define a map from the displayed wedge of three-spheres to \(|X|\) inducing an integral homology isomorphism. The homological Whitehead theorem for simply connected CW complexes upgrades that map to a homotopy equivalence. This proves the classification, including the contractible cases.

## Verification
The standalone `verify.py` reconstructs graph edges and **all** forbidden triangles independently of the proof's defect-simplex cover. It enumerates all subsets of the graph vertex set and directly tests whether they contain a forbidden triangle. It then independently enumerates the faces of the explicit cover (1) and asserts equality as entire face sets. For nine parameter instances, it calculates every reduced mod-two Betti number from augmented simplicial boundary matrices and compares with the predicted third Betti number. It also constructs a spanning-tree minor of each integral difference matrix and verifies its determinant is \(\pm1\) by exact fraction-free elimination.

The largest checked instance has 13 vertices and 1,633 nonempty faces. Across all nine cases the program checks 3,853 nonempty faces and reports `TWO_MATCHING_TRIANGLE_AVOIDANCE_PASS 9 cases 3853 faces`. Run `python3 verify.py` with the standard Python library; the matching output is recorded in `verification_output.txt`. Finite checks corroborate the decomposition; the proof above supplies the universal integral statement.

## Relationship to prior work
Ghosh and Selvaraja (arXiv:2602.09623v1, 2026-02-10) define clique-free complexes and prove shellability results for diamond-free chordal graphs, disjoint-union join formulas, and clique attachments. Their full public text does not classify triangle-free vertex sets of the nonchordal cross-deficient tripartite graphs considered here. The publicly recorded triangle-free-graph-join homotopy-splitting theorem covers graph joins of triangle-free factors. That theorem cannot be applied to the present graph: its complement is connected, since each part is a clique in the complement and the two nonempty deleted matchings join the three parts. Another related public theorem allows perfect matchings **inside** two multipartite parts, retaining all cross-part edges. Its construction and homotopy decomposition do not imply the present two cross-part deletion result.

The proof uses standard nerve, long exact sequence, van Kampen, Hurewicz and Whitehead theorems. These tools are background; the new content is the exact face decomposition, the primitive complete-bipartite attaching matrix, and the all-size three-sphere-wedge phase. Search limitations and potential unindexed equivalent work remain residual originality risks.

## Limitations
The matching endpoints in the middle part must be disjoint; overlapping missing edges can produce different face types and are not classified. The statement is only for triangles, not higher clique-avoidance thresholds. The homotopy equivalence is not claimed equivariant under all graph automorphisms, and no arbitrary edge-deletion result is asserted. The checker runs finite examples and is not a machine certification of the infinite theorem. Independent mathematical review is not performed.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first publicly submitted 2026-02-10, https://arxiv.org/html/2602.09623v1.
2. *Triangle-free graph joins: a complete integral homotopy splitting for three-clique avoidance*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-triangle-free-graph-joins-a-complete-integral-homotopy-splitting--f6e42b155b01.
3. *Mixed-dimensional triangle-avoidance homotopy for two matched multipartite parts*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-mixed-dimensional-triangle-avoidance-homotopy-for-two-matched-mu--e70c09dbfa5c.
4. A. Hatcher, *Algebraic Topology* (2002), sections on the nerve lemma, CW pairs, van Kampen, Hurewicz and Whitehead, https://pi.math.cornell.edu/~hatcher/AT/AT.pdf.
