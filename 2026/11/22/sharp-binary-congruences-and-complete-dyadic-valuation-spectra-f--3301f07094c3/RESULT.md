# Sharp binary congruences and complete dyadic valuation spectra for type-B Eulerian rows

## Finding
Let \(B(n,k)\) be the number of signed permutations of length \(n\) with precisely \(k\) descents of Coxeter type \(B\), and put \(B_n(t)=\sum_{k=0}^{n}B(n,k)t^k\). For every integer \(n\ge2\),
\[
 B_n(t)\equiv(1+t)^n\pmod{2^{1+\nu_2(n(n-1))}}.
\]
This coefficientwise congruence is **best possible**: the difference polynomial has at least one coefficient of exactly that valuation, namely
\[
 B(n,1)=3^n-n-1,\qquad
 \nu_2\!\left(B(n,1)-n\right)=1+\nu_2\!\left(n(n-1)\right).
\]
In particular, if \(n=2^r\) with \(r\ge1\), then for every \(1\le k<2^r\),
\[
 \nu_2\!\left(B(2^r,k)\right)=r-\nu_2(k).
\]
Exactly \(2^{j-1}\) interior entries have valuation \(j\), for each \(1\le j\le r\), and the two endpoint entries both have valuation zero. This is a complete nonasymptotic valuation spectrum for each power-of-two row.

## Assumptions and scope
All indices are ordinary nonnegative integers. We use \(\nu_2(a)\) for the highest power of two dividing a nonzero integer \(a\) and \(\nu_2(0)=\infty\). Congruence of integer polynomials means coefficientwise congruence. The type-B Eulerian numbers are normalized by the exact signed Worpitzky identity
\[
 \sum_{m\ge0}(2m+1)^n t^m=\frac{B_n(t)}{(1-t)^{n+1}},
\]
which equivalently yields \(B_0(t)=1\) and the integer recurrence
\[
 B_n(t)=[1+(2n-1)t]B_{n-1}(t)+2t(1-t)B'_{n-1}(t),\quad n\ge1.
\]
There are no primality hypotheses on \(n\). The binary valuation formula for the full interior row is claimed only when \(n\) is an exact power of two.

## Proof
**1. The even-index estimate.** Expanding \((2m+1)^n\) in the signed Worpitzky identity, and using \(\sum_{m\ge0}m^j t^m=tA_j(t)/(1-t)^{j+1}\) for \(j\ge1\), where \(A_j(t)\in\mathbb Z[t]\) is an ordinary Eulerian polynomial, gives the exact integer-polynomial identity
\[
 B_n(t)=(1-t)^n+\sum_{j=1}^n 2^j\binom nj\,tA_j(t)(1-t)^{n-j}.
\]
Since \(j\binom nj=n\binom{n-1}{j-1}\), the \(j\)-th summand is divisible by \(2^{\nu_2(n)+j-\nu_2(j)}\), and \(j-\nu_2(j)\ge1\). Also,
\[
 (1-t)^n-(1+t)^n=-2\sum_{\substack{1\le k\le n\\k\text{ odd}}}\binom nk t^k
\]
has all coefficients divisible by \(2^{1+\nu_2(n)}\), by the same binomial identity with odd \(k\). Hence, for every \(n\ge1\),
\[
 B_n(t)-(1+t)^n\in 2^{1+\nu_2(n)}\mathbb Z[t].\tag{1}
\]
If \(n\) is even, \(\nu_2(n(n-1))=\nu_2(n)\), so this already proves the stated bound.

**2. Odd-index gain.** Put \(E_n(t)=B_n(t)-(1+t)^n\). Substituting into the displayed type-B recurrence and simplifying gives the exact error recurrence
\[
 E_n(t)=[1+(2n-1)t]E_{n-1}(t)+2t(1-t)E'_{n-1}(t)+4(n-1)t(1+t)^{n-2}.\tag{2}
\]
For odd \(n\ge3\), the preceding even index \(n-1\) satisfies \(E_{n-1}(t)\in2^{1+\nu_2(n-1)}\mathbb Z[t]\) by (1). Differentiation and multiplication by integer polynomials preserve coefficient divisibility. The last term of (2) is divisible by \(2^{2+\nu_2(n-1)}\). Consequently \(E_n(t)\in2^{1+\nu_2(n-1)}\mathbb Z[t]\), which equals the claimed exponent \(1+\nu_2(n(n-1))\) for odd \(n\). Thus the coefficientwise congruence holds for all \(n\ge2\).

