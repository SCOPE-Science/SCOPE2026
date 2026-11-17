# The full symmetry quotient of the pentagonal-prism matching complex is a homotopy three-sphere

## Finding
Let \(P=C_5\square K_2\) be the ordinary pentagonal-prism graph and \(X=\mathcal M(P)\) its simplicial **ordinary matching complex**, containing every collection of pairwise vertex-disjoint edges. Its full graph automorphism group is \(G\cong D_5\times C_2\), with \(|G|=20\). Then the ordinary geometric orbit space has integral homotopy type
\[
\boxed{\ |X|/G\simeq S^3.\ }
\]
In particular, the quotient is simply connected and has no reduced integral homology except \(\widetilde H_3\cong\mathbb Z\). This is a homotopy equivalence, not an assertion that the orbit space is homeomorphic to a sphere.

## Assumptions and scope
Label the ten graph vertices by \((i,a)\), with \(i\in\mathbb Z/5\mathbb Z\) and \(a\in\{0,1\}\). The fifteen graph edges are ten pentagon-rim edges \(\{(i,a),(i+1,a)\}\) and five vertical spokes \(\{(i,0),(i,1)\}\). Define rotation, reflection and layer interchange by
\[
r(i,a)=(i+1,a),\quad s(i,a)=(-i,a),\quad t(i,a)=(i,1-a).
\]
These generate all automorphisms, since the five four-cycles are exactly the side squares: spokes lie in two squares and rim edges in one, so every automorphism preserves the spokes and the two rim cycles. The resulting action is \(D_5\times C_2\).

The vertex set of \(X\) consists of the fifteen graph edges, while every matching of size \(k\) is a simplex of dimension \(k-1\). All statements use the ordinary topological quotient of the geometric realization, not the homotopy orbit space or the perfect-matching subcomplex. Every nonempty face is enumerated; matchings of size six are impossible on ten graph vertices.

## Proof
**An admissible cellular quotient.** Barycentrically subdivide \(X\). A subdivision simplex is a nonempty strict chain \(F_0\subsetneq\dots\subsetneq F_d\) of matchings. Each group element preserves the face cardinalities; consequently, if it stabilizes such a chain setwise it fixes each chain vertex. There are no inversions. The orbits of chains therefore form an honest finite regular-orbit CW chain model, with one oriented cell for each orbit of flags. The orientation follows increasing face size; it is preserved under the action. The boundary of an oriented flag is the alternating sum of its deleted-subflag orbits, with repeated faces combined integrally.

**Exact enumeration.** Among the \(2^{15}\) edge subsets, precisely \(341\) nonempty subsets are matchings, with face counts \((15,75,145,95,11)\) by cardinality. Enumerating every nonempty strict face chain gives flag counts \((341,2680,5940,4920,1320)\). Passing to all twenty graph automorphisms produces the cell counts
\[
(c_0,c_1,c_2,c_3,c_4)=(35,188,357,276,72).
\]
A separate fixed-flag Burnside calculation yields the same five orbit counts. Every integral boundary composition vanishes exactly, not just modulo primes.

