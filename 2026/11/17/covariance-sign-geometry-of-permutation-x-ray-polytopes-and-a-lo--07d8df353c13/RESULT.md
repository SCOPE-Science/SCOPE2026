# Covariance sign geometry of permutation X-ray polytopes and a logarithmic positive-pair law

## Finding

For every integer \(k\ge2\), choose a uniformly random permutation \(\pi\in S_k\). Its anti-diagonal X-ray is the vector \(X=(X_0,\ldots,X_{2k-2})\) with
\[
 X_t=\#\{i\in\{0,\ldots,k-1\}:i+\pi(i)=t\}.
\]
This is the **pushforward of uniform measure on the permutation matrices**, not uniform counting measure on the distinct X-rays, not uniform counting measure on vertices of the X-ray polytope, and not uniform volume on the polytope.

Set \(m_t=k-|t-(k-1)|\), let \(R_t=\{i\in\{0,\ldots,k-1\}:0\le t-i<k\}\), and put \(h_{st}=|R_s\cap R_t|\). **Theorem.** Its complete covariance kernel is
\[
 \mathbb EX_t=\frac{m_t}{k},\qquad
 \operatorname{Cov}(X_s,X_t)=
 \frac{k^2m_t\mathbf1_{s=t}-2k h_{st}+m_sm_t}{k^2(k-1)}.
\]
Every diagonal variance is strictly positive. For distinct coordinates on the same side of the central anti-diagonal (including a pair with one central coordinate), covariance is strictly negative. For a left coordinate \(s<k-1\) and right coordinate \(t>k-1\), put \(a=s+1\) and \(b=2k-1-t\), so \(1\le a,b\le k-1\). The covariance is positive, zero, or negative according as
\[
 (2k-a)(2k-b)\quad\text{is greater than, equal to, or less than}\quad 2k^2.
\]
Thus this single hyperbola classifies **all** off-diagonal covariance signs, including all zero cases.

Write \(P_k\) for the number of unordered pairs of distinct X-ray coordinates having positive covariance. Then
\[
 P_k=\sum_{a=1}^{k-1}\left(\left\lceil\frac{2k(k-a)}{2k-a}\right\rceil-1\right),
 \qquad
 \lim_{k\to\infty}\frac{P_k}{\binom{2k-1}{2}}=1-\log 2.
\]
The number of zero-covariance pairs is at most \(k-1\). Hence the fraction of negative pairs converges to \(\log 2\).

Two additional exact consequences are
\[
 \ker\operatorname{Cov}(X)=\operatorname{span}\{(1)_t,(t)_t\},
 \qquad \operatorname{rank}\operatorname{Cov}(X)=2k-3,
\]
and
\[
 \mathbb E\|X-\mathbb EX\|_2^2=k-\frac13-\frac1{3k}.
\]
The kernel and trace are supporting geometric descriptors; the new structural assertion is the complete sign diagram and its exact positive-pair enumeration and logarithmic density.

## Assumptions and scope

Rows, columns and X-ray coordinates are indexed from zero. The X-ray polytope is \(\mathcal X_k=T_k(\mathcal B_k)\), where \(\mathcal B_k\) is the \(k\)-by-\(k\) Birkhoff polytope and \(T_k\) sums matrix entries along \(i+j=t\). The ambient metric for the trace is ordinary Euclidean. The random point \(X\) is obtained from a uniformly random permutation matrix before applying \(T_k\); different permutations yielding the same image retain their multiplicity. All claims hold for every integer \(k\ge2\), with no genericity hypothesis. \(\log\) denotes the natural logarithm.

## Proof

**Permutation-matrix covariance.** Write \(Y_{ij}=\mathbf1_{\pi(i)=j}\). Directly separating equal cells, cells in one row or column, and cells in distinct rows and columns gives, for \(k\ge2\),
\[
 \operatorname{Cov}(Y_{ij},Y_{\ell m})
 =\frac{(\mathbf1_{i=\ell}-1/k)(\mathbf1_{j=m}-1/k)}{k-1}.
\]
Summing over pairs \((i,j)\) on anti-diagonal \(s\) and pairs \((\ell,m)\) on anti-diagonal \(t\), the joint equality of rows and columns contributes \(m_t\mathbf1_{s=t}\); equal rows contribute \(h_{st}\), as do equal columns; the constant term contributes \(m_sm_t/k^2\). The displayed covariance formula follows. The mean follows because each row has \(\mathbb P(\pi(i)=j)=1/k\).

**Signs away from opposite sides.** Each \(R_t\) is a consecutive interval of row indices. For \(0\le s<t\le k-1\), \(R_s\subset R_t\), so \(h_{st}=m_s\). For \(k-1\le s<t\le2k-2\), \(R_t\subset R_s\), so \(h_{st}=m_t\). Thus the off-diagonal numerator in the covariance formula is respectively \(m_s(m_t-2k)\) or \(m_t(m_s-2k)\), both strictly negative. For \(s=t\), the variance numerator is \(m_t(k^2-2k+m_t)>0\) because \(k\ge2\) and \(m_t\ge1\).

**Opposite-side signs.** If \(s<k-1<t\), write \(a=s+1\) and \(b=2k-1-t\). The row intervals are \(R_s=\{0,\ldots,a-1\}\) and \(R_t=\{k-b,\ldots,k-1\}\). Hence \(m_s=a\), \(m_t=b\), \(h_{st}=\max\{0,a+b-k\}\), and the covariance numerator is
\[
 N_{a,b}=ab-2k\max\{0,a+b-k\}.
\]
If \(a+b\le k\), then \(N_{a,b}=ab>0\), while
\((2k-a)(2k-b)-2k^2=2k(k-a-b)+ab>0\). If \(a+b>k\), the two expressions are equal. This proves the asserted strict/zero/negative hyperbolic sign criterion in all cases.

