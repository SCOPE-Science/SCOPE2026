# Exact modulo-nine ternary digit law for three-letter Abelian-square numbers

## Finding
Let \(A(n)\) be the number of Abelian squares of length \(2n\) on a three-letter alphabet, with \(A(0)=1\). For every \(n\ge0\) with ternary expansion \(n=\sum_{j\ge0}d_j3^j\), \(d_j\in\{0,1,2\}\), the complete residue law is
\[
A(n)\equiv\prod_{j\ge0} b_{d_j}\pmod9,\qquad (b_0,b_1,b_2)=(1,3,6).
\]
Consequently \(A(0)\equiv1\pmod9\). For \(n>0\), the residue is \(3\) precisely when \(n=3^j\); it is \(6\) precisely when \(n=2\cdot3^j\); otherwise it is \(0\) modulo \(9\). Thus \(\nu_3(A(n))=1\) at precisely the positive indices with a single nonzero ternary digit. Among the \(3^r\) indices \(0\le n<3^r\), there are precisely \(2r\) valuation-one terms and \(3^r-2r-1\) terms divisible by nine, for every integer \(r\ge1\).

The substantive claim is the *full modulo-nine Lucas factorization* and converse exact digit classification, not the previously known lower bound on valuations.

## Assumptions and scope
For \(n\in\mathbb Z_{\ge0}\), define
\[
A(n)=\sum_{i+j+k=n}\left(\frac{n!}{i!j!k!}\right)^2
=\sum_{j=0}^{n}\binom nj^2\binom{2j}{j}.
\]
The sum counts pairs of equal-length words with the same numbers of each of three letters. The empty word is included for \(n=0\). Set
\[
P(x,y)=(1+x+y)(1+x^{-1}+y^{-1})=3+S(x,y),
\]
where \(S=x+x^{-1}+y+y^{-1}+xy^{-1}+x^{-1}y\). Write \(\operatorname{CT}\) for the two-variable Laurent constant term and \(H^{[3]}=H(x^3,y^3)\). Then \(A(n)=\operatorname{CT}P^n\), with no analytic limiting convention.

## Proof
**1. A finite Cartier-projection identity.** Define the integral Laurent polynomial
\[
Q=\frac{P^3-P^{[3]}}3
\]
and, for any Laurent polynomial \(H\), define \(\Pi(H)\) by discarding terms whose two exponents are not both divisible by \(3\), then dividing each retained exponent by \(3\). The explicit finite polynomial computation gives
\[
\boxed{\Pi(QP^d)\equiv dS\pmod3\quad(d=0,1,2).}\tag{1}
\]
For an inspectable finite expansion, let \(U=1+x+y\), \(V=1+x^{-1}+y^{-1}\), and
\[
R_U=(U^3-U^{[3]})/3=x+x^2+y+y^2+x^2y+xy^2+2xy,
\qquad R_V=R_U(x^{-1},y^{-1}).
\]
Then \(Q\equiv R_UV^{[3]}+U^{[3]}R_V\pmod3\). Multiplication by \(P^d\), restriction to exponents in \(3\mathbb Z^2\) and division of both exponents by three yield the following complete three-row table: \(d=0\) gives zero; \(d=1\) gives \(S\); \(d=2\) gives \(2S\), all modulo three. This is a bounded integer-polynomial coefficient check, not an appeal to sampled sequence values. The standalone checker constructs all Laurent coefficients independently and verifies the entire supports in (1).

