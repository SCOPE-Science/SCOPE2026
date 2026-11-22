# Exact parameter GCDs for dyadic Stern (0,1)-polynomial pairs

## Finding

Let \(P_n(X)\) be the Dilcher–Stolarsky Stern \((0,1)\)-polynomials, and let \(r\ge2\) be an integer. Write \(d=2^{r-1}\) and define the positive odd integer
\[
R_r=\sum_{j=0}^{r-1}2^{d-2^j}.
\]
Then, for **every integer** \(t\),
\[
\boxed{\gcd\bigl(P_{2^r+1}(t),P_{2^r+3}(t)\bigr)=\gcd(2t+1,R_r).}
\]
In particular, as \(t\) ranges over integers, the complete gcd spectrum comprises exactly the positive divisors of \(R_r\). For every \(e\mid R_r\), the value \(e\) occurs at exactly \(\varphi(R_r/e)\) residue classes of \(t\pmod{R_r}\); therefore its natural density is \(\varphi(R_r/e)/R_r\). The **least positive period** of the gcd sequence in \(t\) is exactly \(R_r\).

There is also an exact polynomial resultant identity:
\[
\operatorname{Res}_X(P_{2^r+1}(X),P_{2^r+3}(X))=R_r.
\]
Consequently, for every prime \(p\), the two reduced polynomials have a common root in an algebraic closure of \(\mathbb F_p\) **if and only if** \(p\mid R_r\). The integer \(R_r\) has precisely \(r\) nonzero binary digits. Its first four values, for \(r=2,3,4,5\), are \(3,13,209,53505\), respectively.

## Assumptions and scope

The polynomials are defined in \(\mathbb Z[X]\) by
\[
P_0(X)=0,\qquad P_1(X)=1,
\]
\[
P_{2n}(X)=P_n(X^2),\qquad
P_{2n+1}(X)=XP_n(X^2)+P_{n+1}(X^2)\quad(n\ge1).
\]
This is the \((0,1)\)-coefficient polynomial family, **not** the different Stern polynomial family with even-index recurrence \(B_{2n}(X)=XB_n(X)\). The integer index \(r\) is at least two, while the evaluation parameter \(t\) is any integer, including zero and negative values. Gcds are nonnegative, with \(\gcd(0,a)=|a|\); all resultants are the signed Sylvester resultants in the displayed order.

## Proof

**1. The canonical dyadic polynomial.** Iterating the defining recurrence gives, for each \(r\ge1\),
\[
A_r(X):=P_{2^r+1}(X)=1+X+\sum_{j=1}^{r-1}X^{2^j}.
\]
Indeed \(A_1(X)=1+X\), and the recurrence gives \(A_{r+1}(X)=X+A_r(X^2)\). For \(r\ge2\), its degree is \(d=2^{r-1}\), it is monic, and it has constant coefficient one.

**2. A first-neighbor identity for the separation-two pair.** The same recurrences imply
\[
P_{2^r+3}(X)=XP_{2^{r-1}+1}(X^2)+P_{2^{r-1}+2}(X^2).
\]
The first summand is \(X(A_r(X)-X)\), because \(A_r(X)=X+P_{2^{r-1}+1}(X^2)\). The second is \(A_r(X)-X-X^2\), by one further even-index substitution. Therefore
\[
B_r(X):=P_{2^r+3}(X)=(X+1)A_r(X)-X(1+2X).
\]
Both \(A_r\) and \(B_r\) are monic, of respective degrees \(d\) and \(d+1\).

**3. The integer-gcd identity.** For any integer \(t\), the constant coefficient of \(A_r\) is one, hence \(\gcd(A_r(t),t)=1\). The identity in step 2 yields
\[
\gcd(A_r(t),B_r(t))
=\gcd(A_r(t),t(1+2t))
=\gcd(A_r(t),1+2t).
\]
Let \(m=2t+1\), which is odd, so \(2\) is invertible modulo \(|m|\). Since \(2t\equiv-1\pmod m\), evaluating the degree-\(d\) polynomial \(A_r\) gives
\[
2^d A_r(t)\equiv2^d A_r(-1/2)
=2^{d-1}+\sum_{j=1}^{r-1}2^{d-2^j}
=R_r\pmod m.
\]
Multiplication by \(2^d\) does not change the gcd with odd \(m\). Thus \(\gcd(A_r(t),m)=\gcd(R_r,m)\), proving the boxed identity for all integers \(t\).

