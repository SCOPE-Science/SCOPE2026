# Reflection quotients of path independence complexes as projective suspensions

## Finding
Let \(P_n\) be the path graph on vertices \(1,\ldots,n\), with \(n\geq1\), and let \(\tau(i)=n+1-i\). Write \(K_n=\operatorname{Ind}(P_n)\) for the simplicial complex of nonadjacent vertex sets and \(Q_n=|K_n|/\langle\tau\rangle\) for the **ordinary geometric orbit space**. Define \((a_n,b_n)\) at the noncontractible path lengths by
\[
(a_n,b_n)=\begin{cases}
(k,k),&n=6k,\ k\geq1,\\
(k,k+1),&n=6k+2,\ k\geq0,\\
(k+1,k),&n=6k+3,\ k\geq0,\\
(k+1,k+1),&n=6k+5,\ k\geq0.
\end{cases}
\]
Then the **complete integral homotopy classification** of the reversal orbit spaces is
\[
Q_n\simeq\begin{cases}
\{\mathrm{point}\},&n\equiv1\pmod3\text{ or }n=2,\\
S^0,&n=3,\\
S^{a_n-1}*\mathbb{RP}^{b_n-1},&\text{all remaining }n.
\end{cases}
\]
Here \(*\) is the topological join. In the last case \(a_n,b_n\geq1\); equivalently this join is the \(a_n\)-fold unreduced suspension of \(\mathbb{RP}^{b_n-1}\). More strongly, \(|K_n|\) is **equivariantly homotopy equivalent** to the unit representation sphere \(S(\mathbb R^{a_n}_{+}\oplus\mathbb R^{b_n}_{-})\), where reversal is \(+1\) on the first summand and \(-1\) on the second. If \(n\equiv1\pmod3\), the complex has an equivariant contraction to a fixed point.

In particular,
\[
Q_{14}\simeq\Sigma^2\mathbb{RP}^{2},\qquad
\widetilde H_3(Q_{14};\mathbb Z)\cong\mathbb Z/2,
\]
with all other reduced integral homology zero. At \(n=20\), \(Q_{20}\simeq\Sigma^3\mathbb{RP}^{3}\), with \(\widetilde H_4\cong\mathbb Z/2\) and \(\widetilde H_6\cong\mathbb Z\). More generally the number of nonzero integral two-torsion homology degrees of these quotients is unbounded.

## Assumptions and scope
All path graphs are finite and simple. Independence means a subset with no adjacent pair of vertices. A geometric orbit space is the quotient of the usual realization, **not** a homotopy/Borel quotient. Homotopy equivalences are ordinary unless marked equivariant. The fixed-point set is that of the induced geometric involution, not merely the induced subcomplex of individually fixed vertices. The empty path is used only as the identity for simplicial joins in the six-vertex recurrence; no assertion about its geometric realization is required.

## Proof
**1. Two symmetric folds.** For \(n\geq6\), define a vertex map on \(K_n\) by
\[
f_n(3)=1,\qquad f_n(n-2)=n,\qquad f_n(i)=i\ \text{otherwise}.
\]
For an independent face \(\sigma\), the presence of vertex \(3\) excludes \(2\), so adding \(1\) does not violate independence. Likewise, the presence of \(n-2\) excludes \(n-1\), so adding \(n\) preserves independence. The two ends do not interfere for \(n\geq6\). Thus \(\sigma\cup f_n(\sigma)\) is independent; in particular \(f_n\) is a simplicial map and is contiguous to the identity. The map commutes with reversal because \(\tau(3)=n-2\), \(\tau(1)=n\). It fixes pointwise the induced subcomplex \(L_n\) obtained by deleting vertices \(3,n-2\), and its image lies in \(L_n\). The linear contiguity homotopy therefore gives an explicit \(C_2\)-equivariant strong deformation retract \(|K_n|\searrow|L_n|\).

**2. Equivariant six-step reduction.** The induced graph after these deletions is the disjoint union of a two-vertex edge on \(\{1,2\}\), the central path on \(\{4,\ldots,n-3\}\), and a two-vertex edge on \(\{n-1,n\}\). Therefore
\[
L_n=\operatorname{Ind}(P_2)*\operatorname{Ind}(P_{n-6})*\operatorname{Ind}(P_2),
\]
with the middle factor absent at \(n=6\). Each end factor is \(S^0\). Label the two points in the left end factor \(+\) and \(-\) by vertices \(1,2\), and in the right by \(n,n-1\). Reversal interchanges the factors while preserving their \(+/-\) labels. Their join is the unit circle of the two-dimensional swap representation, which has one positive and one negative eigenline. Hence, for \(n\geq7\), there is a natural equivariant homotopy equivalence
\[
|K_n|\simeq_{C_2}S(\mathbb R_{+}\oplus\mathbb R_{-})*|K_{n-6}|.
\]
For \(n=6\), the direct retract onto the two end factors is already \(S(\mathbb R_{+}\oplus\mathbb R_{-})\). Joining two unit representation spheres is equivariantly homeomorphic to the unit sphere of their orthogonal direct sum (with the standard join coordinates).

