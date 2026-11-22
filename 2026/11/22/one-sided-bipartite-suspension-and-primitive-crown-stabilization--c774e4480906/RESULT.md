# One-sided bipartite suspension and primitive crown stabilization

## Finding
Let \(\mathcal N[G]\) be the simplicial complex of subsets contained in a closed graph neighborhood \(N_G[v]=\{v\}\cup N_G(v)\). The general mechanism is as follows:

**One-sided suspension theorem.** If \(G=A\sqcup B\) is a nonempty finite connected simple bipartite graph, no vertex is isolated, and some \(b_\ast\in B\) has \(N_G(b_\ast)=A\), then
\[
|\mathcal N[G]|\simeq\Sigma|G|\simeq\bigvee^{|E(G)|-|V(G)|+1}S^2.
\]
Here \(\Sigma\) is the *unreduced suspension*. The connecting map in the Mayer--Vietoris sequence gives a natural integral \(\widetilde H_2(\mathcal N[G])\cong H_1(G)\) isomorphism under every bipartition-preserving automorphism. Only one shore needs a universal vertex.

**Rectangular-crown stabilization and symmetry.** Fix integers \(m\ge5\) and \(k\ge1\). Write \(A=\{a_1,\ldots,a_m\}\), \(B=\{b_1,\ldots,b_m,c_1,\ldots,c_k\}\), and let \(G_{m,k}\) have every cross edge except the \(m\) disjoint pairs \(a_i b_i\). Put \(X_{m,k}=\mathcal N[G_{m,k}]\). Then
\[
X_{m,k}\simeq\bigvee^{r_{m,k}}S^2,
\qquad r_{m,k}=m^2+mk-3m-k+1.
\]
The **complete integral degree-two symmetry module** under \(\operatorname{Aut}(G_{m,k})=S_m\times S_k\) is the graph-cycle lattice
\[
\widetilde H_2(X_{m,k};\mathbb Z)\cong
\ker\bigl(\partial:\mathbb Z^{E(G_{m,k})}\to\mathbb Z^{V(G_{m,k})}\bigr),
\]
with each edge oriented from \(A\) to \(B\). For \((\sigma,\tau)\in S_m\times S_k\), let \(f\) and \(e\) be the numbers of fixed indices of \(\sigma\) and \(\tau\). Its rational character, indeed the trace of the integral map, is
\[
\operatorname{tr}((\sigma,\tau)_*\mid\widetilde H_2)=f^2+fe-3f-e+1.
\]
In particular \(\widetilde H_*(X_{m,k}/(S_m\times S_k);\mathbb Q)=0\).

For the known balanced crown \(G_{m,0}\), the two additional \((m-2)\)-sphere classes disappear immediately when the first \(c\)-vertex is attached. Each consecutive vertex attachment, starting at \(k=0\), induces a **primitive injection**
\[
\widetilde H_2(X_{m,k};\mathbb Z)\hookrightarrow
\widetilde H_2(X_{m,k+1};\mathbb Z)
\]
with cokernel canonically the \(S_m\)-augmentation lattice
\[
I_m=\{(z_1,\ldots,z_m)\in\mathbb Z^m:\textstyle\sum_i z_i=0\},
\qquad\operatorname{rank}I_m=m-1,
\]
relative to the subgroup fixing the newly attached vertex. This specifies the integral symmetry of each new homology layer, not merely the change in Betti numbers.

## Assumptions and scope
All graphs here are finite, simple, undirected and nonempty. A bipartition is fixed; group actions on the general one-sided suspension statement preserve this bipartition. \(\mathcal N[G]\) uses **closed** graph neighborhoods, not Lovász's open-neighborhood complex. Geometric realizations are understood. Reduced and unreduced integral homology use the usual orientation conventions. The rectangular family has \(m\ge5\) throughout the stabilization and equivariance statements so that the balanced crown's higher sphere dimension \(m-2\) is distinct from two. The sphere-wedge assertions concern ordinary homotopy equivalence, not equivariant homotopy equivalence.

## Proof
**1. The one-sided suspension lemma.** For any such bipartite \(G=A\sqcup B\), put
\[
U=\bigcup_{a\in A}\Delta(N_G[a]),\quad
V=\bigcup_{b\in B}\Delta(N_G[b]).
\]
Then \(\mathcal N[G]=U\cup V\). A face of \(U\) contains at most one vertex of \(A\); a face of \(V\) contains at most one vertex of \(B\). Since every vertex has a neighbor, \(U\cap V\) contains exactly the vertices and cross edges of \(G\), and nothing else: \(U\cap V=G\) as an abstract one-dimensional simplicial complex.

