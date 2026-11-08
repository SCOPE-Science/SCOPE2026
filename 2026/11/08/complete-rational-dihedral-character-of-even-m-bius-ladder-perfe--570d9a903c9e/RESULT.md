# Complete rational dihedral character of even Möbius-ladder perfect-matching complexes

## Finding
Let \(n=2k\ge4\), and let \(M_{2n}\) be the Möbius ladder with graph vertices \(\mathbb Z/(2n)\), perimeter edges \(e_i=\{i,i+1\}\), and opposite spokes \(a_j=\{j,j+n\}\). Let \(X_n=\mathcal M_p(M_{2n})\) be the simplicial complex of matchings *extendible to a perfect matching*. The natural dihedral group \(D_{2n}=\langle r,s\mid r^{2n}=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\), \(s(i)=-i\).

By the known nonequivariant homotopy theorem, \(\widetilde H_i(X_n;\mathbb Q)\) vanishes except at degree \(d=k-1\), where \(V_n=\widetilde H_d(X_n;\mathbb Q)\) has dimension two. **The complete dihedral character** \(\chi_n(g)=\operatorname{tr}(g\mid V_n)\), with all subscripts interpreted modulo \(2n\), is
\[
\chi_n(r^{2j})=2(-1)^{(k-1)j},\qquad \chi_n(r^{2j+1})=0,
\]
\[
\chi_n(r^{2j}s)=0,\qquad
\chi_n(r^{2j+1}s)=
\begin{cases}
0,&k\ \text{even},\\
2(-1)^{(k-1)/2},&k\ \text{odd}.
\end{cases}
\]
In the case \(k\) odd, let \(\epsilon=(-1)^{(k-1)/2}\). As a rational \(D_{2n}\)-module, \(V_n\) splits as two one-dimensional characters, specified by \((r,s)=(1,\epsilon)\) and \((-1,-\epsilon)\). For \(k\) even, \(V_n\) is the standard irreducible two-dimensional rational representation of the dihedral quotient in which \(r\) is a quarter-turn and \(s\) a reflection. In both cases the reflection character carries information not recoverable from homology ranks alone. The rotation values were determined previously; the new content is the complete reflection classification, including its residue-class orientation sign.

## Assumptions and scope
All graphs are finite simple graphs and \(k\ge2\). An abstract vertex of \(X_n\) is a graph edge and a face is a graph-edge matching contained in at least one perfect matching. This is not the ordinary matching complex, nor the strong discrete-Morse matching complex. Homology is reduced simplicial homology over \(\mathbb Q\); this is a representation classification, not an equivariant homotopy classification or integral lattice classification.

The only external homotopy input is Agarwal and Basak's theorem for even \(n\):
\[
X_n\simeq S^{k-1}\vee S^{k-1}.
\]
Their Section 4 (first public version, Lemmas 13–15 and Theorem 18) also proves the following **exact face characterization**. Two graph edges are incompatible if they share a graph endpoint, or if they are perimeter edges \(e_i,e_j\) with \(j-i\equiv n-1\) or \(n+1\pmod{2n}\). Every independent set in this incompatibility graph extends to a perfect matching. Its independence complex is therefore *equal as a simplicial complex* to \(X_n\), not just homotopy equivalent. The two extra forbidden perimeter differences are the minimal nonextendible matchings in even width. This exact characterization is indispensable in the fixed-orbit enumeration.

## Proof
**1. A signed orbit reduction.** For a symmetry \(g\) of the graph, permute the \(3n\) graph edges. An invariant simplex of \(X_n\) is a union of orbits of this permutation. Discard every orbit containing a pair of incompatible edges, and make an auxiliary graph \(Q_g\) whose remaining vertices are edge-orbits, with adjacency when any member of one orbit is incompatible with a member of the other. Thus invariant simplices are precisely independent subsets of \(Q_g\). Define \(I(Q_g;z)=\sum_{S\text{ independent}}z^{|S|}\). A fixed nonempty simplex consisting of \(o\) edge-orbits and \(q\) graph edges contributes \((-1)^{q-1}(-1)^{q-o}=(-1)^{o-1}\) to the reduced simplicial Lefschetz trace. The empty simplex contributes \(-1\). Hence
\[
\widetilde L(g;X_n)=-I(Q_g;-1),\qquad
\chi_n(g)=(-1)^{k}I(Q_g;-1).
\]
Here the second identity uses concentration in degree \(d=k-1\). This argument includes the orientation sign: merely counting fixed faces would be incorrect.

