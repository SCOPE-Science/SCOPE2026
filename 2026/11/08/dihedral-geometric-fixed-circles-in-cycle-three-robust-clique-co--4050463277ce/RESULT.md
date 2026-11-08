# Dihedral geometric fixed circles in cycle three-robust clique complexes

## Finding
For every integer \(n\ge3\), let \(C_n\) be the ordinary cycle on \(\mathbb Z/n\mathbb Z\), and put
\[
K_n=\{\sigma\subseteq\mathbb Z/n\mathbb Z:\alpha(C_n[\sigma])\le2\},
\]
the three-robust clique (bounded-independence) complex. Let \(r_a(i)=i+a\) and \(s_a(i)=a-i\) denote the standard rotations and reflections. The following is a **geometric pointwise fixed-space** classification, not merely a homology-character statement.

For \(3\le n\le5\), the fixed space \(|K_n|^g\) is contractible for every dihedral element \(g\). For \(n\ge6\), all reflections have geometric fixed-point spaces PL-homeomorphic to polygons:
\[
|K_n|^{s_a}\cong_{\mathrm{PL}}\begin{cases}
|C_{(n+1)/2}|,&n\text{ odd},\\
|C_{n/2+1}|,&n\text{ even and }a\text{ even},\\
|C_{n/2}|,&n\text{ even and }a\text{ odd}.
\end{cases}
\]
For a nonidentity rotation \(r_a\) with \(1\le a<n\),
\[
|K_n|^{r_a}\cong_{\mathrm{PL}}\begin{cases}
|C_{n/2}|,&n\text{ even and }a=n/2,\\
\varnothing,&\text{otherwise}.
\end{cases}
\]
Thus every nonempty fixed locus of a **nonidentity** symmetry at \(n\ge6\) is a circle; rotations of order at least three have empty fixed loci. The precise numbers of vertices in the canonical fixed-locus triangulations distinguish the two reflection-axis types when \(n\) is even.

## Assumptions and scope
Here \(\alpha\) denotes ordinary graph independence number. Vertices of \(C_n\) are joined when their residue classes differ by \(1\) or \(-1\). All geometric fixed points are **pointwise** fixed under the piecewise-linear action on the usual simplicial realization. The notation \(|C_m|\) denotes the realization of the one-dimensional **unfilled** cycle on \(m\ge3\) vertices. The result concerns individual elements, not simultaneous fixed points for arbitrary noncyclic subgroups. It makes no assertion about the fixed set of the identity for \(n\ge6\).

## Proof
**1. Exact fixed-orbit model.** Let \(g\) be a permutation of the vertex set preserving \(K_n\), and let \(\mathcal O\) be its collection of complete vertex orbits. Construct a complex \(F_g\) on orbit symbols by making a family \(\mathcal U\subseteq\mathcal O\) a face precisely if \(\bigcup_{O\in\mathcal U}O\) is a face of \(K_n\). In any simplex of \(K_n\) preserved setwise by \(g\), the coefficients of a fixed geometric point are equal along each orbit. Therefore sending an orbit symbol to the barycenter of its original vertices, with the obvious orbit-weight normalization, is a piecewise-linear homeomorphism \(|F_g|\to|K_n|^g\). In particular, fixed vertices alone do **not** describe the full geometric fixed set.

**2. Maximum face size and pair criterion.** Assume \(n\ge6\). Every vertex subset with at least five elements contains an independent triple: a proper induced subgraph of \(C_n\) is a disjoint union of paths, with independence number at least the ceiling of half its vertex number; for the entire cycle the same conclusion holds since \(\lfloor n/2\rfloor\ge3\). Consequently a face of \(K_n\) has at most four vertices. A triple of original vertices is admissible exactly when it contains a cycle edge. For a four-element subset that induces a forest, independence number at most two is equivalent to the existence of a perfect matching of two cycle edges: the forest is bipartite and \(\alpha=4-\nu\) by the matching-cover equality. The same perfect-matching test applies to a four-subset of the even cycle, which is bipartite. Since \(n\ge6\), a four-subset is always proper and therefore induces a forest.

**3. Rotations.** Let \(d=\gcd(n,a)\) and \(\ell=n/d\), the order of \(r_a\). Each vertex orbit comprises a regularly spaced \(\ell\)-set. If \(\ell\ge3\), when \(d\ge2\) three consecutive orbit positions are independent (their circular gaps are at least two), while for \(d=1\) the orbit equals the whole cycle and contains an independent triple. Thus \(F_{r_a}\) has no vertices and its realization is empty. If \(\ell=2\), then \(n=2k\), \(a=k\), and the orbits are \(O_i=\{i,i+k\}\) for \(i\in\mathbb Z/k\mathbb Z\). Two orbit symbols span an edge exactly when their indices are adjacent modulo \(k\): their four vertices then admit two disjoint cycle edges, while nonadjacent positions induce no two-edge perfect matching. Three orbits contain six original vertices and are forbidden by Step 2. Therefore \(F_{r_k}\) is exactly the unfilled \(C_k\), with \(k\ge3\).

