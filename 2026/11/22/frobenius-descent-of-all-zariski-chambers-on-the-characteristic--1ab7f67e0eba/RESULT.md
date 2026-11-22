# Frobenius descent of all Zariski chambers on the characteristic-two Fano-plane blowup

## Finding
Let \(k=\mathbb F_q\), where \(q\) is any power of \(2\), and let \(X_0/k\) be the blowup of the seven \(\mathbb F_2\)-points of \(\mathbb P^2\). The collineation group \(G=\operatorname{GL}_3(\mathbb F_2)\) acts on \(X_0\). For each \(g\in G\), let \(X_g/k\) denote the finite-field twist defined by the cocycle taking geometric Frobenius to \(g\). Define a *rational Zariski chamber* to mean a chamber of the big cone of \(X_g\otimes_k\bar k\) that has an interior divisor class defined over \(k\), equivalently a chamber arising from the intersection of the rational Néron–Severi subspace with the geometric big cone. Count chambers by their geometric negative-part supports, and let \(r\) be the number of negative curves in the support.

The complete support-size generating polynomials for the rational chambers depend only on the order of \(g\):

| Order of \(g\) | Elements of \(G\) | Rational chamber count | Coefficients for \(r=0,1,\ldots,7\) |
| --- | ---: | ---: | --- |
| \(1\) | \(1\) | \(2257\) | \((1,14,91,322,651,728,392,58)\) |
| \(2\) | \(21\) | \(209\) | \((1,6,19,34,51,48,40,10)\) |
| \(3\) | \(56\) | \(25\) | \((1,2,1,4,6,2,5,4)\) |
| \(4\) | \(42\) | \(21\) | \((1,2,3,2,3,4,4,2)\) |
| \(7\) | \(48\) | \(3\) | \((1,0,0,0,0,0,0,2)\) |

The \(48\) elements of order \(7\) comprise two distinct conjugacy classes of \(24\) elements each; both produce the same polynomial. In an order-seven twist the **only** rational Zariski chambers are the nef chamber and the two chambers supported respectively on all seven exceptional curves and all seven strict transforms of the Fano lines. Consequently there is no rational chamber having \(1\) through \(6\) negative components, despite the \(2257\) geometric chambers.

The full \(168\)-element collineation group partitions the \(2257\) geometric chambers into exactly \(54\) orbits. The orbit-size multiplicities are
\[
\begin{array}{c|rrrrrrr}
\text{orbit size}&1&7&21&28&42&84&168\\\hline
\text{number of orbits}&3&10&8&12&4&16&1.
\end{array}
\]
This is the complete arithmetic descent classification for the specified \(G\)-twists; it does not claim classification under automorphisms interchanging points with lines.

## Assumptions and scope
A point is indexed by a nonzero vector \(v\in\mathbb F_2^3\), and a Fano line by a nonzero covector \(a\in(\mathbb F_2^3)^*\); incidence means \(a\cdot v=0\). The seven exceptional \((-1)\)-curves are \(E_v\). The seven strict transforms of the Fano lines are \((-2)\)-curves \(L_a\). Distinct \(E\)-curves are disjoint, distinct \(L\)-curves are disjoint, and \(E_v\cdot L_a=1\) precisely at incidence. Their negative-curve intersection graph is the Heawood graph, with \(14\) vertices and \(21\) edges.

A rational chamber is counted if the relative interior of its geometric Zariski chamber contains the class of a big \(\mathbb Q\)-divisor over \(k\). This is a statement about geometric negative supports and descent of the big-cone decomposition, not a count of \(k\)-rational points on a moduli variety of chambers. All twists \(X_g\) exist for every \(\mathbb F_{2^m}\) by ordinary finite-field descent from the \(k\)-defined collineation action; the conclusion does not require a specified plane-model realization of the descended zero-cycle. Only \(G\)-twists are asserted, not all forms of the underlying surface.

## Proof
**1. Exhaustiveness of the fourteen negative curves.** The anticanonical divisor \(-K=3H-\sum_v E_v\) has square \(2\) and is nef: the cubics \(XY(X+Y)\), \(XZ(X+Z)\) and \(YZ(Y+Z)\) vanish precisely at the seven chosen geometric points, and their linear terms at each point generate the cotangent space. They therefore give a basepoint-free subsystem of \(|-K|\) on the blowup. In particular \(-K\) is nef and big.

For a reduced irreducible negative curve \(C\), adjunction and \(-K\cdot C\geq0\) imply \((C^2,-K\cdot C)=(-1,1)\) or \((-2,0)\). The exceptional curves are seven examples of the first type. For any other irreducible negative curve write \(C=dH-\sum m_vE_v\) with \(d\ge1\), \(m_v\ge0\). In the \((-2)\)-case, the equations \(\sum m_v=3d\) and \(\sum m_v^2=d^2+2\) and Cauchy–Schwarz force \(d\le2\). When \(d=1\), exactly three simple points are collinear, yielding the seven \(L_a\); when \(d=2\), the six simple base points always include three collinear points, impossible for an irreducible conic. In the \((-1)\)-case, \(\sum m_v=3d-1\), \(\sum m_v^2=d^2+1\), and Cauchy–Schwarz give \(d\le3\). The only respective multiplicity patterns are two simple points (\(d=1\)), five simple points (\(d=2\)), and one double plus six simple points (\(d=3\)). A Fano line through the two points forbids the first, a collinear triple among any five points forbids the second, and the Fano lines through the double point each contribute intersection multiplicity at least \(4>3\), forbidding an irreducible cubic. Hence there are precisely fourteen negative curves.

