# Exact \(5\)-adic saturation for four 5-core tuple progressions

## Finding

Let \(A_{5,k}(m)\) count ordered \(k\)-tuples of 5-core partitions whose total size is \(m\). Put \(R=\{9,14,19,24\}\). For every integer \(i\ge0\), let \(e(i)\) be the largest nonnegative integer such that
\[
A_{5,125i+21}(25n+r)\equiv0\pmod{5^{e(i)}}
\quad\text{for every }n\ge0\text{ and }r\in R.
\]
Then the exact exponent is
\[
\boxed{e(i)=\begin{cases}
3,&i\not\equiv3\pmod5,\\
4,&i\equiv3\pmod5\ \text{but}\ i\not\equiv13\pmod{25},\\
5,&i\equiv13\pmod{25}.
\end{cases}}
\]
In particular, the exceptional class \(i=13+25b\) supports the previously unavailable *second uniform lift* to \(5^5=3125\), and no third lift holds uniformly in that class. More precisely, for every integer \(b\ge0\), the fifth dissection satisfies the coefficientwise identity
\[
\boxed{\sum_{n\ge0}A_{5,1646+3125b}(5n+4)q^n
\equiv1920\,E(q^5)^{1584+3000b}\pmod{3125},}
\]
where \(E(q)=\prod_{m\ge1}(1-q^m)\). Its right side has only powers of \(q\) divisible by five. The sharp obstruction to a congruence modulo \(15625\) is witnessed by the pair of coefficients at indices \(9\) and \(14\), rather than by either coefficient alone.

## Assumptions and scope

All formal-series congruences are coefficientwise over \(\mathbb Z[[q]]\). The 5-core generating function, valid for all positive integer \(k\), is
\[
F(q)^k=\sum_{m\ge0}A_{5,k}(m)q^m,
\qquad F(q)=\frac{E(q^5)^5}{E(q)}.
\]
The parameters \(i,b,n\) range over nonnegative integers. The exponent is a *common* exponent across all four progressions and all indices, not an assertion of optimality separately for each progression.

## Proof

**1. The published baseline and the first lift.** Maity's Theorem 3.1 proves that the four progressions are zero modulo \(125\) for every \(k=21+125i\). A known first-lift result (also derivable below) shows the stronger uniform modulus \(625\) when \(i=3+5a\), i.e. \(k=396+625a\).

For transparency, we reproduce the formal-series mechanism and derive the further lift without invoking a finite Sturm computation. Define
\[
\zeta(q)=\frac{E(q)}{qE(q^{25})},\qquad
\xi(q)=\frac{E(q)^6}{qE(q^5)^6},\qquad
U_5\left(\sum_j c_jq^j\right)=\sum_j c_{5j}q^j.
\]
The fifth-order modular equation in Maity's Lemma 2.2 gives \(U_5(\zeta^m)=P_m(\xi)\), with initial values
\[
P_0=1,\quad P_1=P_2=-1,\quad P_3=5,\quad P_4=-5,
\]
and integral polynomial recurrence, for all \(m\ge0\),
\[
P_{m+5}=-5P_{m+4}-15P_{m+3}-25P_{m+2}-25P_{m+1}+XP_m.
\]
Here \(X\) is the indeterminate. Exact recurrence arithmetic yields
\[
P_{229}(X)\equiv45X^{45}\pmod{625},\qquad
P_{1479}(X)\equiv1920X^{295}\pmod{3125}.
\tag{1}
\]
Both assertions mean that *every other polynomial coefficient* vanishes at the stated modulus; the standalone checker computes all polynomial coefficients from the displayed recurrence.

Use the elementary integral Frobenius-lifting congruence
\[
E(q)^{5^t}\equiv E(q^5)^{5^{t-1}}\pmod{5^t}\qquad(t\ge1).
\tag{2}
\]
It follows by multiplying the prime-power binomial congruence for each factor \((1-q^m)\); inverse powers are legitimate because the series have constant coefficient one.

Take \(k=396+625a\). From (2),
\[
F(q)^k\equiv E(q^5)^{1855+3000a}E(q)^{229}\pmod{625}.
\]
Substitute \(E(q)^{229}=q^{229}E(q^{25})^{229}\zeta^{229}\), multiply by \(q^{-4}\), and apply \(U_5\). The first identity in (1) gives
\[
\sum_{n\ge0}A_{5,k}(5n+4)q^n
\equiv45E(q)^{2125+3000a}E(q^5)^{-41}\pmod{625}.
\]
The prefactor has 5-adic valuation one, so (2) applied modulo \(125\) to the remaining exponent \(125(17+24a)\) yields
\[
\sum_{n\ge0}A_{5,396+625a}(5n+4)q^n
\equiv45E(q^5)^{384+600a}\pmod{625}.
\tag{3}
\]
Consequently the four target progressions are divisible by \(625\) for all \(i\equiv3\pmod5\).

**2. A second lift for one quarter of those parameters.** Let \(i=13+25b\), hence \(k=1646+3125b\). The same procedure, now using (2) modulo \(3125\), gives
\[
F(q)^k\equiv E(q^5)^{7605+15000b}E(q)^{1479}\pmod{3125}.
\]
The second identity in (1) then yields
\[
\sum_{n\ge0}A_{5,k}(5n+4)q^n
\equiv1920E(q)^{9375+15000b}E(q^5)^{-291}\pmod{3125}.
\]
Since \(1920=5\cdot384\), use (2) modulo \(625\) on the exponent \(625(15+24b)\) to obtain
\[
\sum_{n\ge0}A_{5,k}(5n+4)q^n
\equiv1920E(q^5)^{1584+3000b}\pmod{3125}.
\tag{4}
\]
For each \(r\in R\), the exponent \((r-4)/5\) is one of \(1,2,3,4\) modulo five. Thus (4) proves the common fifth-power divisibility on all four progressions, for every \(b,n\ge0\).

