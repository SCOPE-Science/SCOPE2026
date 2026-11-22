# Spoke–rim edge-fault dichotomy for induced-forest complexes of wheels

## Finding

For every integer \(n\ge5\), let \(W_{n+1}\) have rim vertices \(0,1,\ldots,n-1\) in cycle order and hub \(h\), adjacent to every rim vertex. Let \(G_n^{\mathrm s}=W_{n+1}-h0\) (one spoke deleted) and \(G_n^{\mathrm r}=W_{n+1}-0(n-1)\) (one rim edge deleted). Define \(\mathcal F(G)\) to be the abstract simplicial complex of vertex subsets inducing acyclic subgraphs of \(G\), including the empty face.

Then, integrally and as homotopy types,

\[
\mathcal F(G_n^{\mathrm s})\simeq S^{n-2}\vee Y_n,\qquad
Y_n=\begin{cases}
\ast,&n\equiv0\pmod3,\\
S^{(n+2)/3},&n\equiv1\pmod3,\\
S^{(n+1)/3},&n\equiv2\pmod3,
\end{cases}
\]

and

\[
\mathcal F(G_n^{\mathrm r})\simeq\begin{cases}
S^{n/3},&n\equiv0\pmod3,\\
\ast,&n\equiv1\pmod3,\\
S^{(n+1)/3},&n\equiv2\pmod3.
\end{cases}
\]

Here \(\ast\) means a contractible space, so a wedge with \(\ast\) contributes no extra sphere. All reduced integral homology groups are free. The spoke-fault complex always retains a primitive top class in degree \(n-2\); the rim-fault complex has no class in that degree. Since the wheel's dihedral symmetries are transitive on each of its two types of edges, these formulae classify *every* single-edge deletion up to graph isomorphism.

For example, with five rim vertices the spoke fault gives \(S^3\vee S^2\), whereas the rim fault gives \(S^2\); with six rim vertices they give \(S^4\) and \(S^2\); with seven rim vertices they give \(S^5\vee S^3\) and a contractible complex.

## Assumptions and scope

All graphs are simple, finite and undirected. The graph complex uses **vertex-induced** forests, not forests of selected graph edges, not the matching complex, and not a cut complex. There is no restriction on maximum induced degree. The homotopy types are non-equivariant and do not claim a canonical equivalence compatible with edge deletion. The range \(n\ge5\) is part of the theorem.

Write \(I(P_m)\) for the independence complex of the path on \(m\) vertices. The elementary path recurrence is

\[
I(P_m)\simeq\Sigma I(P_{m-3})\quad(m\ge3),
\]

using the standard unreduced suspension in the vertex-deletion pushout. The initial types are \(I(P_1)\simeq\ast\), \(I(P_2)\simeq S^0\), \(I(P_3)\simeq S^0\). Hence for every positive \(m\), \(I(P_m)\) is contractible if \(m\equiv1\pmod3\), and otherwise has type \(S^{\lfloor (m-1)/3\rfloor}\) for \(m\equiv0\pmod3\) or \(S^{\lfloor m/3\rfloor}\) for \(m\equiv2\pmod3\). The case \(m=0\) is handled explicitly below rather than by an empty-realization convention.

## Proof

**Path recurrence.** For \(m\ge3\), take the penultimate vertex \(u=m-1\) of \(P_m\). Its deletion complex is \(I(P_{m-2})\ast\{m\}\), a cone. Its link is \(I(P_{m-3})\), because deleting \(u\) and its two neighbors leaves the first \(m-3\) path vertices. Writing the entire independence complex as the union of the deletion complex and the cone on the link proves \(I(P_m)\simeq\Sigma I(P_{m-3})\). The three initial cases give the claimed periodic classification.

**Rim-edge fault.** The rim vertices of \(G_n^{\mathrm r}\) induce the path \(P_n\), so every rim subset is a face and the hub-free subcomplex is the full simplex \(\Delta^{n-1}\). A face containing the hub is a forest precisely when its rim vertices are independent in \(P_n\): any selected adjacent pair completes a triangle through the hub, and without a selected adjacent pair the induced graph is a star plus isolated vertices. Therefore

\[
\mathcal F(G_n^{\mathrm r})=\Delta^{n-1}\cup_{I(P_n)}(h\ast I(P_n)).
\]

Both pieces are contractible, with the displayed intersection a simplicial subcomplex, so the homotopy pushout is \(\Sigma I(P_n)\). Applying the path recurrence yields the rim-edge formula, including the contractible congruence class.

**Spoke fault and its hub link.** The entire rim is still a cycle, so the hub-free complex is \(\partial\Delta^{n-1}\cong S^{n-2}\). Let \(I=I(P_{n-1})\) for the path on rim vertices \(1,\ldots,n-1\). Let \(A\subset I\) be the subcomplex of independent sets that do not contain both endpoints \(1\) and \(n-1\). For a face containing the hub, the selected vertices among \(1,\ldots,n-1\) must be independent: adjacent selected vertices with the hub make a triangle. If \(0\) is selected, selecting both \(1\) and \(n-1\) makes the four-cycle \(h,1,0,n-1,h\). These are the only possible cycles, since all other selected rim edges are incident to \(0\). Thus the hub link is exactly

