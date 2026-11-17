# Cyclic fixed-point–descent covariance reverses sign at the unbiased Ewens law

## Finding
Let \(\Pi\in S_n\), \(n\ge3\), have Ewens probability proportional to \(\theta^{c(\Pi)}\) for \(\theta>0\), where cycles include singleton cycles. Let \(F=\sum_{j=1}^n\mathbf1\{\Pi(j)=j\}\) and let
\[
D_\circ=\sum_{i=1}^{n-1}\mathbf1\{\Pi(i)>\Pi(i+1)\}
+\mathbf1\{\Pi(n)>\Pi(1)\}.
\]
The last indicator compares the *one-line* image sequence across its end-to-start boundary, not the cycle notation of the permutation. Then the exact covariance is
\[
\boxed{\operatorname{Cov}(F,D_\circ)=
-\frac{n\theta(n-2)(\theta-1)(n+2\theta-3)}{(n+\theta-3)(n+\theta-2)(n+\theta-1)^2}.}
\]
For every \(n\ge3\), it is strictly positive for \(0<\theta<1\), vanishes at \(\theta=1\), and is strictly negative for \(\theta>1\). Zero covariance is **not** an assertion that \(F\) and \(D_\circ\) are independent. The ordinary, noncyclic fixed-point/adjacent-descent covariance matrix and the aggregate noncyclic covariance are already established by *A sharp locality transition for fixed-point–descent covariance under the Ewens law* (published November 8, 2026); those results are used as prior input rather than claimed anew. The contribution here is the additional **cyclic-boundary covariance identity and its all-size one-crossing sign law**.

## Proof
Put
\[
p_n=\Pr\{\Pi(j)=j\}=\frac\theta{n+\theta-1},\qquad
q_m=\frac{(m-1)(m/2+\theta-1)}{(m+\theta-1)(m+\theta-2)}.
\]
The formula for \(q_m\) is the previously established Ewens probability of a descent at any adjacent ordinary positions. Ewens consistency gives: conditioned on one specified fixed point, deleting that label produces an Ewens permutation on \(n-1\) labels with the same \(\theta\). Thus the earlier ordinary-descent cross-covariance theorem gives, by summing over positions,
\[
\operatorname{Cov}(F,D)
=p_n\left\{(n-1)(n-2)q_{n-1}
+\frac{(n-1)(n-2)}{n+\theta-2}-n(n-1)q_n\right\}.
\tag{1}
\]
We now supply the **new boundary calculation** for \(W=\mathbf1\{\Pi(n)>\Pi(1)\}\). For any prescribed pair of distinct images \(a=\Pi(n)\), \(b=\Pi(1)\), the Ewens weight is the common two-arrow denominator \([(n+\theta-1)(n+\theta-2)]^{-1}\), multiplied by \(\theta\) once per completed directed cycle among the prescribed arrows. Among the \(\binom n2\) pairs with \(a>b\), there are \(n-1\) in which \(\Pi(n)=n\), and \(n-1\) in which \(\Pi(1)=1\); exactly one, \((a,b)=(n,1)\), satisfies both. The endpoint transposition \(\Pi(n)=1,\Pi(1)=n\) is an ascent for \(W\), so it gives no extra cycle contribution. Inclusion-exclusion in the weighted sum therefore yields
\[
 w_n:=\Pr(W=1)=
\frac{\binom n2+2(n-1)(\theta-1)+(\theta-1)^2}{(n+\theta-1)(n+\theta-2)}.
\tag{2}
\]
Conditional on \(\Pi(j)=j\), the event \(W\) is certain if \(j\in\{1,n\}\), because \(\Pi(1)=1\) or \(\Pi(n)=n\) forces \(\Pi(n)>\Pi(1)\). If \(j\notin\{1,n\}\), deletion and order-preserving relabeling leave exactly the same wrap-around event on \(n-1\) labels, hence conditional probability \(w_{n-1}\). Consequently
\[
\operatorname{Cov}(F,W)=p_n\{2+(n-2)w_{n-1}-nw_n\}.
\tag{3}
\]
Equations (1)–(3), with their displayed rational expressions, combine to the claimed factored covariance. Every denominator is strictly positive for \(n\ge3\), \(\theta>0\), as is \(n+2\theta-3\); thus the sign equals that of \(1-\theta\) throughout the domain. For \(n=2\), outside this theorem's scope, the cyclic descent count is identically one and its covariance with fixed points is zero. \(\square\)

## Verification, meaning, and limitations
The unchanged `verify.py` exhaustively computes exactly weighted permutation moments for \(3\le n\le8\) at seven rational positive values of \(\theta\), checking both ordinary and circular formulas. These finite checks corroborate, but do not prove, the all-size identity. The ordinary cross-covariance matrix, its remote entries and its ordinary aggregate are known from the November 8 locality theorem; this result claims none of them independently. A still earlier uniform-permutation theorem proves the \(\theta=1\) cancellation. The mathematically new point is the *exact response of the circular boundary observable to nonuniform cycle weighting*, distinguishing the positive/negative sides of the unbiased parameter in every sample size. General Ewens moment formulas of Féray and cycle/descent-set enumerators may provide alternate derivations, so historical priority is provisional.

## References
- *A sharp locality transition for fixed-point–descent covariance under the Ewens law*, published November 8, 2026, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-a-sharp-locality-transition-for-fixed-point-descent-covariance-u--413586e500a3/RESULT.md .
- *Boundary localization of fixed-point–descent dependence in a uniform permutation*, published October 4, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-boundary-localization-of-fixed-point-descent-dependence-in-a-uni--6e228e1e9495 .
- V. Féray, *Asymptotic behavior of some statistics in Ewens random permutations*, Electronic Journal of Probability 18 (2013), arXiv:1201.2157.
- I. M. Gessel and Y. Zhuang, *Plethystic formulas for permutation enumeration*, Advances in Mathematics 375 (2020), arXiv:2001.00654.
