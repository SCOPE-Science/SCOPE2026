# Norm-saturation runs and local curvature of constrained numerical radii for nilpotent weighted shifts

## Finding
Let \(n\ge2\), and let \(T\) on complex \(\mathbb C^n\) be the nilpotent weighted forward shift \(Te_j=a_je_{j+1}\) for \(1\le j<n\), with at least one nonzero complex weight. For \(0\le q\le1\) put
\[
w_q(T)=\max_{\|x\|=\|y\|=1,\ \langle x,y\rangle=q}|\langle Tx,y\rangle|.
\]
Write \(M=\max_j|a_j|>0\); let \(L\) be the maximum number of consecutive indices for which \(|a_j|=M\). Then
\[
\boxed{\quad w_q(T)=M\quad\Longleftrightarrow\quad 0\le q\le\cos\frac{\pi}{L+1}.\quad}
\]
If there is a unique maximal index \(j\), set \(\ell=|a_{j-1}|\) if \(j>1\) and \(\ell=0\) otherwise, and set \(r=|a_{j+1}|\) if \(j<n-1\) and \(r=0\) otherwise. Then as \(q\downarrow0\),
\[
\boxed{\quad w_q(T)=M-\frac{(M^2-\ell^2)(M^2-r^2)}{2M(2M^2-\ell^2-r^2)}q^2+o(q^2).\quad}
\]
The positive coefficient is independent of all weights except the maximal one and its two immediate neighbors.

## Assumptions and scope
Finite-dimensional complex Hilbert space; arbitrary complex weight phases and zero weights are allowed. The index \(j\) in the second assertion is unique, so \(\ell,r<M\) and the denominator is positive. \(q\) is real with \(0\le q\le1\). At \(q=1\) the radius is the classical numerical radius; at \(q=0\) it is the orthogonal numerical radius. No analogous conclusion about an arbitrary infinite shift is asserted, because norm attainment can fail.

## Proof
A diagonal unitary conjugation removes all phases from the weights, so take \(a_j\ge0\). For any unit vector \(x\), write \(c(x)=\langle Tx,x\rangle\). Every unit \(y\) with \(\langle x,y\rangle=q\) has form \(y=qx+\sqrt{1-q^2}z\), with \(z\perp x\), \(\|z\|=1\). Optimizing its phase yields
\[
w_q(T)=\max_{\|x\|=1}\left(q|c(x)|+\sqrt{1-q^2}\sqrt{\|Tx\|^2-|c(x)|^2}\right). \tag{1}
\]
In particular \(w_q(T)\le\|T\|=M\). Equality requires \(\|Tx\|=M\) and equality in Cauchy--Schwarz, hence \(y=e^{it}Tx/M\). The norm-attaining vectors \(x\) are exactly the unit vectors in \(E=\operatorname{span}\{e_j: a_j=M\}\). Therefore equality is possible precisely when \(q\) lies in the absolute-value numerical range of the compression \(P_ET|_E/M\). Each maximal consecutive run of \(L_i\) input indices is one nilpotent Jordan block of order \(L_i\), and distinct runs are orthogonal blocks. The compression is their direct sum. Its numerical range is the centered disk of radius \(\max_i\cos(\pi/(L_i+1))\): phase rotation invariance gives disks, and the largest eigenvalue of the real symmetric part of a Jordan block is \(\cos(\pi/(L_i+1))\), by the sine eigenvectors. Every radius from zero to the maximum occurs, proving the first assertion, including endpoint equality.

