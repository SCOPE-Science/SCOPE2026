# All natural dihedral subgroup fixed spaces of cycle discrete-Morse complexes

## Finding
For every integer \(n\ge3\), write \(X_n=\mathfrak M(C_n)\) for the **full ordinary** discrete-Morse complex of the unfilled polygon with \(n\) vertices, and let the natural dihedral group \(D_n\) act through graph automorphisms. This is not the pure, strong, or multipath complex. For an arbitrary subgroup \(H\le D_n\), let \(\langle r^t\rangle=H\cap\langle r\rangle\), where \(t\mid n\). There are two mutually exclusive cases:

- If \(H=\langle r^t\rangle\) is purely rotational, then \(|X_n|^H\) is empty when \(t=1\), consists of four isolated points when \(t=2\), and is **PL-homeomorphic** to \(|X_t|\) when \(t\ge3\).
- If \(H\) contains any reflection, then \(|X_n|^H\) is empty for \(t\le2\), and is **PL-homeomorphic** to the independence complex of the path \(P_{t-2}\) for \(t\ge3\).

Consequently, when \(H\) contains a reflection and \(t\ge3\), the fixed space is contractible if \(t\equiv0\pmod3\), a sphere of dimension \((t-5)/3\) if \(t\equiv2\pmod3\), or a sphere of dimension \((t-4)/3\) if \(t\equiv1\pmod3\). Here \(P_m\) denotes the simple path on \(m\) vertices, and an empty geometric space is distinguished from a contractible nonempty one. For purely rotational \(H\) with \(t\ge3\), the previously established ordinary homotopy formula for \(X_t\) supplies the exact integral wedge decomposition:
\[
 X_t\simeq\begin{cases}
 (S^{2k-1})^{\vee2}\vee(S^{3k-2})^{\vee2},&t=3k,\\
 S^{2k}\vee(S^{3k-1})^{\vee2},&t=3k+1,\\
 S^{2k}\vee(S^{3k})^{\vee2},&t=3k+2.
 \end{cases}
\]
Coincident dimensions are combined. This known nonequivariant formula is used, not claimed as a new result.

## Assumptions and scope
The cycle has distinct vertices \(x_i\) and edges \(e_i=\{x_i,x_{i+1}\}\) for \(i\in\mathbb Z/n\mathbb Z\), and no filled two-simplex. Each incidence \((x_i,e_i)\) is denoted \(w_{2i}\), while \((x_{i+1},e_i)\) is \(w_{2i+1}\). A simplex of \(X_n\) is a set of incidences forming a matching in the Hasse diagram whose reversal produces no closed gradient path. The natural generators act on incidence labels by
\[
 r(w_j)=w_{j+2},\qquad s(w_j)=w_{2n-1-j},
\]
with indices modulo \(2n\). The standard dihedral relation and classification of subgroups show that every \(H\le D_n\) has one of the forms \(\langle r^t\rangle\) or \(\langle r^t,sr^b\rangle\), with \(t\mid n\) and \(0\le b<t\). The group action is the geometric action on the ordinary realization, not merely the action on vertices fixed individually.

## Proof
**1. Incidence-cycle model.** The Hasse diagram of the one-dimensional cycle is the subdivided cycle, with its \(2n\) incidence edges indexed by \(w_j\). Incidence matchings correspond to independent subsets of the cycle graph on these \(2n\) labels. A forbidden closed gradient path can only follow all edges of the underlying polygon in one common direction. Thus the only independent sets that are not gradient-acyclic are the two alternating perfect incidence matchings \(E=\{w_0,w_2,\ldots,w_{2n-2}\}\) and \(O=\{w_1,w_3,\ldots,w_{2n-1}\}\). Deleting precisely those two maximal simplices (retaining their proper faces) gives \(X_n\).

**2. Exact fixed-orbit lemma.** If a finite group acts by simplicial automorphisms on any finite abstract complex, its geometric fixed points are obtained from orbits of vertices whose entire union forms a face. A fixed point has equal barycentric weights on all vertices in each orbit, and the rescaled orbit weights are barycentric coordinates in the new orbit-simplex. These affine formulas have affine inverses on every face and agree on intersections, yielding a canonical PL homeomorphism. Crucially, this construction does not replace geometric fixed points by individually fixed vertices.

**3. Pure rotation case.** For \(H=\langle r^t\rangle\), the vertex orbits are labeled by the residues \(j\in\mathbb Z/(2t)\mathbb Z\). Two selected orbits meet an incompatible pair of incidence labels exactly when their residues are adjacent on the length-\(2t\) cycle. The only extra prohibited orbit sets are the entire even-residue set and the entire odd-residue set, because their complete unions are the two directed cyclic gradients. For \(t\ge3\), this is *exactly* the incidence-cycle model of \(X_t\), a simplicial isomorphism of the orbit model, hence a PL homeomorphism of fixed spaces. When \(t=2\), the cycle on four residues has only four allowed singleton vertices and no allowed pairs, so the fixed space is four points. When \(t=1\), both possible singleton orbit choices give an oriented directed cycle, so there are no fixed points.

