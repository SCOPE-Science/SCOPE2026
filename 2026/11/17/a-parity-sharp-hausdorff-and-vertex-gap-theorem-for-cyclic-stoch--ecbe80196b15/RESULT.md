# A parity-sharp Hausdorff and vertex-gap theorem for cyclic stochastic permutation polytopes

## Finding
For every integer \(n\ge3\), let \(\mathcal B_n\) be the convex hull, in the Frobenius Euclidean space of real \(n\times n\) matrices, of all permutation matrices. Let \(T_k\) be the cyclic-shift permutation matrix with entries \((T_k)_{i,j}=1\) precisely when \(j-i\equiv k\pmod n\), for \(0\le i,j,k<n\), and set \(\mathcal C_n=\operatorname{conv}\{T_0,\ldots,T_{n-1}\}\). Thus \(\mathcal C_n\) is the simplex of circulant doubly stochastic matrices.

The exact Euclidean Hausdorff distance is
\[
d_H(\mathcal B_n,\mathcal C_n)^2=\begin{cases}n-1,&n\text{ odd},\\n-1-2/n,&n\text{ even}.\end{cases}
\]
Every farthest point of \(\mathcal B_n\) is a permutation matrix. For a permutation \(\pi\) of \(\mathbb Z/n\mathbb Z\), put \(m_k(\pi)=|\{i:\pi(i)-i\equiv k\pmod n\}|\). The nearest point of \(\mathcal C_n\) to its permutation matrix \(P_\pi\) is uniquely
\[
\Pi(P_\pi)=\sum_{k=0}^{n-1}\frac{m_k(\pi)}nT_k.
\]
For odd \(n\), the farthest permutations are exactly those with all \(m_k(\pi)=1\), equivalently the complete mappings (Latin transversals) of the cyclic group. For even \(n\), they are exactly those having one displacement residue \(a\) repeated twice, one residue \(b\) missing, all other residues used once, and \(a-b\equiv n/2\pmod n\). The latter congruence is necessary and automatic for a permutation with this histogram.

Among permutation matrices, the **second-largest distinct squared distance** for every \(n\ge4\) is exactly
\[
d_{\mathrm{second,vertex}}^2=n-1-4/n.
\]
Thus the sharp squared-distance gap below the maximum *among permutation vertices* is \(4/n\) for odd \(n\ge5\), and \(2/n\) for even \(n\ge4\). At \(n=3\), the only squared vertex-distance values are \(2\) and \(0\). These second-level statements do not extend to all points of the continuous polytope: nonvertex points can approach a maximizing vertex continuously.

## Assumptions and scope
All spaces are real; Frobenius norm is \(\|A\|_F=(\sum_{i,j}|A_{ij}|^2)^{1/2}\). The ambient dimension is \(n^2\), not an arbitrarily rescaled intrinsic metric. The two polytopes are closed, and \(\mathcal C_n\subset\mathcal B_n\), so the directed distance from \(\mathcal C_n\) to \(\mathcal B_n\) vanishes. Indices are taken modulo \(n\). The second-level comparison is over the finite set of permutation vertices only. At \(n=2\), the two polytopes coincide, and their Hausdorff distance is zero.

## Proof
**1. Exact projection for arbitrary doubly stochastic matrices.** The shift matrices \(T_k\) are pairwise orthogonal in the Frobenius inner product with \(\langle T_j,T_k\rangle_F=n\delta_{jk}\). The linear space of circulant matrices is their span. Hence the orthogonal projection of any matrix \(X\) onto this linear space equals
\[
\Pi(X)=\sum_{k=0}^{n-1}c_k(X)T_k,\qquad c_k(X)=\frac1n\sum_{i=0}^{n-1}X_{i,i+k}.
\]
For \(X\in\mathcal B_n\), the coefficients are nonnegative and sum to one. Therefore \(\Pi(X)\in\mathcal C_n\); by orthogonality it is the unique nearest point of the **convex** set \(\mathcal C_n\), not merely of its affine span. Pythagoras yields the exact pointwise formula
\[
\operatorname{dist}_F(X,\mathcal C_n)^2=\sum_{i,j}X_{ij}^2-\frac1n\sum_{k=0}^{n-1}\left(\sum_{i=0}^{n-1}X_{i,i+k}\right)^2.
\]
For permutation matrices this becomes
\[
\operatorname{dist}_F(P_\pi,\mathcal C_n)^2=n-\frac1n\sum_{k=0}^{n-1}m_k(\pi)^2,
\qquad \sum_k m_k(\pi)=n.
\]

**2. Combinatorial lower bound and its equality cases.** Since the \(m_k\) are nonnegative integers summing to \(n\),
\[
\sum_k m_k^2=n+\sum_k(m_k-1)^2\ge n.
\]
Equality means every \(m_k=1\). Every displacement multiset of a permutation also obeys
\[
\sum_k k\,m_k\equiv \sum_i(\pi(i)-i)\equiv0\pmod n.
\]
If \(n\) is even, the all-ones histogram would have residue sum \(n(n-1)/2\equiv n/2\pmod n\), so is forbidden. Any nonconstant nonnegative integral histogram summing to \(n\) has \(\sum_k(m_k-1)^2\ge2\), with equality precisely for one entry \(2\), one entry \(0\), and all others \(1\). The congruence forces the repeated and absent classes to differ by \(n/2\).

Both lower bounds are attained. For odd \(n\), take \(\pi(i)\equiv 2i\pmod n\); its displacements visit every residue once. For even \(n=2h\), take
\[
\pi(i)=\begin{cases}2i,&0\le i<h,\\2(i-h)+1,&h\le i<2h.\end{cases}
\]
Its images are respectively all even and all odd residues; its displacement counts are two at residue zero, none at residue \(h\), and one elsewhere. Substitution into the pointwise distance gives the asserted Hausdorff formulas and the vertex equality descriptions.

