# Half-turn and reflection characters of the \(2\times2\times3\) honeycomb perfect-matching complex

## Finding
Let \(H\) be the dual graph of the \(2\times2\times3\) triangular-lattice hexagon, and let \(X=\mathcal M_p(H)\) be the simplicial complex of edge sets extendible to a perfect matching. Let \(s\) interchange the two equal short side directions of the hexagon, let \(r\) be its planar half-turn, and let \(G=\langle r,s\rangle\cong C_2\times C_2\). Then all reduced rational homology vanishes outside degree four, and the complete rational \(G\)-homology character is
\[
\bigl(\chi(1),\chi(s),\chi(r),\chi(rs)\bigr)=(2,-2,0,0).
\]
In particular,
\[
\widetilde H_4(X;\mathbb Q)\cong\mathbb Q_{(s=-1,r=1)}\oplus\mathbb Q_{(s=-1,r=-1)}.
\]
For the quotients by the three order-two subgroups and by the entire symmetry group, the only possibly nonzero reduced rational Betti number is in degree four and equals
\[
\bigl(\widetilde\beta_4(X/\langle s\rangle),\widetilde\beta_4(X/\langle r\rangle),\widetilde\beta_4(X/\langle rs\rangle),\widetilde\beta_4(X/G)\bigr)=(0,1,1,0).
\]
Thus the short-direction interchange kills rational reduced quotient homology, whereas the half-turn and the other reflection each retain one degree-four class.

## Assumptions and scope
The hexagon has consecutive side lengths \(2,2,3,2,2,3\) in the triangular lattice. Vertices of its dual graph are its \(32\) elementary triangles; an edge joins triangles sharing a complete side. This dual graph has \(41\) edges, and each of its \(50\) perfect matchings has \(16\) edges. A face of \(X\) is any subset of such a matching. The half-turn and the indicated reflections are actual planar symmetries of the hexagonal tiling, acting on the dual graph and thus on its perfect-matching complex. All groups and homology in the character calculation are over \(\mathbb Q\).

