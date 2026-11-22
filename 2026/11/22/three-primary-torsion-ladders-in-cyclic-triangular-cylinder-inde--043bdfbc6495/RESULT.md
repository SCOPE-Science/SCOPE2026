# Three-primary torsion ladders in cyclic triangular-cylinder independence quotients

## Finding
For every integer \(m\ge4\), let \(G_m=P_m\square C_3\), let \(X_m=\operatorname{Ind}(G_m)\), and let \(Y_m=|X_m|/C_3\), where \(C_3\) simultaneously rotates the three vertices in every triangular layer. Define
\[
d_m=\begin{cases}
2k-1,&m=3k,\\
2k,&m=3k+1,\\
2k+1,&m=3k+2.
\end{cases}
\]
Here \(k=\lfloor m/3
floor\). Then the **complete integral homology classification** of the ordinary geometric quotient is
\[
H_i(Y_m;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/3\mathbb Z,&i\text{ odd and }1\le i<d_m,\\
\mathbb Z,&i=d_m\text{ and }m\not\equiv1\pmod{3},\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, higher odd-degree torsion occurs at every odd dimension below \(d_m\), even though the covering independence complex has torsion-free integral homology. For \(m\equiv1\pmod{3}\), the quotient has no positive-degree rational homology, whereas for the other two residue classes it has the integral homology groups of an odd-dimensional lens space. This is a **homology** statement, not a homeomorphism or homotopy equivalence to a lens space.

## Assumptions and scope
The vertices of \(G_m\) are \((r,c)\), with \(1\le r\le m\) and \(c\in\mathbb Z/3\mathbb Z\). Edges join distinct colors in the same layer and the same color in successive layers. The independence complex \(X_m\) consists of all vertex subsets containing no graph edge, including the empty face. The generator \(g\) acts as \(g(r,c)=(r,c+1)\); its realization acts simplicially. The quotient \(Y_m\) is the actual geometric orbit space, not a quotient of the vertex set and not a complex of invariant faces.

The graph \(C_3\) is the three-vertex complete graph. Therefore this notation coincides with the triangular-cylinder graph \(C_{m,3}\) in the original cylinder literature. The integer \(d_m\) is at least two for \(m\ge4\).

## Proof

**Step 1: free action and known covering homotopy.** Each simplex contains at most one vertex in any given layer. A nontrivial color rotation cyclically permutes three vertices in every layer, so a nonempty simplex cannot be invariant under it. If a point of \(|X_m|\) were fixed by the rotation, its unique positive barycentric support would be an invariant nonempty simplex. Hence the action is free. The quotient is a finite CW space, and the Borel construction \(EC_3\times_{C_3}X_m\) maps by a homotopy equivalence to \(Y_m\).

Thapper's Proposition 3.2 (see References) determines the **already known** nonequivariant homotopy types:
\[
|X_m|\simeq
\begin{cases}
S^{2k-1},&m=3k,\\
S^{2k}\vee S^{2k},&m=3k+1,\\
S^{2k+1},&m=3k+2.
\end{cases}
\]
Thus \(|X_m|\) is simply connected for \(m\ge4\). The quotient is a regular threefold covering and therefore has \(\pi_1(Y_m)\cong C_3\). This fundamental-group fact was previously determined for the broader \(P_m\square K_q\) family and is recalled only to specify the topology; the new classification concerns every higher integral homology group.

**Step 2: the two-row spectral sequence.** Write \(d=d_m\). The integral cohomology Serre spectral sequence of the Borel fibration is
\[
E_2^{p,q}=H^p(C_3;H^q(X_m;\mathbb Z))\Longrightarrow H^{p+q}(Y_m;\mathbb Z).
\]
It has only the rows \(q=0,d\), with the bottom row \(H^*(BC_3;\mathbb Z)=\mathbb Z[u]/(3u)\), where \(|u|=2\). The only potentially nonzero differential is \(d_{d+1}\), and the spectral sequence is a module over the bottom-row ring. Since \(Y_m\) is finite-dimensional, \(H^j(Y_m;\mathbb Z)=0\) for all sufficiently large \(j\). This forces a nonzero transgression wherever infinitely many powers of \(u\) would otherwise survive.

**Step 3: the odd-sphere cases.** When \(m\equiv0,2\pmod{3}\), \(d\) is odd and \(H^d(X_m;\mathbb Z)\cong\mathbb Z\). The order-three action on this rank-one group is trivial, because \(\operatorname{Aut}(\mathbb Z)\cong\{\pm1\}\). Both rows are consequently copies of \(\mathbb Z[u]/(3u)\). For a generator \(z\in E_2^{0,d}\cong\mathbb Z\), the only possible transgression is
\[
d_{d+1}(z)=a u^{(d+1)/2},\qquad a\in\mathbb Z/3\mathbb Z.
\]
If \(a=0\), multiplication by \(u\) forces all sufficiently high even-degree bottom-row classes to survive, contradicting the finite dimension of \(Y_m\). Hence \(a\) is nonzero and therefore a unit modulo three. All positive-even-degree source classes in the top row map isomorphically to the corresponding targets; the kernel in bidegree \((0,d)\) is \(3\mathbb Z\). It follows, with no additive-extension ambiguity, that \(H^0(Y_m;\mathbb Z)=\mathbb Z\), \(H^{2j}(Y_m;\mathbb Z)=\mathbb Z/3\mathbb Z\) for \(1\le j\le(d-1)/2\), \(H^d(Y_m;\mathbb Z)=\mathbb Z\), and all other positive cohomology groups vanish.

**Step 4: the two-even-sphere cases.** When \(m=3k+1\), \(d=2k\) is even and \(M=H^d(X_m;\mathbb Z)\cong\mathbb Z^2\). The action of \(g\) on \(|X_m|\) is fixed-point-free; the Lefschetz number therefore vanishes. Since the only nonzero rational homology groups are in degrees zero and the even degree \(d\), the trace of \(g\) on \(M\otimes\mathbb Q\) is \(-1\). Together with \(g^3=1\), this forces characteristic polynomial \(t^2+t+1\). Therefore the norm \(1+g+g^2\) vanishes integrally on \(M\), \(M^{C_3}=0\), and \(|\det(g-1)|=3\).

The standard periodic resolution for the cyclic group now gives
\[
H^p(C_3;M)\cong
\begin{cases}
\mathbb Z/3\mathbb Z,&p\ge1\text{ odd},\\
0,&p=0\text{ or }p\ge2\text{ even}.
\end{cases}
\]
The possible differential \(d_{d+1}\colon E_{d+1}^{1,d}\to E_{d+1}^{d+2,0}\) is between two copies of \(\mathbb Z/3\mathbb Z\). It must be nonzero: otherwise, by the period-two action of \(u\), infinitely many even-degree bottom-row classes would survive. It is therefore an isomorphism, and \(u\)-linearity makes the analogous differential an isomorphism for every odd \(p\ge1\). Thus the only nonzero integral cohomology groups are \(H^0(Y_m;\mathbb Z)=\mathbb Z\) and \(H^{2j}(Y_m;\mathbb Z)=\mathbb Z/3\mathbb Z\) for \(1\le j\le d/2\). Again, each total degree has only one surviving filtration summand, so no additive extension is left.

**Step 5: integral homology.** The integral homology groups are finitely generated because \(Y_m\) is finite. Applying the integral universal coefficient theorem in each degree to the two explicit cohomology descriptions gives precisely the formula in the Finding section. In particular, no higher powers of three and no torsion at other primes occur. This concludes the unrestricted proof.

## Verification
The accompanying `CHECKER.py` constructs all independent sets for each \(m=4,5,6,7,8,9\), checks that every nonempty simplex orbit has three members, and computes the signed integral simplicial quotient boundary. It checks \(\partial^2=0\) before reducing the matrices modulo \(2\), \(3\), and \(5\). Every resulting field Betti vector agrees with the universal-coefficient predictions from the claimed integral homology, including the mod-three Tor classes one degree above each integral torsion class. The output is in `VERIFICATION_OUTPUT.txt`. The arithmetic is exact; the finite sweep is corroboration, not a replacement for the preceding proof of the infinite family or for exact integral Smith forms.

## Relationship to prior work
Thapper's Proposition 3.2, published as a preprint in December 2008, already classifies the **nonequivariant** homotopy types of \(\operatorname{Ind}(P_m\square C_3)\) and is an explicit input, not a claimed new result. Chakraborty's November 13, 2026 preprint studies Cohen–Macaulay and Buchsbaum properties of these independence complexes, but not the ordinary cyclic-color quotient or its integral higher homology. A prior determination of \(\pi_1\) for cyclic color quotients of \(\operatorname{Ind}(P_m\square K_q)\) includes the group \(C_3\) here; the first homology is therefore **not** claimed as new. The new contribution is the exact unbounded ladder of higher order-three torsion and the complete integral homology classification, including the sharp congruence dichotomy for top free homology. General orbit-space spectral-sequence literature develops related methods for other types of sphere wedges, but no inspected result supplies this particular all-length integral classification.

## Limitations
The result applies to the simultaneous threefold **color rotation** on triangular cylinders with \(m\ge4\), not to rotations along the path, to the full color-permutation group, or to general \(P_m\square C_q\). It determines integral homology, not a cellwise homotopy decomposition, multiplicative cohomology ring, Postnikov invariants, smooth structure, or lens-space homeomorphism. The argument uses the published nonequivariant homotopy theorem and standard group-cohomology/Serre spectral-sequence facts. Source indexing may miss equivalent literature, and independent mathematical validation has not been performed.

## References
- Bidwan Chakraborty, *Cohen–Macaulayness and Buchsbaumness of Cartesian Products of Paths and Cycles*, arXiv:2611.18495v1, initially posted 13 November 2026, https://arxiv.org/html/2611.18495v1.
- Johan Thapper, *Independence Complexes of Cylinders Constructed from Square and Hexagonal Grid Graphs*, arXiv:0812.1165v1, initially posted 5 December 2008, Proposition 3.2, https://arxiv.org/pdf/0812.1165.
- Dimpi and Hemant Kumar Singh, *Fixed Point Sets and Orbit Spaces of Wedge of Three Spheres*, arXiv:2303.16484v1, initially posted 29 March 2023; methodological comparison involving spectral sequences and different sphere-wedge hypotheses, https://arxiv.org/pdf/2303.16484.
