# Uniform prime-power valuations across a binomial gcd family

## Finding
For an integer \(k\ge 2\), define
\[
D(k)=\gcd_{2\le q\le k+1}\binom{qk}{k}.
\]
For every prime \(p\) and every integer \(a\ge1\) with \(N=p^a\ge3\), set \(k=N-1\). **Every member** of this family has the same exact valuation:
\[
\nu_p\left(\binom{q(N-1)}{N-1}\right)=a\qquad(2\le q\le N).
\]
As a consequence the full integer gcd, not merely its prime support, is
\[
\boxed{D(p^a-1)=p^a.}
\]
The uniform valuation assertion is stronger than the gcd formula: it shows no choice of multiplier in the entire defining interval changes the \(p\)-adic order.

## Assumptions and scope
Here \(\nu_p(M)\) is the exponent of prime \(p\) in the positive integer \(M\). The index \(N=p^a\) is an exact prime power with \(N\ge3\), and \(q\) ranges over **all integers** from \(2\) through \(N\), inclusive. The claim concerns this prime-power subfamily; it does not assert a formula for composite \(k+1\) with multiple distinct prime factors.

## Proof
**Step 1: a digit-sum identity.** Write \(s_p(t)\) for the sum of base-\(p\) digits of a nonnegative integer \(t\), with \(s_p(0)=0\). Since \(N=p^a\), for any \(0\le t<N\), subtraction from the \(a\)-digit number \(N-1\), all of whose digits equal \(p-1\), gives
\[
s_p(N-1-t)=a(p-1)-s_p(t).
\]
For every \(2\le q\le N\), the exact base-\(N\) decompositions are
\[
(q-1)(N-1)=(q-2)N+(N-q+1),
\]
\[
q(N-1)=(q-1)N+(N-q).
\]
Both right-hand remainders lie in \([0,N-1]\), so the high and low blocks occupy disjoint groups of \(a\) base-\(p\) digits. Hence, applying the preceding complement rule with \(t=q-2\) and \(t=q-1\), respectively,
\[
\begin{aligned}
s_p((q-1)(N-1))&=s_p(q-2)+s_p(N-q+1)=a(p-1),\\
s_p(q(N-1))&=s_p(q-1)+s_p(N-q)=a(p-1).
\end{aligned}
\]
Also \(s_p(N-1)=a(p-1)\). Legendre's factorial valuation identity now yields
\[
\begin{aligned}
\nu_p\binom{q(N-1)}{N-1}
&=\frac{s_p(N-1)+s_p((q-1)(N-1))-s_p(q(N-1))}{p-1}\\
&=a.
\end{aligned}
\]
This argument includes both endpoints \(q=2\) and \(q=N\), with no asymptotic or computational assumptions.

**Step 2: no other prime enters the gcd.** We reproduce the relevant finite-difference argument for completeness. Fix \(k\ge1\), and suppose a prime \(\ell\) divides each \(\binom{qk}{k}\), for \(2\le q\le k+1\). Consider the degree-\(k\) polynomial \(F(X)=\binom{kX}{k}\). At integer inputs it is integer-valued and has \(F(0)=0\), \(F(1)=1\), and \(F(2),\ldots,F(k+1)\equiv0\pmod\ell\). The integer forward differences at \(1\) therefore satisfy
\[
\Delta^rF(1)\equiv(-1)^r\pmod\ell\qquad(0\le r\le k).
\]
By Newton's forward-difference identity evaluated at zero,
\[
0=F(0)=\sum_{r=0}^{k}\binom{-1}{r}\Delta^r F(1)\equiv k+1\pmod\ell,
\]
because \(\binom{-1}{r}=(-1)^r\). Thus every prime divisor of \(D(k)\) divides \(k+1\). This is also Lemma 4 of Guo–Qiu–Cao–Feng–Gao.

Apply this lemma with \(k=N-1\) and \(N=p^a\): the only possible prime factor of the gcd is \(p\). Step 1 says its valuation in **every** gcd term is exactly \(a\), so the gcd itself is precisely \(p^a\). \(\square\)

## Verification
The included `verify.py` independently computes valuations using factorial valuations and base-\(p\) digit sums, and for small prime powers also uses direct integer binomial coefficients and their gcd. Run `python3 verify.py` in the directory containing the extracted files. This finite verification tests instances but is not needed to establish the infinite theorem, which follows from the two proofs above.

## Relationship to prior work
Guo, Qiu, Cao, Feng, and Gao (2026) proved an exact criterion for \(D(k)=1\) and described which primes may divide it. Their theorem does not state the magnitude of \(D(k)\) in the prime-power subfamily or a valuation uniform across all defining multipliers. The present proof uses their prime-support lemma (also independently supplied above) and adds an all-multiplier digit-sum identity.

Hong (2016) gives a formula for a different binomial gcd: the upper argument is fixed while the lower argument ranges over indices coprime to a specified integer. Neither its theorem nor the classical gcd of an entire Pascal row has the defining index family here. OEIS A080170 records the **unit-gcd predicate** rather than the full gcd value.

## Limitations
This is a precise prime-power-index result, not a full formula for all integers \(k\). It does not show an analogous uniform valuation for composite \(k+1\) with more than one prime divisor. Although the named source papers and a mathematical research-record index were checked, an earlier implicit or unindexed formulation of this simple digit-sum identity remains a genuine originality risk. A separate independent audit has not been performed.

## References
- D. Guo, R. Qiu, Y. Cao, R. Feng, X.-S. Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1 (first posted 22 June 2026). https://arxiv.org/html/2606.22997
- S. Hong, *The greatest common divisor of certain binomial coefficients*, C. R. Math. Acad. Sci. Paris 354 (2016), 756–761. https://doi.org/10.1016/j.crma.2016.06.001
- OEIS A080170, indices with unit gcd in the family. https://oeis.org/A080170
- Legendre's factorial valuation formula and Newton's forward-difference interpolation formula (standard identities).
