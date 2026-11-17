# Equivariant topology of non-strongly-connected digraph complexes and regular-group subgroup lattices

## Finding
For an integer \(n\ge3\), let \(\mathrm{NSC}_n\) denote the simplicial complex with vertex set the \(n(n-1)\) directed arcs \((i,j)\), \(i\ne j\), and a face for every arc set whose directed graph is not strongly connected. The symmetric group \(S_n\) acts by relabeling vertices. Put \(V_n=\{(u_1,\ldots,u_n)\in\mathbb R^n:\sum u_i=0\}\), and let \(\overline\Pi_n\) be the proper part of the set-partition lattice on \([n]\), acted on by relabeling.

**Theorem.** There exists a genuine \(S_n\)-equivariant homotopy equivalence
\[
 |\mathrm{NSC}_n|\simeq_{S_n} S(V_n)*|\overline\Pi_n|.
\]
Here \(S(V_n)\) is the unit sphere of the vertex-augmentation representation; the diagonal action on the join is understood. In particular, for every transitive subgroup \(H\le S_n\),
\[
 |\mathrm{NSC}_n|^H\simeq |(\overline\Pi_n)^H|.
\]
An \(H\)-fixed partition is an invariant equivalence relation, not necessarily a partition into pointwise fixed blocks.

**Regular-action corollary.** For every finite group \(G\) with \(|G|\ge3\), regard \(G\) as a regular permutation group on its own elements. Its invariant partitions are precisely the coset partitions arising from subgroups. Writing \(\overline L(G)\) for the poset of subgroups strictly between \(\{1\}\) and \(G\), one obtains
\[
 |\mathrm{NSC}_{|G|}|^G\simeq |\overline L(G)|.
\]
In particular, for cyclic \(G=C_n\) with \(n\ge3\), the fixed space is empty if \(n\) is prime, contractible if \(n\) is nonsquarefree, and homotopy equivalent to \(S^{\omega(n)-2}\) if \(n\) is squarefree composite, where \(\omega(n)\) is the number of distinct prime factors. For \(G=(C_p)^r\), \(r\ge2\), the fixed space is a wedge of \(p^{\binom r2}\) spheres of dimension \(r-2\). For the regular action of \(S_3\) on six letters the fixed space is four isolated points.

## Assumptions and scope
All arc sets use a directed loopless complete graph, so an ordered pair and its reverse are two different vertices. Strong connectivity is understood on the full labeled vertex set, even when some vertices are isolated. The statement is a homotopy equivalence of finite \(S_n\)-spaces in the **genuine** sense: the map is a homotopy equivalence on the fixed-point spaces of every subgroup, not merely on the underlying spaces or their homology. It is not a claim of equivariant PL homeomorphism. The main theorem uses \(n\ge3\); the two-vertex complex is a separate degenerate case.

## Proof
**1. Constellation model and an equivariant poset map.** Associate the directed arc \((i,j)\) with the root \(z_{ij}=(e_j-e_i)/\sqrt 2\) on \(S(V_n)\). For a nonempty arc set \(I\), put \(C_I=\operatorname{cone}\{z_{ij}:(i,j)\in I\}\) and let \(W_I=C_I\cap(-C_I)\) be its lineality space. A directed graph is acyclic exactly when its roots belong to a common open hemisphere (a strictly monotone real potential is a topological ordering). It is non-strongly-connected exactly when its roots belong to a common **closed** hemisphere: the condensation directed acyclic graph admits a nonconstant nondecreasing potential, while a potential nondecreasing on all arcs of a strongly connected graph must be constant. This is the type-A specialization established in Ayzenberg–Beketov–Magai.

