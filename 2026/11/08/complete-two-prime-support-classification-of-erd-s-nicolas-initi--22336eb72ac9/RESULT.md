# Complete two-prime-support classification of Erdős–Nicolas initial-divisor sums

## Finding
For a positive integer \(n\), enumerate its positive divisors as \(1=d_1<\cdots<d_{\tau(n)}=n\). Call \(n\) an *initial-divisor-sum number* if \(\sum_{i=1}^{j}d_i=n\) for some \(j<\tau(n)\). Call it an *Erdős–Nicolas number* if in addition \(j<\tau(n)-1\), hence the equality does not merely sum all proper divisors.

**Theorem.** For every integer \(a,b\ge1\) and every odd prime \(p\), \(n=2^a p^b\) is an initial-divisor-sum number precisely in the following mutually exclusive cases:

1. \(a=3\), \(b=1\), \(p=3\), giving \(n=24\) and the equality \(1+2+3+4+6+8=24\);
2. \(b=1\) and \(p=2^{a+1}-1\) is prime, giving an even perfect number, for which the prefix consists of all proper divisors.

In particular, \(24\) is the **only** Erdős–Nicolas number of the form \(2^a p^b\) with exactly two distinct prime divisors, one of them \(2\). The theorem rules out *every* odd-prime exponent \(b\ge2\), without a bound on \(a,b\) or \(p\).

## Assumptions and scope
All divisors and sums are over positive integers. The letter \(p\) ranges over odd primes and \(a,b\) over strictly positive integers; the theorem does not address odd integers or even integers with three or more distinct prime divisors. Define \(T_n(x)=\sum_{d\mid n,\ d\le x}d\). This is a nondecreasing step function on \(0\le x<n\), whose jumps are at the proper divisors. The largest proper divisor of \(n\) is \(n/2\).

## Proof
Put \(A=2^a\) and \(n=Ap^b\).

**Case 1: \(p\ge5\), \(b\ge2\).** The sum over all divisors with \(p\)-exponent below \(b\) is
\[
S_{<b}=(2A-1)\frac{p^b-1}{p-1}<\frac{2Ap^b}{p-1}\le\frac n2.
\]
For \(x<n/2\), any included divisor of the form \(2^i p^b\) has \(i\le a-2\); hence their total is at most \((2^{a-1}-1)p^b<n/2\). (For \(a=1\) this sum is empty.) Therefore \(T_n(x)<n\) for all \(x<n/2\). The only possible remaining prefix ends at \(n/2\); its sum is
\[
T_n(n/2)=S_{<b}+(A-1)p^b.
\]
Equality to \(n\) would force
\[
2A-1=(p-1)\frac{p^b}{p^b-1}=(p-1)+\frac{p-1}{p^b-1},
\]
which lies strictly between the successive integers \(p-1\) and \(p\), impossible. Thus there are no such numbers.

**Case 2: \(p\ge5\), \(b=1\).** For \(x<A\), each of the two divisor blocks \(1,2,\ldots,2^a\) and \(p,2p,\ldots,2^a p\), if touched, contributes less than \(2x\); thus \(T_n(x)<4x<4A\le Ap=n\). For \(A\le x<n/2\), all pure powers of two have appeared, and the \(p\)-block contributes at most \(p(2^{a-1}-1)\); consequently
\[
T_n(x)\le(2A-1)+p(A/2-1)<Ap,
\]
since \(p(A/2+1)-2A+1>0\) for \(p\ge5\). At \(n/2\), the sum of all proper divisors is
\[
T_n(n/2)=(2A-1)+p(A-1),
\]
which equals \(Ap\) precisely if \(p=2A-1=2^{a+1}-1\). These are exactly the classical even perfect numbers in the family.

**Case 3: \(p=3\), \(b\ge2\).** We exhibit two *consecutive proper divisors* \(u<v\) with \(T_n(u)<n<T_n(v)\). There can be no equality at any prefix. The consecutive-divisor property follows because the only possible integers strictly between the reciprocal ratios \(2,3\), \(3,4\), or \(4,6\) are, respectively, none, none, or \(5\); \(5\nmid n\).

