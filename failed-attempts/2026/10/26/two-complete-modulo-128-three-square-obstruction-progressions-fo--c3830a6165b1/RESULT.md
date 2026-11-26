# Two complete modulo-128 three-square obstruction progressions for two-colour binary partitions

## Finding
Let \(b_2(n)\) count partitions of the nonnegative integer \(n\) into powers of two, with each individual part independently assigned one of two colors. Then
\[
 b_2(128n+36)\equiv b_2(128n+62)\equiv112\pmod{128}
 \qquad(n\ge0).
\]
Conversely, if \(r\in\{0,\ldots,127\}\) and \(b_2(128n+r)\equiv112\pmod{128}\) for every \(n\ge0\), then \(r\in\{36,62\}\). The two progressions therefore constitute the complete set of universally residue-112 progressions at modulus \(128\).

Because \(112=16\cdot7\), every partition count in these progressions is of the forbidden three-square form \(4^2(8s+7)\) with \(s\ge0\). Thus none can be expressed as a sum of three integer squares. The set of obstructed indices has lower natural density at least \(2/128=1/64\). The exact overall density is not determined.

## Assumptions and scope
All power series below are formal over integers or the indicated residue ring. Set
\[
 B(y)=\sum_{n\ge0}b_2(n)y^n
 =\prod_{j\ge0}(1-y^{2^j})^{-2},\qquad
 T(y)=\prod_{j\ge0}(1-y^{2^j}).
\]
Thus \(B=T^{-2}\). A congruence between formal series means coefficientwise congruence; no analytic convergence is required. The argument holds for every integer \(n\ge0\), not only a finite range.

## Proof
**1. A periodic description of the square of the Thue–Morse series.** Let
\[
 P(y)=1+6y+7y^2+4y^3+5y^4+2y^5+3y^6.
\]
The exact polynomial identity
\[
 P(y)(1+y^8)-(1-y)^2P(y^2)\in8\mathbb Z[y]
\]
is verified by expansion (and by the attached integer-arithmetic checker). Since \(T(y)^2=(1-y)^2T(y^2)^2\), the formal series \(R(y)=P(y)/(1-y^8)\) satisfies the same functional equation modulo \(8\). Both \(T(y)^2\) and \(R(y)\) have constant coefficient \(1\). The solution with prescribed constant term is unique, because in any difference \(H(y)=(1-y)^2H(y^2)\) of two solutions, the coefficient of degree \(m\ge1\) depends only on coefficients of smaller degrees, and hence vanishes inductively. Consequently
\[
 T(y)^2\equiv\frac{P(y)}{1-y^8}\pmod8.
 \tag{1}
\]

**2. A finite rational numerator for the seven low binary-part sizes.** Define
\[
 U(y)=\prod_{j=0}^{6}\left(\sum_{k=0}^{2^{7-j}-1}y^{k2^j}\right)^2.
\]
Each finite geometric sum equals \((1-y^{128})/(1-y^{2^j})\). Splitting the partition generating product at exponent \(128\) yields the exact identity
\[
 B(y)=\frac{U(y)}{(1-y^{128})^{14}} B(y^{128}). \tag{2}
\]
The polynomial \(U\) has degree \(1538\). For \(r\in\{0,\ldots,127\}\) define its residue extraction
\[
 V_r(z)=\sum_{k\ge0}[y^{128k+r}]U(y)\,z^k.
\]
An exact integer convolution of the seven explicit finite squared geometric sums gives, for **both** \(r=36\) and \(r=62\), the following complete polynomial congruence:
\[
 V_r(z)\equiv112+112z+16z^2+16z^3+96z^4+96z^5
 +32z^6+32z^7+48z^8+48z^9+80z^{10}+80z^{11}
 \pmod{128}. \tag{3}
\]
There are no higher coefficients because \(\deg U=1538\). Multiplying the displayed polynomial by \(1-z^8\), and comparing the finitely many coefficients, gives the further exact certificate
\[
 V_r(z)(1-z^8)\equiv112P(z)(1-z)^{13}\pmod{128}. \tag{4}
\]
All \(21\) possible coefficients in (4) are verified by the standalone checker. Equations (3) and (4) are finite polynomial identities, not numerical sampling of the claimed infinite sequence.

