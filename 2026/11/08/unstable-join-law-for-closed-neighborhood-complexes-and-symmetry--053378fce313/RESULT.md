# Unstable join law for closed-neighborhood complexes and symmetry of joined cycles

## Finding
For every \(k\ge2\) and every family of finite nonempty simple graphs \(G_1,\ldots,G_k\) on disjoint vertex sets, put \(J=G_1\vee\cdots\vee G_k\) for their graph join, and write \(K_i=\mathcal N[G_i]\) for their **closed**-neighborhood simplicial complexes. Then the complete **unstable homotopy type** obeys
\[
|\mathcal N[J]|\simeq\Sigma^{k-1}|K_1*\cdots*K_k|.
\]
In addition, if a group \(\Gamma\) acts on \(J\) by permuting these graph factors and by graph isomorphisms within them, then, for every integer \(q\), there is a natural isomorphism of integral \(\Gamma\)-modules
\[
\widetilde H_q(\mathcal N[J];\mathbb Z)
\cong
\operatorname{sgn}_{\mathrm{factors}}\otimes
\widetilde H_{q-k+1}(K_1*\cdots*K_k;\mathbb Z).
\]
The action on the right-hand join is the signed simplicial action induced by permutations and within-factor isomorphisms. The sign character records the induced permutation of the \(k\) graph factors.

In particular, for \(m\ge5\) and \(k\ge2\), the graph join \(J_{m,k}=C_m\vee\cdots\vee C_m\) of \(k\) copies of the \(m\)-cycle satisfies
\[
|\mathcal N[J_{m,k}]|\simeq S^{3k-2}.
\]
Its full automorphism group is \(D_m\wr S_k\), and its integral top-homology character is
\[
\chi((\gamma_1,\ldots,\gamma_k);\pi)=
\operatorname{sgn}(\pi)\prod_{i=1}^k\varepsilon(\gamma_i),
\]
where \(\varepsilon\) is \(+1\) on rotations and \(-1\) on reflections of the cycle, and \(\pi\in S_k\) permutes the factors. This top homology is a free group of rank one; all other reduced integral homology groups vanish.

## Assumptions and scope
The graphs are finite, simple, nonempty and have pairwise disjoint vertex sets. The **graph join** adds all cross edges between distinct graph factors, and must not be confused with the simplicial join \(*\). The closed-neighborhood complex \(\mathcal N[G]\) has a face \(\sigma\) precisely when \(\sigma\subseteq N_G[v]\) for some vertex \(v\), where \(N_G[v]=\{v\}\cup N_G(v)\). Every \(K_i\) therefore has nonempty realization. Suspension is unreduced. For the equivariant homology assertion, the factor-permuting action must carry each graph factor isomorphically onto another; a larger automorphism group is not asserted to preserve an arbitrary factorization. The final family \(J_{m,k}\) has full wreath-product automorphism group as proved below.

## Proof
**1. Exact cover and all intersections.** Put \(V_i=V(G_i)\), \(V=\bigsqcup_i V_i\), and \(\Delta_W\) for the full simplex on a finite vertex set \(W\). For each \(i\), set
\[
U_i=K_i*\Delta_{V\setminus V_i}.
\]
A closed neighborhood of a vertex \(v\in V_i\) in \(J\) is exactly \(N_{G_i}[v]\cup(V\setminus V_i)\). Thus the following are equalities of abstract simplicial complexes, without replacing their homotopy types:
\[
\mathcal N[J]=\bigcup_{i=1}^k U_i,
\qquad
\bigcap_{i\in S}U_i=\Bigl(*_{i\in S}K_i\Bigr)*\Delta_{V\setminus\cup_{i\in S}V_i}
\quad(\varnothing\ne S\subseteq[k]).
\]
Every proper nonempty intersection is contractible, since the last simplex has nonempty vertex set. The unique full intersection is \(K=K_1*\cdots*K_k\). All intersections are nonempty; their inclusions are simplicial cofibrations.

**2. Homotopy type without suspension cancellation.** Use the following finite-cover lemma: if \(k\ge2\) subcomplexes cover a simplicial complex, their proper nonempty intersections are nonempty and contractible, and their full intersection is \(K\ne\varnothing\), then their union is homotopy equivalent to \(\Sigma^{k-1}|K|\). To prove the lemma inductively, the union of the first \(k-1\) pieces is contractible by the nerve lemma, because all its nonempty intersections are contractible. The final piece is contractible. Their intersection is a union of \(k-1\) subcomplexes, all of whose proper nonempty intersections are contractible and whose full intersection is \(K\). Induction identifies this intersection with \(\Sigma^{k-2}|K|\). The final union is a homotopy pushout of two contractible spaces along that intersection, hence is its suspension. The base case \(k=2\) is the usual homotopy pushout of two contractible subcomplexes. Applying this lemma to the displayed cover gives the claimed **unsuspended** equivalence; no cancellation of a suspension of a previously known theorem is used.

