# A one-step covariance eigenspace transition for complete-bipartite stable-set polytopes

## Finding

Let \(a,b\ge2\) be integers, let \(n=a+b\), and let \(P_{a,b}\subset\mathbb R^a\times\mathbb R^b\) be the standard stable-set polytope of the complete bipartite graph \(K_{a,b}\). If \(X=(X_1,\ldots,X_a,Y_1,\ldots,Y_b)\) is **uniform with respect to full-dimensional Euclidean volume** on \(P_{a,b}\), its covariance has a complete explicitly computable spectrum, given below (some listed eigenvalues coincide at equal block sizes). In particular its largest eigenvalue is always a two-block eigenvalue, while the eigenspace of its smallest eigenvalue changes type at the exact boundary \(\lvert a-b\rvert=2\).

Write \(D=(n+1)(n+2)\) and
\[
 c_a=\frac{(a+1)(a+2)}{12D},\qquad
 c_b=\frac{(b+1)(b+2)}{12D}.
\]
Define the real symmetric matrix
\[
 M=\begin{pmatrix} A & C\\ C & B\end{pmatrix},
\quad A=\frac{(a+1)(a^2+4ab+3a+2b+2)}{12(n+1)^2(n+2)},
\]
\[
 B=\frac{(b+1)(b^2+4ab+3b+2a+2)}{12(n+1)^2(n+2)},\qquad
 C=-\frac{\sqrt{ab}(a+1)(b+1)}{4(n+1)^2(n+2)}.
\]
Then the complete spectrum is
\[
 \{\lambda_+,\lambda_-,c_a\ (a-1\text{ times}),c_b\ (b-1\text{ times})\},
 \qquad \lambda_\pm=\frac{A+B\pm\sqrt{(A-B)^2+4C^2}}2.
\]
The \(c_a\) and \(c_b\) eigenspaces are the zero-sum contrast spaces within their respective parts. The remaining two eigendirections lie in the span of the normalized block-indicator vectors. In every case \(\lambda_+\) is the largest covariance eigenvalue.

Put \(s=\min(a,b)\) and \(t=\max(a,b)\). **The smallest eigenvalue and its exact eigenspace are**
\[
 \lambda_{\min}=\begin{cases}
 \lambda_-,&t-s\le1,\\
 \dfrac{(s+1)(s+2)}{12(n+1)(n+2)},&t-s\ge2.
 \end{cases}
\]
In the second case the smallest eigenspace is precisely the \((s-1)\)-dimensional within-smaller-part contrast space; in the first case it is the one-dimensional block-constant \(\lambda_-\) direction. There are no tie cases for integer \(a,b\ge2\).

For balanced sizes \(a=b=r\), the spectral extrema simplify to
\[
 \lambda_{\max}=\frac1{12},\quad
 \lambda_{\min}=\frac{r^2+r+1}{12(2r+1)^2},\quad
 \kappa=\frac{(2r+1)^2}{r^2+r+1}\longrightarrow4.
\]
For fixed \(a\ge2\) and \(b\to\infty\), the condition number instead obeys the sharp growth law
\[
 \kappa(P_{a,b})\sim\frac{b^2}{(a+1)(a+2)}.
\]
Here \(\kappa\) is the ratio of the largest to smallest eigenvalue of the (positive-definite) covariance operator, **not** an ellipsoidal John or Löwner invariant.

## Assumptions and scope

All coordinates have their standard orthonormal Euclidean metric; no volume-one, intrinsic-hyperplane, or edge-length rescaling is performed. The distribution is continuous uniform volume, not uniform counting measure on stable sets. The exact domain is all integer \(a,b\ge2\). The polytope has full dimension \(n\) and is
\[
 P_{a,b}=\operatorname{conv}\bigl(([0,1]^a\times\{0\})\cup(\{0\}\times[0,1]^b)\bigr)
 =\{(x,y):x_i,y_j\ge0,\ x_i+y_j\le1\text{ for all }i,j\}.
\]
To see the second equality without invoking general perfect-graph theory, take \(u=\max_i x_i\). Each feasible point is \(u\) times an element of the first cube plus \(1-u\) times an element of the second, with the cases \(u=0,1\) read by continuity. Both cubes are convex hulls of their stable-set incidence vertices. The volume is \(a!b!/n!\), although this volume identity is not new.

## Proof

