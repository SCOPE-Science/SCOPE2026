# Gaussian distinct-prime-factor law and sharp parity bias for consecutive LCM quotients

## Finding
For every integer \(k\ge 1\) and positive integer \(n\), set
\[
Q_k(n)=\frac{\prod_{j=0}^{k}(n+j)}{\operatorname{lcm}(n,n+1,\ldots,n+k)},\qquad W_k(n)=\omega(Q_k(n)),
\]
where \(\omega(1)=0\) and \(\omega(m)\) counts distinct prime divisors. Write \(L=k+1\),
\[
\mathcal H_k=\{p\text{ prime}:L/2<p<L\},\quad T_k=\prod_{p\in\mathcal H_k}p,
\quad \theta_{p,k}=\frac{L-p}{p}.
\]
The empty product is one. **The following are exact for every \(k\ge1\).**

1. The least positive period in \(n\) of \(W_k(n)\) is \(T_k\). Over one period, its complete probability-generating polynomial is
\[
\frac1{T_k}\sum_{n=1}^{T_k}z^{W_k(n)}
=z^{\pi(L/2)}\prod_{p\in\mathcal H_k}
\left(1-\theta_{p,k}+\theta_{p,k}z\right).
\]
In particular, the distribution is a deterministic shift of independent, non-identically distributed Bernoulli variables, and the positive and negative unitary-Möbius signs have natural densities \((1+B_k)/2\) and \((1-B_k)/2\), respectively, with
\[
B_k=\frac1{T_k}\sum_{n=1}^{T_k}(-1)^{W_k(n)}
=(-1)^{\pi(L/2)}\prod_{p\in\mathcal H_k}\left(3-\frac{2L}{p}\right).
\]
The signs are exactly balanced **only for \(k=2\)**; for all other \(k\) the bias is nonzero.

2. The exact mean and variance are
\[
\mu_k=\pi(L/2)+\sum_{p\in\mathcal H_k}\theta_{p,k},\qquad
\sigma_k^2=\sum_{p\in\mathcal H_k}\theta_{p,k}(1-\theta_{p,k}).
\]
As \(k\to\infty\),
\[
\mu_k\sim(\log2)\frac{k}{\log k},\qquad
\sigma_k^2\sim(3\log2-2)\frac{k}{\log k}.
\]
If \(n\) is sampled uniformly from \(\{1,\ldots,T_k\}\), then
\[
\sup_{x\in\mathbb R}\left|
\mathbb P\left(\frac{W_k(n)-\mu_k}{\sigma_k}\le x\right)
-\Phi(x)\right|=O\!\left(\sqrt{\frac{\log k}{k}}\right),
\]
where \(\Phi\) is the standard normal distribution function. The assertion is for sufficiently large \(k\), so that \(\sigma_k>0\).

3. The sign bias has a separate sharp, non-Gaussian exponential scale. For all \(k\ge3\),
\[
\log|B_k|=-\left(\frac{2\log2}{3}+o(1)\right)\frac{k}{\log k}.
\]
The absolute value is essential: this asserts neither eventual positivity nor eventual negativity of \(B_k\).

The new growing-window conclusions in (2) and (3), including their three explicit constants, are the main results; the exact finite generating polynomial is the bridge from the established LCM-quotient framework to those asymptotics.

## Assumptions and scope
All integers \(n\) are positive. The parameter \(k\) is a positive integer, with \(\pi(x)\) the number of rational primes at most \(x\). The natural density for each fixed \(k\) is taken as \(n\to\infty\). The subsequent normal limit and decay statement take \(k\to\infty\) **after** selecting the exact uniform residue distribution in \(n\); no assertion is made for an arbitrary simultaneous growth relation between \(k\) and the sampling endpoint in \(n\). We use the usual prime number theorem and, for the sharp logarithmic sign asymptotic, its standard classical zero-free-region error term. The word *unitary Möbius sign* denotes \((-1)^{\omega(m)}\), not the classical Möbius function, and must not be confused with the Liouville sign \((-1)^{\Omega(m)}\).

