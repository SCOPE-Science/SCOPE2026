# The exact content of every interior Eulerian row

## Finding

Let \(A(n,k)\) count permutations of \(\{1,\ldots,n\}\) with exactly \(k\) descents. For every integer \(n\ge3\), the greatest common divisor of the strictly interior Eulerian coefficients satisfies

\[
\gcd_{1\le k\le n-2}A(n,k)=
\begin{cases}
4,&n=3,\\
11,&n=4,\\
2,&n\ge5\text{ and }n-1\text{ is a power of }2,\\
1,&\text{otherwise}.
\end{cases}
\]

Equivalently, this is the integer content of \(E_n(t)-1-t^{n-1}\), where \(E_n(t)=\sum_{k=0}^{n-1}A(n,k)t^k\). In particular, the unique odd-prime factor across all such row contents occurs in the four-permutation row and equals \(11\).

## Assumptions and scope

The index \(n\) is an arbitrary integer at least three; the endpoints \(k=0\) and \(k=n-1\), both equal to one, are excluded. The gcd is positive and taken over the complete nonempty set of \(n-2\) interior coefficients. All congruences in the argument concern integers or polynomials with coefficients in a specified prime field. The theorem does not assert a classification of gcds of any proper subcollection of the interior columns.

## Proof

**1. A parity identity.** The classical Eulerian generating identity is

\[
\frac{E_n(t)}{(1-t)^{n+1}}=\sum_{m\ge1}m^n t^{m-1}.
\]

For every positive \(n\), reduction coefficientwise modulo two yields \(m^n\equiv m\pmod2\). Thus the series on the right becomes \((1-t^2)^{-1}\), and hence

\[
E_n(t)\equiv(1+t)^{n-1}\pmod2.
\]

By Lucas's theorem, all intermediate coefficients of \((1+t)^{n-1}\) are even exactly when the positive integer \(n-1\) is a power of two. If \(n-1\) is not a power of two, the interior row gcd is odd. If \(n=2^r+1\ge5\), the closed form \(A(n,1)=2^n-n-1\) gives \(A(n,1)\equiv2\pmod4\), so the gcd has exactly one factor of two. Directly, \(E_3(t)=1+4t+t^2\) and \(E_4(t)=1+11t+11t^2+t^3\), giving the two small cases.

**2. The obstruction posed by a hypothetical odd divisor.** Fix \(n\ge5\), and assume an odd prime \(p\) divides every interior coefficient. Then

\[
E_n(t)\equiv1+t^{n-1}\pmod p.
\]

Setting \(t=1\) gives \(n!\equiv2\pmod p\). For an odd prime \(p\le n\) this is impossible, since \(n!\equiv0\) but \(2\not\equiv0\pmod p\). Therefore \(p>n\ge5\), in particular \(p\ge7\). All denominators used in the next step are units modulo \(p\).

**3. Two exact cumulants.** For \(n\ge4\), put \(H_n(z)=E_n(e^z)/n!\). Its logarithmic derivatives at zero are the cumulants of the (uniform-permutation) descent statistic. The above Eulerian identity and the Laurent expansion of \(e^z/(1-e^z)\) give, as a formal rational power-series identity through degree four,

\[
\log H_n(z)=-z+(n+1)\log\!\left(\frac{e^z-1}{z}\right)+O(z^5)
\]

and

\[
\log\!\left(\frac{e^z-1}{z}\right)
=\frac z2+\frac{z^2}{24}-\frac{z^4}{2880}+O(z^5).
\]

For clarity, the omitted analytic part of \(\sum_{m\ge1}m^n e^{mz}\) first contributes in degree strictly greater than four after multiplication by \((1-e^z)^{n+1}\). Hence the second and fourth cumulants of the normalized Eulerian row are exactly

\[
\kappa_2=\frac{n+1}{12},\qquad \kappa_4=-\frac{n+1}{120}.
\]

As \(p>n\), normalization by \(n!\) is legitimate modulo \(p\). Under the hypothetical polynomial congruence, the normalized moment generating function is \((1+e^{(n-1)z})/2\); this two-point law has

