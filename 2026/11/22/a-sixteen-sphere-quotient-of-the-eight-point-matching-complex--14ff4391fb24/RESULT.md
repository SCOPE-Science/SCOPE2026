# A sixteen-sphere quotient of the eight-point matching complex

## Finding

Let \(K=\mathcal M(K_8)\) be the matching complex of the complete graph on vertex set \(\mathbb Z/8\mathbb Z\). Its simplices are collections of pairwise vertex-disjoint graph edges. Let \(C_8\) act by cyclically adding one to each graph-vertex label. For the **ordinary geometric orbit space**, not a Borel construction, there is a homotopy equivalence

\[
|K|/C_8\simeq\bigvee^{16} S^2.
\]

In particular, the quotient is simply connected and has integral reduced homology \(\widetilde H_2\cong\mathbb Z^{16}\), with all other reduced integral homology zero.

## Assumptions and scope

The graph is the ordinary loopless complete graph on eight distinct vertices; edges are unordered pairs. A face of \(K\) is a set of pairwise disjoint edges, including the empty face. Rotations send each endpoint \(i\) to \(i+t\pmod 8\), with \(t\in\mathbb Z/8\mathbb Z\). The topology concerns the quotient of the geometric realization with its actual nonfree action. No assertion is made for other graph sizes, subgroups, or dihedral reflections.

## Proof

**1. Simple connectivity.** The matching-complex connectivity theorem of Björner–Lovász–Vrećica–Živaljević, reproduced in Shareshian–Wachs [1] and Mondal–Mukherjee–Saha [2], states that \(\mathcal M(K_n)\) is \((\nu_n-1)\)-connected, where \(\nu_n=\lfloor(n+1)/3\rfloor-1\). At \(n=8\), \(\nu_8=2\), so \(|K|\) is simply connected. The four-edge matching

\[
\sigma_* = \{\{0,4\},\{1,5\},\{2,6\},\{3,7\}\}
\]

is preserved as a set by every rotation. Its barycenter is therefore fixed by all of \(C_8\). Armstrong's orbit-space fundamental-group theorem [3] gives \(\pi_1(|K|/C_8)=0\).

**2. An exact integral quotient chain complex.** The nonempty matching counts, for one through four edges, are respectively

\[
(28,210,420,105).
\]

To handle the nonfree action without mistaking a setwise-stabilized simplex for an ordinary simplex downstairs, take the barycentric subdivision. Its \(k\)-simplices are strict chains \(\sigma_0\subsetneq\cdots\subsetneq\sigma_k\) of nonempty matchings. The rotational action preserves the dimension of every face and is without inversions on this subdivision. Quotient cells are precisely orbits of such chains; give them the orientation of increasing chain position. The quotient has exact cell counts

\[
(c_0,c_1,c_2,c_3)=(107,576,804,318).
\]

For every representative chain the integral boundary is obtained by deleting the \(j\)-th member with coefficient \((-1)^j\) and canonically rotating the remaining flag into its orbit representative; coinciding orbit faces are added with signs. The resulting matrices have \(\partial^2=0\) over \(\mathbb Z\).

**3. Integral chain reduction.** In a finitely generated free integral chain complex, a boundary coefficient \(+1\) or \(-1\) gives a contractible two-generator direct summand after integer changes of bases. Eliminating such a pair updates its differential by the exact integral Schur complement, deleting the corresponding row from the next differential and the corresponding column from the previous differential. This preserves integral homology, including torsion. Applying the deterministic minimum-fill unit-pivot rule implemented in `verify_m8_cyclic.py` performs exactly \(106\), \(470\), and \(318\) cancellations in dimensions one, two, and three. The remaining chain groups have ranks

\[
(1,0,16,0),
\]

with zero differentials. In particular, there is no residual nonunit invariant factor, and the integral homology is \(H_0\cong\mathbb Z\), \(H_2\cong\mathbb Z^{16}\), and zero otherwise. The Euler characteristic independently agrees: \(107-576+804-318=17\).

**4. Homotopy type.** Because the quotient is simply connected, the Hurewicz map \(\pi_2\to H_2\) is an isomorphism. Choose based maps of sixteen two-spheres representing an integral basis of \(H_2\). Their wedge gives a map \(\bigvee^{16}S^2\to |K|/C_8\) which is an isomorphism on every integral homology group. Whitehead's homology theorem for simply connected CW complexes makes it a homotopy equivalence.

## Verification

Run `python3 verify_m8_cyclic.py` with a standard Python 3 interpreter; no third-party libraries or external files are required. It exhaustively generates all 763 nonempty matchings, their nested flags, and the eight rotational images, assembles the complete integral orbit-chain matrices, checks \(\partial^2=0\), carries out exact unit-pivot cancellations, verifies the global fixed simplex, and independently checks boundary ranks modulo \(2,3,5,7,11,101\). The required terminal marker is `M8_ROTATION_QUOTIENT_INTEGRAL_CHECKS_OK`.

The modular checks corroborate the computation but are not, by themselves, a proof of absence of integer torsion; the integral unit-pivot elimination supplies that proof.

## Relationship to prior work

The known nonequivariant result is \(|\mathcal M(K_8)|\simeq\bigvee^{132}S^2\) [2]. The matching-complex connectivity, integral homology and symmetric-group representation literature [1,2] does not in the inspected matching-complex sections identify the **ordinary geometric quotient by this specific cyclic rotation**. A rational invariant calculation or the nonequivariant wedge decomposition would not by itself establish the integral torsion-freeness or simple connectivity of this nonfree orbit space. The new statement is this quotient's complete integral homotopy type, not the known homotopy type of its covering complex.

## Limitations

The classification concerns the eight-vertex case and the full cyclic rotation group only. It is a homotopy equivalence, not a claimed homeomorphism, equivariant collapse of the covering complex, or an integral decomposition of the covering homology as a group module. The integer computation is finite and exhaustive for this specific complex; it does not establish a formula for all matching-complex sizes. Published equivalents outside the inspected literature may exist; independent mathematical review has not been performed.

## References

[1] J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1, first public 2004-09-03. https://arxiv.org/abs/math/0409054

[2] A. Mondal, S. Mukherjee and K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, Discrete Mathematics & Theoretical Computer Science 26(3) (2024), Example 3.3 and Theorem 1.1. https://doi.org/10.46298/dmtcs.12887

[3] M. A. Armstrong, *On the fundamental group of an orbit space*, Proceedings of the Cambridge Philosophical Society 61 (1965), 639–646. https://doi.org/10.1017/S0305004100038974
