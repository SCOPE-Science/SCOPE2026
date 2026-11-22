# Exact dyadic image, fibers, and periods of consecutive fifth-power sums

## Finding

Let \(F(n)=\sum_{j=1}^{n}j^5\) for \(n\ge0\). For every integer \(k\ge2\), the least period of \(F(n)\bmod 2^k\), as a function of the nonnegative integer index, is exactly \(2^k\); modulo two the least period is four. Define
\[
N_k(y)=\#\{0\le n<2^k:F(n)\equiv y\pmod{2^k}\}\qquad(k\ge2).
\]
Then, writing \(j=k-2r\) whenever \(\nu_2(y)=2r\) with \(r\ge1\), the complete fiber law is:

* \(N_k(0)=2^{\lfloor k/2\rfloor}\).
* If \(y\) is odd, \(N_k(y)=2^{\min(2,k-1)}\) precisely when \(y\equiv1\pmod{2^{\min(3,k)}}\), and otherwise it is zero.
* If \(y\ne0\), \(\nu_2(y)=2r\ge2\), and its odd part \(u=y/2^{2r}\) satisfies \(u\equiv5\pmod{2^{\min(3,j)}}\), then \(N_k(y)=2^{r+\min(2,j-1)}\). In every other even nonzero case it is zero.

Here \(y\) is represented by its unique integer in \(\{0,\dots,2^k-1\}\), and all valuations of nonzero representatives are ordinary valuations. For \(k=1\), both residues have exactly two occurrences in the least period \(0\le n<4\).

Consequently the image cardinality at precision \(k\ge2\) is
\[
V(k)=1+2^{\max(k-3,0)}+
\sum_{r=1}^{\lfloor(k-1)/2\rfloor}2^{\max(k-2r-3,0)}.
\]
At \(k=1\), \(V(1)=2\). The continuous extension \(F:\mathbb Z_2\to\mathbb Z_2\) has image exactly
\[
\boxed{\{0\}\;\sqcup\;(1+8\mathbb Z_2)\;\sqcup\;
\bigsqcup_{r\ge1}2^{2r}(5+8\mathbb Z_2).}
\]
Its Haar measure is exactly \(1/6\). Every nonzero value in this image has exactly four distinct preimages in \(\mathbb Z_2\), and zero has exactly two.

## Assumptions and scope

All congruences and index ranges refer to the ordinary nonnegative-integer sum of fifth powers, with the empty sum \(F(0)=0\). The two-adic extension is given by its rational Faulhaber polynomial, which is integral on \(\mathbb Z_2\). The image and preimage assertions are over \(\mathbb Z_2\); the finite fiber assertions use one *least* full integer-index period. This is a local statement at the prime two, not a statement about simultaneous global integer representability at other primes.

## Proof

**1. An isometric triangular coordinate.** Put
\[
T(x)=\frac{x(x+1)}2,\qquad H(t)=\frac{t^2(4t-1)}3.
\]
The classical fifth-power identity is \(F(x)=H(T(x))\). Both \(T\) and \(H\) take two-adic integer values, since \(x(x+1)\) is even and three is a unit. On the parity classes, set
\[
T(2a)=a(2a+1),\qquad T(2a+1)=(a+1)(2a+1).
\]
Differences of either displayed polynomial at arguments \(a,b\) equal \((a-b)\) multiplied by an odd integer. Thus each map \(a\mapsto T(2a+\epsilon)\), for \(\epsilon\in\{0,1\}\), preserves exactly the two-adic distance. It is bijective on each finite ring \(\mathbb Z/2^m\mathbb Z\) by injectivity and equal cardinalities, and hence bijective on \(\mathbb Z_2\). In particular every \(t\in\mathbb Z_2\) has exactly two \(T\)-preimages, one of each parity.

**2. The odd branch of \(H\).** The difference factorization is
\[
H(t)-H(s)=\frac{t-s}{3}\bigl(4(t^2+ts+s^2)-(t+s)\bigr).
\]
For odd \(t,s\) with \(t\equiv s\pmod4\), the factor in parentheses is exactly twice an odd unit: the first summand vanishes modulo four, while \(t+s\equiv2\pmod4\). Hence
\[
\nu_2(H(t)-H(s))=\nu_2(t-s)+1.
\]
Since \(H(t)\equiv1\pmod8\) for odd \(t\), on each of \(1+4\mathbb Z_2\) and \(3+4\mathbb Z_2\) the normalized map \(a\mapsto(H(c+4a)-H(c))/8\) is an isometry of \(\mathbb Z_2\), and hence a bijection. Each class maps bijectively onto \(1+8\mathbb Z_2\). Every target in this ball therefore has exactly two odd \(H\)-preimages.

**3. Every positive even valuation branch.** Write \(t=2^r u\) with \(r\ge1\) and \(u\) odd. Because \(4t-1\) and three are units,
\[
\nu_2(H(t))=2r,
\qquad H(t)/2^{2r}=H_r(u)=\frac{u^2(2^{r+2}u-1)}3\equiv5\pmod8.
\]
For odd \(u,v\) with \(u\equiv v\pmod4\), factorization gives
\[
H_r(u)-H_r(v)=\frac{u-v}{3}
\bigl(2^{r+2}(u^2+uv+v^2)-(u+v)\bigr),
\]
whose second factor has valuation exactly one. Consequently the normalized map \(a\mapsto(H_r(c+4a)-H_r(c))/8\) is an isometry, hence a bijection, on each class \(c=1,3\). Both classes map onto \(5+8\mathbb Z_2\), so each value of valuation \(2r\) and odd part congruent to five modulo eight has exactly two \(H\)-preimages. No other even nonzero valuations occur. Also \(H(t)=0\) forces \(t=0\), since \(4t-1\) is always an odd unit. Composing with the two bijective parity branches of \(T\) proves the stated image and the exact four-versus-two infinite fiber law.