**3. Exact coefficient obstructions.** Write \(a_m(k)=[q^m]F(q)^k\), with \(a_0(k)=1\). Formal logarithmic differentiation gives the exact *integer* recurrence
\[
m\,a_m(k)=k\sum_{j=1}^m
\left(\sigma_1(j)-25\mathbf1_{5\mid j}\sigma_1(j/5)\right)a_{m-j}(k),
\tag{5}
\]
where \(\sigma_1(j)\) is the sum of positive divisors of \(j\). The six base values and increments calculated with (5) imply, for every nonnegative \(i,a,b\),
\[
\begin{aligned}
a_9(21+125i)&\equiv125(3-i)\pmod{625},\\
a_9(396+625a)&\equiv625(2-a)\pmod{3125},\\
a_9(1646+3125b)&\equiv3125(3-b)\pmod{15625},\\
a_{14}(1646+3125b)&\equiv3125(3+b)\pmod{15625}.
\end{aligned}
\tag{6}
\]
To justify these as identities for *all* parameters, rather than just five tested residues, note that the coefficients of \(F(q)^{5^t}-1\) through degree fourteen are divisible by \(5^{t-1}\) for \(t=3,4,5\). This follows from (2) and the fact that the first potentially lower-valuation terms in \(E(q^5)^{24\cdot5^{t-1}}\) occur only at degree at least \(25\). Thus, through degree fourteen, the binomial identity \((1+B)^h\equiv1+hB\) holds modulo \(5^{t+1}\) for each of these three values of \(t\); its terms of order two are divisible by \(5^{2t-2}\), at least \(5^{t+1}\). The residue formulas follow by evaluating (5) at the six displayed base/next parameter values. The code includes these exact integer checks.

When \(i\not\equiv3\pmod5\), the first line of (6) has valuation exactly three, matching the known lower bound. If \(i=3+5a\) but \(a\not\equiv2\pmod5\), the second line has valuation exactly four, matching (3). Finally, for \(i=13+25b\), the last two lines cannot both vanish modulo \(15625\): their normalized residues are \(3-b\) and \(3+b\), which have no common zero modulo five. They have valuation at least five by (4), and at least one has valuation exactly five. Hence the common exponent is *exactly* five in this final stratum. These three cases exhaust all \(i\ge0\), completing the proof.

## Verification

Run the standalone standard-library-only checker with `python3 check.py`. It verifies both complete polynomial identities in (1) from the modular-equation recurrence and all six low-degree integer coefficients needed for (6), with additional residue checks. Its success marker is `FIVE_CORE_SHARP_5ADIC_CERTIFICATE_OK 1479 6 15`. The checker does not attempt an exhaustive search over the infinite index ranges: the infinite statements are proved by the formal-series operations, binomial lifting, and parameter linearization above.

## Relationship to prior work

Maity's October 31, 2026 preprint (Theorem 3.1) establishes modulus \(125\) across exactly these four progressions. An earlier exact first-lift result had already established modulus \(625\) when \(i\equiv3\pmod5\), even with the explicit dissection (3); neither of these facts is claimed as new. The additional modulus \(3125\) on \(i\equiv13\pmod{25}\), together with the pairwise obstruction stopping all further *common* lifting and the complete exact-depth classification, is the distinct contribution here. Liang–Tang treat primarily fixed tuple orders up to twenty-five, and Tang's earlier conjectures have the lower common modulus. The 2026 polynomial-weight congruences of Ananya–Keerthana–Ranganatha do not have this combined parameter and progression configuration. A more general unindexed formal congruence could potentially imply this result, and should be considered in independent priority assessment.

## Limitations

No assertion is made about the largest exponent separately for each of the four residue classes, nor about other tuple-order progressions. The proof uses the established fifth-order modular equation and its integer recurrence as a cited ingredient. Numerical or finite recurrence verification alone does not prove the infinite congruences. The exact classification is argued within this note; no independent mathematical audit has been performed.

## References

1. S. Maity, *On Certain Congruences for Partition \(k\)-Tuples with \(5\)-Cores*, arXiv:2611.00693 (first public version October 31, 2026), Theorem 3.1 and Lemma 2.2, https://arxiv.org/abs/2611.00693.
2. D. Tang, *An iterative approach for proving congruences of partition k-tuples with t-cores*, J. Ramanujan Math. Soc. **40** (2025), 245–256, https://www.mathjournals.org/jrms/2025-040-003/2025-040-003-004.html.
3. X. Liang and D. Tang, *Congruences modulo powers of 5 for partition k-tuples with 5-cores*, Proc. Edinburgh Math. Soc. **68** (2025), 1245–1261, https://doi.org/10.1017/S0013091525000215.
4. S. Ananya, G. Kavya Keerthana, and D. Ranganatha, *Partition k-tuples with 5-cores modulo powers of 5*, Bol. Soc. Mat. Mex. **32** (2026), Paper 72, https://doi.org/10.1007/s40590-026-00901-5.
5. A previously reported fifth-dissection formula for the tuple-order family \(396+625a\), whose exact modulus-\(625\) identity is independently derived in (3).
