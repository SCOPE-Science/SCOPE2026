# Forty-word triple spectrum of central trinomial residues modulo five

## Finding

Let \(T_n=[x^0](x^{-1}+1+x)^n\) for \(n\ge0\), and let \(e(0),\ldots,e(4)=(0,0,1,3,2)\). Identify the four nonzero residues modulo five with exponents \(a\in\mathbb Z/4\mathbb Z\) through \(3^a\pmod5\). For \(a,b,c\in\mathbb Z/4\mathbb Z\), the natural density of indices satisfying
\[
(T_n,T_{n+1},T_{n+2})\equiv(3^a,3^b,3^c)\pmod5
\]
exists and is
\[
\boxed{P(a,b,c)=\frac1{20}\sum_{t=0}^{2}
 \mathbf1_{(b,c)=(a-e(t)+e(t+1),\ a-e(t)+e(t+2))}
 +\frac1{80}\mathbf1_{b=a-1}
 +\frac1{80}\mathbf1_{c=b}.}
\]
All displayed exponent equalities are modulo four. Consequently exactly **40 of the 64** possible consecutive residue triples ever occur. Their positive densities consist of twelve cells of mass \(1/20\), four cells of mass \(1/40\), and twenty-four cells of mass \(1/80\); the other twenty-four are **strictly forbidden for every index**. All forty occur already among the triples starting at \(0\le n<5^3\). Although each adjacent pair has limiting uniform distribution \(1/16\), the consecutive three-point law is strongly nonuniform.

The finite-level law is also exact. Put \(R=r-1\) for \(r\ge1\), and, for \(s,d\in\mathbb Z/4\mathbb Z\), define
\[
A_R(s)=\frac{5^R-1}{4}+\mathbf1_{s=0},\qquad
B_R(s,d)=\sum_{k=0}^{R-1}\left(\frac{5^{R-k-1}-1}{4}+
\mathbf1_{s=e(a_k)+2k}\right)+\mathbf1_{s=2R,\ d=-2R},
\]
where \(a_k\) is the unique element of \(\{0,1,2,3\}\) congruent to \(d+2k\) modulo four. For \(s_t=a-e(t)\), the exact count among \(0\le n<5^r\) is
\[
\boxed{N_r(a,b,c)=\sum_{t=0}^2
 \mathbf1_{(b,c)=(s_t+e(t+1),s_t+e(t+2))}A_R(s_t)
 +\mathbf1_{b=a-1}B_R(a-3,c-a+3)
 +\mathbf1_{c=b}B_R(a-2,b-a+2).}
\]
In particular \(N_r(a,b,c)=5^rP(a,b,c)+O(r)\) uniformly over the sixty-four cells. For every integer \(N\ge2\), the count up to \(N\) differs from \(NP(a,b,c)\) by at most \(O((1+\log_5 N)^2)\), with an absolute implied constant.

## Assumptions and scope

All indices are nonnegative integers; \(r\ge1\); \(N\ge2\); and exponents, indicator equations, and additions inside \(P,A_R,B_R,N_r\) are in \(\mathbb Z/4\mathbb Z\). The count uses the actual infinite central-trinomial sequence even when \(n+1\) or \(n+2\) exceeds the base-five cutoff. The density is a natural density over all indices, not only over powers-of-five cutoffs. No prime other than five is covered.

## Proof

**Digit product.** The freshman's-dream congruence and the fact that a degree-at-most-four Laurent polynomial cannot cancel a nonzero exponent divisible by five show
\[
T_{5m+t}\equiv T_mT_t\pmod5\quad(0\le t<5).
\]
The initial residues are \((T_0,\ldots,T_4)\equiv(1,1,3,2,4)=(3^{e(0)},\ldots,3^{e(4)})\pmod5\). Thus if \(S(m)\) is the sum of \(e\) over the base-five digits of \(m\), then \(T_m\equiv3^{S(m)}\pmod5\). In the group ring of \(\mathbb Z/4\mathbb Z\), the single-digit polynomial is \(2+X+X^2+X^3=1+J\), with \(J=1+X+X^2+X^3\) and \(J^2=4J\). Its \(R\)-th power is \(1+(5^R-1)J/4\), giving the exact count \(A_R(s)\) for \(S(m)=s\) among \(0\le m<5^R\).

**A digit increment.** Put \(\Delta(m)=S(m+1)-S(m)\pmod4\). If \(m\) has precisely \(k\) trailing base-five digits equal to four, followed by digit \(a\in\{0,1,2,3\}\), then
\[
\Delta(m)=e(a+1)-e(a)-k e(4)=a-2k\pmod4,
\]
using \(e(a+1)-e(a)=a\pmod4\). The remaining \(R-k-1\) high digits have the known \(A\)-distribution. With \(a=a_k\) forced by \(\Delta=d\), their exact contribution to \((S,\Delta)=(s,d)\) is \((5^{R-k-1}-1)/4+\mathbf1_{s=e(a_k)+2k}\). The exceptional \(m=5^R-1\), consisting solely of digits four, has \((S,\Delta)=(2R,-2R)\pmod4\). This proves the exact formula for \(B_R(s,d)\) with no omitted boundary term. Summing its geometric part gives
\[
B_R(s,d)=\frac{5^R-1-4R}{16}+E_R(s,d),\qquad 0\le E_R(s,d)\le R+1,
\]
so \(B_R(s,d)=5^R/16+O(R+1)\) uniformly.

