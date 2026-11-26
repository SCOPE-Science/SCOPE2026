# Exact cubic two-adic valuations of central Delannoy numbers

## Finding
Let \(D_n=\sum_{k=0}^{n}2^k\binom nk^2\). For every positive integer \(n\equiv0\pmod4\),
\[
\nu_2(D_n-1)=3\nu_2(n).
\]
For every nonnegative integer \(n\equiv3\pmod4\),
\[
\nu_2(D_n+1)=3\nu_2(n+1).
\]
Thus all three central-Delannoy valuation conjectures numbered 1, 2, 3 in Lengyel (2021) hold, including their uniformity in odd multipliers and unbounded two-power heights. A stronger analytic assertion is proved: for every \(x\in4\mathbb Z_2\setminus\{0\}\), \(\nu_2(d(x)-1)=3\nu_2(x)\), where \(d(x)=\sum_{k\ge0}2^k\binom{x}{k}^2\).

## Assumptions and scope
The ring \(\mathbb Z_2\) consists of 2-adic integers; \(\nu_2\) is normalized by \(\nu_2(2)=1\) and \(\nu_2(0)=+\infty\). Binomial polynomials \(\binom{x}{k}\) take integral values on \(\mathbb Z_2\). Consequently \(d(x)\) converges uniformly on \(\mathbb Z_2\) and agrees with \(D_n\) for nonnegative integers. No assertion concerns \(\nu_2(d(0)-1)\), which is infinite. The only finite computation in the proof is exact expansion of two fixed rational polynomials (the heights 2 and 3); the arbitrary-height argument is symbolic.

## Proof
**1. An exact 2-adic cancellation.** In the formal rational power series ring, the dilogarithm identity
\[
\operatorname{Li}_2(z)+\operatorname{Li}_2\left(\frac{z}{z-1}\right)=-\frac12\log^2(1-z)
\]
is proved by differentiating both sides (each has zero constant coefficient). At \(z=2\) both dilogarithms converge in \(\mathbb Q_2\), and \(\log(-1)=0\) because \(-1\) has order two. Hence
\[
L=\sum_{k\ge1}\frac{2^k}{k^2}=0.
\]
Put \(H_j=\sum_{i=1}^{j}1/i\), \(H_0=0\), and
\[
A=-2\sum_{k\ge1}\frac{2^k H_{k-1}}{k^2}.
\]
Then \(A\) is a 2-adic unit. Indeed, \(\nu_2(H_{k-1})\ge-\lfloor\log_2(k-1)\rfloor\) for \(k\ge2\), and the individual summands have lower valuation \(1+k-2\nu_2(k)-\lfloor\log_2(k-1)\rfloor\). Only the \(k=4\) term can have valuation zero: it is \(-11/3\); the \(k=1\) term vanishes, and every other term is even. For \(k\ge16\) this follows from \(k\ge4\lfloor\log_2k\rfloor\), and the cases \(2\le k\le15\) are direct. Thus \(A\equiv1\pmod2\).

**2. Uniform large-height expansion.** Let \(x=2^hu\) with \(h\ge4\) and \(u\in\mathbb Z_2^\times\). Define \(Q_k(x)=\prod_{j=1}^{k-1}(1-x/j)^2\) (empty product 1). The exact identity
\[
 d(x)-1=x^2\sum_{k\ge1}\frac{2^k}{k^2}Q_k(x)
\]
follows from \(\binom{x}{k}=(-1)^{k-1}(x/k)\prod_{j=1}^{k-1}(1-x/j)\). Set \(K=4h\). If \(2\le k\le K\), put \(a_k=\lfloor\log_2(k-1)\rfloor\). Since \(K\le2^h\), each \(x/j\) in this product has 2-adic valuation at least \(h-a_k\ge1\). Expanding the finite product gives
\[
Q_k(x)=1-2xH_{k-1}+E_k(x),\qquad \nu_2(E_k(x))\ge2(h-a_k).
\]
For all \(k\ge2\),
\[
k-2\nu_2(k)-2a_k\ge-2.
\]
This follows by direct inspection for \(2\le k\le15\), and for \(k\ge16\) by \(k\ge4\lfloor\log_2 k\rfloor\). Therefore the contribution of \(E_k\) to \(d(x)-1\) has valuation at least \(4h-2\ge3h+1\). For \(k>K\), the original terms \(2^k\binom{x}{k}^2\) have valuation at least \(k>4h\), while the omitted tails of \(x^2L\) and \(Ax^3\) also have valuations at least \(3h+1\) by the displayed elementary bounds. Consequently,
\[
d(x)-1\equiv x^2L+Ax^3=Ax^3\pmod{2^{3h+1}}.
\]
The coefficient \(A\) is odd, so \(\nu_2(d(x)-1)=3h\).

