# Sharp antipodal rigidity below two-thirds of a cyclotomic period

## Finding
For an integer \(h\ge0\), put \(t=2^h\) and \(N=30t\). If a nonzero polynomial \(F\in\mathbb R_{\ge0}[X]\) is divisible by the cyclotomic polynomial \(\Phi_N\), define its **support diameter** by
\[
D(F)=\max\{j:[X^j]F>0\}-\min\{j:[X^j]F>0\}.
\]
Then the following exact subcritical-cone classification holds:
\[
D(F)<20t \quad\Longleftrightarrow\quad
F(X)=X^b(1+X^{15t})A(X),
\]
where \(b\ge0\) is an integer, \(A\) is a nonzero polynomial with nonnegative real coefficients, \(A(0)>0\), and \(\deg A<5t\). The representation is unique. In the converse direction, the displayed factorization is assumed and then both the cyclotomic divisibility and the claimed diameter follow.

The threshold is sharp: the nonnegative polynomial
\[
T_t(X)=1+X^{10t}+X^{20t}
\]
is divisible by \(\Phi_{30t}\), has diameter \(20t\), and is not an antipodal pair mixture of the displayed subcritical type. Thus precisely at two-thirds of the cyclotomic period, non-antipodal positive relations first become possible.

An exact enumerative consequence is that normalized zero-one polynomials with constant coefficient one and diameter exactly \(15t+k<20t\) number \(1\) at \(k=0\) and \(2^{k-1}\) for \(1\le k<5t\). In total, the number of normalized zero-one multiples in the half-open diameter window is \(2^{5t-1}\).

## Assumptions and scope
The parameter \(h\) ranges over all nonnegative integers; equivalently \(N=30,60,120,240,\ldots\). Polynomial divisibility means ordinary divisibility in \(\mathbb R[X]\), not merely vanishing at one selected primitive root with arbitrary real weights. The condition on diameter concerns the difference between the largest and smallest exponents with positive coefficients, and is invariant under a monomial shift. No integrality assumption on the positive coefficients is needed. For uniqueness, \(b\) is always the smallest exponent in the support and \(A(0)>0\).

## Proof
**Step 1: a positive dual certificate for the order-thirty polynomial.** The cyclotomic polynomial is
\[
P(X)=\Phi_{30}(X)=X^8+X^7-X^5-X^4-X^3+X+1.
\]
For each integer \(0\le j\le19\), let \(r_j(X)\) be the remainder of \(X^j\) upon division by \(P\). The linear functional on degree-at-most-seven polynomials
\[
\mathcal L(R)=2[X^5]R+[X^6]R+[X^7]R
\]
has the following **exact** values, obtained using the single relation
\[
X^8\equiv-X^7+X^5+X^4+X^3-X-1\pmod P:
\]
\[
\bigl(\mathcal L(r_0),\ldots,\mathcal L(r_{19})\bigr)
=(0,0,0,0,0,2,1,1,1,2,2,1,1,1,2,0,0,0,0,0).
\]
This is a finite identity of integer polynomials, not a numerical approximation. If \(G(X)=\sum_{j=0}^{19}c_jX^j\) has \(c_j\ge0\) and \(P\mid G\), linearity gives
\[
0=\mathcal L(G\bmod P)=2c_5+c_6+c_7+c_8+2c_9+2c_{10}+c_{11}+c_{12}+c_{13}+2c_{14}.
\]
Every term is nonnegative, so all ten coefficients \(c_5,\ldots,c_{14}\) vanish. Hence \(G=A_0+X^{15}B_0\), where both blocks have degrees at most four and nonnegative coefficients. As \(X^{15}\equiv-1\pmod P\), the divisibility condition now says \(P\mid(A_0-B_0)\). Its degree is at most four, strictly smaller than \(\deg P=8\), and therefore \(A_0=B_0\). This proves
\[
G=(1+X^{15})A_0,\qquad A_0\in\mathbb R_{\ge0}[X],\quad\deg A_0\le4.
\]
Conversely, \(P\mid(1+X^{15})\), so every such product is a nonnegative multiple.

