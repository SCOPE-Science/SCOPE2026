# The full Shrikhande independence-homology character and symmetry quotients

## Finding
Let \(S\) be the Shrikhande graph on \(V=(\mathbb Z/4\mathbb Z)^2\), with adjacency defined by differences in
\[D=\{\pm(1,0),\pm(0,1),\pm(1,1)\}.\]
Put \(X=\operatorname{Ind}(S)\). The full graph automorphism group is the affine group \(G=T\rtimes H\) of order \(192\), where \(T=(\mathbb Z/4\mathbb Z)^2\) is the translation group and \(H\) comprises the twelve invertible \(2\times2\) matrices over \(\mathbb Z/4\mathbb Z\) preserving \(D\). The only nonzero reduced rational homology is \(\widetilde H_2(X;\mathbb Q)\), of dimension \(23\).

**Complete character.** For \(g(v)=Av+t\in G\), define \(\chi(g)=\operatorname{Tr}(g_*\mid\widetilde H_2(X;\mathbb Q))\). The following finite signed-face formula explicitly determines its value for *each* \(g\):
\[
\chi(g)=-1+\sum_{\substack{\varnothing\ne F\in\operatorname{Ind}(S)\\gF=F}}(-1)^{|F|-1}\operatorname{sgn}(g|_F).
\]
Here \(\operatorname{sgn}(g|_F)\) is the sign of the permutation induced on the vertices of the invariant face \(F\). Evaluation for all \(192\) automorphisms gives the exact character-value distribution:

| \(\chi(g)\) | Number of group elements |
|---:|---:|
| \(-7\) | 12 |
| \(-3\) | 4 |
| \(-1\) | 69 |
| \(0\) | 32 |
| \(1\) | 24 |
| \(2\) | 32 |
| \(3\) | 18 |
| \(23\) | 1 |

The restriction to translations has, in the order \((u,v)=(0,0),(0,1),\ldots,(3,3)\), the character-value matrix
\[
\begin{pmatrix}
23&-1&-1&-1\\
-1&-1&3&3\\
-1&3&-1&3\\
-1&3&3&-1
\end{pmatrix}.
\]
Writing \(\lambda_{a,b}(u,v)=i^{au+bv}\), its full complex-character decomposition is \(\bigoplus_{a,b=0}^3 m_{a,b}\lambda_{a,b}\), with multiplicity matrix
\[
(m_{a,b})=\begin{pmatrix}
2&1&1&1\\
1&2&2&1\\
1&2&1&2\\
1&1&2&2
\end{pmatrix}.
\]
In particular, \(\dim\widetilde H_2(X;\mathbb Q)^T=2\), while \(\dim\widetilde H_2(X;\mathbb Q)^G=0\). Therefore
\[
\widetilde H_2(X/T;\mathbb Q)\cong\mathbb Q^2,
\qquad \widetilde H_j(X/G;\mathbb Q)=0\quad\text{for every }j\ge0.
\]
These are rational homology statements for the underlying orbit spaces, not claims about integral quotient torsion.

## Assumptions and scope
The graph is finite, simple and undirected, with vertex order \((0,0),(0,1),\ldots,(3,3)\). An independent face is a subset containing no adjacent pair. All homology is ordinary singular homology of the geometric realization. The \(G\)-action is induced by vertex permutations, and quotient spaces have their ordinary quotient topology. The calculation does not assert a new nonequivariant homotopy type: a published finite calculation already establishes \(X\simeq\bigvee^{23}S^2\), which is independently checked here as an input to the Lefschetz argument. The contribution is the full automorphism character and the different translation/full-group invariant dimensions.

## Proof
**Automorphism group.** Every translation preserves \(D\). The checker enumerates all matrices \(A\) with determinant odd and \(AD=D\), finding exactly twelve. Thus there are \(192\) explicit automorphisms. Conversely, every automorphism is determined by the image of \((0,0)\) (at most sixteen choices) and by its permutation of the six neighbors of that vertex. The induced neighborhood graph is a six-cycle, with at most twelve automorphisms. The remaining nine vertices have *nine distinct* unordered pairs of neighbors among those six, so fixing the center and its six neighbors fixes the whole graph. Hence \(|\operatorname{Aut}(S)|\le16\cdot12=192\), proving that all graph automorphisms are accounted for.

