# Sharp simultaneous generalized-Fermat divisibility threshold

## Finding

For an even integer \(b\ge2\) and positive integers \(c,d\) with \(c\mid d\) and \(d/c\) even, define

\[
K_b(c,d)=\min\{k\in\mathbb Z_{\ge1}:\exists n\in\mathbb Z_{\ge1},\ (b^c+1)(b^d+1)\mid kb^n+1\}.
\]

Then the minimum exists, and its exact value and an attaining exponent are

\[
\boxed{K_b(c,d)=b^d+b^c+1,\qquad n=d-c.}
\]

There are no restrictions on the primality of either divisor, on the coefficient \(k\), or on \(kb^n+1\). The result includes both generalized Fermat numbers and their composite analogues. In particular, for conventional Fermat numbers with \(0\le a<e\), setting \(b=2\), \(c=2^a\), \(d=2^e\) gives an exact simultaneous-divisor threshold without requiring either Fermat number to be prime.

## Assumptions and scope

All symbols \(b,c,d,k,n\) denote ordinary positive integers. The base \(b\) is even, \(c\mid d\), and \(d/c\in2\mathbb Z_{\ge1}\), hence \(d\ge2c\). Set \(A=b^c\), \(D=b^d\), \(C=A+1\) and \(B=D+1\). Both \(B\) and \(C\) are odd. Since \(D\equiv1\pmod C\), their greatest common divisor divides \(2\), and consequently \(\gcd(B,C)=1\). The divisibility condition by \(BC\) is therefore equivalent to simultaneous divisibility by \(B\) and \(C\).

The output is a **least coefficient** over all positive exponents; it is not a primality theorem or a classification of all solutions. The special case \(d/c\) odd is excluded, since then \(C\mid B\), changing the arithmetic problem.

## Proof

**Existence and sharp upper bound.** Put \(k_0=D+A+1\) and \(n_0=d-c\). The exact integer identity

\[
 (D+A+1)b^{d-c}+1=(D+1)(b^{d-c}+1)
\]

holds because \(A=b^c\). Since \((d-c)/c=d/c-1\) is odd, the factor \(b^c+1\) divides \(b^{d-c}+1\). Therefore \(BC\mid k_0b^{n_0}+1\), and \(K_b(c,d)\le k_0\).

**Exclusion below the bound.** Suppose \(1\le k<k_0\) and \(n\ge1\), with \(B\mid kb^n+1\). Since \(b^d\equiv-1\pmod B\), the residue \(-b^{-n}\pmod B\) belongs to the signed-power orbit

\[
\{b^j,-b^j:0\le j<d\}.
\]

More precisely, according to \(n\pmod{2d}\), one can choose \(j\in\{0,\ldots,d-1\}\) such that **either**

\[
 k\equiv b^j\pmod B,\qquad n+j\equiv d\pmod{2d},
\]

**or**

\[
 k\equiv-b^j\pmod B,\qquad n+j\equiv0\pmod{2d}.
\]

This follows directly by reducing \(n\) modulo \(2d\): for residues \(1\le r\le d\), use \(j=d-r\), and for residues \(d<r<2d\) use \(j=2d-r\); for \(r=0\) use \(j=0\). Because \(0<b^j<B\) and \(0<k<k_0<2B\), all possible positive representatives are

\[
 b^j,\quad B+b^j,\quad B-b^j,\quad 2B-b^j.
\]

The last possibility lies above the proposed cutoff: for every \(j<d\),

\[
 2B-b^j\ge2(D+1)-b^{d-1}>D+A+1=k_0.
\]

The strict inequality follows from \((b-1)b^{d-1}\ge b^c=A\), since \(b\ge2\) and \(d\ge2c\). Hence only the first three types can occur. For the type \(B+b^j\), the assumed strict upper bound implies \(b^j<A\), so \(j<c\).

In all cases, \(n+j\) is a multiple of \(2c\), since \(2c\mid d\). Thus \(b^{n+j}\equiv1\pmod C\), and also \(B\equiv2\pmod C\).

If \(k=b^j\), then \(kb^n+1\equiv2\pmod C\), impossible because \(C\ge3\) is odd.

