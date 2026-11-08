# The signed-coordinate torsion character of a doubled cross-polytope boundary

## Finding

For an integer \(d\geq2\), let \(C_d\) be the \(d\)-dimensional cross-polytope, with vertices \((i,+)\) and \((i,-)\) for \(1\leq i\leq d\). Put \(Y_d=D^2(\partial C_d)\), where a vertex of the simplicial double is an edge of \(\partial C_d\), and a collection of these vertices is a face when the corresponding edges are disjoint and their union is a face of \(\partial C_d\).

**The theorem** is that \(Y_d\) has torsion-free reduced integral homology for \(2\leq d\leq6\), while \(Y_7\) is the first member with integral torsion and
\[
\widetilde H_1(Y_7;\mathbb Z)\cong\mathbb Z/3\mathbb Z,\qquad
\widetilde H_2(Y_7;\mathbb Z)\cong\mathbb Z^{5123},
\]
with all other reduced integral homology groups zero. In particular, the double of this shellable flag sphere is **not** homotopy equivalent to a wedge of spheres, since such a wedge has torsion-free integral homology. More precisely, the natural signed-coordinate group \(W_7=(C_2)^7\rtimes S_7\) acts on its unique torsion group by the sign character pulled back from \(S_7\):
\[
 (\varepsilon,\sigma)_*x=\operatorname{sgn}(\sigma)x\quad
 \text{for every }x\in\widetilde H_1(Y_7;\mathbb Z),
 \quad \varepsilon\in(C_2)^7,\ \sigma\in S_7.
\]
This distinguishes the two possible one-dimensional \(S_7\)-modules over \(\mathbb F_3\) and gives a torsion-sensitive equivariant invariant of the first such double.

As a consequence, if \(\tau\) swaps two coordinate labels, then
\[
\widetilde H_1(|Y_7|/\langle\tau\rangle;\mathbb F_3)=0,
\]
although \(\widetilde H_1(Y_7;\mathbb F_3)\cong\mathbb F_3\). The quotient statement concerns ordinary geometric realization modulo the involution.

## Assumptions and scope

All simplicial complexes are finite and abstract; a face may be empty. Homology is reduced unless explicitly stated otherwise. Coordinate reflections independently interchange the two signs for each index; coordinate permutations permute the indices without changing the signs. The double operation is exactly that of Lesh--Schreiner--Wahl. The first-public source date is June 12, 2025, not the October 2026 revision date.

Let \(M_d=\mathcal M(K_d)\) be the ordinary matching complex of the complete graph on \(d\) labels. The vertex-inflation \(\operatorname{Infl}_4(M_d)\) replaces every vertex of \(M_d\) by four alternative copies, with faces choosing at most one copy of each original vertex. All homotopy types in this note are ordinary, not equivariant homotopy decompositions.

## Proof

**1. Canonical inflation identification.** A vertex of \(Y_d\) is a pair of signed coordinates \(\{(i,s),(j,t)\}\) with \(i\ne j\) and \(s,t\in\{+,-\}\). There are exactly four such vertices above each edge \(\{i,j\}\) of \(K_d\). A collection belongs to \(Y_d\) precisely when its coordinate pairs are mutually disjoint, because a face of the cross-polytope cannot contain both signs of any coordinate. Thus
\[
Y_d\cong\operatorname{Infl}_4(M_d).
\]
This isomorphism intertwines the signed-coordinate action with the quotient action on \(M_d\) and the independent relabelling of its four copies.

**2. Homotopy decomposition and threshold.** The vertex-inflation wedge theorem (Björner--Wachs--Welker, in the form of Ayzenberg--Khoroshavkina, Corollary 7.1) gives, for connected \(M_d\),
\[
|Y_d|\simeq|M_d|\ \vee\!
\bigvee_{\substack{\varnothing\ne\sigma\in M_d}}
\bigvee^{3^{|\sigma|}}\Sigma^{|\sigma|}|\operatorname{lk}_{M_d}\sigma|.
\]
For \(d=7\), matchings have one, two or three edges, and the links of an \(r\)-edge matching are exactly \(M_{7-2r}\). Here \(M_5\simeq\bigvee^6S^1\), \(M_3\simeq\bigvee^2S^0\), and \(M_1=\{\varnothing\}\) contributes the conventional empty-face sphere under suspension. There are \(21\) one-edge, \(105\) two-edge, and \(105\) three-edge matchings. Therefore the additional two-sphere multiplicity is
\[
 21\cdot3\cdot6+105\cdot9\cdot2+105\cdot27=5103.
\]
It follows that \(|Y_7|\simeq|M_7|\vee\bigvee^{5103}S^2\). The established integral homology calculation of \(M_7\) gives \(\widetilde H_1(M_7;\mathbb Z)=\mathbb Z/3\mathbb Z\) and \(\widetilde H_2(M_7;\mathbb Z)=\mathbb Z^{20}\). Combining these results proves the displayed integral homology. As a direct check, the face counts of \(Y_7\) are \((84,1680,6720)\), so its reduced Euler characteristic is \(5123\).

For \(d\le6\), each matching complex \(M_d\) and every link \(M_{d-2r}\) has torsion-free reduced integral homology: the small matching complexes are homotopy-equivalent to graphs or discrete spaces, as described in the matching-complex literature. Applying the same vertex-inflation splitting therefore proves the sharp torsion-free cutoff. The cases \(d=2,3\), whose bases are not connected, are checked directly: \(Y_2\) is a discrete four-point space, and \(Y_3\) is a discrete twelve-point space. For \(d=4\), the three edges of \(M_4\) inflate to three copies of \(K_{4,4}\), a disjoint union of graphs; for \(d=5,6\), the connected-base formula applies.

