# Two-conic union shattering in the ternary projective plane

## Finding
Let \(P=\operatorname{PG}(2,\mathbb F_3)\) have thirteen points. Let \(\mathcal O\) be the 234 geometrically nonsingular rational projective conics, identified with their four-point zero sets, and let
\[
\mathcal U=\{C\cup D:C,D\in\mathcal O,\ C\ne D\}.
\]
For \(S\subseteq P\), call \(S\) shattered when \(\{S\cap U:U\in\mathcal U\}=2^S\).

**Complete classification.** A set of at most six points is always shattered. A seven-point set is shattered **if and only if** it is not the union of two distinct projective lines. No eight-point set is shattered. Equivalently, the complete face polynomial is
\[
\Phi_{\mathcal U}(z)=1+13z+78z^2+286z^3+715z^4+1287z^5+1716z^6+1638z^7,
\]
so \(\operatorname{VCdim}(\mathcal U)=7\). Every maximal shattered support has seven points, and there are exactly 1638 such facets, in three \(\operatorname{PGL}_3(\mathbb F_3)\) orbits of sizes \(936,468,234\). The 78 forbidden seven-point supports form one projective orbit, consisting of the unions of two distinct lines. Thus the shattering complex is pure despite a sharp incidence obstruction at its top dimension.

## Assumptions and scope
Only \(\mathbb F_3\)-rational points and geometrically nonsingular conics are used. The two component conics must be distinct, with their order irrelevant. The concept is the union of their **rational point sets**, not the algebraic intersection scheme. Shattering refers to ordinary point-membership Boolean traces. All stated counts are exact and restricted to this thirteen-point projective plane, with no assertion for larger finite fields or arbitrary projective planes.

## Proof
**1. An exact coordinate model.** Choose the thirteen lexicographically ordered nonzero triples in \(\mathbb F_3^3\), normalized so the first nonzero entry equals one. The thirteen projective lines arise from the thirteen nonzero normalized linear forms \(aX+bY+cZ\); each has four points, every point lies on four lines, and two distinct lines meet in exactly one point. A four-set is an *oval* when it meets every projective line in at most two points. Enumerating all \(\binom{13}{4}=715\) four-sets yields 234 ovals. Every oval uniquely arises from a geometrically nonsingular ternary quadratic form, as can be seen by normalizing its four points to the standard projective frame: the projective pencil of quadrics through the frame has three reducible members and one smooth member. Conversely a smooth plane conic over this odd field has four rational points forming an oval. This identification is also checked independently by a quadratic-form determinant calculation.

**2. Complete concept enumeration.** Form the bitwise unions of the \(\binom{234}{2}=27261\) unordered distinct pairs of oval masks. Their 4641 distinct rational point sets have sizes and counts
\[
\begin{array}{c|rrrr}
|U|&5&6&7&8\\\hline
\#U&468&1248&1638&1287.
\end{array}
\]
No larger union is possible because each oval has four points. This is a finite exact enumeration, with both oval and quadratic-form constructors supplied below.

**3. Symmetry-reduced exhaustive trace certificate.** The four explicitly coded invertible matrices (coordinate interchange, diagonal multiplication by two, shear, and cyclic coordinate rotation) generate 5616 permutations of the thirteen points, the full \(\operatorname{PGL}_3(\mathbb F_3)\). Both the family \(\mathcal U\) and shattering are invariant under this action. For each orbit representative \(S\) of size six, seven, or eight, enumerate the **distinct** traces \(U\cap S\) over all 4641 concepts. The complete projective-orbit table is:

| \(\lvert S\rvert\) | Representative bitmask | Orbit size | Number of distinct traces |
|---:|---:|---:|---:|
| 6 | 63 | 468 | 64 |
| 6 | 126 | 78 | 64 |
| 6 | 183 | 936 | 64 |
| 6 | 187 | 234 | 64 |
| 7 | 127 | 78 | 127 |
| 7 | 191 | 936 | 128 |
| 7 | 254 | 468 | 128 |
| 7 | 439 | 234 | 128 |
| 8 | 255 | 468 | 254 |
| 8 | 447 | 702 | 255 |
| 8 | 510 | 117 | 255 |

A bitmask is the sum of \(2^i\) over included point indices \(i=0,\ldots,12\) in the lexicographically normalized coordinate list. Orbit sizes in each row of fixed cardinality sum to \(\binom{13}{|S|}\). Thus all six-point sets, and exactly three of the four seven-point orbits, are shattered; none of the three eight-point orbits is shattered. Shattering is hereditary, so all supports of size at most five are also shattered. The exhaustion of eight-point supports excludes all larger supports.

