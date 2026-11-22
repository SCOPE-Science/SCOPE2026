# Exact Liouville-parity cancellation for consecutive-integer LCM quotients

## Finding
For integers \(k\ge 1\) and \(n\ge1\), define Farhi's integer quotient
\[
Q_k(n)=\frac{\prod_{i=0}^k(n+i)}{\operatorname{lcm}(n,n+1,\ldots,n+k)},\qquad
\lambda(m)=(-1)^{\Omega(m)},
\]
where \(\Omega(m)\) counts prime factors with multiplicity. Let \(L_k=\operatorname{lcm}(1,\ldots,k)\), with \(L_1=1\). The exact natural-density mean, equivalently the signed mean over this period, is
\[
B_k=\lim_{X\to\infty}\frac1X\sum_{n=1}^X\lambda(Q_k(n))
=\frac1{L_k}\sum_{n=1}^{L_k}\lambda(Q_k(n)).
\]
**Theorem.** For every integer \(k\ge1\),
\[
\boxed{B_k=0\ \Longleftrightarrow\ k+1=3\cdot2^a\quad\text{for some integer }a\ge0.}
\]
Consequently the number of inputs giving even \(\Omega(Q_k(n))\) equals the number giving odd \(\Omega(Q_k(n))\) in any complete period exactly for \(k=2,5,11,23,47,\ldots\). At all other window lengths there is a strict parity imbalance. This is a statement about **total** prime-factor multiplicity, not the distinct-prime count \(\omega\).

## Assumptions and scope
Every product and least common multiple consists of positive integers, and \(k,n\) have the ranges above. All signs are \(+1\) or \(-1\); no zero is possible. An identity of means is not a claim that the least positive period equals \(L_k\): it suffices that \(L_k\) is a period. The theorem classifies exact balance and does not assert a universal sign for nonzero \(B_k\).

## Proof
**Prime-local valuation and product mean.** Fix a prime \(p\le k\), put \(e_p=\lfloor\log_p k\rfloor\), and for \(1\le j\le e_p\) define
\[
N_{p^j}(n)=\#\{0\le i\le k:p^j\mid n+i\}.
\]
For each \(j\le e_p\), at least one member of the interval is divisible by \(p^j\), so the contribution of the largest valuation to the denominator is exactly one at this level. For \(j>e_p\), there is at most one such member and its contribution cancels. It follows without a finite cut-off on the individual valuations that
\[
\nu_p(Q_k(n))=\sum_{j=1}^{e_p}(N_{p^j}(n)-1). \tag{1}
\]
For \(p>k\), at most one member of the interval is divisible by \(p\), hence \(\nu_p(Q_k(n))=0\). Thus every local exponent depends only on \(n\bmod p^{e_p}\), and the Chinese remainder theorem gives the exact signed-mean factorization
\[
B_k=\prod_{p\le k}b_{p,k},\quad
b_{p,k}=\frac1{p^{e_p}}\sum_{t\bmod p^{e_p}}
(-1)^{\sum_{j=1}^{e_p}(N_{p^j}(t)-1)}. \tag{2}
\]
For odd \(p\), the numerator of \(b_{p,k}\) is a sum of an odd number \(p^{e_p}\) of signs, so it is an **odd integer**, in particular nonzero. Therefore \(B_k\) can vanish only through its factor at \(p=2\).

**Reduction to a dyadic cyclic word.** For \(k\ge2\), put \(e=\lfloor\log_2 k\rfloor\), \(M=2^e\), and write \(k+1=M+r\), where \(1\le r\le M\). On residues modulo \(M\), let \(v_e(t)=\min\{\nu_2(t),e\}\), with \(v_e(0)=e\), and set
\[
S_e(r)=\sum_{t=0}^{M-1}(-1)^{\sum_{i=0}^{r-1}v_e(t+i)},\qquad 0\le r\le M,
\tag{3}
\]
where the arguments are interpreted modulo \(M\), and an empty sum is zero. A full block of \(M\) consecutive integers contributes \(M-1\) to the sum of their truncated \(2\)-adic valuations, while equation (1) subtracts \(e\). Therefore
\[
b_{2,k}=\frac{(-1)^{M-1-e}}M S_e(r).\tag{4}
\]

