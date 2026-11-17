# Sharp dyadic valuations for alternating central Delannoy sums

## Finding

Let \(D_k=\sum_{j=0}^k\binom{k}{j}\binom{k+j}{j}\) be the central Delannoy number, and set
\[
A_n=\sum_{j=0}^{n-1}\binom{n-1}{j}\binom{n+j}{j},\qquad
S_n=\sum_{k=0}^{n-1}(-1)^k(2k+1)D_k\qquad(n\ge1).
\]
Then the following **exact** valuations hold for every integer \(n\ge1\):
\[
\nu_2(A_n)=\begin{cases}0,&n\text{ odd},\\3\nu_2(n)-1,&n\text{ even},\end{cases}
\qquad
\nu_2(S_n)=\begin{cases}0,&n\text{ odd},\\4\nu_2(n)-1,&n\text{ even}.\end{cases}
\]
In particular, for every \(t\ge1\), the alternating weighted sum of length \(2^t\) is divisible by \(2^{4t-1}\) but **not** by \(2^{4t}\). This sharpens the previously known even-length congruence modulo \(2n\) to an exact exponent.

## Assumptions and scope

The sums are over ordinary integers, \(n\ge1\), and \(\nu_2(m)\) denotes the exponent of \(2\) in a nonzero integer \(m\). The binomial coefficients are ordinary integer coefficients. A useful representation, proved below, is
\[
A_n=\frac{D_n+D_{n-1}}4
=\frac12[z^n]\left(\frac{1+z}{1-z}\right)^n.
\]
All assertions concern exact infinite families, not statistical patterns in initial terms.

## Proof

**1. The common sequence and the alternating sum.** The Legendre generating function and hypergeometric binomial formula give
\[
\sum_{n\ge0}D_n x^n=(1-6x+x^2)^{-1/2},\qquad D_n=P_n(3),
\]
where \(P_n\) is the classical Legendre polynomial. The elementary Christoffel--Darboux specialization (valid for \(u\ne1\)) is
\[
\sum_{k=0}^{n-1}(2k+1)P_k(u)
=\frac{n(P_n(u)-P_{n-1}(u))}{u-1}.
\]
Using \(P_k(-3)=(-1)^kD_k\) at \(u=-3\), we obtain
\[
S_n=(-1)^{n+1}\frac n4(D_n+D_{n-1}).
\tag{1}
\]
Thus it suffices to prove the displayed valuation formula for \(A_n=(D_n+D_{n-1})/4\). To relate this to the stated binomial sum, let
\(T(z)=(1+z)/(1-z)\) and let \(w(x)\in x\mathbb Q[[x]]\) solve \(w=xT(w)\). Lagrange inversion followed by differentiation gives
\[
[x^n]\left(\frac x2\frac{d}{dx}\log T(w(x))\right)
=\frac12[z^n]T(z)^n\qquad(n\ge1).
\]
Since \(w=(1-x-\sqrt{1-6x+x^2})/2\), direct substitution yields
\[
\frac x2\frac{d}{dx}\log T(w(x))
=\frac14\left(\frac{1+x}{\sqrt{1-6x+x^2}}-1\right).
\]
Its positive-degree coefficients are \((D_n+D_{n-1})/4\). Finally, the classical binomial identity
\[
\frac12[z^n]T(z)^n
=\sum_{j=0}^{n-1}\binom{n-1}{j}\binom{n+j}{j}
\qquad(n\ge1)
\]
can also be verified using the Jacobi-polynomial identity \(P_{n-1}^{(0,1)}(u)=(P_n(u)+P_{n-1}(u))/(u+1)\). Indeed, the terminating hypergeometric expansion of \(P_{n-1}^{(0,1)}(3)\) is exactly the binomial sum on the right, while the Jacobi identity evaluates it as \((D_n+D_{n-1})/4\). This identity is also recorded in OEIS A047781. Thus all representations of \(A_n\) agree.

**2. An exact reciprocal-sum lemma.** For every integer \(m\ge1\), put
\[
H_m^{\mathrm{odd}}=\sum_{j=1}^{m}\frac1{2j-1}\in\mathbb Z_2.
\]
We claim
\[
\boxed{\nu_2(H_m^{\mathrm{odd}})=2\nu_2(m).}\tag{2}
\]
For odd \(m\), the sum contains an odd number of odd-denominator units, so its reduction modulo two is one.

For \(m=2^su\) with \(s\ge1\) and \(u\) odd, divide its terms into \(u\) consecutive blocks of \(2^s\) terms. In block \(j\), with \(0\le j<u\), pair each first-half odd denominator
\(a=2^{s+1}j+2i-1\) (\(1\le i\le2^{s-1}\)) with its reflected partner \(b=2^{s+1}(j+1)-(2i-1)\). Their sum is \(C_j=2^{s+1}(2j+1)\), and
\[
\frac1a+\frac1b=\frac{C_j}{ab},\qquad
\frac1{ab}\equiv-\frac1{(2i-1)^2}\pmod{2^s}.
\]
The unit-square inverse sum obeys
\[
\sum_{\substack{1\le a<2^s\\a\text{ odd}}}a^{-2}
\equiv 2^{s-1}\pmod{2^s}.\tag{3}
\]
Indeed the case \(s=1\) is immediate. Lifting each odd residue \(a\) to the two residues \(a,a+2^s\) modulo \(2^{s+1}\), their inverse squares agree modulo \(2^{s+1}\), and the sum doubles. Consequently each block is congruent to
\(2^{2s}(2j+1)\) modulo \(2^{2s+1}\). Adding the odd number \(u\) of blocks gives
\(H_m^{\mathrm{odd}}\equiv2^{2s}\pmod{2^{2s+1}}\), proving (2).

