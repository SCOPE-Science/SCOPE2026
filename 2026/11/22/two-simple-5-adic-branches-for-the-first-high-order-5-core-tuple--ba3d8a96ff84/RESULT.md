# Two simple \(5\)-adic branches for the first high-order 5-core tuple coefficient

## Finding

Let \(A_{5,k}(n)\) count ordered \(k\)-tuples of 5-core partitions with total size \(n\). Define
\[
B(i)=A_{5,111+125i}(39),\qquad i\in\mathbb Z_{\ge0}.
\]
There exist **exactly two** roots \(\alpha,\beta\in\mathbb Z_5\) of the normalized polynomial \(B(X)/5^4\), with
\[
\alpha\equiv0\pmod5,\qquad \beta\equiv4\pmod5.
\]
Both roots are simple, and, for every nonnegative integer \(i\),
\[
\boxed{\nu_5(B(i))=4+\nu_5(i-\alpha)+\nu_5(i-\beta).}
\]
In particular, for every integer \(t\ge1\), **exactly two residue classes modulo \(5^t\)** have \(5^{4+t}\mid B(i)\). Their representatives are the unique Hensel lifts of \(0\) and \(4\) modulo five. The density of parameters with \(\nu_5(B(i))=4\) is \(3/5\); the density with \(\nu_5(B(i))=4+e\) is \(8/5^{e+1}\) for each \(e\ge1\).

## Assumptions and scope

A 5-core partition has no hook length divisible by five; the empty partition is allowed. For positive integer \(k\), the known generating function is
\[
\sum_{n\ge0}A_{5,k}(n)z^n=F(z)^k,\qquad F(z)=\frac{E(z^5)^5}{E(z)},\quad E(z)=\prod_{m\ge1}(1-z^m).
\]
The first index of the four progressions in Maity's \(5^4\)-congruence for \(k=111+125i\) is \(39\), corresponding to its progression with residue \(39\pmod{125}\). All valuations are the usual valuations of nonzero integers or elements of \(\mathbb Q_5\). The result concerns **one exact coefficient**, not a sufficient criterion for lifting *all* coefficients in any progression.

## Proof

Write \(\sigma_1(m)=\sum_{d\mid m}d\), with \(\sigma_1(u)=0\) when \(u\) is not a positive integer. Logarithmic differentiation of the generating function gives
\[
z\frac{d}{dz}\log F(z)=\sum_{m\ge1}b_mz^m,\qquad
b_m=\sigma_1(m)-25\,\mathbf 1_{5\mid m}\sigma_1(m/5).
\]
For \(n\ge0\), put \(R_n(X)=[z^n]F(z)^{111+125X}\in\mathbb Q[X]\). Coefficient comparison proves the **exact polynomial recurrence**
\[
R_0(X)=1,\qquad nR_n(X)=(111+125X)\sum_{m=1}^n b_mR_{n-m}(X),\quad 1\le n\le39.
\]
This is a finite recurrence in rational polynomials, not an extrapolation from numerical interpolation.

Write \(R_{39}(X)=\sum_{j=0}^{39}c_jX^j\). Exact rational arithmetic using the displayed recurrence gives the finite certificate
\[
\nu_5(c_0)=5,\quad \nu_5(c_1)=\nu_5(c_2)=4,\quad
5^{-4}c_1\equiv5^{-4}c_2\equiv3\pmod5,
\]
\[
\nu_5(c_j)\ge6\quad(3\le j\le39).
\]
The standalone `verify.py` regenerates and checks all forty coefficients using rational integer arithmetic; it also checks several full coefficient values by an independent finite Euler-product expansion. These finite identities are the only computation-dependent part of the proof.

Therefore \(P(X)=5^{-4}R_{39}(X)\in\mathbb Z_5[X]\) and
\[
P(X)\equiv3X(X+1)\pmod5.
\]
The two roots \(0,4\) modulo five are simple, since \(P'(X)\equiv3(2X+1)\pmod5\) is nonzero at both. Hensel's lemma gives unique lifts \(\alpha\in5\mathbb Z_5\), \(\beta\in4+5\mathbb Z_5\), and excludes all other roots in \(\mathbb Z_5\).

If \(i\equiv\alpha\pmod5\), the polynomial difference quotient
\((P(i)-P(\alpha))/(i-\alpha)\) is a 5-adic unit because its reduction is \(P'(0)=3\). Hence \(\nu_5(P(i))=\nu_5(i-\alpha)\). The identical argument applies to the \(\beta\)-branch, with reduction \(P'(4)=2\). For the three other residue classes modulo five, \(P(i)\) is a unit. Exactly one of \(i-\alpha\), \(i-\beta\) can be divisible by five, yielding the boxed valuation identity. Finally \(A_{5,111+125i}(39)>0\): assign the one-box 5-core partition to 39 distinct components, so no value vanishes.

Each root lifts to one class modulo every \(5^t\), proving the two-class assertion and, by subtraction of tail densities, the exact valuation densities.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. It regenerates the degree-39 polynomial, checks the 5-adic coefficient certificate, independently expands the truncated Euler product for eight tuple orders, and confirms uniqueness of the two lifted roots to precision \(5^8\). The proof of the valuation law is the finite coefficient certificate **plus** Hensel's lemma; isolated numerical checks alone would not prove it. The two roots reduce modulo \(5^6\) to \(1980\) and \(249\), respectively.

## Relationship to prior work

Maity, *On Certain Congruences for Partition \(k\)-Tuples with \(5\)-Cores* (arXiv:2611.00693v1, first posted 2026-10-31), Theorem 3.3, proves \(A_{5,111+125i}(125n+r)\equiv0\pmod{5^4}\) for \(r\in\{39,64,89,114\}\). It does not determine exact valuations as a function of the tuple-order parameter or the number of lifting classes. The present result identifies both 5-adic root branches at the **first index of one such progression**, giving a sharp necessary restriction on any proposed higher-modulus congruence across the full progression.

Earlier work of Tang (2025) describes an iterative congruence method; Liang and Tang (2025) treat other tuple-order ranges. Related exact saturation results for a distinct family \(k=21+125i\) concern a common valuation bound across four progressions; such a bound does not imply the present two-root coefficient law. The methods of polynomial parameterization and Hensel lifting are standard; the finite coefficient identity and the exact two-root profile for this natural parameter family are the object-specific contribution.

## Limitations

No full-progression improvement beyond Maity's theorem is asserted. Two residue classes satisfy the higher divisibility of the *index-39 coefficient*, but further coefficients may obstruct the same lift uniformly. Independent mathematical audit has not been performed. A potentially relevant older full-text article by Tang was inaccessible through the available journal interface, so implicit prior coverage remains a possibility. The result does not classify all coefficient valuations for arbitrary \(n\).

## References

1. S. Maity, *On Certain Congruences for Partition \(k\)-Tuples with \(5\)-Cores*, arXiv:2611.00693v1 (2026), https://arxiv.org/html/2611.00693v1.
2. D. Tang, *An iterative approach for proving congruences of partition k-tuples with t-cores*, Journal of the Ramanujan Mathematical Society **40** (2025), 245–256, https://www.mathjournals.org/jrms/2025-040-003/2025-040-003-004.html.
3. X. Liang and D. Tang, *Congruences modulo powers of 5 for partition k-tuples with 5-cores*, Proceedings of the Edinburgh Mathematical Society **68** (2025), 1245–1261, https://doi.org/10.1017/S0013091525000215.
4. F. G. Garvan, D. Kim and D. Stanton, *Cranks and t-cores*, Inventiones Mathematicae **101** (1990), 1–17.
