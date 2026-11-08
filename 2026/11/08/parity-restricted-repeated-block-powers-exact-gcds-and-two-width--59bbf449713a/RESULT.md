# Parity-restricted repeated-block powers: exact gcds and two-width witnesses

## Finding

Fix integers \(b\ge2\) and \(k\ge2\). For each positive block width \(h\), define
\[
R_{b,k}(h)=\sum_{j=0}^{k-1}b^{jh}=\frac{b^{kh}-1}{b^h-1}.
\]
A positive base-\(b\) repeated-block \(k\)-th power with block width \(h\) is an integer \(aR_{b,k}(h)\), where \(b^{h-1}\le a<b^h\). The coefficient bound ensures a canonical digit block with no leading zeros. Let \(\mathcal S^{\mathrm{odd}}_{b,k}\) and \(\mathcal S^{\mathrm{even}}_{b,k}\) denote these numbers with odd and even \(h\), respectively; including zero would not change their gcds.

Write \(k=2^s t\), where \(s\ge0\) and \(t\ge1\) is odd, and put
\[
U=\frac{b^t-1}{b-1},\qquad H=\frac{b^k-1}{b^t-1}.
\]
**Parity-width gcd theorem.** For all such \(b,k\),
\[
\boxed{\gcd(\mathcal S^{\mathrm{odd}}_{b,k})
=H\gcd(t,U)
=\gcd\bigl(R_{b,k}(1),R_{b,k}(t)\bigr)}
\]
and
\[
\boxed{\gcd(\mathcal S^{\mathrm{even}}_{b,k})
=\gcd\!\left(k,\frac{b^{2k}-1}{b^2-1}\right).}
\]
The new arithmetic component for **even** repetition counts is the odd-width formula and its *two-width certificate*: block widths \(1\) and \(t\) suffice to determine the gcd of every odd-width repeated-block power. The even-width identity follows directly from the published unrestricted-base result applied to base \(b^2\). For odd \(k\), Theorem 1 of [1] already implies the odd-width identity, because its two gcd witnesses have widths \(1\) and \(k\), both odd; the novel distinction concerns even \(k\).

In particular, if \(k\) is a power of two, the odd-width gcd is \((b^k-1)/(b-1)\). When \(b=2\) and \(k=4\), the odd-width gcd is \(15\) while the even-width gcd is \(1\); the unrestricted gcd is \(1\). Thus the length-parity restriction can produce a strict and arbitrarily large new congruence obstruction even when the unrestricted repeated-block powers have gcd one.

## Assumptions and scope

The base \(b\) and repetition count \(k\) are arbitrary integers at least two, and widths range over **all** positive integers of the specified parity. The gcd of an infinite nonzero set is the unique positive generator of its integer span. The leading block coefficient is an integer in the stated half-open range; numbers with a leading zero are excluded. No primality, coprimality, or asymptotic assumption on \(b,k\) is required.

## Proof

**1. Reduction to geometric sums.** For fixed \(h=1\), the coefficient \(a=1\) occurs, so the gcd of the permitted \(a\)'s is one. For every \(h\ge2\), the interval of allowed \(a\)'s contains two consecutive positive integers and hence also has gcd one. It follows that, for either width parity, the gcd of all permitted \(aR_{b,k}(h)\) equals the gcd of the corresponding \(R_{b,k}(h)\).

**2. Lower bound for every odd width.** The elementary identities
\[
H=\prod_{i=0}^{s-1}\bigl(b^{2^i t}+1\bigr),\qquad
R_{b,k}(h)=R_{b,t}(h)\prod_{i=0}^{s-1}\bigl(b^{2^i t h}+1\bigr)
\]
hold with empty products interpreted as one when \(s=0\). For odd \(h\), \(X+1\) divides \(X^h+1\) for every integer \(X\). Applying this to each factor shows that \(H\) divides the displayed product of \(s\) factors. By Theorem 1 of Kane–Sanna–Shallit [1], applied with repetition count \(t\) and base \(b\),
\[
\gcd_{h\ge1}R_{b,t}(h)=\gcd\left(t,\frac{b^t-1}{b-1}\right)=\gcd(t,U).
\]
Hence \(g:=\gcd(t,U)\) divides \(R_{b,t}(h)\) for every \(h\). Since the displayed factors are multiplied, \(Hg\mid R_{b,k}(h)\) for every odd \(h\). This argument does not require \(H\) and \(g\) to be coprime.