**Step 2: dyadic lifting.** For every power \(t=2^h\), the cyclotomic identity
\[
\Phi_{30t}(X)=\Phi_{30}(X^t)=P(X^t)
\]
follows from the orders of primitive roots (or by iterating the identity \(\Phi_{2m}(X)=\Phi_m(X^2)\) for even \(m\)). Remove the initial monomial from \(F\), obtaining \(F_0\) with positive constant coefficient and \(\deg F_0=D(F)<20t\). Decompose its exponents into residues modulo \(t\):
\[
F_0(X)=\sum_{r=0}^{t-1}X^r G_r(X^t),\qquad\deg G_r\le19
\]
for each nonzero block. Since \(P(X^t)\) divides \(F_0\), polynomial division, which preserves residue classes modulo \(t\), gives \(P(Y)\mid G_r(Y)\) for every \(r\). Step 1 shows that
\[
G_r(Y)=(1+Y^{15})A_r(Y),\qquad\deg A_r\le4,
\]
with nonnegative real coefficients. Therefore
\[
F_0(X)=(1+X^{15t})A(X),\qquad
A(X)=\sum_{r=0}^{t-1}X^r A_r(X^t),\quad \deg A<5t.
\]
Its constant coefficient is positive. Conversely, any such \(A\) produces a nonnegative multiple of \(P(X^t)\), and the two shifted copies of its support are disjoint. Thus \(D(F)=15t+\deg A<20t\). The first exponent determines \(b\), and polynomial division determines \(A\) uniquely.

**Step 3: optimality.** A primitive \(30t\)-th root raised to the power \(10t\) has order three. Thus \(T_t\) vanishes at every primitive \(30t\)-th root, so \(\Phi_{30t}\mid T_t\). Its middle exponent \(10t\) lies strictly between the two blocks permitted by Step 2, so it is not an antipodal mixture. Its diameter is exactly \(20t\), proving that the strict cutoff cannot be increased.

**Step 4: exact zero-one distribution.** In the displayed factorization, the two coefficient blocks never overlap. Hence \(F\) has coefficients in \(\{0,1\}\) if and only if \(A\) does. For the normalized case \(F(0)=1\), necessarily \(A(0)=1\). If \(\deg A=k\), then \(A_k=1\) as well; the \(k-1\) coefficients strictly between the endpoints are free binary choices. This gives \(1\) polynomial for \(k=0\) and \(2^{k-1}\) for each \(1\le k<5t\). Summing gives \(2^{5t-1}\).

## Verification
The accompanying standalone `verify.py` uses only Python's standard library and exact integers. It reconstructs \(\Phi_{30}\), checks the twenty-entry dual certificate, and exhaustively traverses all \(2^{20}\) binary masks of degrees at most nineteen. Exactly thirty-two masks, counting the zero polynomial, are divisible by \(\Phi_{30}\); the nonzero ones are precisely the positive antipodal-pair mixtures. It also verifies the cyclotomic lifting identity, two boundary witnesses, and sample positive coefficient mixtures for \(N=30,60,120,240,480\). The complete proof above is algebraic and holds for all \(h\); these computations are finite cross-checks, not a substitute for proof.

## Relationship to prior work
Tan and Zhang (2026, Theorem 1.1) prove the general minimum-diameter bound and classify equality. Applied to this family, their result gives the minimum \(15t\) but does not classify all positive multiples in the longer interval \(15t\le D<20t\). Their Section 5 bounds concentration near equality rather than identifying an exact subcritical positive cone. The new result gives an explicit half-open phase transition with a sharp first non-antipodal threshold, and the entire binary-mask diameter distribution.

Steinberger (2012, Theorem 1) established minimum degree for even indices; the Rédéi–de Bruijn–Schoenberg cone decomposition cited there applies to moduli with two distinct prime factors, while the present order has three. Lam and Leung (2000, Theorems 3.1, 3.3, 4.8, 6.5 and Example 6.7) analyze vanishing sums and describe an asymmetric six-term order-thirty relation. Its known support can be shifted into \(\{0,1,7,13,19,20\}\), so it itself reaches the threshold \(20\). Their weight and minimal-sum results do not supply the all-coefficient lower-diameter exclusion proved here. The exact witness is not claimed as new.

OEIS A321419 counts vanishing multisets by the **number** of terms; this does not determine their permitted arc lengths or the real positive cone. We claim neither the classical cyclotomic identity nor the three-point witness as new.

## Limitations
This proves a sharp statement only for the dyadic tower \(N=30\cdot2^h\) and for actual cyclotomic divisibility. No assertion is made for arbitrary indices containing three distinct primes, or for real-coefficient polynomials that vanish at one primitive root without polynomial divisibility. External independent audit has not been performed. Historical priority remains subject to possible unindexed formulations or stronger earlier cone classifications.

## References
1. H. Tan and Y. Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646v1, first posted September 7, 2026, especially Theorem 1.1 and Section 5. https://arxiv.org/abs/2609.07646
2. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1, originally posted November 13, 1995; published as *On Vanishing Sums of Roots of Unity*, Journal of Algebra 224 (2000), 91–109, especially Sections 3, 4, and 6. https://arxiv.org/abs/math/9511209
3. J. P. Steinberger, *The Lowest-Degree Polynomial with Nonnegative Coefficients Divisible by the n-th Cyclotomic Polynomial*, Electronic Journal of Combinatorics 19 (2012), P1. https://doi.org/10.37236/2755
4. OEIS A321419, *Number of n element multisets of the 30th roots of unity with zero sum*. https://oeis.org/A321419
