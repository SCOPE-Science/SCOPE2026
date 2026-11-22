# Parallelism-sensitive VC-shattering in the affine plane of order four

## Finding
Let \(K=\mathbb F_2[\omega]/(\omega^2+\omega+1)\), and let \(X=K^2\), the sixteen points of \(\operatorname{AG}(2,4)\). Consider three Boolean point-membership concept classes consisting of unions \(L\cup M\) of **two distinct affine lines**, with the lines respectively (P) parallel, (N) nonparallel, or (A) unrestricted. For a concept class \(\mathcal H\), let
\[
\Phi_{\mathcal H}(z)=\sum_{S\subseteq X}\mathbf1_{\{\mathcal H\text{ shatters }S\}}z^{|S|}.
\]
Then the complete polynomials are
\[
\begin{aligned}
\Phi_{\rm P}(z)&=1+16z+120z^2+560z^3+1680z^4,\\
\Phi_{\rm N}(z)&=1+16z+120z^2+560z^3+1680z^4+2400z^5,\\
\Phi_{\rm A}(z)&=1+16z+120z^2+560z^3+1800z^4+3840z^5.
\end{aligned}
\]
Thus all three classes shatter every support of size at most three. Their VC dimensions are respectively \(4,5,5\).

**Exact support criteria.** For a four-element set \(Q\), call it an *additive parallelogram* when \(\sum_{p\in Q}p=0\) in \(K^2\). For any support \(S\), write \(B(S)\) for the existence of an additive-parallelogram four-subset; \(T(S)\) for the existence of three distinct points on an affine line; and \(F(S)\) for the existence of four points on an affine line. Then:

- \(\mathcal H_{\rm P}\) shatters \(S\) exactly when \(|S|\le4\) and \(\neg B(S)\).
- \(\mathcal H_{\rm N}\) shatters \(S\) exactly when either \(|S|\le4\) and \(\neg B(S)\), or \(|S|=5\), \(T(S)\), and \(\neg B(S)\).
- \(\mathcal H_{\rm A}\) shatters \(S\) exactly when either \(|S|\le4\) and \(\neg F(S)\), or \(|S|=5\), \(T(S)\), and \(\neg F(S)\).

In particular, the parallel-only and nonparallel-only families have **identical shattered four-supports**: exactly the \(1680\) affinely independent four-sets when \(K^2\) is viewed as a four-dimensional affine space over \(\mathbb F_2\). Nevertheless, the nonparallel class has \(2400\) shattered five-sets, while the parallel class has none. In the unrestricted class, exactly \(1440\) further five-supports and \(120\) further four-supports are shattered. These additional supports are controlled by additive parallelograms rather than merely the incidence of a single line.

## Assumptions and scope
The ground set consists only of the sixteen labeled points of \(K^2\); a query at a point is positive precisely when that point belongs to the union of the two lines. The two component lines must be distinct; they may or may not intersect according to P, N, A. A set \(S\) is shattered if all \(2^{|S|}\) Boolean traces \(C\cap S\) occur. There are exactly twenty lines, partitioned into five parallel classes of four lines. The three concept classes have respectively \(30\), \(160\), and \(190\) distinct concepts. This is a finite-order statement, not a uniform result for arbitrary finite-plane orders and not an assertion about Littlestone dimension.

## Proof
**1. Finite-field incidence model.** Represent \(K\) by the integers \(0,1,2,3\), with addition performed by componentwise binary XOR and \(2^2=3\), \(2\cdot3=1\), \(3^2=2\). Enumerate points lexicographically by \((x,y)\). The twenty lines are precisely \(y=mx+b\) for \(m,b\in K\) and \(x=c\) for \(c\in K\). Every unordered pair of points lies on exactly one of these lines, and two lines in the same slope class are disjoint. The source files `verify_affine.py` and `verify_incidence.py` implement this incidence model in two different ways.

