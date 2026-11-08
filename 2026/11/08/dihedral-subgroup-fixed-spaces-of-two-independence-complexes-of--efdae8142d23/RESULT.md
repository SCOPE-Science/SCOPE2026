# Dihedral subgroup fixed spaces of two-independence complexes of cycles

## Finding
For every integer \(n\geq3\), let \(X_n=\operatorname{Ind}_2(C_n)\): its faces are the subsets of the cyclically ordered vertex set \(\mathbb Z/n\mathbb Z\) having no three consecutive vertices. Let \(D_n=\langle r,s\rangle\) act by \(r(i)=i+1\), \(s(i)=-i\). The following describes the **geometric** fixed-point spaces \(|X_n|^H\) for **every** subgroup \(H\leq D_n\).

Every subgroup is either a rotation subgroup \(H=\langle r^d\rangle\) or a reflection-containing subgroup \(H=\langle r^d,r^a s\rangle\), where \(d\mid n\), \(1\leq d\leq n\), and \(0\leq a<d\). The case \(d=n\) in the rotation family denotes the trivial subgroup.

* **Rotation-only:** For \(d=1\), the fixed space is empty. For \(d=2\), it is two points, \(S^0\). For \(d\geq3\), it is PL-homeomorphic to \(|\operatorname{Ind}_2(C_d)|\), whose homotopy type is
  \[
  |X_n|^{\langle r^d\rangle}\simeq
  \begin{cases}
  \bigvee^3 S^{2k-1},&d=4k,\quad k\geq1,\\
  S^{2k-1},&d=4k+1,\quad k\geq1,\\
  S^{2k},&d=4k+2,\quad k\geq1,\\
  S^{2k+1},&d=4k+3,\quad k\geq0.
  \end{cases}
  \]
  The ordinary cycle homotopy types are the established theorem of Deshpande and Singh; the new contribution is the geometric subgroup-fixed classification, including its reduction to smaller cycles.

* **Reflection-containing:** For \(d=1\), the fixed space is empty. For \(d=2\), it is \(S^0\) when \(a\) is even and empty when \(a\) is odd. For \(d\geq3\), put
  \[
  \ell=\begin{cases}
  (d+1)/2,&d\text{ odd},\\
  d/2+1,&d\text{ even and }a\text{ even},\\
  d/2,&d\text{ even and }a\text{ odd}.
  \end{cases}
  \]
  Then \(|X_n|^H\simeq S^{\lfloor\ell/2\rfloor-1}\). More precisely, this fixed space is PL-homeomorphic to an explicitly described \(\ell\)-vertex complex \(F_\ell\) that **simplicially collapses** onto the boundary of a \(\lfloor\ell/2\rfloor\)-dimensional cross-polytope.

In particular, all nonempty reflection-containing subgroup-fixed spaces have the homotopy type of a **single** sphere, including the disconnected sphere \(S^0\); no such subgroup has a multi-sphere wedge fixed space.

## Assumptions and scope
The graph \(C_n\) is the simple cycle of length \(n\geq3\). The two-independence complex \(\operatorname{Ind}_2(G)\) comprises subsets whose induced connected components have at most two vertices. For cycles, this is equivalent to avoiding every cyclic triple of consecutive vertices (also when \(n=3\)). The fixed space is fixed pointwise in the geometric realization; it is not the subcomplex consisting only of individually fixed vertices. Empty fixed spaces mean no nonempty geometric points, even though the abstract empty face exists.

Define \(F_\ell\), for integers \(\ell\geq2\), on vertices \(1,\ldots,\ell\). A face contains neither endpoint pair \(\{1,2\}\) nor \(\{\ell-1,\ell\}\), and no triple \(\{i,i+1,i+2\}\) for \(1\leq i\leq\ell-2\). When \(\ell=2\), the endpoint pairs coincide. Write \(k=\lfloor\ell/2\rfloor\), and let \(K_\ell\) be the subcomplex on vertices \(1,\ldots,2k\) containing at most one from each pair \(P_j=\{2j-1,2j\}\), \(1\leq j\leq k\). Thus \(K_\ell=(S^0)^{*k}\), the boundary of the \(k\)-cross-polytope, with dimension \(k-1\).

## Proof
**1. Fixed points as orbit simplices.** Let a finite group act simplicially on a finite complex \(K\). Every point in \(|K|\) has unique vertex barycentric coordinates. Being group-fixed means these coefficients are constant on every vertex orbit. A nonempty set of such orbits can have positive coefficients simultaneously exactly when the union of their vertices is a face of \(K\). Sending each orbit-vertex to the uniform barycenter of that orbit therefore gives a PL homeomorphism from the *orbit-face complex* onto \(|K|^H\). This handles fixed geometric points lying in interiors of non-fixed simplices.

**2. Rotation reduction.** For \(H=\langle r^d\rangle\), the vertex orbits are residue classes modulo \(d\). Selecting orbit classes gives an allowed face exactly when their union has no cyclic three-run in \(C_n\). For \(d\geq3\), this is equivalent to having no three-run in \(C_d\). If \(d=1\), the unique nonempty orbit fills the entire cycle and is forbidden. If \(d=2\), either parity orbit is permissible but their union is forbidden, yielding two isolated vertices. The ordinary \(d\geq3\) homotopy formula is Theorem 4.6 of Deshpande--Singh, specialized to the parameter \(r=2\) (their auxiliary integer equals four).