**Integral homology.** The complete boundary matrices undergo the \(463\) explicit unit-pivot cancellations in `certificate.json`, replayed by `verify_prism_quotient.py`. Their numbers by differential dimension \(1,2,3,4\) are respectively \((34,154,203,72)\). A pivot of coefficient \(\pm1\) permits an integral change of basis splitting off a contractible two-term free-chain summand; the residual differential is the exact Schur complement. All coefficients remain integers. The final free-chain complex has exactly one generator in degree zero and one in degree three and no differentials. Thus
\[
H_k(|X|/G;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0\text{ or }k=3,\\
0,&\text{otherwise}.
\end{cases}
\]
This calculation excludes torsion in every degree; rational Betti-number ranks alone would not do so.

**Fundamental group.** The one-skeleton has \(35\) vertices and \(188\) edges. The deterministic spanning tree in the certificate has \(34\) edges, leaving \(154\) non-tree edge generators for the fundamental-group presentation. Each of the \(357\) triangular two-cells supplies its oriented three-edge relator. In four rounds, the certificate gives relators that, after discarding generators previously shown trivial and freely reducing, each contain just one remaining generator with exponent \(\pm1\). The round sizes are \((97,36,17,4)\); all \(154\) generators are eliminated. Every witness relator is checked directly from the constructed quotient, proving \(\pi_1(|X|/G)=1\).

**Conclusion.** The quotient is a simply connected finite CW complex with the integral homology of \(S^3\). Hurewicz supplies a map \(S^3\to |X|/G\) inducing an isomorphism on degree-three homology; it is then a homology equivalence in every degree. The homological Whitehead theorem for simply connected CW complexes makes this a homotopy equivalence, as claimed.

## Verification
Run `python3 verify_prism_quotient.py` in the directory also containing `certificate.json`. The script uses the Python 3 standard library only. It exhaustively regenerates all faces and strict flags, checks the twenty induced edge permutations and Burnside orbit counts, assembles signed integer boundaries, verifies \(\partial^2=0\), checks each of the \(463\) integer unit pivots, and replays the spanning-tree and four-round triangular-relator proof of simple connectivity. `verification_output.txt` contains the output reproduced from these exact packaged files. Its final line is `INTEGRAL_PRISM_QUOTIENT_VERIFY_OK`.

For the rank checks it is essential to work over \(\mathbb Z\): a correct computation over \(\mathbb Q\) alone cannot exclude finite torsion. The unit-pivot certificate is a full integral homology proof for this finite cell complex, not a statistical sample. The noncomputational homotopy step invokes the stated classical theorems with their simply-connected hypotheses verified above.

## Relationship to prior work
Braun and Hough (arXiv:1606.01204v1, first public June 3, 2016) investigate matching complexes of **open** two-row grids, using a discrete-Morse framework. Their edge lists omit the closing rim edges of \(P\); their conclusions do not establish this closed prism's orbit-space homotopy type. The paper's introduction and graph definition were inspected in full text.

Two relevant previously available mathematical results determine \(\mathcal M(P)\simeq S^2\vee S^2\vee S^3\vee S^3\) and the full \(D_5\times C_2\) rational homology representation. The latter proves that the quotient has the **rational cohomology ring** of \(S^3\), but expressly does not determine its integral torsion, fundamental group or homotopy type. The theorem here upgrades that rational result by independent exact integral chain and fundamental-group certificates, rather than restating it.

The independence-complex formulation \(\operatorname{Ind}(L(P))\) is identical to the ordinary matching complex considered here; its automorphism quotient was included among the comparison formulations. Agarwal and Basak (arXiv:2608.30601, first public August 2026) study independence and **perfect-matching** complexes of Möbius and circular ladders. These are different simplicial objects from the ordinary matching complex; their accessible text does not give the asserted orbit-space classification. A mathematically equivalent unindexed result remains possible.

## Limitations
Only \(P=C_5\square K_2\) and the full graph-automorphism action are treated. No assertion is made for every circular ladder, for the separate rotation or reflection quotients, or for the homeomorphism type of this orbit space. This exact finite certificate proves a mathematical statement but does not establish publication priority or constitute independent external review. The closest published symmetry analysis is rational, and inaccessible or unindexed equivalent sources remain a novelty risk.

## References
1. B. Braun and W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, arXiv:1606.01204v1, June 3, 2016, https://arxiv.org/abs/1606.01204.
2. *Full rational symmetry modules of the pentagonal-prism matching complex*, public mathematical record, November 8, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-full-rational-symmetry-modules-of-the-pentagonal-prism-matching--a7af5f6df3e9/RESULT.md.
3. *The pentagonal-prism matching complex: a mixed sphere wedge and its symmetry*, public mathematical record, November 8, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-pentagonal-prism-matching-complex-a-mixed-sphere-wedge-and-i--9bb20a383389/RESULT.md.
4. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, September 2026, https://arxiv.org/abs/2608.30601.
5. T. Matsushita, *Matching Complexes of Small Grids*, Electron. J. Combin. 26 (2019), #P3.1, https://doi.org/10.37236/8480.
