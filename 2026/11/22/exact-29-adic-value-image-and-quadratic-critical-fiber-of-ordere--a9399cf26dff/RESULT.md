# Exact 29-adic value image and quadratic critical fiber of ordered Bell numbers

## Finding
For \(F_n=\sum_{j=0}^n j!S(n,j)\), define the *eventual* image \(I_k=\{F_n\bmod29^k:n\ge k\}\), for \(k\ge1\). With
\[
R=\{0,1,3,9,10,13,14,15,17,18,19,20,22,23,25,26\},
\]
we have \(I_1=R\cup\{24\}\). Its full 29-adic image closure is
\[
\left(\bigcup_{r\in R}(r+29\mathbb Z_{29})\right)\ \sqcup\ (\delta+29^2u\mathbb Z_{29}^{2}),
\]
where \(\delta\equiv20672\pmod{29^3}\), \(u\equiv19\pmod{29}\), and \(\mathbb Z_{29}^{2}\) means the set of squares (not the entire group). The first component comprises sixteen full balls; the second lies entirely in the output class \(24\pmod{29}\) and occupies a translated, scaled square image.

Write \(S_0=1\) and, for \(m\ge1\),
\[
S_m=1+14\sum_{j=0}^{\lfloor(m-1)/2\rfloor}29^{m-2j-1}.
\]
Then \(|I_k|=16\cdot29^{k-1}+S_{k-2}\) for every \(k\ge2\). In particular the image sizes for \(k=1,2,3\) are \(17,465,13471\); the closure has additive Haar measure
\[
\frac{16}{29}+\frac{1}{29^2}\frac{29}{2(29+1)}=\frac{961}{1740}.
\]

There is also a full multiplicity statement in a complete eventual index period \(P_k=28\cdot29^{k-1}\): each output \(y\) with \(y\equiv r\pmod{29}\), \(r\in R\), has \(m_r\) preimages where
\[
(m_0,m_1,m_3,m_9,m_{10},m_{13},m_{14},m_{15},m_{17},m_{18},m_{19},m_{20},m_{22},m_{23},m_{25},m_{26})=(1,3,1,2,2,1,3,1,1,1,3,1,1,2,2,2).
\]
On the singular component, the number of preimages equals \(29\) times the number of roots of \(z^2\equiv(y-\delta)/(29^2u)\pmod{29^{k-2}}\), with the modulus-one case defined to have one root. Otherwise the multiplicity is zero.

## Assumptions and scope
All indices are nonnegative integers; for the power \(29^k\), indices smaller than \(k\) are excluded from the eventual image. The exact period \(P_k\) is used only in the eventually periodic range. The center \(\delta\) and unit \(u\) are fixed 29-adic numbers defined by the unique critical branch of the analytic interpolation; their displayed congruences do not define their higher digits. The square-image formula does specify every level unambiguously through those full 29-adic constants. No claim is made about adding possible exceptional early values.

## Proof
**Step 1: a bounded 29-adic moment measure.** Set \(Q=29^e\) and assign the cylinder \(r+Q\mathbb Z_{29}\), \(0\le r<Q\), the 29-adic weight
\[
\mu(r+Q\mathbb Z_{29})=\frac{2^{Q-r-1}}{2^Q-1}.
\]
The denominator is a unit because \(2^{29^e}\equiv2\pmod{29}\). The weights sum to one, are compatible under refinement \(Q\mapsto29Q\) by the finite geometric-series identity, and have 29-adic norm at most one. Thus they define a bounded measure. The geometric-moment identity \(F_n=\frac12\sum_{h\ge0}h^n2^{-h}\) (as a rational-function identity evaluated at \(1/2\)) gives \(F_n=\int x^n\,d\mu(x)\). Precisely, replace \(h\) by \(h\bmod Q\) in the rational generating series; its difference is divisible by \(Q\) upon evaluation since \(2^Q-1\) is a 29-adic unit. This also proves the moment equality by passage to the limit.

