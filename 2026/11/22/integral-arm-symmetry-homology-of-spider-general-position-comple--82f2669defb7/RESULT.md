# Integral arm-symmetry homology of spider general-position complexes

## Finding
For every pair of integers \(r\ge3\) and \(\ell\ge1\), let \(T_{r,\ell}\) be the finite spider tree obtained by identifying one endpoint of \(r\) disjoint paths of \(\ell\) edges, and let \(X_{r,\ell}=\operatorname{GP}(T_{r,\ell})\) be the simplicial complex of vertex sets containing no geodesically collinear triple. The symmetric group \(S_r\) acts by permuting equal-length arms and fixing their common center.

Let \(P=\mathbb Z^r\) be the arm-permutation lattice, let \(M=\mathbb Z^\ell\) be the depth lattice with trivial \(S_r\)-action, let \(A=\ker(M\xrightarrow{\sum}\mathbb Z)\), and let \(W=\ker(P\otimes M\xrightarrow{\sum}\mathbb Z)\). There are **natural integral \(S_r\)-module isomorphisms**
\[
\widetilde H_i(X_{r,\ell};\mathbb Z)\cong
\begin{cases}
P^{\oplus\binom{\ell}{2}}\oplus W,&i=1,\\
\operatorname{sgn}_{S_r}\otimes A^{\otimes r},&i=r-1,\\
0,&\text{otherwise},
\end{cases}
\]
where \(S_r\) permutes the \(r\) tensor factors in the second line, and the sign twist is the ordinary permutation sign. In particular the underlying integral homotopy type is
\[
|X_{r,\ell}|\simeq
\bigvee^{r(\binom{\ell}{2}+\ell)-1}S^1\ \vee\
\bigvee^{(\ell-1)^r}S^{r-1}.
\]
Zero-multiplicity summands are omitted. For an arm permutation \(\sigma\), write \(f(\sigma)\) for its number of fixed arms and \(c(\sigma)\) for its number of cycles, counting fixed points. The complete rational character is
\[
\operatorname{tr}(\sigma\mid H_1)=\left(\binom{\ell}{2}+\ell\right)f(\sigma)-1,
\qquad
\operatorname{tr}(\sigma\mid H_{r-1})=\operatorname{sgn}(\sigma)(\ell-1)^{c(\sigma)}.
\]
Taking the **genuine geometric quotient** by arm permutations gives the rational Betti ranks
\[
\boxed{\ 
\dim_{\mathbb Q}\widetilde H_1(|X_{r,\ell}|/S_r;\mathbb Q)=\binom{\ell}{2}+\ell-1,
\quad
\dim_{\mathbb Q}\widetilde H_{r-1}(|X_{r,\ell}|/S_r;\mathbb Q)=\binom{\ell-1}{r}.
\ }
\]
No other reduced rational homology occurs in the quotient. Hence all high-dimensional rational homology disappears in the full arm quotient exactly when \(\ell\le r\), despite \((\ell-1)^r\) high-dimensional generators in the original complex when \(\ell\ge2\).

## Assumptions and scope
All graphs are finite, simple, unweighted and undirected. The spider has exactly one vertex \(c\) of degree \(r\ge3\); its arm vertex sets are \(V_1,\ldots,V_r\), with \(|V_i|=\ell\). Each \(V_i\) is indexed by graph distance \(1,\ldots,\ell\) from \(c\). A subset is a face of \(\operatorname{GP}(T)\) precisely when no one of its vertices lies on the unique tree geodesic between two others. Homology is unreduced in the displayed positive degrees, reduced otherwise. Module isomorphisms refer only to the genuine graph-automorphism subgroup \(S_r\) permuting equal-length arms, not arbitrary depth permutations.

The integral homology, full rational character and geometric quotient ranks form a single equivariant classification; the unequivariant wedge decomposition is included to identify its geometric content.

