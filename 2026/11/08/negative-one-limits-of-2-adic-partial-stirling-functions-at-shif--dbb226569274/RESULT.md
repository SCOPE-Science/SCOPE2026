# Negative-one limits of 2-adic partial Stirling functions at shifted dyadic indices

## Finding
For every fixed pair of integers \(a\ge1\), \(\Delta\ge0\), define
\[
P_n(-1)=\frac1{n!}\sum_{\substack{1\le j\le n\\j\text{ odd}}}\binom nj\frac1j\quad(n\ge1),\qquad P_0(-1)=0.
\]
Write \(s_2(a)\) for binary digit sum and \(U(N!)=N!/2^{\nu_2(N!)}\) for the odd part of a factorial. Then
\[
U_a:=\lim_{e\to\infty}U((a2^e)!)\in\mathbb Z_2^\times
\]
exists, and the exact \(2\)-adic limit is
\[
\boxed{\lim_{e\to\infty}P_{a2^e+\Delta}(-1)=\frac{2^{s_2(a)}}{U_a}P_\Delta(-1).}
\]
For \(\Delta\ge1\) the limit is nonzero; for \(\Delta=0\) it is zero. In the first nontrivial case,
\[
\lim_{e\to\infty}P_{2^e+1}(-1)=\frac2{U_1}.
\]

## Assumptions and scope
All limits are in the field \(\mathbb Q_2\), and the stated values are in \(\mathbb Z_2\). The integers \(a\) and \(\Delta\) are fixed before \(e\to\infty\); no rate uniform in these two parameters is claimed. The definition agrees with the partial Stirling function of Davis at its integer input \(-1\). For \(n=0\) the empty sum is zero. A nonzero rational number is also nonzero in \(\mathbb Q_2\).

## Proof
**1. Exact binomial-harmonic transformation.** For each \(n\ge0\), put \(S_n=\sum_{j=1}^n2^{j-1}/j\), with \(S_0=0\). Two elementary integrals give
\[
\sum_{j=1}^n\frac1j\binom nj
=\int_0^1\frac{(1+t)^n-1}t\,dt
=\sum_{k=1}^n\frac{2^k-1}k
\]
and
\[
\sum_{j=1}^n\frac{(-1)^{j-1}}j\binom nj
=\int_0^1\frac{1-(1-t)^n}t\,dt
=\sum_{k=1}^n\frac1k.
\]
Taking half the sum isolates odd \(j\). Therefore the exact rational identity
\[
\boxed{n!P_n(-1)=\sum_{\substack{1\le j\le n\\j\text{ odd}}}\binom nj\frac1j=S_n}
\]
holds for every \(n\ge0\).

**2. The vanishing dyadic logarithm and its tail.** The series \(\sum_{j\ge1}2^{j-1}/j\) converges in \(\mathbb Q_2\), because \(j-1-\nu_2(j)\to\infty\). By the convergent power series for the \(2\)-adic logarithm,
\[
\sum_{j\ge1}\frac{2^{j-1}}j=-\frac12\log(1-2)=-\frac12\log(-1)=0.
\]
The last equality uses \(\log((-1)^2)=2\log(-1)=0\). Hence, with
\[
R(N):=\sum_{r\ge1}\frac{2^{r-1}}{N+r},
\]
for every integer \(N\ge0\) we have
\[
S_N=-\sum_{j>N}\frac{2^{j-1}}j=-2^N R(N),
\qquad R(\Delta)=-2^{-\Delta}S_\Delta.
\]

**3. Factorial-unit convergence.** For \(m\ge1\), the exact identity
\[
U((2m)!)=U(m!)\prod_{j=1}^m(2j-1)
\]
holds. Set \(m=a2^{e-1}\). For each fixed modulus \(2^K\), once \(e\) is large, the odd factors \(2j-1\) form a whole number of complete residue cycles through the units modulo \(2^K\). Their product is \(1\pmod{2^K}\): for \(K\ge3\), the full product of units modulo \(2^K\) equals one (pair inverses and multiply the four self-inverse units); for \(K=1,2\), sufficiently many repeats also give one. Consequently \(U((a2^e)!)\) is Cauchy and tends to an odd unit \(U_a\). If \(0\le\Delta<2^e\), then \(\nu_2(a2^e+i)=\nu_2(i)\) for each \(1\le i\le\Delta\), and
\[
U((a2^e+\Delta)!)\longrightarrow U_a U(\Delta!).
\]

