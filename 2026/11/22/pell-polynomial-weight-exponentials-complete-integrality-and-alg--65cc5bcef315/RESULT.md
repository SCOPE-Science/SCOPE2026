# Pell polynomial-weight exponentials: complete integrality and algebraic-degree spectra

## Finding

Let the Pell integers satisfy \(U_0=0\), \(U_1=1\), and \(U_{n+2}=2U_{n+1}+U_n\). For every \(P(T)\in\mathbb Z[T]\), define the formal exponential
\[
\mathcal E_P(x)=\exp\!\left(\sum_{n\ge1}\frac{P(U_n)}{n}x^n\right)\in1+x\mathbb Q[[x]].
\]

**Complete integrality criterion.** The coefficients of \(\mathcal E_P\) are all integers if and only if
\[
P(T)=P(-T)\quad\text{and}\quad P(0)\equiv P(1)\pmod2.
\]
Equivalently, there exist \(c\in\mathbb Z\) and \(A,B\in\mathbb Z[Y]\) such that
\[
P(T)=c+2T^2A(T^2)+T^2(T^2-1)B(T^2).
\]

**Complete algebraic-degree criterion.** The series \(\mathcal E_P\) is algebraic over \(\mathbb Q(x)\) if and only if \(P\) is even. Write an even \(P\) as \(P(T)=c_0+\sum_{j=1}^{J}c_jT^{2j}\), with \(c_j\in\mathbb Z\), and put \(\nu_2(0)=+\infty\). Then
\[
H(P)=\max\bigl(\{0\}\cup\{3j-\nu_2(c_j):1\le j\le J,\ c_j\ne0\}\bigr),
\qquad
[\mathbb Q(x,\mathcal E_P):\mathbb Q(x)]=2^{H(P)}.
\]
This power of two is also the least positive \(D\) for which \(\mathcal E_P^D\in\mathbb Q(x)\).

In particular, for every \(k\ge1\), the least positive integer \(c\) making \(\mathcal E_{cT^{2k}}\) integral is \(c=2\), and
\[
[\mathbb Q(x,\mathcal E_{2T^{2k}}):\mathbb Q(x)]=2^{3k-1}.
\]
For any nonzero integer \(c\) and \(k\ge1\), \(\mathcal E_{cT^{2k-1}}\) is not integral and is transcendental over \(\mathbb Q(x)\). These facts establish all three families of Pell-series integrality conjectures recorded in OEIS A208034.

## Assumptions and scope

All polynomials have integer coefficients; the variable \(x\) is formal. Integrality refers to the coefficients in \(\mathbb Z[[x]]\). Algebraic degree is over \(\mathbb Q(x)\). The parity and degree conditions apply to *all* such polynomials, not merely to monomials. A rational series has degree one. The statement uses the ordinary Pell sequence, not the higher-order generalized Pell sequences and not index-substituted sequences \(U_{n^s}\).

Set
\[
\alpha=1+\sqrt2,\quad\beta=1-\sqrt2,\quad\alpha\beta=-1,\quad \Delta=(\alpha-\beta)^2=8,
\]
and \(V_n=\alpha^n+\beta^n\). Thus \(U_n=(\alpha^n-\beta^n)/(2\sqrt2)\) and \(V_0=V_1=2\), \(V_{n+2}=2V_{n+1}+V_n\).

## Proof

**1. The prime-power integrality test.** For any integers \(b_n\), the Dold–Euler criterion states that \(\exp(\sum_{n\ge1}b_nx^n/n)\in\mathbb Z[[x]]\) if and only if, for every prime \(p\), \(r\ge1\), and \(m\ge1\) with \(p\nmid m\),
\[
b_{mp^r}\equiv b_{mp^{r-1}}\pmod{p^r}.\tag{1}
\]
This is the standard Euler-product/Möbius inversion criterion, also reproduced as Corollary 2.3 of Li–Zhong–Zhou.

**2. Every odd prime is good for squares.** The Binet identity is
\[
8U_n^2=V_{2n}-2(-1)^n.\tag{2}
\]
Let \(M=\begin{pmatrix}2&1\\1&0\end{pmatrix}\) and \(C=M^2\). Since \(V_{2n}=\operatorname{tr}(C^n)\), the elementary integral-matrix trace congruence gives \(V_{2mp^r}\equiv V_{2mp^{r-1}}\pmod{p^r}\) for every prime \(p\). It follows, when \(p\) is odd, that the two parity terms in (2) agree and \(8\) is invertible modulo \(p^r\); hence
\[
U_{mp^r}^2\equiv U_{mp^{r-1}}^2\pmod{p^r}.\tag{3}
\]
Consequently (1) holds at every odd prime for any even polynomial \(P(T)=Q(T^2)\).

