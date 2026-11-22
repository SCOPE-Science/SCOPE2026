# Exact adjacent central-binomial valuation law and its covariance sign transition

## Finding
For each odd prime \(p\), positive integer \(k\), and \(0\le n<p^k\), write
\[
B_n=\binom{2n}{n},\qquad X_n=\nu_p(B_n),\qquad Y_n=\nu_p(B_{n+1}).
\]
Here the endpoint value \(\nu_p(B_{p^k})=0\), so the pair sequence is cyclic at its boundary. Let \(m=(p-1)/2\). Its complete two-variable counting polynomial is
\[
F_{p,k}(u,v)=\sum_{n=0}^{p^k-1}u^{X_n}v^{Y_n}
=(1,0,0,0,0)M_p(u,v)^k\begin{pmatrix}1\\1\\1\\1\\1\end{pmatrix},
\]
where
\[
M_p(u,v)=\begin{pmatrix}
0&u&m&v&(m-1)uv\\
0&u&m&0&muv\\
0&0&m+1&0&muv\\
0&0&m&v&muv\\
0&0&m&0&(m+1)uv
\end{pmatrix}.
\]
In particular every joint multiplicity is the coefficient \([u^a v^b]F_{p,k}(u,v)\), for all integers \(a,b\ge0\).

For uniformly chosen \(n\) from the same range, put \(\Delta=Y_n-X_n\). Its **exact finite-depth signed jump law** is
\[
\Pr(\Delta=0)=1-\frac2p,\qquad
\Pr(\Delta=j)=\Pr(\Delta=-j)=
\begin{cases}
(p-1)p^{-j-1}&1\le j<k,\\
p^{-k}&j=k,
\end{cases}
\]
and all other values are impossible. Equivalently \(\Pr(|\Delta|\ge j)=2p^{-j}\) for \(1\le j\le k\).

Writing \(\mu_{p,k}=\mathbb EX_n\), \(W_{p,k}=\operatorname{Var}(X_n)\), and \(K_{p,k}=\operatorname{Cov}(X_n,Y_n)\), their exact finite-depth values are
\[
\mu_{p,k}=\frac{k}{2}-\frac{1-p^{-k}}{2(p-1)},
\]
\[
W_{p,k}=\frac{(p+1)k}{4(p-1)}-\frac{2p+1}{4(p-1)^2}
+\frac{2(p+1)p^{-k}-p^{-2k}}{4(p-1)^2},
\]
\[
\boxed{K_{p,k}=W_{p,k}-\sum_{j=1}^{k}(2j-1)p^{-j}.}
\]
The exact **covariance sign phase** is
\[
K_{p,k}<0\ \Longleftrightarrow\ (p,k)\in\{(3,1),(3,2)\};
\qquad K_{p,k}>0\quad\text{otherwise}.
\]
Moreover \(K_{p,k}\) is strictly increasing in \(k\) for each fixed odd prime. For fixed \(p\) and \(k\to\infty\), the Pearson correlation satisfies
\[
\operatorname{Corr}(X_n,Y_n)
=1-\frac{4}{(p-1)k}+O_p(k^{-2}).
\]

## Assumptions and scope
The prime \(p\ge3\) is odd and \(k\ge1\) is integral; all sampling is uniform on the complete finite block \(\{0,\ldots,p^k-1\}\). The valuation \(\nu_p\) counts the exponent of \(p\) in a positive integer. The polynomial \(F_{p,k}\) has nonnegative integer coefficients and is interpreted in \(\mathbb Z[u,v]\). The displayed finite matrix gives an exact joint distribution, not a limiting approximation. The central binomial coefficient at \(n=0\) equals one.

