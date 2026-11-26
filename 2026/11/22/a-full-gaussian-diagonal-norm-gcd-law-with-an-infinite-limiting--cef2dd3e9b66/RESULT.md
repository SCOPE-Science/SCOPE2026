# A full Gaussian-diagonal norm-GCD law with an infinite limiting mean

## Finding
For positive integers \(x,y\), define
\[
A(x,y)=x^2+y^2,\qquad B(x,y)=(x+1)^2+(y+1)^2,
\qquad G(x,y)=\gcd(A(x,y),B(x,y)).
\]
For any positive integer \(m\), the number of simultaneous congruence roots satisfies the exact formula
\[
R(m):=\#\{(x,y)\bmod m:m\mid G(x,y)\}
=\begin{cases}
2^{\omega(m)},&4\nmid m\ \text{and every odd prime }p\mid m\text{ obeys }p\equiv1\pmod4,\\
0,&\text{otherwise},
\end{cases}
\]
where \(\omega(1)=0\). If \((X_N,Y_N)\) is uniform on \(\{1,\ldots,N\}^2\), then \(G(X_N,Y_N)\) converges in distribution, as \(N\to\infty\), to a finite positive integer-valued random variable \(G_\infty=\prod_p p^{V_p}\), with independent local exponents specified by
\[
\begin{aligned}
&\mathbb P(V_2=0)=\mathbb P(V_2=1)=\tfrac12,\\
&V_p=0\text{ almost surely if }p\equiv3\pmod4,\\
&\mathbb P(V_p=0)=1-2p^{-2},\quad p\equiv1\pmod4,\\
&\mathbb P(V_p=e)=2(1-p^{-2})p^{-2e},\quad e\ge1,\quad p\equiv1\pmod4.
\end{aligned}
\]
In particular,
\[
\mathbb P(G_\infty=1)=\mathbb P(G_\infty=2)
=\frac12\prod_{p\equiv1\ (\mathrm{mod}\ 4)}(1-2p^{-2})
\approx0.44742061.
\]
Despite almost-sure finiteness, its exact moment threshold is
\[
\boxed{\mathbb E[G_\infty^t]<\infty\quad\Longleftrightarrow\quad t<1}
\qquad(t\in\mathbb R).
\]
Thus the limiting mean is infinite. The same result supplies every individual probability, by multiplying the local masses in the unique prime factorization of its argument.

## Assumptions and scope
The sampling box is the uniform product measure on ordered positive integer pairs \((x,y)\in\{1,\ldots,N\}^2\); the limiting law is not a statement about the size-normalized GCD or Gaussian greatest common divisors. The rational-integer gcd is always taken positive. A prime in a congruence may have any exponent; the formula for \(R(m)\) includes \(m=1\). The moment assertion concerns the limiting distribution only, not a uniform bound on the finite-box means.

## Proof
**Exact prime-power congruence count.** Since
\[
B(x,y)-A(x,y)=2(x+y+1),
\]
for odd primes \(p\), the two congruences modulo \(p^e\) are equivalent to \(y\equiv-x-1\) and
\[
(2x+1)^2\equiv-1\pmod{p^e}.
\]
For \(p\equiv1\pmod4\), \(-1\) has exactly two roots modulo \(p\). Both roots are simple, so Hensel lifting gives exactly two roots modulo every \(p^e\), yielding exactly two ordered pairs. For \(p\equiv3\pmod4\), no roots exist. Modulo \(2\), precisely the two pairs with \(x\equiv y\pmod2\) solve both equations. Modulo \(4\), no pair solves them: opposite parities make \(A\) odd, while equal parities make one of \(A,B\) congruent to \(2\pmod4\). The Chinese remainder theorem now gives the formula for \(R(m)\), including arbitrary products of prime powers.

**Finite-local limits and independence.** Fix any finite collection of prime powers. Uniform sampling from the box becomes uniform modulo their product, with error tending to zero. The Chinese remainder theorem makes the divisibility events for different primes independent in the limit. Dividing the prime-power root counts by \(p^{2e}\) gives \(\mathbb P(V_p\ge e)=2/p^{2e}\) for \(p\equiv1\pmod4\), and \(\mathbb P(V_2\ge1)=1/2\), \(\mathbb P(V_2\ge2)=0\). Subtracting tails gives exactly the displayed local exponent laws.

**No probability escapes through large primes.** If an odd prime \(p\) divides both norms in the sampling box, then \(p\mid x+y+1\), so \(p\le2N+1\). For each such prime the simultaneous root condition forces \(2x+1\) to be one of at most two residues modulo \(p\), and then forces \(y\equiv-x-1\pmod p\). Thus at most \(2(N/p+1)^2\) pairs in the box have \(p\mid G\). For \(Y\ge3\), the union bound yields
\[
\mathbb P\bigl(\exists p>Y:p\mid G(X_N,Y_N)\bigr)
\le\frac2{N^2}\sum_{Y<p\le2N+1}(N/p+1)^2.
\]
The upper limit of the right-hand side as \(N\to\infty\) is bounded by \(2\sum_{p>Y}p^{-2}\), which tends to zero as \(Y\to\infty\); terms arising from \(N^{-1}\sum_{p\le2N+1}p^{-1}\) and \(N^{-2}\pi(2N+1)\) vanish. In addition the local series \(\sum_{p\equiv1(4)}\mathbb P(V_p>0)=\sum_{p\equiv1(4)}2p^{-2}\) converges. Therefore the independent-prime product is almost surely finite, the finite-local limits extend to the complete integer-valued law, and its mass function is exactly the product of local masses.

