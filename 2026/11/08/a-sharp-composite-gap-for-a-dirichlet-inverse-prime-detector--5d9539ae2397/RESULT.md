# A sharp composite gap for a Dirichlet-inverse prime detector

## Finding
For each integer \(k\ge2\) define
\[
F_k(n)=\sigma_k^{(-1)}(n)+\mu(n)+J_k(n)+3\qquad(n\ge1),
\]
where \(\sigma_k(n)=\sum_{d\mid n}d^k\), \(\sigma_k^{(-1)}\) denotes its inverse under Dirichlet convolution, \(\mu\) is the Möbius function, and \(J_k\) is the \(k\)-th Jordan totient. Then **every composite integer \(n\)** satisfies the sharp inequality
\[
\boxed{\lvert F_k(n)\rvert\ge4^k+3},
\]
and equality holds **if and only if \(n=4\)**. Moreover \(F_k(p)=0\) for every prime \(p\), and \(F_k(1)=6\).

Thus \(4\) is the unique composite whose detector value is closest to zero, for every integer \(k\ge2\). The assertion concerns exact arithmetic values, not computational efficiency.

## Assumptions and scope
All integers \(n\) are positive and \(k\) is an integer at least \(2\). The inverse \(\sigma_k^{(-1)}\) is characterized by \(\sigma_k*\sigma_k^{(-1)}=\varepsilon\), with \(\varepsilon(1)=1\) and \(\varepsilon(n)=0\) for \(n>1\); it is not a pointwise reciprocal.

We use the standard local identities
\[
\begin{aligned}
\sigma_k^{(-1)}(p)&=-(1+p^k),\\
\sigma_k^{(-1)}(p^2)&=p^k,\\
\sigma_k^{(-1)}(p^e)&=0\quad(e\ge3),\\
J_k(p^e)&=p^{k(e-1)}(p^k-1).
\end{aligned}
\]
The values of \(\sigma_k^{(-1)}\) and \(J_k\) are multiplicative. Hence every composite falls into exactly one of three cases: squarefree, divisible by a prime cube, or cube-free but nonsquarefree.

## Proof
**Primes and the minimum candidate.** For every prime \(p\), the local identities give
\[
F_k(p)=-(1+p^k)-1+(p^k-1)+3=0.
\]
Also \(F_k(1)=6\). At \(n=4\),
\[
F_k(4)=2^k+2^k(2^k-1)+3=4^k+3.
\]
It remains to show every other composite has strictly larger absolute value.

**Case I: squarefree composite.** Write \(n=p_1\cdots p_r\) with distinct primes and \(r\ge2\), and put \(q_i=p_i^k\). Multiplicativity yields
\[
F_k(n)=(-1)^r\prod_{i=1}^r(q_i+1)+(-1)^r+\prod_{i=1}^r(q_i-1)+3.
\]
If \(r\) is even, both products are positive, and at least the primes \(2,3\) occur in the comparison minimum. Thus
\[
F_k(n)\ge(2^k+1)(3^k+1)+(2^k-1)(3^k-1)+4=2\cdot6^k+6>4^k+3.
\]
If \(r\) is odd then \(r\ge3\), and
\[
F_k(n)=2-\left(\prod_i(q_i+1)-\prod_i(q_i-1)\right).
\]
The difference is a positive sum of monomials and is at least \(2\prod_{i=2}^r q_i\). Labeling the primes in increasing order, \(p_2\ge3\) and \(p_3\ge5\), so
\[
\lvert F_k(n)\rvert\ge2\cdot15^k-2>4^k+3.
\]

**Case II: some prime cube divides \(n\).** Then \(\sigma_k^{(-1)}(n)=\mu(n)=0\), whence \(F_k(n)=J_k(n)+3\). A prime-power factor \(p^e\) with \(e\ge3\) contributes at least \(2^{2k}(2^k-1)\) to the positive integer \(J_k(n)\), and the other local Jordan factors are positive integers. Consequently
\[
F_k(n)\ge 4^k(2^k-1)+3>4^k+3.
\]

**Case III: cube-free and nonsquarefree.** Write uniquely \(n=ab^2\), where \(a,b\) are coprime squarefree integers and \(b>1\). Let \(s\) denote the number of primes of \(a\), and put
\[
A=\prod_{p\mid a}(p^k+1),\qquad
B=\prod_{p\mid a}(p^k-1),\qquad
C=\prod_{p\mid b}(p^k-1).
\]
Empty products equal \(1\). The local identities give
\[
F_k(ab^2)=3+b^k\bigl((-1)^s A+BC\bigr).
\]
If \(s\) is even, the bracket is \(A+BC\). When \(a=1\), it is \(1+C\ge2^k\), with equality precisely for \(b=2\); thus the asserted minimum occurs exactly at \(n=4\). When \(a>1\), evenness of \(s\) implies at least two prime factors, so \(A+BC>2^k\) and \(b^k\ge2^k\); the resulting value is strictly greater than \(4^k+3\).

