# Exact prime-power intersections of two translated cusps and the limiting GCD moment frontier

## Finding

For integers \(x,y\) let \(P(x,y)=x^2+y^3\) and \(Q(x,y)=(x+1)^2+(y+1)^3\). For every prime \(p\) and integer \(k\ge 1\), set
\[
R_{p,k}=\#\{(x,y)\in(\mathbb Z/p^k\mathbb Z)^2:P(x,y)\equiv Q(x,y)\equiv0\pmod{p^k}\}.
\]
The complete local formula is
\[
R_{p,k}=\begin{cases}
p^{\lfloor k/2\rfloor}+2\mathbf1_{\left(\frac{-2}{p}\right)=1},&p\ge5,\\
3^{k-1},&p=3,\ 1\le k\le3,\\
3^{k-2},&p=3,\ 4\le k\le6,\\
81+3^{k-\max\{3,\lceil(k-2)/2\rceil\}},&p=3,\ k\ge7,\\
2,&p=2,\ k=1,\\
4,&p=2,\ 2\le k\le5,\\
2^{\lfloor k/2\rfloor},&p=2,\ k\ge6.
\end{cases}
\]
Here \(\left(\frac{-2}{p}\right)\) is the Legendre symbol. For every integer \(m\ge1\), the number of simultaneous solutions modulo \(m\) is \(\prod_{p^k\parallel m}R_{p,k}\), with the empty product equal to one.

For independent uniform \(X_N,Y_N\in\{1,\ldots,N\}\), the GCD \(\gcd(P(X_N,Y_N),Q(X_N,Y_N))\) converges in distribution to an almost surely finite integer-valued \(G_\infty\). Its independent local valuations \(V_p=\nu_p(G_\infty)\) satisfy
\[
\mathbb P(V_p\ge k)=\frac{R_{p,k}}{p^{2k}}\quad(k\ge1).
\]
Consequently,
\[
\mathbb P(G_\infty=1)=\frac49\prod_{p\ge5}\left(1-\frac{2+\left(\frac{-2}{p}\right)}{p^2}\right),
\quad \mathbb E[G_\infty^t]<\infty\ \Longleftrightarrow\ t<1\quad(t\ge0).
\]
For **each fixed prime** \(p\), the different local threshold is \(\mathbb E[p^{tV_p}]<\infty\) exactly for \(0\le t<3/2\). A product truncated at primes below \(200001\) evaluates to approximately \(0.391193242\); this decimal is illustrative, without a certified tail error.

## Assumptions and scope

All polynomial coefficients, variables and moduli are integers; the ring is \(\mathbb Z/p^k\mathbb Z\) or \(\mathbb Z/m\mathbb Z\). Root counts include every ordered pair, and a simultaneous root is counted once. The Legendre symbol is used only for odd primes \(p\ge5\). The random-variable result uses the ordinary uniform positive square box and convergence **in distribution**, not convergence of moments of the finite-box random variables. The moment statements concern the limiting random variable only. For \(t<0\), its negative moments are trivially bounded by one.

## Proof

**1. Reduction for odd primes.** Subtracting the two equations gives
\[
Q-P=2x+3y^2+3y+2.
\]
When \(p\) is odd, this uniquely determines \(x\equiv-(3y^2+3y+2)/2\pmod{p^k}\). On substitution and multiplication by the unit \(4\), the remaining equation becomes
\[
F(y):=(y+1)^2(9y^2+4y+4)\equiv0\pmod{p^k}.
\]
Thus \(R_{p,k}\) is exactly the number of roots of \(F\) modulo \(p^k\).

**2. Primes at least five.** Put \(T(y)=9y^2+4y+4\). Its discriminant is \(-128=-2\cdot 8^2\), and \(T(-1)=9\) is a unit. The factor \(T\) has two distinct simple roots modulo \(p\) exactly when \(\left(\frac{-2}{p}\right)=1\), and no root otherwise. Every simple root has exactly one Hensel lift at each precision. Separately, the factor \((y+1)^2\) has precisely \(p^{\lfloor k/2\rfloor}\) roots modulo \(p^k\), since its valuation must be at least \(k\). The two root classes are disjoint because \(T(-1)\) is a unit. Summing proves the first case.

**3. The prime three.** Put \(u=y+1\). Then
\[
F(y)=u^2T(u-1),\qquad T(u-1)=9u^2-14u+9.
\]
As the derivative is \(-14\equiv1\pmod3\), Hensel lifting gives a unique root \(\alpha\in\mathbb Z_3\) with \(\alpha\equiv0\pmod3\). Its exact valuation is \(\nu_3(\alpha)=2\), since the constant term has valuation two and the linear coefficient is a unit; in fact \(\alpha\equiv18\pmod{27}\). Factorization gives
\[
9u^2-14u+9=(u-\alpha)[9(u+\alpha)-14],
\]
whose second factor is a 3-adic unit for every \(u\in\mathbb Z_3\). Therefore \(\nu_3(F)=2\nu_3(u)+\nu_3(u-\alpha)\). If \(\nu_3(u)=1\), this is exactly three; if \(\nu_3(u)=2\), it is \(4+\nu_3(u-\alpha)\) and at least six; if \(\nu_3(u)\ge3\), it is \(2\nu_3(u)+2\). For \(k\le3\), precisely the \(3^{k-1}\) residues divisible by three qualify. For \(4\le k\le6\), precisely the \(3^{k-2}\) residues divisible by nine qualify. For \(k\ge7\), the two disjoint qualifying branches are \(\nu_3(u)=2\) and \(u\equiv\alpha\pmod{3^{k-4}}\), giving exactly \(3^4=81\) residues, or \(\nu_3(u)\ge\max\{3,\lceil(k-2)/2\rceil\}\), giving \(3^{k-\max\{3,\lceil(k-2)/2\rceil\}}\) residues. This proves every ternary case.