**2. Certified exhaustive orbit reduction.** The eight permutations of \(X\) given by translations by \(1,\omega\) separately in each coordinate, multiplication of the first coordinate by \(\omega\), the shear \((x,y)\mapsto(x+y,y)\), coordinate interchange, and simultaneous Frobenius squaring preserve the twenty lines and the parallelism relation. Consequently they preserve all three concept classes and each class's shattering predicate. Starting from the lexicographically first unvisited \(k\)-set, close under these eight transformations; repeat until all \(\binom{16}{k}\) sets are partitioned. This exact finite group-action algorithm gives respectively \(1,1,1,2,4,5\) orbits in cardinalities \(0,1,2,3,4,5\). Orbit-size totals are verified against \(\binom{16}{k}\), and a representative's trace set is obtained directly by intersecting all \(30\), \(160\), or \(190\) line-union masks with it. The file `orbit_certificate.json` records every representative, orbit size, geometric signature, and all three trace masks. For extra protection against implementation error, both standalone implementations independently enumerate **every** support of size at most five and agree with the orbit results and the exact support criteria.

There are four orbits of four-sets, with sizes \(20,120,720,960\). The first orbit consists of all twenty complete affine \(K\)-lines; none is shattered by P, N, or A. The second consists of the \(120\) noncollinear four-point additive parallelograms; these are shattered by A but by neither P nor N. The remaining orbits (sizes \(720,960\)) are shattered by all three families. Thus the four-support counts are \(1680,1680,1800\). Independently, each triple of distinct points completes uniquely to the additive parallelogram with fourth point equal to the sum of the three, so exactly \(\binom{16}{3}/4=140\) four-sets have zero vector sum. Of these, twenty are whole \(K\)-lines.

The five orbits of five-sets have the following sizes and signatures, where a *circuit* means an additive-parallelogram four-subset:

| Orbit size | Geometric signature | P | N | A |
|---:|---|---|---|---|
| 288 | no collinear triple | no | no | no |
| 960 | one collinear triple, no circuit | no | yes | yes |
| 1440 | two collinear triples, no circuit | no | yes | yes |
| 1440 | one collinear triple, one circuit | no | no | yes |
| 240 | four collinear points | no | no | no |

The five sizes total \(\binom{16}{5}=4368\). For each row, the asserted answers are exact equality or inequality between the directly computed trace mask and the full \(32\)-trace mask. All five representative trace masks and explicit coordinates are in `orbit_certificate.json`. Since the transformations preserve line parallelism, one representative establishes the answer for its entire orbit. The resulting five-support counts are \(0,2400,3840\). The absence of five-shattering for P also follows from the elementary count of only thirty concepts (fewer than \(32\) traces).

**3. Geometric count and interpretation.** Every five-set with four selected points on one line fails shattering: two other lines can meet that line in at most two points, so the trace selecting three of the four but excluding the fourth is impossible. A five-set with no collinear triple likewise cannot be covered by two lines, since each meets it in at most two points. Among five-sets, there are exactly \(240=20\cdot12\) containing a whole four-point line. Exactly \(1440\) have two collinear triples: choose their common point (sixteen choices), two distinct directions (\(\binom52\) choices), and two of the three other points on each chosen line (\(\binom32^2\) choices). Counting pairs (support, chosen triple) gives \(20\binom43\binom{12}{2}=5280\); after subtracting the twice-counted double-triple sets, exactly \(2400\) five-sets have one collinear triple and no four-point line. Thus the total with at least one triple and no full line is \(3840\), consistent with A. Of these, \(1440\) contain an additive four-circuit: choose one of the \(120\) noncollinear additive parallelograms and one of the remaining twelve points. Such a five-set has a unique four-circuit, and every extension contains one collinear triple. It accounts exactly for the five-supports shattered by A but not N. This explains the parallelism-sensitive contrast.

**4. No support of six points is shattered.** Suppose a six-set is shattered by any union of two distinct lines. It cannot contain four collinear points, by the four-point obstruction above. But its all-positive trace must be covered by two lines. Each line therefore contains exactly three selected points, with those two triples disjoint. Delete one selected point from the first triple and request all other five to be positive. Any two-line cover must use the unique line through the other triple, leaving two original first-triple points to be covered by the other line, which is the original first-triple line and necessarily contains the excluded point. Contradiction. By heredity, no larger support is shattered. The same upper bound applies to P and N, which are subfamilies of A. This closes the polynomial proof for all cardinalities.

