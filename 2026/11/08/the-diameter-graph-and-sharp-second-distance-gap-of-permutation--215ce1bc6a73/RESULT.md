# The diameter graph and sharp second-distance gap of permutation X-ray polytopes

## Finding

Let \(\mathcal B_k\) be the \(k\)-by-\(k\) Birkhoff polytope, with rows and columns indexed by \(0,\ldots,k-1\). For a matrix \(Z\), define its anti-diagonal X-ray \(T_k(Z)\in\mathbb R^{2k-1}\) by
\[
  T_k(Z)_t=\sum_{0\le i,j<k\,;\,i+j=t} Z_{ij}
  \qquad(0\le t\le 2k-2).
\]
Equip \(\mathcal X_k=T_k(\mathcal B_k)\) with its **ambient standard Euclidean metric on these \(2k-1\) X-ray coordinates**. Let \(e_t\) denote the corresponding coordinate unit vectors and set
\[
 H_k=k e_{k-1},\qquad
 L_k=(k-1)e_{k-2}+e_{2k-2},\qquad
 U_k=(k-1)e_k+e_0.
\]

**Theorem (complete diameter graph).** For every integer \(k\ge2\),
\[
 \operatorname{diam}_2(\mathcal X_k)^2=2k^2-2k+2.
\]
The **entire set of unordered pairs of points** attaining this diameter is
\[
 \big\{\{H_k,L_k\},\{H_k,U_k\}\big\}.
\]
When \(k=2\), the two listed pairs coincide and there is just one diametral pair; for every \(k\ge3\), they are distinct. In particular these are vertices, and no pair involving a nonvertex point is diametral.

**Theorem (sharp finite-image second-distance gap).** Let
\[
 \mathcal V_k=\big\{T_k(P_\pi):\pi\in S_k\big\}
\]
be the **set of distinct projected permutation X-rays**, rather than all points of its convex hull. For \(k\ge4\), the second-largest squared distance between two distinct elements of \(\mathcal V_k\), strictly below the squared diameter, is
\[
 D_2(k)=2k^2-4k+8;
 \qquad D_1(k)-D_2(k)=2(k-3).
\]
At \(k=3\) the second-largest value is \(10\), versus diameter square \(14\); at \(k=2\) there is no second positive distance. The runner-up statement is only about the finite set \(\mathcal V_k\): points of the continuum \(\mathcal X_k\) have distances arbitrarily close to its diameter.

These assertions may equivalently be interpreted for probability distributions of a sum of two variables with uniform \(k\)-point marginals: dividing each X-ray vector by \(k\) divides all distances by \(k\).

## Assumptions and scope

The integers satisfy \(k\ge2\). A permutation matrix \(P_\pi\) has ones at positions \((i,\pi(i))\) and zeros elsewhere. The object is the **linear image** of the Birkhoff polytope under the stated anti-diagonal sum map, not the Birkhoff polytope with its Frobenius metric and not a differently rescaled X-ray realization. Repeated permutation matrices with the same X-ray are identified in \(\mathcal V_k\). Coordinate indices are zero-based. The result uses no genericity assumption and applies to all convex combinations in \(\mathcal X_k\).

## Proof

**1. Reduction to finitely many integer X-rays.** The Birkhoff--von Neumann theorem gives
\[
 \mathcal X_k=\operatorname{conv}\mathcal V_k.
\]
Each \(h\in\mathcal V_k\) is an integral vector with nonnegative coordinates and total coordinate sum \(k\). It can have coordinate value \(k\) only if all its permutation-matrix ones lie on one anti-diagonal containing \(k\) cells. The only anti-diagonal of length \(k\) is \(t=k-1\), and its full occupancy forces the reversal permutation. Thus \(H_k\) is the unique image having any coordinate of size \(k\).

**2. Bounding all distances between images not equal to \(H_k\).** If \(h\ne H_k\), its entries are nonnegative integers summing to \(k\), each at most \(k-1\), hence
\[
 \|h\|_2^2\le (k-1)^2+1.
\]
This is the elementary concentration bound obtained by moving units from smaller positive entries into larger entries until the available cap is met. For distinct \(u,v\in\mathcal V_k\setminus\{H_k\}\), nonnegativity gives \(\langle u,v\rangle\ge0\), and so
\[
 \|u-v\|_2^2\le2\big((k-1)^2+1\big)
   =2k^2-4k+4<2k^2-2k+2.
\]
Therefore every diametral image pair contains \(H_k\).

**3. All equality cases with \(H_k\).** For \(h\ne H_k\),
\[
 \|H_k-h\|_2^2
   =k^2+\|h\|_2^2-2k h_{k-1}
   \le k^2+(k-1)^2+1.
\]
Equality requires \(h_{k-1}=0\) and the multiset of its positive coordinate masses to be \(\{k-1,1\}\) (for \(k=2\), the same multiset has two ones). An anti-diagonal holding \(k-1\) permutation ones must have at least \(k-1\) cells. The only candidates are \(t=k-2,k-1,k\). If \(t=k-1\) holds \(k-1\) ones, the remaining unused row and column form the missing cell on that same central anti-diagonal, forcing all \(k\) ones there; thus it is \(H_k\), which is excluded. If \(t=k-2\), all its \(k-1\) cells must be occupied, leaving only row and column \(k-1\); the final one is at \((k-1,k-1)\), giving \(L_k\). The reflected case \(t=k\) leaves \((0,0)\), giving \(U_k\). Conversely these two permutations exist and attain equality. This proves the exact image-pair classification and diameter value.

