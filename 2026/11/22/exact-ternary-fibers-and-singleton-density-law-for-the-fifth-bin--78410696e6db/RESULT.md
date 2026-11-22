# Exact ternary fibers and singleton-density law for the fifth binomial column

## Finding
Let \(F(n)=\binom n5\). For \(k\ge1\), the least period of \(F(n)\pmod{3^k}\) is \(3^{k+1}\), and define
\[
N_k(y)=\#\{0\le n<3^{k+1}:F(n)\equiv y\pmod{3^k}\}.
\]
There are two uniquely defined critical 3-adic values \(\beta_0,\beta_1\in3\mathbb Z_3\), with \(\beta_0\equiv6\pmod9\) and \(\beta_1\equiv3\pmod9\), described explicitly below. Define \(R_0(z)=1\) and, for \(m\ge1\),
\[
R_m(z)=\#\{u\bmod3^m:u^2\equiv z\pmod{3^m}\}.
\]
Then for every \(k\ge1\) and every \(y\bmod3^k\),
\[
\boxed{N_k(y)=1+3\mathbf1_{3\mid y}\left[R_{k-1}\!\left(\frac{y-\beta_0}{3}\right)+R_{k-1}\!\left(\frac{\beta_1-y}{3}\right)\right].}
\]
The two quotients are used only when \(3\mid y\), and the square-root counts depend only on their residues modulo \(3^{k-1}\). In particular every target is attained, but multiplicities vary with the target and exponent.

Let \(Q_0=1\), and for \(m\ge1\) let
\[
Q_m=1+\sum_{j=0}^{\lfloor(m-1)/2\rfloor}3^{m-2j-1},
\]
the exact number of squares modulo \(3^m\), including zero. For \(k\ge3\), the number of targets with a **unique** preimage in a least period is exactly
\[
\boxed{U_k=3^k-3^{k-2}-2Q_{k-3};\qquad\lim_{k\to\infty}\frac{U_k}{3^k}=\frac{31}{36}.}
\]
For \(k\ge4\), the maximal fiber size is
\[
\boxed{\max_yN_k(y)=\begin{cases}
1+2\cdot3^{k/2},&k\text{ even},\\
1+3^{(k+1)/2},&k\text{ odd},
\end{cases}}
\]
and precisely two target classes attain it. The maxima at \(k=1,2,3\) are \(7,13,13\), respectively.

