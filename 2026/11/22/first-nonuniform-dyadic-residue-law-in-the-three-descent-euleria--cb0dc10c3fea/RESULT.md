# First nonuniform dyadic residue law in the three-descent Eulerian column

## Finding
For the Eulerian number \(A(n,3)\), the number of permutations of \(n\) elements with exactly three descents, fix any integer \(k\ge4\), a residue \(y\bmod 2^k\), and a starting index \(N\ge k\). Then the exact fiber law is
\[
\#\{n:N\le n<N+2^{k+1},\ A(n,3)\equiv y\pmod{2^k}\}=1+8\mathbf1_{\{y\equiv0,10\pmod{16}\}}.
\]
The least eventual index period modulo \(2^k\) equals \(2^{k+1}\). In particular the output reaches all residues, but exactly two of the sixteen residue balls carry nine times the multiplicity of the others. For each fixed \(y\), the natural density of indices giving that residue is the displayed count divided by \(2^{k+1}\).

## Assumptions and scope
The Eulerian numbers use the classical convention \(A(n,d)=\sum_{j=0}^{d+1}(-1)^j\binom{n+1}j(d+1-j)^n\) for \(n\ge1\); the recurrence \(A(n,d)=(d+1)A(n-1,d)+(n-d)A(n-1,d-1)\) is equivalent. The claim holds for all \(k\ge4\) and all consecutive blocks beginning at \(N\ge k\), not just blocks starting at multiples of their period. Only the three-descent column is considered; the polynomial-exponential congruence is asserted only from index \(n\ge k\).

## Proof
For every \(n\ge1\), the Eulerian inclusion–exclusion formula gives
\[
A(n,3)=4^n-(n+1)3^n+\binom{n+1}2 2^n-\binom{n+1}3.
\]
For \(n\ge k\), the first and third terms vanish modulo \(2^k\). Put
\[
F(n)=-(n+1)3^n-\frac{n^3-n}6.
\]
Then \(A(n,3)\equiv F(n)\pmod{2^k}\) for all \(n\ge k\). For positive even \(h\), a direct difference calculation yields
\[
\frac{F(x+h)-F(x)}h=-3^x\left(3^h+(x+1)\frac{3^h-1}h\right)-\frac{3x^2+3xh+h^2-1}6.
\tag{1}
\]
By lifting the exponent, \(\nu_2(3^h-1)=\nu_2(h)+2\), so the first summand on the right of (1) is a two-adic integer. If \(x\) is even, the numerator of the second fraction is odd. Hence its valuation is exactly \(-1\), proving
\[
\nu_2(F(x+h)-F(x))=\nu_2(h)-1\quad(x\text{ even},\ h\text{ even}).
\tag{2}
\]
In particular \(t\mapsto F(2t)\) preserves every two-adic distance, and therefore permutes the residues modulo \(2^k\): each output has exactly one even-index preimage in an index interval of length \(2^{k+1}\).

If \(x\) is odd and \(8\mid h\), the first summand of (1) is congruent to \(1\pmod4\): indeed \(3^h\equiv1\pmod4\), \((3^h-1)/h\equiv0\pmod4\), and \(-3^x\equiv1\pmod4\). Meanwhile, as \(x^2\equiv1\pmod8\), the numerator of the second fraction is \(2\pmod8\); its negative quotient by six is \(1\pmod4\). Thus (1) is \(2\pmod4\) in \(\mathbb Z_2\), giving
\[
\nu_2(F(x+h)-F(x))=\nu_2(h)+1\quad(x\text{ odd},\ 8\mid h).
\tag{3}
\]
For each \(r\in\{1,3,5,7\}\), equation (3) proves the map \(t\mapsto(F(r+8t)-F(r))/16\) preserves two-adic distances and therefore is a bijection modulo \(2^j\) for every \(j\ge0\). Hence each such odd-index branch maps onto precisely one full ball \(F(r)+16\mathbb Z_2\), four-to-one modulo \(2^k\) when inputs are counted over a full period \(2^{k+1}\). Direct substitution gives
\[
F(1)\equiv F(5)\equiv10\pmod{16},\qquad F(3)\equiv F(7)\equiv0\pmod{16}.
\]
Thus the four odd branches contribute eight additional preimages to each residue congruent to zero or ten modulo sixteen, and none elsewhere. Adding the unique even preimage proves the formula.

Equation (2) and (3) also imply \(F(n+2^{k+1})\equiv F(n)\pmod{2^k}\). No positive *even* period \(h\) smaller than \(2^{k+1}\) can work: by (2), the difference at every even index has valuation \(\nu_2(h)-1<k\). No odd period can work either: at even indices, the outputs run through every residue modulo sixteen, whereas at odd indices they lie only in two residue classes modulo sixteen. Therefore \(2^{k+1}\) is the least eventual period. The exact periodic histogram proves the natural densities.

## Verification
The companion `verify.py` independently generates Eulerian numbers via their recurrence and checks the closed formula and the exact histograms at every level from \(k=4\) through \(k=10\), including translated blocks and the failure of the half-period. It also checks both two-adic valuation laws on finite samples. The universal theorem follows from (1)–(3), not from finite computation.

## Relationship to prior work
Xiong, Tsao and Hall (2013) give the classical Eulerian-number definitions and related polynomial identities, but their inspected work does not classify residues of the three-descent column modulo powers of two. The earlier exact modular distribution of the *two*-descent column is uniform with two preimages per period; the three-descent column first exhibits a sharply nonuniform, two-ball ramification. A separate exact-fiber theorem for the fixed binomial column \(\binom n3\) concerns a different arithmetic sequence and does not imply this law. OEIS A000498 tabulates the three-descent column but does not supply the all-depth fiber classification.

## Limitations
The formula concerns the three-descent Eulerian column only, all powers \(2^k\) with \(k\ge4\), and indices \(n\ge k\). It does not determine analogous distributions for other descent counts or odd prime powers. Priority against every possible older general theorem on integer-valued exponential polynomials is not guaranteed by the sources inspected.

## References
1. T. Xiong, H.-P. Tsao, J. I. Hall, *General Eulerian Numbers and Eulerian Polynomials*, 2013, DOI: 10.1155/2013/629132, https://onlinelibrary.wiley.com/doi/10.1155/2013/629132 (first publicly dated January 31, 2013).
2. OEIS A000498, classical Eulerian numbers with three descents, https://oeis.org/A000498.
3. Prior indexed result: *Uniform dyadic residues in the two-descent Eulerian column with sharp onset*, indexed mathematical record: Uniform dyadic residues in the two-descent Eulerian column with sharp onset (2026).
