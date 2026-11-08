# Projective suspensions in half-turn quotients of bounded-independence cycle spheres

## Finding
For every integer \(d\ge2\), let \(X_d=BI_d(C_{2d})\) be the simplicial complex whose faces are those subsets of the vertices of the cycle \(C_{2d}\) containing no independent set of cardinality \(d\). Let \(h\) be the central half-turn \(h(i)=i+d\pmod {2d}\), and set \(Q_d=|X_d|/\langle h\rangle\), the **geometric orbit space**. Define
\[
(p_d,q_d)=\begin{cases}(d-2,d),&d\text{ even},\\(d-1,d-1),&d\text{ odd}.\end{cases}
\]
There is a homeomorphism
\[
Q_d\cong\begin{cases}\mathbb {RP}^{1},&d=2,\\S^{p_d-1}*\mathbb {RP}^{q_d-1},&d\ge3,\end{cases}
\]
where \(*\) denotes the topological join. Equivalently, for \(d\ge3\), \(Q_d\) is the \(p_d\)-fold **unreduced** suspension of \(\mathbb {RP}^{q_d-1}\). In particular, all reduced integral homology groups vanish except
\[
\widetilde H_{2d-3}(Q_d;\mathbb Z)\cong\mathbb Z,
\quad
\widetilde H_{p_d+2j+1}(Q_d;\mathbb Z)\cong\mathbb Z/2
\quad(0\le j\le(q_d-4)/2),
\]
with the latter range empty for \(q_d=2\). The cases \(d=2,3\) are circles and three-spheres, respectively. Integral torsion first occurs at \(d=4\), and its number of nonzero degrees increases without bound as \(d\) increases.

## Assumptions and scope
The undirected simple cycle has vertex set \(\mathbb Z/(2d)\) and edges between residues differing by one. An independent set contains no adjacent vertices. The bounded-independence complex \(BI_d\) uses the strict inequality \(\alpha(C_{2d}[F])<d\). The group action on the *geometric realization* is induced by vertex permutation. Quotients here are ordinary orbit spaces, not homotopy/Borel quotients. The source's nonequivariant sphere homotopy calculation and the general rational orientation character of dihedral symmetries are prior results; this theorem identifies the exact quotient homeomorphism and integral torsion.

## Proof
Put \(A=\{0,2,\dots,2d-2\}\) and \(B=\{1,3,\dots,2d-1\}\). Every independent \(d\)-set of \(C_{2d}\) must alternate around the cycle: the \(d\) cyclic gaps between its selected vertices are each at least two, but total \(2d\), so all gaps are exactly two. Consequently the only such sets are \(A\) and \(B\). Hence, as an actual simplicial complex (not merely up to homotopy),
\[
X_d=\partial\Delta_A^{d-1}*\partial\Delta_B^{d-1}.
\]
Realize each \((d-1)\)-simplex as the standard coordinate simplex in its augmented coordinate hyperplane \(U_A=\{x\in\mathbb R^A:\sum_{a\in A}x_a=0\}\) and \(U_B\) analogously. Radial projection from the barycenter gives a vertex-permutation-equivariant homeomorphism \(|\partial\Delta_A|\cong S(U_A)\), and similarly for \(B\). Joining these maps gives the explicit \(h\)-equivariant homeomorphism \(|X_d|\cong S(U_A\oplus U_B)\). The half-turn is orthogonal on this sphere.

If \(d\) is even, \(h\) preserves \(A\) and \(B\), acting as \(d/2\) disjoint transpositions on each shore. Thus the full real permutation space has \(d\) positive and \(d\) negative dimensions. Passing to \(U_A\oplus U_B\) removes two positive constant vectors, leaving \(p_d=d-2\) positive and \(q_d=d\) negative dimensions. If \(d\) is odd, \(h\) exchanges \(A\) and \(B\) through \(d\) disjoint transpositions. It has \(d\) positive and \(d\) negative dimensions in the full permutation space, and the two-dimensional constants-on-shores space decomposes as one positive and one negative eigenline; thus \(p_d=q_d=d-1\).

Choose an orthogonal decomposition \(U_A\oplus U_B=W_+\oplus W_-\) into these eigenspaces. The unit sphere decomposes as a topological join \(S(W_+)*S(W_-)\), with \(h\) the identity on the first sphere and the antipodal map on the second. Quotienting gives \(S^{p_d-1}*\mathbb{RP}^{q_d-1}\) whenever \(p_d>0\), while for \(p_d=0\) it is \(\mathbb{RP}^{q_d-1}\). This proves the claimed homeomorphisms, with the sole \(p_d=0\) instance at \(d=2\).

Since \(q_d\) is even, \(\mathbb{RP}^{q_d-1}\) has integral reduced homology \(\mathbb Z/2\) in precisely odd degrees \(1,3,\dots,q_d-3\), and \(\mathbb Z\) in degree \(q_d-1\), with no other nonzero reduced groups. The suspension homology isomorphism shifts degrees by \(p_d\), proving the stated groups. At \(d=2\), \(\mathbb{RP}^1\cong S^1\), consistent with the same formula. The smallest possible \(q_d\ge4\) occurs at \(d=4\); as \(q_d\) grows the number of odd interior degrees grows without bound.

## Verification
A standalone exact-arithmetic verifier, `verify.py`, enumerates every maximum independent set of \(C_{2d}\) for \(2\le d\le8\) and obtains exactly \(A,B\). It constructs the integral permutation matrix on a basis of \(U_A\oplus U_B\), verifies involution and determinant, and computes its rational \(+1\) and \(-1\) eigenspace dimensions by exact ranks. The output `verification_output.txt` records all seven cases and `ALL_VERIFY_OK`. These computations check finite instances; the all-parameter claim is established by the independent preceding proof.

## Relationship to prior work
Carnero Bravo [1] defines bounded-independence complexes and establishes the nonequivariant cycle homotopy sphere result (see especially §5.3, Theorem 38 and Corollary 39). Existing dihedral orientation-character calculations [2] establish that rotations act trivially on rational top homology and give rational-quotient information. That rational representation does not determine the present geometric half-turn quotient, its exact homeomorphism to a projective suspension, or its integral \(2\)-torsion. The standard orthogonal sphere and real-projective-space constructions used in the proof are classical; the statement concerns their specific equivariant realization by bounded-independence cycle complexes and the resulting complete quotient classification.

## Limitations
Only the central half-turn of \(C_{2d}\) at the threshold \(n=2d\) is treated. Other rotations and reflections, powers of cycles, and larger lengths are not covered. The homeomorphism describes the geometric quotient, not the homotopy quotient. Independent mathematical audit has not been performed.

## References
[1] A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first made public 2026-02-24; §3 and §5.3.

[2] *Dihedral orientation characters of bounded-independence spheres on cycles*, published mathematical research record, 2026-10-11, identifier `2026/10/11/SCOPE-dihedral-orientation-characters-of-bounded-independence-spheres--8a099ca44501`.

[3] A. Hatcher, *Algebraic Topology*, Chapter 2, the classical integral homology of real projective spaces and suspension isomorphism.