\[
\kappa_2=\frac{(n-1)^2}{4},\qquad
\kappa_4=-\frac{(n-1)^4}{8}.
\]

These are polynomial identities in the first four normalized moments with denominators invertible modulo \(p\), so reducing them modulo \(p\) is justified. Comparing cumulants yields

\[
n+1\equiv3(n-1)^2\pmod p,\qquad
n+1\equiv15(n-1)^4\pmod p.
\]

The first is \((3n-1)(n-2)\equiv0\pmod p\). Since \(p>n\), \(n-2\not\equiv0\pmod p\), hence \(3n\equiv1\pmod p\). Also \(n-1\) is nonzero modulo \(p\), and combining the two congruences gives \(5(n-1)^2\equiv1\pmod p\). Substituting \(n\equiv1/3\) produces \(20\equiv9\pmod p\), so \(p\mid11\), forcing \(p=11\). Yet \(5\le n<p=11\) and \(n\equiv4\pmod{11}\) cannot both hold. This contradiction eliminates every odd prime divisor for all \(n\ge5\).

**4. Completion.** The prime two occurs precisely in the power-of-two predecessor cases, and then only to exponent one, by Step 1. Step 3 excludes all odd primes for \(n\ge5\). The two directly evaluated initial rows finish the proof. \(\square\)

## Verification

A standalone dependency-free program `check_eulerian.py` reconstructs Eulerian rows by their integer recurrence, computes the interior gcd for every \(3\le n\le240\), and compares it with the formula. It independently checks the inclusion-exclusion coefficient formula through row \(48\) and verifies the exact mean, variance, and fourth cumulant by rational arithmetic for rows \(4\le n\le20\). On execution it reports `passed 1462 assertions, n 3..240`. The unbounded classification follows from the preceding proof, not from finite tests.

## Relationship to prior work

Cao and Pan's 2006 preprint (published in 2008) proves prime-adic bounds for arithmetic-progressions sums of Eulerian coefficients; its Theorem 1.1 concerns sums over congruence classes, not the simultaneous divisibility of every interior coefficient. Nymann and Sáenz (1999), Theorem 4.1, prove that every coefficient in a prime-indexed Eulerian row is congruent to one modulo the row prime; this rules out that particular prime but gives no exact all-index interior gcd. Iijima, Sasaki, Takahashi and Yoshinaga study local polynomial congruences and Eulerian polynomials, but not this complete integer coefficient-content problem. The known Eulerian triangle and an indexed `RowGcd` table list matching finite values, which do not constitute an all-index proof or a general implication. Results on interior Narayana-row contents concern a different triangular array and cannot be specialized to Eulerian rows.

## Limitations

The result is restricted to the full collection of interior Eulerian coefficients and integer gcds. It does not classify the individual prime-adic valuations of all Eulerian numbers, gcds under column restrictions, or related arrays. Database entries support only finite numerical cases. Historical priority remains qualified: older Eulerian congruence literature not fully accessible and possible unindexed gcd classifications may contain equivalent statements. No independent mathematical audit is asserted.

## References

- H.-Q. Cao and H. Pan, *Congruences on Stirling numbers and Eulerian numbers*, arXiv:math/0608564 (first submitted 2006-08-23); Acta Arithmetica 132 (2008), 315–328, DOI 10.4064/aa132-4-2. https://arxiv.org/abs/math/0608564
- J. E. Nymann and R. A. Sáenz, *Eulerian Numbers: Inversion Formulas and Congruences Modulo a Prime*, Fibonacci Quarterly 37 (1999), 154–161. https://www.fq.math.ca/Scanned/37-2/nymann.pdf
- R. Iijima, T. Sasaki, T. Takahashi and M. Yoshinaga, *Eulerian polynomials and polynomial congruences*, arXiv:1611.10147. https://arxiv.org/abs/1611.10147
- N. J. A. Sloane et al., *OEIS A008292: Triangle of Eulerian numbers*. https://oeis.org/A008292
- P. Luschny, *Eulerian: IntegerTriangles.py*, indexed finite `RowGcd` table. https://luschny.de/math/oeis/Eulerian.html
