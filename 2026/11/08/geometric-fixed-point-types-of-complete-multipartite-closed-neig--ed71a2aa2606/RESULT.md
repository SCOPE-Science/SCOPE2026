# Geometric fixed-point types of complete multipartite closed-neighborhood complexes

## Finding
Let \(G=K_{n_1,\ldots,n_k}\) be a finite complete multipartite graph with \(k\ge2\) distinguished nonempty parts \(A_1,\ldots,A_k\), each of size \(n_i\ge2\). Let \(X=\mathcal N[G]\) be its closed-neighborhood simplicial complex: a set of vertices is a face exactly when it is contained in \(N_G[v]\) for some graph vertex \(v\). Let \(H\le\prod_{i=1}^k S(A_i)\) be **any** subgroup (not necessarily cyclic or a direct product). Write \(f_i=|A_i^H|\) for the number of vertices fixed by every element of \(H\), and \(r=|\{i:f_i>0\}|\). The geometric fixed-point set of the induced action on \(|X|\) has the following complete homotopy classification.

* If some \(f_i=1\), then \(|X|^H\) is contractible.
* If every \(f_i=0\), then \(|X|^H\simeq S^{k-2}\). In particular, for \(k=2\) this is two points, not a connected sphere.
* Otherwise, all positive \(f_i\) are at least two and \(r\ge1\); then

\[
|X|^H\simeq\bigvee^{\prod_{i:f_i\ge2}(f_i-1)} S^{k+r-2}.
\]

This classifies **geometric** fixed points, which may include orbit barycenters, not just simplices on vertices fixed individually. For \(H=\{1\}\), the known nonequivariant wedge formula is recovered, but that special case is not the new contribution. The nonidentity subgroup cases give a dimension-drop and contractibility classification not specified by the ambient Betti numbers or its integral automorphism representation.

## Assumptions and scope
Throughout, graphs are finite and simple, the geometric realization uses barycentric coordinates, and all homotopy types are nonequivariant homotopy types of the fixed spaces. The subgroup \(H\) must stabilize each specified part setwise. The result does not claim a classification for subgroups permuting different parts. For a set with no fixed vertices we use the augmented simplicial complex \(\{\varnothing\}\), whose geometric realization is empty and whose join acts as the unit. An empty wedge is interpreted as a contractible space only in the explicitly stated \(f_i=1\) case.

## Proof
**1. Fixed-point orbit triangulation.** Every point of \(|X|\) has a unique barycentric coordinate vector on \(V(G)\). It is fixed by \(H\) if and only if its coefficients are constant on every \(H\)-orbit. Consequently \(|X|^H\) is naturally homeomorphic to the realization of the orbit complex \(Y_H\): its vertices are the \(H\)-orbits \(O\subset V(G)\), and a set of such orbits is a face exactly when their union is a face of \(X\). This follows directly by assigning to each chosen orbit its normalized barycenter and taking convex hulls, with inverse given by the unique orbit coefficients. No assertion about pointwise fixed vertices alone is used.

**2. Closed neighborhoods and the cover.** Each closed neighborhood has form \(N_G[v]=(V(G)\setminus A_i)\cup\{v\}\), for \(v\in A_i\). Hence a vertex set \(S\) is a face of \(X\) if and only if \(|S\cap A_i|\le1\) for at least one \(i\). Because \(H\) preserves every part, each orbit lies within a unique part. Let \(B_i\) be the set of all \(H\)-orbits lying in \(A_i\), and \(F_i\subset B_i\) the singleton orbits, so \(|F_i|=f_i\). Denote by \(\Delta(B)\) the full simplex and by \(D(F)\) the discrete complex of singletons (including the empty face). In particular \(D(\varnothing)=\{\varnothing\}\). The face criterion gives the **exact equality**

\[
Y_H=\bigcup_{i=1}^k U_i,\qquad
U_i= D(F_i)*\Delta\!\left(\bigcup_{j\ne i}B_j\right).
\]

For every proper nonempty index set \(I\subsetneq[k]\),

\[
\bigcap_{i\in I}U_i
=\left(*_{i\in I}D(F_i)\right)*\Delta\!\left(\bigcup_{j\notin I}B_j\right).
\]

This intersection is nonempty and contractible because the final simplex factor has at least one vertex. Each \(U_i\) is contractible for the same reason. The full intersection is exactly \(T=*_{i=1}^k D(F_i)\).

