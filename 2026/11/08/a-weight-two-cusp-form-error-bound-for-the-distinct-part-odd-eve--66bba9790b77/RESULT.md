# A weight-two cusp-form error bound for the distinct-part odd-even sum

## Finding

Let \(Q(n)\) be the number of partitions of \(n\) into distinct positive parts, and let \(D(n)\) be the sum, over these partitions, of (total odd parts minus total even parts), where 'odd' and 'even' refer to the sizes of parts. For all integers \(n\ge0\), define \(C(n)=Q(n)-8D(n)\). Then
\[
F(z):=\frac{\eta(24z)^7}{\eta(48z)^3}
=\sum_{n\ge0} C(n)e^{2\pi i(24n+1)z}
\]
is a holomorphic cusp form of weight \(2\) on \(\Gamma_0(1152)\) with nebentypus \(\chi_8(d)=(2/d)\) for odd \(d\) coprime to \(1152\). Consequently, for every \(\varepsilon>0\),
\[
D(n)=\frac{Q(n)}8+O_\varepsilon\big((n+1)^{1/2+\varepsilon}\big)
\quad(n\ge0).
\]
In particular \(D(n)/Q(n)\to1/8\), and \(D(n)>0\) for all sufficiently large \(n\). The error is polynomial in \(n\) although the main term grows exponentially.

## Assumptions and scope

Partitions have positive, pairwise distinct integer parts. The empty partition contributes \(Q(0)=1\), \(D(0)=0\). Write \(f_r(q)=\prod_{j\ge1}(1-q^{rj})\) and \(\eta(z)=e^{\pi iz/12}\prod_{j\ge1}(1-e^{2\pi ijz})\), for \(\operatorname{Im}z>0\). The bound's implied constant may depend on \(\varepsilon\), not on \(n\). The exponent \(1/2+\varepsilon\) is not asserted to be individually optimal. No explicit finite threshold for positivity is asserted.

## Proof

**1. Exact correction series.** Baruah and Gogoi's published identity (Theorem 1.1, equation (1.2) of arXiv:2602.20025) states
\[
\sum_{n\ge0}D(n)q^n=\frac18\left(\frac{f_2(q)}{f_1(q)}-\frac{f_1(q)^7}{f_2(q)^3}\right).
\]
Since \(f_2/f_1=\prod_{j\ge1}(1+q^j)=\sum_{n\ge0}Q(n)q^n\), it follows coefficientwise that
\[
\sum_{n\ge0}C(n)q^n=\frac{f_1(q)^7}{f_2(q)^3}.
\]
Substituting \(q=e^{2\pi i24z}\) gives the asserted eta quotient, because its eta prefactor is \(e^{2\pi iz(24\cdot7-48\cdot3)/24}=e^{2\pi iz}\).

**2. Modularity.** For \(F=\eta(24z)^7\eta(48z)^{-3}\), the nonzero exponents are \(r_{24}=7\) and \(r_{48}=-3\); the candidate level is \(N=1152\) and the weight is \((7-3)/2=2\). The eta-quotient congruence conditions are
\[
\sum_{\delta\mid N}\delta r_\delta=24,
\qquad
\sum_{\delta\mid N}(N/\delta)r_\delta=264,
\]
both divisible by \(24\). The nebentypus parameter is
\[
\prod_{\delta\mid N}\delta^{r_\delta}=24^7/48^3=2^9 3^4,
\]
whose Kronecker character for odd \(d\) is \((2/d)=\chi_8(d)\).

For every positive \(c\mid1152\), the eta-quotient cusp-order formula gives
\[
\operatorname{ord}_{1/c}(F)=
\frac{1152}{24c\gcd(c,1152/c)}
\left(\frac{7\gcd(c,24)^2}{24}-\frac{3\gcd(c,48)^2}{48}\right).
\]
Put \(u=\gcd(c,24)\) and \(v=\gcd(c,48)\). Either \(v=u\) or \(v=2u\). In the former case the parenthesis is \(11u^2/48>0\); in the latter it is \(u^2/24>0\). Thus all cusps have positive order. The eta-quotient modularity and cusp criteria yield \(F\in S_2(\Gamma_0(1152),\chi_8)\).

