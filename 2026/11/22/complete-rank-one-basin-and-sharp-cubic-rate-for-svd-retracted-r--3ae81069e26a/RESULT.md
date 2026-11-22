# Complete rank-one basin and sharp cubic rate for SVD-retracted Riemannian Gauss–Newton

## Finding
For full observations of any real rank-one target, SVD-retracted rank-one Riemannian Gauss–Newton converges from every nonzero rank-one starting matrix except those whose left and right column spaces are **both** perpendicular to the respective true factors. If either starting factor is already aligned, it terminates in one iteration; if exactly one factor is orthogonal, it terminates in two. Every remaining start has strictly improving left and right principal angles, never terminates finitely, and converges with a sharp **cubic** logarithmic precision rate:
\[
\lim_{k\to\infty}\frac1k\log\log\left(\frac{\|X_\star\|_F}{\|X_k-X_\star\|_F}\right)=\log 3.
\]
The convergence statement includes arbitrary nonzero singular scales at initialization and arbitrary ambient dimensions at least two. The cubic rate is specific to the singular-value-decomposition retraction; an orthographic retraction has a different population behavior.

## Assumptions and scope
Fix integers \(m,n\ge2\), unit vectors \(u_\star\in\mathbb R^m\), \(v_\star\in\mathbb R^n\), and a nonzero scalar \(\gamma\). Let the observed target be \(X_\star=\gamma u_\star v_\star^\top\). By absorbing the target sign and scaling, the proof below uses \(\gamma=1\); the algorithm and error rescale homogeneously. Start from any nonzero rank-one \(X_0\in\mathbb R^{m\times n}\), with unit left and right singular directions \(u_0,v_0\) (each defined up to sign). No restriction is placed on its nonzero singular magnitude.

For a current nonzero rank-one \(X_k\) having factor spans \(\operatorname{span}(u_k)\) and \(\operatorname{span}(v_k)\), its embedded fixed-rank tangent-space projection is
\[
P_{T_k}(Z)=Z-(I-u_ku_k^\top)Z(I-v_kv_k^\top).
\]
With the identity measurement operator (noiseless full Frobenius observations), consider the Gauss–Newton tangent solve followed by **best rank-one SVD retraction**:
\[
W_k=P_{T_k}(X_\star),\qquad X_{k+1}=\mathcal T_1(W_k),
\]
where \(\mathcal T_1(W)\) is its unique largest-singular-value rank-one approximation whenever the top singular value is strictly greater than the second and is positive. A zero \(W\) is excluded from the rank-one manifold, so the rule does not define its next rank-one iterate. The method is the full-observation specialization of the SVD-retracted Riemannian Gauss–Newton update in Wu–Cai–Xu–Yang [1].

Write \(a_k=\sqrt{1-|u_k^\top u_\star|^2}\) and \(b_k=\sqrt{1-|v_k^\top v_\star|^2}\) for the principal-angle sines. If \(a_k=b_k=1\), then \(W_k=0\). If \(a_k=0\) or \(b_k=0\), the next iterate equals \(X_\star\). If exactly one of \(a_k,b_k\) equals one and the other is strictly smaller, the first update aligns the orthogonal factor, and the second equals \(X_\star\).

For the nontrivial case \(0<a_0,b_0<1\), all iterates exist, \(0<a_{k+1}<a_k\), \(0<b_{k+1}<b_k\), both angle errors tend to zero, and
\[
a_{k+1}=a_k b_k^2\left[1+O(a_k^2+b_k^2)\right],\qquad
b_{k+1}=a_k^2 b_k\left[1+O(a_k^2+b_k^2)\right].
\]
The big-O estimates are uniform in a fixed sufficiently small angle neighborhood, with numerical constants independent of dimension. The displayed double-logarithmic limit holds for these nontrivial starts; it is not asserted for finite-termination cases, where the logarithm becomes infinite.

