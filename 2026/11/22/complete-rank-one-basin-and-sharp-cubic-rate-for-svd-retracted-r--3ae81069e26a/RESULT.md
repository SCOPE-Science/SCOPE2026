# Complete rank-one basin and sharp cubic rate for SVD-retracted Riemannian Gauss–Newton

## Finding

For exact, noiseless full observations of a nonzero real rank-one target, the SVD-retracted rank-one Riemannian Gauss–Newton iteration is defined and converges from every nonzero rank-one matrix except when both its column space and its row space are perpendicular to those of the target. At that exceptional set the tangent projection vanishes and there is no next rank-one iterate. The complete classification of the other starts is:

- If either factor span already matches its target span, the next update returns the target. This includes the case where the other factor span is perpendicular to its target span.
- If neither factor span matches its target span and exactly one is perpendicular to its target span, the iteration reaches the target in exactly two updates.
- If both principal angles lie strictly between zero and \(\pi/2\), both angles decrease strictly at every step and no iterate equals the target. The sharp logarithmic precision rate is
  \[
  \lim_{k\to\infty}\frac1k\log\log\left(\frac{\|X_\star\|_F}{\|X_k-X_\star\|_F}\right)=\log 3.
  \]

The starting singular magnitude is arbitrary and nonzero. The cubic angle map below is for SVD retraction; an orthographic retraction can have different population dynamics.

## Assumptions and scope

Let \(m,n\ge2\), \(X_\star=\gamma u_\star v_\star^\top\), where \(\gamma\ne0\) and \(u_\star,v_\star\) are real unit vectors. Let \(X_0\) be nonzero and rank one. If \(u_k,v_k\) are its current unit singular directions, put
\[
  P_{T_k}(Z)=Z-(I-u_ku_k^\top)Z(I-v_kv_k^\top),\qquad
  W_k=P_{T_k}(X_\star),\qquad X_{k+1}=\mathcal T_1(W_k).
\]
The first formula is the orthogonal projector onto the embedded rank-one tangent space. For the identity observation operator the Gauss–Newton step projects \(X_\star-X_k\) to that tangent space; since \(P_{T_k}(X_k)=X_k\), adding the step gives \(W_k\). Here \(\mathcal T_1\) denotes the truncated SVD, unique when the leading singular value is positive and simple. The exceptional zero projection is not retracted to a rank-one iterate. The proof sets \(\gamma=1\): rescaling the target rescales each projected and retracted matrix by the same factor, preserving the spans, the strict ordering of singular values and the relative Frobenius error.

## Proof

**1. Interior starts and monotonicity.** Suppress the iteration index. Define \(a,b\) as the sines of the left and right principal angles to the target and set \(c=\sqrt{1-a^2}\), \(d=\sqrt{1-b^2}\). In the interior all four numbers are positive. Choose signs of the current factors to have positive target overlaps, and choose unit \(u_\perp,v_\perp\) with \(u_\star=cu+au_\perp\), \(v_\star=dv+bv_\perp\). The projected matrix has nonzero singular directions in these two-dimensional planes. In the bases starting with \(u,v\), the matrix and its Gram matrices are
\[
 W=\begin{pmatrix}cd&cb\\ad&0\end{pmatrix},\quad
 WW^\top=\begin{pmatrix}c^2&ac d^2\\ac d^2&a^2 d^2\end{pmatrix},\quad
 W^\top W=\begin{pmatrix}d^2&bd c^2\\bd c^2&b^2 c^2\end{pmatrix}.
\]
The leading eigenvalue \(\lambda_+\) of \(WW^\top\) is simple and exceeds \(c^2\) by strict positivity of the off-diagonal. The determinant is \(a^2b^2c^2d^2>0\), so \(\lambda_+<c^2+a^2d^2\), the trace. The leading left eigenvector has positive first coordinate and slope
\[
 0<\frac{\lambda_+-c^2}{ac d^2}<\frac ac.
\]
Thus the updated direction is strictly between the old and true directions: \(0<a_+<a\). The right Gram matrix gives \(0<b_+<b\) by the same argument. This proves uniqueness, strict decrease and nontermination in the interior. The two angle sines have limits in \([0,a_0]\times[0,b_0]\) with both upper bounds strictly below one. The angle update is continuous there: the leading singular value is simple in the interior and at aligned boundaries, where the projected target is the target itself. An interior limit would violate strict decrease at a fixed point, and a boundary point with one angle zero maps to both angles zero. The two angle sines therefore tend to zero.

