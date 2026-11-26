# A maximal \(p\)-adic plateau and sharp collapse for selected binomial GCDs at \(p^r-1\)

## Finding
Fix a prime \(p\) and integer \(r\ge 2\); put \(b=p^r\) and \(m=b-1\). For every integer \(q\ge2\), define
\[
G(mq;m)=\gcd\left\{\binom{mq}{md}:1\le d<q\right\}.
\]
Then the complete initial run of rows achieving the sharp \(p\)-adic exponent \(r\) is
\[
\boxed{v_p(G(mq;m))=r\quad\text{for every }2\le q\le p^r,}
\]
while the immediately following row satisfies
\[
\boxed{v_p(G(m(p^r+1);m))=0.}
\]
In particular, the **least multiplier losing maximal \(p\)-adic valuation** is exactly \(p^r+1\), and the valuation at that first failure falls all the way from \(r\) to zero. The statement concerns the exponent of \(p\) in the selected-binomial GCD, not the entire integer GCD.

## Assumptions and scope
Here \(v_p(x)\) denotes the exponent of prime \(p\) in the positive integer \(x\). The index \(md\) ranges over all proper positive multiples of \(m\) below the admissible row \(mq\). Every quantifier in the theorem is unrestricted apart from \(p\) prime, \(r\ge2\), and the stated integer intervals for \(q\). The source-independent proof below needs no unproved conjecture, finite search bound, or asymptotic estimate.

Write \(s_p(x)\) for the sum of the base-\(p\) digits of a nonnegative integer \(x\). Legendre's factorial formula implies the exact identity
\[
v_p\binom{u+v}{u}=\frac{s_p(u)+s_p(v)-s_p(u+v)}{p-1}
\qquad(u,v\ge0).
\]

## Proof
**Digit-sum lemma.** For any positive integer \(x\) divisible by \(m=p^r-1\),
\[
s_p(x)\ge r(p-1).
\]
To prove it, take all the base-\(p\) digits of \(x\) and fold positions modulo \(r\), obtaining nonnegative coefficients \(c_0,\dots,c_{r-1}\) with
\[
\sum_{j=0}^{r-1}c_j= s_p(x),\qquad
\sum_{j=0}^{r-1}c_jp^j\equiv x\equiv0\pmod{p^r-1}.
\]
Whenever some \(c_j\ge p\), replace \(p\) units at position \(j\) by one unit at position \(j+1\pmod r\). Each such operation preserves the congruence, keeps all coefficients nonnegative, and decreases their sum by exactly \(p-1\). It terminates because the sum is a positive integer. In the terminal state, each \(c_j\) is between zero and \(p-1\), and
\[
1\le\sum_{j=0}^{r-1}c_jp^j\le p^r-1.
\]
The middle expression is a positive multiple of \(p^r-1\), so it must equal \(p^r-1\). Thus every terminal digit is \(p-1\), giving terminal digit sum \(r(p-1)\). The original digit sum was no smaller.

**Digits of the candidate rows.** For every integer \(1\le t\le b=p^r\),
\[
mt=(t-1)b+(b-t).
\]
Both summands occupy disjoint blocks of at most \(r\) base-\(p\) digits, and \(b-t=(b-1)-(t-1)\) is the digitwise complement of \(t-1\) in its padded \(r\)-digit block. Therefore
\[
s_p(mt)=s_p(t-1)+s_p(b-t)=r(p-1).
\tag{1}
\]
This includes both endpoints \(t=1\) and \(t=b\).

**The full plateau.** Fix any integer \(2\le q\le b\). Equation (1) gives \(s_p(mq)=r(p-1)\). For each selected index \(md\), \(1\le d<q\), both \(md\) and \(m(q-d)\) are positive multiples of \(m\), hence their digit sums are at least \(r(p-1)\) by the lemma. Consequently
\[
v_p\binom{mq}{md}
=\frac{s_p(md)+s_p(m(q-d))-s_p(mq)}{p-1}\ge r.
\]
For \(d=1\), equation (1) applies to \(t=1\) and \(t=q-1\), giving equality:
\[
v_p\binom{mq}{m}=\frac{r(p-1)+r(p-1)-r(p-1)}{p-1}=r.
\]
The minimum valuation among **all** selected binomial coefficients is therefore exactly \(r\), proving the first boxed identity.