## Proof
**1. Reduction to a two-dimensional plane on each side.** Since \(W_k\) is built from the target and current one-dimensional factor spaces, its nonzero singular vectors lie in \(\operatorname{span}(u_\star,u_k)\) and \(\operatorname{span}(v_\star,v_k)\). Orient the current factors so their overlaps with the target are nonnegative. Set \(a=\sin\theta\), \(b=\sin\phi\), \(c=\cos\theta=\sqrt{1-a^2}\), \(d=\cos\phi=\sqrt{1-b^2}\). In orthonormal bases \((u,u_\perp)\), \((v,v_\perp)\), where \(u_\star=c u+a u_\perp\) and \(v_\star=d v+b v_\perp\), direct substitution gives
\[
W=\begin{pmatrix}cd&cb\\ad&0\end{pmatrix}.
\]
This expression does not depend on the initial singular magnitude. Its squared leading singular value is simple for all \(0<a,b<1\): the off-diagonal entries of both positive semidefinite Gram matrices are strictly positive.

**2. Strict improvement and convergence for every interior start.** The left Gram matrix is
\[
WW^\top=\begin{pmatrix}c^2&ac d^2\\ac d^2&a^2d^2\end{pmatrix}.
\]
If \(\lambda_+\) denotes its larger eigenvalue, strict positivity of the off-diagonal gives \(\lambda_+>c^2\). Its determinant is \(a^2b^2c^2d^2>0\), hence \(\lambda_+<\operatorname{tr}(WW^\top)=c^2+a^2d^2\). Thus the leading left eigenvector, represented by \((1,t)\) in these bases, has
\[
0<t=\frac{\lambda_+-c^2}{ac d^2}<\frac ac.
\]
It lies strictly between the old left direction \(u\) and the true direction \(u_\star\). Hence its principal-angle sine satisfies \(0<a_{+}<a\). Exchanging left and right gives \(0<b_{+}<b\), since
\[
W^\top W=\begin{pmatrix}d^2&bd c^2\\bd c^2&b^2c^2\end{pmatrix}.
\]
For interior starts, both angle sequences decrease and remain strictly positive. Suppose their limits are \(a_\infty,b_\infty\). The update is continuous through the interior and through each singly aligned boundary. A positive interior limit contradicts strict improvement, and a limit with exactly one zero forces the other angle to zero at the next update, since \(W=X_\star\) on that boundary. Therefore both limits are zero. Positivity at each finite step excludes finite termination in the interior case.

**3. Cubic local angle map.** In bases with first axes \(u_\star,v_\star\), the same tangent projection has exact form
\[
W=\begin{pmatrix}
1-a^2b^2&a^2bd\\ab^2c&-abcd
\end{pmatrix}.
\]
Its Gram off-diagonal entries factor exactly as
\[
(WW^\top)_{12}=ab^2c^3,\qquad
(W^\top W)_{12}=a^2bd^3.
\]
The gaps between the respective Gram eigenvalues equal \(1+O(a^2+b^2)\) as \(a,b\to0\). For the dominant normalized eigenvector of a real symmetric \(2\times2\) matrix with diagonal gap tending to one, its second coordinate equals the off-diagonal entry times \(1+O(a^2+b^2)\). Consequently,
\[
\frac{a_+}{ab^2}=1+O(a^2+b^2),\qquad
\frac{b_+}{a^2b}=1+O(a^2+b^2).
\]
The leading singular value \(s_+(W)\) satisfies \(1-a^2b^2\le s_+(W)\le\|W\|_F\le1\); the last inequality uses orthogonality of the tangent projector. Thus the retracted amplitude error is \(O(a^2b^2)\), of higher order than the new angle errors. The strictly positive singular vectors of the old-basis matrix can be oriented with positive target overlaps, so, writing \(s=s_+(W)\), the next-error identity is
\[
\|X_+-X_\star\|_F^2=(s-1)^2+2s\left(1-\sqrt{1-a_+^2}\sqrt{1-b_+^2}\right).
\]
Its right side is \((1+o(1))(a_+^2+b_+^2)\) as the angle errors vanish; in particular the matrix error is comparable to \(\max(a_+,b_+)\).