**Coprimality probability and moment transition.** The event that every \(V_p=0\) has probability the displayed convergent Euler product, with the factor \(1/2\) from \(p=2\). As \(V_2=1\) also has probability \(1/2\), and the odd components are independent, the probabilities at \(1\) and \(2\) coincide. For a split prime and \(t<2\), geometric summation gives
\[
\mathbb E[p^{tV_p}]
=1-2p^{-2}+\frac{2(1-p^{-2})p^{t-2}}{1-p^{t-2}}.
\]
When \(t<1\), its deviation from one is \(O_t(p^{t-2})\), and \(\sum_p p^{t-2}<\infty\). Product convergence, monotone convergence for nonnegative factors when \(t\ge0\), and elementary boundedness for \(t<0\) show the stated finiteness. At \(t=1\), the split-prime factor simplifies **exactly** to \(1+2/p\), so the full formal mean-product is \(\frac32\prod_{p\equiv1\ (\mathrm{mod}\ 4)}(1+2/p)\). The classical divergence of the reciprocal-prime sum in the progression \(p\equiv1\pmod4\) forces the product of these factors to diverge. Therefore \(\mathbb E[G_\infty]=\infty\). For \(t>1\), the inequality \(G_\infty^t\ge G_\infty\) completes the divergence argument. This proves the exact moment frontier.

## Verification
An exact-integer checker (`checker.py`) compares direct pairs with the Chinese-remainder formula for every modulus \(1\le m\le129\), and tests divisibility support and empirical coprimality frequencies in square boxes of sides \(100,300,600\). The execution output is included in `verification_output.txt`. For the decimal, the partial product \(P_M=\frac12\prod_{p\le M,\ p\equiv1\ (4)}(1-2p^{-2})\) at \(M=10^8\) is about \(0.447420612512\). Since \(\sum_{k\ge0}2/(M+1+4k)^2\le 2/(M+1)^2+1/(2(M+1))\), multiplying \(P_M\) by one minus this bound gives a lower bound for the full product; \(P_M\) itself is an upper bound. This yields the eight-place rounding above and is not needed for the proof. No finite enumeration is used to justify the infinite distribution or moment statements.

## Relationship to prior work
Kabluchko and Marynych, *Divisibility properties of polynomial expressions of random integers* (first public posting 2023-11-09), already imply convergence and an independent-local representation for this pair (Theorem 3.1): a common nonconstant factor would have to divide \(2(x+y+1)\), but the restriction of \(A\) to that line is \(2x^2+2x+1\), not zero. Their Remark 4.4 also gives the form of the coprimality Euler product. The contribution here is to evaluate the prime-power counts, local masses and sharp moment boundary explicitly; the elementary large-prime argument is an alternative proof for this pair. Bodin and Dèbes treat general coprimality densities. Magness, Nugent, and Robertson discuss divisibility on primitive Gaussian lines. A related fixed-line norm-GCD spectrum does not give this two-dimensional box-sampling distribution or its infinite-mean threshold. A homogeneous-form resultant-density theorem is not applicable to this inhomogeneous translated pair.

## Limitations
The result concerns exactly the diagonal shift \((1,1)\) and the limiting random variable for a two-coordinate box; it does not give rates of convergence or asymptotics for finite-box moments. Only the limiting mean is asserted infinite. The complete law is an explicit specialization of general polynomial-GCD convergence techniques, and the possibility of an implicit equivalent in an unindexed source or a stronger universal theorem is an originality risk.

## References
1. Z. Kabluchko and A. Marynych, *Divisibility properties of polynomial expressions of random integers*, arXiv:2311.05369v1 (first posted 2023-11-09), Theorem 3.1, https://arxiv.org/html/2311.05369v1.
2. A. Bodin and P. Dèbes, *Coprime values of polynomials in several variables*, arXiv:2105.13883 (first posted 2021-05-28), https://arxiv.org/html/2105.13883v3.
3. E. Magness, B. Nugent, and L. Robertson, *Walking to Infinity Along Gaussian Lines*, arXiv:2001.05018 (first posted 2020-01-14), https://arxiv.org/abs/2001.05018.
4. *Complete norm-gcd spectrum on primitive Gaussian lines* (2026-10-12), Resultary, record 395dc3659689.
5. *Finite-resultant correction for coprime values of homogeneous binary forms* (2026-10-04), Resultary, record 0efa4a963ad2.
