# Reflection-fixed homotopy types of higher path-independence complexes

## Finding

Let \(P_n\) be the path on vertices \(1,\ldots,n\), let \(\tau(i)=n+1-i\), and let \(\operatorname{Ind}_r(P_n)\) be the simplicial complex consisting of vertex subsets whose induced connected components have at most \(r\) vertices. The following formulas determine the **geometric** fixed-point space of reflection, with its integral homotopy type, for every integer \(n\geq1\) and \(r\geq1\).

**Even paths.** If \(n=2m\) with \(m\geq1\), set \(s=\lfloor r/2\rfloor\) and write \(m=a(r+2)+b\), where \(a\geq0\) and \(0\leq b\leq r+1\). Then
\[
|\operatorname{Ind}_r(P_{2m})|^{\tau}\simeq
\begin{cases}
S^{ar-1},&b=0,\\
S^{ar+s-1},&b=s+1,\\
\mathrm{point},&\text{otherwise}.
\end{cases}
\]

**Odd paths.** If \(n=2m+1\) with \(m\geq0\), set \(t=\lfloor(r-1)/2\rfloor\) and again write \(m=a(r+2)+b\). Then
\[
|\operatorname{Ind}_r(P_{2m+1})|^{\tau}\simeq
\begin{cases}
S^{ar+t},&b=t+1,\\
S^{ar+r-1},&b=r+1,\\
\mathrm{point},&\text{otherwise}.
\end{cases}
\]
Here \(\mathrm{point}\) denotes a contractible space. The unique occurrence of \(S^{-1}\), at \((n,r)=(2,1)\), means the empty geometric fixed-point space. A sphere \(S^0\) means two points, not a connected space.

## Assumptions and scope

All simplicial complexes are finite. A face of \(\operatorname{Ind}_r(P_n)\) has no consecutive run of occupied path vertices longer than \(r\). Geometric fixed points mean fixed points of the induced affine action on the geometric realization, not the realization of the subcomplex of individually fixed vertices. The reflection is the specified reversal, with no additional subgroup or graph action.

For integers \(m\geq0\), \(r\geq1\), and \(0\leq s\leq r\), define the **terminal-run complex** \(K(m;r,s)\) on positions \(1,\ldots,m\) by requiring each consecutive occupied run to have length at most \(r\) and the occupied terminal run ending at \(m\) to have length at most \(s\). The empty terminal run has length zero. The complex on zero vertices is \(\{\varnothing\}\), with empty geometric realization.

## Proof

**1. Exact geometric fixed model.** The reflection partitions the vertices of \(P_n\) into two-element orbits \(\{i,n+1-i\}\), one for each \(i\leq\lfloor n/2\rfloor\), and for odd \(n\) a single central singleton orbit. A point in the fixed realization has equal barycentric weights at the vertices of each orbit; its support is a union of complete orbits and is a face. The orbit barycenters therefore identify the fixed space *homeomorphically* with the realization of the complex on admissible orbits.

For \(n=2m\), selecting a set of paired orbits produces mirrored runs. A run reaching the central seam is doubled; it is admissible exactly if it has length at most \(s=\lfloor r/2\rfloor\). All other runs have length at most \(r\). Thus the orbit complex is exactly \(K(m;r,s)\).

For \(n=2m+1\), let \(c\) denote the central singleton orbit. With \(c\) absent, all paired-orbit runs have bound \(r\). With \(c\) present, a run of \(\ell\) pairs touching the center has \(2\ell+1\) original vertices and hence \(\ell\leq t=\lfloor(r-1)/2\rfloor\). Accordingly the orbit complex is
\[
Y(m;r,t)=K(m;r,r)\ \cup\ (c*K(m;r,t)),
\]
where \(c*\) denotes the simplicial cone on an additional vertex.

**2. Uniform acyclic reduction.** We give an explicit *augmented* face-poset matching, including the empty face. It applies to either \(K(m;r,s)\) for the fixed terminal bound or \(Y(m;r,t)\). When \(m\geq r+2\), pair every admissible face that omits position \(1\) with the face obtained by adjoining position \(1\), if that adjunction is admissible. No faces containing \(1\) remain. An unpaired face must omit \(1\), contain every position \(2,\ldots,r+1\), and omit position \(r+2\). The last assertion follows because adjoining \(1\) fails precisely when all the next \(r\) positions occur, in which case the next position must be absent. The remaining selected positions, strictly to the right of \(r+2\), form precisely the same terminal-run complex on \(m-r-2\) positions, or the same odd-center model \(Y\) on that many paired positions. The correspondence preserves inclusion. Apply the same matching recursively to this residual set, adjoining the forced \(r\) selected positions to each lifted face.

