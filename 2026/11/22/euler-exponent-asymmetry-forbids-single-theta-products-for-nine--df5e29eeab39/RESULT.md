# Euler-exponent asymmetry forbids single theta products for nine-color components modulo \(19\)

## Finding

Write \(\mathbb F_{19}\) for the field of nineteen elements, and define
\[
P_0(y)=\prod_{j\ge1}(1-y^{19j}),\qquad
P_a(y)=\prod_{j\ge0}(1-y^{a+19j})(1-y^{19-a+19j})\quad(1\le a\le9).
\]
Let \(p_9(n)\) count partitions with nine independent colors per positive part, and set
\[
D(y)=\prod_{a=1}^{9}P_a(y),\quad
\Phi_r(y)=\sum_{n\ge0}p_9(19n+r)y^n,\quad
B_r(y)=\frac{D(y)}{P_0(y)}\Phi_r(y)\in\mathbb F_{19}[[y]]
\]
for each \(r\in\{0,1,\ldots,18\}\). The equality involving \(B_r\) is in the coefficientwise reduction modulo \(19\).

**Theorem.** For each \(r\in\{0,1,\ldots,18\}\setminus\{17\}\), the series \(B_r\) is nonzero and there exist **no** \(c\in\mathbb F_{19}^{\times}\), \(s\in\mathbb Z_{\ge0}\), and integer exponents \(h_0,h_1,\ldots,h_9\) such that
\[
B_r(y)=c\,y^s\prod_{a=0}^{9}P_a(y)^{h_a}
\quad\text{in }\mathbb F_{19}[[y]].
\]
Thus none of the eighteen nonvanishing nine-color components in the Winquist dissection can be reduced to one monomial of the specified level-\(19\) theta factors, even allowing repeated factors, denominators and a scalar monomial shift. The known component \(B_{17}\) is zero and is excluded.

## Assumptions and scope

All products are formal power series over \(\mathbb F_{19}\); their constant coefficients are one, so integer negative powers are well-defined. A *single theta product* means exactly the multiplicative alphabet \(P_0,P_1,\dots,P_9\), with arbitrary integral powers, scalar and monomial shift. No claim is made about theta functions of other conductors or arbitrary sums of products. The series \(B_r\) is normalized as in Bilgici, Theorems 2.3 and 3.2, by multiplying the nine-color progression component by the common unit \(D/P_0\).

## Proof

