# Sharp first tetrahedral-volume gap in Birkhoff polytopes

## Finding
Let \(\Omega_n\) denote the convex polytope of real \(n\)-by-\(n\) doubly stochastic matrices, with its ambient Frobenius Euclidean metric. For any four points, their tetrahedral volume means the intrinsic three-dimensional Euclidean volume of their convex hull, and is zero when they are affinely dependent. For every integer \(n\ge4\), the largest tetrahedron with vertices anywhere in \(\Omega_n\) has volume
\[
V_{\max}(n)=\frac{n^{3/2}}3.
\]
Every maximizer consists of four permutation matrices with pairwise disjoint supports (equivalently, a four-row Latin rectangle of order \(n\)), and all such quadruples maximize.

Among **vertex-supported** tetrahedra that do not maximize, the largest volume is exactly
\[
V_{\mathrm{next}}(n)=
\begin{cases}
\frac{\sqrt{46}}3,&n=4,\\[3pt]
\sqrt{\frac{n(n-1)(2n+1)}{18}},&n\ge5.
\end{cases}
\]
For \(n\ge5\), equality holds exactly when one unordered pair of the four permutations agrees at exactly one coordinate and the other five unordered pairs have no agreements. In particular, the **sharp first squared-volume gap** for \(n\ge5\) is
\[
V_{\max}(n)^2-V_{\mathrm{next}}(n)^2=\frac{n(n+1)}{18}.
\]
For \(n=4\), every second-level quadruple has two one-coordinate agreements, occurring in two pairs that share one of the four permutations, and otherwise no agreements; the squared-volume gap is \(2\). Exact enumeration gives 24 maximizers and 288 second-level vertex quadruples at order four, and 6,720 maximizers and 72,000 second-level vertex quadruples at order five.

## Assumptions and scope
The metric is the unweighted real Frobenius metric \(\|A-B\|_F^2=\sum_{i,j}(a_{ij}-b_{ij})^2\), not intrinsic graph distance, normalized matrix-operator norm, or the normalized metric obtained by dividing by the matrix order. A permutation matrix \(P_\sigma\) has a one at \((i,\sigma(i))\). Two permutations have coincidence number \(c(\sigma,\tau)=|\{i:\sigma(i)=\tau(i)\}|\); their squared Frobenius distance is \(2(n-c(\sigma,\tau))\). The second level is among unordered four-element subsets of distinct **vertices**, not among all nonmaximal tetrahedra with arbitrary interior points: the latter have volumes tending continuously to the maximum.

## Proof
**A sharp four-point diameter lemma.** Let \(A,B,C,D\) lie in a real Euclidean space, with all six pairwise distances at most \(L>0\) and \(\|A-B\|=a\le L\). Their tetrahedron satisfies
\[
\operatorname{Vol}_3(A,B,C,D)^2\le\frac{a^2L^2(3L^2-a^2)}{144}.
\tag{1}
\]
For nonzero \(a\), equality in (1) requires and is implied by all **other five** pairwise distances being exactly \(L\).

To prove this, set \(u=(A-B)/2\), \(w=(C-D)/2\), and \(v=(C+D-A-B)/2\). Direct exterior-product expansion gives \(\operatorname{Vol}_3=\frac23\|u\wedge v\wedge w\|\). The bound by the product of norms yields \(\operatorname{Vol}_3^2\le\frac49\|u\|^2\|v\|^2\|w\|^2\). The sum of the four cross-pair squared distances is \(4(\|u\|^2+\|v\|^2+\|w\|^2)\le4L^2\). Also \(\|u\|^2=a^2/4\) and \(\|w\|^2\le L^2/4\). For \(0\le z\le L^2/4\), the function \(z(L^2-a^2/4-z)\) is strictly increasing (its derivative is at least \(L^2/4>0\)), hence (1). Equality forces \(\|C-D\|=L\) and all four cross-pair distances equal \(L\); those equalities also make \(u,v,w\) mutually orthogonal, giving equality in the exterior-product inequality.

**Exact unrestricted maximum.** For \(X,Y\in\Omega_n\), row sums and nonnegativity give \(\|X\|_F^2\le n\) with equality only for a permutation matrix. Since \(\langle X,Y\rangle_F\ge0\), every distance is at most \(L=\sqrt{2n}\). Equality holds exactly for pairs of support-disjoint permutation matrices. The diameter lemma with \(a\le L\), and monotonicity of \(a^2(3L^2-a^2)\) over \([0,L^2]\), gives \(\operatorname{Vol}_3^2\le L^6/72=n^3/9\). Equality forces all six distances to equal \(L\), hence four support-disjoint permutation matrices. Four distinct cyclic shifts supply such a configuration for every \(n\ge4\).