**Step 2: analytic branches.** Put \(N=140\) and, for \(0\le a<28\),
\[
G_a(t)=\int_{\mathbb Z_{29}^{\times}}x^{N+a}(x^{28})^t\,d\mu(x),\qquad t\in\mathbb Z_{29}.
\]
Here \((x^{28})^t\) is defined by the convergent 29-adic exponential/logarithm, since \(x^{28}\in1+29\mathbb Z_{29}\). Its Mahler expansion has coefficients
\[
B_{a,j}=\int_{\mathbb Z_{29}^{\times}}x^{N+a}(x^{28}-1)^j\,d\mu(x)\in29^j\mathbb Z_{29}.
\]
Consequently \(G_a\) is analytic, and its Taylor terms of degree \(j\ge3\) are 29-adically divisible by \(29^3\); derivative/Lipschitz error bounds follow from the same integral. For any \(k\ge1\) and integer \(t\ge0\) with \(N+a+28t\ge k\), the nonunit integral is zero modulo \(29^k\), hence \(G_a(t)\equiv F_{N+a+28t}\pmod{29^k}\). The nonnegative integers \(t\) are dense in \(\mathbb Z_{29}\), so the eventual image is precisely the union of branch images modulo \(29^k\). The indices in every residue class \(a\pmod{28}\) appear once per \(29^{k-1}\) successive values of \(t\), giving the asserted period.

**Step 3: complete exact branch certificate.** The table below lists \(a\), \(F_{140+a}\bmod29\), and the reductions modulo \(29\) of the normalized first and second finite differences
\[
b_a=\frac{F_{168+a}-F_{140+a}}{29},\qquad c_a=\frac{F_{196+a}-2F_{168+a}+F_{140+a}}{29^2}.
\]
The displayed divisions are integral modulo the required powers. These are exact finite computations from the Stirling recurrence \(S(n+1,j)=jS(n,j)+S(n,j-1)\), repeated and independently checked by the attached standalone script.

| a | output mod 29 | b | c |
|---:|---:|---:|---:|
| 0 | 0 | 21 | 1 |
| 1 | 1 | 3 | 24 |
| 2 | 3 | 15 | 16 |
| 3 | 13 | 18 | 21 |
| 4 | 17 | 4 | 19 |
| 5 | 19 | 22 | 18 |
| 6 | 14 | 12 | 1 |
| 7 | 23 | 19 | 6 |
| 8 | 26 | 12 | 8 |
| 9 | 9 | 14 | 26 |
| 10 | 1 | 3 | 24 |
| 11 | 10 | 19 | 15 |
| 12 | 19 | 23 | 22 |
| 13 | 15 | 11 | 7 |
| 14 | 22 | 4 | 5 |
| 15 | 14 | 28 | 28 |
| 16 | 26 | 23 | 4 |
| 17 | 19 | 2 | 18 |
| 18 | 24 | 0 | 9 |
| 19 | 9 | 6 | 10 |
| 20 | 10 | 11 | 26 |
| 21 | 25 | 25 | 5 |
| 22 | 23 | 20 | 8 |
| 23 | 20 | 11 | 23 |
| 24 | 25 | 6 | 20 |
| 25 | 18 | 6 | 21 |
| 26 | 14 | 12 | 0 |
| 27 | 1 | 13 | 5 |

**Step 4: regular and critical branches.** For each \(a\ne18\), \(b_a\ne0\pmod{29}\). Since higher Mahler differences are divisible by \(29^2\), these 27 maps satisfy
\[
\nu_{29}(G_a(t)-G_a(s))=1+\nu_{29}(t-s)
\]
for distinct 29-adic inputs. Therefore each is an isometric parametrization of the full output ball of its base residue, and the output-ball multiplicity is the number of rows with that residue. The table gives sixteen distinct regular residue classes and the stated multiplicities.