**2. A reflection through vertices.** For \(s(i)=-i\), the spoke \(a_0=\{0,n\}\) is a fixed edge-orbit. Every perimeter edge incident to \(0\) or \(n\) lies in one of the two orbits \(\{e_0,e_{2n-1}\}\) and \(\{e_{n-1},e_n\}\). Each of these orbits is discarded because its edges share a vertex. No other spoke conflicts with \(a_0\), and no retained perimeter orbit meets its endpoints. Consequently the vertex of \(Q_s\) corresponding to \(a_0\) is isolated. Pairing independent sets by toggling this vertex yields \(I(Q_s;-1)=0\). Therefore \(\chi_n(s)=0\).

**3. A reflection through edges.** Consider \(t=rs\), so \(t(i)=1-i\), which sends \(e_i\) to \(e_{-i}\). The retained perimeter orbits are \(E_0=\{e_0\}\), \(E_n=\{e_n\}\), and \(E_i=\{e_i,e_{2n-i}\}\) for \(1\le i<n\). The spoke orbits are \(A_j=\{a_{j+1},a_{-j}\}\), for \(0\le j<k\), with spoke indices modulo \(n\).

The perimeter incompatibility relation is invariant under shifting an edge index by \(n\): each \(e_i\) has exactly the same incompatible perimeter and spoke edges as \(e_{i+n}\), and those two edges are mutually compatible. It follows that, in \(Q_t\), the vertices \(E_i,E_{n-i}\) are **nonadjacent false twins with identical open neighborhoods** for \(0\le i<k\). For such false twins \(u,v\), independent-set deletion at \(v\) gives
\[
I(G;z)=I(G-v;z)+zI(G-N[v];z).
\]
The vertex \(u\) is isolated in \(G-N[v]\), so \(I(G-N[v];-1)=0\). Therefore deleting \(v\) does not change \(I(G;-1)\). Delete \(E_n\) and all \(E_{n-i}\) for \(1\le i<k\). The remaining \(2k+1\) vertices are rim vertices \(p_i=E_i\) for \(0\le i\le k\), and tips \(b_j=A_j\) for \(0\le j<k\). Their **entire** edge set is
\[
\{p_ip_{i+1},\ p_ib_i,\ p_{i+1}b_i:0\le i<k\}.
\]
Thus the auxiliary graph reduces at \(z=-1\) to a path of \(k\) triangles sharing consecutive vertices (without tip-tip edges).

To evaluate its independence polynomial at \(-1\), first choose an independent subset \(S\) of the rim path. A tip \(b_i\) can independently be included or excluded exactly when neither endpoint \(p_i,p_{i+1}\) is in \(S\); at \(-1\), the choices cancel. Nonzero contributions require **every** rim edge to have one endpoint in \(S\). There are exactly two such independent vertex covers: the alternating even and odd rim vertices. Their weights are
\[
I(Q_t;-1)=(-1)^{\lceil(k+1)/2\rceil}+(-1)^{\lfloor(k+1)/2\rfloor}
=\begin{cases}0,&k\ \text{even},\\2(-1)^{(k+1)/2},&k\ \text{odd}.\end{cases}
\]
Multiplication by \((-1)^k\) from Step 1 yields \(\chi_n(rs)=0\) for even \(k\) and \(2(-1)^{(k-1)/2}\) for odd \(k\).

**4. Rotations and all other reflections.** A one-step rotation \(r\) has just two invariant faces: the empty simplex and the full spoke matching. Its reduced Lefschetz trace is zero. For \(r^2\), the complete invariant-face list is the empty face, the two half-spoke sets, their union, and the two alternating perimeter perfect matchings. Their signed contributions give reduced Lefschetz number two. Thus \(\operatorname{tr}(r\mid V_n)=0\), \(\operatorname{tr}(r^2\mid V_n)=2(-1)^{k-1}\). The operator \(r^2\) has finite order and dimension two; its eigenvalues are roots of unity with sum \(\pm2\), so both eigenvalues equal \((-1)^{k-1}\). Therefore
\[
(r^2)_*=(-1)^{k-1}\operatorname{id}_{V_n}.
\]
This rotation computation is also explicitly known from the earlier published cyclic-character result. It implies the displayed character on all rotations. Since \(r^{2j}\) acts as the scalar \((-1)^{(k-1)j}\), every reflection \(r^{2j}s\) has trace a scalar multiple of \(\chi_n(s)=0\), and every \(r^{2j+1}s\) is a scalar multiple of \(rs\). In the latter class the scalar is \(1\) whenever the \(rs\)-trace is nonzero (because then \(k\) is odd). Hence the complete formulas follow.

