# Sharp two-sided shadowing constants for a two-regime bilateral weighted shift

## Finding
For \(1\le p\le\infty\) and \(a,b>0\), let \(X=\ell_p(\mathbb Z;\mathbb K)\), where \(\mathbb K=\mathbb R\) or \(\mathbb C\). Define the invertible bilateral forward weighted shift \(T\) by
\[
 (Tx)_n=w_nx_{n-1},\qquad w_n=\begin{cases}a,&n\le0,\\ b,&n\ge1.\end{cases}
\]
Here \(\ell_\infty\) is the space of all bounded two-sided scalar sequences. Given any uniformly bounded two-sided sequence \(e=(e_k)_{k\in\mathbb Z}\) in \(X\), consider corrections \(y=(y_k)_{k\in\mathbb Z}\) solving
\[
 y_{k+1}=Ty_k+e_k,\qquad k\in\mathbb Z.
\]
Let \(K_p(a,b)\) be the infimum of numbers \(K\) for which every \(e\) with \(\sup_k\|e_k\|_p\le1\) has such a solution with \(\sup_k\|y_k\|_p\le K\); set the value to infinity if no finite uniform bound works. Then
\[
 K_p(a,b)=\begin{cases}
 (1-\max\{a,b\})^{-1},&a<1,\ b<1,\\
 (\min\{a,b\}-1)^{-1},&a>1,\ b>1,\\
 \big((a-1)^{-p}+(1-b)^{-p}\big)^{1/p},&a>1>b,\ 1\le p<\infty,\\
 \max\{(a-1)^{-1},(1-b)^{-1}\},&a>1>b,\ p=\infty,\\
 \infty,&\text{otherwise.}
 \end{cases}
\]
All finite constants are optimal. For \(a>1>b\) and \(1\le p<\infty\), every \(\lambda\in\mathbb C\) satisfying \(b<|\lambda|<a\) is an eigenvalue of the complexification of \(T\), hence in particular \(1\) is an eigenvalue. Thus this finite-shadowing regime need not be hyperbolic.

## Assumptions and scope
The weights are strictly positive constants on the two half-lines, with the interface between coordinates zero and one. This fixes the orientation: the left tail has weight \(a\) and the right tail weight \(b\). We use a genuinely two-sided time axis. Any bounded error sequence can be realized as the residual of some bi-infinite pseudotrajectory because \(T\) is invertible: fix \(x_0=0\) and recursively solve \(x_{k+1}=Tx_k+e_k\) forwards and backwards. An exact orbit \(u_k\) shadows that pseudotrajectory with error at most \(K\) precisely when the correction \(y_k=x_k-u_k\) is a bounded solution of this equation. Therefore \(K_p(a,b)\) is the optimal Lipschitz constant in the standard shadowing estimate; the pseudotrajectory itself need not be bounded.

## Proof
**Case 1: two contracting tails.** If \(r=\max\{a,b\}<1\), then \(\|T\|=r\) and the series \(y_k=\sum_{j\ge0}T^je_{k-1-j}\) converges absolutely in \(X\), solves the equation, and satisfies \(\sup_k\|y_k\|_p\le(1-r)^{-1}\). To prove sharpness, fix a positive integer \(m\), and choose a coordinate \(N\) such that the path from \(N-m\) to \(N\) remains in a half-line with weight \(r\). Set \(e_{-1-j}=\mathbf e_{N-j}\) for \(0\le j<m\) and every other error to zero; \(\mathbf e_n\) denotes a unit coordinate vector. Iterating any correction equation from time \(-m\) to time zero, the \(N\)-coordinate of \(y_0\) has modulus at least \((1-r^m)/(1-r)-r^mK\), provided \(\sup_k\|y_k\|_p\le K\). Consequently \(K\ge(1-r^m)/((1-r)(1+r^m))\), which tends to \((1-r)^{-1}\).

**Case 2: two expanding tails.** If \(s=\min\{a,b\}>1\), then \(\|T^{-1}\|=s^{-1}\). The series \(y_k=-\sum_{j\ge1}T^{-j}e_{k+j-1}\) is a bounded correction with bound \((s-1)^{-1}\). For sharpness, place a unit error at each of \(m\) distinct future times, on successive coordinates of a path entirely contained in the tail of weight \(s\). The inverse-iteration identity \(y_0=T^{-m}y_m-\sum_{j=1}^m T^{-j}e_{j-1}\) yields \(K\ge\sum_{j=1}^m s^{-j}-s^{-m}K\). Let \(m\to\infty\) to obtain \(K\ge(s-1)^{-1}\).

**Case 3: expanding left tail, contracting right tail.** Suppose \(a>1>b\). Define a correction directly, for every integer time \(k\), by
\[
 (y_k)_0=0,\qquad
 (y_k)_n=\sum_{j=0}^{n-1}b^j(e_{k-1-j})_{n-j}\quad(n\ge1),
\]
\[
 (y_k)_{-m}=-\sum_{j=1}^{m}a^{-j}(e_{k+j-1})_{-m+j}\quad(m\ge1).
\]
Direct substitution verifies \((y_{k+1})_n=w_n(y_k)_{n-1}+(e_k)_n\) for each \(n\in\mathbb Z\), including the interface \(n=0\). On the positive half-line, truncating the right shift yields norm at most \(\sum_{j\ge0}b^j=(1-b)^{-1}\). On the negative half-line, truncating inverse left shifts yields norm at most \(\sum_{j\ge1}a^{-j}=(a-1)^{-1}\). These half-line supports are disjoint. Hence their \(\ell_p\) norm combines by the claimed \(p\)-sum for finite \(p\), and by the maximum when \(p=\infty\).