**3. A single surviving term in the exponential expansion.** Define the formal series
\[
h(z)=\sum_{j\ge0}\frac{z^{2j+1}}{2j+1}\in\mathbb Z_2[[z]],
\qquad
T(z)^n=\exp(2n h(z)).
\]
At every positive degree \(n\), therefore,
\[
A_n=\frac12\sum_{r=1}^{n}\frac{(2n)^r}{r!}[z^n]h(z)^r.\tag{4}
\]
Because \(h\) has only odd-degree monomials, only \(r\equiv n\pmod2\) contribute. All coefficients of \(h(z)^r\) are \(2\)-adic integers. For a nonzero \(r\)-summand in (4), writing \(t=\nu_2(n)\), its valuation is at least
\[
r(t+1)-\nu_2(r!)-1=rt+s_2(r)-1,\tag{5}
\]
where \(s_2(r)\) is the binary digit sum and Legendre's formula \(\nu_2(r!)=r-s_2(r)\) was used.

When \(n\) is odd, the \(r=1\) term is exactly \(1\), while every contributing odd \(r\ge3\) has \(s_2(r)\ge2\) and hence its term is divisible by \(2\). Thus \(A_n\) is odd.

When \(n=2m\) is even, let \(t=\nu_2(n)\ge1\). The first contributing term, \(r=2\), equals
\[
\frac12\frac{(2n)^2}{2!}[z^n]h(z)^2
=n^2\sum_{j=1}^{m}\frac1{(2j-1)(2m-(2j-1))}
=2nH_m^{\mathrm{odd}}.
\]
By (2), its valuation is \(1+t+2(t-1)=3t-1\). Every other contributing term has even \(r\ge4\), so (5) gives valuation at least \(rt\ge4t>3t-1\). No cancellation at the leading valuation is possible. Hence \(\nu_2(A_n)=3t-1\). Equation (1) then gives \(\nu_2(S_n)=t+3t-1=4t-1\), completing the proof.

## Verification

The accompanying stdlib-only Python program `verify.py` independently constructs central Delannoy values using the three-term recurrence, compares the binomial definition through \(n=128\), compares the formal-coefficient identity through \(n=64\), and checks both exact valuation laws and the signed sum identity through \(n=1024\). It additionally checks the reciprocal-sum lemma modulo powers of two for \(64\) cases reaching \(m=1920\). Running `python3 verify.py` returned:

```text
VERIFY_OK delannoy_n=1024 binomial_n=128 coefficient_n=64 harmonic_cases=64 max_harmonic_m=1920
```

These finite computations only corroborate the explicitly proved infinite statements.

## Relationship to prior work

The arithmetic sequence is OEIS A047781; its formulas and Delannoy generating function were already known. Guo and Zeng, *New congruences for sums involving Apéry numbers or central Delannoy numbers* (arXiv:1008.2894), Theorem 3.2, prove a congruence of this alternating weighted sum modulo \(2n\). Their cited result does not give the exact valuation \(4\nu_2(n)-1\) for every even \(n\). Sun's *On sums of Apéry polynomials and related congruences* (arXiv:1101.1946), Theorem 1.4, studies closely related alternating sums at odd primes \(p>3\), not the composite-index dyadic exponent proved here. OEIS A142978 discusses conjectural congruences at odd primes, not this result. The new assertion is the **uniform sharp dyadic valuation** and its reciprocal-sum explanation, not the known coefficient or telescoping identities.

## Limitations

This result concerns the prime two and the stated single alternating weighting. It does not establish analogous sharp valuations at odd primes, weighted higher moments, or the complete odd parts of the sums. The theorem has undergone only self-review; no independent mathematical audit has been performed. Historical priority could change if an unexamined stronger valuation theorem covers this exact sequence.

## References

1. OEIS Foundation, *A047781*, https://oeis.org/A047781 (dated comments from 2002 and formulas from 2004 onward).
2. OEIS Foundation, *A142978*, https://oeis.org/A142978 (diagonal array and odd-prime congruence discussion).
3. V. J. W. Guo and J. Zeng, *New congruences for sums involving Apéry numbers or central Delannoy numbers*, arXiv:1008.2894, first posted 2010-08-17, especially Theorem 3.2.
4. Zhi-Wei Sun, *On sums of Apéry polynomials and related congruences*, arXiv:1101.1946, first posted 2011-01-10, especially Theorem 1.4.