**Three consecutive positions.** Write \(n=5m+t\), \(0\le t<5\). For \(t=0,1,2\), there is no carry into \(m\) and the triple of exponents is \((S(m)+e(t),S(m)+e(t+1),S(m)+e(t+2))\). For \(t=3\), it is \((S(m)+3,S(m)+2,S(m)+\Delta(m))\). For \(t=4\), it is \((S(m)+2,S(m)+\Delta(m),S(m)+\Delta(m))\). These five mutually exhaustive cases, together with \(A_R\) and \(B_R\), give exactly the stated formula for \(N_r\). Division by \(5^r\) gives the displayed \(P\), with error \(O(r/5^r)\).

**Support and sharp onset.** The three no-carry classes \(t=0,1,2\) contribute twelve distinct words, with respective differences between the second and first exponent \(0,1,2\) and unequal second and third exponents. The \(t=3\) class has \(b=a-1\) and arbitrary third exponent, hence sixteen words; the \(t=4\) class has \(c=b\) and arbitrary first exponent, hence sixteen words. The last two classes intersect in exactly four words. All these classes are disjoint from the first twelve, so there are \(12+16+16-4=40\) words. For \(R\ge2\), choose \(k=0\), the digit \(a=d\), and a further high digit realizing any chosen exponent (the five digits realize all four). Hence every \((s,d)\) has positive \(B_R(s,d)\), proving that all forty words already occur at \(r=3\); the case analysis excludes every other word at every index. Their probabilities are respectively \(1/20\), \(1/80\), with the four intersections doubled to \(1/40\).

**All cutoffs.** In any aligned interval \([u5^r,(u+1)5^r)\), outside at most two terminal indices, the three central-trinomial residues are the corresponding residues at indices in \([0,5^r)\) multiplied by the same factor \(T_u\pmod5\). The formula for \(P\) is invariant under simultaneous multiplication, equivalently translation of all three exponents by one constant. Hence the aligned-block error is \(O(r+1)\), uniformly in \(u\). The base-five decomposition of \([0,N)\) uses at most four aligned blocks of each level. Adding errors for levels at most \(\lfloor\log_5 N\rfloor\) yields \(O((1+\log_5 N)^2)\). Marginalizing \(P\) over the last or first exponent yields \(1/16\) for either adjacent pair.

## Verification

The reproducible standalone Python checker `verify_three_point.py` verifies the direct integer three-term recurrence for the first 3,127 central trinomial numbers, compares its residues with an independently implemented base-five digit exponent, verifies the sixty-four-cell finite count formula for every cutoff \(5^r\), \(1\le r\le6\), checks the first occurrence cutoff and all forty positive word classes, and checks the exact rational mass tiers, pair marginals, and lag-two ratio marginal. It completed with `VERIFY_OK assertions=3614 exact_depths=1..6 integer_terms=3127 words=40 forbidden=24`. These are finite checks; the proof above establishes all-depth and all-cutoff statements.

## Relationship to prior work

Deutsch and Sagan (2004) establish classical congruences for central trinomial numbers; Rowland and Yassawi (2013) establish a broad automatic-congruence and Lucas-product framework. The published published-finding corpus two-point analysis, *All-lag two-point laws and exact logarithmic bias for central trinomial residues modulo five* (2026), gives all fixed-lag **pair** distributions and exact adjacent-pair counts. It does not assert any evaluated three-consecutive-position law or the forty-word spectrum. The formula here marginalizes to its adjacent-pair uniformity and lag-two nonuniform ratio law, but those pairwise data do not fix a joint distribution of three variables. General automaton existence makes a computation possible; it does not state the evaluated support and exact rational frequencies proved here. An indexed search and primary-source comparison found no specific covering triple result.

## Limitations

The claims are restricted to modulus five and three consecutive positions. The new value is the **evaluated joint three-point law**, not the established Lucas product, automaticity or two-point distribution. The search for prior presentations is incomplete, and an earlier unindexed three-point enumeration or a stronger explicit multi-point theorem remains an originality risk. The finite checker is supporting evidence only. No independent scientific audit has been performed.

## References

1. E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326, first public 2004-07-19, https://arxiv.org/abs/math/0407326; see Section 4.
2. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, first public 2013-10-31, https://arxiv.org/abs/1310.8635; see Sections 4.2 and 5.
3. *All-lag two-point laws and exact logarithmic bias for central trinomial residues modulo five*, RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-all-lag-two-point-laws-and-exact-logarithmic-bias-for-central-tr--fa9f646a7cb7/RESULT.md.
4. OEIS A002426, *Central trinomial coefficients*, https://oeis.org/A002426 (the sequence entry records public contributions dated from 2002).