## Proof
**Prime-support lemma.** Fix a prime \(p\). If \(p\ge L\), any interval of length \(L\) contains at most one multiple of \(p\), and its exponent in the product is equal to its maximum exponent in the LCM. Hence \(p\nmid Q_k(n)\). If \(p<L\), the exponent of \(p\) in \(Q_k(n)\) is positive precisely when at least two of the \(L\) consecutive terms are divisible by \(p\): their positive valuations sum to strictly more than their maximum. This is an equivalence, even when one or several terms are divisible by higher powers of \(p\).

If \(2p\le L\), every interval of \(L\) consecutive integers contains at least two multiples of \(p\), so \(p\mid Q_k(n)\) for every \(n\). If \(L/2<p<L\), write \(L=p+r\) with \(1\le r<p\). Every interval of \(L\) consecutive integers contains either one or two multiples of \(p\), and exactly \(r=L-p\) of the \(p\) residue classes of its starting point give two multiples. Consequently
\[
W_k(n)=\pi(L/2)+\sum_{p\in\mathcal H_k} I_{p,k}(n),
\]
where \(I_{p,k}(n)\) is a nonconstant indicator depending only on \(n\bmod p\), taking the value one on exactly \(L-p\) residues. The Chinese remainder theorem makes the indicators independent for uniform \(n\bmod T_k\). This proves the generating polynomial and its moments, and also demonstrates that \(T_k\) is a period.

**Exact least period.** Suppose a positive integer \(t\) is any period of \(W_k\). Fix \(p\in\mathcal H_k\) and put \(R=T_k/p\). Then \(tR\) is also a period. Shifting by \(tR\) leaves all indicators indexed by primes \(q\ne p\) unchanged, since \(q\mid R\). Therefore it must leave \(I_{p,k}\) unchanged. Since \(I_{p,k}\) is nonconstant and is periodic modulo the prime \(p\), this forces \(p\mid tR\). But \(p\nmid R\), so \(p\mid t\). Repeating for every prime in \(\mathcal H_k\) gives \(T_k\mid t\). For \(\mathcal H_k=\varnothing\), \(W_k\) is constant and the least period is one.

**Exact parity and its single zero.** Setting \(z=-1\) in the generating polynomial yields the product for \(B_k\). A zero requires \(3p=2L\). This forces \(p\) to be even, hence \(p=2\), and then \(L=3\) or \(k=2\). Conversely \(k=2\) supplies this zero. The exact density formula follows because the two sign indicators sum to one and differ by \((-1)^{W_k(n)}\).

**Growing-window moments and normality.** The prime number theorem gives the weak convergence of the rescaled primes, in the form
\[
\sum_{L/2<p<L}h(p/L)=\frac{L}{\log L}\left(\int_{1/2}^{1}h(t)\,dt+o(1)\right)
\]
for each continuous \(h\) on \([1/2,1]\). Apply it to \(h(t)=t^{-1}-1\) and to \(h(t)=(t^{-1}-1)(2-t^{-1})\), noting that
\[
\int_{1/2}^{1}(t^{-1}-1)\,dt=\log2-\frac12,
\qquad
\int_{1/2}^{1}(t^{-1}-1)(2-t^{-1})\,dt=3\log2-2>0.
\]
Adding \(\pi(L/2)\sim L/(2\log L)\) gives the asserted mean and variance asymptotics. For independent Bernoulli variables of parameters \(\theta_{p,k}\), each centered third absolute moment is at most the variance of that variable. Hence the total third absolute moment is at most \(\sigma_k^2\), and the non-identically distributed Berry--Esseen inequality bounds the Kolmogorov distance by \(C/\sigma_k\). Since \(\sigma_k^2\asymp k/\log k\), this proves the quantitative normal approximation.

