# Mixed-dimensional homotopy and full dihedral homology of a Buchsbaum circulant

## Finding
Let \(G=C_{16}(1,2,6)\) have vertex set \(\{0,1,\dots,15\}\), with \(i\sim j\) precisely when the cyclic distance between the residues is one of \(1,2,6\). Define \(X=\operatorname{Ind}(G)\), the simplicial complex of independent vertex sets. There is an ordinary integral homotopy equivalence
\[
X\simeq S^1\vee\bigvee^4 S^3.
\]
The graph's complete automorphism group is \(D_{16}=\langle r,s\mid r^{16}=s^2=1,\ srs=r^{-1}\rangle\), where \(r(i)=i+1\) and \(s(i)=-i\) modulo 16. Define the rational reflection-sign representation \(\varepsilon\) by \(r\mapsto1,\ s\mapsto-1\). Let \(\zeta_8\) be a primitive eighth root of unity and let \(W=\mathbb Q(\zeta_8)\), a four-dimensional rational vector space. Define a rational \(D_{16}\)-representation on it by
\[
r\cdot z=\zeta_8 z,\qquad s\cdot z=\overline z\quad (z\in W).
\]
These maps satisfy \(r^{16}=s^2=1\) and \(srs=r^{-1}\), with \(r\) acting effectively with order eight.
As rational modules of the *entire* graph-automorphism group,
\[
\widetilde H_j(X;\mathbb Q)\cong
\begin{cases}
\varepsilon,&j=1,\\
W,&j=3,\\
0,&j\notin\{1,3\}.
\end{cases}
\]
Equivalently, for each \(a\in\{0,\ldots,15\}\), the degree-one character satisfies \(\chi_1(r^a)=1\) and \(\chi_1(r^as)=-1\). The degree-three character vanishes on all reflections and is
\[
\chi_3(r^a)=\begin{cases}
4,&a\equiv0\pmod8,\\
-4,&a\equiv4\pmod8,\\
0,&\text{otherwise}.
\end{cases}
\]
Since both rational representations have no invariant vectors, the finite orbit space satisfies \(H^*(|X|/D_{16};\mathbb Q)\cong\mathbb Q\), concentrated in degree zero.

## Assumptions and scope
The graph is simple and undirected, with all edges defined by the conventional cyclic-distance graph \(C_{16}(1,2,6)\). The independence complex contains the empty simplex; all homology statements are reduced unless explicitly written as unreduced cohomology. The homotopy equivalence is ordinary, not claimed equivariant. The integral homology *groups* are \(\mathbb Z\) in degree one and \(\mathbb Z^4\) in degree three; the complete integral lattice of the degree-three action is not classified. The representation and quotient assertions use rational coefficients.

## Proof
**(1) Complete acyclic matching and homotopy type.** Enumerate every nonempty independent vertex subset as a bit mask. There are 260 masks in dimensions zero through three, with face vector \((16,72,112,60)\). Starting with all masks unmatched, perform sequential toggles at vertices
```
10, 1, 8, 7, 3, 5, 14, 0, 12, 15, 11, 13, 9, 2, 6, 4.
```
At a toggle vertex \(v\), pair every still-unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\) when both remain unmatched. Every matched pair is a codimension-one face incidence. The exhaustive directed Hasse graph (unmatched incidences downward, matched incidences upward) contains 260 vertices and 720 incidences and has a topological ordering; hence the matching is acyclic. Exactly 127 pairs and six critical faces remain. Their dimension counts are \((1,1,0,4)\), represented in bit-mask notation by \(264,1024,8721,8772,34884,34960\). These are checks in the bundled standalone program and not assertions based on sampling.

The acyclic-matching theorem gives a CW complex with exactly one cell in degree zero, one in degree one, no degree-two cells, and four degree-three cells. Its one-skeleton is \(S^1\); every three-cell attaches by a map \(S^2\to S^1\), which is null-homotopic because \(\pi_2(S^1)=0\). Thus it is homotopy equivalent to \(S^1\vee\bigvee^4S^3\). This proves the stated integral homology groups as well.

**(2) Full graph symmetries.** The maps \(r:i\mapsto i+1\) and \(s:i\mapsto-i\) preserve cyclic distances, yielding 32 distinct graph automorphisms. Exhaustive adjacency-and-nonadjacency-preserving backtracking over possible vertex images finds exactly these 32, proving that this is the full automorphism group, not merely a subgroup.