Because every \(N_G[a]\) contains \(b_\ast\), the subcomplex \(U\) is a cone with apex \(b_\ast\). For the other half, the facet centered at \(b_\ast\) includes the full \(A\)-simplex. For each \(b\in B\setminus\{b_\ast\}\), all faces of \(V\) involving \(b\) lie in the simplex \(\Delta(\{b\}\cup N_G(b))\), attached along its nonempty base \(\Delta(N_G(b))\subseteq\Delta(A)\). Since it is a cone over a nonempty simplex, it collapses relative to its base. These collapses remove all vertices in \(B\setminus\{b_\ast\}\), leaving the simplex \(\Delta(\{b_\ast\}\cup A)\). Thus both \(U\) and \(V\) are contractible.

Their intersection inclusions are cofibrations. The union is the homotopy pushout of \(U\leftarrow G\to V\), hence equivalent to the homotopy pushout of two constant maps, which is the unreduced suspension \(\Sigma G\). Because \(G\) is connected and one-dimensional, this is a wedge of precisely \(b_1(G)=|E|-|V|+1\) two-spheres, with zero copies interpreted as contractible. The natural Mayer--Vietoris sequence gives
\[
\delta:\widetilde H_2(U\cup V;\mathbb Z)\xrightarrow{\cong}H_1(U\cap V;\mathbb Z)=H_1(G;\mathbb Z).
\]
The halves and intersection are invariant under every bipartition-preserving graph automorphism, so \(\delta\) is equivariant *integrally*. There is no claim of a canonical equivariant suspension homotopy equivalence.

**2. The rectangular family.** The graph \(G_{m,k}\) is connected for the stated parameters and has \(2m+k\) vertices and \(m(m+k-1)\) edges. Any \(c_j\) is universal to \(A\), and no vertex is isolated. Step 1 applies, giving
\[
r_{m,k}=m(m+k-1)-(2m+k)+1=m^2+mk-3m-k+1.
\]
Its unequal shore sizes force each automorphism to preserve the shores. Among vertices in \(B\), exactly the \(c_j\) have full \(A\)-neighborhood; the remaining \(b_i\) have distinct omitted partners \(a_i\). Thus every automorphism permutes matched pairs simultaneously, freely permutes the extra vertices, and there are no others: the full group is \(S_m\times S_k\).

**3. Complete character and quotient.** Orient each edge from \(A\) to \(B\). Since a connected graph has no two-cells, its chain sequence
\[
0\to H_1(G;\mathbb Z)\to C_1(G;\mathbb Z)\xrightarrow{\partial}C_0(G;\mathbb Z)\to\mathbb Z\to0
\]
is exact and equivariant. A permutation with \(f\) fixed matched indices and \(e\) fixed extra vertices fixes precisely \(f(f-1)+fe\) oriented edges and \(2f+e\) vertices. Taking traces gives \(f^2+fe-3f-e+1\) on \(H_1\) and, by step 1, on \(\widetilde H_2\). Averaging over the group uses \(\mathbb E[f]=\mathbb E[e]=1\), \(\mathbb E[f^2]=2\) for \(m\ge2\), and independent \(\mathbb E[fe]=1\). Hence the invariant subspace has dimension \(2+1-3-1+1=0\). For a finite simplicial group action, barycentric subdivision makes the action without inversions and identifies the rational homology of the geometric quotient with the invariant rational homology. Therefore the quotient is rationally acyclic. This does not assert that it is contractible or integrally acyclic.

**4. The balanced endpoint.** For \(k=0\), the hemispheres from step 1 instead collapse onto the boundaries of the \((m-1)\)-simplices on the two shores, each a sphere \(S^{m-2}\). Their intersection is the balanced crown \(G_{m,0}\) with cycle rank \(m^2-3m+1\). Since \(m\ge5\), the hemispheres are simply connected and the maps from this connected graph to them are nullhomotopic. The homotopy pushout is the **previously published** balanced-crown type
\[
X_{m,0}\simeq\bigvee^{m^2-3m+1}S^2\vee S^{m-2}\vee S^{m-2}.
\]
The new assertions concern what happens when universal vertices on just one shore are appended. In degree two the endpoint's Mayer--Vietoris connecting map still identifies \(H_2(X_{m,0})\) with \(H_1(G_{m,0})\), because the two hemispheres have no positive homology below degree \(m-2\ge3\).