**Exact counts and limits.** For each \(a\in\{1,\ldots,k-1\}\), positive correlation occurs exactly when
\[
 1\le b<\frac{2k(k-a)}{2k-a}.
\]
The threshold lies strictly between \(0\) and \(k\), so the number of allowable integer \(b\) is exactly its ceiling minus one. Each positive pair consists of one left and one right coordinate and is counted once, proving the finite sum. For fixed \(a\), at most one integer \(b\) makes the covariance vanish; consequently at most \(k-1\) unordered pairs are zero.

After dividing by \(k^2\), the ceiling error in the sum is \(O(1/k)\), and the Riemann sums converge:
\[
 \lim_{k\to\infty}\frac{P_k}{k^2}
 =\int_0^1\frac{2(1-x)}{2-x}\,dx
 =2-2\log 2.
\]
Since \(\binom{2k-1}{2}/k^2\to2\), the positive-pair fraction tends to \(1-\log 2\). The zero-pair fraction vanishes because there are at most \(k-1\) such pairs. The remaining fraction is therefore \(\log2\).

**Kernel and centered second moment.** For real coefficients \(z_t\), the variance of \(\sum_t z_tX_t\) vanishes if and only if \(\sum_i z_{i+\pi(i)}\) is the same for all permutations. Swapping the assigned columns in two distinct rows forces
\(z_{i+j}+z_{i'+j'}-z_{i+j'}-z_{i'+j}=0\).
Taking adjacent rows and adjacent columns gives \(z_u-2z_{u+1}+z_{u+2}=0\) for every \(0\le u\le2k-4\), since every such \(u\) is a sum of two indices from \(\{0,\ldots,k-2\}\). Therefore \(z_t=\alpha+\beta t\). Conversely this is constant over permutations because \(\sum_tX_t=k\) and \(\sum_t tX_t=k(k-1)\). This proves the kernel and rank claims, including \(k=2\).

Finally, \(\sum_tm_t=k^2\) and \(\sum_tm_t^2=k^2+2\sum_{j=1}^{k-1}j^2=(2k^3+k)/3\). Summing the covariance diagonal and simplifying yields
\(\operatorname{tr}\operatorname{Cov}(X)=k-1/3-1/(3k)\), which equals the stated Euclidean centered second moment.

## Verification

The standalone `verify.py` uses only the Python standard library. It constructs all \(k!\) permutations independently for each \(2\le k\le8\), records the raw X-ray coordinate moments, compares the resulting rational covariances against the formula, and checks every off-diagonal sign, pair count, centered moment, and two kernel vectors. For \(9\le k\le100\), it checks all off-diagonal signs and positive-pair counts directly from the explicit integer formula. It also prints large-dimensional ratios for \(k\in\{200,500,1000,2500\}\), without claiming these finite approximations prove the limit.

Executing `python verify.py` produced `PASS: 662674 exact assertions; exhaustive permutation samples through k=8; sign counts through k=100.` These finite computations test the formulas but do not establish any universal statement; the proof above supplies the all-parameter justification.

## Relationship to prior work

Chaudhary and Khandelwal [1] identify the anti-diagonal X-ray image of the Birkhoff polytope and classify facets, including its affine hull. Their paper gives neither the canonical permutation-pushforward covariance sign diagram nor the logarithmic positive-pair density. Bebeacua, Mansour, Postnikov and Severini [2] study X-rays of permutations and their combinatorial degeneracies; their mean-profile viewpoint is compatible with, but does not assert, this covariance-sign classification. Li, Liu and Yao [3] develop X-ray feasibility and facial inequalities. An earlier study of Hankel and Toeplitz X-rays [4] remains a potential but unverified priority source because complete text was not obtained.

The general permutation-indicator covariance identity is elementary and explicitly used as an established building block. The theorem's assessed contribution is the exact **cross-coordinate sign classification, integer-pair census and limiting logarithmic density** for this specific projected polytope distribution, not the generic matrix covariance identity or the already known affine dimension. Related results on the Euclidean diameter of the same image [5] do not imply these covariance statements without a new distributional calculation.

## Limitations

Uniform source permutations are not uniformly distributed over distinct X-rays or over all vertices of \(\mathcal X_k\); multiplicities are essential. Covariance here measures dependence of **coordinates of this canonical random image**, not covariance of uniform interior volume. Sign and density statements are for the unnormalized counts (they are unchanged under a positive common normalization). The result does not determine the complete eigenvalue spectrum of the covariance matrix or the distribution of all X-rays. Historical originality is provisional because relevant older discrete-tomography literature may contain an equivalent unsurfaced calculation. No independent audit has been performed.

## References

[1] P. Chaudhary and K. Khandelwal, *Facets of the X-ray polytope of doubly stochastic matrices*, arXiv:2610.30058v1 (first public 2026-10-21). https://arxiv.org/abs/2610.30058

[2] C. Bebeacua, T. Mansour, A. Postnikov, S. Severini, *On the X-rays of permutations*, arXiv:math/0506334 (2005). https://arxiv.org/abs/math/0506334

[3] B. Li, Y. Liu, Y. Yao, *Binary X-rays of doubly stochastic matrices*, arXiv:2608.01442 (2026). https://arxiv.org/abs/2608.01442

[4] R. A. Brualdi and E. Fritscher, *Hankel and Toeplitz X-rays of permutations*, Linear Algebra Appl. (2014). https://doi.org/10.1016/j.laa.2014.02.037

[5] *The diameter graph and sharp second-distance gap of permutation X-ray polytopes* (2026), available in the public mathematical findings index. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-diameter-graph-and-sharp-second-distance-gap-of-permutation--215ce1bc6a73
