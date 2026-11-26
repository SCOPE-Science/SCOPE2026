# Base-\(p\) digit classification of absolute-minimum restricted-GCD extremal rows
## Finding
Let \(p\) be a prime and let \(m\ge 2\) satisfy \(p\nmid m\). Define
\[
G(N;m)=\gcd\left\{\binom{N}{k}:0<k<N,\ m\mid k\right\},
\qquad
r_p(m)=\min\left\{r\ge1:m<p^r\right\}.
\]
The recent extremal theorem for this family shows that the maximum possible value of \(v_p(G(N;m))\) over admissible rows is \(r_p(m)\), and therefore defines the least row \(T_p(m)\) attaining that maximum.

Write \(r=r_p(m)\) and the base-\(p\) expansion
\[
m=\sum_{j=0}^{r-1}d_jp^j,
\qquad 0\le d_j<p.
\]
Because \(p\nmid m\), one has \(d_0>0\). Then the least extremal row attains its absolute possible minimum precisely under the digit conditions
\[
T_p(m)=2m
\quad\Longleftrightarrow\quad
2d_0\ge p
\ 	ext{ and }\
2d_j+1\ge p\quad(1\le j<r).
\]
For odd \(p\), this is equivalently
\[
d_0\ge\frac{p+1}2,
\qquad
d_j\ge\frac{p-1}2\quad(1\le j<r).
\]
For \(p=2\), it is equivalently \(m=2^r-1\).

A counting consequence is exact. For odd \(p\) and fixed \(r\ge1\), the number of \(r\)-digit integers \(m\) with \(p\nmid m\) and \(T_p(m)=2m\) is
\[
\frac{p-1}2\left(\frac{p+1}2\right)^{r-1}.
\]
In particular, every admissible repunit-complement parameter satisfies
\[
T_p(p^a-1)=2(p^a-1)
\]
whenever \(p^a-1\ge2\).

## Assumptions and scope
An admissible row is an integer \(N>m\) divisible by \(m\). The parameter \(T_p(m)\) is the least admissible row at which \(v_p(G(N;m))\) equals the sharp maximum \(r_p(m)\). The result assumes \(p\) prime, \(m\ge2\), and \(p\nmid m\). It classifies exactly when the least extremal row is as small as it can possibly be, namely \(2m\).

The result does not determine \(T_p(m)\) when the digit inequalities fail. The recently proved family \(m=p^a+1\), whose least row is much larger, is complementary rather than a special case of the classification here.

## Proof
Every admissible row has the form \(N=mq\) with integer \(q\ge2\). Hence \(2m\) is the smallest admissible row, so
\[
T_p(m)=2m
\]
if and only if \(2m\) already attains the sharp maximum \(r\).

At the row \(N=2m\), the divisibility restriction leaves exactly one proper positive selected lower index: \(k=m\). Therefore
\[
G(2m;m)=\binom{2m}{m},
\]
and Kummer's theorem gives
\[
v_p(G(2m;m))=v_p\binom{2m}{m}
=\#\{\text{carries in the base-}p\text{ addition }m+m\}.
\]
Because \(m<p^r\), this addition can create at most one carry out of each of the \(r\) occupied digit positions, hence at most \(r\) carries altogether. The row \(2m\) is extremal exactly when all \(r\) possible carries occur.

At the units digit there is no incoming carry. Thus a carry leaves digit \(0\) exactly when
\[
2d_0\ge p.
\]
If carries have occurred at every earlier position, then digit \(j\ge1\) receives an incoming carry of \(1\). A carry leaves that digit exactly when
\[
2d_j+1\ge p.
\]
Consequently all \(r\) carries occur if and only if the displayed system holds. This proves the classification.

For odd \(p\), the first inequality is \(d_0\ge(p+1)/2\), giving \((p-1)/2\) choices for \(d_0\). Each higher digit must satisfy \(d_j\ge(p-1)/2\), giving \((p+1)/2\) choices. The top digit is automatically nonzero under this condition, so multiplication of independent digit choices gives
\[
\frac{p-1}2\left(\frac{p+1}2\right)^{r-1}.
\]
For \(p=2\), the conditions force every digit \(d_j=1\), hence \(m=2^r-1\). Finally, \(p^a-1\) has every base-\(p\) digit equal to \(p-1\), so it satisfies the criterion whenever it lies in the stated domain.

## Verification
The proof is symbolic and does not depend on finite computation. A standalone verifier included with this result independently checks the carry criterion, the exact odd-prime counting formula, the binary classification, and the family \(m=p^a-1\) over a deterministic grid of primes and digit lengths. It computes carry counts directly from base-\(p\) addition and compares them to the digit predicate.

## Relationship to prior work
Fairfax-Ball's recent paper on sharp \(p\)-adic extrema for the same restricted GCD proves that the maximum over rows is \(r_p(m)\), establishes existence of equality rows, defines \(T_p(m)\), and determines the separate family \(T_p(p^a+1)=p^{3a}+1\). Its examples record the previously known isolated case \(T_2(3)=6\), but the paper does not state a classification of all parameters for which \(T_p(m)=2m\), nor the digit-count formula above.

McTague studies the same multiple-index GCD under a congruence hypothesis and explicitly contains the isolated \(v_2(G(6;3))=2\) case. Wu studies the identical family in the notation \(g(m,n)=G(mn;m)\) and gives other computation results. The new statement is a complete characterization of the absolute-minimum extremal row using the central row \(2m\); it contains known isolated and congruence-overlap cases but is not implied by their stated theorems. Targeted searches for the exact \(T_p(m)=2m\) classification, central-binomial formulation, and digit-threshold equivalent did not locate an equivalent result.

## Limitations
The classification relies on the already established sharp maximum \(r_p(m)\); it does not reprove that global extremal theorem. It determines only the absolute-minimum branch \(T_p(m)=2m\), not the least extremal row outside that branch. The full text of one supporting 2026 source was not available through the inspected HTML endpoint, so its abstract and the direct source's theorem-level comparison were used; this leaves a residual bibliographic risk, as does unindexed or differently phrased literature.

## References
1. John Fairfax-Ball, *Sharp \(p\)-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328v1, 2026.
2. Carl McTague, *On the Greatest Common Divisor of Binomial Coefficients \(\binom n q,\binom n{2q},\binom n{3q},\ldots\)*, arXiv:1510.06696v5; Amer. Math. Monthly 124 (2017), 353--356.
3. Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients \(\binom{mn}{mk}\)*, arXiv:2606.20940v2, 2026.
4. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. 44 (1852), 93--146.