Suppose \(s\) is odd. We first record the strict Euler-product bound
\[
\frac AB=\prod_{p\mid a}\frac{1+p^{-k}}{1-p^{-k}}
<\prod_p\frac{1+p^{-k}}{1-p^{-k}}
\le\frac{\zeta(2)^2}{\zeta(4)}=\frac52.
\]
The inequality uses \(k\ge2\) and the monotonic decrease of each Euler factor with \(k\). Hence the bracket \(BC-A\) exceeds \(B(C-5/2)\), which is positive because \(C\ge2^k-1\ge3\).

If \(b=2\), then \(a\) is odd, nonempty, and \(B\ge3^k-1\), so
\[
F_k(n)>3+2^k(3^k-1)(2^k-7/2).
\]
For \(k\ge2\), the last product is greater than \(4^k\): indeed \(3^k-1\ge8\) and \(2^k-7/2\ge2^{k-3}\) (at \(k=2\) this is equality), giving a lower bound \(2^k\cdot8\cdot2^{k-3}=4^k\). Thus the desired strict bound holds.

If \(b\ge3\), then \(B\ge2^k-1\), and \(C\ge3^k-1\) (because \(b\) is squarefree and at least \(3\)). It follows that
\[
F_k(n)>3+3^k(2^k-1)(3^k-7/2).
\]
Here \(2^k-1\ge2^{k-1}\) and \(3^k-7/2\ge3^k/2\), so the extra term is at least \(18^k/4>4^k\). The desired strict bound holds in every odd-\(s\) case as well.

The cases are exhaustive, establishing the inequality and its unique equality case. \(\square\)

## Verification
The file `verify.py` independently evaluates \(\sigma_k\) by divisor summation, obtains \(\sigma_k^{(-1)}\) through its convolution recurrence, and computes \(\mu\) and \(J_k\) by prime-factor recurrence. It checks every \(2\le n\le10000\) for each \(2\le k\le8\). Each of the seven runs confirms the exact composite minimum \(4^k+3\) with unique minimizer \(n=4\), and zero values at all primes tested. Reproduce with `python3 verify.py` using the standard Python library.

These finite checks do not establish the unrestricted theorem. The proof above separately covers all \(n\) and \(k\) using the Euler product and elementary inequalities.

## Relationship to prior work
Liu [1] introduces \(F_k\), proves the complete zero set (only primes for \(k\ge2\)), and supplies the prime-power and three-case formulas. The sharp uniform **magnitude gap** and the **unique minimizing composite** above are additional statements; knowing only that the detector is nonzero at composites does not imply a \(k\)-dependent bound or its equality case.

A subsequent analysis [2] proves a sharp real-parameter interval for a related mixed detector and, in particular, strict positivity for the cube-free nonsquarefree bracket when \(k\ge2\). The positivity argument and its Euler-product estimate are existing mathematics, not claimed as new here. The new assertion is the full-domain exact minimum \(4^k+3\), including comparison across all three prime-exponent patterns and a unique extremizer. The cited earlier analysis does not state that minimum, and its generic lower bound in the repeated-prime case is weaker.

OEIS A046692 [3] tabulates the ordinary Dirichlet inverse of \(\sigma_1\). It does not supply the stated higher-\(k\) mixed-function minimum. Searches using the function, its aliases, the exact constant, and the extremizing integer did not reveal an earlier statement of this sharp gap; that does not prove historical uniqueness.

## Limitations
The sharp gap is proved only for integer \(k\ge2\); at \(k=1\) the detector has the exceptional composite zero \(18\), so no positive global composite gap exists. The exact values require arithmetic functions that may themselves require factorization, so this is a structural separation theorem, not a faster primality algorithm. The literature comparison is limited to accessible sources; independent mathematical and historical-priority assessment remain outstanding.

## References
1. Z. Liu, *Prime-Detecting Identities from Dirichlet Inversion and Jordan Totients*, arXiv:2609.33278v2, first posted 2026-09-27, https://arxiv.org/abs/2609.33278.
2. *Sharp parameter stability for mixed Dirichlet-inverse prime criteria*, published-finding corpus (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-parameter-stability-for-mixed-dirichlet-inverse-prime-crit--09c92f70d81c.
3. OEIS A046692, *Dirichlet inverse of the sum-of-divisors function*, https://oeis.org/A046692.