If \(a=1\), set \(u=n/3\), \(v=n/2\), and write \(C=3^b\ge9\). Exact sums give
\[
T_n(u)=\frac{3(C-1)}2<2C=n<\frac{5C-3}2=T_n(v).
\]
For \(a\ge2\), let \(B=3^{b-1}\ge3\) and \(A=2^a\). By summing each \(3\)-adic divisor layer, one obtains
\[
T_n(n/4)=\frac{(7A-9)B-2A+1}{2},\qquad
T_n(n/3)=\frac{(9A-9)B-2A+1}{2}.
\]
Since \(n=3AB\), the differences satisfy
\[
T_n(n/4)-n=\frac{(A-9)B-2A+1}{2},\qquad
T_n(n/3)-n=\frac{(3A-9)B-2A+1}{2}.
\]
For \(a=2\) or \(a=3\), the first expression is negative and the second positive for every \(B\ge3\). For \((a,b)=(4,2)\), the two consecutive divisors \(n/4=36\), \(n/3=48\) have prefix sums \(139<n=144<187\).

In every other case with \(a\ge4\), one has \(T_n(n/4)>n\). Indeed, its displayed difference is strictly positive if \(A\ge32\) and \(B\ge3\), or if \(A=16\) and \(B\ge9\). The additional identity, valid for \(a\ge3\),
\[
T_n(n/6)-n=-\frac{(A+18)B+4A-2}{4}<0,
\]
shows that the consecutive divisors \(n/6\) and \(n/4\) straddle \(n\). This excludes all \(p=3\), \(b\ge2\).

**Case 4: \(p=3\), \(b=1\).** If \(a=1\), then \(n=6\) is even perfect and fits Case 2's classical conclusion. For \(a\ge2\), exact prefix sums at \(n/4\) and \(n/3\) are
\[
T_n(n/4)=\frac52 A-4,
\qquad T_n(n/3)=\frac72 A-4,
\qquad n=3A.
\]
At \(a=2\), the consecutive divisors \(n/3=4\) and \(n/2=6\) have sums \(10<12<16\), so no equality. At \(a=3\) one has \(T_{24}(24/3)=24\), giving the claimed exception. At \(a\ge4\), the consecutive divisors \(n/4\) and \(n/3\) strictly straddle \(n\), because \(\frac52A-4<3A<\frac72A-4\). These four cases cover all primes and exponents, completing the proof.

## Verification
A standalone exact-integer script `verify.py` independently enumerates all proper-divisor prefixes for \(1\le a\le20\), \(1\le b\le10\), and all odd primes below \(181\); it checks the classification in 8,000 cases. It separately checks 323 explicit consecutive-divisor straddles for \(3\)-power odd parts, and 336 prime-power evaluations of the closed prefix-sum formulas. The execution prints `VERIFY_OK`. The finite checks corroborate, but do not prove, the universal quantifiers.

## Relationship to prior work
Erdős and Nicolas introduced the initial-divisor-sum property and gave early nonperfect examples, including \(24\), in 1975 [1]. OEIS A064510 includes the corresponding perfect-number cases, while A194472 records the nonperfect examples [2,3]. A previously published investigation of \(2^a p^b\) [4] proved the \(b=1\) classification, excluded \(b=2\), and reduced \(b\ge3\) to a bounded-per-\(a\) set of candidates. Its result explicitly **did not exclude the remaining higher odd-prime exponents**. The new claim strictly strengthens that result: the proof above eliminates every \(b\ge3\), including its formerly unresolved candidate set. The already known \(b=1\) and \(b=2\) statements are included for completeness, not independently presented as new results.

## Limitations
The theorem concerns only the even family with exactly one odd prime divisor. It does not settle the general distribution, density, parity, or infinitude of Erdős–Nicolas numbers. Historical originality is asserted subject to the possibility of unindexed earlier work; no universal novelty guarantee is claimed. The computation is bounded, while the written proof is unbounded.

## References
1. P. Erdős and J.-L. Nicolas, *Répartition des nombres superabondants*, Bull. Soc. Math. France **103** (1975), 65–90, https://doi.org/10.24033/bsmf.1793 ; full text https://www.renyi.hu/~p_erdos/1975-37.pdf , especially p. 89.
2. OEIS A064510, *Numbers whose first \(k\) divisors sum to the number*, https://oeis.org/A064510 (initial public entry October 6, 2001).
3. OEIS A194472, *Erdős–Nicolas numbers*, https://oeis.org/A194472 (initial public entry dated August 24, 2011).
4. *Prime-power odd parts in initial-divisor sums*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/9/21/SCOPE-erdos-nicolas-two-prime-power-reduction--fab5fef920f2/RESULT.md .