**4. Identify the exceptional orbit and maximality.** The 78 unions of two distinct lines are precisely the 78 seven-point supports in the 127-trace orbit. The missing trace in the displayed representative is the singleton consisting of the intersection point of its two lines. This obstruction has a geometric explanation: a nonsingular conic through a point has a unique tangent there, so it cannot meet two distinct lines through that point only at that point; therefore a union of two nonsingular conics cannot isolate that intersection point from the other six points on the two lines. For all 1716 six-point supports, an explicit extension check finds at least one seventh point producing a non-double-line support; hence no six-point face is maximal. The 1638 shattered seven-point supports, and only these, are facets.

**5. Independent all-support check.** A second implementation enumerates all nonzero quadratic forms up to scalar as coefficient sextuples, retains exactly the forms whose symmetric polar matrix has nonzero determinant, and computes their rational point sets. It independently recovers 234 smooth conics, 4641 union concepts, every trace of all 8192 possible query supports, the polynomial above, the 78 double-line nonfaces, and the 1638 seven-point facets. This independently verifies the finite computation without assuming the arc enumeration or the symmetry generators.

## Verification
With Python 3 standard library, execute `python3 verify_arcs.py` and `python3 verify_quadratics.py` in this directory. The first proves finite exhaustive coverage by all group orbits, checks the group cardinality and incidence axioms, and tests every orbit representative at sizes six through eight. The second directly enumerates all supports, constructs smooth conics using nonzero determinants of polar matrices, and checks the precise bad-seven-set and facet predicates. Neither calls external packages, requires random seeds, or relies on unverified simulation. The expected markers are `ARCS_ORBITS_PASS` and `QUADRATIC_CENSUS_PASS`.

## Relationship to prior work
Lavrauw, Popiel and Sheekey (2020) study classification and orbit invariants for finite-field nets of conics. Their Theorems 1.1 and 1.3 concern line-orbit distributions and stabilizers of nets, not point-query shattering by unions of two distinct smooth conics. Csikós, Kupavskii and Mustafa (2018) give general theory for finite unions of concepts, including broad VC-dimension bounds, but do not determine this ternary finite-geometry face polynomial.

The closest available finite-geometry classification, *The five projective types of blocking unions of two smooth conics over \(\mathbb F_3\)*, enumerates and classifies conic **pairs whose unions are blocking**; its full finding and proof were inspected. It reports five projective orbits of blocking conic pairs and their decomposition counts, not all Boolean traces on each of the 8192 query supports. Its published pair-orbit count \(1638\) denotes nontrivially blocking **pairs**, a different set of objects from the 1638 shattered seven-point **supports** in the present result. A separate finite-plane theorem on the shattering of unions of **two projective lines** proves a different concept class, with VC dimension five at order three. Thus neither statement implies the precise seven-point obstruction or the three facet orbits asserted here. Historical equivalence under a less direct coding remains possible.

## Limitations
This is an exact finite mathematical classification, not an asymptotic theorem and not an assertion about unions of three conics, field orders larger than three, or adaptive Littlestone dimension. Its exhaustive arguments rest on small, explicitly described finite sets and validated standalone code; external independent mathematical review has not been performed. A preexisting unindexed conic-pair incidence table may contain enough information to rederive the result, and literature priority remains subject to a broader independent search.

## References
1. M. Lavrauw, T. Popiel and J. Sheekey, *Combinatorial invariants for nets of conics in \(\mathrm{PG}(2,q)\)*, arXiv:2010.00177, first posted 2020-10-01, especially Theorems 1.1 and 1.3. https://arxiv.org/abs/2010.00177
2. M. Csikós, A. Kupavskii and N. H. Mustafa, *Optimal Bounds on the VC-dimension*, arXiv:1807.07924, first posted 2018-07-20, especially Sections 1–2. https://arxiv.org/abs/1807.07924
3. K. Coolsaet, A. Botteldoorn and V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, J. Combin. Des. 30 (2022), 561–580. https://doi.org/10.1002/jcd.21842
4. *The five projective types of blocking unions of two smooth conics over \(\mathbf F_3\)*, public research record, scientific statement and proof inspected. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-the-five-projective-types-of-blocking-unions-of-two-smooth-conic--72387a8e16d3/RESULT.md
5. *Finite-order exceptions and the shattering polynomial of two-line unions in projective planes*, public research record, scientific statement and proof inspected. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-finite-order-exceptions-and-the-shattering-polynomial-of-two-lin--94f22e63c9c6/RESULT.md