**3. The integral torsion representation.** Let \(p:Y_7\to M_7\) forget the signs and let \(s:M_7\to Y_7\) choose plus signs everywhere. Since \(p\circ s\) is the identity, the homomorphism \(p_*\) is surjective in first integral homology. By the computation above its domain and codomain are both \(\mathbb Z/3\mathbb Z\); hence it is an isomorphism. Every coordinate sign flip fixes \(p\), so every element of \((C_2)^7\) acts trivially on this group. The \(S_7\)-action transfers identically from \(M_7\) along \(p_*\).

To determine that action, label \(M_7\)'s vertices by unordered pairs of \(\{0,1,\ldots,6\}\), ordered lexicographically, and orient each edge accordingly. Consider the integral cycle
\[
\begin{split}
 z={}&[(01),(23)]-[(01),(34)]-[(02),(15)]\\
    &+[(02),(34)]-[(15),(23)].
\end{split}
\]
The brackets denote an oriented edge between two pair-vertices, not a single edge of \(K_7\). Direct cancellation verifies \(\partial_1z=0\) **over the integers**. Exact elimination over \(\mathbb F_3\) on the complete \(105\)-column triangle boundary matrix gives rank \(84\), and reduction of \(z\) is nonzero. Its mod-three homology class therefore spans the one-dimensional \(H_1(M_7;\mathbb F_3)\). By the integral homology calculation and universal coefficients, reduction induces an injection from \(H_1(M_7;\mathbb Z)\cong\mathbb Z/3\mathbb Z\) onto that line; hence \(z\) represents the integral generator.

Let \(\tau=(0\ 1)\) act on coordinate labels. The standalone 32-triangle chain in `torsion_witness.json` satisfies the **exact** mod-three chain identity
\[
 \partial_2 b=z+\tau_*(z)\pmod3.
\]
The accompanying verifier reconstructs and checks every oriented incidence in this identity, and separately proves \([z]\ne0\) by full rank reduction. It follows that \(\tau_*[z]=-[z]\) on integral \(\mathbb Z/3\mathbb Z\). Every transposition is conjugate to \(\tau\), and the action is a homomorphism \(S_7\to\operatorname{Aut}(\mathbb Z/3\mathbb Z)\cong C_2\); therefore it is precisely the sign character. This proves the \(W_7\)-module statement.

**4. Quotient by an odd permutation.** Barycentrically subdivide \(Y_7\) equivariantly to remove inversions. Over \(\mathbb F_3\), transfer and averaging for the order-two group \(\langle\tau\rangle\) identify the quotient's homology with the invariant homology of \(Y_7\). The nontrivial sign action has no invariant vector in degree one, so the displayed quotient homology vanishes.

## Verification

Run `python verify.py` in the directory containing `torsion_witness.json`. The executable constructs the complete matching complex, checks the oriented integral five-edge cycle and the explicit 32-triangle mod-three boundary identity, computes the triangle boundary rank independently, and verifies the inflated face counts and sphere multiplicities. It uses Python's standard library only. The recorded output is in `verification-output.txt`. All finite checks are exact. For the *integral* homology of \(M_7\), and for the inflation homotopy splitting, the proof uses the cited published theorems rather than asserting that finite-field elimination alone proves them.

## Relationship to prior work

Lesh--Schreiner--Wahl introduce the simplicial double and study connectivity; they identify doubles of simplices with matching complexes. Ayzenberg--Khoroshavkina and the earlier Björner--Wachs--Welker work supply the general vertex-inflation wedge decomposition. Mondal--Mukherjee--Saha, following Bouc, provide the integral \(M_7\)-homology groups. Thus **the non-equivariant homology calculation and the sharp torsion threshold are applications of known structural theorems, not independently claimed as a new general inflation theorem**. The specific new comparison target is the exact signed-coordinate action on the nonzero \(3\)-torsion of the cross-polytope **double**, exhibited by the finite chain witness and its quotient consequence. The inspected source statements do not supply that torsion character. Any implicit published integral \(S_7\)-module determination of \(H_1(M_7)\) would also determine it; this remains a residual novelty risk.

## Limitations

The result gives one integral torsion module and ordinary integral homology, not an equivariant sphere-wedge splitting, the entire integral degree-two representation, or the homotopy type of the quotient. The calculation does not classify all doubled spheres or all higher-dimensional cross-polytopes; the cutoff is only the **first** torsion occurrence. The rank computation is exact for \(M_7\), but it is not a substitute for the cited integral matching-complex result. Independent human verification and comprehensive bibliographical originality certification have not been carried out.

## References

1. K. Lesh, B. Schreiner, N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436v1 (first public June 12, 2025), https://arxiv.org/abs/2506.10436 .
2. A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (2026), Corollary 7.1, https://arxiv.org/html/2602.08694 .
3. A. Björner, M. Wachs, V. Welker, *Poset Fiber Theorems*, Theorem 6.2; vertex-inflation decomposition, https://www.math.miami.edu/~wachs/papers/fibers.pdf .
4. A. Mondal, S. Mukherjee, K. Saha, *Discrete Morse theoretic computations in the matching complex of \(K_7\)*, arXiv:2305.02973v1, Theorem 1.1, https://arxiv.org/abs/2305.02973 .
5. J. Shareshian and M. L. Wachs, *Torsion in the matching complex and chessboard complex*, arXiv:math/0409054, https://arxiv.org/abs/math/0409054 .