**Step 1 — exact volume moments.** For a uniform point \((x,y)\) in \(P_{a,b}\), let \(U=\max_i x_i\). At a.e. \(u\in(0,1)\), the slice in the \(y\)-variables is \([0,1-u]^b\). Differentiating the volume \(u^a\) of \([0,u]^a\) shows that \(U\) has the beta density proportional to \(u^{a-1}(1-u)^b\), namely \(U\sim\mathrm{Beta}(a,b+1)\). Conditional on \(U=u\), precisely one uniformly selected \(x\)-coordinate equals \(u\), the other \(a-1\) coordinates are independent uniform on \([0,u]\), and all \(y\)-coordinates are independent uniform on \([0,1-u]\). Boundary coincidences have zero volume.

The standard beta identities give
\[
 \mathbb E U=\frac{a}{n+1},\quad
 \mathbb E U^2=\frac{a(a+1)}D,\quad
 \mathbb E(1-U)^2=\frac{(b+1)(b+2)}D,
\]
\[
 \mathbb E\bigl[U(1-U)\bigr]=\frac{a(b+1)}D,
 \qquad\operatorname{Var}(U)=\frac{a(b+1)}{(n+1)^2(n+2)}.
\]
It follows, for distinct indices in the indicated blocks, that
\[
 \mathbb E X_i=\frac{a+1}{2(n+1)},\quad
 \mathbb E Y_j=\frac{b+1}{2(n+1)},
\]
\[
 \mathbb E X_i^2=\frac{(a+1)(a+2)}{3D},\quad
 \mathbb E X_i X_{i'}=\frac{(a+1)(a+2)}{4D},
\]
\[
 \mathbb E Y_j^2=\frac{(b+1)(b+2)}{3D},\quad
 \mathbb E Y_j Y_{j'}=\frac{(b+1)(b+2)}{4D},\quad
 \mathbb E X_i Y_j=\frac{(a+1)(b+1)}{4D}.
\]
Thus the covariance is constant on each of its six coordinate-pair types. The cross-block covariance is the strictly negative quantity
\[
 \operatorname{Cov}(X_i,Y_j)=-\frac{(a+1)(b+1)}{4(n+1)^2(n+2)}.
\]

**Step 2 — exact spectrum.** The symmetry group of the two coordinate blocks leaves invariant the orthogonal decomposition into the two within-part zero-sum spaces and the two-dimensional span of
\[
 e_a=(1,\ldots,1,0,\ldots,0)/\sqrt a,\qquad
 e_b=(0,\ldots,0,1,\ldots,1)/\sqrt b.
\]
On the contrast spaces, diagonal covariance minus off-diagonal covariance gives respectively \(c_a\) and \(c_b\). On \(\operatorname{span}\{e_a,e_b\}\), direct summation of the moments in Step 1 gives exactly \(M\). This proves the displayed spectrum.

**Step 3 — extreme eigenvalues and the transition.** Direct exact algebra yields
\[
 A-c_a=\frac{ab(a+1)}{4(n+1)^2(n+2)}>0,\qquad
 B-c_b=\frac{ab(b+1)}{4(n+1)^2(n+2)}>0.
\]
Since \(\lambda_+\ge\max(A,B)\), the largest eigenvalue exceeds both contrast eigenvalues. For \(a\le b\), we have \(c_a\le c_b\). The decisive identity is
\[
 \det(M-c_a I)=\frac{ab(a+1)(b^2-a^2-3a-3)}{48(n+1)^3(n+2)^2}.
\]
Because \(\lambda_+>c_a\), the sign of this determinant is the sign of \(\lambda_- -c_a\). For integer \(b\ge a\), its last factor is negative for \(b=a\) and \(b=a+1\), but is positive from \(b=a+2\) onward: at these latter two boundary points it equals respectively \(-a-2\) and \(a+1\). Strict monotonicity in \(b\) proves the assertion for all larger differences. Consequently, \(\lambda_-\) is the strict minimum when \(b-a\le1\), and \(c_a\) is the strict minimum when \(b-a\ge2\). Symmetry proves the general case. Neither a nontrivial eigenspace tie nor a missing lower eigenvalue is possible, since these classes are the entire spectrum.

**Step 4 — balanced and unbalanced limits.** Substituting \(a=b=r\) into \(M\) gives
\[
 A=B,\qquad A+|C|=\frac1{12},\qquad
 A-|C|=\frac{r^2+r+1}{12(2r+1)^2}.
\]
The transition establishes the minimum as \(\lambda_-\); taking the ratio proves the balanced formula. If \(a\ge2\) is fixed and \(b\to\infty\), then \(B\to1/12\), \(A\to0\), \(C\to0\), so \(\lambda_+\to1/12\). For all sufficiently large \(b\), the smallest eigenvalue is \(c_a\sim(a+1)(a+2)/(12b^2)\). This proves the quadratic condition-number limit.

## Verification

The accompanying `check_covariance.py` uses **two distinct exact-rational moment calculations**: direct conditional beta integration and a triangulation via linear extensions of an ordinal sum of two antichains. After the isometric reflection \(z_j=1-y_j\), the polytope is the order polytope \(0\le x_i\le z_j\le1\). Its \(a!b!\) equal-volume order chambers correspond to permutations within the two antichains. Uniform points on each chamber are order statistics of \(n\) uniform random variables. The script sums exact first and second order-statistic moments without using the beta formulas, and compares all entries and the spectral identities.

To reproduce from the directory containing the file, run `python3 check_covariance.py`. The checked execution reported:

`BIPARTITE_STABLE_COVARIANCE_CHECKS_PASSED exact_rank_and_beta_profiles=196 threshold_sign_tests=8970`

The 196 pairs comprise every \(2\le a,b\le15\). The second family covers 8,970 integer sign checks. These tests do **not** independently certify the universally quantified polynomial identities; Steps 1–4 give their analytical proof.

## Relationship to prior work

The graph stable-set polytope construction, its vertices and the general geometry of its one-skeleton were treated by Aliniaeifard, Benedetti, Bergeron, Li and Saliola (first public preprint on 2018-04-02). Freij-Hollanti and Lundström (first public preprint 2023-12-21) explicitly treat ordinal sums and the associated subdirect sums of order and chain polytopes, including the construction underlying this two-antichain family. Davis and Kohl (2022) study Ehrhart invariants of stable-set polytopes of graph complements. These results cover definitions and combinatorial structure, **not** the uniform-volume covariance eigenvalues or the sharp eigenspace transition established here.

Two published calculations concerning the **exact same two-level order/chain polytope** have also been inspected in full: the balanced and unbalanced John-ellipsoid constructions (published-finding corpus, 2026-10-11, identifiers ending `8659155ecca7` and `c200d8f4f023`). They compute unique largest-volume **inscribed ellipsoids** and their facet contact weights. Their ellipsoid shape matrices are not the covariance operators of uniform **volume** distributions, and their theorems neither evaluate the latter moments nor determine the strict spectral crossing at block-size difference two. This comparison distinguishes the two invariants; it is not a claim that every possible equivalent source has been located.

The standard order-statistic moments and block symmetry used in the proof are classical facts; their use alone is not claimed as new. The proposed contribution is the **complete Euclidean covariance spectrum, strict one-step eigenspace transition, and contrasting balanced/unbalanced anisotropy laws** for this graph-polytope family.

## Limitations

This is a self-reviewed mathematical argument, not independently audited or historically priority certified. The literature review included source-text inspection of the specifically relevant papers listed below and comparisons with related published geometric findings. A previously known equivalent expression through order-statistic covariance matrices or chain-polytope second moments is possible. The formulas apply only to the standard Euclidean metric, the exact \(K_{a,b}\) family with \(a,b\ge2\), and the continuous uniform-volume law; they do not describe uniform random vertices, arbitrary bipartite graphs, or John/Löwner ellipsoids. No monotonicity of condition number across all fixed-sum parameter pairs is asserted.

## References

1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (v1 2018-04-02; inspected accessible full HTML v3), https://arxiv.org/abs/1804.00360 .
2. R. Freij-Hollanti and T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890 (v1 2023-12-21; inspected accessible full-text rendering), https://arxiv.org/abs/2312.13890 .
3. R. Davis and F. Kohl, *Perfectly Matchable Set Polynomials and \(h^*\)-polynomials for Stable Set Polytopes of Complements of Graphs*, arXiv:2207.14759 (v1 2022-07-29; inspected accessible full-text rendering), https://arxiv.org/abs/2207.14759 .
4. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. For the classical order/chain-polytope framework; not a qualifying date anchor.
5. *Exact John ellipsoid of balanced two-layer order polytopes*, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-john-ellipsoid-of-balanced-two-layer-order-polytopes--8659155ecca7 (full RESULT.md inspected; same polytope, different invariant).
6. *Exact John ellipsoid of unbalanced two-layer chain and order polytopes*, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-john-ellipsoid-of-unbalanced-two-layer-chain-and-order-pol--c200d8f4f023 (full RESULT.md inspected; same polytope, different invariant).