**Homology concentration, with an integral check.** Exhaustively test the \(2^{16}\) possible vertex sets, retaining the independent ones. The numbers of nonempty faces in dimensions \(0,1,2,3\) are \((16,72,96,16)\). Pair currently unmatched nonempty faces with their supersets obtained by adjoining the next vertex, processing vertices \(0,1,\ldots,15\) sequentially and faces in ascending mask order. This constructs \(88\) pairs. Reversing the matched edges in the complete \(496\)-incidence Hasse graph produces an acyclic directed graph, checked by full topological sorting of its \(200\) face vertices. Exactly one critical vertex and \(23\) critical two-faces remain. Forman's acyclic-matching theorem gives a CW model with one point and \(23\) two-cells and no other cells, hence \(X\simeq\bigvee^{23}S^2\). This independent finite proof agrees with the published nonequivariant classification.

**Character calculation.** The oriented simplicial chain basis uses increasing vertex indices. An automorphism contributes zero to the trace on a chain group unless it sends an oriented face to itself; an invariant \((k+1)\)-element face contributes the sign of its restricted vertex permutation. The reduced chain Euler trace equals the alternating reduced homology trace by the Hopf trace formula. Since the only nonzero reduced rational homology is degree two, it equals \(\chi(g)\) exactly, producing the displayed formula. Exhaustively applying it to all \(192\) verified affine permutations yields the character distribution and translation grid above.

**Translation modules and quotients.** Fourier inversion in the abelian group \(T\) gives
\[
m_{a,b}=\frac1{16}\sum_{u,v=0}^3\chi(u,v)i^{-au-bv},\]
whose explicitly evaluated integer matrix appears above and sums to \(23\). Thus the trivial character of \(T\) has multiplicity two. Averaging the complete \(G\)-character gives \(192^{-1}\sum_{g\in G}\chi(g)=0\), while \(16^{-1}\sum_{t\in T}\chi(t)=2\). For any finite cellular action, after equivariant barycentric subdivision the quotient rational chain complex is the group-coinvariant complex; over \(\mathbb Q\) coinvariants are exact and isomorphic in dimension to invariants. Thus the stated rational quotient homology follows, including the absence of positive-degree groups for the full quotient. Connectedness gives one ordinary degree-zero class in each quotient.

## Verification
Run `python3 verify_shrikhande_symmetry.py` using Python 3 with no dependencies beyond its standard library. It builds the graph and all independent faces from first principles; verifies the graph parameters, the nonempty face census, all discrete-Morse pairs and all \(496\) directed Hasse incidences, proves full acyclicity, enumerates the twelve stabilizer matrices and all \(192\) automorphisms, and checks every signed invariant-face trace and Fourier multiplicity. Success marker: `SHRIKHANDE_INDEPENDENCE_FULL_192_EQUIVARIANT_CHARACTER_OK`. The finite enumeration is exhaustive because each vertex subset and each candidate affine permutation belongs to an explicitly bounded finite set; the automorphism upper bound is proved separately. No approximation or numerical eigensolver is used.

## Relationship to prior work
The earlier published *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types* already establishes the \(23\)-sphere homotopy type; this result does **not** claim that as novel. That proof does not calculate the induced action of \(\operatorname{Aut}(S)\) or its quotient homology. Bodnar and colleagues' 2021 comparison treats clique complexes of the *original* Shrikhande and rook graphs; the present independence complex is the clique complex of the **complement**. Cioabă and collaborators' homology calculations for original-graph clique complexes are likewise on different simplicial complexes. Goyal–Shukla–Singh investigate other specified graph-family independence complexes, not the Shrikhande automorphism character. The exact signed character, its translation Fourier table and the symmetry-quotient distinction are not statements implied by the displayed nonequivariant Betti numbers or homotopy type.

## Limitations
The complete character is for one canonical finite graph; no claim is made for all strongly regular graphs or all graph-independence complexes. The character computation depends on exhaustive **finite** enumeration and the explicitly supplied automorphism-group bound; neither is presented as evidence for a general infinite-family theorem. The claim concerns rational representations and rational homology of orbit spaces; the calculation does not determine integral homology of the quotients. Searches and material inspections did not identify a covering equivariant result, but unindexed or unpublished equivalents remain possible. Independent external validation has not been performed.

## References
1. C. Bodnar, F. Frasca, Y. G. Wang, N. Otter, G. Montúfar, P. Liò and M. Bronstein, *Weisfeiler and Lehman Go Topological: Message Passing Simplicial Networks*, arXiv:2103.03212v1, first posted 2021-03-04, Figure 3 and proof of Theorem 8: https://arxiv.org/abs/2103.03212.
2. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, public finite proof and executable discrete-Morse check, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187.
3. S. M. Cioabă and collaborators, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328, https://arxiv.org/abs/2606.27328.
4. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1, https://arxiv.org/abs/1905.06926.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; finite acyclic-matching theorem.