**3. Exact upper bound from two odd widths.** At width \(1\), \(R_{b,k}(1)=HU\). Because \(t\) is odd, \(U=1+b+\cdots+b^{t-1}\) is odd: this is immediate for even \(b\), and for odd \(b\) it is a sum of an odd number of odd integers. As \(b^t\equiv1\pmod U\),
\[
H=\sum_{j=0}^{2^s-1}b^{tj}\equiv2^s\pmod U,
\]
so \(\gcd(H,U)=1\). The second selected width \(h=t\) is odd, and
\[
R_{b,k}(t)=\sum_{j=0}^{k-1}b^{tj}\equiv k\pmod U.
\]
Step 2 shows that \(H\mid R_{b,k}(t)\); let \(Y=R_{b,k}(t)/H\). If \(t=1\), then \(U=1\), the two selected widths coincide, and the gcd is already \(H\) because \(R_{b,k}(1)=H\). For \(t>1\), we have \(U>1\); inverting \(H\) modulo \(U\) gives \(Y\equiv kH^{-1}\pmod U\), whence
\[
\begin{aligned}
\gcd\bigl(R_{b,k}(1),R_{b,k}(t)\bigr)
&=H\gcd(U,Y)\\
&=H\gcd(U,k)\\
&=H\gcd(U,t),
\end{aligned}
\]
where the last equality uses that \(U\) is odd and \(k=2^s t\). Since every odd-width gcd divides the gcd of these two particular widths, this matches Step 2 and proves the first boxed formula, with \(t=1\) covered by the preceding direct case.

**4. Even widths.** Write \(h=2j\). Then \(R_{b,k}(2j)=R_{b^2,k}(j)\). The same fixed-width coefficient reduction from Step 1 applies, so Theorem 1 of [1] with base \(b^2\) gives
\[
\gcd_{j\ge1}R_{b^2,k}(j)=\gcd\!\left(k,\frac{(b^2)^k-1}{b^2-1}\right).
\]
This is the claimed even-width formula.

**5. Additive interpretation.** A sum of odd-width powers must be divisible by the first boxed gcd. Conversely, the width-one number and finitely many numbers at width \(t\) have gcd exactly that value: at each fixed width, consecutive coefficients recover its full geometric-sum gcd. After division by the gcd, these give a finite set of positive coprime integers. The classical numerical-semigroup/Frobenius principle then shows every *sufficiently large* multiple of the gcd is a sum of some number of permitted odd-width powers. This does **not** establish any uniform bound on the number of summands.

## Verification

The standalone file `verify.py` computes the claimed odd-width formula, the two-width gcd, and the direct gcd through many odd widths using exact integers; it also computes the even-width formula against many even widths. It tests bases \(2\) through \(10\) and repetition counts \(2\) through \(40\). Run `python3 verify.py`. These finite checks are consistency evidence; Steps 1–5 establish the theorem for every base and repetition count.

## Relationship to prior work

Kane, Sanna, and Shallit [1, Theorem 1] prove the unrestricted-width formula \(\gcd(k,(b^k-1)/(b-1))\) and the stronger Waring-type additive result with bounded numbers of summands. The even-width formula here is an immediate substitution of base \(b^2\) into that theorem and is included only for the parity comparison. For odd \(k\) the published two-witness identity already gives the restricted odd-width gcd. For even \(k\), the factorization along the two-primary part of \(k\) and a new two-width certificate go beyond the unrestricted statement. For example, base \(2\), repetition count \(4\), has unrestricted gcd \(1\) but odd-width gcd \(15\).

The classification concerns common divisors and the corresponding elementary eventual *unbounded-summand* reachability. It is not a proof that there is a bounded Waring order within either parity-restricted set.

## Limitations

The formula does not determine minimal Waring orders, Frobenius numbers, exact representation counts, or widths restricted by congruences other than parity. The novelty comparison is relative to inspected literature and does not certify absolute bibliographic priority. There has been no independent scientific audit.

## References

[1] D. M. Kane, C. Sanna, and J. Shallit, *Waring's Theorem for Binary Powers*, arXiv:1801.04483v1, publicly submitted 13 January 2018, especially Section 2, Theorem 1; https://arxiv.org/abs/1801.04483 . An open author-hosted complete text is available at https://cseweb.ucsd.edu/~dakane/waring.pdf .
