# Two consecutive three-primary torsion degrees in a nine-point matching quotient

## Finding

Let \(M_9\) be the ordinary matching complex of the complete graph on the nine cyclically labelled vertices \(\mathbb Z/9\mathbb Z\). A simplex is a set of pairwise vertex-disjoint unordered graph edges. Let \(C_9=\langle r\rangle\) act by \(r(i)=i+1\), and let \(Q=|M_9|/C_9\) denote the **ordinary geometric quotient**, not a coinvariant chain complex of un-subdivided simplices. Its complete integral homology and fundamental group are

\[
H_j(Q;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z/3\mathbb Z,&j=1,\\
\mathbb Z^6\oplus\mathbb Z/3\mathbb Z,&j=2,\\
\mathbb Z^8,&j=3,\\
0,&j\ge4,
\end{cases}
\qquad \pi_1(Q)\cong\mathbb Z/3\mathbb Z.
\]

Thus the nonfree rotation quotient carries order-three torsion in two consecutive positive homology degrees. Nine is the first *odd composite* number of cyclically labelled points, making this a natural first case in which a nontrivial proper rotation subgroup can fix a matching although the full rotation generator fixes none.

## Assumptions and scope

All spaces are ordinary finite geometric realizations, homology is with integral coefficients, and the group action permutes the nine graph vertices. The complex \(M_9\) contains every nonempty matching of sizes one through four. The quotient identifies points in the realization, not merely simplices with the same orbit. All chain matrices use cardinality-increasing face flags, giving canonical orientations in the barycentric subdivision. The statement concerns exactly nine vertices and makes no extrapolation to other composite parameters or the full homotopy type.

## Proof

**1. Valid quotient triangulation.** A nonempty face \(F\) is a matching, and a vertex of \(\operatorname{sd}(M_9)\) is its nonempty face \(F\). A simplex is a strict flag \(F_0\subsetneq\cdots\subsetneq F_k\). Every group element that preserves such a flag setwise fixes each member because all its cardinalities are distinct. Thus the subdivided action is without inversions. One \(k\)-cell for each orbit of cardinality-increasing flags, with boundary \(\partial[F_0<\cdots<F_k]=\sum_{i=0}^k(-1)^i[F_0<\cdots<\widehat F_i<\cdots<F_k]\), is therefore the **actual integral cellular chain complex** of \(Q\); duplicate quotient faces contribute their signed integer multiplicities.

**2. Exhaustive finite incidence and Smith normal form.** The matching-face counts by size one through four are \((36,378,1260,945)\), total \(2619\). Counts of subdivision flags in simplex dimensions zero through three are \((2619,21546,41580,22680)\). The action of nine rotations gives exactly \((293,2394,4620,2520)\) quotient cells in these dimensions. The included `verify_matching9.py` rebuilds every matching, every flag and every orbit. It computes each signed integral boundary, checks \(\partial^2=0\), and carries out exact unimodular unit-pivot eliminations. After splitting the unit diagonal factors, each remaining nonzero matrix is checked to have rational rank one (all \(2\)-by-\(2\) minors zero), with all entries having gcd three. The resulting nonzero Smith factors are

\[
\operatorname{SNF}(\partial_1):1^{292},\qquad
\operatorname{SNF}(\partial_2):1^{2101},3,\qquad
\operatorname{SNF}(\partial_3):1^{2511},3.
\]

Here zero factors are omitted. The ranks are \((292,2102,2512)\). Since the image of each cellular boundary is free abelian, the torsion subgroup of \(H_{j-1}\) equals the torsion subgroup of \(\operatorname{coker}(\partial_j)\): the quotient of the latter by the former is the free group \(\operatorname{im}(\partial_{j-1})\). Rank-nullity consequently gives the displayed complete homology groups, with free ranks six and eight in degrees two and three. The alternating cell count gives Euler characteristic \(-1=1+6-8\). An independent Burnside Euler check uses \(\chi(M_9)=-27\) and fixed-set Euler characteristics \(9\) for each of \(r^3,r^6\), and zero for the other six nonidentity rotations; the group average is \((-27+9+9)/9=-1\).

**3. Fundamental group.** The standard matching-complex connectivity bound gives that \(|M_9|\) is simply connected. No matching is preserved by a one-step rotation: its edge orbit has nine elements, whereas a matching has at most four. A three-step rotation preserves precisely nine three-edge matchings, including \(\{\{0,1\},\{3,4\},\{6,7\}\}\); their barycenters are fixed points. No element with order nine fixes a nonempty matching, and every nonidentity element with fixed points lies in \(\langle r^3\rangle\cong C_3\). Armstrong's orbit-space theorem therefore gives \(\pi_1(Q)\cong C_9/\langle r^3\rangle\cong C_3\).

## Verification

Run `python3 verify_matching9.py` from this package. The script depends only on Python's standard library, uses exact integers throughout, verifies all boundary compositions and the rank-one/gcd certificates, and prints the expected output in `verification_output.txt`. The actual observed output was reproduced after executing the standalone verifier; neither a probabilistic rank estimate nor floating-point arithmetic is used. The Smith reductions check the complete enumerated finite chain complex, not a nonexhaustive sample.

## Relationship to prior work

Shareshian–Wachs (2004) develops matching-complex homology, connectivity, and torsion for the unquotiented \(M_n\). Jonsson's published ambient-homology table records \(\widetilde H_2(M_9;\mathbb Z)\cong\mathbb Z^{42}\oplus(\mathbb Z/3\mathbb Z)^8\) and \(\widetilde H_3(M_9;\mathbb Z)\cong\mathbb Z^{70}\), which does not determine the nonfree quotient groups. Jonsson (2012), *Exact Sequences*, treats the unquotiented matching complexes. Jonsson (2012), *More Torsion*, considers invariant or symmetrized **chain subcomplexes** under group actions, which are not generally the integral cellular chains of a geometric quotient when simplex stabilizers permute its vertices. The published cycle-type fixed-point classification provides fixed-space information for complete-graph matching complexes; it does not supply the present geometric orbit-chain Smith invariants. The finite-case computation here depends on keeping all barycentric flag orbits and their integral incidence multiplicities. Armstrong (1965) provides the fundamental-group implication but not the higher integral homology computation.

## Limitations

This is one exact nine-point case, not an infinite-family theorem. It establishes integral homology and the fundamental group, not the complete homotopy or cohomology-ring type. Finding no equivalent earlier geometric quotient computation in the inspected sources does not establish exhaustive publication novelty; obscure unpublished or unindexed classifications remain possible. Independent validation has not been performed.

## References

1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1 (first public 2004-09-03), https://arxiv.org/pdf/math/0409054.
2. J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, arXiv:1203.5641v1 (2012-03-26), https://arxiv.org/pdf/1203.5641.
3. J. Jonsson, *More Torsion in the Homology of the Matching Complex*, arXiv:1203.5658 (first public 2012-03-26), https://arxiv.org/pdf/1203.5658.
4. M. A. Armstrong, *On the fundamental group of an orbit space*, Proc. Cambridge Philos. Soc. **61** (1965), 639–646, doi:10.1017/S0305004100038974.
5. *Cycle-type geometric fixed points of complete-graph matching complexes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-cycle-type-geometric-fixed-points-of-complete-graph-matching-com--790f558ef1ba.
