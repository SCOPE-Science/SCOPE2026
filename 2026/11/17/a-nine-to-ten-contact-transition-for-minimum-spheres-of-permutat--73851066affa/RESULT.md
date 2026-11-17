# A nine-to-ten contact transition for minimum spheres of permutation X-ray polytopes

## Finding
For each integer \(2\le k\le10\), let \(P_k\subset\mathbb R^{2k-1}\) be the convex hull of the anti-diagonal count vectors \(X(\pi)\) of permutations \(\pi\) of \(\{0,\ldots,k-1\}\):
\[
 X_s(\pi)=\#\{i:0\le i<k,\ i+\pi(i)=s\},\qquad0\le s\le2k-2.
\]
This is the X-ray image of the \(k\)-by-\(k\) Birkhoff polytope. Equip its affine hull with the Euclidean distance inherited from \(\mathbb R^{2k-1}\).

Put \(h_j=(k-j)^2+j^2\), and define the active index set
\[
 J_k=\begin{cases}\{0,\ldots,k-1\},&2\le k\le9,\\
 \{0,\ldots,9\}\setminus\{5\},&k=10.\end{cases}
\]
Set \(S_k=\sum_{j\in J_k}h_j^{-1}\), \(t_k=(|J_k|-2)/S_k\), and \(w_j=(1-t_k/h_j)/2\) for \(j\in J_k\). With \(e_s\) the standard coordinate vectors, define
\[
 Z_0=ke_{k-1},\qquad Z_j=(k-j)e_{k-1-j}+je_{2k-1-j}\quad(1\le j\le k-1),
 \qquad C_k=\sum_{j\in J_k}w_jZ_j.
\]
Then \(w_j>0\) and \(\sum_{j\in J_k}w_j=1\). The **unique** minimum enclosing Euclidean ball of \(P_k\) has center \(C_k\) and squared radius
\[
 \boxed{R_k^2=t_k+\|C_k\|^2=\frac14\left(\sum_{j\in J_k}h_j-\frac{(|J_k|-2)^2}{S_k}\right).}
\]
The **only distinct X-ray vectors on its boundary** are \(Z_j\) for \(j\in J_k\). Thus exactly \(k\) distinct X-rays contact the minimum sphere for \(2\le k\le9\), but only **nine** contact for \(k=10\): the central cyclic-shift X-ray \(Z_5\) becomes strictly interior. In particular, \(R_{10}^2=235064670/3593269\). Every value is rational; there are no further boundary X-rays.

The exact squared radii, in increasing order \(k=2,\ldots,10\), are
\[
 \frac32,\ \frac{98}{23},\ \frac{261}{31},\ \frac{24140}{1721},\ \frac{8579}{406},\ \frac{8744806}{293679},\ \frac{212978}{5323},\ \frac{103319448}{1991573},\ \frac{235064670}{3593269}.
\]

## Assumptions and scope
The theorem covers all real doubly stochastic matrices (not just permutation matrices), and uses unnormalized anti-diagonal sums and the ambient standard Euclidean metric. Its assertions are restricted to the ten-minus-one explicitly stated integer orders, \(2\le k\le10\). In particular it does not claim an all-order formula or classify contacts for \(k\ge11\). The critical contact change is a theorem for this finite range, not a conjectured eventual pattern.

## Proof
**1. Permutation reduction.** By the Birkhoff–von Neumann theorem the doubly stochastic matrices are the convex hull of permutation matrices; taking anti-diagonal sums gives \(P_k=\operatorname{conv}\{X(\pi):\pi\in S_k\}\). The squared distance to a fixed center is convex, so it suffices to check permutation X-rays.

**2. Orthogonal cyclic-shift certificate.** For \(j=0,\ldots,k-1\), the permutation \(\pi_j(i)=(k-1-j-i)\bmod k\) has X-ray \(Z_j\) defined above. The supports of the \(Z_j\) are pairwise disjoint, so \(\langle Z_j,Z_l\rangle=0\) if \(j\ne l\), and \(\|Z_j\|^2=h_j\). From the explicit rational expressions, direct exact comparison proves all \(w_j\) in the stated \(J_k\) are positive, their sum is one, and at \(k=10\) the omitted \(h_5\) satisfies \(h_5<t_k\). Since \(\langle C_k,Z_j\rangle=w_jh_j=(h_j-t_k)/2\) for each active \(j\),
\[
 \|Z_j-C_k\|^2=h_j-2\langle C_k,Z_j\rangle+\|C_k\|^2=t_k+\|C_k\|^2.
\]
Thus all active \(Z_j\) are equidistant from \(C_k\). Furthermore, for every center \(y\),
\[
 \sum_{j\in J_k}w_j\|Z_j-y\|^2=R_k^2+\|y-C_k\|^2.
\]
Therefore no ball with a different center can enclose even these active vertices with radius at most \(R_k\), establishing the necessary optimality and uniqueness once containment is verified. The closed radius formula follows from expanding \(\|C_k\|^2=\sum_jw_j^2h_j\).

