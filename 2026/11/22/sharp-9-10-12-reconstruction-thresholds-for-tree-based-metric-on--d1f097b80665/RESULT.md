# Sharp 9–10–12 reconstruction thresholds for tree-based metric one-point type spectra

## Finding

Let \(\mathbb U_3\) be the countable homogeneous universal metric structure with positive distances \(\{1,2,3\}\). For an unlabelled tree \(T\) on \(n\ge1\) vertices, form the finite parameter metric \(A_T\) by assigning distance \(1\) to adjacent vertices and distance \(2\) to nonadjacent distinct vertices. Name each parameter separately. Let \(\Theta_T(x,y,z)\) count nonalgebraic complete one-point types according to the numbers of named points at distances \(1,2,3\), respectively. Consider three progressively more informative natural invariants:

\[
N_T=\Theta_T(1,1,1),\qquad
W_T(t)=\Theta_T(t,1,t),\qquad
\Theta_T(x,y,z).
\]

**Sharp reconstruction hierarchy.** Among all nonisomorphic unlabelled trees of a given order, the scalar \(N_T\) separates every tree through eight vertices and first collides at order nine, in exactly one unordered pair. The occupied-distance polynomial \(W_T\) separates every tree through nine vertices and first collides at order ten, in exactly one pair. The complete distance-graded polynomial \(\Theta_T\) separates every tree through eleven vertices and first collides at order twelve, again in exactly one pair. These are finite, exhaustive thresholds, not asymptotic or infinite-order reconstruction claims.

The unique first nine-vertex scalar collision has value \(3753\). Its two degree multisets, in nondecreasing order, are
\[
(1,1,1,1,2,2,2,2,4)\quad\text{and}\quad
(1,1,1,1,1,2,3,3,3).
\]
The occupancy coefficients, in ascending degree, differ: the respective coefficient lists are
\[
(1,18,128,468,960,1132,748,256,40,2),
\qquad
(1,18,128,468,962,1136,748,252,38,2).
\]

The unique first ten-vertex occupancy collision has shared polynomial
\[
W_T(t)=1+20t+162t^2+692t^3+1704t^4+2492t^5+2160t^6
+1080t^7+296t^8+40t^9+2t^{10}.
\]
Its scalar value is \(8649\). The complete polynomial distinguishes these trees: the coefficient corresponding to two distance-\(1\) points, four distance-\(2\) points and four distance-\(3\) points is \(364\) for the first and \(363\) for the second.

The unique first twelve-vertex complete-polynomial collision consists of two nonisomorphic trees with the same degree multiset
\[
(1,1,1,1,1,1,2,2,2,3,3,4).
\]
Both have scalar count \(55491\) and the identical complete \(\Theta_T\) (not merely the same occupancy specialization). A full list of labelled-edge witnesses, canonical unlabelled tree codes, and every nonzero coefficient appears in `artifacts/witnesses.json`; the exhaustive fibre census is `artifacts/census.tsv`.

## Assumptions and scope

The finite parameter metric uses distance \(1\) precisely on tree edges and distance \(2\) on other distinct pairs. This is a valid metric because every nonzero distance is either \(1\) or \(2\). Parameters are individually named, and algebraic types realized by parameters are excluded. Trees are connected simple unrooted unlabelled graphs; an isomorphism of their associated metrics is exactly a graph isomorphism of the trees. The results concern every unlabelled tree of order at most the claimed threshold, including trees of all diameter and degree profiles. The polynomial is homogeneous of total degree \(n\), so it is equivalent to the two-variable recording of distances \(1\) and \(3\), with the number at distance \(2\) recovered by subtraction.

## Proof

**One-point metric-type reduction (previously established).** A nonalgebraic one-point extension over \(A_T\) is specified by a function \(f:V(T)\to\{1,2,3\}\) satisfying all triangle inequalities
\[
|f(u)-f(v)|\le d_T(u,v)\le f(u)+f(v).
\]
If \(d_T(u,v)=2\), these hold for every pair of function values. If \(d_T(u,v)=1\), they exclude exactly the choices \((1,3)\) and \((3,1)\). Fraïssé homogeneity gives exactly one complete nonalgebraic type per admissible vector. This is the standard Widom–Rowlinson representation already published for this generic metric space; the present finding does not claim it as new. In particular,
\[
\Theta_T(x,y,z)=\sum_{Z\subseteq V(T)}y^{|Z|}
\prod_{C\in\pi_0(T-Z)}(x^{|C|}+z^{|C|}).
\]
The vacancy set \(Z\) consists of the parameters at distance \(2\), and each connected component remaining after deletion has uniform distance label \(1\) or \(3\).

**Complete enumeration of unlabelled trees.** Start at the unique one-vertex tree. To obtain candidate trees at order \(n\ge2\), attach one new leaf to every vertex of every previously generated \((n-1)\)-vertex tree. Every finite tree has a leaf, whose deletion gives a smaller tree, so this process covers every tree. To remove duplicates, root each candidate at its centre (or consider both centres if there are two), recursively sort rooted-subtree parenthesis codes and select the lexicographically least complete code. The centre-rooted AHU encoding is a complete invariant of unlabelled tree isomorphism. Thus deduplication neither merges nonisomorphic trees nor omits isomorphism types. The resulting counts at orders one through twelve are
\[
1,1,1,2,3,6,11,23,47,106,235,551,
\]
independently agreeing with the classical unlabelled-tree census (OEIS A000055).