An explicit finite combinatorial model is as follows. List all weakly row- and column-decreasing matrices \(h=(h_{ij})\) of shape \(2\times2\) with entries in \(\{0,1,2,3\}\). Every matrix corresponds to one lozenge tiling and hence one perfect matching. Its \(16\) lozenges have plane-coordinate labels, in three orientations:
\[
\begin{aligned}
 (z,i-h_{ij},j-h_{ij})&\quad(0\le i,j<2),\\
 (y,i-b_i(t),t-b_i(t))&\quad(0\le i<2,\ 1\le t\le3),\\
 (x,j-a_j(t),t-a_j(t))&\quad(0\le j<2,\ 1\le t\le3),
\end{aligned}
\]
where \(b_i(t)=\#\{j:h_{ij}\ge t\}\) and \(a_j(t)=\#\{i:h_{ij}\ge t\}\). Lozenge labels encode projected unit squares and are shared across tilings exactly when the same graph edge occurs. The reflections and half-turn on these labels are
\[
\begin{array}{c|ccc}
 & (x,u,v)&(y,u,v)&(z,u,v)\\\hline
s&(y,u,v)&(x,u,v)&(z,v,u)\\
r&(x,-1-u,2-v)&(y,-1-u,2-v)&(z,-2-u,-2-v).
\end{array}
\]
These permutations preserve all \(50\) matching facets, are commuting involutions, and generate the indicated geometric four-element group.

## Proof
**Nonequivariant homology, verified afresh.** The plane-partition construction enumerates exactly \(50\) facets on \(41\) distinct edge labels. Its downward closure contains exactly \(2,517,787\) nonempty faces, with face numbers in dimensions zero through fifteen
\[
(41,706,6186,31566,104477,241386,407750,517618,501141,371866,210600,89700,27900,6000,800,50).
\]
Index the \(41\) labels lexicographically and process them in order. At pivot \(p\), match every currently unmatched face \(F\) not containing \(p\) to \(F\cup\{p\}\) whenever both remain unmatched. The full enumeration yields \(1,258,892\) matched pairs and precisely three critical faces: one of dimension zero and two of dimension four. This matching is acyclic by the ordered-pivot lemma: if a closed gradient path existed, choose the earliest pivot stage it traverses. The corresponding upward matched step inserts that pivot. It cannot subsequently be removed by an unmatched downward step from a face paired at the same stage, since that would be the matched edge; nor from a face paired at a later stage, since both the upper face and the subsequent lower face would have survived the earlier stage and would then have been paired using that pivot. Hence a closed gradient path cannot return to its starting face. The resulting discrete-Morse CW complex has one zero-cell and two four-cells, with constant attaching maps, so
\[
X\simeq S^4\vee S^4,
\]
including its integral homology. This rederives the previously established nonequivariant result; it is not presented as novel here.

**Signed fixed-face traces.** For any simplicial automorphism \(g\), the augmented Lefschetz number is the alternating trace on oriented simplicial chains, with the empty face contributing \(-1\). An invariant nonempty face \(F\) is a union of orbits of the permutation on the \(41\) vertices. If it selects \(o(F)\) orbits, the orientation sign of \(g\) on \(F\) is \((-1)^{|F|-o(F)}\), so its alternating trace contribution is \((-1)^{o(F)-1}\). Therefore
\[
\widetilde L(g)=\sum_{\substack{\varnothing\ne F\in X\\gF=F}}(-1)^{o(F)-1}-1.
\]
To evaluate this *exactly*, form the orbit complex whose vertices are the cycles of \(g\) on lozenge labels and whose faces are orbit collections whose union lies inside some perfect matching. Enumerating all orbit subsets of all \(50\) matching facets gives: for \(s\), \(23\) vertex orbits, \(7,175\) nonempty orbit faces and reduced Euler characteristic \(-2\); for \(r\), \(21\) orbits, \(1,369\) faces and characteristic \(0\); for \(rs\), \(21\) orbits, \(85\) faces and characteristic \(0\). Independent enumeration over all \(2,517,787\) original nonempty faces, testing setwise invariance and the sign of the induced permutation, gives the same three values. For the identity, the reduced Euler characteristic is \(2\).

As the sole reduced rational homology is in even degree four, the Hopf trace formula gives \(\chi(g)=\widetilde L(g)\), proving the four character values. All irreducible rational representations of \(C_2\times C_2\) are one-dimensional signs; these traces force exactly the two summands stated in the finding. The formula \(\dim H_4(X;\mathbb Q)^K=|K|^{-1}\sum_{g\in K}\chi(g)\) gives the invariant ranks. Barycentric subdivision removes simplex inversions, and rational finite-group transfer identifies the homology of the orbit space with invariant homology, giving the four quotient Betti numbers.

## Verification
Run `python3 verify_honeycomb_symmetry.py` using Python 3 with no third-party dependencies. It independently generates all plane partitions and lozenge vertices, enumerates every face, verifies both geometric generators preserve the set of matching facets and commute, verifies the complete ordered-pivot matching, and computes each reduced Lefschetz number by two distinct algorithms: orbit-face enumeration and signed fixed-original-face enumeration. Its checked output is `verification_output.txt`. All values stated in the proof are checked by exact integer and set operations. Neither an extrapolation from finite sampling nor an unproved claim about larger honeycombs is involved.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega introduced these perfect-matching complexes and computed the full one-unit-width family and the \(2\times2\times2\) homotopy type (first public preprint September 6, 2022; published June 16, 2023). Their general lozenge–plane-partition correspondence supplies the finite tiling model but does not determine this symmetry character. The publicly archived 2026 result *The \(2\times2\times3\) honeycomb perfect-matching complex is a wedge of two four-spheres* already determines the exact nonequivariant homotopy type; that fact is explicitly treated as prior work. It does not identify the action of the planar half-turn or either reflection, nor the quotient invariant dimensions. The two published treatments of rational dihedral characters for the regular \(2\times2\times2\) honeycomb address a different hexagon with sixfold, rather than only twofold, rotational symmetry. Their character tables do not imply the values for the \(2\times2\times3\) hexagon.

## Limitations
The theorem determines a rational symmetry representation and rational quotient homology for this particular hexagonal region only. It does **not** determine integral \(\mathbb Z[G]\)-module extension classes, equivariant homotopy types, or the integral homology or contractibility of the quotient spaces. The previous nonequivariant homotopy calculation is credited, not reclaimed. Relevant unindexed equivalent equivariant calculations cannot be excluded by the available bibliographic searches.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (2022-09-06); *Electronic Journal of Combinatorics* 30(2) (2023), P2.45. https://arxiv.org/abs/2209.02803
2. *The \(2\times2\times3\) honeycomb perfect-matching complex is a wedge of two four-spheres*, publicly archived research result (2026-10-18), https://github.com/published-finding corpus/2026.
3. *Dihedral homology characters of the side-two honeycomb perfect-matching complex*, publicly archived research result (2026-10-25), https://github.com/published-finding corpus/2026.
4. *Two sign lines in honeycomb perfect-matching homology*, publicly archived research result (2026-11-02), https://github.com/published-finding corpus/2026.
5. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
