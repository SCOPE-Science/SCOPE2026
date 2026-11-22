# A free-to-torsion homology map in the icosahedral cut-complex filtration

## Finding
Let \(I\) be the graph of the regular icosahedron, and \(\Delta_k(I)\) its *ordinary* \(k\)-cut complex. Its adjacent cut stages satisfy \(\Delta_6(I)\subseteq\Delta_5(I)\). The complete reduced integral homology of the six-cut stage is
\[
\widetilde H_j(\Delta_6(I);\mathbb Z)\cong
\begin{cases}
\mathbb Z^6,&j=3,\\
\mathbb Z^{26},&j=4,\\
0,&\text{otherwise}.
\end{cases}
\]
The inclusion induces a **surjection from free homology onto torsion**:
\[
\widetilde H_4(\Delta_6(I);\mathbb Z)\longrightarrow
\widetilde H_4(\Delta_5(I);\mathbb Z)\cong\mathbb Z/2\mathbb Z
\]
is onto. Its kernel is consequently an index-two sublattice of \(\mathbb Z^{26}\), and the mod-two induced homology map has rank one. The pure five-dimensional complex \(\Delta_6(I)\) is not shellable and is not Cohen–Macaulay over any field.

## Assumptions and scope
The twelve vertices are labeled \(0,\ldots,11\) with the thirty edges written explicitly in `verify_icosahedral_cut_transition.py`; this fixes the standard icosahedral graph without relying on external graph libraries. For \(k\in\{5,6\}\), the facets of \(\Delta_k(I)\) are precisely the complements of the \(k\)-element sets \(S\) for which \(I[S]\) is disconnected. The cut filtration is decreasing as \(k\) grows. All homology and homomorphisms are integral unless a coefficient field is specified. Nothing is claimed about a wedge-of-spheres homotopy decomposition, or any other graph.

## Proof
**Finite complexes.** Enumerate the \(\binom{12}{5}=792\) and \(\binom{12}{6}=924\) induced vertex sets, and test connectivity by breadth-first search in the induced graph. There are respectively 300 and 112 disconnected sets. Taking complements and all subfaces gives the complete face vectors (including the empty face)
\[
 f(\Delta_5)=(1,12,66,220,495,792,732,300),\qquad
 f(\Delta_6)=(1,12,66,220,465,432,112).
\]
An independently implemented membership test checks every one of the 4096 vertex subsets against the defining disconnected-complement predicate. It agrees on every face. The 112 facets of \(\Delta_6\) are five-dimensional, making that complex pure.

**Exact integral chain contraction.** Orient each face by increasing vertex labels and use the augmented simplicial chain complex. If a signed boundary coefficient \(d_{r,s}\) is a unit \(u\in\{\pm1\}\), cancel its row generator \(r\) and column generator \(s\) by the integral transformation
\[
 d'_{a,b}=d_{a,b}-d_{a,s}u^{-1}d_{r,b}.
\]
This is an invertible integral basis change followed by removal of a contractible two-term summand, so it preserves **all integral homology**. In every dimension, repeatedly choose a unit pivot minimizing the fill-product of its row and column (with deterministic face-label tie breaks). This algorithm terminates because the total number of generators decreases by two at every step. The standalone code constructs actual signed boundaries and performs every cancellation, without a floating-point rank approximation.

For \(\Delta_6\), exactly 638 unit cancellations leave six degree-three generators and 26 degree-four generators, with every remaining differential zero. Hence its reduced integral homology is exactly as claimed and torsion-free. For \(\Delta_5\), an independent 1,293-unit cancellation leaves one generator each in degrees four and five and thirty in degree six. Its only nonzero residual differential is multiplication by \(2\), from degree five to four. Thus \(\widetilde H_4(\Delta_5;\mathbb Z)=\mathbb Z/2\mathbb Z\), \(\widetilde H_6(\Delta_5;\mathbb Z)=\mathbb Z^{30}\), and all other reduced groups vanish. In both cases the code checks that the residual differential squares to zero. These computations are complete finite, signed integer chain calculations, not finite-field guesses.

