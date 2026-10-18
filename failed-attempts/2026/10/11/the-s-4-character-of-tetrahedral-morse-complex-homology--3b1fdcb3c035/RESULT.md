# The \(S_4\)-character of tetrahedral Morse-complex homology
## Finding
Let \(\Delta^3\) be the closed tetrahedron and let \(\mathcal M(\Delta^3)\) denote its complex of discrete Morse matchings: vertices are primitive regular pairs in the face poset of \(\Delta^3\), and simplices are acyclic collections of pairwise disjoint regular pairs. Relabeling the four tetrahedron vertices gives a natural action of \(S_4\) on \(\mathcal M(\Delta^3)\).

For the cycle types \((1^4),(2,1^2),(2^2),(3,1),(4)\), respectively, the character of the induced action on fourth rational homology is
\[
\chi_{H_4}=(99,1,-1,0,-1).
\]
Equivalently, as a rational \(S_4\)-module,
\[
H_4(\mathcal M(\Delta^3);\mathbb Q)\cong
4S^{(4)}\oplus13S^{(3,1)}\oplus8S^{(2,2)}\oplus12S^{(2,1,1)}\oplus4S^{(1,1,1,1)}.
\]
Here \(S^\lambda\) denotes the irreducible Specht module indexed by the partition \(\lambda\vdash4\).

## Assumptions and scope
The action is the one induced by permuting the four vertices of the abstract tetrahedron. Homology is taken with rational coefficients. The statement concerns the natural \(S_4\)-representation on the unique nonzero reduced rational homology group; it does not assert an equivariant wedge decomposition of the space itself.

## Proof
There are \(28\) primitive regular pairs in the Hasse diagram of \(\Delta^3\). Exhaustive enumeration of acyclic collections gives the face vector
\[
(28,300,1544,3932,4632,2128,256).
\]
A deterministic acyclic matching on the face poset of \(\mathcal M(\Delta^3)\) has one critical \(0\)-cell, two critical \(3\)-cells, and \(101\) critical \(4\)-cells. Its signed Morse differential from dimension \(4\) to dimension \(3\) is a \(2\times101\) integer matrix containing a \(2\times2\) minor of determinant \(-1\). Hence the matrix has Smith invariants \((1,1)\), so
\[
H_0\cong\mathbb Z,\qquad H_4\cong\mathbb Z^{99},
\]
and every other integral homology group vanishes.

For each conjugacy-class representative \(g\in S_4\), compute the signed trace of \(g\) on every simplicial chain group. A simplex contributes only when its set of primitive regular pairs is preserved setwise; its contribution is the sign of the induced permutation of its ordered vertices. The resulting chain traces in dimensions \(0\) through \(6\) are
\[
\begin{array}{c|rrrrrrr}
(1^4)&28&300&1544&3932&4632&2128&256\\
(2,1^2)&6&6&-20&-38&-4&20&8\\
(2^2)&0&-8&0&8&0&0&0\\
(3,1)&1&0&2&2&0&1&1\\
(4)&0&0&0&0&0&0&0
\end{array}.
\]
By equivariant Euler--Poincaré, the alternating sum of each row equals the alternating trace on homology. Since \(H_0\) is the trivial representation and reduced homology is concentrated in degree \(4\), subtracting the \(H_0\)-trace gives
\[
(99,1,-1,0,-1).
\]
Taking inner products with the five irreducible characters of \(S_4\), whose class sizes are \((1,6,3,8,6)\), gives multiplicities \((4,13,8,12,4)\), proving the decomposition.

## Verification
The accompanying `verify.py` reconstructs \(\Delta^3\), enumerates all \(12{,}820\) nonempty simplices of its Morse complex, checks the published face vector, verifies all \(58{,}680\) Hasse covers in the auxiliary acyclic matching, reconstructs the signed Morse differential, finds a unit full-rank minor, computes the five signed chain-trace vectors, and decomposes the resulting character using the irreducible character table of \(S_4\). A successful replay ends with `TETRA_S4_VERIFY_OK`; `verify_output.txt` records one such replay.

## Relationship to prior work
Donovan--Lin--Scoville identified \(\Delta^3\) as a small case whose Morse-complex homotopy type was still elusive and placed the subject in primary MSC \(55U05\). Chari--Joswig had earlier computed the face vector and integral homology. Scoville subsequently determined the nonequivariant homotopy type \(\mathcal M(\Delta^3)\simeq\bigvee^{99}S^4\). Lin--Scoville determined automorphism groups of Morse complexes, so the natural tetrahedral symmetry is canonical. The sources inspected for those results do not state the character of the action on \(H_4\) or its irreducible decomposition.

## Limitations
The result is an equivariant homology calculation, not a classification of the \(S_4\)-equivariant homotopy type. It does not specify a symmetry-compatible basis of the \(99\) sphere classes over \(\mathbb Z\), nor does it determine analogous representations for \(\Delta^n\) with \(n\ge4\). Originality is supported by the explicit source comparisons and database searches recorded in `AUDIT.json`, not by an assertion of exhaustive literature coverage.

## References
1. C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440, first submitted 2019-09-25.
2. M. K. Chari and M. Joswig, *Complexes of discrete Morse functions*, arXiv:math/0011234; Discrete Mathematics 302 (2005), 39--51.
3. M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907; Advances in Applied Mathematics 131 (2021), 102250.
4. N. A. Scoville, *The complex of discrete Morse matchings of the \(n\)-simplex: homotopy types and structural results*, arXiv:2604.18172, first submitted 2026-04-20.