Let \(\mathrm{DAG}_n\) be the acyclic arc complex, and let \(\mathcal F\) denote the poset of nonempty faces. The type-A hyperplane arrangement's proper flat lattice, identified by taking orthogonal complements, is \(\overline\Pi_n\), up to order reversal. Define
\[
 f:\mathcal F(\mathrm{NSC}_n)\longrightarrow
 \mathcal F(\mathrm{DAG}_n)+\overline\Pi_n^{\mathrm{op}}
\]
by \(f(I)=I\) if \(I\) is acyclic and \(f(I)=W_I\) otherwise, using the flat identification in the second case. The sum is the *ordered sum* of posets: all DAG faces are below all proper flats. This is the natural poset map of Ayzenberg–Beketov–Magai, Construction 2.9. The relabeling action permutes roots orthogonally and satisfies \(W_{gI}=gW_I\), hence \(f\) is \(S_n\)-equivariant.

**2. Fixed lower fibers: the additional argument.** Fix any \(H\le S_n\) and \(t\) fixed by \(H\) in the target poset. We verify contractibility of \(f^{-1}(T_{\le t})^H\). If \(t=I\) is a DAG face, the lower fiber has the fixed greatest element \(I\), and is contractible.

If \(t=\Pi\) is a proper nonzero arrangement flat, the lower fiber is the face poset of \(K_\Pi=\{I:W_I\subseteq\Pi\}\). For each root \(z_i\), define the closed convex polyhedron
\[
 B_i=\begin{cases}
 \{u\in V_n:\langle u,z_i\rangle\ge0\},&z_i\in\Pi,\\
 \{u\in V_n:\langle u,z_i\rangle\ge1\},&z_i\notin\Pi.
 \end{cases}
\]
The convex-cover construction and recession-cone argument in Ayzenberg–Beketov–Magai, Proposition 2.12 and Lemma 2.13, identify \(K_\Pi\) with the nerve of \(\{B_i\}\). Because \(\Pi\) is an \(H\)-fixed flat, this collection is \(H\)-stable. The geometric fixed-point set of the nerve equals the order-complex fixed space of its nonempty face poset. It has a simplicial orbit model whose vertices are the \(H\)-orbits \(O\) of roots and whose faces are orbit unions having nonempty intersection of the corresponding polyhedra. This is exactly the nerve of the convex sets
\[
 C_O=V_n^H\cap\bigcap_{i\in O}B_i.
\]
Indeed, if an \(H\)-invariant intersection of the \(B_i\) is nonempty, averaging any point in the intersection over \(H\) produces a point of \(V_n^H\) in it; convexity preserves every inequality. The union of the \(C_O\) covers \(V_n^H\): a nonzero proper arrangement flat contains at least one antipodal root pair, whose two corresponding closed halfspaces already cover all of \(V_n\); for a fixed point lying in \(B_i\), its entire \(H\)-orbit of labels also contains that point. All finite intersections are convex. The finite convex nerve theorem implies the fixed nerve is homotopy equivalent to the contractible space \(V_n^H\). Therefore every lower fiber is contractible **after taking \(H\)-fixed points**, which is stronger than its ordinary contractibility.

Quillen's poset fiber theorem, applied to every fixed-poset map \(f^H\), gives a homotopy equivalence on all subgroup-fixed spaces. The equivariant Whitehead criterion for finite group CW complexes then gives a genuine \(S_n\)-equivariant homotopy equivalence from \(|\mathrm{NSC}_n|\) to the realization of the ordered sum.

**3. Equivariant identification of the DAG factor.** The open hemispheres with centers \(z_{ij}\) cover \(S(V_n)\), and their nerve is \(\mathrm{DAG}_n\). The equivariant nerve equivalence follows directly on fixed points. For any \(H\), an \(H\)-invariant family of hemispheres with nonempty intersection has an \(H\)-fixed witness: average a witness over \(H\), obtaining a nonzero vector satisfying every strict inequality, and normalize. Thus the fixed face nerve is the nerve of a good open cover of \(S(V_n^H)\) by orbit intersections. When \(V_n^H=0\), both fixed spaces are empty. Consequently \(|\mathrm{DAG}_n|\simeq_{S_n}S(V_n)\). Since realizations of ordered sums are joins, the theorem follows.

