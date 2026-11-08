# The antipodal scale-two four-cube Rips quotient is \(\mathbb{RP}^3\vee\bigvee^4 S^3\)

## Finding
Let \(Q_4=\{0,1\}^4\) carry Hamming distance, let \(K=\operatorname{VR}(Q_4;2)\) be the inclusive diameter-two Vietoris–Rips complex, and let \(\iota(x)=x+(1,1,1,1)\) denote bitwise complementation. Then the **actual geometric orbit space** satisfies
\[
|K|/\langle\iota\rangle\simeq\mathbb{RP}^{3}\vee\bigvee^{4}S^{3}.
\]
In particular its fundamental group is \(\mathbb Z/2\), its second homotopy group vanishes, and its integral homology is \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z/2\), \(H_3\cong\mathbb Z^5\), with all other integral homology groups zero.

## Assumptions and scope
Represent each binary vertex by an integer from 0 to 15 (least significant bit first); bitwise complementation is the XOR operation with 15. A nonempty collection of vertices is a simplex if and only if the Hamming distance between every pair is at most two. Define \(E\subset Q_4\) as the eight even-Hamming-weight vertices. All quotient spaces are geometric, not naïve simplicial quotients on vertex orbits; the action is free on every geometric simplex because no two complementary vertices are joined by an edge. Only this four-cube and scale two are asserted.

## Proof
**1. A canonical projective subcomplex.** Among distinct even-parity vertices the distance is exactly two, except complementary pairs, which have distance four. Thus the induced full subcomplex \(K[E]\) is the join of four two-point sets, namely the boundary of the four-dimensional cross-polytope, \(S^3\). The involution swaps the endpoints of all four opposite pairs; under the standard cross-polytope realization this is \(-I\) on its ambient \(\mathbb R^4\). Hence \(A=|K[E]|/\langle\iota\rangle\) is the standard real projective three-space \(\mathbb{RP}^3\), embedded as a CW subcomplex of the quotient \(Y=|K|/\langle\iota\rangle\).

**2. A regular orbit-CW structure.** If a simplex contains both \(x\) and \(\iota(x)\), its diameter is at least four, contradicting the scale. Therefore the involution acts freely on cells. Distinct proper codimension-one faces of any simplex lie in different involution orbits (else an antipodal pair would lie together in the simplex); consequently the geometric orbit has a regular CW face poset obtained by passing to orbits of nonempty simplices. The full simplicial face vector, by ascending dimension, is \((16,80,160,120,16)\). The quotient orbit-CW vector is \((8,40,80,60,8)\). The subcomplex \(A\) has orbit-CW vector \((4,12,16,8,0)\).

**3. Exact relative discrete-Morse certificate.** Encode a face by the integer mask with bit \(v\) set exactly when vertex \(v\) is present. The involution sends its mask to the mask obtained by replacing every set vertex \(v\) by \(v\oplus15\). An orbit is represented by the lesser of those two masks. The accompanying `matching.json` gives **76 explicit pairs** (a lower-dimensional orbit cell and a codimension-one coface orbit cell), all in \(Y\setminus A\), and the four critical relative cell masks. The companion `verify.py` reconstructs all 392 nonempty simplices, all 196 orbit cells and their 600 face incidences, checks the pairs are disjoint actual cover incidences, reverses exactly the matched cover arrows, and confirms that the resulting full 196-vertex directed Hasse graph is acyclic. The matching has lower-cell dimension counts \((4,24,40,8)\) for dimensions zero through three. The only unmatched cells outside \(A\) are four three-cells, represented by hexadecimal masks `0x96`, `0x303`, `0x505`, and `0x2092`.

**4. Relative Morse reduction and attaching maps.** Relative discrete Morse theory for a finite regular CW pair, with no cells of \(A\) matched, gives a homotopy equivalence under \(A\) from \(Y\) to a CW complex formed from \(A\) by attaching precisely four three-cells. Each attaching map has domain \(S^2\) and lands in \(A=\mathbb{RP}^3\), whose universal cover is \(S^3\); therefore \(\pi_2(A)=0\), so all four maps are nullhomotopic. The resulting space is \(A\vee\bigvee^4 S^3\), proving the stated homotopy equivalence. These are finite exhaustive checks for a single fixed complex, rather than finite samples from a larger parameter family.

## Verification
Run `python verify.py` in a directory containing the included `matching.json`. No external Python packages or network requests are needed. The program reconstructs the combinatorial quotient rather than trusting recorded f-vectors, checks all 76 matching pairs and the global acyclicity of the matching, verifies four relative critical three-cells, and independently reduces the signed orbit boundary operators modulo two and three. The checked boundary ranks in dimensions one through four are respectively \((7,32,47,8)\) modulo two and \((7,33,47,8)\) modulo three. These modular checks support, but are not used as substitutes for, the integral homotopy argument from the complete discrete-Morse certificate and the projective subcomplex.

## Relationship to prior work
Adamaszek–Adams (2021) proved the **unquotiented** scale-two hypercube Rips complexes are wedges of three-spheres (nine spheres at the four-cube). Feng (2023) explains this result and studies scale three. Bendersky–Elia–Grbić (first posted May 1, 2026) analyze cohomological properties of the original Rips complex, while Galetto–Montaño–Wellner (first posted June 18, 2026) determine rational hyperoctahedral homology representations at scale two. Character restriction can recover rational invariant ranks but does not by itself determine the geometric quotient's fundamental group, integral two-torsion, or wedge splitting with \(\mathbb{RP}^3\). This finding identifies the **actual quotient's full homotopy type**, not simply the invariant part of the upstairs homology.

## Limitations
The result is for the four-dimensional binary cube at inclusive scale two and its full bitwise-complement involution. It does not classify all dimensions, other scales, homotopy fixed points, Borel quotients, or other subgroup actions. It is a proof with an exact finite CW matching certificate, not an independently validated publication claim.

## References
- M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first public March 1, 2021), https://arxiv.org/abs/2103.01040.
- Z. Feng, *Homotopy types of Vietoris–Rips complexes of hypercube graphs*, arXiv:2305.07084 (first public May 11, 2023), https://arxiv.org/abs/2305.07084.
- M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips complex of a hypercube graph*, arXiv:2605.00705 (first public May 1, 2026), https://arxiv.org/abs/2605.00705.
- F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first public June 18, 2026), https://arxiv.org/abs/2606.20784.
