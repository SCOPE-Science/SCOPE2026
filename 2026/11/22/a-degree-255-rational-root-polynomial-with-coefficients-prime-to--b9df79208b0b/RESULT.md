# A degree-255 rational-root polynomial with coefficients prime to ten

## Finding
Let
\[
F(X)=(X-1)^{112}(X+1)^{143}=\sum_{j=0}^{255}c_jX^j\in\mathbb Z[X].
\]
For every integer \(j\) with \(0\le j\le255\), one has \(\gcd(c_j,10)=1\). All roots of \(F\) lie in \(\{1,-1\}\). Consequently, if \(B_{2,5}\) is any integer such that every nonzero polynomial over \(\mathbb Z\) having only rational roots and no coefficient divisible by either \(2\) or \(5\) has degree at most \(B_{2,5}\), then \(B_{2,5}\ge255\).

This is a constructive lower bound for the prime pair \(\{2,5\}\) in Problem 1 of Hajdu, Tijdeman and Varga (2023); it does not assert that such a finite bound exists.

## Assumptions and scope
A coefficient is counted even if its integer value is negative; requiring \(\gcd(c_j,10)=1\) also ensures no coefficient is zero. The result concerns a single explicit, monic degree-\(255\) polynomial with the rational roots \(1\) and \(-1\), of multiplicities \(112\) and \(143\). No statement of extremality or classification for other polynomials or other degrees is made.

## Proof
**Parity.** In \(\mathbb F_2[X]\), the two linear factors coincide, and the characteristic-two Frobenius identity gives
\[
\overline F(X)=(1+X)^{255}=\frac{1+X^{256}}{1+X}=\sum_{j=0}^{255}X^j.
\]
Thus all \(256\) coefficients are odd.

**Reduction modulo five.** Since \(112=2+2\cdot5+4\cdot25\) and \(143=3+3\cdot5+125\), the characteristic-five Frobenius identity yields
\[
\overline F(X)=A(X)A(X^5)B(X^{25})(1+X^{125}),
\]
where
\[
A(X)=(X-1)^2(X+1)^3\equiv1+X+3X^2+3X^3+X^4+X^5\pmod5,
\]
\[
B(X)=(X-1)^4\equiv1+X+X^2+X^3+X^4\pmod5.
\]
Write \(A(X)=\sum_{i=0}^5a_iX^i\), with \((a_0,\ldots,a_5)=(1,1,3,3,1,1)\) modulo \(5\), and \(H(X)=A(X)A(X^5)=\sum_{j=0}^{30}h_jX^j\). For \(1\le r\le4\), the coefficient of \(X^{5i+r}\) in \(H\) is either \(a_ra_i\), when \(0\le i\le5\), or zero outside its degree range. In the residue class \(r=0\), the coefficients are \(a_0a_i+a_5a_{i-1}=a_i+a_{i-1}\) for \(1\le i\le5\), together with the boundary values \(h_0=a_0^2=1\) and \(h_{30}=a_5^2=1\). These successive neighbor sums are
\[
(2,4,1,4,2)\pmod5,
\]
so every coefficient of \(H\) is nonzero modulo five. Its first and last six coefficients (low to high degree) are, respectively,
\[
(h_0,\ldots,h_5)=(1,1,3,3,1,2),\qquad
(h_{25},\ldots,h_{30})=(2,1,3,3,1,1).
\]
Their componentwise sums are \((3,2,1,1,2,3)\), also all nonzero modulo \(5\).

Now put
\[
G(X)=H(X)B(X^{25})=\sum_{i=0}^4 X^{25i}H(X).
\]
Each coefficient of \(G\) is either one coefficient of \(H\), or an overlap sum \(h_r+h_{25+r}\) for some \(0\le r\le5\). The preceding calculation proves that every coefficient of \(G\), of degrees \(0\) through \(130\), is nonzero modulo five. Moreover, its initial six coefficients are \((h_0,\ldots,h_5)\) and its terminal six coefficients are \((h_{25},\ldots,h_{30})\), because the shifted copies overlap only at the other ends. Finally,
\[
\overline F(X)=G(X)+X^{125}G(X).
\]
The two summands overlap only in degrees \(125\) through \(130\), where the coefficients are again the six nonzero sums \((3,2,1,1,2,3)\) modulo five. All remaining coefficients come from a single nonzero coefficient of \(G\). Thus no coefficient of \(F\) is divisible by \(5\). Together with the parity result this proves \(\gcd(c_j,10)=1\) for all \(j\).

The displayed factorization gives exactly the claimed rational roots, and degree \(112+143=255\) proves the lower-bound consequence.

## Verification
The standalone Python 3 checker `verification.py` constructs all \(256\) coefficients independently by exact iterated multiplication modulo \(10\), checks their residue histogram, and reconstructs the characteristic-five Frobenius factorization via polynomial convolution. It checks all \(256\) coefficients of both expressions and confirms that the overlap proof gives no zero residues. To reproduce, run `python3 verification.py` from the directory containing this file. The expected output begins with `VERIFY_OK` and includes the four nonzero residue counts modulo ten. The proof above, not the finite checker alone, establishes the exact claim.

## Relationship to prior work
Hajdu, Tijdeman and Varga, *On polynomials with only rational roots* (first published June 9, 2023), Theorem 1.2, give the sharp degree bound \(3\) under the **different** condition that no coefficient is divisible by either \(2\) or \(3\). Their Problem 1 asks whether some degree bound exists for *each* pair of primes. The present construction exhibits a concrete lower bound at \(\{2,5\}\), rather than proving existence or nonexistence of a finite upper bound. Their use of Fine's parity lemma and their prime-three coefficient analysis do not assert the prime-five example above. The direct Lucas/Frobenius coefficient argument is included so the example can be checked without a large expansion.

## Limitations
No global upper bound, maximum admissible degree, or infinite sequence of admissible degrees is proved for the pair \(\{2,5\}\). A lower-bound witness does not settle the cited open problem. Searches cannot establish that the identical polynomial or an equivalent high-degree witness has never appeared in unindexed literature; independent priority review is still needed. The value of the result is confined to a concrete, structurally verified obstruction for this prime pair.

## References
1. L. Hajdu, R. Tijdeman and N. Varga, “On polynomials with only rational roots,” *Mathematika* 69 (2023), 867–878, first published June 9, 2023, DOI: 10.1112/mtk.12209. Full text: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/mtk.12209.
2. N. J. Fine, “Binomial coefficients modulo a prime,” *American Mathematical Monthly* 54 (1947), 589–592. Referenced for parity context by Hajdu–Tijdeman–Varga; the present proof is self-contained.