## Verification
Running `python3 verify_affine.py` in the directory containing the two checkers generates `orbit_certificate.json` and prints `AFFINE_TWO_LINE_SHATTERING_PASS`. It checks all \(14893\) supports of sizes zero through six against the stated formula (all sizes at most five individually, plus all six-sets for the two larger classes). It also regenerates all orbit sizes, geometric signatures, and representative trace masks from the eight explicitly listed transformations. Running `python3 verify_incidence.py` independently builds lines from pairs of points by the zero-determinant equation, groups line unions by geometric intersection rather than slope names, and verifies all coefficients up to degree five plus the six-point obstruction. It prints `AFFINE_INCIDENCE_INDEPENDENT_PASS`. Both scripts use only the Python standard library and include exact integer assertions; the outputs were observed on the packaged files. The finite enumeration here is an exhaustive proof because every support in the finite universe is included, not an extrapolation from samples. The noncomputational six-point argument also establishes the vanishing of all higher coefficients.

## Relationship to prior work
The literature on VC complexity of finite-field incidence concepts motivates this question: Fitzpatrick, Iosevich, McDonald and Wyman (2021) study finite-field *distance spheres*, not unions of two lines; Iosevich, Pham, Senger and Tait (2023) use VC bounds for point-line incidence estimates, rather than exact support profiles. Eleftheriou, Papadopoulos and Westhead (first preprint January 2025) prove that unions of two **real** lines have VC dimension five and identify two five-point incidence types. Their results are acknowledged, and neither that dimension bound nor the general two-triple geometry is claimed new. This result instead determines the complete three-way finite-field **parallelism-refined** support census at order four, in which two five-point supports with the same line-collinearity type may differ under the nonparallel-line restriction because one contains an additive parallelogram.

Relevant earlier mathematical records establish the sharp static/online dimensions of the two-distinct-parallel-line class, the sharp online dimension of nonparallel two-line unions, and the all-order shattering polynomial for two projective-line unions. These neither state the present three coefficient vectors nor imply the distinction between the \(960\) and \(1440\) single-triple affine orbits; their proofs and exact scopes were directly compared before this claim was retained. The projective theorem concerns a different point universe (twenty-one points at order four) and allows coincident component lines. The nonparallel affine theorem proves VC dimension five but not the full support polynomial or parallelism-sensitive five-orbit split.

## Limitations
This is an exact finite result for the Desarguesian affine plane of order four only. It does not extend the polynomial formulas to arbitrary affine planes, does not assess online learning rank, and does not claim that the generic two-line upper bound five or the real-plane incidence-isomorphism classification is new. The arithmetic and orbit assertions have two executable exact checks but no external independent mathematical audit. A historical-priority search cannot exclude unknown or unindexed equivalent literature; the closest known public mathematical records and full-text comparisons are given explicitly.

## References
1. D. Fitzpatrick, A. Iosevich, B. McDonald, E. Wyman, *The VC-dimension and point configurations in* \(\mathbb F_q^2\), arXiv:2108.13231, first posted 2021-08-30. https://arxiv.org/html/2108.13231v1
2. A. Iosevich, T. Pham, S. Senger, M. Tait, *An improved point-line incidence bound over arbitrary finite fields via the VC-dimension theory*, arXiv:2303.00330, 2023-03-01. https://arxiv.org/html/2303.00330v1
3. P. E. Eleftheriou, A. Papadopoulos, F. Westhead, *Exact VC-Dimensions of Certain Geometric Set Systems*, arXiv:2501.09847, 2025-01-16, particularly Theorems A/B and Proposition 7.1. https://arxiv.org/html/2501.09847v1
4. *Sharp online shattering for unions of two nonparallel lines in finite affine planes*, public mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-online-shattering-for-unions-of-two-nonparallel-lines-in-f--0156eb59f663
5. *Exact static and online dimensions of double-parallel-line concepts in finite affine planes*, public mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-static-and-online-dimensions-of-double-parallel-line-conce--d4d1e8676d77
6. *Finite-order exceptions and the shattering polynomial of two-line unions in projective planes*, public mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-finite-order-exceptions-and-the-shattering-polynomial-of-two-lin--94f22e63c9c6