**4. Complete divisor frequencies and sharp period.** The exponents \(d-1,d-2,d-4,\ldots,d-2^{r-1}=0\) are distinct nonnegative integers; hence \(R_r\) has exactly \(r\) one-bits and is odd. The transformation \(t\mapsto2t+1\) is a bijection modulo the odd integer \(R_r\). The number of residue classes \(u\pmod{R_r}\) with \(\gcd(u,R_r)=e\) is \(\varphi(R_r/e)\), for every divisor \(e\mid R_r\), and is zero otherwise. This proves the spectrum and its exact frequencies.

To show minimality of the period, note that there is a unique residue \(t_0\pmod{R_r}\) satisfying \(2t_0+1\equiv0\pmod{R_r}\), so the gcd at \(t_0\) is \(R_r\). Any period \(h>0\) must also give this maximum at \(t_0+h\), forcing \(R_r\mid2h\), hence \(R_r\mid h\). The stated period \(R_r\) is therefore least.

**5. Resultant and modular collision interpretation.** Reducing \(B_r\) modulo \(A_r\) and using the multiplicativity of the resultant,
\[
\operatorname{Res}(A_r,B_r)=\operatorname{Res}(A_r,-X(1+2X)).
\]
If \(\alpha\) runs over the \(d\) complex roots of the monic polynomial \(A_r\), with multiplicities, then
\[
\operatorname{Res}(A_r,B_r)
=\prod_{A_r(\alpha)=0}[-\alpha(1+2\alpha)].
\]
Because \(A_r(0)=1\), we have \(\prod\alpha=(-1)^d\). The product therefore equals \(\prod(1+2\alpha)=(-1)^d2^d A_r(-1/2)=R_r\), since \(d\) is even. Both input polynomials are monic over the integers, so their degrees remain unchanged modulo every prime. The standard resultant criterion over a field therefore gives exactly the asserted common-root equivalence over \(\overline{\mathbb F_p}\). This is an algebraic-closure statement; no claim that the common root belongs to \(\mathbb F_p\) is made.

## Verification

The accompanying standalone Python 3 script `verify.py`, using only the standard library, independently constructs the Stern polynomials from their coefficient recurrence. It verifies the explicit polynomial identity and binary weight for \(2\le r\le8\), then compares exact integer gcds against the predicted formula at 119 parameter values per index (including negative and large parameters). For \(2\le r\le5\), it also computes the full signed Sylvester determinant via exact fraction-free elimination and tests modular polynomial gcds at 25 primes; for \(2\le r\le4\), it exhaustively checks one entire predicted parameter period. The terminal status is `VERIFY_OK` with 1158 exact finite comparisons, four Sylvester determinants, and seven polynomial identities. All-integer quantifiers rely on the proof, not on these finite tests.

## Relationship to prior work

The recurrence and the canonical sparse dyadic polynomial are already present in the foundational literature. Dilcher and Ericksen (2014) analyze factorization, cyclotomic factors, discriminants and zeros; their resultants occur as a tool for **self-discriminants**, whereas the present identity concerns the integer resultant and value gcd of two **different** dyadic-index polynomials. Dilcher and Ericksen (2015) develop the extended hyperbinary polynomial family, its structure and degrees, without a separation-two evaluation-gcd classification in the inspected article. Beck and Dilcher (2021, published 2022) study coefficient matrices, inverse matrices and associated combinatorial identities; their inspected text does not state the exact all-parameter gcd law or the related resultant. The elementary resultant criterion and totient counting are standard and are not asserted new.

## Limitations

This theorem concerns the specified separation-two dyadic-index family, not arbitrary Stern-polynomial pairs. It does not factor \(R_r\) for all \(r\), estimate the number of its distinct prime factors, or assert that a shared modular root lies in the prime field. The complete 2007 foundational article was available only in publisher preview, and older or unindexed equivalent identities could still exist. The mathematical proof is exact; the finite checker is supporting reproducibility evidence and not an independent mathematical audit.

## References

1. G. Beck and K. Dilcher, *A Matrix Related to Stern Polynomials and the Prouhet–Thue–Morse Sequence*, arXiv:2106.10400v1 (first posted 2021-06-19); *Integers* 22 (2022), A42. https://arxiv.org/abs/2106.10400.
2. K. Dilcher and L. Ericksen, *Reducibility and irreducibility of Stern (0,1)-polynomials*, *Communications in Mathematics* 22 (2014), 77–102. https://dml.cz/handle/10338.dmlcz/143908.
3. K. Dilcher and L. Ericksen, *Hyperbinary Expansions and Stern Polynomials*, *Electronic Journal of Combinatorics* 22(2) (2015), P2.24. https://doi.org/10.37236/4822.
4. K. Dilcher and K. B. Stolarsky, *A polynomial analogue to the Stern sequence*, *International Journal of Number Theory* 3 (2007), 85–103. https://doi.org/10.1142/S179304210700081X.
