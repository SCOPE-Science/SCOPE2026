# Complete algebraicity trichotomy for Fibonacci-polynomial exponentials

## Finding

Write \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). For **every** integer polynomial \(P\in\mathbb Z[T]\), define the formal series

\[
\mathcal E_P(x)=\exp\!\left(\sum_{n\ge1}\frac{P(F_n)}n x^n\right)\in1+x\mathbb Q[[x]].
\]

**Complete algebraicity classification.** The series \(\mathcal E_P\) is algebraic over \(\mathbb Q(x)\) **if and only if** \(P\) is even, meaning \(P(-T)=P(T)\). Every non-even \(P\) gives a transcendental formal power series over \(\mathbb Q(x)\).

For an even polynomial write \(P(T)=\sum_{j=0}^d c_jT^{2j}\) and set \(\nu_5(0)=+\infty\), and

\[
h(P)=\max\left(\{0\}\cup\{j-\nu_5(c_j):1\le j\le d,\ c_j\ne0\}\right).
\]

Then the **exact algebraic degree**, and the minimal positive rationalizing power, are

\[
[\mathbb Q(x,\mathcal E_P):\mathbb Q(x)]=5^{h(P)},
\qquad
\min\{m\ge1:\mathcal E_P^m\in\mathbb Q(x)\}=5^{h(P)}.
\]

In particular, \(\mathcal E_P\) is rational precisely when every \(c_j\) for \(j\ge1\) is divisible by \(5^j\). This is a complete classification for arbitrary integer polynomial weights, not only those whose exponential series has integral coefficients.

In the integral subfamily, the result combines with the integrality criterion in [1]: \(\mathcal E_P\in\mathbb Z[[x]]\) if and only if \(P\) is even and \(P(0)\equiv P(1)\equiv P(2)\pmod5\). For every \(d\ge3\), the polynomial \(P_d(T)=T^{2d}-T^{2d-4}\) meets this integrality criterion and produces degree **exactly** \(5^d\). Thus integer-coefficient series with no global factor of five in their weight polynomial realize unbounded powers of five as their algebraic degrees.

The first instance is \(P_3(T)=T^6-T^2\), for which

\[
\mathcal E_{P_3}(x)^{125}=
\frac{(1+7x+x^2)^6(1-3x+x^2)^{10}}{(1-18x+x^2)(1+x)^{30}},
\qquad
[\mathbb Q(x,\mathcal E_{P_3}):\mathbb Q(x)]=125.
\]

## Assumptions and scope

All polynomials have coefficients in \(\mathbb Z\), including possibly negative or zero coefficients. All series are formal at \(x=0\), with exponential constant term \(1\). Algebraic and transcendental always refer to the extension \(\mathbb Q(x)\subseteq\mathbb Q((x))\). The degree of a rational function is taken to be \(1\) as a field extension. The classification includes \(P=0\) and constant polynomials, for which \(h(P)=0\).

The source date of the motivating integrality and monomial-degree study [1] is November 12, 2026 (first arXiv submission); its primary classification is 11B83.

## Proof

**1. The rational-residue obstruction for every non-even polynomial.** Put

\[
\alpha=\frac{1+\sqrt5}{2},\quad\beta=\frac{1-\sqrt5}{2}=-\alpha^{-1},
\quad F_n=\frac{\alpha^n-\beta^n}{\sqrt5}.
\]

Expand \(P(T)=\sum_{k=0}^D a_kT^k\). By the binomial theorem,

\[
P(F_n)=\sum_{k=0}^D\frac{a_k}{(\sqrt5)^k}
\sum_{i=0}^k(-1)^i\binom{k}{i}
\bigl((-1)^i\alpha^{k-2i}\bigr)^n.
\]