**4. The prime two.** Directly modulo two there are exactly two simultaneous roots. For \(k\ge2\), subtracting gives
\[
2(x+1)\equiv-3y(y+1)\pmod{2^k}.
\]
Since \(y(y+1)\) is even, there are exactly two solutions for \(x\pmod{2^k}\) over each \(y\), separated by \(2^{k-1}\); their squares agree modulo \(2^k\). Choose \(x_0=-1-3y(y+1)/2\), and observe the exact integer identity \(4P(x_0,y)=F(y)\). Therefore \(R_{2,k}\) is twice the number of \(y\pmod{2^k}\) for which \(\nu_2(F(y))\ge k+2\).

For odd \(y\), \(T(y)\) is odd and \(\nu_2(F(y))=2\nu_2(y+1)\). For even \(y=2z\), \(T(y)=4(9z^2+2z+1)\), while \(y+1\) is odd. If \(z\) is even, the valuation is two. If \(z\equiv1\pmod4\), it is four; if \(z\equiv3\pmod4\), it is five. The latter assertions follow from \(9(9z^2+2z+1)=(9z+1)^2+8\). Counting these cases gives four roots for every \(2\le k\le5\). For \(k\ge6\), no even \(y\) qualifies; the odd residues must obey \(\nu_2(y+1)\ge\lceil(k+2)/2\rceil\). There are \(2^{k-\lceil(k+2)/2\rceil}\) such \(y\), each with two corresponding \(x\), giving \(2^{\lfloor k/2\rfloor}\). This proves every binary case.

**5. Arbitrary moduli, convergence and moments.** Chinese remaindering proves multiplicativity of \(R_m\). Because \(Q-P\) is linear in \(x\) and substituting its unique rational solution into \(P\) gives the nonzero quartic \(F/4\), the two polynomials have no nonconstant common factor over \(\mathbb Q[x,y]\). Kabluchko–Marynych [1, Theorem 3.1] therefore supplies convergence to an almost surely finite GCD whose independent prime-adic valuation tails equal the Haar probabilities \(R_{p,k}/p^{2k}\). The density of \(G_\infty=1\) is the product of their complements at \(k=1\): the factors at two and three are respectively \(1/2\) and \(8/9\); for \(p\ge5\), the root count is \(2+\left(\frac{-2}{p}\right)\).

For any nonnegative integer-valued \(V\) and \(t\ge0\), tail summation yields
\[
\mathbb E[p^{tV}]=1+\sum_{k\ge1}(p^{tk}-p^{t(k-1)})\mathbb P(V\ge k).
\]
For each fixed prime, the exact formulas imply \(R_{p,k}\) is bounded above and below by positive prime-dependent multiples of \(p^{k/2}\) for all sufficiently large \(k\). Hence its local series converges exactly for \(t<3/2\). To establish the **global** moment boundary, for every \(t<1\) the sum of excess local Euler factors is bounded, apart from finitely many small primes, by a constant times \(\sum_{p\ge5}(p^{t-2}+p^{2t-3})\), which converges for \(t<1\) (the terms with \(k\ge3\) are a geometric tail). Consequently the product of local moments converges. For \(t\ge1\), the first-level tail gives \(\mathbb E[p^{tV_p}]-1\ge(p^t-1)/p^2\) for every prime \(p\ge5\). The divergence of \(\sum_p1/p\) then forces the product of local moments, and thus \(\mathbb E[G_\infty^t]\), to diverge. Nonnegative monotone convergence justifies the infinite product.

## Verification

The standalone file `check_counts.py` uses only Python's standard library and evaluates the two **original** congruences, not the factored quartic, at 71 prime-power cases; direct full square-box enumeration validates 29 of those small prime-power cases and 19 composite CRT cases. All 119 tests passed. This computation checks finite cases only; the all-primes and all-precisions statements follow from the proof. The decimal Euler-product illustration uses primes through 200000 and has no rigorous error interval.

## Relationship to prior work

Kabluchko and Marynych [1] establish the general polynomial-GCD distribution convergence under a coprimality hypothesis. The exact local intersection counts, their exceptional prime two and prime three branches, and the two distinct moment frontiers here are not stated in [1]; this result *uses* their convergence theorem and does not claim to reprove it. Bodin and Dèbes [2] discuss coprime polynomial values, gcd/lcm stability and Euler-product densities, but do not tabulate this two-curve all-prime-power intersection spectrum. Local counting methods (Hensel lifting, character tests and valuation stratification) are standard; the content is the exact simultaneous cuspidal intersection classification and its consequences.

## Limitations

No quantitative finite-box convergence rate is asserted. There is no assertion that the finite-box GCD moments converge to the moments of \(G_\infty\). Exact local counts can conceivably be derived implicitly from a more general, unindexed local-zeta or arithmetic intersection theorem; the accessible inspected sources do not settle that bibliographic possibility. The numerical density is only a truncated-product estimate. This work has not received an independent mathematical audit.

## References

[1] Z. Kabluchko and A. Marynych, *Divisibility properties of polynomial expressions of random integers*, first publicly posted 2023-11-09, arXiv:2311.05369v1, https://arxiv.org/html/2311.05369v1 (Theorem 3.1, Section 4 and Remark 4.4).

[2] A. Bodin and P. Dèbes, *Coprime values of polynomials in several variables*, arXiv:2105.13883, first posted 2021-05, https://arxiv.org/html/2105.13883v3 (Sections 1, 5, 6).