**4. Haar measure.** The image components are disjoint, so their measures add to
\[
\frac18+\sum_{r\ge1}2^{-2r-3}
=\frac18+\frac1{24}=\frac16.
\]

**5. Finite fibers and image counts.** When \(k\ge2\), the above difference factorization shows that \(H(t+2^{k-1})\equiv H(t)\pmod{2^k}\), because \(t\) and \(t+2^{k-1}\) have the same parity, forcing the bracket even. The triangular map \(n\mapsto T(n)\bmod2^{k-1}\) is exactly two-to-one on \(0\le n<2^k\). For nonzero odd targets, the two odd \(H\)-branches yield two \(t\)-preimages when \(k\ge3\) (one when \(k=2\)), hence the claimed \(N_k\). For a target with valuation \(2r\), put \(j=k-2r\ge1\). Every admissible odd unit maps to the same unit class when \(j=1,2\), giving \(2^{r+j-1}\) index preimages. When \(j\ge3\), the two isometric unit branches give \(2^{r+2}\) index preimages; these three cases combine as \(2^{r+\min(2,j-1)}\). The zero fiber consists exactly of those \(t\) divisible by \(2^{\lceil k/2\rceil}\), yielding \(2^{\lfloor k/2\rfloor}\) indices. Counting the one zero target, the odd target cylinder, and the positive even-valuation target cylinders gives \(V(k)\) above. The full period is established next.

**6. Least periods.** On either parity class,
\[
T(n+2^k)-T(n)=2^{k-1}(2n+2^k+1).
\]
The bracket is odd. Since \(H(t)-H(s)\) is divisible by \(2(t-s)\) whenever \(t\equiv s\pmod2\), this proves that \(2^k\) is a period modulo \(2^k\) for all \(k\ge2\). To show leastness, it suffices to rule out a period of \(2^{k-1}\), because any least period divides \(2^k\). At \(k=2,3\), the respective witnesses are \(F(2)=33\not\equiv F(0)\pmod4\) and \(F(4)=1300\not\equiv F(0)\pmod8\). For \(k\ge4\), let \(M=2^{k-1}\). Then
\[
F(M+1)-F(1)=F(M)+(M+1)^5-1.
\]
We have \(\nu_2(F(M))=2(k-2)\ge k\) by \(F=H\circ T\), and \(\nu_2((M+1)^5-1)=k-1\). Thus the difference is nonzero modulo \(2^k\). Modulo two, \(F(n)\equiv T(n)\) and its least period is four. This establishes every claimed period.

## Verification

The standalone `check.py` enumerates each complete least period modulo \(2^k\), compares the exact target-by-target fiber law and image count for every \(1\le k\le13\), and independently tests all candidate periods and half-period failures. Its completed run reported **32,805 passed exact modular assertions**. Image counts for \(k=2,3,4,5,6,7,8,9,10\) are \(2,3,4,7,12,23,44,87,172\), respectively. These finite computations corroborate but do not establish the infinite classification, which follows from the isometry and valuation arguments above.

Reproduce with `python3 check.py` using only the Python standard library.

## Relationship to prior work

Faulhaber's fifth-power identity and the expression of odd power sums as polynomials in triangular numbers are classical; neither is claimed as new. T. Lengyel, *On Divisibility of Some Power Sums*, *Integers* 7 (2007), A41, Theorem 1, determines the two-adic valuation of sums at indices \(2^m-1\), including the fifth-power instance. That specialization is compatible with the present result but does not classify all attained target residues or their multiplicities, nor give the exact index period. The 2013 article *A Fast Algorithm for Computing Binomial Coefficients Modulo Powers of Two* discusses algorithms for evaluating finite power sums, not a complete all-precision target-fiber theorem in the accessible Section 4. Other digital-image and polynomial-fiber studies concern different maps or sums of independently chosen powers. The new result is the explicit global fifth-power partial-sum image, all target fibers and all sharp periods, not the original polynomial identity or the special-index valuation.

## Limitations

This classification is at the prime two and for fifth powers only. It does not assert an analogous classification at odd primes or for every higher odd exponent. The historical originality comparison covers accessible named primary sources and relevant searched mathematical records; an undiscovered equivalent or a specialized formulation in inaccessible work cannot be excluded. The finite checker is not an independent audit and is not a substitute for the proof.

## References

1. Johann Faulhaber, classical formulas for sums of powers, 1631; fifth-power identity summarized in *Faulhaber's Formula*, Wolfram MathWorld, https://mathworld.wolfram.com/FaulhabersFormula.html .
2. Tamás Lengyel, *On Divisibility of Some Power Sums*, *Integers* 7 (2007), A41, published 2007-09-19, https://math.colgate.edu/~integers/h41/h41.pdf .
3. *A Fast Algorithm for Computing Binomial Coefficients Modulo Powers of Two*, 2013, Section 4 (computational power-sum methods), https://onlinelibrary.wiley.com/doi/10.1155/2013/751358 .