This matching is acyclic, not merely cardinality-perfect. Indeed, the initially matched faces are a downward-closed region \(A\) of the face poset: faces with position \(1\) present or with its addition allowed. Every cover crossing between \(A\) and its complement is directed **from the complement into \(A\)** in the reversed-unmatched / forward-matched Hasse orientation. There is therefore no directed cycle using both regions. The pairs in \(A\) all toggle the same coordinate \(1\), hence are acyclic; the residual region inherits the inductively acyclic matching. The argument works even for the empty face and the central singleton \(c\). At each reduction step, a critical face, if any, gains exactly \(r\) vertices, so its dimension increases by \(r\).

**3. Base cases when \(0\leq m\leq r+1\).** For \(K(m;r,s)\): when \(m=0\), the only augmented face is \(\varnothing\), the \((-1)\)-sphere; when \(m=s+1\geq1\), the complex is the boundary of the simplex on \(m\) vertices and has one unmatched augmented face of dimension \(s-1\). At other positive \(m\leq r+1\), it is a simplex if \(m\leq s\), or is a cone on the first position if \(m>s+1\); in both cases the augmented matching has no critical face.

For \(Y(m;r,t)\), the case \(m=0\) is a point, so no critical augmented face. If \(m=t+1\), the complex is the boundary of the simplex on the \(m\) paired positions and \(c\), giving one critical face of dimension \(t\). If \(m=r+1\), the subcomplex with \(c\) absent is the boundary of the simplex on its \(m\) paired positions. The \(c\)-containing faces can all be matched by toggling the first position: the bound \(t<r\) on a terminal run precludes the only possible obstruction. The remaining boundary then has one critical face of dimension \(r-1\). For \(0<m\leq t\), the central vertex is a cone apex. Finally, for \(t+1<m<r+1\), first pair all \(c\)-containing faces by toggling position \(1\) (again the terminal bound prevents obstruction); the residual complex without \(c\) is the full simplex on \(m\) vertices, paired by the same toggle. These matchings are acyclic by the same downward-closed-region argument. This list exhausts the bases.

**4. Recovering the homotopy types.** Write \(m=a(r+2)+b\) with \(0\leq b\leq r+1\). After \(a\) recursive reductions, the residual is one of the base cases, and each surviving critical face gains \(ar\) vertices. The even bases occur at \(b=0\) (dimension \(-1\)) or \(b=s+1\) (dimension \(s-1\)); the odd bases occur at \(b=t+1\) (dimension \(t\)) or \(b=r+1\) (dimension \(r-1\)). All other cases have no critical augmented faces. The acyclic matching theorem, equivalently the elementary collapse/Morse CW construction with the empty face paired when possible, yields a sphere in exactly the dimension of its sole critical face, or a contractible complex when there is none. This proves both formulas integrally, including their zero-dimensional and empty-space endpoints.

## Verification

The standalone file `verification/reflection_path_verifier.py` exhaustively constructs the original reflected vertex-orbit face sets from all subsets of orbits for every \(2\leq n\leq22\) and \(1\leq r\leq9\) (189 cases). It compares every face with the exact terminal-run model, constructs the recursive pairs, checks that every augmented face is matched once or has the stated critical status, and topologically sorts the **complete oriented Hasse diagram** in every instance. All tests passed, totaling 254,981 covering relations. These finite tests do not prove the infinite theorem; the unrestricted argument above does.

Reproduce from the supplied standalone files with `python3 verification/reflection_path_verifier.py`. The actual captured standard output is `verification/verification_output.txt`.

## Relationship to prior work

Sawant [1, Theorem 3.6, p. 15] proves vertex decomposability of ordinary \(r\)-independence complexes of all trees, without deriving fixed-point spaces under reversal. Deshpande and Singh [2, §4] determine ordinary path \(r\)-independence homotopy via the perfect matching of Paolini–Salvetti, not the reflection orbit complexes. Ehrenborg and Hetyei [3, Theorem 4.4, pp. 912–913] prove **the broad qualitative result** that the independence complex of *any* interval family is contractible or sphere-like. Our orbit complexes belong to that pre-existing qualitative class; this is not claimed as new. The specific contribution is the simultaneous, parameter-explicit reflected-path formulas (both path parities), including the exact sphere dimension, vanishing residue classes, and the exceptional empty case, with a single recursive matching proving them. Their general theorem does not state those numerical formulas. Independent later equivalences may exist.

## Limitations

Only the order-two reflection of finite paths and the indicated \(r\)-independence condition are classified. This is not an equivariant equivalence of the ambient complexes, does not specify fixed-point inclusion maps, and does not imply a similar periodic classification for trees with branching. General interval-hypergraph sphere-or-point existence was known already [3]. The overlap search cannot rule out unindexed special-case classifications; no independent audit has been performed.

## References

[1] R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (first posted 2026-05-24), especially Theorem 3.6. https://arxiv.org/abs/2605.25150

[2] P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448v2 (2021), §4. https://arxiv.org/abs/2001.05448

[3] R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics **27** (2006), 906–923; Theorem 4.4, pp. 912–913. DOI: 10.1016/j.ejc.2005.04.010. Author-hosted full text: https://www.ms.uky.edu/~jrge/Papers/Independence.pdf