**3. Base cases.** At \(n=1\), \(K_1\) is a fixed point. At \(n=2\), it consists of two exchanged vertices, hence is \(S(\mathbb R_{-})\). At \(n=3\), its edge \(\{1,3\}\) collapses equivariantly onto its fixed midpoint, leaving two individually fixed points, so \(K_3\simeq_{C_2}S(\mathbb R_{+})\). At \(n=4\), the three edges \(\{1,3\},\{1,4\},\{2,4\}\) form an interval with reflection, equivariantly contractible to the midpoint of \(\{1,4\}\). At \(n=5\), the unique two-simplex \(\{1,3,5\}\) retracts, respecting reflection, onto its opposite edge \(\{1,5\}\), leaving the four-edge circle \(1-4-2-5-1\). Reflection exchanges \(1\leftrightarrow5\) and \(2\leftrightarrow4\), fixing the midpoints of two opposite edges. It is the standard reflection circle \(S(\mathbb R_{+}\oplus\mathbb R_{-})\).

**4. Induction and orbit spaces.** Each application of Step 2 adds one positive and one negative direction. Starting from the base cases at path lengths \(2,3,5,6\) gives the stated \((a_n,b_n)\) for all spherical cases. Starting from the fixed-point contractions at lengths \(1,4\), the same equivariant joins remain equivariantly contractible (a join with a contractible based factor admitting a fixed-point contraction contracts equivariantly). Thus the \(n\equiv1\pmod3\) cases have contractible quotients.

For \(a,b\geq1\), express the sphere \(S(\mathbb R^a_{+}\oplus\mathbb R^b_{-})\) as the join \(S^{a-1}*S^{b-1}\). The involution is trivial on the first factor and antipodal on the second, so its geometric orbit is **homeomorphic** to \(S^{a-1}*\mathbb{RP}^{b-1}\). An equivariant homotopy equivalence induces a homotopy equivalence on ordinary orbit spaces, proving the formula for \(Q_n\). At \(n=2\), the swapped two-point space has a point quotient; at \(n=3\), the two fixed components give \(S^0\).

**5. Integral consequence.** The cellular chain complex of \(\mathbb{RP}^m\) has one integral cell in each dimension \(0,\ldots,m\), with boundary multiplication by \(2\) in even positive degrees and \(0\) in odd degrees. Suspending \(a\) times shifts reduced integral homology by \(a\). At \((a,b)=(2,3)\) this gives exactly \(\widetilde H_3\cong\mathbb Z/2\). At \((a,b)=(3,4)\) it gives \(\widetilde H_4\cong\mathbb Z/2\) and \(\widetilde H_6\cong\mathbb Z\). As \(b_n\) grows, the number of odd interior degrees of \(\mathbb{RP}^{b_n-1}\) with \(\mathbb Z/2\) homology is unbounded.

## Verification
Execute `python3 verification/verify.py` using Python 3 and only its standard library. The supplied `verification/verification_output.txt` is the captured output. The program enumerates every independent face for \(2\leq n\leq24\), tests the equivariant contiguous fold on every independent face for \(6\leq n\leq24\), enumerates symmetric faces to calculate fixed-space Euler characteristics, and independently checks original and quotient Euler characteristics against the representation-sphere predictions. It reports `ALL_FINITE_CHECKS_PASSED`. These finite tests corroborate Steps 1 and 4 but do not prove the all-integer theorem; the structural equivariant argument does.

## Relationship to prior work
Ehrenborg and Hetyei [1], Section 6, prove that forest independence complexes are sphere-like or contractible and determine the ordinary path periodicity; their result does **not** determine the reversal orbit homotopy type or its integral torsion. Kawamura [2] also treats ordinary forest independence complexes. The published 2026 study *Path-reversal orientation of all higher-independence spheres* [3] determines the reversal action on the rank-one integral homology and hence rational quotient homology, but explicitly does not assert equivariant homotopy equivalences or integral orbit homology. The published *Reflection-fixed homotopy types of higher path-independence complexes* [4] gives geometric fixed loci, not a classification of ordinary orbit spaces. An independently published half-turn result on bounded-independence complexes of cycles [5] produces projective suspensions from a different simplicial join and does not give an equivariant map from those cycle complexes to the present path complexes. The new contribution is the equivariant six-step fold that identifies the entire ordinary reversal quotient of every path, including unbounded two-primary torsion.

## Limitations
The classification covers simple paths and their single reversal, not arbitrary forest automorphisms, graph cycles, higher-independence parameters, or general group actions. No homeomorphism between \(Q_n\) and the displayed joins is asserted, only a homotopy equivalence. The finite verification does not certify all values of \(n\). Equivalent literature not indexed in the searches could alter publication priority. Independent mathematical review has not been performed.

## References
1. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, especially Section 6, first available online 2005-11-28. DOI: 10.1016/j.ejc.2005.04.010. https://www.ms.uky.edu/~jrge/Papers/Independence.pdf
2. K. Kawamura, *Homotopy types of independence complexes of forests*, Contributions to Discrete Mathematics 5(2) (2010), 67–75, published 2010-09-28. DOI: 10.55016/ojs/cdm.v5i2.62064. https://cdm.ucalgary.ca/article/view/62064
3. *Path-reversal orientation of all higher-independence spheres*, published mathematical research record, 2026-10-25, especially its Findings, Proof and Limitations sections.
4. *Reflection-fixed homotopy types of higher path-independence complexes*, published mathematical research record, 2026-11-08, especially its Finding and Limitations sections.
5. *Projective suspensions in half-turn quotients of bounded-independence cycle spheres*, published mathematical research record, 2026-11-08, especially its Finding and Proof sections.