**5. Representations.** If \(k\) is odd, \(r^2=1\), and \(r\) has two eigenlines with eigenvalues \(1,-1\). The relation \(srs=r^{-1}=r\) on these lines shows that \(s\) preserves them. Its trace zero and the trace \(2\epsilon\) of \(rs\) force the eigenvalues \((\epsilon,-\epsilon)\). If \(k\) is even, the two-dimensional rational module has \(r^2=-1\) and \(srs=r^{-1}\), identifying the rational standard dihedral two-dimensional representation. No integral-module conclusion is needed.

## Verification
Run `python3 verify.py` using only the Python 3 standard library. The script constructs the graph and **every perfect matching** recursively for even \(n=4,6,8,10,12,14\). For \(n=4,6,8,10\), it also exhaustively forms the entire simplicial face set from perfect matchings and independently enumerates all independent sets of the incompatibility graph, confirming equality of those two face sets. It calculates the signed reduced simplicial Lefschetz trace directly on faces for every group element, not using the proof's orbit recurrence. It separately constructs orbit graphs for all tested widths, checks their false twins and triangle-chain residue, and verifies \(s\), \(rs\), \(r\) and \(r^2\) traces. The largest exhaustively tested face set has \(59{,}050\) simplices (including the empty simplex), with \(123\) generating perfect matchings. The observed \(rs\) traces at widths \(n=4,6,8,10,12,14\) are \(0,-2,0,2,0,-2\), agreeing with the theorem. Execution ends with `ALL_VERIFY_OK`; the recorded output is in `verify_output.txt`. All computations are finite cross-checks, not the reason the theorem holds for every \(k\).

## Relationship to prior work
Agarwal and Basak determine the nonequivariant homotopy type, the exact forbidden-pair description, and an even-width sphere multiplicity of two. Neither the sphere ranks nor their proof identifies both reflection actions. Earlier published calculations separately determine the **one-step rotation**, the central half-turn, and the full dihedral module in **odd** width. Their statements do not determine \(\chi_n(rs)\) for even \(n\), and the orientation sign at \(n\equiv2\pmod4\) is not implied by the rotational character. The present proof completes the even-width rational dihedral character without re-claiming those older ingredients as new. A similar published representation result for circular ladders studies their *independence* complexes, not this perfect-matching complex. Searches for reflection characters, equivalent signed fixed-simplex formulas, and full symmetry modules did not reveal a dominating theorem; absence from a search index is not a uniqueness proof.

## Limitations
This is a rational representation theorem for even \(n\ge4\). It does not claim an integral \(\mathbb Z[D_{2n}]\)-lattice splitting, equivariant CW or homotopy type, an all-width result for odd \(n\), or a new nonequivariant classification. The source's initial public version was inspected in full for the mathematical statements used, while its later expanded revision was available only at abstract level; possible unindexed or inaccessible equivalent work remains an originality risk. Independent validation has not been performed.

## References
1. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601v1 (first public 2026-08-31), §4, Lemmas 13–15 and Theorem 18; expanded v2 dated 2026-09-14. https://arxiv.org/abs/2608.30601
2. *Rotation has order two or four on Möbius-ladder perfect-matching homology*, published mathematical finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rotation-has-order-two-or-four-on-m-bius-ladder-perfect-matching--3551187dd347
3. *The antipodal half-turn representation on Möbius-ladder perfect-matching homology*, published mathematical finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-antipodal-half-turn-representation-on-m-bius-ladder-perfect--317e26dcb314
4. *Complete dihedral rational homology representations of odd Möbius-ladder perfect-matching complexes*, published mathematical finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-dihedral-rational-homology-representations-of-odd-m-biu--d5bba5f21863