**The inclusion is nonzero.** Use the actual inclusion of face sets to construct the simplicial chain map over \(\mathbb F_2\). In \(\Delta_6\), the space of degree-four mod-two cycles has dimension 138 (the boundary rank from degree four to three is 294). In \(\Delta_5\), the boundary space from degree five to degree four has rank 461. The standalone verifier constructs a degree-four cycle in \(\Delta_6\) whose 44 five-vertex supports are recorded in `verification_output.json`; Gaussian reduction shows that the image of this cycle is *not* a degree-five boundary in \(\Delta_5\). Its boundary is zero in both complexes, so the induced \(\mathbb F_2\)-homology map is nonzero. Since \(\widetilde H_4(\Delta_5;\mathbb F_2)\cong\mathbb F_2\), its rank is one.

The integral chain results show that \(\widetilde H_3(\Delta_6;\mathbb Z)\) is free and \(\widetilde H_3(\Delta_5;\mathbb Z)=0\). The universal coefficient theorem therefore identifies reduction modulo two in degree four with tensoring the integral degree-four homology by \(\mathbb F_2\) at both stages, naturally with respect to inclusion. A nonzero mod-two map from \(\mathbb Z^{26}\otimes\mathbb F_2\) to \((\mathbb Z/2)\otimes\mathbb F_2\) forces the original integral map to be onto \(\mathbb Z/2\), proving the central statement.

**Shellability.** A pure five-dimensional shellable complex has reduced homology only in degree five, whereas \(\widetilde H_3(\Delta_6;\mathbb Z)\ne0\). Nonzero degree-three homology over every field likewise obstructs Cohen–Macaulayness.

## Verification
Run `python verify_icosahedral_cut_transition.py` with Python 3.10 or newer (standard library only). It enumerates disconnected vertex sets and verifies a second face-membership predicate, constructs signed augmented boundary operators, carries out exact unit chain contractions for both adjacent complexes, and independently calculates the nontrivial mod-two inclusion image. `verification_output.json` is its captured deterministic output. Expected critical generator counts after the integral reductions are \((6,26)\) in degrees \((3,4)\) for the six-cut stage, and \((1,1,30)\) in degrees \((4,5,6)\) for the five-cut stage, with residual boundary \(\pm2\) only in the latter. The verifier contains all graph and algorithm inputs and raises an exception if any check fails.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduce ordinary graph cut complexes and their decreasing filtration in *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v1 (first public April 26, 2023), particularly Definition 2.7. Their paper provides broad graph-family constructions and does not determine this six-cut complex or the map from stage six to five. Their sequel, *Topology of Cut Complexes II*, arXiv:2407.08158v1 (July 11, 2024), includes six-cut results for **grid graphs** but not the icosahedral graph. The earlier result *Integral two-torsion in the five-cut complex of the icosahedral graph* determines the target group \(\mathbb Z/2\) and hence supplies essential motivation, but does not describe the six-cut source or the inclusion map. The present exact recomputation independently establishes both stages before resolving their connecting map.

## Limitations
The statement is confined to the standard twelve-vertex icosahedral graph and the ordinary six-to-five cut transition. The unit-based chain reduction is an integral chain-homotopy equivalence, not by itself a geometric collapse or an assertion of homotopy wedge type. The nonzero mod-two witness and the universal coefficient argument establish surjectivity but do not specify a preferred integral basis of its rank-26 source. Mathematical literature searches cannot exclude every unpublished or unindexed equivalence. No independent external audit has occurred.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v1, April 26, 2023. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158v1, July 11, 2024. https://arxiv.org/abs/2407.08158
3. *Integral two-torsion in the five-cut complex of the icosahedral graph*, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-integral-two-torsion-in-the-five-cut-complex-of-the-icosahedral--a96727170cea/RESULT.md
