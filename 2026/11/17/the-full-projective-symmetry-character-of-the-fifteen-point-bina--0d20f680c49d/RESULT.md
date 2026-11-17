# The full projective symmetry character of the fifteen-point binary cap complex

## Finding
Let \(K\) be the simplicial complex of subsets of the fifteen projective points of \(\operatorname{PG}(3,2)\) containing no complete three-point projective line. Its natural symmetry group \(G=\operatorname{GL}_4(\mathbb F_2)\) has order \(20160\). The already established ordinary integral homotopy type is \(M(\mathbb Z/2,3)\vee\bigvee^{77}S^4\), so the only nonzero positive-degree rational homology is \(\widetilde H_4(K;\mathbb Q)\cong\mathbb Q^{77}\).

**Theorem.** The complete rational fourth-homology character \(\chi\) has precisely twelve distinct profiles, with triples \((\text{element order},\chi,\text{number of elements})\):
\[
\begin{array}{c|r|r}
\text{order}&\chi&\text{count}\\\hline
1&77&1\\2&-3&105\\2&5&210\\3&-1&112\\3&2&1120\\
4&-3&1260\\4&1&2520\\5&2&1344\\6&-1&1680\\6&0&3360\\
7&0&5760\\15&-1&2688
\end{array}
\]
In particular \(\sum_{g\in G}\chi(g)=0\). Hence \(\widetilde H_4(K;\mathbb Q)^G=0\) and all positive-degree rational homology of \(|K|/G\) vanishes. The involutions, order-three elements, order-four elements and order-six elements each split into character-distinguished families.

## Assumptions and scope
Identify the points with nonzero four-bit vectors, encoded by integers \(1,\ldots,15\). A projective line is \(\{a,b,a\oplus b\}\), where \(\oplus\) is binary XOR and \(a,b\) are distinct nonzero vectors. A face contains no such triple. The group acts by invertible binary-linear changes of coordinates. The quotient is the topological orbit space of the geometric realization. The known nonequivariant homotopy classification is used as a prior theorem, not newly inferred from finite character traces.

## Proof
**Underlying homology.** The published integral classification supplies \(\widetilde H_3(K;\mathbb Z)=\mathbb Z/2\), \(\widetilde H_4(K;\mathbb Z)=\mathbb Z^{77}\), and zero other reduced homology, by an integral discrete-Morse certificate. Over \(\mathbb Q\) only degree four survives.

**Finite chain formula.** For any element \(g\in G\), decompose its permutation of the fifteen nonzero vectors into disjoint cycles \(C_1,\ldots,C_t\). An invariant face is a union of these cycles. Let \(\mathcal A_g\) be the family of subsets \(J\subseteq\{1,\ldots,t\}\) such that \(\bigcup_{j\in J}C_j\) contains no projective line. The signed trace on an oriented simplex associated with an invariant face \(F\) is \((-1)^{|F|-1}\operatorname{sgn}(g|F)=(-1)^{|J|-1}\) when \(F\) uses \(|J|\) permutation cycles; the augmented empty simplex contributes \(-1\). The Hopf trace theorem therefore gives the exact identity
\[
\chi(g)=-\sum_{J\in\mathcal A_g}(-1)^{|J|}.
\]
Every term and sign is determined by an explicit finite incidence test; no geometric fixed-point homology assumption is used.

**Exhaustive group enumeration.** Every invertible four-by-four binary matrix is uniquely determined by an ordered independent quadruple \((a,b,c,d)\) of nonzero vectors, giving \(15\cdot14\cdot12\cdot8=20160\) matrices. The reproducible verifier constructs all these maps, tests every subset of their point-permutation cycles for the thirty-five line obstructions, and evaluates the displayed alternating sum. It obtains exactly the twelve profiles in the theorem. An independent calculation of the signed oriented-chain trace on one explicitly chosen group element in each of the twelve profiles agrees. Summing the distribution gives zero, establishing the stated character average.

**Quotient.** Rational homology of a finite-group quotient of a finite simplicial complex equals its invariant rational homology (use an equivariant barycentric subdivision and rational transfer). Thus the zero invariant line count proves reduced rational acyclicity of \(|K|/G\). This asserts neither contractibility nor integral acyclicity.

## Verification
Run `python3 verify.py` using Python 3 standard library in the same folder; it independently builds the thirty-five lines, the entire cap face set of \(3048\) nonempty simplices, and the complete invertible matrix group of order \(20160\). It checks the twelve character profiles, verifies the identity trace \(77\), checks the exact character average, and independently replays twelve oriented-chain traces. The last line is `CAP_GL4_CHARACTER_PASS`. Exact output is in `verification_output.txt`.

## Relationship to prior work
Forbes, Grannell and Griggs studied independent sets in Steiner triple systems, providing the classical finite-geometric combinatorial setting, not this homological symmetry character. The published fifteen-point binary cap-complex result establishes its integral homotopy type but expressly makes no assertion about complete automorphism-group action. The present theorem does not reclaim that nonequivariant classification; it determines the full \(20160\)-element degree-four character, including the symmetry quotient's rational homology. Related calculations for the ternary projective-plane cap complex involve a different finite geometry and representation.

## Limitations
The result concerns the rational character of fourth homology for exactly this finite projective geometry. It does not classify the integral \(G\)-lattice, integral quotient homology, or geometric fixed spaces of every subgroup. The existing homotopy theorem is required to isolate the fourth-degree character; finite trace enumeration alone would not prove absence of other rational homology. Matching unindexed equivariant literature remains a publication-priority risk. Independent validation of this new result has not been performed.

## References
1. A. D. Forbes, M. J. Grannell and T. S. Griggs, *Independent Sets in Steiner Triple Systems*, Ars Combinatoria **72** (2004), 161–169; first public journal record 31 July 2004; publisher article: https://combinatorialpress.com/ars-articles/volume-072-ars-articles/independent-sets-in-steiner-triple-systems/.
2. *A two-torsion Moore summand in the binary projective three-space cap complex* (2026), publicly available mathematical result with exhaustive integral Morse certificate. This provides the nonequivariant homotopy theorem used above.
3. A. Lew, *Spectral Gaps of Generalized Flag Complexes*, MSc thesis (2017), Section 6.2: definition and examples of projective cap simplicial complexes.