**4. Why no other points of the polytope attain the diameter.** Write any \(x,y\in\mathcal X_k\) as convex combinations of distinct images,
\(x=\sum_u\alpha_u u\) and \(y=\sum_v\beta_v v\). Strict convexity of squared Euclidean norm gives
\[
 \|x-y\|_2^2
 \le\sum_{u,v}\alpha_u\beta_v\|u-v\|_2^2
 \le 2k^2-2k+2.
\]
Equality requires every \((u,v)\) with positive product weight to be a diametral image pair, and their difference vectors to be identical. But the only unordered image pairs are \(\{H_k,L_k\}\) and \(\{H_k,U_k\}\); for \(k\ge3\) these have different difference vectors, and for \(k=2\) they coincide as one pair. Consequently both convex combinations must be singletons. This proves the entire diameter graph, including the absence of nonvertex contacts.

**5. The second-largest finite-image distance.** Now assume \(k\ge4\). Step 2 bounds any pair avoiding \(H_k\) by \(2k^2-4k+4\). If \(h\in\mathcal V_k\) is neither \(H_k\) nor \(L_k,U_k\) and \(h_{k-1}\ge1\), then Step 3 gives
\[
 \|H_k-h\|_2^2\le 2k^2-4k+2.
\]
If \(h_{k-1}=0\), Step 3 implies \(\max_t h_t\le k-2\), since a mass of \(k-1\) would force \(L_k\) or \(U_k\). By the same concentration argument as Step 2, now with cap \(k-2\ge2\),
\[
 \|h\|_2^2\le (k-2)^2+2^2,
 \qquad
 \|H_k-h\|_2^2\le 2k^2-4k+8.
\]
To attain this bound, choose the permutation defined by
\[
 \pi(i)=k-3-i\quad(0\le i\le k-3),
 \qquad\pi(k-2)=k-1,
 \qquad\pi(k-1)=k-2.
\]
Its X-ray is
\[
 W_k=(k-2)e_{k-3}+2e_{2k-3},
\]
which has no central mass and satisfies \(\|H_k-W_k\|_2^2=2k^2-4k+8\). This proves the sharp runner-up formula and the exact gap. For \(k=3\), the five distinct X-rays are
\[
 (1,0,1,0,1),\quad (1,0,0,2,0),\quad (0,2,0,0,1),
 \quad(0,1,1,1,0),\quad(0,0,3,0,0).
\]
Checking their ten unordered distances gives maximum squared distance \(14\) and next value \(10\), attained for example between \( (0,2,0,0,1)\) and \( (1,0,0,2,0)\). At \(k=2\) the distinct image set has only two points, so no runner-up exists. The proof is complete.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library and exact integer arithmetic. It enumerates all projected X-rays through \(k=8\); it exhaustively checks all unordered distinct image pairs for \(k=2,\ldots,7\); it checks the projection-profile inequalities through \(k=8\), additional deterministic random cases up to \(k=15\), and explicit sharp witnesses through \(k=100\). Executing it produced:

`PASS: 694526 exact-integer assertions; complete projected-X-ray pair checks for k=2,...,7, projection-profile checks through k=8, and constructed exact witnesses through k=100.`

These finite tests corroborate but do not establish the infinite-family proof. The inequalities, equality classification, and runner-up construction in the proof establish the universal statements.

## Relationship to prior work

Chaudhary and Khandelwal [1] define and classify facets of exactly this X-ray image. Their treatment reveals a polytope with rapidly growing facial complexity, but does not give Euclidean diameter, equality pairs, or a second-distance gap. Li, Liu and Yao [2] study feasibility of binary X-rays, and Bebeacua, Mansour, Postnikov and Severini [3] study permutation X-ray degeneracies and enumeration. Bouthat, Mashreghi and Morneau-Guérin [4] determine the diameter of the **original** Birkhoff polytope under matrix norms, including Frobenius (Schatten-2) distance; their formula is not a theorem about the non-isometric anti-diagonal aggregation image. The classical Birkhoff--von Neumann theorem is used explicitly and is not claimed as new.

## Limitations

The norm is the unweighted ambient Euclidean norm on unnormalized anti-diagonal sums; changing coordinate weights changes the problem. The second-distance gap is a discrete fact about distinct projected permutation X-rays, not a forbidden annulus of distances between arbitrary continuous polytope points. No claim is made about the complete distance distribution, all edges of the one-skeleton, or other normed metrics. Published-priority assessment is provisional: the closely related Brualdi--Fritscher work on Hankel and Toeplitz X-rays was identifiable but its full text was not accessible for a decisive page-level comparison; its accessible description concerns combinatorial X-rays rather than the Euclidean metric.

## References

[1] P. Chaudhary and K. Khandelwal, *Facets of the X-ray polytope of doubly stochastic matrices*, arXiv:2610.30058v1 (first public 2026-10-21). https://arxiv.org/abs/2610.30058

[2] B. Li, Y. Liu and Y. Yao, *Binary X-rays of doubly stochastic matrices*, arXiv:2608.01442 (2026). https://arxiv.org/abs/2608.01442

[3] C. Bebeacua, T. Mansour, A. Postnikov and S. Severini, *On the X-rays of permutations*, arXiv:math/0506334 (2005). https://arxiv.org/abs/math/0506334

[4] L. Bouthat, J. Mashreghi and F. Morneau-Guérin, *The diameter of the Birkhoff polytope*, Special Matrices 12 (2024), article 20230113. https://doi.org/10.1515/spma-2023-0113

[5] R. A. Brualdi and E. Fritscher, *Hankel and Toeplitz X-rays of permutations*, Linear Algebra and its Applications (2014). https://doi.org/10.1016/j.laa.2014.02.037