For the reverse bound, fix \(m\ge1\) and prescribe the following errors, with all unspecified coordinates zero:
\[
 (e_{-1-j})_{m+1-j}=1\quad(0\le j<m),\qquad
 (e_{j-1})_{-m-1+j}=-1\quad(1\le j\le m).
\]
At every time there is at most one nonzero coordinate and its modulus is one, so \(\sup_k\|e_k\|_p=1\). For any correction \(y\) bounded by \(K\), the forward and backward recurrences give
\[
 (y_0)_{m+1}=b^m(y_{-m})_1+\sum_{j=0}^{m-1}b^j,
\]
\[
 (y_0)_{-m-1}=a^{-m}(y_m)_{-1}+\sum_{j=1}^m a^{-j}.
\]
Both terminal coordinates have absolute value at least their respective displayed positive geometric sums minus \(b^mK\) and \(a^{-m}K\). Since they are distinct coordinates, \(K\) is no smaller than their \(\ell_p\) two-coordinate norm (or maximum for \(p=\infty\)). Sending \(m\to\infty\) proves the stated sharp constant, with no assumption that the correction is unique.

**Case 4: the reversed interface.** If \(a<1<b\), let \(e_0=\mathbf e_0\), and all other errors vanish. For any bounded solution, the unforced past along the path of coordinates \((-m-1,-m)\) forces \((y_0)_{-1}=0\), because \((y_0)_{-1}=a^m(y_{-m})_{-m-1}\) and \(a^m\to0\). The forced coordinate then gives \((y_1)_0=1\), and the unforced future gives \((y_{1+j})_j=b^j\), unbounded. Thus no bounded solution exists.

**Case 5: unit weights.** If \(a=1\), prescribe \(e_k=\mathbf e_{k+1}\) for all \(k\le-1\), and zero otherwise. Along the left characteristic, \((y_{k+1})_{k+1}=(y_k)_k+1\); boundedness on all negative times is impossible. If \(b=1\), prescribe \(e_k=\mathbf e_{k+2}\) for all \(k\ge0\), and zero otherwise. Along the right characteristic, \((y_{k+1})_{k+2}=(y_k)_{k+1}+1\), so boundedness fails. These arguments apply even when the other weight is arbitrary. All parameter cases have now been exhausted.

**Nonhyperbolic eigenvalues.** For \(a>1>b\) and \(b<|\lambda|<a\), define \(x_0=1\), \(x_n=(b/\lambda)^n\) for \(n\ge1\), and \(x_{-j}=(\lambda/a)^j\) for \(j\ge1\). This is in every finite-exponent \(\ell_p\), and the coordinate equations give \(Tx=\lambda x\). Thus the exact finite constant can coexist with unit-modulus eigenvalues.

## Verification
The finite diagnostic program `check_shadowing_two_regime.py` checks all coordinate recurrences for 30 independently sampled finite error configurations, the two-tail sharpness witnesses, and the boundary-case formulas. It executes without nonstandard dependencies and reports 5,972 passed finite assertions. It checks calculations but is not a proof of any infinite quantifier. The complete proof above uses explicit summable series, norm estimates and lower-bound witnesses for arbitrary long paths.

## Relationship to prior work
Bernardes and Messaoudi's characterization of weighted-shift shadowing (Theorem 17 in the 2019 preprint) already determines the qualitative finite-versus-infinite cases for \(\ell_p\) with finite \(p\), under reflection of the orientation; the qualitative classification is **not** asserted to be new. Hevessy and Raunig (2025) study related shadowing and periodic shadowing conditions on sequence spaces. The present calculation determines the **exact least uniform error-correction constant**, its full exponent dependence, and explicit simultaneous-tail lower witnesses; these are not stated in the inspected theorems. A 2026 preprint by Pinto deals with broad qualitative shadowing criteria; its complete text was not accessible for a full comparison, leaving a priority risk for the quantitative theorem.

## Limitations
This result concerns step-constant positive weights, not arbitrary variable, periodic, or zero weights. The exponent range includes \(\ell_\infty\), but no assertion is made for general Banach lattices. No independently certified publication priority is claimed. The eigenvalue observation is a consequence of the displayed explicit vector and is included for interpretation, not as a new qualitative phenomenon.

## References
1. N. C. Bernardes Jr. and A. Messaoudi, *Shadowing and Structural Stability in Linear Dynamical Systems*, arXiv:1902.04386v1 (2019), Theorem 17. https://arxiv.org/abs/1902.04386
2. M. Hevessy and T. Raunig, *Dynamical Properties of Weighted Shifts on Sequence Spaces*, arXiv:2509.11852v1 (first posted September 15, 2025), especially Sections 1 and 4. https://arxiv.org/abs/2509.11852
3. J. V. A. Pinto, *Shadowing for Weighted Composition Operators on Spaces of Continuous Functions*, arXiv:2607.28361v1 (2026); abstract consulted, complete text not inspected. https://arxiv.org/abs/2607.28361
4. N. C. Bernardes Jr., A. Bonilla, and J. V. A. Pinto, *On the Dynamics of Weighted Composition Operators II*, arXiv:2512.06425v1 (2025); journal open-access version (2026). https://doi.org/10.1007/s00009-026-03136-w
