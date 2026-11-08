# Sharp two-coefficient recognition of mod-seven colored-odd partition congruences

## Finding

For every integer \(k\ge1\), let \(a_k(n)\) count integer partitions of \(n\) with one color on even parts and \(k\) colors on odd parts. The complete list of vanishing progressions at prime modulus seven is

\[
\forall n\ge0:\ a_k(7n+r)\equiv0\pmod7
\quad\Longleftrightarrow\quad
(k\bmod7,r)\in\{(0,3),(1,5),(3,2),(4,4),(5,6)\},
\]

for every \(r\in\{0,1,\ldots,6\}\). Equivalently—and with a **uniform, sharp finite stopping rule**—

\[
\left[\forall n\ge0:\ a_k(7n+r)\equiv0\pmod7\right]
\quad\Longleftrightarrow\quad
\left[a_k(r)\equiv a_k(r+7)\equiv0\pmod7\right].
\]

The five infinite positive congruence families are **previously known**, from Hirschhorn–Sellers, Theorem 1.3 and Corollary 4.1. The result here is their exhaustive converse over *all* positive color parameters and all seven progressions, and the sharp two-coefficient recognition theorem; it does not claim the published positive families as new.

## Assumptions and scope

All identities are in the formal power-series ring \(\mathbb Z[[q]]\), reduced coefficientwise modulo seven. Let

\[
 f_m(q)=\prod_{j\ge1}(1-q^{mj}),\qquad
 P(q)=f_1(q)^{-1},\qquad D(q)=\frac{f_2(q)}{f_1(q)}=\prod_{m\ge1}(1+q^m).
\]

The defining generating function is

\[
 F_k(q):=\sum_{n\ge0}a_k(n)q^n
 =\frac{f_2(q)^{k-1}}{f_1(q)^k}=P(q)D(q)^{k-1}.
\]

The colors are labeled and their multiplicities independent. The statement concerns prime modulus seven and step exactly seven; no claim is made for arbitrary prime powers, finer progressions, or another number of even-part colors.

## Proof

**1. Seven-color shift gives exact reduction to seven parameters.** In characteristic seven, the formal binomial identity \((1+x)^7\equiv1+x^7\pmod7\) applies to every factor of \(D(q)\). Hence

\[
 D(q)^7\equiv D(q^7)\pmod7,
 \qquad F_{k+7j}(q)\equiv F_k(q)D(q^7)^j\pmod7
\]

for each integer \(j\ge0\). For \(0\le r\le6\), define residue extraction

\[
 \mathcal E_r(F)(Q):=\sum_{n\ge0}[q^{7n+r}]F(q)\,Q^n.
\]

Then

\[
 \mathcal E_r(F_{k+7j})(Q)
 \equiv \mathcal E_r(F_k)(Q)D(Q)^j\pmod7.
\]

Since \(D(Q)^j\) has constant coefficient one, it is invertible over \(\mathbb F_7[[Q]]\). Therefore \(\mathcal E_r(F_{k+7j})=0\) identically modulo seven **if and only if** \(\mathcal E_r(F_k)=0\) identically. Every color number reduces to one representative \(k\in\{1,\ldots,7\}\), with seven representing zero modulo seven. Moreover, comparing the first two terms and using \(D(Q)^j\equiv1+jQ\pmod{Q^2}\) gives

\[
 a_{k+7j}(r)\equiv a_k(r),\qquad
 a_{k+7j}(r+7)\equiv a_k(r+7)+j\,a_k(r)\pmod7.
\]

Thus simultaneous vanishing of the first two coefficients is also invariant under seven-color shifts.

**2. Exhaustive first-two-coefficient table.** Exactly compute coefficients of \(F_k(q)\) through degree 13. The two independent methods in `verify.py` agree. Rows list the seven entries at indices 0 through 6, then those at indices 7 through 13, all modulo seven:

| \(k\) | \(a_k(0),\ldots,a_k(6)\) | \(a_k(7),\ldots,a_k(13)\) | common zero residues \(r\) |
| --- | --- | --- | --- |
| 1 | 1,1,2,3,5,0,4 | 1,1,2,0,0,0,3 | 5 |
| 2 | 1,2,4,1,0,3,5 | 1,2,0,1,1,0,0 | none |
| 3 | 1,3,0,2,4,5,0 | 1,0,0,2,0,5,1 | 2 |
| 4 | 1,4,4,0,0,6,5 | 0,4,1,2,0,0,5 | 4 |
| 5 | 1,5,2,3,0,4,0 | 2,0,2,3,1,4,0 | 6 |
| 6 | 1,6,1,5,3,3,5 | 1,2,2,0,3,3,5 | none |
| 7 | 1,0,1,0,2,0,3 | 1,5,1,0,2,4,3 | 3 |