## Proof
**1. Five-state joint transfer.** Write the base-\(p\) digits of \(n\) from least to most significant. Track three binary carries: \(c\) in doubling \(n\), \(e\) in adding one to \(n\), and \(d\) in doubling \(n+1\). Initially \((c,e,d)=(0,1,0)\). If the current digit of \(n\) is \(a\in\{0,\ldots,p-1\}\), the corresponding digit of \(n+1\) is \(b=(a+e)\bmod p\), and the next state is
\[
(c',e',d')=\left(\left\lfloor\frac{2a+c}{p}\right\rfloor,
\left\lfloor\frac{a+e}{p}\right\rfloor,
\left\lfloor\frac{2b+d}{p}\right\rfloor\right).
\]
The digit contributes the weight \(u^{c'}v^{d'}\). The only states reachable from the initial triple are
\[
A=(0,1,0),\quad B=(1,1,0),\quad C=(0,0,0),\quad
D=(0,0,1),\quad E=(1,0,1).
\]
Put \(p=2m+1\). Directly splitting the digit range at \(m-1,m,m+1,2m\), one gets the following weighted transitions: from \(A\), to \(B,C,D,E\) with weights \(u,m,v,(m-1)uv\); from \(B\), to \(B,C,E\) with weights \(u,m,muv\); from \(C\), to \(C,E\) with weights \(m+1,muv\); from \(D\), to \(C,D,E\) with weights \(m,v,muv\); and from \(E\), to \(C,E\) with weights \(m,(m+1)uv\). These are precisely the entries of \(M_p\). Kummer's theorem counts the outgoing doubling carries to give \(X_n\) and \(Y_n\). After exactly \(k\) digits, any possible remaining digit of \(n+1\) is \(1\), whose double \(2\) is strictly less than \(p\), so no additional doubling carry is produced. Therefore there is no terminal weight correction. Summing over all five final states proves the matrix identity at every \(k\), including \(k=1\).

**2. Exact signed differences.** The binomial recurrence yields
\[
\frac{B_{n+1}}{B_n}=\frac{2(2n+1)}{n+1},\qquad
\Delta=\nu_p(2n+1)-\nu_p(n+1).
\]
The integers \(2n+1\) and \(n+1\) are coprime, since their integer linear combination \((2n+1)-2(n+1)=-1\). For each \(1\le j<k\), the unique root of \(2n+1\equiv0\pmod{p^j}\) has exactly \((p-1)p^{k-j-1}\) representatives modulo \(p^k\) of valuation exactly \(j\); the same count holds for \(n+1\). These two sets are disjoint. At the top level there is exactly one positive root \(n=(p^k-1)/2\) of valuation \(k\), and one negative root \(n=p^k-1\). No zero-valuation overflow occurs at these roots because \(2n+1\le2p^k-1\) and \(n+1\le p^k\), and \(p\) is odd. The remaining \((p-2)p^{k-1}\) indices give \(\Delta=0\), proving every count and its geometric tail.

**3. The marginal moments from Kummer carries.** Write \(c_i\) for the outgoing carry in position \(i-1\) when doubling \(n\), with \(c_0=0\). Kummer's theorem gives \(X_n=\sum_{i=1}^k c_i\). Because the \(k\) base-\(p\) digits of uniformly sampled \(n\) are independent, for \(i\ge1\),
\[
\mathbb E(c_i)=\frac{1-p^{-i}}2,\qquad
\operatorname{Var}(c_i)=\frac{1-p^{-2i}}4,
\]
and for \(1\le i<j\),
\[
\operatorname{Cov}(c_i,c_j)=p^{-(j-i)}\frac{1-p^{-2i}}4.
\]
Indeed \(\Pr(c_i=1\mid c_{i-1}=0)=(p-1)/(2p)\) and \(\Pr(c_i=1\mid c_{i-1}=1)=(p+1)/(2p)\), so the conditional expectation contracts the centered state by \(1/p\) at each step. Summing the means proves \(\mu_{p,k}\). Summing variances and covariances, or adding the \(k\)th carry one at a time, gives
\[
W_{p,0}=0,\qquad W_{p,k}-W_{p,k-1}=
\frac{p+1}{4(p-1)}(1-p^{-k})^2.
\]
Summing this geometric expression for \(k\ge1\) gives exactly the displayed closed variance formula.

**4. Covariance and sign phase.** For every integer \(d\), \(d^2=\sum_{j=1}^{|d|}(2j-1)\), so the jump tails from Step 2 give
\[
\mathbb E(\Delta^2)=2\sum_{j=1}^k(2j-1)p^{-j}.
\]
Since \(B_{p^k}\) is prime-to-\(p\) by Kummer (doubling \(p^k\) creates no carry for odd \(p\)), the shift \(n\mapsto n+1\) cyclically permutes the valuation values on the finite block. Hence \(X_n,Y_n\) have identical means and variances, and
\(\mathbb E(\Delta^2)=2(W_{p,k}-K_{p,k})\). This proves the covariance identity.