**4. The tail is continuous along the indices in question.** Set \(N_e=a2^e+\Delta\). For each fixed \(r\ge1\), \(1/(N_e+r)\to1/(\Delta+r)\). To justify passage of the limit through the infinite series, assume \(2^e>\Delta\). If \(r+\Delta<2^e\), then \(\nu_2(N_e+r)=\nu_2(r+\Delta)\). Otherwise \(N_e+r\le(a+1)(r+\Delta)\). In both cases,
\[
\nu_2\!\left(\frac{2^{r-1}}{N_e+r}\right)
\ge r-1-\log_2((a+1)(r+\Delta)),
\]
which tends to infinity with \(r\), uniformly in \(e\). Thus the tails are uniformly \(2\)-adically small and
\[
R(N_e)\longrightarrow R(\Delta)=-2^{-\Delta}S_\Delta.
\]

**5. Assemble the limit.** For large \(e\), binary supports do not overlap, so \(s_2(N_e)=s_2(a)+s_2(\Delta)\). Legendre's factorial-valuation identity gives \(\nu_2(N_e!)=N_e-s_2(N_e)\). By the identities above,
\[
P_{N_e}(-1)=-\frac{2^{N_e}}{N_e!}R(N_e)
=-\frac{2^{s_2(a)+s_2(\Delta)}}{U(N_e!)}R(N_e).
\]
Taking the limit and using \(\Delta!=2^{\Delta-s_2(\Delta)}U(\Delta!)\) yields
\[
\begin{aligned}
\lim_{e\to\infty}P_{N_e}(-1)
&=\frac{2^{s_2(a)+s_2(\Delta)-\Delta}S_\Delta}{U_aU(\Delta!)}\\
&=\frac{2^{s_2(a)}}{U_a}\frac{S_\Delta}{\Delta!}
=\frac{2^{s_2(a)}}{U_a}P_\Delta(-1).
\end{aligned}
\]
For \(\Delta\ge1\), the rational sum \(S_\Delta\) is strictly positive as an ordinary rational, hence not zero in \(\mathbb Q_2\), and the claimed nonvanishing follows. For \(\Delta=0\), both sides are zero. This proves the theorem.

## Verification
The standard-library Python program `verify.py` checks the exact rational binomial-harmonic identity for \(1\le n\le30\), compares direct exact fractions with independent modular computations for \(0\le n\le26\), computes dyadic factorial units through high levels, and checks \(96\) sample approximants for \(a\in\{1,2,3,5\}\), \(0\le\Delta\le5\), and \(4\le e\le7\), at \(13\)-bit precision. Run `python3 verify.py`. The program is finite corroboration only; Steps 1–5 above establish the infinite statement.

## Relationship to prior work
Davis defined and investigated the \(2\)-adic partial Stirling functions. In *2-adic partial Stirling functions and their zeros* (2014), Theorem 2.6 and equation (2.8) establish the limiting formula for **nonnegative** integer inputs \(x\), and Conjecture 2.13 concerns eventual-periodic \(2\)-adic inputs. The negative integer \(-1\) is not covered by Theorem 2.6. The present identity handles \(x=-1\), every fixed shift \(\Delta\ge0\), and every fixed multiplier \(a\ge1\), with an explicit expression in terms of \(P_\Delta(-1)\) and a factorial unit.

Davis's *Binomial coefficients involving infinite powers of primes* (2013) provides the factorial-unit limits and related binomial limits; those facts are foundational rather than independently claimed. The distinctive additional ingredient is the exact odd-binomial harmonic identity followed by the cancellation \(\log(-1)=0\), which makes the weighted partial-Stirling limit computable. A direct substitution \(x=-1\) into the nonnegative-input formula is not justified. The result supplies a concrete all-shift negative-input case of the previously posed convergence problem; it does not settle the general eventual-periodic conjecture.

## Limitations
Only the fixed input \(x=-1\) is treated. No conclusion is asserted for all negative integers or arbitrary rational \(2\)-adic inputs, no joint limit in \(a\) or \(\Delta\) is claimed, and no uniform quantitative error term is proved. The originality comparison is based on the cited primary texts and targeted searches; broader historical coverage is possible.

## References
1. D. M. Davis, *Binomial coefficients involving infinite powers of primes*, arXiv:1301.6285v1 (public 2013-01-26), Theorem 1.1 and Corollary 1.2, https://arxiv.org/abs/1301.6285.
2. D. M. Davis, *2-adic partial Stirling functions and their zeros*, arXiv:1402.0433v1 (public 2014-02-03), especially Theorem 2.6, equation (2.8), Conjecture 2.13, and Section 5, https://arxiv.org/abs/1402.0433.