**3. The entire dyadic obstruction.** The recurrence for \(V_n\), initialized at \(V_0=V_1=2\), shows inductively that \(V_n\equiv2\pmod4\) for all \(n\ge0\). The doubling identity \(U_{2n}=U_nV_n\) therefore yields \(\nu_2(U_{m2^r})=r\) for every odd \(m\) and \(r\ge0\), because \(U_m\) is odd exactly when \(m\) is odd. For \(r\ge2\), the squares at indices \(m2^r\) and \(m2^{r-1}\) are both divisible by \(2^r\), so (1) holds for every even \(P\). For \(r=1\), (1) holds exactly when \(Q(0)\equiv Q(1)\pmod2\). Necessity already follows at \(m=1\) from \(U_1=1\) and \(U_2=2\). Thus the dyadic condition is exactly \(P(0)\equiv P(1)\pmod2\).

**4. An integral weight must be even.** Infinitely many primes satisfy \(p\equiv3\pmod8\) (Dirichlet); for these, \(2\) is a quadratic nonresidue. Modulo such a prime, Frobenius interchanges \(\alpha\) and \(\beta\), so \(U_{mp}\equiv-U_m\pmod p\). If \(\mathcal E_P\) is integral, (1) with \(r=1\) implies \(P(-U_m)\equiv P(U_m)\pmod p\) for infinitely many primes, for every fixed \(m\). Therefore \(P(-U_m)=P(U_m)\) over the integers. As \(U_m\) assumes infinitely many distinct values, \(P(T)=P(-T)\). Parts 2–4 prove the integrality criterion.

To see the alternative polynomial form, set \(P(T)=Q(T^2)\) and \(c=Q(0)\). Since \(Q(1)-c\) is even, the polynomial \((Q(Y)-c)/Y\) has even value at \(Y=1\), and polynomial division by \(Y-1\) gives \(Q(Y)-c=2YA(Y)+Y(Y-1)B(Y)\) with integral \(A,B\). The converse is immediate.

**5. Rational powers for even polynomials.** For \(j\ge1\) the exact Binet expansion is
\[
8^jU_n^{2j}=\sum_{t=0}^{2j}(-1)^t\binom{2j}{t}\bigl(\alpha^{2j-t}\beta^t\bigr)^n.\tag{4}
\]
For an even \(P\), put \(D=2^{H(P)}\). Then \(Dc_j/8^j\in\mathbb Z\) for every \(j\ge1\). Formal integration of (4) and exponentiation express \(\mathcal E_P^D\) as an integral-exponent product of linear factors \(1-\alpha^{2j-t}\beta^t x\), together with \((1-x)^{-Dc_0}\). Conjugation \(\alpha\leftrightarrow\beta\) pairs the factors and preserves their exponents, so their product belongs to \(\mathbb Q(x)\).

If \(H(P)>0\), choose the largest \(j_0\) with \(3j_0-\nu_2(c_{j_0})=H(P)\). In \(\mathbb Q(\sqrt2)(x)\), at the linear factor \(1-\alpha^{2j_0}x\), the contribution from \(j_0\) has valuation \(-Dc_{j_0}/8^{j_0}\), which is odd. No smaller \(j\) contributes there because its spectral roots have smaller absolute value. Every larger \(j\) contributes an *even* integer valuation, since its 2-adic deficit is smaller than \(H(P)\). Hence \(\mathcal E_P^D\) has odd valuation at this place. Because \(D\) is a power of two, the binomial equation \(Y^D=\mathcal E_P^D\) has degree exactly \(D\) over \(\mathbb Q(\sqrt2)(x)\): a rational function with odd valuation cannot be a proper power, and its binomial defines a totally ramified extension of degree \(D\). It follows that \([\mathbb Q(x,\mathcal E_P):\mathbb Q(x)]=D\). The same valuation shows that no smaller positive power of \(\mathcal E_P\) lies in \(\mathbb Q(x)\). If \(H(P)=0\), the series itself is rational.