**Sharp first failure.** At \(q=b+1\),
\[
mq=(b-1)(b+1)=b^2-1=p^{2r}-1,
\]
whose digit sum is \(2r(p-1)\). Choosing again the permitted lower index \(m\), the complementary summand is \(bm\), and both \(m\) and \(bm\) have digit sum \(r(p-1)\). Thus
\[
v_p\binom{m(b+1)}m
=\frac{r(p-1)+r(p-1)-2r(p-1)}{p-1}=0.
\]
Since all binomial coefficients are integers, the selected GCD valuation is nonnegative; its having one selected coefficient of valuation zero proves that it is zero. No earlier \(q\) fails by the plateau already established. \(\square\)

## Verification
The standalone `verify.py` evaluates factorial valuations using Legendre's floor-sum formula, independently from the symbolic digit-sum argument. It checks every selected coefficient for 13 pairs \((p,r)\), for each multiplier from \(2\) through \(p^r+1\), totalling 83,211 exact binomial valuation checks. All comparisons reproduced the plateau and first failure. Run `python3 verify.py`. These bounded checks corroborate the formulas but are not used to prove their universal quantifiers.

## Relationship to prior work
Fairfax-Ball, arXiv:2610.01328v1 (public 2026-10-01, primary MSC 11B65), proves that for \(p\nmid m\) the maximal selected-GCD valuation over all rows is \(r_p(m)=\min\{j\ge1:m<p^j\}\), and determines the least row for \(m=p^a+1\). The present theorem addresses the complementary natural family \(m=p^r-1\), giving the entire initial contiguous block of maximizing rows and the first row with no factor \(p\), rather than only a maximizing row.

Guo et al., arXiv:2606.22997v1, consider \(D(k)=\gcd_{2\le q\le k+1}\binom{qk}{k}\), a GCD **across row multipliers** of one binomial coefficient per row. A known specialization (also obtained by a separate exact congruence) says that \(v_p\binom{q(p^r-1)}{p^r-1}=r\) for \(2\le q\le p^r\). This identifies the valuation of one selected coefficient, but by itself only supplies an **upper** bound on the GCD of all selected indices in each row. The digit-sum lemma above supplies the missing simultaneous lower bound for every \(md\), and the sharp zero-valued transition. Wu, arXiv:2606.20940v2, and McTague (2017) study the selected-binomial-GCD family; the documented results concern other restrictions, such as restriction parameters that are powers of \(p\) or \(p\equiv1\pmod m\). Neither implies this all-selected-coefficient plateau for \(r\ge2\).

## Limitations
No claim is made about the full integer value of \(G(mq;m)\), or about any multiplier \(q>p^r+1\). The classical digit-sum/Legendre identity and the single-index congruence are antecedents, not independent inventions. The primary papers and indexed comparisons checked are not a proof that earlier unindexed computations or implicit special cases do not exist. Independent external review has not been performed.

## References
1. J. Fairfax-Ball, *Sharp p-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328v1 (2026), https://arxiv.org/abs/2610.01328 .
2. D. Guo, R. Qiu, Y. Cao, R. Feng, X.-S. Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1 (2026), https://arxiv.org/abs/2606.22997 .
3. C. W. Wu, *Computing the Greatest Common Divisor of Binomial Coefficients*, arXiv:2606.20940v2 (2026), https://arxiv.org/abs/2606.20940 .
4. C. McTague, *On the Greatest Common Divisor of Binomial Coefficients*, American Mathematical Monthly **124** (2017), 353–356, doi:10.4169/amer.math.monthly.124.4.353 .
5. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen* (1852); classical carry theorem and Legendre's factorial valuation formula.