**(3) Degree-one action via an integral cocycle.** Orient simplicial edges from smaller to larger vertex. Define a \(\mathbb Z\)-valued one-cochain \(\omega\) by zero except on the following pairs, listed with their values:
```
(1,6):+1, (2,6):+1, (2,7):+1, (6,9):-1,
(1,10):+1, (2,10):+1, (5,10):+1, (2,11):+1,
(6,13):-1, (10,13):-1, (1,14):+1, (2,14):+1,
(5,14):+1, (9,14):+1, (2,15):+1.
```
For each of the 112 oriented triangles \((i,j,k)\), the identity \(\omega(j,k)-\omega(i,k)+\omega(i,j)=0\) holds. Thus \(\omega\) is closed. It evaluates as \(+1\) on the oriented five-edge cycle
```
1 -> 6 -> 3 -> 0 -> 4 -> 1.
```
Since \(H_1(X;\mathbb Z)\cong\mathbb Z\), it is a primitive generator of \(H^1\). Evaluation of \(\omega\) on the image of this cycle under every \(r^as^b\) yields \((-1)^b\). This computes the degree-one character without relying on the alternating trace alone.

**(4) Degree-three action and quotient.** A simplicial automorphism sends each ordered face to an ordered face; when a face is setwise fixed, its signed chain trace contribution is the sign of the induced vertex permutation. Including the empty-face contribution \(-1\), define the reduced Lefschetz sum as \(L(g)=\sum_{j\ge0}(-1)^j\operatorname{Tr}(g\mid\widetilde C_j)-1\). Because only \(\widetilde H_1\) and \(\widetilde H_3\) are nonzero, \(L(g)=-\chi_1(g)-\chi_3(g)\). Enumerating fixed faces and their permutation signs for all 32 automorphisms gives the stated values of \(\chi_3\). These exactly equal the character of \(W\), proving the rational module decomposition (characters determine rational representations of finite groups in characteristic zero). The finite simplicial action admits a barycentric subdivision, and characteristic-zero averaging identifies rational cohomology of the orbit space with the invariant part of rational cohomology of \(X\). Both positive-degree invariant spaces vanish; \(X\) is connected, so the claimed quotient cohomology follows.

## Verification
Run `python3 verify.py` from the directory containing the bundled program. Only the standard library is needed. The program reconstructs the 48 graph edges, all 260 faces and 720 cover incidences, all matched pairs and the acyclicity topological sort, all 32 automorphisms by backtracking, the integral one-cocycle and 112 cocycle identities, and all 32 reduced signed Lefschetz character values. Its complete actual output is in `verification_output.txt`. Reproduction uses integer arithmetic only; the finite enumeration checks the finite certificates used in the proof and does not purport to prove results for other graph orders.

## Relationship to prior work
Earl, Vander Meulen and Van Tuyl classify small well-covered circulants by properties such as Buchsbaum and Cohen–Macaulay. Their 2015 Table 1 lists \(C_{16}(1,2,6)\) as Buchsbaum (but not Cohen–Macaulay) and one-well-covered. Its homotopy type and full automorphism homology character are not stated in the inspected text. Adamaszek provides homotopy splitting theorems and a recursion for independence complexes of consecutive powers of cycles, but this graph has step set \(\{1,2,6\}\), so the cited cycle-power recursion does not imply the present computation. The contribution here is the mixed-dimensional homotopy classification, the complete rational dihedral character and the quotient's rational cohomology, not the earlier Buchsbaum classification. Equivalent results in unindexed literature remain possible.

## Limitations
This is a theorem about exactly the specified 16-vertex graph, not all Buchsbaum circulants. The individual Morse pairs are not claimed equivariant. Rational homology characters do not determine the integral lattice of the degree-three automorphism representation. Rational cohomology of the orbit space does not determine its integral cohomology or equivariant homotopy type. No independent mathematical audit or definitive publication-priority certification is claimed.

## References
- J. Earl, K. N. Vander Meulen and A. Van Tuyl, *Independence complexes of well-covered circulant graphs*, arXiv:1505.02837 (first public preprint 2015-05-11). https://arxiv.org/abs/1505.02837
- M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250 (first public preprint 2011-06-30). https://arxiv.org/abs/1106.6250
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145 (acyclic matching/CW construction).