**4. Reflection-containing case.** Let \(H=\langle r^t,sr^b\rangle\). On residue labels modulo \(2t\), reflection sends \(j\) to \(-1-j-2b\). Shifting labels by \(b\) conjugates this action to \(j\mapsto 2t-1-j\). The \(t\) resulting orbit candidates are
\[
 Q_i=\{i,2t-1-i\},\qquad 0\le i<t.
\]
Both \(Q_0\) and \(Q_{t-1}\) contain adjacent cycle residues and are inadmissible. Each of \(Q_1,\ldots,Q_{t-2}\) is individually admissible, and two such orbits are incompatible precisely when their indices differ by one. Every remaining orbit includes an even residue and an odd residue, so their unions can never be one of the deleted monochromatic perfect-gradient simplices. Hence the complete orbit-simplex complex is exactly \(\operatorname{Ind}(P_{t-2})\). When \(t\le2\) there are no admissible orbit vertices.

**5. Homotopy classification.** The homotopy type of \(\operatorname{Ind}(P_m)\) is known by path reduction: for \(m=3k\) it is \(S^{k-1}\) (\(k\ge1\)); for \(m=3k+1\) it is contractible; for \(m=3k+2\) it is \(S^k\). Substitute \(m=t-2\) to get the stated cases. For the rotation case, invoke Kozlov's nonequivariant cycle Morse formula as quoted in Chari–Joswig's Theorem 4.2; no new proof or priority is asserted for that formula. The PL quotient identifications above are the claimed classification.

## Verification
A standalone Python 3 verifier, `verify_morse_fixed.py`, independently constructs each incidence assignment as a directed rooted forest, enumerates group orbits directly on the original \(2n\) incidences, and exhaustively compares each invariant orbit subset to the *exact proposed simplicial model* under an explicit orbit-label bijection. It checks 151 dihedral subgroup parameter instances, testing 184,212 orbit subsets. A separate mod-two boundary computation verifies 68 small fixed-complex reduced Betti tables. Sample sizes are \(3\le n\le12\); for computational bounds, full unreflected trivial-action enumerations are restricted to \(n\le8\). These finite checks corroborate rather than prove the infinite-family theorem. Run `python3 verify_morse_fixed.py` from the directory containing the program; the expected success marker is `FULL_CYCLE_MORSE_DIHEDRAL_FIXED_MODELS_PASS`.

## Relationship to prior work
Chari and Joswig (2000 preprint, Theorem 4.2, crediting Kozlov) give the exact **ordinary** cycle Morse homotopy formula invoked here and distinguish full from pure Morse complexes. Their treatment of pure cycle Morse homotopy does not classify natural dihedral-subgroup geometric fixed spaces. Jojić (2011/2012) studies directed-tree complex shellability and confirms the directed-forest framework, but does not provide the stated fixed-orbit identifications. Lin and Scoville (2019) determine the **abstract** automorphism group of the ordinary cycle Morse complex as the automorphism group of the subdivided cycle; a group-isomorphism calculation does not determine subgroup fixed-space homotopy types. The published records *Integral dihedral homology of pure Morse complexes of cycles* and *Uniform integral homology of full strong Morse matching complexes of cycles* concern, respectively, a pure subcomplex and a different strong-filtration complex, so neither implies the present **full ordinary** geometric fixed-space classification. The standard path-independence homotopy result is also explicitly cited rather than claimed.

## Limitations
The statement concerns only the natural dihedral action induced from the original cycle, not every automorphism in the generally larger full abstract automorphism group of \(X_n\). It concerns geometric fixed spaces, not integral homology of orbit quotients or genuine equivariant stable homotopy. Only the PL identifications of fixed spaces and their consequences are new claims; the nonequivariant cycle and path calculations are established literature. Further specialized literature not fully indexed could contain equivalent subgroup calculations. Independent mathematical audit has not been performed.

## References
1. M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1, first posted 2000-11-28, especially Proposition 3.1 and Theorem 4.2, https://arxiv.org/html/math/0011234v1.
2. D. Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475v2, first posted 2011-09-21, https://arxiv.org/html/1109.4475v2.
3. M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907, 2019, https://arxiv.org/abs/1904.10907.
4. J. Jonsson, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), Corollary 6.3, doi:10.1016/j.ejc.2005.04.010, https://doi.org/10.1016/j.ejc.2005.04.010.
5. Published research record, *Integral dihedral homology of pure Morse complexes of cycles*, record `a9ef20f4f6de` (2026), for comparison with the distinct pure complex.
6. Published research record, *Uniform integral homology of full strong Morse matching complexes of cycles*, record `43f58158c288` (2026), for comparison with the distinct strong complex.
