# An equivariant two-skeleton model for ordinary Kneser independence complexes

## Finding
Let \(m\ge4\) be an integer. Define \(K_m\) to be the independence complex of the graph with vertices the two-element subsets of \([m]=\{1,\ldots,m\}\) and with two such vertices adjacent precisely when they are disjoint. The symmetric group \(\mathfrak S_m\) acts by permuting \([m]\). Write \(\Delta_{m-1}^{(2)}\) for the two-dimensional skeleton of the simplex on \([m]\), and write \(U_m=\ker(\varepsilon:\mathbb Z^{m}\to\mathbb Z)\), where \(\varepsilon(e_i)=1\) for each standard basis vector.

There is an \(\mathfrak S_m\)-equivariant homotopy equivalence
\[
K_m\simeq_{\mathfrak S_m}\Delta_{m-1}^{(2)}.
\]
In particular, the *integral* top-homology lattice with its natural symmetry action is
\[
\widetilde H_2(K_m;\mathbb Z)\cong_{\mathbb Z[\mathfrak S_m]}\bigwedge\nolimits^3 U_m,
\]
of free rank \(\binom{m-1}{3}\). All other reduced integral homology groups vanish. The same complex has the ordinary homotopy type \(\bigvee^{\binom{m-1}{3}}S^2\), a non-equivariant result already established by Barmak; that homotopy type is **not** claimed as new.

An explicit full rational character follows: if \(g\in\mathfrak S_m\) has \(c_j(g)\) cycles of length \(j\), then
\[
\operatorname{tr}\bigl(g\mid\widetilde H_2(K_m;\mathbb Q)\bigr)
=[t^3]\,\frac{\prod_{j\ge1}(1-(-t)^j)^{c_j(g)}}{1+t}.
\]
Thus the natural top homology is the integral exterior-power augmentation lattice, rather than merely an abstract free abelian group of the known rank.

## Assumptions and scope
Here \(m\ge4\) and graph edges join disjoint pairs of two-element subsets of \([m]\). Equivariance is with respect to the entire coordinate-permutation group \(\mathfrak S_m\). No assumption on a coefficient field is used in the integral lattice statement. The assertion concerns ordinary reduced simplicial homology, not Bredon equivariant homology.

## Proof
**1. Classification of simplices.** Write \(v_{ij}=v_{ji}\) for the graph vertex associated with the pair \(\{i,j\}\). A simplex of \(K_m\) is a family of pairwise intersecting two-element subsets. If such a family has a common label \(i\), it is contained in the star simplex \(A_i=\{v_{ij}:j\ne i\}\). If it has no common label, take \(\{i,j\},\{i,k\}\) and a third member avoiding \(i\); pairwise intersection forces this third member to be \(\{j,k\}\), and any further member meeting all three belongs to that same three-edge family. Thus the remaining maximal simplices are exactly the triangles \(T_{ijk}=[v_{ij},v_{jk},v_{ki}]\), for three distinct labels. This classification is exhaustive.

**2. A natural equivariant retraction.** Let \(L=\bigcup_i\Delta(A_i)\). For distinct \(i,j\), the two star simplices intersect in the single vertex \(v_{ij}\), and there are no triple intersections. Let \(b_i\) be the barycenter of \(\Delta(A_i)\), and let \(E_i\) be the tree formed by the segments \([b_i,v_{ij}]\) for \(j\ne i\). On the simplex \(\Delta(A_i)\), write a point as the barycentric vector \((x_j)_{j\ne i}\), and put
\[
d_j(x)=\max\bigl(0,x_j-\max_{k\ne i,j}x_k\bigr),\qquad
r_i(x)=b_i+\sum_{j\ne i}d_j(x)(v_{ij}-b_i).
\]
At most one \(d_j(x)\) is positive. Hence \(r_i\) has image in \(E_i\); it is continuous, equivariant for permutations fixing \(i\), and fixes every point of \(E_i\). In particular it fixes all intersection vertices \(v_{ij}\). The straight-line homotopy from the identity to \(r_i\) stays inside the simplex and fixes its tree. Consequently the local homotopies glue to an \(\mathfrak S_m\)-equivariant strong deformation retraction
\[
L\longrightarrow E=\bigcup_i E_i,
\]
where \(E\) is the graph obtained by subdividing every edge of the complete graph on \([m]\) at its midpoint \(v_{ij}\).