**4. Odd reflections.** Let \(n=2k+1\ge7\). Conjugating by a rotation reduces to \(s_0\). Its orbits are \(O_0=\{0\}\) and \(O_i=\{i,n-i\}\) for \(1\le i\le k\). In particular \(O_k\) is a pair of adjacent vertices. For \(1\le i<j\le k\), the union of the two size-two orbits has a perfect matching exactly when \(j=i+1\). The singleton \(O_0\) is compatible exactly with \(O_1\) (an original edge) and \(O_k\) (the internal edge of that orbit). Any three orbit symbols cover at least five original vertices and are forbidden by Step 2. Hence \(F_{s_0}\) is \(O_0-O_1-\cdots-O_k-O_0\), the unfilled cycle \(C_{k+1}\).

**5. Even vertex-axis reflections.** Let \(n=2k\ge6\) and \(a\) even. By rotation conjugacy assume \(a=0\), with two singleton orbits \(O_0=\{0\}\), \(O_k=\{k\}\) and pairs \(O_i=\{i,n-i\}\) for \(1\le i<k\). Exactly the consecutive pairs \(O_iO_{i+1}\) are compatible, along with \(O_0O_k\) (any original two-element set is admissible). Two size-two orbits need a matching of two cycle edges; a singleton together with one size-two orbit requires an original edge. The union of both singleton orbits and any size-two orbit admits no perfect matching, hence is forbidden. Every other triple of orbit symbols contains at least five original vertices and is forbidden by Step 2. The fixed orbit complex is precisely the unfilled \(C_{k+1}\).

**6. Even edge-axis reflections.** Let \(n=2k\ge6\) and \(a\) odd. Assume \(a=1\), with \(k\) size-two orbits \(O_i=\{i+1,-i\}\), \(0\le i<k\). The endpoint orbits \(O_0\) and \(O_{k-1}\) are themselves original graph edges. For two distinct orbits, the required two-edge matching exists exactly when their indices are successive, or when they are the two endpoint orbits (whose own internal edges provide the matching). There are no triples of orbit symbols, since three size-two orbits cover six original vertices. Thus \(F_{s_1}\) is the unfilled \(C_k\). Reflection types exhaust all possibilities.

**7. Small cycles.** For \(n=3,4,5\), the independence number of \(C_n\) is at most two, so \(K_n\) is a full simplex. Its fixed points under any vertex permutation form the nonempty simplex spanned by complete orbit barycenters, hence are contractible. This proves the complete statement. \(\square\)

## Verification
Run `python3 verify_dihedral_fixed.py` with Python 3.9 or newer. This independent enumeration builds every vertex orbit directly from each dihedral permutation, forms all allowable orbit unions by checking **every** original independent triple, and tests connectivity, degrees, vertices, edges, and absence of higher faces. It checked every nonidentity dihedral action for every \(3\le n\le35\), including all vertex-axis and edge-axis reflections. Its recorded output is provided as `verification_output.txt`; no external dependencies are required. Finite checks corroborate the proof but do not establish the unrestricted result.

## Relationship to prior work
Filakovský's 2026 paper introduced and systematically studied these three-robust clique complexes for square-sequence and grid graphs, rather than geometric dihedral fixed spaces of cycles. Carnero Bravo's 2026 Corollary 32 establishes that the underlying cycle bounded-independence complexes have the nonequivariant homotopy type \(S^3\) for \(n\ge6\); this determines neither individual geometric fixed spaces nor their polygon triangulations. A separate published dihedral orientation calculation determines the sign action on that sphere's integral homology, and another published general bipartite equivariant Euler formula determines Lefschetz numbers for even cycles. Those character/Euler statements do not imply that the actual pointwise fixed spaces are circles rather than some other spaces with Euler characteristic zero. The present claim is a PL homeomorphism classification of the actual fixed loci, including odd cycles, reflections of both types, and every nontrivial rotation.

## Limitations
The result concerns individual dihedral elements, not intersections of their fixed sets for arbitrary subgroups, higher robust parameters, powers of cycles, or equivariant homotopy equivalences for the whole space. A broader published or unindexed equivariant geometric classification could overlap with the result. The enumerations cover only the displayed finite range; the unlimited theorem rests on the orbit and matching argument above. Independent mathematical validation has not been performed.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365v1 (first posted 2026-02-11), https://arxiv.org/abs/2602.11365; full text https://arxiv.org/html/2602.11365.
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427v1 (first posted 2026-02-24), Corollary 32 and Section 5.3, https://arxiv.org/html/2602.21427v1.
3. *Dihedral orientation characters of bounded-independence spheres on cycles*, published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-dihedral-orientation-characters-of-bounded-independence-spheres--8a099ca44501/RESULT.md.
4. *Equivariant Euler characters of three-robust clique complexes of connected bipartite graphs*, published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-equivariant-euler-characters-of-3-robust-clique-complexes-of-con--f9d874df12e5/RESULT.md.
5. *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs*, published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b/RESULT.md.