**Exact first forbidden-overlap gap for \(n\ge5\).** Every vertex is a permutation matrix. If a vertex quadruple does not maximize, at least one pair coincides in one or more coordinates, giving \(a^2\le2(n-1)\). Apply (1) with \(L^2=2n\), noting that its right-hand side is strictly increasing in \(a^2\) over \([0,2n]\). We obtain
\[
\operatorname{Vol}_3^2\le\frac{2(n-1)\,2n\,[6n-2(n-1)]}{144}
=\frac{n(n-1)(2n+1)}{18}.
\]
Equality forces exactly one coordinate agreement in the selected pair and all other five pairs support-disjoint. Such a quadruple exists for every \(n\ge5\): begin with the four cyclic permutations \(i\mapsto i+s\pmod n\), \(s=0,1,2,3\), then interchange the images of coordinates \(i=0\) and \(i=1\) **only in the shift-zero permutation**. The modified first row agrees at \(i=0\) with shift one, but no other coincidences occur since shift \(n-1\) is absent when \(n\ge5\). Subtracting squared extrema gives the stated gap.

**The order-four exception.** The foregoing universal upper bound is not attainable at order four because a four-row permutation array of order four cannot have precisely one coincidence among its six row pairs. Indeed, each symbol occurs exactly four times across the four permutation rows. If one column contains a repeated symbol, that column omits another symbol, whose four total appearances force a repetition in some other column. Thus a single coincident pair-position is impossible. A finite exhaustive computation resolves the actual second level. Left multiplication of all four permutation matrices by the inverse of one of them is a Frobenius isometry; hence every unordered quadruple is represented by \((I,P,Q,R)\) with \(P,Q,R\) selected without repetition from the other 23 permutations. The supplied standard-library checker visits each of the \(\binom{23}{3}=1771\) choices; for each it computes all six integer coincidence numbers and the exact Gram determinant of the three difference matrices. It certifies that the largest determinant is \(256\) and the next distinct determinant is \(184\), with anchored multiplicities 4 and 48. Squared volumes are determinants divided by \(36\). At determinant 184 the coincidence pattern always consists of exactly two ones and four zeros, with the two nonzero pairs incident. Multiplying the anchored counts by \(24/4\) gives the unoriented total counts of 24 and 288. At order five, the same exact, exhaustive process over \(\binom{119}{3}=273819\) choices finds determinants \(500\) and \(440\) with anchored multiplicities 224 and 2400, respectively; multiplying by \(120/4\) gives 6720 and 72000. The general order-five-and-higher theorem does **not** rely on this enumeration.

## Verification
Run `python check.py` using Python 3 with no optional packages. It independently forms difference matrices entry by entry for selected small instances and compares their integer Gram determinants against the coincidence-number formula. It exhaustively checks all order-four and order-five anchored vertex quadruples, verifies their two highest distinct determinant levels, multiplicities, and coincidence patterns, and separately verifies the exact constructed witnesses in orders 5 through 44. Its expected final line is `BIRKHOFF_TETRA_GAP_PASS full_orders=4,5 example_orders=5..44 high_levels_n5=500,440 independent_gram=PASS`. These finite checks support, but do not replace, the all-order diameter-lemma proof.

## Relationship to prior work
Bouthat, Mashreghi and Morneau-Guérin (2023) study Frobenius/Schatten Chebyshev geometry of the Birkhoff polytope, including its minimum enclosing sphere, not low-dimensional inscribed simplex-volume levels. Paffenholz (2013) classifies combinatorial types of faces; the present tetrahedra generally need not be faces, and the statement is metric. General algorithms for largest-volume simplices (Di Summa and collaborators) do not imply these exact values without a Birkhoff-specific analysis. A classical regular-simplex diameter bound supplies the elementary largest-volume intuition; the exact first nonmaximal level, the unique one-coincidence characterization, and the order-four obstruction are the distinguishing claims. The comparison is provisional: no assertion of comprehensive historical priority is made.

## Limitations
The second volume level is only asserted for tetrahedra with four permutation-matrix vertices. Arbitrarily small perturbations of an unrestricted maximizer produce volumes arbitrarily close to maximal, so there is no second-largest unrestricted volume. No enumeration of higher-dimensional inscribed simplices is claimed. The order-four exhaustive proof assumes only the elementary, explicitly enumerated permutation-list reduction and exact integer arithmetic; independent external auditing has not been performed. Earlier literature may contain equivalent extremal formulations under matching or Latin-rectangle terminology.

## References
- L. Bouthat, J. Mashreghi, and F. Morneau-Guérin, *On the Geometry of the Birkhoff Polytope. II. The Schatten p-norms*, arXiv:2310.14043, first posted 2023-10-21, https://arxiv.org/abs/2310.14043.
- L. Bouthat, J. Mashreghi, and F. Morneau-Guérin, *On the Geometry of the Birkhoff Polytope. I. The operator \(\ell^p\)-norms*, arXiv:2310.14041, first posted 2023-10-21, https://arxiv.org/abs/2310.14041.
- A. Paffenholz, *Faces of Birkhoff Polytopes*, arXiv:1304.3948 (2013), https://arxiv.org/abs/1304.3948.
- B. Baumeister and F. Ladisch, *A property of the Birkhoff polytope*, Algebraic Combinatorics 1 (2018), 275–281, https://doi.org/10.5802/alco.6.
- M. Di Summa, F. Eisenbrand, Y. Faenza, and C. Moldenhauer, *On largest volume simplices and sub-determinants*, arXiv:1406.3512 (2014), https://arxiv.org/abs/1406.3512.