\[
L=I\cup_A(0\ast A).
\]

This is the homotopy cofiber of \(A\hookrightarrow I\). For \(n\ge6\), the faces of \(I\) containing both endpoints have precisely their remaining vertices in the middle path \(P_{n-5}\), on vertices \(3,\ldots,n-3\). Writing \(K=I(P_{n-5})\) and \(E=\{1,n-1\}\), we have

\[
I=A\cup(\Delta^E\ast K),\qquad
A\cap(\Delta^E\ast K)=\partial\Delta^E\ast K.
\]

Because the simplicial inclusion \(A\hookrightarrow I\) is a cofibration, its homotopy cofiber is \(I/A\). The quotient \((\Delta^E\ast K)/(\partial\Delta^E\ast K)\) is the double suspension of \(K\), up to homotopy, giving

\[
L\simeq\Sigma^2I(P_{n-5})\qquad(n\ge6).
\]

For \(n=5\), \(I(P_4)\) is a three-edge path and \(A\) is its two disjoint end edges; coning off \(A\) creates one circle. Hence \(L\simeq S^1\) when \(n=5\), consistently with the direct quotient \(\Delta^1/\partial\Delta^1\cong S^1\).

The hub-free subcomplex and the hub star now give

\[
\mathcal F(G_n^{\mathrm s})=\partial\Delta^{n-1}\cup_L(h\ast L).
\]

Every face of \(L\) has at most \(\lceil(n-1)/2\rceil+1\) vertices, so \(\dim L\le\lceil(n-1)/2\rceil\le n-3\) for \(n\ge5\). The sphere \(S^{n-2}\) is \((n-3)\)-connected; consequently the attaching inclusion \(L\hookrightarrow S^{n-2}\) is null-homotopic. Since \(L\) is connected (the cone on \(A\) joins every vertex of \(I\)), the homotopy cofiber splits as

\[
\mathcal F(G_n^{\mathrm s})\simeq S^{n-2}\vee\Sigma L.
\]

For \(n=5\) this is \(S^3\vee S^2\). For \(n\ge6\), substitute \(\Sigma L\simeq\Sigma^3 I(P_{n-5})\), and apply the path classification. When \(n\) is divisible by three the latter complex is contractible; in the other two congruence classes it is exactly the sphere stated above. This proves both formulae for all \(n\ge5\), including integral homotopy rather than only rational or field homology. \(\square\)

## Verification

A standalone program `verify.py` enumerates all nonempty vertex subsets of both fault graphs for each \(5\le n\le12\), tests induced acyclicity by union–find, constructs every simplicial boundary over \(\mathbb F_2\), and performs exact binary rank elimination. It compares every computed Betti group with the above closed formulas. The included `checks.json` reports 16 passing graph cases. These finite calculations corroborate the proof; the *all-parameter* and integral assertions follow from the preceding pushout and suspension arguments, not from finite enumeration.

## Relationship to prior work

Carnero Bravo's *The Forest Filtration of a Graph* (first posted July 25, 2023, arXiv:2307.13271), especially its join lemma and Proposition 38, studies the **intact** wheel's induced-forest filtration. **The rim-fault formula is already an immediate corollary of the general join lemma**, since \(G_n^{\mathrm r}=K_1\ast P_n\); it is included here as the natural baseline and is **not claimed as an independent new theorem**. The new part is the missing-spoke formula: \(G_n^{\mathrm s}\) has no universal vertex and is not in the same join family. Its endpoint-exclusion hub link and resulting mod-three sphere are not supplied by the intact-wheel result. Combining the new spoke result with the elementary rim baseline gives a complete edge-fault orbit comparison.

Barton, Brown and Pike study the face-counting acyclic polynomial of vertex-induced forest complexes. An acyclic face polynomial or its Euler evaluation does not specify the integral homotopy type of these defect families. Published wheel **spanning-forest** complexes of selected edges use a different underlying simplicial complex. A separate indexed theorem about deleting a wheel spoke from an ordinary **three-cut complex** also concerns different faces and does not imply this theorem.

## Limitations

The result is limited to one missing edge, rim length at least five, and the unrestricted induced-forest complex. It does not classify the lower maximum-degree stages, equivariant actions, or maps induced by inclusion of the intact-wheel complex. The included finite computations check mod-two homology only; they cannot by themselves prove an integral or all-length theorem. The homotopy pushout argument supplies those claims. Bibliographic comparisons cannot exclude all unindexed equivalent results, and independent validation has not been performed.

## References

1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first public version July 25, 2023. https://arxiv.org/abs/2307.13271
2. C. Barton, J. I. Brown and D. A. Pike, *Acyclic polynomials of graphs*, Australasian Journal of Combinatorics 82(2) (2022), 146–181. https://ajc.maths.uq.edu.au/pdf/82/ajc_v82_p146.pdf
3. D. Kozlov, *Complexes of directed trees* (1999), cited for the classical independence-path recursion in reference 1. The recurrence is proved directly above.