**3. No nonvertex farthest points.** Define the orthogonal residual \(R(X)=X-\Pi(X)\). For a convex combination \(X=\sum_j\lambda_jP_j\), the exact Hilbert-space variance identity gives
\[
\|R(X)\|_F^2=\sum_j\lambda_j\|R(P_j)\|_F^2-\frac12\sum_{i,j}\lambda_i\lambda_j\|R(P_i)-R(P_j)\|_F^2.
\]
Thus a nontrivial mixture can be maximally distant only if every positively weighted vertex is maximally distant and all their residuals agree. If distinct permutation matrices \(P,Q\) have \(R(P)=R(Q)\), then \(P-Q\) is circulant. Any positive entry of the nonzero circulant matrix \(P-Q\) repeats along a full cyclic diagonal, forcing \(P=T_a\); likewise a negative entry forces \(Q=T_b\). But each cyclic shift is in \(\mathcal C_n\) and has distance zero, whereas the displayed maximum is positive for \(n\ge3\). Therefore distinct maximizing vertices have distinct residuals; no nonvertex maximizer exists.

**4. The sharp second vertex level.** In any integral histogram with sum \(n\), the increment \(\sum_k(m_k-1)^2\) is a nonnegative even integer. The levels below the minimum allowed by Step 2 are therefore separated by at least two units in the histogram square sum. At odd \(n\), the increment \(2\) is forbidden by the same modular sum as before, hence every nonmaximizing permutation has square sum at least \(n+4\). At even \(n\), the best square sum is \(n+2\), so the next possible square sum is at least \(n+4\).

These bounds are attained. For odd \(n\ge5\), start with \(\pi(i)=2i\) and exchange the images at inputs \(0\) and \(1\). The formerly unique displacements \(0,1\) are replaced by \(2,-1\), which are distinct from \(0,1\) and each other, producing exactly two doubled and two missing classes, hence square sum \(n+4\). For even \(n\ge6\), perform the same exchange on the even-order permutation displayed in Step 2. The classes \(0,1\) are replaced with \(2,-1\); \(0\) was the doubled class and \(2,-1\) were singleton classes, yielding square sum \(n+4\). For \(n=4\), the permutation \((0,3,2,1)\) has displacement counts \((2,0,2,0)\) and square sum \(8=n+4\). Directly, at \(n=3\), the three cyclic shifts have distance zero and the three remaining permutations have all displacement counts one. This completes the exact second-level proof.

## Verification
Run `python check_circulant.py` with Python 3. The exact checker exhausts all \(2!+\cdots+8!\) permutations for orders \(2\) to \(8\), verifies the first two histogram-square levels and all maximizing histogram constraints, and checks both all-order constructions for \(3\le n\le1000\). With NumPy/SciPy installed, 48 additional independent constrained least-squares solves compare the formula for nearest circulant matrices against numerical minimization for vertices and interior doubly stochastic matrices. The exact proofs above, not finite enumeration, establish the infinite claims.

## Relationship to prior work
The 2021 study of Rajchel-Mieldzioć, Korzekwa, Puchała and Życzkowski treats circulant unistochastic matrices inside the Birkhoff polytope and their spectral geometry. The 2011 work of Baumeister, Haase, Nill and Paffenholz develops the combinatorics of cyclic permutation polytopes. Circulant Frobenius projection as a stand-alone operation is prior work, including general structured-matrix approximation treatments in 2022 and 2023. The complete-mapping obstruction for even cyclic groups and existence of odd cyclic Latin transversals are also classical; they are not claimed as discoveries here. The present contribution is the *geometric combination*: sharp Hausdorff value between the two specified convex bodies, rigidity of every farthest point, and the exact first nonmaximal vertex-distance level in all dimensions. The inspected references do not explicitly state these results, although earlier unindexed coverage remains possible.

## Limitations
Only the Frobenius metric is addressed; no formula for other Schatten norms is asserted. The second largest squared distance is classified only on the discrete permutation vertex set. Counts of farthest permutations in arbitrary dimension (cyclic Latin transversals and their near analogues) are not evaluated. Historical originality is subject to a broader literature review, and no independent mathematical audit has been performed.

## References
- G. Rajchel-Mieldzioć, K. Korzekwa, Z. Puchała, K. Życzkowski, *Algebraic and geometric structures inside the Birkhoff polytope*, first public arXiv version 2021-01-27, arXiv:2101.11288, https://arxiv.org/abs/2101.11288.
- B. Baumeister, C. Haase, B. Nill, A. Paffenholz, *Permutation Polytopes of Cyclic Groups*, first public arXiv version 2011-09-01, arXiv:1109.0191, https://arxiv.org/abs/1109.0191.
- C. Salahub, *Approximating real symmetric Toeplitz matrices using the nearest circulant*, 2022, arXiv:2208.05771, https://arxiv.org/abs/2208.05771.
- C. Salahub, J. Uhlmann, *Optimal Structured Matrix Approximation for Robustness to Incomplete Biosequence Data*, first public arXiv version 2023-10-23, arXiv:2310.15375, https://arxiv.org/abs/2310.15375.
- L. Bouthat, J. Mashreghi, F. Morneau-Guérin, *On the Geometry of the Birkhoff Polytope. II. The Schatten p-norms*, first public arXiv version 2023-10-21, arXiv:2310.14043, https://arxiv.org/abs/2310.14043.
- L. Goddyn, K. Halasz, *All group-based latin squares possess near transversals*, J. Combin. Designs 28 (2020), 358–365, DOI:10.1002/jcd.21701.