**4. Transitive and regular corollaries.** For transitive \(H\), \(V_n^H=0\), so the only fixed points of the join are contributed by the partition-lattice end. A regular group's invariant equivalence relations are exactly its left-translation-invariant equivalences: the class of the identity is a subgroup, and the other classes are its translates. This proves the regular-action statement. For cyclic groups the proper subgroup poset is the proper divisor lattice, whose order complex is the boundary of an \((\omega(n)-1)\)-simplex if squarefree, and is contractible if a prime-power exponent exceeds one. For elementary abelian groups the subgroup poset is the proper nonzero-subspace building; its Solomon–Tits homotopy type is a wedge of \(p^{\binom r2}\) spheres in degree \(r-2\).

## Verification
A standalone Python script accompanies this statement. It computes true geometric fixed-face complexes by taking arc orbits, enumerating their unions, and testing strong connectivity by transitive closure. It checks all permutation cycle types for \(2\le n\le5\), all ten nonidentity classes of \(S_6\), all cyclic regular fixed complexes for \(2\le n\le12\), and the regular actions of \(S_3\), \((C_2)^2\), and \((C_2)^3\). Exact binary boundary ranks verify the predicted reduced homology in the indicated small cases. The independent Euler-character traces agree with the standard multilinear free-Lie character \(\mu(d)d^{k-1}(k-1)!\) on permutations with \(k\) cycles of equal length \(d\), and zero on other cycle types. These finite checks corroborate the theorem but do not replace the infinite proof. Run `python3 verify.py` using the standard Python library; see `verification_output.txt` for the recorded output.

## Relationship to prior work
Björner–Welker determined the **nonequivariant** homotopy type of the non-strongly-connected digraph complex as \(\bigvee^{(n-1)!}S^{2n-4}\); Hultman proved related directed-subgraph results. Ayzenberg–Beketov–Magai constructed the decisive type-A big-constellation model and the **nonequivariant** poset-map join decomposition. The present point is the additional fixed-fiber argument for arbitrary permutation subgroups, which upgrades that decomposition to genuine equivariance. The resulting realization of proper subgroup lattices as fixed spaces of a single canonical digraph-complex family is not obtained from the nonequivariant wedge formula alone. The Solomon–Tits classification of elementary abelian subgroup lattices and the known partition-lattice Lie representation are used as existing ingredients, not claimed as new.

## Limitations
This result is a genuine equivariant homotopy equivalence, not a homeomorphism or an equivariant simple-homotopy equivalence. It applies to the **complete loopless directed graph** on at least three vertices and does not directly classify non-strongly-connected subcomplexes of arbitrary ambient digraphs. The older Björner–Welker full article was inaccessible during this comparison; consequently an unrecognized earlier equivariant refinement or a differently described equivalent theorem remains a publication-priority risk. The 2023 join construction is a very close precursor; the new part is its subgroup-fixed fiber refinement and consequences. This is not independent mathematical validation.

## References
1. E. Babson, A. Björner, S. Linusson, J. Shareshian, V. Welker, *Complexes of not i-connected graphs*, arXiv:math/9705219 (first posted 1997-05-11). Background on symmetry and graph-connectivity complexes.
2. A. Björner and V. Welker, *Complexes of Directed Graphs*, SIAM J. Discrete Math. 12 (1999), 413–424, DOI 10.1137/S0895480198338724.
3. A. Hultman, *Directed Subgraph Complexes*, Electron. J. Combin. 11 (2004), R75, DOI 10.37236/1828 (published 2004-10-26).
4. A. Ayzenberg, M. Beketov and G. Magai, *Coverings by open and closed hemispheres*, arXiv:2310.02827v1 (posted 2023-10-04), especially Construction 2.9, Theorem 5 and Lemmas 2.13–2.14.
5. A. Björner and M. L. Wachs, *Geometrically Constructed Bases for Homology of Partition Lattices of Types A, B and D*, Electron. J. Combin. 11 (2004), R3, DOI 10.37236/1860.
6. E. Gottlieb and M. L. Wachs, *Cohomology of Dowling Lattices and Lie (Super)Algebras*, Adv. Appl. Math. 24 (2000), 301–336, DOI 10.1006/aama.1999.0670.