**6. Odd terms force transcendence.** If \(P\) is not even, let \(d\) be its highest odd exponent with nonzero coefficient \(a_d\). By Binet expansion, the rational function
\[
\frac{\mathcal E_P'(x)}{\mathcal E_P(x)}=\sum_{n\ge1}P(U_n)x^{n-1}\in\mathbb Q(\sqrt2)(x)
\]
has, at \(x=\alpha^{-d}\), residue \(-a_d/(2\sqrt2)^d\), an irrational algebraic number. No other term has the same spectral root: even powers give only even powers of \(\alpha\), and smaller odd powers have smaller absolute spectral roots. If \(\mathcal E_P\) were algebraic over \(\mathbb Q(x)\), its local Puiseux expansion would force every residue of its logarithmic derivative to be a rational order of vanishing or pole. This contradiction proves transcendence.

**7. Explicit rational powers.** For every \(k\ge1\), set \(G_k=\mathcal E_{2T^{2k}}\) and \(D_k=2^{3k-1}\). From (4),
\[
G_k(x)^{D_k}=\bigl(1-(-1)^kx\bigr)^{(-1)^{k+1}\binom{2k}{k}}
\prod_{t=0}^{k-1}\bigl(1-(-1)^tV_{2(k-t)}x+x^2\bigr)^{(-1)^{t+1}\binom{2k}{t}}.\tag{5}
\]
In particular,
\[
G_1^4=\frac{(1+x)^2}{1-6x+x^2},\qquad
G_2^{32}=\frac{(1+6x+x^2)^4}{(1-34x+x^2)(1-x)^6}.
\]
The pole of the first conjugate pair has valuation \(-1\), establishing the exact degree. At the smallest modulus, (1) for the weights \(cU_n^{2k}\) gives \(cU_2^{2k}\equiv cU_1^{2k}\pmod2\), which holds only when \(c\) is even; the sufficiency was proved above. A nonzero odd power is excluded by part 4.

## Verification

Run `python3 checker.py` with a standard Python 3 interpreter. The program independently computes the Pell and trace recurrences, checks prime-power Dold congruences for several nontrivial even polynomial weights, constructs their exponential coefficients by exact integer arithmetic, checks the OEIS A208034 initial coefficients, checks the exact logarithmic derivatives of (5), and verifies first dyadic obstructions. It reports 2,917 finite exact congruence/identity tests plus seven integral series through \(x^{36}\). These checks are finite consistency evidence only; the infinite quantifiers and algebraic degrees are proved in parts 1–7.

## Relationship to prior work

Li, Zhong, and Zhou (arXiv:2611.16283, first posted November 12, 2026) prove the corresponding polynomial-weight classification and specific algebraic-degree results for the **Fibonacci** sequence; their article does not treat the Pell sequence. Their Dold–Euler criterion is used here, but the dyadic local obstruction and the exact Pell degree spectrum are separately established. OEIS A208034 records the \(k=1\) Pell series and expressly formulates the three all-\(k\) statements as conjectures. Byszewski, Graff, and Ward survey general Dold sequences and integer matrix traces; Minton classifies the broad linear-recurrence/Gauss-congruence setting. Those general criteria motivate the argument but do not state the all-polynomial Pell criterion with the explicit \(2\)-adic algebraic degrees. An earlier implicit specialization in broad recurrence literature remains a possibility.

## Limitations

This theorem concerns ordinary Pell numbers and integer polynomial weights only, not arbitrary Lucas recurrences or other rings. It does not assert transcendence measures or coefficient asymptotics. Exact algebraic degrees are proved without a claim of independent external verification. The available OEIS text was indexed rather than read through a working direct full-text endpoint; a broader unpublished or unindexed statement could exist. Finite checker tests do not replace the infinite proof.

## References

- J. Li, Y. Zhong, Y. Zhou, *Integral Exponential Series: Fibonacci Weights and Implicit Equations*, arXiv:2611.16283v2, §2–4, https://arxiv.org/html/2611.16283v2 (first public version November 12, 2026).
- OEIS A208034, *Generating function with Pell-square exponential weights* and three all-power conjectures, https://oeis.org/A208034.
- J. Byszewski, G. Graff, T. Ward, *Dold sequences, periodic points, and dynamics*, Bull. London Math. Soc. 53 (2021), 1263–1298, https://doi.org/10.1112/blms.12531, especially §§2 and 4.
- G. T. Minton, *Linear recurrence sequences satisfying congruence conditions*, Proc. Amer. Math. Soc. 142 (2014), 2337–2352, https://doi.org/10.1090/S0002-9939-2014-12168-X.