**2. Cubic angle map and relative matrix error.** In the bases starting with the target directions, oriented so the current directions have coordinates \((c,a)\) and \((d,b)\), the same projection has matrix
\[
 W=\begin{pmatrix}1-a^2b^2&a^2bd\\ab^2c&-abcd\end{pmatrix}.
\]
The Gram off-diagonals are exactly \((WW^\top)_{12}=ab^2c^3\) and \((W^\top W)_{12}=a^2bd^3\). The gaps between the respective diagonal entries are \(1+O(a^2+b^2)\). For a real symmetric two-by-two Gram matrix with such a diagonal gap and off-diagonal entry \(h\), the dominant eigenvector has slope \(h/(\lambda_+-G_{22})\) over the first axis. Since \(\lambda_+-G_{22}=1+O(a^2+b^2)\), normalization gives its second coordinate as \(h[1+O(a^2+b^2)]\). Consequently
\[
 a_+=ab^2[1+O(a^2+b^2)],\qquad b_+=a^2b[1+O(a^2+b^2)].
\]
The estimates are uniform in a fixed sufficiently small angle neighborhood with dimension-independent constants. The leading singular value \(s\) satisfies \(1-a^2b^2\le s\le\|W\|_F\le1\), from the target-axis entry and orthogonality of the projection. The leading left and right singular vectors can be paired with positive target overlaps, since in the old-factor bases the leading Gram eigenvectors have positive entries and \(W\) has nonnegative entries. Thus
\[
 \|X_+-X_\star\|_F^2=(s-1)^2+2s(1-\sqrt{1-a_+^2}\sqrt{1-b_+^2}).
\]
The scale error is \(O(a^2b^2)=o(\max(a_+,b_+))\) by the displayed angle formulas, so the squared matrix error is \((1+o(1))(a_+^2+b_+^2)\). In particular, the iterates converge in Frobenius norm.

**3. Sharp double-logarithmic exponent.** For an interior orbit put \(p_k=-\log a_k\), \(q_k=-\log b_k\). The angle recurrences yield \(p_{k+1}=p_k+2q_k+o(1)\) and \(q_{k+1}=2p_k+q_k+o(1)\). Set \(S_k=p_k+q_k\), \(D_k=p_k-q_k\). Then \(S_{k+1}=3S_k+o(1)\) and \(D_{k+1}=-D_k+o(1)\). The errors are bounded, so the increments of \(3^{-k}S_k\) are absolutely summable with tail \(O(3^{-k})\), giving \(S_k=C3^k+O(1)\). Necessarily \(C>0\) because \(S_k\to\infty\). The other recurrence gives \(D_k=O(k)\). It follows that \(\min(p_k,q_k)=C3^k/2+O(k)\), and the matrix error comparison gives \(-\log\|X_k-X_\star\|_F=\min(p_k,q_k)+O(1)\) in the normalized problem. This proves the stated double-logarithmic limit. No rate limit is asserted for finite termination.

**4. Boundary starts.** If both directions are perpendicular to their targets, the normal part is the full target, leaving \(W=0\). If one span matches its target span, the normal part vanishes and the first update is the target regardless of the other span. Otherwise, if \(c=0\) and \(d>0\), we have \(0<b<1\) and \(W=d u_\star v^\top\). This rank-one matrix aligns the left span but leaves the still nonaligned right span unchanged, so it is not the target. The next update is the target. Exchanging the sides gives the same conclusion when \(d=0\) and \(c>0\) and the left span is nonaligned. These cases and the interior exhaust all starts.

## Verification

The unchanged `verify.py` checks exact rational Gram identities, strict interior contraction in finite numerical cases, higher-dimensional consistency, boundary projection formulas and the leading cubic coefficients. Run `python verify.py` from the original support-file directory using Python 3 and NumPy. The original verification reports 15,310 assertions. These are diagnostic checks; the proof is the universal convergence argument.

## Relationship to prior work

Wu, Cai, Xu and Yang [1, §2.2 and Algorithm 1] define the tangent least-squares update with truncated-SVD retraction. Their Theorem 3.1 gives a local quadratic guarantee under Gaussian sensing and spectral initialization, not the deterministic rank-one basin or exact double-logarithmic rate here. Cai, Lu and You [2, Eq. (14), Lemma 5.3] prove a local population one-step identity for **orthographic** retraction, not the SVD retraction. Absil and Oseledets [3] distinguish these retractions. Hou, Li and Zhang [4] analyze gradient descent, not this map. The recursive importance sketching method [5] uses an orthographic retraction and gives a local quadratic result under its sensing assumptions. No absolute priority is claimed.

## Limitations

The theorem is for the real rank-one manifold, exact tangent solves and exact SVD with full noiseless observations. It does not imply the same basin or rate for incomplete observations, noise, rounding, higher rank, or other retractions.

## References

1. X. Wu, J.-F. Cai, Z. Xu and Z. Yang, *Rank-Optimal Sample Complexity of Riemannian Gauss-Newton for Low-Rank Matrix Recovery*, arXiv:2611.01542v1, https://arxiv.org/html/2611.01542v1.
2. J.-F. Cai, X. Lu and L. You, *Near-Optimal Nonconvex Matrix Completion*, arXiv:2609.17048, https://arxiv.org/abs/2609.17048.
3. P.-A. Absil and I. Oseledets, *Low-rank retractions: a survey and new results*, 2014, https://sites.uclouvain.be/absil/2013-04/low_rank_retraction_13PA_techrep.pdf.
4. Y. Hou, Z. Li and Z. Zhang, *Fast Global Convergence for Low-rank Matrix Recovery via Riemannian Gradient Descent with Random Initialization*, arXiv:2012.15467, https://arxiv.org/abs/2012.15467.
5. Y. Luo, W. Huang, X. Li and A. R. Zhang, *Recursive Importance Sketching for Rank Constrained Least Squares: Algorithms and High-order Convergence*, *Operations Research* **72** (2024), 237–256; https://arxiv.org/pdf/2011.08360.