## Proof
**1. Exact face decomposition.** Every subset with at most two vertices is permitted. For three or more vertices, a valid subset cannot contain \(c\), since any other two vertices either lie on different arms (making \(c\) intermediate) or on one arm (making the nearer vertex intermediate). It cannot have two vertices in one arm: with any third vertex, the nearer or middle vertex lies on a geodesic between the other two. Conversely, sets not containing \(c\) and choosing at most one vertex from each arm are permitted, since the unique geodesic between vertices from two arms runs only through those arms and \(c\). This proves the full labelled simplicial decomposition
\[
X_{r,\ell}=J\ \cup\ \bigcup_{i=1}^r E_i\ \cup\ (c*D(V)),
\qquad J=D(V_1)*\cdots*D(V_r),
\]
where \(D(V_i)\) is discrete on \(V_i\), \(V=\bigcup_i V_i\), \(E_i\) consists of all internal two-vertex edges in \(V_i\) and their faces, and \(c*D(V)\) is the central star of \(r\ell\) edges. None of the added internal or central edges lies in a two-simplex of \(X_{r,\ell}\).

**2. Homotopy and vanishing ranges.** The join \(J\) is connected and simply connected for \(r\ge3\), because it is the join of at least three nonempty discrete spaces. Its reduced integral homology is concentrated in degree \(r-1\) and is the tensor product of the \(r\) augmentation lattices \(\widetilde H_0(D(V_i);\mathbb Z)\cong A\), of rank \((\ell-1)^r\). The join is an integral wedge of that many spheres of dimension \(r-1\); if any factor is a singleton it is contractible. Attaching the \(r\binom{\ell}{2}\) internal edges and the \(r\ell\) central edges with one new vertex changes the homotopy type by wedging \(r\binom{\ell}{2}+r\ell-1\) circles. Indeed, the already-connected base joins all endpoints, and the first central edge attaches the new vertex contractibly; every further edge has both ends in a path-connected space and wedges on one circle. This gives the displayed homotopy classification and integral torsion-freeness.

**3. Integral first-homology module.** Orient every internal arm edge by increasing depth and every central edge from \(c\) toward an arm vertex. In degree one the chain group is a direct sum of the cross-arm edge chains \(C_1(J)\), the internal oriented arm-edge lattice \(E\cong P^{\oplus\binom{\ell}{2}}\), and the central edge lattice \(P\otimes M\). All two-dimensional boundaries lie in \(C_1(J)\). Project any one-cycle to \(E\oplus(P\otimes M)\). Its central-edge coefficients must sum to zero, by taking its boundary coefficient at \(c\). Conversely, given arbitrary internal coefficients and central coefficients summing to zero, the boundary of that partial chain is a zero-sum zero-chain on \(V\); it can be cancelled by an integral cross-arm edge chain, since the one-skeleton of \(J\) is connected. Two resulting lifts differ by an integral one-cycle in \(J\), and this bounds integrally since \(H_1(J;\mathbb Z)=0\). Projection therefore induces the canonical integral isomorphism \(H_1(X;\mathbb Z)\cong E\oplus W\). Arm permutations preserve increasing-depth edge orientations, so this is \(S_r\)-equivariant without hidden sign changes.

**4. Top module and character.** The top homology is unchanged by the attached edges: \(\widetilde H_{r-1}(X;\mathbb Z)\cong\widetilde H_{r-1}(J;\mathbb Z)\). The reduced join-chain Künneth isomorphism identifies it with \(A^{\otimes r}\). Interchanging two degree-zero reduced homology factors changes the orientation of their join by \(-1\); hence a general arm permutation carries the stated sign twist. The first-homology character follows from \(E\cong P^{\oplus\binom{\ell}{2}}\) and from the equivariant exact sequence \(0\to W\to P\otimes M\to\mathbb Z\to0\): their traces are respectively \(\binom{\ell}{2} f(\sigma)\) and \(\ell f(\sigma)-1\). The signed tensor permutation on \(A^{\otimes r}\) has trace \(\operatorname{sgn}(\sigma)(\ell-1)^{c(\sigma)}\): each permutation cycle enforces equality of tensor-basis indices.