For the second assertion, let the maximal index be \(j\), so at \(q=0\) formula (1) has the unique maximizing ray \(x=e_j\). Compactness forces all maximizing rays at small \(q\) to converge to this ray. Fix its phase and write
\[
x=\sqrt{1-\|z\|^2}e_j+\sum_{k\ne j}z_ke_k.
\]
Because every other weight is strictly smaller than \(M\), the quadratic deficit at \(q=0\) is positive definite in \(z\). The perturbation from \(q>0\) is at most \(O(q\|z\|+q^2)\); the maximizing displacement thus obeys \(\|z\|=O(q)\). For \(u=z_{j-1}\) and \(v=z_{j+1}\) (take nonexistent coordinates to be zero), the linear term of \(c(x)\) is \(\ell u+M\overline v\) after a harmless choice of inner-product convention. Coordinates farther away occur only in the positive quadratic penalty and are zero at leading order. Uniform Taylor expansion of (1), for \(u,v=O(q)\), gives
\[
\begin{split}
M-w_q(T)={}&\min_{u,v\in\mathbb C}\Bigg\{\frac{Mq^2}{2}
+\frac{(M^2-\ell^2)|u|^2+(M^2-r^2)|v|^2+|\ell u+Mv|^2}{2M}\\
&\hspace{38mm}-q|\ell u+Mv|\Bigg\}+o(q^2).
\end{split}\tag{2}
\]
Here the phases of \(u,v\) may be chosen so the two linear contributions align: for any fixed value of their absolute sum, this minimizes the positive diagonal penalty, and does not change the remaining expression. Thus optimize over real nonnegative \(u,v\). Define
\[
Q=\begin{pmatrix}M/2&\ell/2\\\ell/2&(2M^2-r^2)/(2M)\end{pmatrix},\qquad b=\begin{pmatrix}\ell\\M\end{pmatrix}.
\]
The variable portion of (2) is \((u,v)Q(u,v)^t-qb^t(u,v)^t\), whose unique minimizer is \((q/2)Q^{-1}b\). It is entrywise nonnegative because \(M^2-\ell^2>0\) and \(M^2-r^2>0\). Moreover \(\det Q=(2M^2-\ell^2-r^2)/4>0\). The resulting minimum is \(Mq^2/2-q^2 b^tQ^{-1}b/4\), and direct inversion simplifies it to the displayed coefficient. This proves the claimed expansion; the uniform local expansion and compactness rule out remote competing maximizers.

## Verification
The accompanying `check.py` computes the quadratic optimization identity exactly in the symbolic field \(\mathbb Q(M,\ell,r)\), verifies the inverse-matrix optimizer and checks the block sine-law eigenvector formula for finite sizes. Numerical diagnostics are illustrative only: the proof above supplies the global quantifiers.

## Relationship to prior work
Azadi (arXiv:2610.32504v1) formulates general joint \(q\)-numerical ranges and the norm bound but does not characterize equality for arbitrary finite weighted nilpotent shifts. Chien and Nakazato (2010) analyze a particular tridiagonal family with both upper and lower entries; their concrete results are not a consecutive-maxima classification. Their 2007 paper on periodic infinite weighted shifts is potentially relevant but was not available for complete comparison; it is a priority risk, particularly if a general formula subsumes the finite result. The classical Jordan-block numerical radius \(\cos(\pi/(L+1))\) is an input, not a new claim. Published results for equal-weight Jordan blocks give special cases; neither a unique-max local curvature involving two neighboring weights nor the full run classification was identified in inspected statements.

## Limitations
This is a self-review, not an independent or exhaustive publication-priority assessment. A stronger earlier theorem for general weighted shifts could imply these results. The curvature statement is asymptotic rather than an exact formula for arbitrary positive \(q\), and requires a unique largest weight. Infinite-dimensional norm-attainment issues are excluded.

## References
[1] A. Azadi, *Joint q-Numerical Ranges of Continuous Operator-Valued Functions*, arXiv:2610.32504v1 (first posted 2026-10-23), https://arxiv.org/html/2610.32504v1.
[2] M.-T. Chien and H. Nakazato, *The q-numerical range of 3 by 3 tridiagonal matrices*, Electronic Journal of Linear Algebra 20 (2010), 376–390, https://journals.uwyo.edu/index.php/ela/article/download/765/765/765.
[3] M.-T. Chien and H. Nakazato, *The q-numerical radius of weighted shift operators with periodic weights*, Linear Algebra Appl. 422 (2007), 198–218, DOI:10.1016/j.laa.2006.09.017 (abstract inspected; full text unavailable).
[4] A. Vandanjav and B. Undrakh, *On the numerical range of some weighted shift matrices and operators*, Linear Algebra Appl. 449 (2014), 76–88, DOI:10.1016/j.laa.2014.02.018.
