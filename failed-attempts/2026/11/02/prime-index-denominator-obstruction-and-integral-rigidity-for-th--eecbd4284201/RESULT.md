# Prime-index denominator obstruction and integral rigidity for the fourth-power Franel recurrence

## Finding

Define the fourth-power Franel numbers by
\[
H_n=\sum_{k=0}^{n}\binom nk^4\qquad(n\ge0).
\]
Fix any integers \(u,v\), and let \((U_n)_{n\ge0}\) be the unique rational sequence with \(U_0=u\), \(U_1=v\), and
\[
(n+1)^3U_{n+1}=2(6n^3+9n^2+5n+1)U_n+4n(4n-1)(4n+1)U_{n-1}\quad(n\ge1).
\]
Put \(\Delta=v-2u\). For every prime \(p\ge5\), if \(\Delta\ne0\), then the adjacent-solution determinant
\[
W_{p-1}=H_{p-1}U_p-H_pU_{p-1}
\]
satisfies the **exact local obstruction**
\[
\nu_p(W_{p-1})=\nu_p(\Delta)-1.
\]
Consequently, if \(p\nmid\Delta\), at least one of \(U_{p-1}\) and \(U_p\) is not an integer. In particular, the complete lattice of integer-valued solutions is
\[
\boxed{(\forall n\ge0,\ U_n\in\mathbb Z)\ \Longleftrightarrow\ v=2u\ \Longleftrightarrow\ (\forall n\ge0,\ U_n=uH_n).}
\]

## Assumptions and scope

All indices \(n\) are nonnegative integers; the recurrence is imposed for \(n\ge1\), so initial pairs \((u,v)\in\mathbb Z^2\) determine rational solutions uniquely. The \(p\)-adic valuation \(\nu_p\) is defined on nonzero rational numbers as the exponent of \(p\) in the numerator minus that in the denominator of a reduced fraction. The local identity is asserted only when \(\Delta\ne0\) and \(p\ge5\); the global integral classification includes \(\Delta=0\).

## Proof

**1. A known integral reference solution.** Every \(H_n\) is an integer by its binomial sum. Franel's fourth-power recurrence, given explicitly for example in Cusick's 1989 paper, is precisely the displayed recurrence with \(U_n=H_n\). It starts at \(H_0=1\) and \(H_1=2\). The same recurrence is recorded for the Yang–Zudilin sequence in Straub (2014, Example 3.6) with parameters \((a,b,c,d)=(6,2,-64,4)\).

**2. Exact determinant propagation.** For any two solutions, subtraction of their recurrence equations gives
\[
W_n=-\frac{4n(4n-1)(4n+1)}{(n+1)^3}W_{n-1}\qquad(n\ge1),
\]
where \(W_n=H_nU_{n+1}-H_{n+1}U_n\). Since \(W_0=v-2u=\Delta\), iteration yields the **rational identity**
\[
W_n=\Delta(-4)^n\frac{\prod_{j=1}^{n}j(4j-1)(4j+1)}{((n+1)!)^3}\qquad(n\ge0).
\]
An empty product is one. No integrality of \(U_n\) is assumed in this calculation.

**3. A universal prime-index defect.** Fix a prime \(p\ge5\) and take \(n=p-1\). Among \(j=1,\ldots,p-1\), no \(j\) is divisible by \(p\). Each linear congruence \(4j-1\equiv0\pmod p\) and \(4j+1\equiv0\pmod p\) has exactly one solution in this interval. The two solutions are different because \(p\) is odd. Moreover, \(0<4j-1<4p\le p^2\) and \(0<4j+1<4p\le p^2\); hence none of these factors is divisible by \(p^2\). Therefore
\[
\nu_p\!\left(\prod_{j=1}^{p-1}j(4j-1)(4j+1)\right)=2.
\]
But \(\nu_p((p!)^3)=3\), and \(p\nmid4\). Applying the determinant identity proves
\[
\nu_p(W_{p-1})=\nu_p(\Delta)+2-3=\nu_p(\Delta)-1.
\]

**4. Integral-rigidity conclusion.** If \(U_{p-1}\) and \(U_p\) were both integers, their determinant with integer \(H_{p-1},H_p\) would be an integer. The valuation identity rules this out whenever \(p\nmid\Delta\). If \(\Delta\ne0\), infinitely many primes \(p\ge5\) fail to divide the fixed nonzero integer \(\Delta\), so the entire sequence cannot consist of integers. Conversely, if \(\Delta=0\), the sequences \((U_n)\) and \((uH_n)\) have the same initial values and recurrence, and therefore coincide term-by-term; every term is integral. This proves both directions.

## Verification

Run `python3 verify.py` using the standard library. The program constructs the binomial sums and independently propagates rational solutions to index 96. It checks 672 determinant instances from seven initial pairs, the exact fourth-power recurrence, and the two linear-factor valuations for all 22 primes from five through 89. It also computes the asserted rational denominator defect at each tested prime. These are finite consistency checks; the proof above supplies the unrestricted quantifiers.

## Relationship to prior work

The binomial-sum reference sequence and its three-term recurrence are classical, dating to Franel's 1895 work. Cusick (1989) states the exact recurrence and studies recurrences for generalized binomial power sums. Straub (2014, Example 3.6) identifies \(H_n\) with the Yang–Zudilin sequence and studies its supercongruences. Straub and Zudilin (2022, Theorem 1.3) construct rational companion solutions and their Apéry limits for generalized Franel sums; they do not state a prime-index integrality obstruction or classify all integral initial pairs. Tonien (2026, Theorem 6) gives an analogous determinant identity for the distinct *cubic* Franel recurrence, not the present fourth-power case. Thus the recurrence, integrality of \(H_n\), and standard determinant propagation are not claimed as new; the contribution is the explicit two-root prime-local denominator defect and its resulting complete integral-solution classification for the fourth-power recurrence.

## Limitations

The theorem concerns the specified fourth-power binomial-sum recurrence, with integer initial values and all nonnegative indices. It does not classify all integral solutions of arbitrary Apéry-like recurrences, nor does it claim that the early nonintegral term can be prescribed as one specific member of the pair \(U_{p-1},U_p\). For \(p=2,3\) the displayed local-valuation proof is not used. Related results could exist under the terminology *Yang–Zudilin numbers*, *generalized Franel numbers*, *Casoratian*, or *integral recurrence solutions*; historical priority is not independently certified.

## References

1. J. Franel, *L'Intermédiaire des Mathématiciens*, volume 2 (1895), 33–35 (original recurrence; calendar-day publication evidence not determined).
2. T. W. Cusick, “Recurrences for sums of powers of binomial coefficients,” *Journal of Combinatorial Theory, Series A* 52 (1989), 77–83, DOI:10.1016/0097-3165(89)90063-0.
3. A. Straub, “Multivariate Apéry numbers and supercongruences of rational functions,” arXiv:1401.0854, first posted 2014-01-05, especially Section 2 and Example 3.6. This is the earliest precisely day-dated public source verified for the archival framing here; older published works are cited above without inventing day-level evidence.
4. A. Straub and W. Zudilin, “Sums of powers of binomials, their Apéry limits, and Franel's suspicions,” arXiv:2112.09576, first posted 2021-12-17, especially Theorems 1.1 and 1.3.
5. J. Tonien, “Franel Numbers and a Continued Fraction Conjecture Discovered by the Ramanujan Machine,” *The Mathematical Intelligencer*, DOI:10.1007/s00283-025-10497-9, especially Theorem 6 (cubic counterpart).