## Assumptions and scope
All indices \(n\) are nonnegative integers, and all moduli are powers of three. Write the 3-adic integer-valued polynomial \(P(x)=x(x-1)(x-2)(x-3)(x-4)/120\). For \(r\in\{0,1,2\}\), set \(g_r(t)=P(r+3t)\). Explicitly,
\[
\begin{aligned}
g_0(t)&=\frac{3t(t-1)(3t-4)(3t-2)(3t-1)}{40},\\
g_1(t)&=\frac{3t(t-1)(3t-2)(3t-1)(3t+1)}{40},\\
g_2(t)&=\frac{t(3t-2)(3t-1)(3t+1)(3t+2)}{40}.
\end{aligned}
\]
Because 40 is a 3-adic unit, all three are polynomials over \(\mathbb Z_3\). Set \(h_0=g_0/3\), \(h_1=g_1/3\), and \(\sigma_0=1\), \(\sigma_1=-1\). For each \(r\in\{0,1\}\), let \(\alpha_r\in\mathbb Z_3\) be the unique root of \(h_r'(\alpha_r)=0\), with \(\alpha_r\equiv2\pmod3\), and put \(\beta_r=g_r(\alpha_r)\). Existence and uniqueness are proved below. These values need not be rational integers; their reductions are computed unambiguously by Hensel lifting.

For clarity, for \(m\ge1\), if \(z\equiv0\pmod{3^m}\) then \(R_m(z)=3^{\lfloor m/2\rfloor}\). Otherwise let \(v\) be the valuation of \(z\) truncated below \(m\); then \(R_m(z)=0\) if \(v\) is odd or the unit part is \(2\pmod3\), and \(R_m(z)=2\cdot3^{v/2}\) if \(v\) is even and the unit part is \(1\pmod3\). Thus the main formula is fully evaluable by integer arithmetic at every finite level.

## Proof
**1. Period.** Vandermonde's identity gives, with \(H=3^{k+1}\),
\[
P(n+H)-P(n)=\sum_{j=1}^{5}\binom Hj\binom n{5-j}.
\]
Since \(H\ge9\) and \(1\le j\le5\), one has \(\nu_3(\binom Hj)=k+1-\nu_3(j)\ge k\). Hence \(H\) is a period modulo \(3^k\). The third branch is an isometry (step 2). Replacing \(n=2+3t\) by \(n+3^k\) changes \(t\) by \(3^{k-1}\), and therefore changes \(g_2(t)\) by an element of exact valuation \(k-1\). Thus \(3^k\) is not a period. Since the least period divides \(H\), it is exactly \(H\).

**2. A regular bijective branch.** Coefficientwise reduction of the displayed polynomials gives \(g_2(t)\equiv t\pmod3\). Hence \(g_2(t)=t+3A(t)\) with \(A\in\mathbb Z_3[t]\), and
\[
g_2(t)-g_2(s)=(t-s)(1+3B(t,s)),\qquad B\in\mathbb Z_3[t,s].
\]
Thus \(g_2\) is an isometry on \(\mathbb Z_3\). Its induced map on each finite quotient is injective and therefore bijective; equivalently it is a 3-adic bijection. This branch contributes exactly one index in \(n=2+3t\) modulo the full least period for every \(y\pmod{3^k}\), since \(t\) runs through \(3^k\) classes.

**3. Two global quadratic branches.** Coefficientwise modulo-three reduction gives
\[
h_r(t)\equiv\sigma_r t(t-1)\pmod3\qquad(r=0,1).
\]
Consequently \(h_r'(t)\equiv\sigma_r(2t-1)\pmod3\), with a single simple root \(t\equiv2\pmod3\). Hensel's lemma supplies the unique \(\alpha_r\). Writing \(t=\alpha_r+u\), Taylor expansion (with coefficients in \(\mathbb Z_3\)) yields
\[
h_r(\alpha_r+u)=h_r(\alpha_r)+u^2 B_r(u),\qquad
B_r(u)\equiv\sigma_r\pmod3.
\]
Every element of \(1+3\mathbb Z_3\) has a unique square root congruent to one modulo three. Put \(S_r(u)=\sqrt{B_r(u)/\sigma_r}\) and \(\phi_r(u)=uS_r(u)\). For \(u,v\in\mathbb Z_3\), the difference of the corresponding square roots satisfies \(S_r(u)-S_r(v)\in3(u-v)\mathbb Z_3\): subtract their squares and use that their sum is a unit. Therefore
\[
\phi_r(u)-\phi_r(v)=(u-v)\bigl(S_r(u)+v\,C(u,v)\bigr),
\quad C(u,v)\in3\mathbb Z_3,
\]
so \(\phi_r\) is an isometry. It maps every finite quotient injectively to itself, hence bijectively, and therefore is an onto 3-adic isometry. The exact, global normal form is
\[
\boxed{g_r(\alpha_r+u)=\beta_r+3\sigma_r\phi_r(u)^2.}
\]
Modulo nine, \(g_r(\alpha_r)\equiv g_r(2)\) since \(g_r\) is three times an integral polynomial and \(\alpha_r\equiv2\pmod3\). Now \(g_0(2)=\binom65=6\) and \(g_1(2)=\binom75=21\), giving \(\beta_0\equiv6\pmod9\) and \(\beta_1\equiv3\pmod9\). Their output balls are therefore disjoint modulo nine.

**4. Fiber formula.** For a fixed \(k\) and \(r=0,1\), the quadratic normal form requires \(3\mid y\) and
\[
\phi_r(u)^2\equiv\sigma_r\frac{y-\beta_r}{3}\pmod{3^{k-1}}.
\]
There are \(R_{k-1}\) solutions \(u\bmod3^{k-1}\), and each has exactly three lifts modulo \(3^k\). The value \(n=r+3t\) has exactly these \(t\)-classes in one period. The third branch contributes one everywhere; adding proves the boxed formula, including \(k=1\) by \(R_0=1\).

**5. Singleton targets and maxima.** When \(k\ge3\), the targets divisible by nine (exactly \(3^{k-2}\) classes) receive 12 additional solutions from the two quadratic branches and have \(N_k(y)=13\). Among outputs \(y\equiv6\pmod9\), only the first quadratic branch can contribute more than one, and its nonzero additional contributions occur exactly in \(\beta_0+27\mathbb Z_3^2\), giving \(Q_{k-3}\) target classes modulo \(3^k\). Similarly \(y\equiv3\pmod9\) contributes the disjoint component \(\beta_1-27\mathbb Z_3^2\), also \(Q_{k-3}\) classes. Everything else has one solution. Thus \(U_k=3^k-3^{k-2}-2Q_{k-3}\).

For \(m\ge1\), the largest value of \(R_m\) is \(3^{m/2}\) if \(m\) is even (only at \(z\equiv0\pmod{3^m}\)), and \(2\cdot3^{(m-1)/2}\) if \(m\) is odd and at least three (only at \(z\equiv3^{m-1}\pmod{3^m}\)). At \(k\ge4\), \(m=k-1\ge3\), and each of the two disjoint critical balls contributes exactly one maximizing target. Multiplying the maximum square-root count by three and adding one gives the formula for \(\max_yN_k(y)\). Directly substituting \(k=1,2,3\) yields the initial maxima. Finally, by the sum formula for \(Q_m\), \(Q_m/3^m\to3/8\), and hence \(U_k/3^k\to1-1/9-2(3/8)/27=31/36\).

## Verification
The included standard-library program `verify.py` performs independent exact integer enumeration of \(F(n)\pmod{3^k}\) over the entire least period for every \(1\le k\le10\), totaling 88,572 target comparisons and 265,716 index values. It compares every observed fiber to the stated square-root formula, verifies 3-adic Hensel lifts of both critical values, independently verifies the square-root count formula through level six, and checks all claimed singleton counts and maximal sizes within the tested range. Run `python3 verify.py`; no external dependencies are needed. This computation corroborates the algebraic argument; it is not substituted for the proof at unbounded \(k\).

## Relationship to prior work
Fiorot, Gilblas, and Tonolo, *Modular binomials with an application to periodic sequences* (initial posting 2023-07-05), analyze finite-modulus primitive sequences and periodic binomial columns, including the known period of \(\binom n5\) modulo powers of three. Neither the period nor the underlying binomial congruences are claimed as new. Sun and Zhang (first public posting 2008-12-16) already show that the fifth binomial column meets **every** residue class modulo every power of three. Surjectivity is explicitly excluded from the novelty claim. Their stated density criterion does not give the exact number of preimages per period, the two quadratic critical values, the singleton-target count, or the maximal multiplicities.

The published result *Exact three-level 2-adic fibers of the fifth binomial column* treats the **same column** for powers of two, explicitly without odd-prime claims. The result *Exact ternary residue images of the sixth binomial polynomial* treats the **different lower index six** and classifies image support rather than the present fifth-column preimage counts. Multiplying \(\binom n5\) by the input-dependent factor \((n-5)/6\) to obtain \(\binom n6\) is not a reversible transformation over \(\mathbb Z_3\), so the latter result does not imply this fiber law. The standard Hensel and square-map lemmas used in the proof are classical techniques; only their evaluated application to these three specific branches and exact distributional consequences are claimed.

## Limitations
The theorem concerns the fixed lower index five at powers of three; no classification for all lower indices or other primes is asserted. The exact 3-adic critical values are given by unique Hensel roots rather than rational closed forms, but their reductions are algorithmically explicit. The comparison covers the named primary sources and accessible research records; an unindexed equivalent statement could exist. Finite verification covers the displayed tested moduli, not infinitely many levels. Independent audit has not been performed.

## References
1. Luisa Fiorot, Riccardo Gilblas, and Alberto Tonolo, *Modular binomials with an application to periodic sequences*, arXiv:2307.02366v1 (initially posted 2023-07-05), https://arxiv.org/abs/2307.02366 . Published version: *Periodic sequences, binomials modulo a prime power, and a math/music application*, *Advances in Applied Mathematics* **162** (2025), 102786, https://doi.org/10.1016/j.aam.2024.102786 .
2. Zhi-Wei Sun and Wei Zhang, *Binomial coefficients and the ring of p-adic integers*, arXiv:0812.3089 (first public posting 2008-12-16), *Proceedings of the American Mathematical Society* **139** (2011), 1569–1577, https://arxiv.org/abs/0812.3089 .
3. *Exact three-level 2-adic fibers of the fifth binomial column*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-three-level-2-adic-fibers-of-the-fifth-binomial-column--68ab08bc975b .
4. *Exact ternary residue images of the sixth binomial polynomial*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-residue-images-of-the-sixth-binomial-polynomial--2c5deda1b9d1 .