**5. Exact stabilization sequence.** Adding \(c_{k+1}\) connects one new vertex to all \(m\) vertices of \(A\), leaving the earlier graph induced. The relative cellular graph complex \((G_{m,k+1},G_{m,k})\) has \(C_1^{\mathrm{rel}}=\mathbb Z^m\), \(C_0^{\mathrm{rel}}=\mathbb Z\), and differential \((z_i)\mapsto\sum_i z_i\). Thus \(H_1^{\mathrm{rel}}=I_m\), and \(H_0^{\mathrm{rel}}=0\). The long exact sequence of the pair yields
\[
0\to H_1(G_{m,k};\mathbb Z)\to H_1(G_{m,k+1};\mathbb Z)\to I_m\to0.
\]
This is an integral \(S_m\times S_k\)-module exact sequence for the subgroup fixing the new vertex (\(S_k\) acts trivially on the quotient). The graph inclusions induce inclusions of their closed-neighborhood complexes; naturality of the Mayer--Vietoris connecting maps (also at \(k=0\) for degree two) carries the short exact sequence to \(\widetilde H_2\). The cokernel is free, hence the injection is primitive and splits as abelian groups, without claiming an integral equivariant splitting. At \(k=0\), the old two degree-\(m-2\) generators map into a complex with only degree-two homology, so both die immediately. All assertions follow for every \(k\ge0\).

## Verification
The companion standard-library Python file `verify.py` builds closed-neighborhood faces directly from adjacency, forms both hemispheres, checks the **exact** intersection with the original graph, computes mod-two simplicial homology by exact binary boundary ranks, and computes Lefschetz traces by signed fixed simplices. Its recorded run (`check_output.txt`) verifies nine rectangular instances \(3\le m\le5\), \(1\le k\le3\), and 270 individual automorphism traces for \(m=3,4\), \(k=1,2,3\). Three balanced endpoint controls are also checked at \(m=4,5,6\). All tests passed. The checker corroborates the statement and its boundary but is not an infinite proof; the integral and all-parameter claims follow from steps 1--5.

## Relationship to prior work
Matsushita's *Closed neighborhood complexes of graphs*, first public 2025-11-16 [1], defines this construction and relates the suspension of a **complement's** closed-neighborhood complex to an independence complex (Theorem 1.2), and identifies its fundamental group (Theorem 1.5). Sections 1, 3 and 5 and Example 3.5 were inspected. They do not evaluate the one-sided-universal bipartite family, its integral symmetry lattice, or the vertex-stabilization maps here.

The published *An edge-restoration transition for closed-neighborhood complexes of crown graphs* [2] establishes \(\mathcal N[G]\simeq\Sigma G\) when **both** shores have universal vertices and analyzes adding back matching **edges** to a balanced crown. Its two-hemisphere proof is a close and explicitly credited antecedent. The present theorem has only one universal shore and studies addition of new universally connected **vertices**, with a nontrivial rank-\(m-1\) integral augmentation quotient and complete \(S_m\times S_k\)-characters. The former theorem's stated domain does not cover these graphs; its homotopy-pushout method is adapted here. The existing balanced-crown homotopy and symmetry classifications [3,4] completely cover \(k=0\), which is treated as prior context, not a new endpoint.

Adams, Shukla and Singh's *Čech complexes of hypercube graphs* [5] concerns hypercubes, including the \(m=4,k=0\) crown isomorphism to the three-cube, but not the stated rectangular stabilization for \(m\ge5,k\ge1\). No queried exact-value table or stronger claim covering the augmentation sequence and full character was found; this is not a guarantee against unindexed equivalent work.

## Limitations
The symmetry and persistence statements hold for the specified rectangular matching-defect family with \(m\ge5\), not arbitrary deleted-edge patterns. The general one-sided lemma assumes finite connected bipartite graphs without isolated vertices and a universal vertex to one opposite shore. The proof identifies integral homology modules, not a full equivariant homotopy type. Rational acyclicity of a quotient does not establish its contractibility or absence of integral torsion. The homotopy type at \(k=0\) is already published. The checker is finite and cannot itself establish the unbounded theorem; older unindexed equivalent literature remains a priority risk.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v1, first public 2025-11-16, https://arxiv.org/abs/2511.12608.
2. *An edge-restoration transition for closed-neighborhood complexes of crown graphs*, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-an-edge-restoration-transition-for-closed-neighborhood-complexes--558907fe28c2.
3. *Mixed-dimensional closed-neighborhood homotopy of crown graphs*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-closed-neighborhood-homotopy-of-crown-graphs--e9b512ccf664.
4. *Closed-neighborhood homotopy and symmetry characters of crown graphs*, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-closed-neighborhood-homotopy-and-symmetry-characters-of-crown-gr--f24d531cfed5.
5. H. Adams, S. Shukla and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, https://arxiv.org/abs/2212.05871.
6. A. Hatcher, *Algebraic Topology* (2002), sections on cofibrations, suspension, Mayer--Vietoris and homotopy pushouts, https://pi.math.cornell.edu/~hatcher/AT/AT.pdf.