**Sharp sign decay.** Put \(x=L\) and \(g(t)=\log|3-2/t|\) for \(t\in[1/2,1]\), \(t\ne2/3\). Its logarithmic singularity at \(2/3\) is integrable, with
\[
\int_{1/2}^{1}\log|3-2/t|\,dt=-\frac23\log2.
\]
To justify summing the unbounded function at primes, take a positive constant \(c_0\) for which the classical prime number theorem error \(O(xe^{-c_0\sqrt{\log x}})\) holds uniformly on \([x/2,x]\), and set \(\eta_x=\exp(-c_0\sqrt{\log x}/3)\). Truncate to \(g_x(t)=\max\{g(t),\log\eta_x\}\). Its total variation is \(O(\sqrt{\log x})\). Stieltjes partial summation and the prime number theorem with the quoted error yield
\[
\sum_{x/2<p<x}g_x(p/x)=\frac{x}{\log x}\int_{1/2}^{1}g_x(t)\,dt+o(x/\log x).
\]
The integral differs from that of \(g\) by \(o(1)\). For \(x\ge4\), \(3p-2x\ne0\) for every prime \(p\) in the sum, so \(|3-2x/p|\ge1/x\). Truncation changes a summand only when \(|p-2x/3|\ll \eta_x x\). There are at most \(O(\eta_x x+1)\) *integers* in this interval, and each changed term has magnitude at most \(O(\log x)\). The total replacement error is therefore \(O((\eta_x x+1)\log x)=o(x/\log x)\). This proves
\[
\sum_{x/2<p<x}\log|3-2x/p|=
-\left(\frac23\log2+o(1)\right)\frac{x}{\log x}.
\]
Since \(x=k+1\) and the sign prefactor has absolute value one, the sign-bias theorem follows.

## Verification
The standalone `checker.py` uses only the Python standard library. It directly constructs the product-to-LCM quotient, counts its distinct prime divisors, and compares the resulting exact rational distribution with the Bernoulli product for every \(1\le k\le14\). It also tests that no smaller divisor of the proposed period is a period and checks the exact sign-bias zero among \(2\le k\le39\). On replay, it printed:

```
PASS: 543 exact quotient instances across k=1..14; distributions and least periods match.
PASS: exact sign bias vanishes for k=2 and for no k from 3 through 39.
```

The verifier is only a finite diagnostic. The statements for all \(k\), the least-period assertion, the normal limit, and the sign-decay constant are supported by the proofs above, not extrapolated from these samples.

## Relationship to prior work
The classical Farhi quotient and its least period were studied by Hong and Qian and are described in Huang and Yang's 2026 treatment of arithmetic-function quotients. Their principal theorem concerns periods of a multiplicative-function quotient, not the growing-window distribution of \(\omega(Q_k(n))\). Tian and Yang (2026) study additive sign patterns of \((-1)^{\omega(n)}\), rather than the unitary-Möbius sign of a Farhi quotient. A published finite value-frequency formula for arithmetic-progression LCM quotients supplies a broader exact *finite-period* framework: the generating polynomial here may be regarded as a specialization of that framework. The claimed new content is the sharp growing-window Gaussian mean and variance, quantitative normal approximation, and the explicit exponentially small parity-bias constant. Results on the **Liouville** sign of the same quotient concern \(\Omega\), not \(\omega\), and have a different balance criterion. A general finite census by itself supplies neither of the uniform growing-window estimates established here.

## Limitations
The probability law samples \(n\) over a full period at each fixed \(k\), then lets \(k\) grow. It does not quantify distribution in short intervals of \(n\), where the period may vastly exceed the interval. The asymptotic parity law is for the absolute bias only; it does not classify its sign changes. The result does not assert a new formula for the full quotient's least period. A closely related unindexed treatment, or an unpublished asymptotic extraction from earlier finite value-frequency formulas, could lessen the originality of the growing-window constants.

## References
1. Wen-Jie Huang and Quan-Hui Yang, *On least periods of a class of arithmetic functions*, arXiv:2611.15379v1 (11 November 2026), https://arxiv.org/abs/2611.15379.
2. Tian Caolin and Yang Chenxi, *A Goldbach-Type Problem for the Unitary Möbius Function*, arXiv:2611.10499v1 (7 November 2026), https://arxiv.org/abs/2611.10499.
3. Shaofang Hong and Guoyou Qian, *The least common multiple of consecutive arithmetic progression terms*, arXiv:0903.0530v3, *Proc. Edinburgh Math. Soc.* 54 (2011), 431–441, https://doi.org/10.1017/S0013091509000431.
4. Published SCOPE result, *Exact value-frequency law for consecutive arithmetic-progression LCM quotients* (26 October 2026), published-finding corpus index ID `2026/10/26/SCOPE-exact-value-frequency-law-for-consecutive-arithmetic-progression--8e35eb7b4fbc` (the index summary, not full paper, was available).
5. Classical prime number theorem with zero-free-region error, and classical non-identically distributed Berry--Esseen inequality, used in their standard unconditional forms.