**3. Exact finite containment certificate.** The accompanying complete standard-library program `verify.py` constructs the fractions \(C_k,t_k\) without floating point. Let \(L_k\) be the denominator of \(t_k\) and let \(U_s=2L_k(C_k)_s\), all integers in the stated finite cases. For each of the \(k!\) permutations, the program constructs the full X-ray \(x\) and checks the integer inequality
\[
 \boxed{L_k\sum_sx_s^2-\sum_sU_sx_s-L_kt_k\le0.}
\]
This is precisely \(\|x-C_k\|^2\le R_k^2\), after cancelling \(\|C_k\|^2\). It also checks that equality occurs at exactly the displayed active X-rays. These loops cover **every** permutation at each integer \(k\in\{2,\ldots,10\}\), not random samples. Together with Step 1, this is an exhaustive integer-arithmetic certificate for all points of \(P_k\) in the claimed finite domain. Step 2 then gives the exact minimum sphere and its uniqueness. It also proves that non-vertex convex combinations cannot generate extra boundary points, because a strictly convex squared-distance function can attain the same maximal value on a nontrivial combination only if all combined points coincide.

## Verification
Execute `python3 verify.py` in the directory containing this document. The verifier requires Python 3.10 or later, uses only the standard library, asserts the claimed rational radii and contact sets, and exhaustively inspects the \(k!\) permutations for every \(2\le k\le10\). It reports respectively \(2,6,24,120,720,5040,40320,362880,3628800\) permutation checks. This finite exhaustive computation is part of the proof of the finite-domain theorem; no inference to higher orders is made. The analysis of the cyclic-shift weights supplies the independent exact geometric lower-bound certificate.

## Relationship to prior work
Chaudhary and Khandelwal (arXiv:2610.30058) define this X-ray polytope, prove facet criteria and enumerate facet counts through order twelve. Their stated results concern linear inequalities, facet structure and tail-probability bounds, not Euclidean enclosing spheres. A separately published calculation of the Euclidean diameter and second-largest vertex separation of permutation X-ray polytopes provides a different metric invariant: the diameter only gives \(R_k^2\ge \operatorname{diam}(P_k)^2/4\). Already at \(k=3\), this bound is \(7/2\), strictly below the present exact \(98/23\). Earlier covariance calculations for uniform permutation X-rays concern average fluctuations, not minimax radii or contact sets. The new object here is the complete minimum-ball classification through the first nontrivial loss of a cyclic-shift contact, at order ten.

## Limitations
The proof is a finite, fully enumerated classification through order ten and does not imply the same contact structure in arbitrary dimension. The factorial certificate is exact but does not give a short uniform combinatorial inequality explaining containment for all orders. The claimed historical originality is subject to possible older, unindexed circumradius calculations; no independent mathematical audit has been performed. The reference source's own facet enumeration is not repurposed as evidence for the metric conclusion.

## References
- P. Chaudhary and K. Khandelwal, *Facets of the X-ray polytope of doubly stochastic matrices*, arXiv:2610.30058v1, first public 2026-10-21, https://arxiv.org/abs/2610.30058.
- P. Chaudhary and K. Khandelwal, *Sums of two dependent uniform random variables: a characterization by joint tail bounds*, arXiv:2610.24197, https://arxiv.org/abs/2610.24197 (related probabilistic interpretation).
- *The diameter graph and sharp second-distance gap of permutation X-ray polytopes*, published mathematical research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-diameter-graph-and-sharp-second-distance-gap-of-permutation--215ce1bc6a73 (diameter comparison only).
- G. Birkhoff, *Tres observaciones sobre el álgebra lineal*, Universidad Nacional de Tucumán Revista A 5 (1946), 147–151 (permutation-vertex theorem).
