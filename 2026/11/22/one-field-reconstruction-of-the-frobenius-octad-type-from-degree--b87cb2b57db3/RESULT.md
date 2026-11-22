# One-field reconstruction of the Frobenius octad type from degree-one del Pezzo exceptional-curve flags

## Finding

Let \(S/\mathbb F_q\) be a smooth degree-one del Pezzo surface in characteristic at least five, obtained by blowing up a Frobenius-stable reduced set of eight geometric points in general position in \(\mathbb P^2\). Let \(\mathcal E\) be its 240 geometric exceptional curves, and let \(F\) denote arithmetic Frobenius. For each distinct unordered pair \(\{C,D\}\subset\mathcal E\), retain its intersection number \(C\cdot D\). Define four **single-ground-field** counts:

\[
R=\#\mathcal E^F,\qquad
P_j=\#\bigl\{\{C,D\}\subset\mathcal E:C\ne D,\ C\cdot D=j\bigr\}^{F}\quad(j=0,1),
\]
\[
T=\#\bigl\{\{A,B,C\}\subset\mathcal E:A\cdot B=A\cdot C=B\cdot C=0\bigr\}^{F}.
\]

The exponent \(F\) means invariance of the **unordered set**, not pointwise rationality of each curve. The tuple \((R,P_0,P_1,T)\) determines the complete Frobenius cycle partition of the original eight-point set. The following table is exhaustive over the 22 partitions of eight:

| Eight-point cycle partition | \(R\) | \(P_0\) | \(P_1\) | \(T\) |
|:--|--:|--:|--:|--:|
| \((1^8)\) | 240 | 6720 | 15120 | 60480 |
| \((2,1^6)\) | 126 | 2072 | 3780 | 11592 |
| \((2^2,1^4)\) | 60 | 544 | 804 | 2080 |
| \((2^3,1^2)\) | 26 | 144 | 168 | 432 |
| \((2^4)\) | 8 | 32 | 72 | 96 |
| \((3,1^5)\) | 72 | 720 | 1080 | 2214 |
| \((3,2,1^3)\) | 30 | 140 | 180 | 330 |
| \((3,2^2,1)\) | 12 | 40 | 24 | 70 |
| \((3^2,1^2)\) | 12 | 12 | 36 | 36 |
| \((3^2,2)\) | 6 | 8 | 0 | 12 |
| \((4,1^4)\) | 40 | 240 | 290 | 400 |
| \((4,2,1^2)\) | 14 | 36 | 42 | 68 |
| \((4,2^2)\) | 4 | 8 | 14 | 8 |
| \((4,3,1)\) | 4 | 0 | 8 | 10 |
| \((4^2)\) | 0 | 0 | 4 | 0 |
| \((5,1^3)\) | 20 | 60 | 60 | 40 |
| \((5,2,1)\) | 6 | 12 | 0 | 12 |
| \((5,3)\) | 2 | 0 | 0 | 4 |
| \((6,1^2)\) | 8 | 6 | 12 | 0 |
| \((6,2)\) | 2 | 2 | 0 | 0 |
| \((7,1)\) | 2 | 0 | 0 | 0 |
| \((8)\) | 0 | 0 | 0 | 0 |

Precisely 21 distinct triples \((R,P_0,P_1)\) occur: the sole collision is between \((5,3)\) and \((7,1)\). More strongly, **every fixed unordered pair count**, including the multiplicities \(2\) and \(3\), is identical in these two cases: the pair-count vector indexed by intersection numbers \(0,1,2,3\) is \((0,0,0,1)\) for both. The mutually-disjoint triple count separates them, being \(4\) and \(0\), respectively. Hence arity three is necessary among all such single-field, intersection-labeled flag counts of arity at most three, and arity three suffices.

## Assumptions and scope

The base is a finite field of characteristic at least five. The blown-up eight-point subscheme is reduced, geometrically in general position, and stable under Frobenius; its eight points need not individually be rational. The assertion is **conditional** on a surface with a given cycle partition; it does not claim that all 22 types occur over each particular finite field. All incidence counts refer to finite étale permutation sets of geometric exceptional curves or their unordered subsets, not to rational geometric intersection points, Picard torsion, or the number of surface rational points. A curve's geometric exceptional divisor is uniquely determined by its exceptional class.

## Proof

Write each exceptional divisor class in the Picard lattice as \(dH-\sum_{i=1}^8m_i E_i\). In the chosen basis, the intersection form is

\[
(d;m)\cdot(e;n)=de-\sum_{i=1}^8m_in_i.
\]

An exceptional class satisfies \(3d-\sum_i m_i=1\) and \(d^2-\sum_i m_i^2=-1\). The standard complete list of geometric exceptional classes consists of seven coefficient-pattern families. Their degrees, multiplicity multisets, and numbers are:

| Degree \(d\) | Multiplicity multiset \(\{m_i\}\) | Number |
|--:|:--|--:|
| 0 | one \(-1\), seven \(0\) | 8 |
| 1 | two \(1\), six \(0\) | 28 |
| 2 | five \(1\), three \(0\) | 56 |
| 3 | one \(2\), six \(1\), one \(0\) | 56 |
| 4 | three \(2\), five \(1\) | 56 |
| 5 | six \(2\), two \(1\) | 28 |
| 6 | one \(3\), seven \(2\) | 8 |

