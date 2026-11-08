# Size-independent invariant homology of four-path-free multipartite complexes

## Finding
Let \(m\ge3\), let \(A_1,\ldots,A_m\) be nonempty, pairwise disjoint finite sets, and put \(G=K_{|A_1|,\ldots,|A_m|}\). Let \(X=\operatorname{PF}_4(G)\) be the simplicial complex of vertex subsets whose induced graph contains no simple path through four distinct vertices (the path is not required to be induced). Let \(\Gamma=\prod_{i=1}^m\mathfrak S(A_i)\) act by permuting vertices within each part. Then

\[
\dim_{\mathbb Q} H_2(X;\mathbb Q)^\Gamma=\binom{m-1}{3},
\]

independently of all positive part sizes. More precisely, write \(T\) for the subcomplex of faces containing at most one vertex from each part and at most three vertices in total. There is a canonical rational identification

\[
H_2(X;\mathbb Q)^\Gamma\cong H_2(T;\mathbb Q)^\Gamma
\cong H_2(\operatorname{sk}_2\Delta^{m-1};\mathbb Q).
\]

There is also a canonical integral sequence, equivariant even under graph automorphisms interchanging equal-sized parts,

\[
0\longrightarrow H_2(T;\mathbb Z)\longrightarrow H_2(X;\mathbb Z)
\longrightarrow\bigoplus_{i=1}^m\widetilde H_1(K_{|A_i|,N-|A_i|};\mathbb Z)
\longrightarrow0,
\]

where \(N=\sum_i|A_i|\), and the complete-bipartite graph appearing in the \(i\)-th term has vertex sides \(A_i\) and \(V(G)\setminus A_i\). In particular \(H_2(X;\mathbb Z)\) is free abelian and all other reduced integral homology groups vanish.

For \(\gamma=(\gamma_i)\in\Gamma\), let \(f_i\) be the number of vertices of \(A_i\) fixed by \(\gamma_i\), put \(F=\sum_i f_i\), and write \(e_j(f_1,\ldots,f_m)\) for the \(j\)-th elementary symmetric polynomial. The full rational second-homology character is

\[
\operatorname{tr}(\gamma\mid H_2(X;\mathbb Q))
=e_3(f_1,\ldots,f_m)+e_2(f_1,\ldots,f_m)-(m-1)(F-1).
\]

This is a statement about the natural symmetry representation, not simply the nonequivariant Betti number.

## Assumptions and scope
All part sizes are positive and there are at least three parts. The group \(\Gamma\) preserves each named part; the exact integral sequence is functorial also for automorphisms permuting parts, but the displayed fixed-point character formula only concerns \(\Gamma\). The complex is defined by forbidden non-induced paths, not by induced paths alone. Every homology group is simplicial homology; orientation signs are the usual signed simplicial boundaries. An empty binomial coefficient is interpreted as zero.

## Proof
**1. Cover and intersections.** Let \(D(S)\) be the discrete simplicial complex on a nonempty set \(S\), and put
\[
F_i=\Delta(A_i)*D(V(G)\setminus A_i).
\]
A face of \(X\) with at most three vertices belongs to either \(T\) or one of the \(F_i\). A face of at least four vertices avoids a four-vertex path exactly when all its vertices lie in a single part, except possibly one vertex outside that part. Indeed, among four chosen vertices with at least two in two separate parts there is an alternating path; if at least three parts are represented, any four include a simple three-edge path. Thus
\[X=T\cup\bigcup_{i=1}^mF_i.\]
Each \(F_i\) is contractible because \(\Delta(A_i)\) is a simplex. Its intersection with \(T\) is the one-dimensional complete-bipartite complex
\[L_i=F_i\cap T=D(A_i)*D(V(G)\setminus A_i)\cong K_{|A_i|,N-|A_i|}.\]
For distinct indices \(i,j\), every face of \(F_i\cap F_j\) belongs to \(T\). All constructions respect graph automorphisms.

**2. Integral exact sequence.** The relative chain complex \(C_*(X,T;\mathbb Z)\) is therefore the direct sum of the \(C_*(F_i,L_i;\mathbb Z)\), including its group action. Contractibility of \(F_i\) and connectedness of each \(L_i\) give
\[
H_q(X,T;\mathbb Z)\cong\begin{cases}\bigoplus_i\widetilde H_1(L_i;\mathbb Z),&q=2,\\0,&q\ne2.\end{cases}
\]
The complex \(T\) is the two-skeleton of the join \(D(A_1)*\cdots*D(A_m)\). For \(m\ge3\), this join is simply connected; passing to its two-skeleton preserves the fundamental group. Hence \(H_1(T;\mathbb Z)=0\), while \(H_q(T)=0\) for \(q>2\). The long exact sequence of \((X,T)\) now yields precisely the asserted integral short exact sequence and homology vanishing. Its right-hand group is free abelian (graph cycle lattices), and its left-hand group is a subgroup of the free simplicial two-chain group. Thus the middle group is free; the sequence splits as abelian groups, with no claim of an equivariant integral splitting.