**Exact polynomial computation.** Root a representative tree at an arbitrary vertex. For each subtree and each root state \(1,2,3\), store a polynomial in the counts of distance-\(1\) and distance-\(3\) labels. For a child with subtree state polynomials \((P_1,P_2,P_3)\), the permitted child-state sums are \(P_1+P_2\) for parent state \(1\), \(P_1+P_2+P_3\) for state \(2\), and \(P_2+P_3\) for state \(3\). Multiply child contributions, include the parent-state monomial, and sum the three root states. Induction on rooted subtree size proves that these coefficients count all valid state assignments exactly once. The number at distance \(2\) equals \(n-i-j\) for coefficient indexed by \((i,j)\), so this computes \(\Theta_T\) without information loss.

For each tree and order, the checker groups the exact polynomial coefficients into three collision-fibre dictionaries: scalar total, occupied-distance coefficient tuple, and full species-coefficient dictionary. It verifies emptiness of all groups with size at least two below the respective orders \(9\), \(10\), and \(12\), and verifies exactly one group of size two at each first collision. These are finite exhaustive classifications justified by the leaf-generation completeness and the proved tree dynamic programming recurrence, rather than evidence from partial sampling. The canonical codes prove the two members of each exceptional group are nonisomorphic.

**Independent witness check.** For both witnesses at each threshold, `artifacts/verify.py` independently enumerates all \(3^n\) distance-label vectors and checks edge admissibility directly, reproducing the complete polynomial computed by subtree recursion. At order nine it additionally constructs the explicit metric and tests all pairs against the full triangle constraints. In particular, the twelve-vertex equality is an equality of every coefficient of the complete distance-graded polynomial, not merely of a specialization.

## Verification

Run `python3 artifacts/verify.py` from a directory containing the bundled artifacts. It prints the canonical collision witnesses, compares independent direct state enumeration with dynamic programming for all six witnesses, confirms the full finite census through twelve vertices, and ends with `VERIFY_OK`. `python3 artifacts/build_evidence.py` regenerates `artifacts/census.tsv` and `artifacts/witnesses.json` (the two programs are colocated in `artifacts/`). Both programs use only the Python 3 standard library. All coefficients are exact integers. The complete code and recorded output accompany the result; the recorded output alone is not used as a proof of completeness.

## Relationship to prior work

Delhomme, Laflamme, Pouzet and Sauer provide an early publicly dated investigation of countable homogeneous metric spaces. The published *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* already derives the Katětov/spin-state bijection and its vacancy-component formula for all graph-metric parameter sets. The present claim concerns **unlabelled-tree reconstruction and the exact first collision fibres of three successive specializations**, neither the bridge nor its computational-complexity consequences.

Cutler and Radcliffe's *Extremal graphs for homomorphisms* determines extremal homomorphism counts to the looped three-vertex path at fixed graph size and edge number; it does not classify arbitrary equal-count tree pairs or the scalar-to-activity-to-full-polynomial first collision progression. Galvin, Marmorino, McMillon, Nir and Redlich's *Hoffman–London graphs: When paths minimize H-colorings among trees* proves path minimization and related extremal statements, including applications to the Widom–Rowlinson target, not the full tree collision-fibre census. Published tree-distance-law collision and tree-source homomorphism fingerprint findings use genuinely different invariants: intrinsic continuous distances or variable source-query families, rather than the target fixed at the three-state looped path and its occupation refinements. Targeted searches did not find the stated \(9\)-\(10\)-\(12\) first-collision hierarchy; this is a best-knowledge originality assessment, not a proof of historical uniqueness.

## Limitations

The reconstruction results are finite and sharp **through order twelve only**. No global classification for larger trees, uniqueness beyond any threshold, or claim about arbitrary graph-metric parameter sets is made. The polynomial-to-type bridge and the isomorphism-canonicalization method are prior mathematics; their new use here is to prove the concrete first-collision hierarchy. Cross-checks confirm the polynomial computations but do not establish historical priority. No independent mathematical audit has been performed.

## References

1. C. Delhomme, C. Laflamme, M. Pouzet, N. Sauer, *Divisibility of countable metric spaces*, arXiv:math/0510254, first posted 2005-10-12. https://arxiv.org/abs/math/0510254
2. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, published 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989
3. J. Cutler, A. J. Radcliffe, *Extremal graphs for homomorphisms*, Journal of Graph Theory 67 (2011), 261–284. https://doi.org/10.1002/jgt.20530
4. D. Galvin, P. Marmorino, E. McMillon, J. D. Nir, A. Redlich, *Hoffman–London graphs: When paths minimize H-colorings among trees*, arXiv:2512.23828, 2025. https://arxiv.org/abs/2512.23828
5. OEIS A000055, *Number of trees with n unlabeled nodes*. https://oeis.org/A000055