**3. Fold reflections.** Suppose \(H=\langle r^d,r^a s\rangle\). First quotient the rotation subgroup to \(\mathbb Z/d\mathbb Z\), then identify vertices exchanged by \(i\mapsto a-i\). If \(d\geq3\), the quotient vertex orbits line up consecutively along an interval. The number of orbits is \(\ell=(d+1)/2\) when \(d\) is odd; when \(d\) is even, a vertex-axis reflection (even \(a\)) has \(d/2+1\) orbits, while an edge-axis reflection (odd \(a\)) has \(d/2\). The cyclic three-runs descend exactly to the ordinary three-run obstructions along that orbit interval, together with the two forbidden end pairs (a doubled endpoint under reflection yields a three-run already from two adjacent orbit choices). Thus the orbit-face complex is exactly \(F_\ell\). When \(d=1,2\), the orbit description gives the small cases separately, as stated.

**4. Explicit relative elementary collapse.** We prove \(F_\ell\searrow K_\ell\) for every \(\ell\geq2\). Fix a face \(\sigma\notin K_\ell\). If it contains a full pair \(P_j\), take the smallest such \(j\); the forbidden first endpoint pair ensures \(j\geq2\). Pair \(\sigma\) with \(\sigma\triangle\{2j-3\}\) (toggle that vertex). Because \(P_j\subseteq\sigma\), the three-run condition forces \(2j-2\notin\sigma\). Consequently either state of \(2j-3\) gives a valid face: a newly completed three-run ending at this vertex, if that triple exists, would require the preceding full pair \(P_{j-2}\) (only relevant when \(j\geq3\)), contradicting minimality of \(j\); the other possible new three-runs require the absent vertex \(2j-2\). The first full pair stays \(j\), and the two faces differ by one vertex. If no pair is full, then necessarily \(\ell=2k+1\) is odd and \(\ell\in\sigma\). The forbidden final endpoint pair forces \(\ell-1\notin\sigma\); pair \(\sigma\) with \(\sigma\triangle\{\ell-2\}\). Again both are faces with the same status (no full pairs and final vertex included): a new forbidden three-run ending at \(\ell-2\), if the triple exists, would require an already-forbidden full preceding pair \(P_{k-1}\) (only relevant when \(k\geq2\)), while any later three-run uses the missing vertex \(\ell-1\). These rules pair every face of \(F_\ell\setminus K_\ell\) exactly once, and never touch \(K_\ell\).

For completeness these pairs can be ordered as **elementary collapses**: process first-full-pair classes in increasing \(j\), followed (when \(\ell\) is odd) by the final-vertex/no-full-pair class. Within each class process paired lower faces in decreasing cardinality. Adding vertices cannot eliminate a full pair or the final vertex, so every proper coface of the lower face either belongs to an already cleared earlier class or, within its own class, belongs to a larger already-cleared pair. Its only remaining coface is therefore its matched partner; hence the lower face is free at its turn. The residual complex is precisely \(K_\ell\). In particular \(F_\ell\simeq K_\ell\cong S^{k-1}\). Combining the steps proves the complete subgroup classification.

## Verification
Run \(\texttt{python3 verify.py}\) with the included standalone Python program. It reconstructs subgroup orbit sets directly in \(C_n\), checks the cyclic and folded orbit-face complexes for all \(3\leq n\leq28\), every divisor \(d\mid n\), and every reflection axis \(0\leq a<d\); performs exact codimension-one relative matching checks for \(2\leq\ell\leq15\), including directed acyclicity tests through \(\ell=12\); and independently calculates mod-two homology for \(2\leq\ell\leq11\). The actual recorded output is included in \(\texttt{verify_output.txt}\). Exhaustive finite checks support but do not replace the unrestricted four-step proof.

## Relationship to prior work
Sawant's 2026 theorem treats vertex decomposability of higher independence complexes of **trees**, not geometric fixed spaces of cycles. Deshpande and Singh's Theorem 4.6 determines the **ordinary** homotopy type of higher independence complexes of cycles, which is the established input to the rotation cases. Neither gives the orbit-fixed complexes or reflection subgroup collapse proved here. Related work determining dihedral **homology characters** for other graph complexes or bounded-independence (robust-clique) spheres does not determine geometric fixed-point spaces of these two-independence complexes. An indexed comparison found no equivalent all-subgroup fixed-space classification, but absence of an indexed result is not proof of global novelty.

## Limitations
This concerns the parameter two, cycles of length at least three, and subgroups of the natural dihedral action. A reflection-fixed space is shown **homotopy equivalent** to a sphere via a simplicial collapse; it is not claimed to be PL-homeomorphic to that sphere before collapse. The cyclic cases rely on a published ordinary homotopy theorem, while the orbit fixed-space reductions and reflection collapse are proved here. No claims are made about higher independence parameters, other automorphism groups, independent certification, or unindexed literature.

## References
1. Rutuja Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150v1, first publicly available 2026-05-24. https://arxiv.org/html/2605.25150v1 . Read abstract, definitions, introduction and main theorem.
2. Priyavrat Deshpande and Anurag Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, Section 4 and Theorem 4.6. https://arxiv.org/html/2001.05448v2 . Read the complete cycle classification and proof.