**2. Ternary recursion.** For \(m\ge1\), \(d\in\{0,1,2\}\), expansion modulo nine gives
\[
P^{3m+d}\equiv P^{[3]m}P^d+3mP^{[3](m-1)}QP^d\pmod9.
\]
Every monomial in \(P^d\) has each coordinate exponent in \([-2,2]\). Hence a term of \(P^d\) with both exponents divisible by three must be constant, so
\[
\operatorname{CT}(P^{[3]m}P^d)=A(m)A(d).
\]
Using the definition of \(\Pi\) and (1),
\[
\begin{aligned}
A(3m+d)&\equiv A(m)A(d)+3md\operatorname{CT}(P^{m-1}S)\pmod9\\
&=A(m)A(d)+3md\bigl(A(m)-3A(m-1)\bigr)\pmod9.
\end{aligned}\tag{2}
\]
Reduction modulo three of (2) gives \(A(3m+d)\equiv A(m)A(d)\pmod3\); the case \(m=0\) holds directly. Because \(A(1)=3\) and \(A(2)=15\), induction on ternary digits proves \(3\mid A(m)\) for all \(m>0\). Thus the correction in (2) is divisible by nine and
\[
\boxed{A(3m+d)\equiv A(m)A(d)\pmod9}
\]
for every \(m\ge0\), \(d\in\{0,1,2\}\). Iterate over the digits of \(n\).

**3. Exact classification and counting.** Every nonzero digit supplies a factor divisible by three, while a zero digit supplies a unit. If there are at least two nonzero digits, their product vanishes modulo nine. If there is exactly one nonzero digit, its factor is either three or six, independently of its position. The zero index has residue one. In a block of \(r\) ternary digits, exactly \(r\) single-one and \(r\) single-two words occur; the remaining \(3^r-2r-1\) positive indices have at least two nonzero digits. All statements follow.

## Verification
The accompanying `checker.py` works over exact integer Laurent polynomials. It constructs \(P\), \(Q\), all three projections in (1), compares direct Laurent constant terms against binomial sums for small indices, and checks the published integer recurrence and the predicted digit law for indices \(0\) through \(1600\). The symbolic coefficient projection and proof of (2) establish the assertion at every index; the finite index tests alone do not prove an infinite theorem. Execute using `python3 checker.py` from the extracted file directory; no extra packages are required.

## Relationship to prior work
Richmond and Shallit [1] introduced the explicit three-letter Abelian-square count and asymptotics; its first public preprint appeared on 31 July 2008. Mellit and Vlasenko [2] developed general Dwork congruences for Laurent constant terms, with modulo-three Lucas factorization. Delaygue [3, Section 1.5] established valuation lower bounds for the same Abelian-square family. In the present three-letter case, that lower bound already implies divisibility by nine whenever the ternary index contains at least two nonzero digits; **it does not determine the residue at a single-nonzero-digit index nor state (2)**. Malik and Straub [4] show ordinary prime-modulus Lucas behavior for sporadic Apéry-like sequences and note that such congruences do not automatically lift to prime powers. Amdeberhan and Tauraso [5, Section 5] consider different, box-truncated multinomial-square sums. None of these inspected statements supplies the specific complete modulo-nine digit factorization in this note. The sequence is OEIS A002893 [6].

## Limitations
This theorem does not determine \(\nu_3(A(n))\) when it is at least two, and it makes no claim about modulo twenty-seven or larger powers of three. It does not claim that the previously known lower bound was new. Earlier or implicit equivalent prime-square congruences might exist, particularly from general Dwork/Cartier identities or specialised hypergeometric-congruence treatments; the literature comparison is not an absolute priority proof. Independent review has not been performed.

## References
[1] L. B. Richmond and J. Shallit, *Counting Abelian Squares*, arXiv:0807.5028 (first version 2008-07-31); *Electronic Journal of Combinatorics* 16 (2009), R72. https://arxiv.org/abs/0807.5028

[2] A. Mellit and M. Vlasenko, *Dwork's congruences for the constant terms of powers of a Laurent polynomial*, arXiv:1306.5811 (2013). https://arxiv.org/abs/1306.5811

[3] E. Delaygue, *Arithmetic properties of Apéry-like numbers*, arXiv:1310.4131 (2013), especially Section 1.5. https://arxiv.org/abs/1310.4131

[4] A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297 (2015), *Research in Number Theory* 2 (2016). https://arxiv.org/abs/1508.00297

[5] T. Amdeberhan and R. Tauraso, *Two Triple binomial sum supercongruences*, arXiv:1607.02483 (2016), Section 5. https://arxiv.org/abs/1607.02483

[6] OEIS A002893, *Sum of squares of multinomial coefficients with three parts*. https://oeis.org/A002893