**Step 1: a necessary paired-exponent identity.** For any formal unit \(U(y)\in1+y\mathbb F_{19}[[y]]\), the coefficients through degree \(18\) determine unique Euler exponents \(\epsilon_1(U),\dots,\epsilon_{18}(U)\in\mathbb F_{19}\) by
\[
U(y)\equiv\prod_{j=1}^{18}(1-y^j)^{\epsilon_j(U)}\pmod{y^{19}}.
\]
To prove uniqueness, remove factors in increasing order of \(j\), choosing the exponent that cancels the coefficient of \(y^j\). Equivalently, if \(L_n=[y^n]yU'(y)/U(y)\), formal differentiation and coefficient comparison give the exact recurrence
\[
\epsilon_n(U)=-n^{-1}\left(L_n+
\sum_{\substack{d\mid n\\d<n}}d\,\epsilon_d(U)\right),
\qquad 1\le n\le18.
\]
Every denominator is invertible in \(\mathbb F_{19}\), so no formal logarithm or division by \(19\) is involved.

For a monomial in the theta factors, \(P_0\equiv1\pmod{y^{19}}\), and for \(1\le a\le9\),
\[
P_a(y)\equiv(1-y^a)(1-y^{19-a})\pmod{y^{19}}.
\]
Consequently every such monomial unit \(U\) satisfies the nine necessary symmetries
\[
\epsilon_a(U)=\epsilon_{19-a}(U)\quad(1\le a\le9).
\tag{1}
\]
These equalities hold with arbitrary positive or negative integer powers, because only exponents modulo \(19\) enter degrees below \(19\).

**Step 2: exact finite calculation of the components.** The generating function is
\[
\sum_{n\ge0}p_9(n)q^n=\prod_{m\ge1}(1-q^m)^{-9}.
\]
To obtain \(B_r\) through degree \(19\), expand this product through degree \(379=19\cdot19+18\), take every nineteenth coefficient for each \(r\), and multiply by the truncation of \(D/P_0\). This is exact arithmetic in \(\mathbb F_{19}\): processing nine distinguishable copies of each part size \(m\le379\), the unbounded-coin recurrence updates the coefficient of \(q^n\) by the coefficient of \(q^{n-m}\), in ascending \(n\).

Let \(s_r=\operatorname{ord}_y B_r\), let \(c_r=[y^{s_r}]B_r\), and let \(U_r=c_r^{-1}y^{-s_r}B_r\). The calculation yields the following full obstruction table, with all displayed values in \(\mathbb F_{19}\):

| \(r\) | \(s_r\) | \(c_r\) | \(\epsilon_1(U_r)\) | \(\epsilon_{18}(U_r)\) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 15 | 4 |
| 1 | 0 | 9 | 14 | 15 |
| 2 | 0 | 16 | 14 | 4 |
| 3 | 0 | 8 | 15 | 15 |
| 4 | 0 | 9 | 4 | 1 |
| 5 | 0 | 10 | 0 | 15 |
| 6 | 1 | 15 | 1 | 0 |
| 7 | 0 | 6 | 1 | 2 |
| 8 | 0 | 6 | 0 | 1 |
| 9 | 0 | 7 | 0 | 9 |
| 10 | 0 | 9 | 16 | 11 |
| 11 | 0 | 9 | 4 | 7 |
| 12 | 0 | 13 | 14 | 9 |
| 13 | 1 | 3 | 0 | 8 |
| 14 | 0 | 7 | 0 | 12 |
| 15 | 0 | 15 | 0 | 1 |
| 16 | 0 | 18 | 6 | 3 |
| 18 | 0 | 14 | 4 | 0 |

All rows except \(r=3\) violate (1) already at the pair \(\{1,18\}\). At \(r=3\), the exact calculation additionally gives
\[
\epsilon_2(U_3)=10\ne18=\epsilon_{17}(U_3).
\]
Thus every nonzero \(B_r\) violates (1). If the asserted monomial factorization existed, its order and initial coefficient would force \(s=s_r\), \(c=c_r\), and its normalized unit to be \(U_r\), contradicting (1). This completes the proof.

## Verification

The included standalone `VERIFY.py` uses only standard Python integer arithmetic. It independently constructs the nineteen series \(B_r\) through \(y^{19}\) in two ways: directly from colored-partition coefficients and from the explicit two-quartic Winquist dissection in Bilgici's Theorem 2.3. It checks equality of all nineteen truncations, calculates and reconstructs the unique Euler exponent vectors, verifies every entry of the table, and confirms the exceptional discrepancy for \(r=3\). As a separate bounded cross-check, it excludes all \(715\) degree-four products with repetitions from the ten factors \(P_0,\dots,P_9\). Run `python3 VERIFY.py`; no external dependency or downloaded data is needed.

The infinite nonfactorization is logically established by a finite-degree obstruction to a purported formal-series identity. It does **not** infer an infinite conclusion from empirical sampling of a number-theoretic sequence.

## Relationship to prior work

Bilgici (2026) derives the nineteen components of the nine-color partition function modulo \(19\) as sums of two quartic theta products and explicitly asks in Section 8, Question 2, whether the two-term components can be reduced to single theta products using theta relations. The theorem here is a negative answer within exactly the stated factor alphabet, and is stronger than merely excluding four-factor positive products: any integer exponent vector and quotient are ruled out. Bilgici's two-term formulas and the previously known vanishing component are prerequisites, not new claims. Hirschhorn (2000) proves the analogous positive single-product phenomenon for modulus \(11\), a genuinely different modulus and partition family; it does not give a nonfactorization at modulus \(19\).

## Limitations

Only products of \(P_0,\dots,P_9\), with scalar monomial factors, are excluded. The proof does not rule out rewriting a component using an enlarged alphabet of theta functions, arbitrary additive sums, or modular objects outside this alphabet, nor does it resolve the other questions of Bilgici. Exact modular calculations are short and fully repeatable, but this finding has not undergone independent mathematical validation. A prior implicit presentation of this coefficient obstruction is possible and is a priority risk.

## References

1. Göksal Bilgici, *Nine-Colored Partition Components Modulo 19*, arXiv:2611.24516v1, first publicly submitted 2026-11-18, especially Theorems 2.3 and 3.2 and Section 8, Question 2. https://arxiv.org/html/2611.24516v1
2. Michael D. Hirschhorn, *Winquist and the Atkin–Swinnerton-Dyer partition congruences for modulus 11*, Australasian Journal of Combinatorics **22** (2000), 101–104. https://ajc.maths.uq.edu.au/pdf/22/ocr-ajc-v22-p101.pdf