**3. Equivariant attachment of the triangles.** The complex \(K_m\) is obtained from \(L\) by attaching the triangles \(T_{ijk}\) along their entire boundaries; their interiors are pairwise disjoint and no triangle lies in \(L\). Each edge of \(\partial T_{ijk}\) is contained in exactly the star simplex centered at the common label of its endpoint pairs. The retraction \(r_i\) sends this edge homeomorphically to the two-edge route through \(b_i\). Thus, after replacing \(L\) by \(E\), the attaching boundary is the simple six-edge loop
\[
b_i\to v_{ij}\to b_j\to v_{jk}\to b_k\to v_{ki}\to b_i.
\]
This is precisely the subdivided boundary of the triangle on labels \(\{i,j,k\}\). The construction and all attaching maps commute with \(\mathfrak S_m\). Equivariant homotopy invariance of attachment along cofibrations therefore identifies \(K_m\) with the ordinary two-skeleton of the \((m-1)\)-simplex as an \(\mathfrak S_m\)-space, up to equivariant homotopy.

**4. Integral lattice, dimensions, and character.** Put \(W=\mathbb Z^m\) with its permutation basis \((e_i)\). The two-chains of the simplex two-skeleton identify equivariantly with \(\bigwedge^3 W\), where the oriented triangle \([i,j,k]\) corresponds to \(e_i\wedge e_j\wedge e_k\). The boundary homomorphism is contraction with \(\varepsilon:W\to\mathbb Z\), namely
\[
\partial_2(e_i\wedge e_j\wedge e_k)
=e_j\wedge e_k-e_i\wedge e_k+e_i\wedge e_j.
\]
Choosing any integral vector \(w\) with \(\varepsilon(w)=1\) gives an abelian-group decomposition \(W=U_m\oplus\mathbb Zw\). Contraction kills \(\bigwedge^3U_m\) and maps \(w\wedge\bigwedge^2U_m\) isomorphically onto \(\bigwedge^2U_m\). Hence \(\ker\partial_2=\bigwedge^3U_m\), as a *canonical equivariant sublattice*; the auxiliary splitting need not be equivariant. The full simplex is contractible, so its two-skeleton has trivial first reduced homology and trivial reduced homology outside degree two. Its integral second homology is this kernel, with rank \(\binom{m-1}{3}\).

Finally, for the permutation representation \(W\), \(\det(1+t g\mid W)=\prod_j(1-(-t)^j)^{c_j(g)}\). Since \(W\otimes\mathbb Q\cong\mathbb Q\oplus(U_m\otimes\mathbb Q)\), dividing by \(1+t\) gives the determinant generating function on \(U_m\). Its coefficient of \(t^3\) is the character of \(\bigwedge^3U_m\), as asserted.

## Verification
The included `verify.py` generates all faces for \(4\le m\le7\), computes the reduced mod-two boundary ranks exactly, and checks they agree with the integral theorem's Betti predictions. For \(m=4,5,6\), it additionally enumerates every one of the \(24\), \(120\), and \(720\) coordinate permutations and compares the simplicial signed Lefschetz trace with the exterior-cube character formula; all \(864\) comparisons passed. The separate mathematical proof establishes all integers \(m\ge4\) and integral coefficients; finite computations are corroboration rather than a substitute for that proof. See `verify_output.txt` for actual output.

## Relationship to prior work
Barmak's Theorem 4.11 establishes the ordinary homotopy type of this *same* independence complex as a wedge of \(\binom{m-1}{3}\) two-spheres, using a contractible star cluster centered at a distinguished label. The present claim concerns a stronger, fully permutation-equivariant model and the resulting complete integral symmetry lattice, neither of which follows from the nonequivariant homotopy-type statement alone. Braun's work treats the *stable* Kneser subgraphs, not this full graph. Recent work on pairwise-intersecting triples addresses different complexes. The ordinary open-neighborhood complex and the intrinsic Čech complex of a Kneser graph are likewise different objects from its independence complex.

## Limitations
The result is restricted to families of two-element subsets (ordinary Kneser graphs with that subset size). It does not classify independence complexes built from three-element or larger intersecting set systems. The new equivariant identification builds on a known nonequivariant theorem, and overlap with unindexed equivariant literature remains possible. There has been no independent mathematical audit.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, July 2, 2010, Section 4.6, Theorem 4.11; subsequently *Advances in Mathematics* 241 (2013), 33–57.
2. B. Braun, *Independence Complexes of Stable Kneser Graphs*, *Electronic Journal of Combinatorics* 18(1) (2011), P118; DOI:10.37236/605.
3. Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394v1, October 12, 2026, Introduction (for distinction between the ordinary two-subset and triple cases).