**3. Infinite progression congruences.** Extracting the terms of index \(128n+r\) in (2) gives
\[
 \sum_{n\ge0}b_2(128n+r)z^n
 =\frac{V_r(z)}{(1-z)^{14}}B(z).
\]
By (4), the right side is congruent modulo \(128\) to
\[
 \frac{112P(z)}{(1-z)(1-z^8)}B(z)
 \equiv\frac{112T(z)^2B(z)}{1-z}
 =\frac{112}{1-z}.
\]
The second congruence uses (1): multiplying a congruence modulo \(8\) by \(112=16\cdot7\) makes it valid modulo \(128\). Coefficient comparison proves both progression formulas for every \(n\ge0\).

**4. Completeness among residue-112 progressions modulo \(128\).** Direct application of the exact recurrence
\[
 b_2(0)=1,\qquad b_2(n)=2b_2(n-1)-b_2(n-2)
 +\mathbf1_{2\mid n}\,b_2(n/2) \quad(n\ge1),
\]
where terms with negative index are zero, gives
\[
 \{0\le r<128:b_2(r)\equiv112\pmod{128}\}=\{36,62,96\}.
\]
The same recurrence gives \(b_2(224)\equiv96\pmod{128}\), eliminating \(r=96\) by taking \(n=1\). The preceding infinite identities retain \(36\) and \(62\). This proves the claimed complete classification.

**5. Three-square obstruction.** Legendre's three-square theorem states that a nonnegative integer is not a sum of three integral squares exactly when it has the form \(4^a(8s+7)\), with \(a,s\ge0\). A positive integer congruent to \(112\) modulo \(128\) has valuation exactly \(4\) and odd part congruent to \(7\) modulo \(8\), hence is forbidden. The two disjoint progressions have natural density \(1/64\) collectively, establishing the asserted lower-density bound.

## Verification
Run `python3 verify.py` using a standard Python 3 interpreter. It reconstructs \(U\) from the seven squared finite geometric sums, checks (1) via the defining polynomial functional equation, checks the two complete degree-20 identities (4) modulo \(128\), and independently computes the defining recurrence through \(128\cdot80+62\). It also checks the finite candidate classification using initial coefficients. The polynomial identities, together with the symbolic generating-function argument above, certify the all-index result; the direct recurrence sampling is supplemental.

## Relationship to prior work
Gawron, Miska, and Ulas developed the colored binary-partition generating functions and their extracted rational forms, and proved several exact valuation progressions for \(b_2\) (Theorem 5.4, arXiv:1703.01955). Their listed progressions control valuations, not the particular residue \(112\) modulo \(128\) on \(36\) and \(62\). The general generating-function machinery informs the present finite-polynomial method, so the claim is not that the method itself is new.

Sobolewski and Ulas studied three-square representability of \(b_m(n)\) for \(m=2^k-1\) and explicitly posed the remaining general-\(m\) characterization (Problem 7.2, arXiv:2211.16622). They did not state these \(m=2\) obstruction progressions. The present result supplies two explicit positive-density obstruction classes in that unresolved case; it does not settle their global characterization question.

## Limitations
The assertion concerns only the exact residue \(112\) modulo \(128\), and it classifies only residue classes forcing that residue at modulus \(128\). Other three-square obstructions, including those with different valuations, remain unclassified. The lower density \(1/64\) is not asserted optimal. No publication-priority or independent validation claim is made.

## References
1. M. Gawron, P. Miska, M. Ulas, *Arithmetic properties of coefficients of power series expansion of the Thue–Morse product*, arXiv:1703.01955, first submitted 6 March 2017; *Monatshefte für Mathematik* 185 (2018), 307–360. See Theorems 4.13, 5.4 and discussion of extracted generating functions.
2. B. Sobolewski, M. Ulas, *Values of binary partition function represented by a sum of three squares*, arXiv:2211.16622, first submitted 29 November 2022; *Results in Mathematics* 78 (2023), article 188. See §§1, 2 and Problem 7.2.
3. A.-M. Legendre, classical three-square theorem (nonrepresentability criterion).