**3. Coefficient bound.** The standard newform decomposition of any fixed-level holomorphic cusp form, together with the Ramanujan--Petersson bound for weight-two Hecke eigenforms, yields for every \(\varepsilon>0\) the coefficient estimate \(a_F(m)=O_\varepsilon(m^{1/2+\varepsilon})\). Indeed, normalized newform coefficients at all indices are bounded by a divisor-type factor times \(m^{1/2}\), and a finite combination of oldforms inherits this bound. Taking \(m=24n+1\) proves \(C(n)=O_\varepsilon((n+1)^{1/2+\varepsilon})\). The definition of \(C(n)\) proves the displayed asymptotic.

Finally, the standard asymptotic for partitions into distinct parts is
\[
Q(n)\sim\frac{\exp(\pi\sqrt{n/3})}{4\,3^{1/4}n^{3/4}}.
\]
Hence \(C(n)/Q(n)\to0\), proving the ratio and eventual positivity.

## Verification

The included independent finite checker computes \(Q(n)\) and \(D(n)\) by adding each allowed distinct part with an odd/even signed part-weight accumulator. Separately it computes coefficients of \(f_1^7/f_2^3\) by an exact logarithmic-derivative recurrence. It verifies \(Q(n)-8D(n)=C(n)\) for all \(0\le n\le1100\), the two modularity congruences, and positive orders at every divisor denominator of \(1152\) (24 possibilities). The checker is not a proof of the infinite assertion; the modular form argument is the proof.

To reproduce, run `python3 verify.py`; its output is recorded in `VERIFICATION_OUTPUT.txt`. The code uses only the Python standard library.

## Relationship to prior work

Andrews and Ghosh Dastidar introduced this distinct-part statistic and its generating series. Baruah and Gogoi established the exact two-quotient formula, which is used here verbatim; that identity is **not** claimed to be new. The additional observation is that the correction is a *weight-two cusp form* with strictly positive cusp orders, providing the polynomial coefficient bound and the asymptotic \(1/8\) law. The related 2026 papers of Bardhan--Saikia and other partition-congruence authors study identities, congruences, and monotonicity, not this cusp-form error estimate. The modularity test and Ramanujan--Petersson theorem are classical tools, not new claims.

## Limitations

This result does not prove an explicit least positivity index or an optimal coefficient exponent. The original generating identity is published; the newly claimed work is specifically its modular error estimate and asymptotic consequence. Standard modular-form theory is invoked, not reproved from first principles. The finding has only self-review; independent mathematical audit and full historical-priority certification have not occurred. An unindexed earlier derivation remains possible.

## References

1. N. D. Baruah and P. Gogoi, *Arithmetic properties of DSOME function*, arXiv:2602.20025 (first public 2026-02-20), Theorem 1.1, https://arxiv.org/abs/2602.20025.
2. G. E. Andrews and M. Ghosh Dastidar, *p(5n+4) again*, Ramanujan Journal 69, article 26 (2026), https://doi.org/10.1007/s11139-025-01280-7.
3. G. Bardhan and N. Saikia, *Some new congruences and identities for SOME(n), DSOME(n), overlined SOME(n) functions and analogues*, arXiv:2606.31264, https://arxiv.org/abs/2606.31264.
4. *Proofs of the Conjectures on SOME(n) and DSOME(n) Functions Related to Integer Partitions*, arXiv:2608.08524, https://arxiv.org/abs/2608.08524.
5. Classical eta-quotient modularity and cusp-order criteria (Newman--Gordon--Hughes and Ligozat); classical Ramanujan--Petersson bound for holomorphic newforms (Deligne); standard distinct-part partition asymptotic.