**Exact dyadic recurrence.** For all \(e\ge2\), separating even and odd starting residues in (3) gives
\[
S_e(2h)=2(-1)^h S_{e-1}(h),\qquad
S_e(2h+1)=(-1)^h\big(S_{e-1}(h)-S_{e-1}(h+1)\big).
\tag{5}
\]
Indeed the sign associated with \(2u\) is \(-(-1)^{v_{e-1}(u)}\), whereas every odd argument contributes sign \(+1\). Pairing successive even-odd entries proves the first recurrence; adjoining one final entry to each pair block proves the second. The base arrays are
\[
(S_1(0),S_1(1),S_1(2))=(2,0,-2),\quad
(S_2(0),\ldots,S_2(4))=(4,2,0,-2,-4).
\tag{6}
\]
We prove by induction on \(e\ge2\) the stronger claim
\[
S_e(0)=2^e,\qquad S_e(2^e)=-2^e,\qquad S_e(2^{e-1})=0,
\tag{7}
\]
and, for all other integers \(1\le r<2^e\),
\[
\nu_2(S_e(r))=1+\nu_2(r).\tag{8}
\]
Here \(\nu_2\) is applied only to nonzero integers. Equations (6) establish the case \(e=2\). Assume (7)–(8) at exponent \(e-1\). The even-index recurrence proves (7) at the endpoints and midpoint and proves (8) at every other even index (with its valuation increased by one). For any odd index \(2h+1\), exactly one of \(h,h+1\) is odd. At exponent \(e-1\ge2\), (8) says that its \(S\)-value has valuation exactly one; the other, even-index value has valuation at least two or is zero, by (7)–(8). Their difference thus has valuation exactly one. This proves (8) at all odd indices and completes the induction. The separate case \(e=1\) follows directly from the first array in (6). Consequently,
\[
S_e(r)=0\quad\Longleftrightarrow\quad r=2^{e-1}
\qquad (e\ge1,\ 1\le r\le2^e).\tag{9}
\]
By (4), \(b_{2,k}=0\) precisely when \(k+1=2^e+2^{e-1}=3\cdot2^{e-1}\). For \(k=1\), the quotient is identically one and \(B_1=1\). Combined with the nonzero odd-prime factors in (2), this proves the theorem. \(\square\)

## Verification
`verify.py` (Python 3 standard library) independently computes \(Q_k(n)\) by products and least common multiples, computes local signs from (1), compares them against complete-period means, and checks (5) both recursively and from the underlying cyclic word. The recorded execution passed **34,161 directly enumerated quotient residues**, **1,031 truncated-valuation word sums** (levels \(1\) through \(9\)), and **3,373 prime-local signed sums** across \(2\le k\le160\). The first exact-balanced window lengths detected were \(2,5,11,23,47,95\). These finite checks corroborate but do not replace the proof for all \(k\).

## Relationship to prior work
Farhi introduced the quotient, and Farhi–Kane and later Huang–Yang studied its least period; equation (1) is a specialization of established local valuation counting. Huang and Yang's 2026 paper determines least periods for a broad class of multiplicative-function quotients, but its full text does not state a Liouville-sign mean or an all-window cancellation classification. An earlier explicit prime-local **value-frequency** formula determines the entire fixed-window distribution of \(Q_k(n)\) and hence already determines \(B_k\) for **each fixed** \(k\) by evaluating its polynomial at \(-1\) at every prime. The present contribution is specifically the **uniform all-window exact zero locus** and its valuation-rigidity proof, not the existence of a finite mean formula or the CRT factorization. Another indexed result studies a distinct statistic \((-1)^{\omega(Q_k(n))}\); replacing \(\omega\) by \(\Omega\) changes the zero set and cannot be inferred from its Bernoulli product. No matching all-window classification was located in the searched records or inspected primary sources.

## Limitations
No assertion about the sign, nonzero magnitude, or asymptotic decay rate of \(B_k\) is made. The general fixed-window signed mean is already implied by a broader prior value-distribution theorem; originality is confined to the exact **infinite family of balanced windows** and the exclusion of all others. The broader formula makes this a structural refinement rather than a discovery of a new factorization identity. Literature discovery is not a proof of publication priority; other indexed or unindexed treatments may encode an equivalent zero classification. Independent mathematical verification has not been performed.

## References
- W.-J. Huang and Q.-H. Yang, *On least periods of a class of arithmetic functions*, arXiv:2611.15379v1, publicly submitted 2026-11-11, https://arxiv.org/abs/2611.15379; full text and proof of Theorem 1.1.
- B. Farhi and D. Kane, *New results on the least common multiple of consecutive integers*, arXiv:0808.1507, https://arxiv.org/abs/0808.1507.
- S. Hong and G. Qian, *The least common multiple of consecutive arithmetic progression terms*, arXiv:0903.0530, https://arxiv.org/abs/0903.0530.
- *Exact value-frequency law for consecutive arithmetic-progression LCM quotients*, published mathematical result (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-value-frequency-law-for-consecutive-arithmetic-progression--8e35eb7b4fbc, especially `RESULT.md` and its carry-matrix formula.