The table is a **finite exact certificate for the negative cases**, not an inference from experimental vanishing to an infinite theorem. It supplies a nonzero coefficient among \(a_k(r),a_k(r+7)\) for each excluded pair; by the first step the same obstruction applies to every positive \(k\) in its residue class.

A short independently checkable integer-coefficient recurrence also certifies the table. Put \(\sigma(m)=\sum_{d\mid m}d\). Logarithmic differentiation of the defining product yields

\[
 n\,a_k(n)=\sum_{m=1}^{n}
 \bigl(k\sigma(m)-2(k-1)\mathbf1_{2\mid m}\sigma(m/2)\bigr)a_k(n-m),\quad n\ge1,
\]

with \(a_k(0)=1\). It uses only integer arithmetic and exact divisions. The independent implementation multiplies the colored-part geometric factors directly.

**3. Positive cases and completion of both directions.** Hirschhorn and Sellers proved in their Theorem 1.3 that \(a_1(7n+5)\), \(a_3(7n+2)\), \(a_4(7n+4)\), \(a_5(7n+6)\), and \(a_7(7n+3)\) are all divisible by seven for every \(n\ge0\). Their Corollary 4.1 extends them to every larger color number congruent modulo seven. Step 1 also establishes the transfer directly. These five cases exhaust the simultaneous zeros in Step 2, while every other pair has an explicit first- or second-coefficient obstruction. This proves the equivalence and classification for all \(k\ge1\), \(0\le r<7\).

**4. Optimality of two samples.** In the \(k=3\) row, \(a_3(6)\equiv0\pmod7\) whereas \(a_3(13)\equiv1\pmod7\). Therefore checking only the first term of every proposed progression would wrongly accept \((k,r)=(3,6)\); the two-sample cutoff is minimal uniformly over all parameters.

## Verification

Run `python3 verify.py` with the Python standard library. The certificate uses two different coefficient algorithms, compares 98 canonical coefficients, cross-checks the seven-color shift for 77 different base color counts through degree 27, reproduces the five admissible color/residue pairs, and checks the sharp one-sample counterexample. It prints `VERIFY_OK`. The unrestricted step relies on the formal identity and the fully stated published positive congruence theorem, not on extrapolating the finite checks.

## Relationship to prior work

Hirschhorn and Sellers [1, Theorem 1.3 and Corollary 4.1] already establish **all five positive congruence families and all their seven-color shifts**. The original content assessed here is only the missing negative converse across all \(7\times7\) residue possibilities and the optimal finite recognition rule. Their proof of the transfer is equivalent to the first half of Step 1 and is not new. Maity, Saikia and Talukdar [2, Theorem 1.1] subsequently extend three selected families to higher powers of seven, but do not supply a classification of all simple progressions modulo seven. Paksok and Saikia [3, Section 3] study related color-partition congruences at various other moduli; no equivalent exhaustive seven-class result was identified in the inspected sections.

## Limitations

The result is specifically for vanishing of an entire arithmetic progression modulo seven with step seven. It does not classify higher-power moduli, nonzero congruence constants, or arbitrary arithmetic steps. Its proof cites the pre-existing five positive congruences; the novelty claim is a *sharp converse and decision criterion*, not their rediscovery. The criterion is short once those results are available; historical priority for an earlier equivalent negative classification remains subject to expert checking. The complete proof is elementary and does not depend on the numerical cross-check alone.

## References

1. Michael D. Hirschhorn and James A. Sellers, *A Family of Congruences Modulo 7 for Partitions with Monochromatic Even Parts and Multi-Colored Odd Parts*, arXiv:2507.09752v1, first posted 2025-07-13; see Theorem 1.3 and Corollary 4.1. https://arxiv.org/abs/2507.09752
2. Saikat Maity, Manjil P. Saikia, and Prabal Talukdar, *Congruences modulo powers of 7 for partitions with colored odd parts*, arXiv:2610.35292v1, first posted 2026-10-26; see Theorem 1.1 and appendices. https://arxiv.org/abs/2610.35292
3. Adam Paksok and Nipen Saikia, *Some New Congruences For Partitions With Monochromatic Even Parts and Multichromatic Odd Parts*, Boletim da Sociedade Paranaense de Matemática 44 (2026), 1–11, DOI:10.5269/bspm.79605; see Section 3. https://doi.org/10.5269/bspm.79605