**5. Quotient homology and sharp threshold.** A finite simplicial group action admits an equivariant barycentric subdivision without inversions, so over \(\mathbb Q\) the homology of the geometric quotient equals the invariant homology of the original. The invariants in \(E\) have rank \(\binom{\ell}{2}\), one diagonal sum for each fixed depth pair. The invariants in \(W\) have rank \(\ell-1\), with equal coefficients across all arms at each depth and one total-sum constraint. The invariants in the signed factor-permutation module \(A^{\otimes r}\otimes\operatorname{sgn}\) are the alternating tensors \(\bigwedge^r(A\otimes\mathbb Q)\), of dimension \(\binom{\ell-1}{r}\). This proves both quotient formulas, with zero higher rank precisely for \(\ell-1<r\).

## Verification
The standalone standard-library script `check_spider.py` reconstructs geodesic distances by breadth-first search, compares every subset with the predicted face decomposition, computes reduced simplicial homology by exact binary boundary elimination, and independently obtains every chain-level signed Lefschetz trace under all permutations of equal-length arms. It checks the character identities by comparing chain traces with the predicted homology traces and verifies the quotient ranks by exact group averaging. Tested cases are \((r,\ell)=(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(5,1),(5,2)\): 981 simplicial faces and 336 arm permutations. Run `python3 check_spider.py` with Python 3 and no third-party packages. The program is a finite cross-check, not the proof of the unrestricted quantifiers.

For example, with \((r,\ell)=(3,4)\), the original reduced Betti ranks are 29 in degree one and 27 in degree two; the full arm quotient has rational ranks 9 and 1. With \((r,\ell)=(4,2)\), the original ranks are 11 in degree one and 1 in degree three, but the full quotient has rational ranks 2 and 0.

## Relationship to prior work
Iršič, Klavžar, Rus and Tuite introduced general-position polynomials and studied special trees including brooms. Rather (first public 6 March 2026) studied general-position counting and unimodality, including graph coronas; neither source computes arm-symmetry homology representations or quotient homology for the present complexes.

A directly relevant public mathematical record entitled *General position polynomials of spiders and the smallest nonunimodal spider* gives the **complete labelled face characterization** of spider general-position complexes and their ordinary enumerator. That characterization is prior input, not claimed new here. The assessed result is the natural integral \(S_r\)-module classification, all character values, and the sharp vanishing threshold for top homology in the genuine geometric quotient. Its topological proof uses that face description but adds the cycle-projection and sign-twisted tensor calculations not present in the record. A separate record on *Mixed-dimensional integral homotopy of geodesic-avoidance complexes of clique bouquets* concerns a different complex: avoidance of full inclusion-maximal geodesics of a clique bouquet, rather than avoidance of collinear triples in a spider tree. Its related circle/sphere wedge does not provide the spider arm-permutation characters or quotient invariant dimensions.

A published mathematical-index search compared the claims using “spider,” “starlike tree,” “subdivided star,” “arm permutation,” “geodesic general position,” and “geometric quotient” formulations, including wider tensor and augmentation-module statements. No directly covering arm-equivariant spider theorem was recovered. Since the known full-face description makes the present calculation accessible using standard chain tools, there is a residual risk of an unindexed or implicit equivalent computation.

## Limitations
The statement is for equal positive arm lengths and the corresponding full arm-permutation automorphism group; it does not determine integral torsion of the quotient, its fundamental group, or homotopy type. A rationally acyclic high-dimensional quotient need not be contractible. The module formulas are integral for the *unquotiented* space only. Numerical checks cover the listed small profiles; the proof establishes all integers \(r\ge3\), \(\ell\ge1\). Independent validation and exhaustive publication-priority determination are not claimed.

## References
1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696v1 (11 January 2024), https://arxiv.org/abs/2401.05696.
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v1 (6 March 2026), https://arxiv.org/abs/2603.06930; full accessible HTML: https://arxiv.org/html/2603.06930v3.
3. *General position polynomials of spiders and the smallest nonunimodal spider*, publicly indexed mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-general-position-polynomials-of-spiders-and-the-smallest-nonunim--86888c8b4991 (retrieved 19 November 2026 UTC).
4. *Mixed-dimensional integral homotopy of geodesic-avoidance complexes of clique bouquets*, publicly indexed mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-integral-homotopy-of-geodesic-avoidance-comple--225b533c1864 (retrieved 19 November 2026 UTC).