**3. Heights two and three.** Set \(P_K(x)=\sum_{k=0}^{K}2^k\binom{x}{k}^2\). For \(x=4u\) and odd \(u\in\mathbb Z_2\), the terms \(k=5,6\) are divisible by \(2^7\), because their binomial coefficients are even, while the terms \(k\ge7\) are divisible by \(2^7\). Thus \(d(4u)\equiv P_4(4u)\pmod{128}\). Exact rational-polynomial expansion proves
\[
\frac{P_4(4u)-1}{64}=\frac{u^2}{9}(256u^6-768u^5+1056u^4-768u^3+333u^2-75u+11).
\]
For odd \(u\), the right-hand side is odd. Likewise for \(x=8u\), \(\binom{8u}{9}\) is even and \(k\ge10\) terms vanish modulo \(2^{10}\), so \(d(8u)\equiv P_8(8u)\pmod{1024}\). An exact expansion over \(\mathbb Q[u]\) shows that every coefficient of \((P_8(8u)-1)/512\) has odd denominator (dividing \(99225\)), and modulo two the resulting polynomial is \(u^3\); see the standalone coefficient-reconstruction verifier. Hence this quotient is odd for odd \(u\), establishing valuations 6 and 9 respectively. These are algebraic identities in one indeterminate, not sample calculations.

**4. Reflection and odd indices.** For any nonnegative integer \(n\), the classical rational generating-function identity
\[
\sum_{k\ge0}\binom{n+k}{k}^2z^k=(1-z)^{-2n-1}\sum_{j=0}^{n}\binom nj^2z^j
\]
follows by Euler's hypergeometric transformation (alternatively, compare coefficients via Vandermonde's identity). Both sides converge in \(\mathbb Q_2\) at \(z=2\); as \((1-2)^{-2n-1}=-1\), the identity yields \(d(-n-1)=-d(n)\). Nonnegative integers are dense in \(\mathbb Z_2\), so continuity yields \(d(-x-1)=-d(x)\) for all \(x\in\mathbb Z_2\). If \(n\equiv3\pmod4\), the number \(-n-1\) has valuation \(h=\nu_2(n+1)\ge2\); applying the first half gives \(\nu_2(D_n+1)=3h\). The first half for \(n\equiv0\pmod4\) is immediate. This proves both asserted statements and Lengyel's three conjectures.

## Verification
Run `python3 artifacts/verify.py` with the Python standard library. It constructs and compares every rational coefficient in the two small-height polynomial identities, verifies the parity of their normalized coefficients, tests the elementary valuation inequality through 100,000, checks the convergent 2-adic constants modulo \(2^{24}\), independently enumerates 1,399 Delannoy recurrence values, and checks the reflection relation modulo \(2^{18}\) for 26 sample arguments. Actual output is embedded in `artifacts/verification_output.txt`. The infinite conclusions depend on the proof rather than these finite checks.

## Relationship to prior work
Guo and Zeng (2010, arXiv:1008.2894, first posted 2010-08-17) studied arithmetic congruences for the central Delannoy numbers, which supplies the archival object and primary number-theory classification. Lengyel (2021, INTEGERS 21, A86, pages 4–5) established a lower bound \(\nu_2(d(2^ha)-1)\ge2h+2\) and explicitly proposed the three exact-valuation conjectures proved here. His paper also proved the complementary small-height statements. The present proof supplies a cubic leading term in the 2-adic interpolation and converts the negative-index symmetry to the positive odd-index valuation. The 2025 work on \(p\)-adic values of Legendre polynomials studies \(\nu_p(P_n(p))\), which in the Delannoy specialization involves \(p=3\) and the values themselves, not the two-adic distances to \(\pm1\). A previously recorded periodicity result gives at most a linear-in-height divisibility modulus for \(D_{n+2^h}-D_n\) and does not imply this sharp cubic valuation. There remains a risk of another unpublished, obscure, or unindexed resolution of Lengyel's conjectures; neither a search nor a self-review certifies global priority.

## Limitations
The formulas concern the two 2-adic neighborhoods \(n\equiv0\pmod4\) and \(n\equiv3\pmod4\), and do not determine every difference \(D_m-D_n\), arbitrary odd primes, or the leading coefficient beyond its parity. The claimed infinite valuations rest on the displayed proof and exact finite polynomial computations; the computational sample checks alone are not proofs. Coverage of unindexed literature is incomplete; scientific priority is provisional.

## References
1. V. J. W. Guo and J. Zeng, *New congruences for sums involving Apéry numbers or central Delannoy numbers*, arXiv:1008.2894 (initial submission 2010-08-17). https://arxiv.org/abs/1008.2894
2. T. Lengyel, *On Some p-Adic Properties and Supercongruences of Delannoy and Schröder Numbers*, INTEGERS **21** (2021), #A86, Conjectures 1–3. https://math.colgate.edu/~integers/v86/v86.pdf
3. *On the p-adic valuations of values of Legendre polynomials*, arXiv:2505.08935 (2025), for comparison of the different prime-adic valuation problems. https://arxiv.org/abs/2505.08935