Consequently its ordinary generating function \(\mathcal E_P'(x)/\mathcal E_P(x)=\sum_{n\ge1}P(F_n)x^{n-1}\) is rational in \(x\) (indeed it lies in \(\mathbb Q(x)\), as its coefficients satisfy an integral linear recurrence).

Suppose \(P\) has a nonzero odd-degree coefficient, and let \(r\ge1\) be its **largest odd degree**, with \(a_r\ne0\). The simple pole at \(x=\alpha^{-r}\) has residue

\[
-\frac{a_r}{(\sqrt5)^r}\notin\mathbb Q.
\]

To see that it cannot cancel, the parameter \(\alpha^r\) comes only from an odd-degree monomial of degree at least \(r\), because all parameters associated with a degree-\(k\) term are \((-1)^i\alpha^{k-2i}\) and \(k-2i\) has the parity of \(k\). Among the odd-degree terms, \(r\) is largest, and the unique occurrence is at \(k=r,i=0\).

A nonzero algebraic formal function \(Y\) over \(\mathbb C(x)\), with rational logarithmic derivative \(Y'/Y\), has **rational residue at each finite pole** of that derivative: a local Puiseux branch at \(x=x_0\) has leading form \((x-x_0)^{u/v}\) times a nonzero Puiseux unit, and the residue of \(Y'/Y\) equals \(u/v\in\mathbb Q\). This contradicts the irrational residue above. Therefore a non-even \(P\) yields a transcendental \(\mathcal E_P\) over \(\mathbb Q(x)\).

**2. Exact rational factorization for even polynomials.** Assume \(P(T)=\sum_{j=0}^d c_jT^{2j}\). Let \(L_n=\alpha^n+\beta^n\) denote the Lucas numbers, and for \(t\ge1\) and \(\sigma\in\{+1,-1\}\) set

\[
Q_{t,\sigma}(x)=1-\sigma L_{2t}x+x^2.
\]

The binomial expansion of the powers of \(F_n\), followed by pairing the parameters \(\sigma\alpha^{2t}\) and \(\sigma\alpha^{-2t}\), gives the exact formal product

\[
\mathcal E_P(x)=
\prod_{\sigma\in\{\pm1\}}(1-\sigma x)^{-C_\sigma}
\prod_{t=1}^d\prod_{\sigma\in\{\pm1\}}Q_{t,\sigma}(x)^{-B_{t,\sigma}},
\]

where all exponents are rational numbers,

\[
C_\sigma=c_0\mathbf1_{\sigma=+1}
+\sum_{\substack{1\le j\le d\\(-1)^j=\sigma}}
\frac{(-1)^j c_j}{5^j}\binom{2j}{j},
\]

\[
B_{t,\sigma}=
\sum_{\substack{t\le j\le d\\(-1)^{j-t}=\sigma}}
\frac{(-1)^{j-t}c_j}{5^j}\binom{2j}{j-t}.
\]

Each rational exponent is a \(\mathbb Z\)-linear combination of the numbers \(c_j/5^j\). Therefore multiplying the exponents by \(m=5^{h(P)}\) makes all of them integral, proving \(\mathcal E_P^m\in\mathbb Q(x)\). This also proves algebraicity for every even \(P\).

**3. Minimality and exact degree.** When \(h(P)=0\), the preceding factorization is rational, so both asserted degrees equal \(1\). Assume \(h=h(P)>0\). Choose the **largest** index \(j_*\ge1\) satisfying \(j_*-\nu_5(c_{j_*})=h\). In the coefficient \(B_{j_*,+1}\), the term at \(j=j_*\) equals \(c_{j_*}/5^{j_*}\), of \(5\)-adic valuation \(-h\). Every contribution from \(j>j_*\) has strictly larger \(5\)-adic valuation by choice of the largest maximizer. Hence

\[
\nu_5(B_{j_*,+1})=-h.
\]

The polynomial \(Q_{j_*,+1}\) is irreducible in \(\mathbb Q[x]\), because its discriminant is \(L_{2j_*}^2-4=5F_{2j_*}^2\), a nonsquare rational integer. The polynomials \(Q_{t,\sigma}\), for distinct pairs \((t,\sigma)\), are pairwise distinct and are also distinct from \(1-x\) and \(1+x\). Thus the order of the rational function \(R(x)=\mathcal E_P(x)^{5^h}\) at the prime \(Q_{j_*,+1}\) is the integer \(-5^h B_{j_*,+1}\), **not divisible by five**.

If \(Y^{5^h}=R(x)\), then any algebraic extension of \(\mathbb Q(x)\) containing \(Y\) must have ramification index divisible by \(5^h\) at \(Q_{j_*,+1}\), because the order of \(R\) at that prime is coprime to \(5^h\). Its degree is therefore at least \(5^h\); the equation itself gives an upper bound \(5^h\). This proves the asserted exact field degree. The same prime-order computation shows that \(Y^m\) can be rational for a positive integer \(m\) only if \(5^h\mid m\). Thus \(5^h\) is also the minimal rationalizing power.

**4. Integral examples.** For \(d\ge3\), \(P_d(0)=P_d(1)=0\), and \(P_d(2)=2^{2d-4}(2^4-1)\) is divisible by \(5\). Thus [1, Theorem 1.1] gives integrality of \(\mathcal E_{P_d}\). Its highest coefficient \(c_d=1\) has deficit \(d\), so \(h(P_d)=d\) and the exact degree is \(5^d\). Substituting \(d=3\) in the factorization proves the explicit rational-power identity in the Finding.

## Verification

A standalone Python 3 checker, `fibonacci_polynomial_degree_check.py`, uses only exact rational and integer arithmetic. It independently computes coefficients through the formal logarithmic-derivative recurrence and through products of the explicit linear/quadratic factors, checking equality through the stated finite truncation for 111 coefficient choices, including random mixed-sign even polynomials, rational examples, nonintegral algebraic examples, and the degree-\(125\) and degree-\(625\) integral examples. It also checks the predicted \(5\)-adic denominator and the isolating irreducible factor's primitive order. Run:

```
python3 fibonacci_polynomial_degree_check.py
```

Expected final message: `FIBONACCI_POLYNOMIAL_DEGREE_EXACT_OK 111 cases 125_degree_example 625_degree_example`.

These finite diagnostics do not prove transcendence, algebraicity, or the infinite degree classification. Those statements rest on the residue/Puiseux obstruction and the irreducible-factor valuation proof above. The published integrality characterization is used only for the displayed integral subfamily and is cited explicitly.

## Relationship to prior work

Li, Zhong and Zhou [1] classify when the exponential has integral coefficients for **arbitrary** integer polynomial Fibonacci weights. Their Theorem 4.1 proves the exact algebraic degree for the single-monomial weights \(5F_n^{2k}\), and Example 3.4 includes \(T^6-T^2\) as an integral polynomial weight. The full text inspected in Sections 1, 3, 4 and 8 does not state a universal algebraicity/transcendence dichotomy, mixed-weight degree formula, or degree for the mixed polynomial in Example 3.4. In particular, integrality cannot be used alone to infer algebraicity or the field degree.

Minton [2] classifies integer linear recurrence sequences satisfying Gauss-type congruences using trace sequences, while Byszewski, Graff and Ward [3] explain the trace characterization and exponential Euler products. Beukers, Houben and Straub [4] study Gauss congruences of rational functions. These supply congruence and trace context; their accessible passages do not state the present exact function-field ramification-degree classification. The local Puiseux-residue criterion and the binomial spectral decomposition are standard techniques; the claim is the resulting complete formula for the specified Fibonacci-polynomial family, not priority over those general methods.

## Limitations

The result is for the standard Fibonacci sequence and polynomial weights with integer coefficients; no analogous classification is claimed for arbitrary Lucas-type recurrences, polynomially sampled indices, or nonpolynomial weights. The explicit degree formula does not bound coefficient heights, describe Galois groups, or address analytic continuation beyond the algebraicity obstruction. Full-text access to every potentially related historical paper was not obtained; particularly the 2014 Minton source was compared through its published abstract and the detailed 2021 survey. An unindexed equivalent treatment remains possible.

## References

[1] J. P. Li, Y. M. Zhong, Y. B. Zhou, *Integral Exponential Series: Fibonacci Weights and Implicit Equations*, arXiv:2611.16283v1, first submitted November 12, 2026. https://arxiv.org/html/2611.16283v1

[2] G. T. Minton, *Linear recurrence sequences satisfying congruence conditions*, Proceedings of the American Mathematical Society 142 (2014), 2337–2352. https://doi.org/10.1090/S0002-9939-2014-12168-X

[3] J. Byszewski, G. Graff, T. Ward, *Dold sequences, periodic points, and dynamics*, Bulletin of the London Mathematical Society 53 (2021), 1263–1298. https://doi.org/10.1112/blms.12531

[4] F. Beukers, M. Houben, A. Straub, *Gauss congruences for rational functions in several variables*, Acta Arithmetica 184 (2018), 341–362. https://arxiv.org/abs/1710.00423
