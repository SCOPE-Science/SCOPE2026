# A sharp analytic phase transition for an implicit Fibonacci-weighted exponential series

## Finding
For each nonnegative integer \(q\), define \(A_q(x)=\sum_{n\ge0}a_n(q)x^n\), with \(a_0(q)=1\), implicitly by
\[
A_q(x)=\exp\left(\sum_{m\ge1}\frac{x^m}{m}(q^m+A_q(x))^m\right).
\]
For every integer \(q\ge2\) and \(n\ge1\),
\[
\frac{q^{n^2}}{n}\le a_n(q)\le 2\cdot6^nq^{n^2},\qquad
\lim_{n\to\infty}\frac{\log a_n(q)}{n^2}=\log q.
\]
The radius of convergence is exactly zero for every \(q\ge2\); these series are transcendental over \(\mathbb Q(x)\) and non-D-finite. Conversely, \(q=0\) and \(q=1\) give algebraic series with positive radius, so this is an exact parameter-phase classification for all \(q\in\mathbb Z_{\ge0}\).

## Assumptions and scope
All variables and coefficients are formal over \(\mathbb Q\) unless analyticity is discussed. For every fixed nonnegative integer \(q\), the equation uniquely determines the coefficients inductively, since its logarithm has zero constant term and every occurrence of \(A_q\) inside the exponent is multiplied by a positive power of \(x\). Algebraicity and D-finiteness refer to the ordinary generating series \(A_q(x)\) over \(\mathbb Q(x)\). The limit holds for each fixed integer \(q\ge2\), not uniformly as \(q\) changes with \(n\).

## Proof
The essential input is the exact positivity and polynomial-degree theorem of Li–Zhong–Zhou, Theorem 7.1: for every \(n\ge1\), the polynomial \(a_n(t)\in\mathbb Q[t]\) has nonnegative coefficients, degree exactly \(n^2\), and leading coefficient \(1/n\). In particular, for any real \(t\ge1\), termwise positivity gives
\[
\frac{t^{n^2}}{n}\le a_n(t)\le t^{n^2}a_n(1).
\]
At \(t=1\), the geometric logarithm identity gives \(A_1(x)=1/(1-x(1+A_1(x)))\), or equivalently \(A_1=1+xA_1+xA_1^2\). Its coefficients are nonnegative, and its analytic branch satisfies \(A_1(1/6)=2\) (the quadratic discriminant at that point equals \(1/36\)). Thus \(a_n(1)(1/6)^n\le A_1(1/6)=2\), so \(a_n(1)\le2\cdot6^n\). Combining these inequalities yields the claimed two-sided bounds. Taking logarithms and dividing by \(n^2\) proves the sharp limit.

For fixed \(q\ge2\), the lower bound implies \(\limsup_{n\to\infty}a_n(q)^{1/n}=+\infty\), giving radius zero by Cauchy–Hadamard. Every algebraic formal power series over \(\mathbb Q(x)\) in characteristic zero has a positive complex convergence radius (Newton–Puiseux/local analytic algebraic functions), so \(A_q\) is transcendental.

For completeness, any sequence satisfying an eventual nontrivial polynomial-coefficient recurrence \(\sum_{j=0}^r p_j(n)b_{n+j}=0\), where \(p_r\not\equiv0\), obeys \(\max_{0\le j\le r}|b_{n+j}|\le C^n(n!)^K\) for some \(C,K\) and large \(n\): divide by \(p_r(n)\) beyond its finitely many zeros and bound each rational function \(p_j(n)/p_r(n)\) by \(C(1+n)^K\); iterate the resulting finite-dimensional maximum bound. Thus \(\log(1+|b_n|)=O(n\log n)\). Since \(\log a_n(q)\ge n^2\log q-\log n\), these coefficients cannot be polynomial-recursive, and the series is not D-finite.

At \(q=0\), the logarithm becomes \(\sum_{m\ge1}(xA_0)^m/m\), hence \(A_0=1/(1-xA_0)\), i.e. \(A_0=1+xA_0^2\). At \(q=1\), it becomes \(\sum_{m\ge1}(x(1+A_1))^m/m\), hence \(A_1=1+xA_1+xA_1^2\). Both equations define algebraic branches analytic at zero.

## Verification
The standalone exact-arithmetic file `check.py` reconstructs coefficients from the exponential formal equation using truncated integer polynomials and rational recurrence, verifies low-order coefficients for \(q=0,1\) against the corresponding quadratic equations, and checks the two-sided growth inequalities for \(q=2,3\). It does not certify infinitely many indices. The proof of the infinite result instead uses the published all-degree positivity/leading-term theorem and the elementary analytic arguments above.

## Relationship to prior work
Li–Zhong–Zhou (2026), Theorem 7.1, establishes nonnegative coefficient polynomials of degree \(n^2\) with leading coefficient \(1/n\), as well as the algebraic endpoint specializations. It does not state the sharp coefficient-growth constant at fixed \(q\), the convergence-radius phase transition, or the non-D-finiteness classification. This result extracts and proves those additional analytic consequences. Related earlier integral-exponential identities and OEIS records emphasize integrality and finite initial coefficients, not the phase transition. Exact claims in accessible research records and closely related published literature were compared for coverage, including the analytically unrelated exponential–apple interpolation class.

## Limitations
The sharp limit is logarithmic; it does not prove a constant-factor asymptotic such as \(a_n(q)\sim q^{n^2}/n\). Only nonnegative integer \(q\) are classified; no claim is made for negative or nonintegral parameters. The proof depends explicitly on the published positivity/leading-term theorem and is not an independent reproof of that input. An unindexed earlier equivalent of the analytic consequences is possible.

## References
- Li, Zhong and Zhou, Integral Exponential Series: Fibonacci Weights and Implicit Equations, arXiv:2611.16283v1 (first posted 2026-11-12). https://arxiv.org/abs/2611.16283
- OEIS A163138, the original implicit enumeration at \(q=2\), cited and discussed in Li–Zhong–Zhou. https://oeis.org/A163138
- Fried, *Further proofs of conjectures from the OEIS* (2026), arXiv:2607.24832, a related integrality treatment of a different OEIS sequence. https://arxiv.org/abs/2607.24832