These total 240. Completeness is the classical exceptional-curve classification reproduced in Desjardins–Winter, Theorem 2.1; the independent program also exhausts every solution of the two numerical exceptional-class equations with \(-1\le m_i\le3\), \(0\le d\le6\). Frobenius acts by the chosen permutation of the eight \(m_i\)-coordinates; two such actions are conjugate exactly when their eight-point cycle partitions coincide.

For any partition \(\lambda\) of eight, select the product of disjoint cycles of lengths given by \(\lambda\). Its induced permutation on the 240 vectors is computed by coordinate permutation and is manifestly compatible with the above intersection form. There are exactly 22 such partitions. To compute \(P_j\), enumerate every unordered pair of different classes having intersection \(j\), and count pairs stabilized as unordered sets. Every invariant pair is either two individually fixed classes or a single two-cycle of Frobenius on the 240 classes.

To compute \(T\), every invariant three-set decomposes uniquely as one Frobenius three-cycle, a fixed curve plus a two-cycle, or three fixed curves. Check pairwise vanishing intersections within each candidate. This yields the table by finite exhaustive integer operations. For an independent check, form all 60,480 pairwise-disjoint triples of the 240 vectors and test each candidate's image directly under each of the 22 permutations. Both algorithms reproduce the table exactly. As numerical invariants, the full intersection-pair totals are 6720, 15120, 6720, 120 at intersections \(0,1,2,3\), respectively, agreeing with the established \(E_8\) face counts.

The only equality among the first three columns is \((5,3)\) versus \((7,1)\); direct testing of all four possible pair intersection labels also gives identical counts \((0,0,0,1)\). Their triple counts differ. There is a geometric explanation: in the \((5,3)\) case the three blown-up points in the three-cycle provide four invariant triples of mutually skew exceptional curves, drawn from the three exceptional divisors, the three lines joining the pairs of these points, the three analogous quintic transforms, and the three sextic transforms with moving triple point. No additional invariant skew triples appear. In the \((7,1)\) case the Frobenius action on exceptional classes has no three-cycles, and it fixes only two individual curves, so an invariant three-set is impossible. Hence \(T=4\) versus \(0\).

Finally the 22 rows have distinct four-tuples, proving reconstruction. The finite case analysis exhausts all possible cycle partitions, so it establishes the stated general claim for every eligible finite-field surface; it is not a probabilistic experiment or extrapolation from a sample of surfaces.

## Verification

Run `python3 verify_orbits.py` and `python3 verify_direct.py` in the directory containing the supplied standalone scripts. The first builds all exceptional classes from their seven geometric patterns, independently generates the 22 conjugacy class representatives, and computes fixed pairs and skew triples from Frobenius orbits. The second generates the 240 classes by an independent Diophantine search and enumerates all pairs and all 60,480 skew triples explicitly, checking their setwise Frobenius invariance. Both assert the full 22-row table, the 21/22 distinctness statements, and the identical pair-count vectors for \((5,3)\) and \((7,1)\). Their exact numerical outputs, not a pre-existing log, are the computation certificate.

## Relationship to prior work

Winter–van Luijk establish the underlying \(E_8\) colored graph, the 6720 disjoint pairs, the 60,480 disjoint triples and Weyl orbits on cliques. Desjardins–Winter reproduce the complete 240 exceptional-curve classes and investigate concurrence and elliptic torsion, not arithmetic Frobenius-fixed unordered flags. Kulkarni studies Galois actions on the 240 classes and an inverse Galois construction via \(D_8\)-sublattices, not the 22-case single-field fixed-flag table. The new claim is the **complete arithmetic four-count reconstruction table and the sharp arity-two obstruction**; the underlying 240-curve and 60,480-triple counts are explicitly prior geometry.

## Limitations

The table detects the permutation type of the specific Frobenius-stable blow-up octad, not the entire Weyl-group Frobenius conjugacy class for arbitrary unmarked degree-one del Pezzo surfaces. It is not an assertion that all 22 cycle types exist for every small field. It does not determine incidence counts for arbitrary higher-order geometric intersection, rational point concurrency, the arithmetic Brauer group, or Picard-group torsion. An older unindexed arithmetic permutation-character table covering the same four counts is a remaining priority risk.

## References

1. J. Desjardins and R. Winter, *Torsion points and concurrent exceptional curves on del Pezzo surfaces of degree one*, first public preprint 21 October 2022, arXiv:2210.11659, especially Theorem 2.1 and Section 2. https://arxiv.org/abs/2210.11659
2. R. Winter and R. van Luijk, *The Action of the Weyl Group on the \(E_8\) Root System*, first public preprint 21 January 2019, arXiv:1901.06945; *Graphs and Combinatorics* 37 (2021), especially Corollary 1 and Remarks 5–6. https://doi.org/10.1007/s00373-021-02315-8
3. A. Kulkarni, *Sixteen points in \(\mathbb P^4\) and the inverse Galois problem for del Pezzo surfaces of degree one*, first public preprint 29 September 2021, arXiv:2109.14106, Sections 1–3. https://arxiv.org/abs/2109.14106
4. J. Desjardins, Y. Fu, K. Isham and R. Winter, *Generalized Eckardt points on del Pezzo surfaces of degree 1*, first public preprint 16 January 2024, arXiv:2401.08800, background exceptional-curve geometry. https://arxiv.org/abs/2401.08800