If \(k=B-b^j\), multiplying \(kb^n+1\) by the unit \(b^j\pmod C\) gives

\[
 b^j(kb^n+1)\equiv(2-b^j)b^{n+j}+b^j\equiv2\pmod C,
\]

again impossible.

Finally, if \(k=B+b^j\), necessarily \(j<c\), and

\[
 b^j(kb^n+1)\equiv(2+b^j)b^{n+j}+b^j\equiv2(1+b^j)\pmod C.
\]

Since \(C\) is odd, the required divisibility would imply \(C\mid1+b^j\), contradicted by \(0<1+b^j<C\) for \(j<c\).

Thus no \(k<k_0\) can satisfy even the two separate necessary congruences. Together with the explicit attaining construction, this proves the formula for all stated parameters.

## Verification

The standalone `verify.py` independently enumerates the entire cyclic set of exponents \(1\le n\le2d\), computing the least positive coefficient residue \(k_n\equiv-b^{-n}\pmod{(b^c+1)(b^d+1)}\) using modular inversion and confirming that its minimum is the formula. It checks 300 parameter triples with even bases \(2\le b\le20\), \(1\le c\le6\), and even quotients \(2\le d/c\le10\), restricted to \(d\le60\). It separately brute-forces smaller coefficients and exponents over a bounded set of small examples. These finite checks corroborate but do not replace the complete symbolic proof.

Example: for \(b=2,c=1,d=2\), the two divisors are \(3\) and \(5\); their product divides \(7\cdot2^1+1=15\), and no coefficient below \(7\) works at any positive exponent.

## Relationship to prior work

Cilleruelo, Luca and Pizarro-Madariaga (arXiv:1305.3580, Lemma 2) bound **one prime Fermat divisor** of \(2^nk+1\) by \(k^2\); their theorem classifies Carmichael-number occurrences rather than determining the least coefficient forced by two designated Fermat factors. Florian Luca (arXiv:2606.28829, Sections 1–2) uses prime Fermat factors to bound possible Carmichael numbers of \(2^np^m+1\). Tiebekabe (arXiv:2609.25104, Theorem 1.3) extends a multiplicative-independence obstruction to even bases but does not give a simultaneous two-modulus coefficient minimum. A subsequent manuscript (arXiv:2611.24275, Theorem 3, initially public after November 15, 2026) sharpens the bound for a **single Fermat prime factor** to \(q<2k\) and likewise does not imply the exact pairwise bound. The present classification uses only the elementary modular structure of the two coprime plus-one factors.

A targeted search of related mathematical records and indexed literature did not locate the exact simultaneous-minimum theorem; absence from search results is not proof of priority. General cyclotomic-divisibility literature may contain a disguised equivalent.

## Limitations

The theorem does not imply that the attaining number is prime or Carmichael; generally it is composite by construction. It addresses a pair of moduli with nested exponents and even ratio, not arbitrary collections of generalized Fermat factors. When the exponent ratio is odd, the smaller plus-one factor divides the larger and the claimed formula need not hold. The stand-alone finite checker tests examples only, while the preceding proof handles all admissible integers. Priority with respect to unindexed general CRT and cyclotomic results remains open to independent assessment.

## References

- J. Cilleruelo, F. Luca, A. Pizarro-Madariaga, *Carmichael numbers in the sequence \((k2^n+1)_{n\ge1}\)*, arXiv:1305.3580 (first public 2013-05-15), Lemma 2 and Theorems 1–2. https://arxiv.org/html/1305.3580v1
- F. Luca, *On Carmichael numbers of the form \(2^np^m+1\)*, arXiv:2606.28829 (first public 2026-06-27). https://arxiv.org/abs/2606.28829
- P. Tiebekabe, *Carmichael numbers of the form \(2^np^m+1\) with odd exponent \(m\)*, arXiv:2609.25104 (first public 2026-09-20), Theorem 1.3. https://arxiv.org/abs/2609.25104
- J. L. Randrianantenaina, A. K. Uncu, *One more curious property of 1729*, arXiv:2611.24275 (first public 2026-11-18), Theorem 3; subsequent related literature, not the motivating source. https://arxiv.org/html/2611.24275v1