**2. Negative definite supports.** The intersection matrix has diagonal weights \(-1\) on the exceptional part and \(-2\) on the Fano-line part, and off-diagonal entries \(1\) exactly on the twenty-one incidences. Any support whose induced graph has maximum degree at most one has a block diagonal intersection matrix consisting of negative scalars and blocks \(\left(\begin{smallmatrix}-1&1\\1&-2\end{smallmatrix}\right)\), all negative definite. If an induced vertex has at least two neighbors, its three-vertex principal intersection matrix has determinant \(0\), so the full matrix cannot be negative definite. By the Zariski-chamber/negative-definite-support correspondence, chambers therefore correspond precisely to induced-degree-at-most-one subsets of the fourteen vertices. This geometric characterization and the untwisted coefficient polynomial are acknowledged as prior published results; they are reconstructed only to establish the arithmetic descent hypothesis independently.

**3. Descent of the chamber.** A geometric support is the negative part of a rational chamber over \(k\) only if the Galois action preserves it, because Zariski decomposition is unique. Conversely, if a negative-definite support \(S\) is invariant under Frobenius, the reduced sum \(\sum_{C\in S}C\) descends to a \(k\)-divisor. Choose a \(k\)-ample divisor \(H\). Proposition 1.1 of Bauer–Funke–Neumann yields, for sufficiently large integral \(n\), an interior big divisor \(H+n\sum_{C\in S}C\) whose geometric negative part is supported exactly on \(S\). Thus the rational chambers correspond bijectively to the Frobenius-invariant induced-degree-at-most-one vertex subsets. A finite-field twist by \(g\) induces precisely the point permutation \(v\mapsto gv\) and contragredient line permutation \(a\mapsto a\circ g^{-1}\).

**4. Exhaustive arithmetic count and global orbit partition.** Enumerate all invertible \(3\)-by-\(3\) matrices over \(\mathbb F_2\); there are \(168\). Label fourteen vertices by the seven nonzero vectors followed by seven nonzero covectors, and enumerate all \(2^{14}=16384\) masks. The mask is a chamber if each selected vertex has at most one selected neighbor. For each group element count fixed chamber masks by support cardinality. The attached standalone program uses two independent fixed-mask counts: it tests all \(2257\) chamber masks under the explicit permutation, and it enumerates unions of entire vertex cycles. Both yield the table, separately for all \(168\) matrices. An independent exact rational positive-definite \(LDL^t\) elimination checks all \(16384\) principal intersection matrices against the induced-degree criterion.

To obtain the orbit counts, the program partitions the entire \(2257\)-element chamber set into orbits under the \(168\) permutations, recording their sizes. These form \(3+10+8+12+4+16+1=54\) orbits with total \(2257\) chambers. Independently, Burnside's lemma gives
\[
\frac{2257+21\cdot209+56\cdot25+42\cdot21+48\cdot3}{168}=54.
\]
Every order-seven matrix acts transitively on the seven points and, separately, on the seven lines. Consequently its only invariant support masks are the empty set, the complete point set, the complete line set and their union. The union is not a negative-definite support, whereas the first three are. This proves the order-seven rigidity and completes the classification.

## Verification
Run `python3 verify_fano_chamber_descent.py` under Python \(3.10\) or newer; the program has no nonstandard dependencies. It rebuilds the Fano incidences, full negative-curve intersection matrix, \(168\) collineations and their two-part actions, then checks each of the \(16384\) supports by both the graph criterion and exact \(LDL^t\) positivity. It independently determines the fixed chamber polynomials directly and by vertex-orbit unions for every group element, and computes all \(54\) collineation orbits. The exact standard output is supplied in `fano_chamber_verification_output.txt` and ends `FANO_FROBENIUS_ZARISKI_CHAMBER_DESCENT_OK`. This finite exhaustive computation proves the combinatorial identities; it is not substituted for the algebraic arguments on negative curves, Zariski decomposition and Galois descent.

## Relationship to prior work
Bauer, Funke and Neumann establish the correspondence between chambers and negative-definite reduced divisors, and count generic blowups of the plane, not the special characteristic-two seven-point configuration or its Galois descent. Bauer and Schmitz give efficient general chamber algorithms and a Segre–Schur quartic application. A prior published calculation, *Zariski chambers of the characteristic-two Fano-plane blowup*, establishes the precise fourteen negative curves, the induced-matching condition, and **all \(2257\) untwisted geometric chambers**; these facts are prior and are not claimed new here. The evaluated contribution here is the complete five-regime rational support polynomial of all collineation twists and the order-seven three-chamber rigidity, together with the full 54-orbit classification. No corresponding result was located in targeted comparisons, but a finite search does not establish universal historical priority.

## Limitations
The theorem is restricted to characteristic-two forms obtained by twisting the specified Fano-plane blowup through its \(168\)-element collineation subgroup. It is not a classification of all possible forms, of arbitrary weak degree-two del Pezzo surfaces, or of the point–line duality extension of the Heawood graph, which does not preserve the self-intersection weights. The rational chamber count refers to interior classes defined over the ground field and negative-support strata; it does not count individual rational divisor classes or rational points. The unchanged geometric support census was known previously.

## References
1. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958v1, first submitted 2009-12-04, Proposition 1.1 and Sections 1–2, https://arxiv.org/html/0912.0958v1.
2. T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373v1, first submitted 2012-04-19, introduction and Section 1, https://arxiv.org/html/1204.4373v1.
3. *Zariski chambers of the characteristic-two Fano-plane blowup*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-zariski-chambers-of-the-characteristic-two-fano-plane-blowup--3bea24e31a7b (existing fourteen-curve support characterization and the 2257-chamber geometric polynomial).