**4. Exact double-logarithmic exponent.** Define \(p_k=-\log a_k\), \(q_k=-\log b_k\) for an interior orbit. The two cubic angle recurrences give
\[
\binom{p_{k+1}}{q_{k+1}}
=\begin{pmatrix}1&2\\2&1\end{pmatrix}\binom{p_k}{q_k}+o(1).
\]
Hence \(S_k=p_k+q_k\) obeys \(S_{k+1}=3S_k+o(1)\), while \(D_k=p_k-q_k\) obeys \(D_{k+1}=-D_k+o(1)\). Since \(S_k\to\infty\), elementary variation of constants gives \(S_k=C3^k+O(1)\) with \(C>0\); and \(D_k=O(k)\), so
\[
\min(p_k,q_k)=\tfrac C2 3^k+o(3^k).
\]
Since \(-\log\|X_k-X_\star\|_F=\min(p_k,q_k)+O(1)\) as \(k\to\infty\), taking another logarithm yields the asserted exact exponent \(\log3\). Reintroducing \(\gamma\ne0\) only changes errors by its absolute scale and leaves the limit unchanged.

**5. Boundary starts.** If both \(c=d=0\), the projected target is zero. If \(a=0\) or \(b=0\), the projected target equals \(X_\star\). When \(c=0,d>0\), the projected matrix is \(W=d u_\star v^\top\), so its SVD retraction sets the left factor exactly and leaves the right factor unchanged, after which \(W=X_\star\). The symmetric case \(d=0,c>0\) is analogous. This exhausts all starts, proving the classification.

## Verification
The included `verify.py` implements the tangent-space formula and truncated SVD independently in NumPy, checks exact rational Gram identities, strict contraction for interior starts, ambient-dimension consistency, degenerate boundaries and the leading cubic coefficients. It produced **15,310 passed assertions**. These finite checks are diagnostic only; the proof above establishes the universal statement over all dimensions and initializations. Reproduce using `python verify.py` with Python 3 and NumPy installed.

## Relationship to prior work
Wu, Cai, Xu and Yang [1, §2, Algorithm 1] specify precisely this tangent solve followed by truncated-SVD retraction, and establish sample-complexity and local Q-quadratic estimates for Gaussian observations and spectral initialization. The full-observation all-start classification, exact exceptional set and cubic (rather than merely quadratic) asymptotic are additional deterministic properties of that SVD-retracted rule. Cai, Lu and You [2, Lemma 5.3 and Appendix C.2.3] prove a population **orthographic** retraction identity giving one-step recovery in a local neighborhood; it is not the SVD retraction here and does not imply a cubic SVD orbit. The general retraction survey [3] distinguishes SVD and orthographic retractions, while Hou, Li and Zhang [4] analyze gradient descent (not Gauss–Newton) with random initialization. The earlier recursive importance sketching method [5, §3.3] employs **orthographic** retraction and proves quadratic convergence, rather than this SVD-specific global cubic dynamics. The matrix formulas in this note are proved directly rather than inferred from those broader theories.

## Limitations
This is a noiseless full-data baseline on the real rank-one manifold. It assumes exact tangent solves and exact singular-value decomposition; it does not prove the same basin or rate under incomplete measurements, noise, numerical rounding, higher rank, non-SVD retractions or constrained initialization. The double-orthogonal start has a zero tangent projection rather than an infinite-error estimate. The result is not a claim of absolute priority against every unindexed source.

## References
[1] X. Wu, J.-F. Cai, Z. Xu, and Z. Yang, *Rank-Optimal Sample Complexity of Riemannian Gauss-Newton for Low-Rank Matrix Recovery*, arXiv:2611.01542v1, publicly posted 2026-11-01. https://arxiv.org/html/2611.01542v1

[2] J.-F. Cai, X. Lu, and J. You, *Near-Optimal Nonconvex Matrix Completion*, arXiv:2609.17048, 2026. https://arxiv.org/abs/2609.17048

[3] P.-A. Absil and I. Oseledets, *Low-rank retractions: a survey and new results*, technical report, 2014. https://sites.uclouvain.be/absil/2013-04/low_rank_retraction_13PA_techrep.pdf

[4] T. Y. Hou, Z. Li, and Z. Zhang, *Fast Global Convergence for Low-rank Matrix Recovery via Riemannian Gradient Descent with Random Initialization*, arXiv:2012.15467, 2020. https://arxiv.org/abs/2012.15467

[5] Y. Luo, W. Huang, X. Li, and A. R. Zhang, *Recursive Importance Sketching for Rank Constrained Least Squares: Algorithms and High-order Convergence*, arXiv:2011.08360v4, 2022; *Operations Research* 72 (2024), 237–256. https://arxiv.org/pdf/2011.08360