**3. Sharpness for every row.** Extracting the coefficient of \(t\) from the Worpitzky identity gives \(B(n,1)=3^n-(n+1)\), and therefore
\[
 B(n,1)-n=3^n-2n-1=2n(n-1)U_n,
\]
where
\[
 U_n=1+\sum_{j=3}^n\frac{2^{j-1}}{j(j-1)}\binom{n-2}{j-2}.
\]
For each \(j\ge3\), \(\nu_2(j(j-1))\le j-2\): precisely one of two consecutive integers is even, and its power-of-two divisor is no greater than \(2^{j-2}\) (check \(j=3\), then \(2^{j-2}\ge j\) for \(j\ge4\)). Thus every summand in \(U_n-1\) has positive two-adic valuation. Hence \(U_n\) is a two-adic unit, proving
\[
 \nu_2\!\left(B(n,1)-n\right)=1+\nu_2\!\left(n(n-1)\right),\quad n\ge2.
\]
This is an actual coefficient attaining the guaranteed valuation, so no larger common modulus is possible.

**4. Full dyadic spectrum.** For \(n=2^r\), the error modulus just established is \(2^{r+1}\). On the other hand
\[
 \binom{2^r}{k}=\frac{2^r}{k}\binom{2^r-1}{k-1},\qquad 1\le k<2^r.
\]
Every \(\binom{2^r-1}{k-1}\) is odd by Lucas's theorem, because the base-two digits of \(2^r-1\) are all ones. Therefore \(\nu_2\binom{2^r}{k}=r-\nu_2(k)\le r\). Adding an error divisible by \(2^{r+1}\) cannot change that exact valuation. For a fixed \(j\) from one through \(r\), the indices attaining valuation \(j\) are exactly those with \(\nu_2(k)=r-j\); among \(1\le k<2^r\), precisely \(2^{j-1}\) indices have this valuation. Finally, \(B(2^r,0)=B(2^r,2^r)=1\) by the recurrence. This completes the proof.

## Verification
A standalone standard-library Python file `verify.py` computes type-B Eulerian rows from the recurrence, independently checks rows through size 32 against the signed Worpitzky coefficient formula, verifies the sharp coefficientwise congruence and the \(k=1\) witness for every \(2\le n\le512\), and checks the entire dyadic valuation spectrum and multiplicities for all powers of two through 512. Executing `python3 verify.py` produces `PASS 134479 exact assertions; rows 1..512, independent finite formulas through 32`. The proof above covers all integer indices; these finite checks are diagnostics rather than certification of its infinite quantifiers.

## Relationship to prior work
Castro, González and Medina (2015) studied prime-adic valuations in the classical Eulerian array, rather than establishing the sharp type-B coefficientwise comparison with Pascal rows. Its accessible abstract gives no type-B theorem; full-text access was not obtained, so an implicit equivalent cannot be ruled out. Santocanale's open preprint (2021) develops exact type-B and type-D Eulerian enumerative identities, including two explicit type-B polynomial formulas, but the relevant material inspected contains no claimed sharp two-adic congruence. The OEIS table of type-B Eulerian numbers records finite coefficients; a table alone does not imply the infinite sharpness theorem. Literature comparisons are qualified, and absence from searches is not proof of historical priority.

## Limitations
The result concerns the standard type-B Eulerian normalization and the prime two. It does not claim valuations for every odd prime, nor does it provide a full valuation spectrum for all non-dyadic row indices. Independent mathematical verification and an exhaustive historical-priority determination have not been performed. Access to the full 2015 valuation paper was unavailable during the comparison; an implicit earlier specialization remains possible.

## References
- F. N. Castro, O. E. González and L. A. Medina, *The p-adic Valuation of Eulerian Numbers: Trees and Bernoulli Numbers*, Experimental Mathematics 24 (2015), 183–195; first available online 27 May 2015. https://doi.org/10.1080/10586458.2014.981899
- L. Santocanale, *Bijective proofs for Eulerian numbers of types B and D*, arXiv:2104.12445 (2021). https://arxiv.org/abs/2104.12445
- OEIS A060187, *Eulerian numbers of type B*. https://oeis.org/A060187