**3. Invariants.** As a \(\Gamma\)-module, the graph-cycle space of \(L_i\), over \(\mathbb Q\), is
\[\widetilde H_1(L_i;\mathbb Q)\cong\widetilde H_0(D(A_i);\mathbb Q)\otimes\widetilde H_0(D(V(G)\setminus A_i);\mathbb Q).\]
If \(|A_i|=1\), the first factor is zero. Otherwise \(\mathfrak S(A_i)\) has no fixed vectors in its augmentation module, so the tensor product has no \(\Gamma\)-invariants. Since averaging makes the invariants functor exact over \(\mathbb Q\), the inclusion \(H_2(T;\mathbb Q)^\Gamma\to H_2(X;\mathbb Q)^\Gamma\) is an isomorphism.

For each part, form the normalized invariant zero-chain \(u_i=|A_i|^{-1}\sum_{v\in A_i}[v]\). Products of these chains in increasing part order identify the reduced invariant simplicial chain complex of \(T\) over \(\mathbb Q\), including its signed boundary, with the reduced simplicial chain complex of \(\operatorname{sk}_2\Delta^{m-1}\). Averaging commutes with homology. The two-skeleton of an \((m-1)\)-simplex has reduced homology concentrated in degree two, of dimension \(\binom{m-1}{3}\). This proves the size-independent invariant dimension.

**4. Full rational character.** The signed cellular trace on \(C_j(T;\mathbb Q)\) is \(e_{j+1}(f_1,\ldots,f_m)\) for \(j=0,1,2\), since a simplex with distinct parts is fixed setwise by a part-preserving automorphism only when each vertex is fixed. As \(T\) is connected and has homology only in degrees zero and two, Hopf trace gives
\[\operatorname{tr}(\gamma\mid H_2(T;\mathbb Q))=e_3(f)-e_2(f)+F-1.\]
For the complete bipartite graph \(L_i\), the trace on \(\widetilde H_1(L_i;\mathbb Q)\) is \(f_i(F-f_i)-F+1\), by the edge-vertex chain sequence. Taking characters in the rationalized short exact sequence, and observing \(\sum_i f_i(F-f_i)=2e_2(f)\), proves the stated expression.

## Verification
The accompanying `verify_equiv_pf4.py` constructs face sets by directly testing all ordered four-vertex paths in the graph, computes signed permutation traces on every simplicial chain group, and compares the reduced Euler trace with the formula. It also averages the traces over the full part-preserving automorphism group and checks the stated invariant dimension. In 76 part-size cases (three or four parts, each size at most three, and at most eight vertices) it checks 1,266 individual group elements; all tests pass. These finite checks are corroboration of, not a substitute for, the all-parameter proof.

## Relationship to prior work
The 2026 preprint of Deshpande, Goyal and Sawant establishes a structural decomposition and shellability thresholds for path-free complexes of complete multipartite graphs, and its abstract reports a full homotopy classification in the bipartite case. The non-equivariant wedge-of-spheres homotopy type for four-path-free complete multipartite complexes does not by itself determine the group action on integral homology. The present statement concerns the natural automorphism action, a canonical integral extension, the full part-preserving rational character, and the dimension of invariant cycles. These are not consequences of the Betti number alone.

## Limitations
No equivariant integral splitting of the displayed extension is asserted, and no claim is made about complete group representations for automorphisms permuting equal-sized parts beyond the functorial exact sequence. The primary 2026 manuscript was available through bibliographic and abstract records, not full-text inspection, leaving the possibility of equivalent results in its inaccessible sections. The exact character can determine the rational representation without specifying a preferred isomorphism with an irreducible direct sum.

## References
1. Priyavrat Deshpande, Shuchita Goyal, Rutuja Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358 (first public version July 6, 2026), https://arxiv.org/abs/2607.05358.
2. Allen Hatcher, *Algebraic Topology* (2002), sections on relative homology, Mayer–Vietoris, and simplicial homology (standard topological tools used in the proof).