**3. Homotopy type of a nearly good cover.** All inclusions of the displayed subcomplexes are cofibrations. If \(|T|\ne\varnothing\), apply the homotopy-pushout description of a union of two contractible subcomplexes, and induct on \(k\), first joining \(U_1,\ldots,U_{k-1}\). Every proper subunion is contractible by the ordinary nerve lemma: all its nonempty intersections are contractible and its nerve is a simplex. The intersection of the last member with this preceding subunion again has the same cover pattern, with final intersection \(T\). Thus

\[
|Y_H|\simeq\Sigma^{k-1}|T|.
\]

For \(|T|=\varnothing\), all proper intersections are contractible and the full intersection is empty; the nerve is the boundary of the \((k-1)\)-simplex, and the nerve lemma gives \(|Y_H|\simeq S^{k-2}\). This includes \(k=2\).

**4. Evaluate the full intersection.** The join factors having \(f_i=0\) contribute only the empty face, so when \(r>0\), \(T\) is the join of the \(r\) discrete complexes with \(f_i>0\). If any \(f_i=1\), that factor is a point, making \(|T|\) and hence \(|Y_H|\) contractible. Otherwise each positive factor is homotopy equivalent to a wedge of \(f_i-1\) copies of \(S^0\). The integral join/smash suspension relation, with no Tor terms, yields

\[
|T|\simeq\bigvee^{\prod_{i:f_i\ge2}(f_i-1)}S^{r-1}.
\]

The \(k-1\) suspensions give the asserted spheres in degree \(k+r-2\). This proves the classification for all finite parameters and all part-preserving subgroups.

## Verification
The accompanying `verify.py` uses only Python standard-library modules. It enumerates orbit partitions generated by one, two, or three explicit within-part permutations (also the identity subgroup), independently constructs every closed neighborhood directly from graph adjacency, computes all allowed unions of vertex orbits, and checks that they coincide with the predicted part-occupancy criterion. It then builds all fixed-complex faces and computes every reduced simplicial Betti number over \(\mathbb F_2\) via exact sparse elimination. There are 233 subgroup/parameter cases over ten multipartition profiles, with up to 1,983 nonempty faces; every result agrees with the appropriate wedge/contractible/Sphere formula. The recorded output is `verify_output.txt` and ends `ALL_VERIFY_OK`. The proof above, not finite enumeration, establishes the integral infinite-family statement.

## Relationship to prior work
Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, submitted 16 November 2025, defines the closed-neighborhood complex and proves the general **nonequivariant suspended** relation \(\Sigma\mathcal N[\overline G]\simeq\operatorname{Ind}(K_2\times G)\) (Theorem 1.2); the paper does not state the present geometric fixed-point classification for within-part symmetry subgroups. The related complete intrinsic graph Čech persistence result, *Complete intrinsic graph Čech persistence of multipartite graphs, including their symmetry modules* (published-finding corpus record `2026/10/11/SCOPE-complete-intrinsic-graph-ech-persistence-of-multipartite-graphs--4c8b867ce9c1`), already proves the \(H=\{1\}\) case and the **integral homology representation** under part-preserving permutations; these are not asserted to be original here. That representation gives traces and dimensions of invariant homology, not homotopy types of geometric fixed-point subsets, which can have different dimensions or be contractible. The new proof explicitly triangulates the actual fixed spaces using whole subgroup orbits and identifies their complete homotopy types. Search/access caveats and exact comparisons are recorded in `AUDIT.json`.

## Limitations
The theorem concerns vertex-centered closed graph neighborhoods, equivalently the intrinsic graph Čech nerve at scale two; other filtration scales are not classified. Subgroups interchanging equal-size parts are excluded. The homotopy equivalences of fixed spaces are not claimed to be equivariant under residual normalizer actions. The finite code checks mod-two homology only; integral and homotopy conclusions follow from the symbolic cover argument. Independently reproduced mathematical certification has not been performed.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v2 (first posted 2025-11-16), especially Definition 1.1 and Theorem 1.2.
2. *Complete intrinsic graph Čech persistence of multipartite graphs, including their symmetry modules*, published-finding corpus, 2026-10-11, record `2026/10/11/SCOPE-complete-intrinsic-graph-ech-persistence-of-multipartite-graphs--4c8b867ce9c1`, `RESULT.md`.
3. D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008, for simplicial cofibrations, the nerve lemma, and standard suspension/join facts.
