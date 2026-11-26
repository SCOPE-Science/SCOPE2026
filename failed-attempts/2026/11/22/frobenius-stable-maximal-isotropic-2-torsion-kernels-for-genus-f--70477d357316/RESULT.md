# Frobenius-stable maximal isotropic 2-torsion kernels for genus-four hyperelliptic Jacobians

## Finding
For any smooth genus-four hyperelliptic curve \(C/\mathbb F_q\) with \(q\) odd, the Galois-stable maximal isotropic subgroup schemes of \(J[2]\), \(J=\operatorname{Jac}(C)\), are classified **numerically** solely by the Frobenius cycle type on the ten geometric Weierstrass points. Every geometric maximal isotropic subgroup is an \(\mathbb F_2\)-vector space of rank four, hence has order \(16\). There are exactly
\[
\prod_{i=1}^4(2^i+1)=3\cdot5\cdot9\cdot17=2295
\]
of them. The complete table gives, for each cycle partition \(\lambda\), both the number \(\#J[2](\mathbb F_q)\) of rational two-torsion points and the number of Frobenius-stable maximal isotropic subgroups. **The latter counts subgroup schemes defined over the base field, not subgroups whose individual points are all rational.**

| Frobenius cycle partition \(\lambda\) | \(\#J[2](\mathbb F_q)\) | Rational maximal isotropic kernels |
|:--|--:|--:|
| \(10\) | 1 | 1 |
| \(9,1\) | 1 | 0 |
| \(8,2\) | 2 | 1 |
| \(8,1,1\) | 2 | 1 |
| \(7,3\) | 1 | 0 |
| \(7,2,1\) | 2 | 2 |
| \(7,1,1,1\) | 4 | 6 |
| \(6,4\) | 2 | 1 |
| \(6,3,1\) | 2 | 0 |
| \(6,2,2\) | 4 | 7 |
| \(6,2,1,1\) | 4 | 3 |
| \(6,1,1,1,1\) | 8 | 3 |
| \(5,5\) | 1 | 5 |
| \(5,4,1\) | 2 | 0 |
| \(5,3,2\) | 2 | 0 |
| \(5,3,1,1\) | 4 | 0 |
| \(5,2,2,1\) | 4 | 0 |
| \(5,2,1,1,1\) | 8 | 0 |
| \(5,1,1,1,1,1\) | 16 | 0 |
| \(4,4,2\) | 4 | 11 |
| \(4,4,1,1\) | 4 | 11 |
| \(4,3,3\) | 2 | 3 |
| \(4,3,2,1\) | 4 | 0 |
| \(4,3,1,1,1\) | 8 | 0 |
| \(4,2,2,2\) | 8 | 7 |
| \(4,2,2,1,1\) | 8 | 7 |
| \(4,2,1,1,1,1\) | 16 | 15 |
| \(4,1,1,1,1,1,1\) | 32 | 15 |
| \(3,3,3,1\) | 4 | 0 |
| \(3,3,2,2\) | 4 | 9 |
| \(3,3,2,1,1\) | 8 | 9 |
| \(3,3,1,1,1,1\) | 16 | 45 |
| \(3,2,2,2,1\) | 8 | 0 |
| \(3,2,2,1,1,1\) | 16 | 0 |
| \(3,2,1,1,1,1,1\) | 32 | 0 |
| \(3,1,1,1,1,1,1,1\) | 64 | 0 |
| \(2,2,2,2,2\) | 16 | 151 |
| \(2,2,2,2,1,1\) | 16 | 39 |
| \(2,2,2,1,1,1,1\) | 32 | 39 |
| \(2,2,1,1,1,1,1,1\) | 64 | 135 |
| \(2,1,1,1,1,1,1,1,1\) | 128 | 135 |
| \(1,1,1,1,1,1,1,1,1,1\) | 256 | 2295 |

A \(10\)-cycle has one rational maximal isotropic kernel although \(J[2](\mathbb F_q)\) is trivial. A \(9,1\)-cycle has no such kernel and the same trivial rational two-torsion; \(5,1,1,1,1,1\) has sixteen rational two-torsion points but no stable maximal isotropic kernel. These contrasts show that neither the rational two-torsion cardinality nor the cycle length alone determines descent of a maximal isotropic subgroup.

## Assumptions and scope
The base field is \(\mathbb F_q\), with odd characteristic, and the curve is smooth, hyperelliptic, and of genus four. Its branch divisor on \(\mathbb P^1\) consists of ten distinct geometric points; these may include the point at infinity in an odd-degree model. The Frobenius element acts as a permutation \(\sigma\in S_{10}\), defined up to conjugacy. A rational maximal isotropic *kernel* means an étale \(\mathbb F_q\)-subgroup scheme \(K\subseteq J[2]\) whose geometric points form a maximal isotropic four-dimensional \(\mathbb F_2\)-subspace for the Weil pairing. Such a kernel defines a polarized \(2\)-isogeny \(J\to J/K\) of degree \(16\), with a descended principal polarization on the quotient. The quotient need not be a Jacobian. The results apply only to Frobenius types which actually arise for the specified curve; no universal realization assertion is made.

## Proof
**1. The canonical symplectic model.** Put \(E=\{x\in\mathbb F_2^{10}:\sum_{i=0}^9x_i=0\}\) and \(\mathbf 1=(1,\ldots,1)\). The classical Weierstrass-divisor description gives a Galois-equivariant identification
\[
J[2](\overline{\mathbb F}_q)\cong V=E/\langle\mathbf 1\rangle.
\]
This vector space has dimension \(8\). The Weil pairing is the symplectic form \(\langle [x],[y]\rangle=\sum_i x_i y_i\pmod2\); it is well defined because both representatives have even support. Frobenius permutes the ten coordinates. The subgroup scheme \(K\) descends precisely when its geometric subspace of \(V\) is preserved by this permutation.

**2. Canonical coordinates and exact representation.** Each class in \(V\) has a unique even-subset representative whose ninth coordinate is zero. Encode it by an integer \(v\in\{0,\ldots,255\}\) recording the first eight coordinates; the eighth coordinate is the parity of their sum. In these coordinates,
\[
\langle a,b\rangle=\operatorname{parity}(a\mathbin{\&}b)+\operatorname{parity}(a)\operatorname{parity}(b)\pmod2.
\]
Here the symbol \(\&\) denotes bitwise intersection of supports. To apply \(\sigma\), reconstruct the even ten-bit vector, permute its coordinates, complement all ten coordinates if the ninth bit is one, then retain the first eight. This provides the full exact linear action of Frobenius on \(V\).

**3. Exhaustive enumeration of all maximal isotropic subspaces.** A subspace \(U\le V\) is encoded by a 256-bit membership integer. Starting with \(\{0\}\), extend each isotropic subspace of dimension \(d\) by every \(v\notin U\) orthogonal to \(U\), adjoining its coset \(v+U\), and deduplicate identical subspaces. The dimension-by-dimension counts are
\[
(1,255,5355,11475,2295),\qquad d=0,1,2,3,4.
\]
The recursion is exhaustive: every nonzero totally isotropic subspace contains a codimension-one totally isotropic subspace; adjoining any omitted vector recovers it. The final dimension four is maximal because \(V\) is symplectic of dimension eight. As a separate certificate, enumerate all reduced-row-echelon \(4\times8\) binary matrices, test pairwise isotropy of their four generating rows, and turn each into its sixteen-element span. Exactly \(200787\) reduced-row-echelon matrices are tested, and the resulting set of \(2295\) subspaces agrees *element for element* with the extension enumeration.

**4. Frobenius invariance in each conjugacy class.** Integer partitions of ten give exactly \(42\) conjugacy classes of \(S_{10}\). For a representative permutation of each partition, calculate its action on all 256 elements of \(V\) by Step 2; count a listed isotropic subspace \(U\) precisely when the image of each of its sixteen members lies in \(U\). Count fixed individual vectors separately to obtain the middle column. The complete 42-row table results. Conjugating the permutation conjugates its action on subspaces, leaving the count unchanged, so a representative per partition suffices. The standalone verifier also tests three nontrivial conjugates per type. Therefore the table applies to every Frobenius action on the ten geometric branch points.

**5. Isogeny interpretation.** Because \(q\) is odd, \(J[2]\) is finite étale. A Frobenius-stable maximal isotropic geometric subspace corresponds uniquely to a rational subgroup scheme. The standard descent of principal polarizations along maximal isotropic torsion quotients gives a principally polarized abelian fourfold \(J/K\) over \(\mathbb F_q\), with degree-\(16\) polarized isogeny from \(J\). No assertion about the quotient being a curve Jacobian follows from its polarization alone.

## Verification
Run `python3 verify_genus4_lagrangians.py` with Python 3.10 or later. The standalone standard-library script constructs the full even-subset Weil module, separately enumerates maximal isotropic subspaces by reduced-row-echelon matrices and recursive extensions, verifies equality, checks the expected \(42\) partition table, and verifies three conjugate representatives for each Frobenius type. It emits `GENUS4_HYPERELLIPTIC_2295_LAGRANGIAN_42_FROBENIUS_TYPES_VERIFIED_OK`. This script was executed successfully before inclusion; no finite experiments are used to extrapolate to field sizes, since the proof reduces every odd-characteristic case to one of the complete finite permutation classes.

## Relationship to prior work
Bruin–Doerksen, *The arithmetic of genus two curves with (4,4)-split Jacobians* (arXiv:0902.3480, first public 2009-02-19), §4, treats genus-two maximal isotropic subgroups and Galois-stable quadratic splittings of **six** Weierstrass points; its full-text §4 (pp. 9–11) does not provide genus-four 2295-kernel or 42-type counts. Bruin–Kulkarni, *On (2,2)-decomposable genus 4 Jacobians* (arXiv:2309.01959, 2023), studies special decompositions of genus-four Jacobians into abelian surfaces, not all degree-16 maximal isotropic two-torsion kernels or their full Frobenius spectrum; the full online text's introduction and §§2,7 were inspected. Related published calculations for a special genus-three Klein-four pencil give rational \((2,2,2)\)-kernels (135, 39, or 15) but operate in a six-dimensional symplectic module, so they do not imply the present genus-four, eight-dimensional table. These comparisons concern implications of statements, not merely different titles. The classical even-subset description of hyperelliptic two-torsion and the general polarization quotient theorem are not claimed to be new.

## Limitations
This is an explicit classification of rational **kernel subgroup schemes**, not pointwise rational kernels, and it does not prove all Frobenius cycle types occur over all finite fields. The result does not classify the isomorphism classes of the quotient principally polarized abelian fourfolds, nor assert they are Jacobians. The finite 42-case check is exhaustive because the group-theoretic reduction is proved; the verification is not an independent external audit. An unindexed preexisting character-table computation or more general published theorem could conceivably contain or imply this table; historical priority is provisional.

## References
- N. Bruin and K. Doerksen, *The arithmetic of genus two curves with (4,4)-split Jacobians*, arXiv:0902.3480, first public 2009-02-19, especially §4. https://arxiv.org/abs/0902.3480
- N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959, first public 2023-09-05, especially Introduction, §2 and §7. https://arxiv.org/abs/2309.01959