For \(k\ge1\), the recurrence for variance gives
\[
K_{p,k+1}-K_{p,k}=
\frac{p+1}{4(p-1)}(1-p^{-(k+1)})^2-(2k+1)p^{-(k+1)}>0.
\]
For \(p=3\), the first summand is at least \(32/81\) and the subtracted term is at most \(1/3\). For \(p\ge5\), they are respectively at least \(144/625\) and at most \(3/25\). The upper bounds hold for every \(k\ge1\), because \((2k+1)p^{-(k+1)}\) decreases in \(k\). At the first depth,
\[
K_{p,1}=\frac{p^2-4p-1}{4p^2},
\]
negative precisely at \(p=3\) among odd primes. Direct exact substitutions give \(K_{3,2}=-4/81\) and \(K_{3,3}=167/729\). Strict monotonicity now proves the complete sign classification.

Finally, \(W_{p,k}=(p+1)k/(4(p-1))+O_p(1)\), whereas \(\sum_{j=1}^k(2j-1)p^{-j}=(p+1)/(p-1)^2+O_p(kp^{-k})\). Dividing their difference by \(W_{p,k}>0\) establishes the correlation expansion.

## Verification
The standalone `verify_adjacent.py` independently computes each valuation by exact integer binomial coefficients and by the base-\(p\) doubling carry process. It compares all coefficients of the five-state joint polynomial, each signed jump multiplicity, the exact means, variances, covariances, and the predicted sign phase for 19 prime-depth pairs at six primes through 17, totaling 2,891 individual integer indices. The checker uses only Python standard-library integer and rational arithmetic. It reports:

```
PASS: 19 (prime, exponent) cases; 2891 individual indices
PASS: independent binomial-integer and Kummer-carry valuations
PASS: five-state full joint counts, exact signed differences, means, variances, covariances, and signs
```

These finite tests corroborate but do not prove the unrestricted statements: the proof is Steps 1–4, which apply to every odd prime and every positive depth.

## Relationship to prior work
Kummer's classical theorem and Straub–Moll–Amdeberhan's 2008 treatment of central-binomial prime valuations supply the known carry mechanism and coefficient recurrence; neither is a new claim here. Ford–Konyagin (first posted 9 September 2019) study asymptotic divisibility of \(B_n\) by powers of its index and their greatest common divisor; these are one-index arithmetic questions rather than adjacent valuation-pair frequencies. A 2026 publicly posted calculation of the marginal carry-count distribution supplies the one-index generating polynomial but does not determine the ordered joint polynomial or the covariance sign transition. Related published exact joint carry results concern different coefficients \(\binom{3n}{n}\), or the prime two, and so do not specialize to this odd-prime, adjacent-index pair. Another modern result determines possible central-binomial residue values under fixed index suffixes, not the paired valuations at consecutive indices. The five-state joint count and sharp adjacent covariance phase are the present additions.

## Limitations
The theorem is restricted to odd primes, adjacent indices, and complete prime-power blocks. There is no assertion for prime two, arbitrary non-unit shifts, or arbitrary incomplete intervals. While the inspected literature did not state the exact five-state adjacent law, a mathematically equivalent transfer computation may exist in broader digital-function literature; absence from inspected sources is not a proof of universal priority. The signed jump distribution is an elementary consequence of the known coefficient recurrence; the principal new synthesis is the exact bivariate law and the complete covariance phase.

## References
1. K. Ford and S. Konyagin, *Divisibility of the central binomial coefficient*, first preprint 9 September 2019, arXiv:1909.03903, https://arxiv.org/abs/1909.03903.
2. A. Straub, V. H. Moll, and T. Amdeberhan, *The \(p\)-adic valuation of \(k\)-central binomial coefficients*, first posted 13 November 2008, arXiv:0811.2028, https://arxiv.org/abs/0811.2028.
3. S. M. N. Sakib, *Carry–Run Theorem and Sakib Index for the Exact Distribution of \(\nu_p\binom{2n}{n}\) over \(n\bmod p^k\)*, 23 January 2026, doi:10.33774/coe-2026-1w9zm; not peer-reviewed at posting.
4. *The full odd-prime p-adic index–value closure of central binomial coefficients*, publicly archived research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-full-odd-prime-p-adic-index-value-closure-of-central-binomia--c0f80e993a75.
5. *Joint ternary valuations of central and threefold binomial coefficients*, publicly archived research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-joint-ternary-valuations-of-central-and-threefold-binomial-coeff--1999135510ae.
6. G. Barat and P. J. Grabner, *Distribution of binomial coefficients and digital functions*, J. London Math. Soc. **64** (2001), 523–547, doi:10.1112/S0024610701002630.
