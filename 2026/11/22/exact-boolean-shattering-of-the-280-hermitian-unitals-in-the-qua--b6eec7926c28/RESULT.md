# Exact Boolean shattering of the 280 Hermitian unitals in the quaternary projective plane

## Finding
Let \(P\) be the 21-point Desarguesian projective plane \(\operatorname{PG}(2,4)\), and let \(\mathcal U\) comprise its 280 nine-point Hermitian unitals. Treat each unital as a binary concept on the point set \(P\). A support \(S\subseteq P\) is shattered precisely when
\[
|S|\le 6\quad\text{and}\quad S\subseteq U\text{ for some }U\in\mathcal U.
\]
Its full shattered-support polynomial is
\[
\Phi_{\mathcal U}(z)=1+21z+210z^2+1330z^3+5880z^4+17640z^5+23520z^6.
\]
Thus \(\operatorname{VCdim}(\mathcal U)=6\). The corresponding simplicial complex is pure of dimension five, with exactly 23,520 facets. Each facet is a six-point subset of a *unique* unital. Within its unique containing unital, the three-point complement is either collinear (3,360 facets) or noncollinear (20,160 facets).

## Assumptions and scope
Take \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), encoded by \(0,1,t,t+1\) as \(0,1,2,3\). Points are nonzero vectors of \(\mathbb F_4^3\), up to nonzero scalar. A *unital* is a nine-point subset meeting each of the 21 projective lines in either one or three points; in this plane all such unitals are Hermitian. Alternatively, a unital is the zero locus of a nondegenerate Hermitian form, or the symmetric difference of three nonconcurrent projective lines. The 280 distinct unitals are the entire concept family, not an arbitrary selection or its Boolean linear span.

For \(S\subseteq P\), the set of traces is \(\{U\cap S:U\in\mathcal U\}\); shattering means that this set equals \(\mathcal P(S)\). The polynomial coefficient of \(z^k\) counts different shattered \(k\)-point supports, not labeled query orderings. No assertion is made for projective planes of other orders.

## Proof
**Finite incidence lemma.** The two standalone, independently formulated enumeration programs in this package establish the following complete finite statements directly over \(\mathbb F_4\). There are 21 points, 21 five-point lines and exactly 280 distinct unitals. Each five-point support contained in a unital is in exactly two unitals; each six-point such support is in exactly one. There are exactly 23,520 distinct six-point supports contained in a unital, and **each of those supports has all 64 Boolean traces** against the 280-unitals family. These are exact exhaustive computations, rather than sampling. The Python verifier constructs nondegenerate Hermitian forms from the 512 coefficient possibilities; the C++ verifier constructs unitals as differences of triples of nonconcurrent lines. The Python verifier also independently matches the two constructions pointwise. Both algorithms use elementary explicitly printed finite-field arithmetic and explore the entire declared finite domains.

If \(S\) is shattered, its all-positive trace requires \(S\subseteq U\) for some unital \(U\). If \(|S|\ge7\), choose six of its points and require these six positive and a seventh negative. The six points are contained in the unique unital \(U\), which also contains the seventh, a contradiction. Hence any shattered \(S\) has size at most six.

Conversely, suppose \(S\subseteq U\) and \(|S|\le6\). Extend \(S\) to a six-subset \(T\subseteq U\). The finite incidence lemma realizes every trace on \(T\); restriction to \(S\) realizes every trace on \(S\). Thus the criterion follows.

For the face numbers, all 21 singletons, all 210 pairs and all 1,330 triples occur in at least one unital. Four-point supports occur exactly when they do not contain four points of a line; since the 21 five-point lines contribute \(21\binom54=105\) distinct forbidden four-sets, their count is \(\binom{21}{4}-105=5880\). Every contained five-set is in two unitals and every contained six-set in one, giving respectively \(280\binom95/2=17640\) and \(280\binom96=23520\). The criterion proves no higher faces. Every face extends to a six-point face, so the complex is pure. For each unital, its nine points have 12 collinear triples (its 12 secant lines) and 72 noncollinear triples, yielding \(280\cdot12=3360\) and \(280\cdot72=20160\) maximal six-sets of the two incidence types (uniqueness prevents double counting).

## Verification
Run `python3 verify_hermitian.py` and compile/run `verify_triangles.cpp` with a conforming C++17 compiler. Both need only standard libraries. The Python program constructs each of 512 Hermitian matrices, filters nonzero determinant, determines its zero locus, compares to the independent line-triangle family and verifies exactly 64 distinct traces for every one of the 23,520 six-point supports. The C++ program generates the 21 points and lines independently, builds 280 unitals from triples of nonconcurrent lines, checks the full positive-incidence support census, the five-/six-subset multiplicities, and exactly 64 traces for every contained six-set. Both have explicit assertions that terminate unsuccessfully on mismatches. Their actual successful outputs are detailed in `VERIFICATION.md`.

The proof's computational lemma applies only to \(\operatorname{PG}(2,4)\); it does not infer a general statement about all finite Hermitian unitals, nor does it replace the proof of the unrestricted dimension bound by a finite search.

## Relationship to prior work
The classical 280 Hermitian unitals, their three-line symmetric-difference representation, and their connection with the Witt designs and binary incidence codes are established independently of this finding. De Bruyn and Gao (2019/2020), especially their §3, study parity intersections and code and pseudo-embedding structures; their 280-unitals count and representation are credited. Della Vedova, Pagani and Pianta (first online 19 November 2022), §5, explicitly list the 280 unitals in the complete classification of binary projective-plane ghosts and note that they are Hermitian. These results provide the concept set and some incidence information, but the inspected statements do not directly compute its entire \(2^k\)-trace shattering criterion, six-query local trace universality, or the face polynomial above. This is a comparison of mathematical implications, not an assertion that every historical source has been inspected.

## Limitations
This is a small exact finite theorem, not an all-field shattering classification and not a new classification of unitals. Its correctness rests in part on fully exhaustive, finite, independently replayable computations; no human-independent audit has been performed. Historical priority remains uncertain for unindexed work, for unpublished equivalent projections of the 280-by-21 incidence matrix, or for consequences that might be implicit in existing incidence tables. No homology groups or adaptive Littlestone dimension are claimed.

## References
1. B. De Bruyn and M. Gao, “On four codes with automorphism group \(P\Sigma L(3,4)\) and pseudo-embeddings of the large Witt designs,” *Designs, Codes and Cryptography* 88 (2020), 429–452. DOI: https://doi.org/10.1007/s10623-019-00690-1. Accessible accepted manuscript: https://biblio.ugent.be/publication/8669545/file/8669546.pdf.
2. M. L. Della Vedova, S. M. C. Pagani and S. Pianta, “Power sum polynomials and the ghosts behind them,” *Journal of Geometry* 114 (2023), article 1; first online 19 November 2022. https://link.springer.com/article/10.1007/s00022-022-00662-2.