For \(a=18\) the linear coefficient vanishes modulo \(29^2\). Put \(H(t)=(G_{18}(t)-G_{18}(0))/29^2\), which has integral analytic coefficients. The table gives
\[
H(t)\equiv4t+9\binom{t}{2}\pmod{29},\qquad H'(t)\equiv9t-\tfrac12\pmod{29}.
\]
The derivative has the unique simple root \(t\equiv21\pmod{29}\), and \(H''(t)\equiv9\pmod{29}\) is a unit. Analytic Hensel lifting gives a unique critical input \(\xi\in\mathbb Z_{29}\). Writing the analytic Taylor expansion about \(\xi\) and factoring yields
\[
G_{18}(t)=\delta+29^2u\,z(t)^2,
\]
where \(\delta=G_{18}(\xi)\), \(u=H''(\xi)/2\in\mathbb Z_{29}^{\times}\), and \(z(t)=(t-\xi)(1+29A(t))\) is an analytic isometry/bijection of \(\mathbb Z_{29}\). The factor \(1+29A(t)\) is the convergent analytic square root of the unit Taylor quotient. Computation modulo \(29^3\) gives \(\delta\equiv20672\pmod{29^3}\), \(u\equiv9/2\equiv19\pmod{29}\). This image lies in residue \(24\pmod{29}\), disjoint from all regular balls.

**Step 5: square counting and fibers.** A nonzero square modulo \(29^m\) has even 29-adic valuation \(2j<m\). There are \((29-1)29^{m-2j-1}/2=14\cdot29^{m-2j-1}\) such squares, plus zero. This yields \(S_m\) and the exact image count. Reducing the bijective critical input coordinate modulo \(29^{k-2}\) and accounting for its \(29\) lifts modulo \(29^{k-1}\) gives the critical fiber multiplier \(29\). The limiting density of squares in \(\mathbb Z_{29}\) is \(29/(2(29+1))\), giving the Haar measure above.

## Verification
`check_fubini29.py` recomputes all 28 branch finite differences exactly, verifies the unique critical row, the normalized critical value and quadratic unit, and independently enumerates all eventual output fibers for \(k=1,2,3\) using the Stirling recurrence. It checks all residue classes in complete periods of sizes \(28\), \(812\), and \(23548\), obtaining image sizes \(17\), \(465\), and \(13471\). These are finite checks of the certificate; the all-level theorem follows from the 29-adic proof.

## Relationship to prior work
Mező's 2013 public preprint (subsequently published in 2014) studies periodic last digits of Fubini and related sequences. Caicedo–Moll–Ramírez–Villamizar (2019), especially their Section 11, prove the eventual prime-power index period and provide a weighted power-sum congruence (Corollary 52), from which the interpolation may be developed. Those established identities are credited and not claimed new. The present result evaluates the range, fiber multiplicities, and the unique singular quadratic output branch specifically at prime 29. Related indexed results on Fubini coefficientwise periods and prime-power shift defects address different invariants, rather than the explicit 29-adic output image.

## Limitations
The theorem concerns eventual indices \(n\ge k\), not the full index range including smaller initial exceptions. The 29-adic center and unit are specified intrinsically through the analytic critical point and only their first listed digits are given; deeper digits can be calculated by Hensel lifting. No claim about arbitrary primes' corresponding images is made. Historical priority is subject to independent bibliographic review; related literature on general 29-adic moment transforms may contain broader results.

## References
- I. Mező, *Periodicity of the Last Digits of Some Combinatorial Sequences*, arXiv:1308.1637, first publicly posted 2013-08-07, https://arxiv.org/abs/1308.1637.
- J. B. Caicedo, V. H. Moll, J. L. Ramírez, D. Villamizar, *Extensions of set partitions and permutations*, Electronic Journal of Combinatorics 26(2), P2.20 (2019), Section 11, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i2p20/pdf/.
- *Ordered Bell Number*, Wolfram MathWorld, https://mathworld.wolfram.com/OrderedBellNumber.html.