**3. Integral symmetry.** Fix an ordering of the \(k\) factors. The augmented Mayer–Vietoris double complex for the cover has a column indexed by every nonempty subset \(S\subseteq[k]\), with differential alternating in the ordered indices. Each proper intersection is acyclic in reduced homology; the only remaining reduced-homology contribution comes from the full intersection \(K\), shifted by \(k-1\) degrees. This yields the displayed integral isomorphism, naturally for within-factor automorphisms. Permuting factor indices acts on the top Čech column through the orientation of the ordered \((k-1)\)-simplex, and therefore contributes \(\operatorname{sgn}(\pi)\). The induced action on \(K\) is the ordinary graded-permutation action on simplicial joins. The construction uses integral chains, not averaging over the symmetry group, and therefore does not impose any characteristic restriction or assert an integral splitting of unrelated extension terms.

**4. Joined cycles.** For every \(m\ge5\), each triangle \(\{i-1,i,i+1\}\) of \(\mathcal N[C_m]\) contains the free non-cycle edge \(\{i-1,i+1\}\), which lies in no other triangle. Simultaneously removing these equivariant free pairs retracts \(\mathcal N[C_m]\) onto \(C_m\). The dihedral action on \(\widetilde H_1\cong\mathbb Z\) is orientation preservation for rotations and reversal for reflections. The simplicial join of \(k\) circles is \(S^{2k-1}\); the cover lemma therefore gives a sphere of dimension \((2k-1)+(k-1)=3k-2\). A factor transposition acts on the join of circles with Koszul sign \((-1)^{(1+1)(1+1)}=+1\), while the Čech orientation sign is \(-1\); arbitrary factor permutations give \(\operatorname{sgn}(\pi)\). Finally, the complement of \(J_{m,k}\) is the disjoint union of \(k\) connected copies of \(\overline{C_m}\); since \(m\ge5\), each complement is connected. Its automorphisms may therefore permute these connected components, with automorphism group \(D_m\) on each component. This proves that the full group is \(D_m\wr S_k\) and establishes the character formula.

## Verification
The standalone standard-library program `verify.py` reconstructs graph closed neighborhoods directly from edges, compares the resulting face set with the exact two-set cover on 121 graph-pair instances, and separately tests the exact homology and signed simplicial Lefschetz traces for joins \(C_5\vee C_5\), \(C_5\vee C_6\), \(C_4\vee C_5\), \(C_4\vee C_4\), and \(C_5\vee C_7\). Its mod-two boundary-rank calculations detect the expected single sphere degree in every case, including the separate exceptional \(C_4\) behavior. Its 22 signed generator traces include rotations, reflections and equal-factor swaps. The recorded output ends `ALL_VERIFY_OK 5 22`. Finite verification is ancillary to the proof for arbitrary \(k,m\), and does not establish new priority.

## Relationship to prior work
Takahiro Matsushita's *Closed neighborhood complexes of graphs*, first public arXiv version November 16, 2025 (arXiv:2511.12608), defines the same complex. Its Theorem 1.2 relates **one suspension** \(\Sigma\mathcal N[\overline G]\) to an independence complex of a canonical double cover. When the complement is a disjoint union, that theorem and the ordinary independence-complex join law imply the **suspended** form of the present identity. This overlapping stable consequence, and any homology ranks obtainable from it, are **not** asserted to be new. That stable theorem alone does not generally permit desuspension to obtain the full unstable homotopy type. The present proof supplies an exact multi-cone cover and a direct unstable decomposition, while its signed cover-chain model makes the wreath-product action explicit.

A distinct published result, *Clique joins suspend Lovász neighborhood complexes*, treats the **open**-neighborhood complex and adjoining complete graphs. The open/closed distinction changes the complex, and its result does not imply the graph-join formula for arbitrary noncomplete factors. A complete-multipartite fixed-point classification concerns a subclass of joins of edgeless graphs and does not give this general join theorem. No claim is made that a lack of a matching indexed title proves priority; an equivalent elementary join law may be unindexed or regarded as folklore.

## Limitations
The statement is for finite simple graphs, and the displayed homotopy equivalence is nonequivariant; no global equivariant homotopy equivalence is asserted for all factor-permuting groups. The induced homology statement is integral and equivariant. The cyclic application assumes all cycles have at least five vertices; the four-cycle has a different closed-neighborhood complex. The stable homology implications of Matsushita's theorem are not new. Equivalent unindexed formulations and stronger general homotopy-colimit statements remain priority risks. Independent verification is not claimed.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v1 (first public November 16, 2025), especially Definition 1.1 and Theorem 1.2; accessible full manuscript text.
2. *Clique joins suspend Lovász neighborhood complexes*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clique-joins-suspend-lov-sz-neighborhood-complexes--46728c3e0714 (distinct open-neighborhood operation).
3. A. Hatcher, *Algebraic Topology*, Chapter 4, standard homotopy pushout, nerve and Mayer–Vietoris techniques.
