# Exact three-adic residue fibers of the pentatope numbers

## Finding

Let \(P_n=\binom n4\) for every integer \(n\ge0\). For any integer \(k\ge1\), the least period of \((P_n\bmod3^k)_{n\ge0}\) is exactly \(3^{k+1}\). Write
\[
N_k(y)=\#\{0\le n<3^{k+1}:P_n\equiv y\pmod{3^k}\}\quad(y\in\mathbb Z/3^k\mathbb Z).
\]
Let \(\kappa=3/128\in\mathbb Z_3\). Define \(R_e(v)=\#\{w\in\mathbb Z/3^e\mathbb Z:w^2\equiv v\pmod{3^e}\}\) for \(e\ge1\), and \(R_0(0)=1\). Then the *complete* fiber law, for every \(k\ge1\) and every residue \(y\), is
\[
\boxed{N_k(y)=\begin{cases}2,&y\not\equiv0\pmod3,\\2+3R_{k-1}((y-\kappa)/3),&y\equiv0\pmod3.\end{cases}}
\]
The quotient in the second line is taken modulo \(3^{k-1}\); it is well-defined because \(y\) and \(\kappa\) are both multiples of three. Thus every residue occurs at least twice in a least period: the image of the pentatope numbers is dense in \(\mathbb Z_3\), and every residue modulo every power of three appears infinitely often.

The distribution of the fiber sizes is also exact. Put \(e=k-1\) and \(J=\{j\in\mathbb Z:0\le j<e/2\}\). For each \(j\in J\), exactly \(3^{e-2j-1}\) output residues have \(N_k(y)=2+6\cdot3^j\). Exactly one output residue has \(N_k(y)=2+3^{1+\lfloor e/2\rfloor}\). The remaining \(3^k-1-\sum_{j\in J}3^{e-2j-1}\) residues have fiber size two. In the cases where two displayed fiber-size values coincide, their multiplicities are added (the formulas themselves determine the counts).

In the three-adic codomain, the exceptional outputs with a nonzero contribution from the index class divisible by three are exactly \(\kappa+3\mathbb Z_3^2\), a closed set of normalized Haar measure \(1/8\). This is the measure of the *exceptional subset*, not of the full value image, which is all of \(\mathbb Z_3\).

## Assumptions and scope

All moduli are positive powers of three. The standard binomial polynomial \(F(x)=x(x-1)(x-2)(x-3)/24\) is integer-valued for nonnegative integers and defines a continuous three-adic function, though its coefficients are not all integral at three. The substitution \(x=3t+r\), \(r\in\{0,1,2\}\), yields three polynomials with coefficients in \(\mathbb Z_3\); these are the objects lifted in the proof. Every number \(N_k(y)\) counts indices in one genuine least period, not indices in an arbitrary sample. All unit fractions below are interpreted in \(\mathbb Z_3\).

## Proof

**1. Two isometric branches.** Direct cancellation of the factor three in the binomial formula gives
\[
F(3t+1)=\frac{t(3t-2)(3t-1)(3t+1)}8,\qquad
F(3t+2)=\frac{t(3t-1)(3t+1)(3t+2)}8.
\]
These belong to \(\mathbb Z_3[t]\) and reduce respectively to \(t\) and \(-t\) modulo three. For two inputs \(s,t\in\mathbb Z_3\), the difference quotient of either branch is a polynomial congruent to its corresponding slope \(\pm1\) modulo three. Therefore
\[
\nu_3(F(3t+r)-F(3s+r))=\nu_3(t-s)\qquad(r=1,2;\ t\ne s).
\]
Each branch induces a bijection on \(\mathbb Z/3^k\mathbb Z\), contributing exactly one index to every output fiber in a block of \(3^{k+1}\) consecutive indices.

**2. An exact square normal form on the remaining branch.** On the divisible-by-three branch,
\[
F(3t)=\frac{3t(t-1)(3t-2)(3t-1)}8.
\]
With \(w=2t-1\), a direct expansion gives the exact identity
\[
\boxed{F(3t)=\frac3{128}+3w^2U(w^2),\qquad U(z)=\frac{9z-10}{128}.}
\]
For every \(w\in\mathbb Z_3\), \(U(w^2)\equiv1\pmod3\). Let \(b(w)\) be its unique square root congruent to one modulo three; existence and uniqueness follow from Hensel's lemma, because the derivative of the squaring map is a unit at one. Set \(\phi(w)=wb(w)\). For distinct \(s,t\in\mathbb Z_3\),
\[
b(t)-b(s)=\frac{9(t^2-s^2)}{128(b(t)+b(s))}\in9(t-s)\mathbb Z_3.
\]
Hence \(\phi(t)-\phi(s)\equiv t-s\pmod{3(t-s)\mathbb Z_3}\) and \(\nu_3(\phi(t)-\phi(s))=\nu_3(t-s)\). In particular \(\phi\) is an isometry and induces an injective map on every finite quotient. It is therefore bijective on every quotient and on \(\mathbb Z_3\) by compactness. Since \(t\mapsto2t-1\) is also a bijection, the third branch has exactly the same value fibers as \(w\mapsto\kappa+3w^2\), with \(\kappa=3/128\).

**3. Fibers and periods.** The third branch always produces outputs divisible by three. For \(k\ge2\), the congruence \(\kappa+3w^2\equiv y\pmod{3^k}\) is equivalent to \(w^2\equiv(y-\kappa)/3\pmod{3^{k-1}}\). Each root modulo \(3^{k-1}\) has precisely three lifts to a residue modulo \(3^k\), giving \(3R_{k-1}\) solutions. For \(k=1\), every third-branch input gives the zero output and contributes three, as prescribed by \(R_0=1\). Adding the two bijective branches proves the main formula.

Each branch modulo \(3^k\) depends only on \(t\bmod3^k\), hence the original sequence has period \(3^{k+1}\). The shift \(3^k\) fails to be a period: on the branch \(n=3t+1\), it changes \(t\) by \(3^{k-1}\), and the isometry shows the output changes by a number of valuation exactly \(k-1\), not divisible by \(3^k\). The least positive period divides any period, so it must be exactly \(3^{k+1}\).

**4. Fiber-size spectrum.** For any exponent \(e\ge1\), a nonzero residue \(v\pmod{3^e}\) is a square exactly when \(\nu_3(v)=2j<e\) and its unit part is a square modulo three. Such a residue has \(R_e(v)=2\cdot3^j\), and exactly \(3^{e-2j-1}\) distinct values \(v\) have this property. At \(v=0\), there are \(3^{\lfloor e/2\rfloor}\) roots. All other values have no roots. The same statement at \(e=0\) is given by the convention \(R_0(0)=1\). Substituting into the main formula gives all listed fiber counts.

**5. The exceptional measure.** The unit group of \(\mathbb Z_3\) has half its elements squares in the Haar sense. Partitioning squares by even valuation gives
\[
\mu(\mathbb Z_3^2)=\sum_{j\ge0}\frac13\,3^{-2j}=\frac38.
\]
Translation and multiplication by three therefore give \(\mu(\kappa+3\mathbb Z_3^2)=\frac13\cdot\frac38=\frac18\). This proves the stated exceptional-set measure.

## Verification

The included reproducible, dependency-free script `artifacts/verify.py` evaluates the exact binomial coefficients \(\binom n4\) across every index in the asserted least period for \(k=1,\ldots,7\). It independently constructs every predicted residue fiber by counting square roots modulo \(3^{k-1}\), compares entire dictionaries and multiplicity spectra, and checks the claimed period across additional index shifts. Run `python3 artifacts/verify.py` using Python 3. The recorded execution reported `PASS: 12926 exact finite index/period checks, all target fiber spectra reproduced`. These finite checks corroborate but do not replace the infinite proof above.

## Relationship to prior work

Beukers's 2022 work studies \(p\)-linear schemes for arithmetic sequences modulo prime powers and motivates exact higher-power residue questions. The particularly close published result *Exact good-prime-power images and p-adic density of pentatope numbers* explicitly treats the same polynomial \(\binom{x}{4}\), but only for \(p\ge7\); its theorem and limitations expressly exclude the prime three. It gives full value-image sets and image cardinalities in good characteristic, rather than the present exact *fiber multiplicities*, least periods and three-adic square-branch law at a bad prime. Earlier Dickson-polynomial results provide related finite-field and Galois-ring value-set theories; their potential implications are a residual priority risk, and the 1991 Galois-ring article has not been checked in full. The present theorem is not a claim of originality for the classic binomial formula, Hensel's lemma, or square-root counting.

## Limitations

The claim is restricted to \(p=3\) and the degree-four binomial column. It does not settle image distributions at the prime two or five, nor assert a general theorem for every integer-valued polynomial. The classification is proved from explicit normal forms, not from a finite search. A possibly implicit equivalent in older general Dickson-polynomial/Galois-ring literature cannot be conclusively excluded by the available full-text checks. Independent validation has not been conducted.

## References

1. F. Beukers, *p-Linear schemes for sequences modulo \(p^r\)*, arXiv:2211.15240v1 (first public 2022-11-28), https://arxiv.org/abs/2211.15240.
2. *Exact good-prime-power images and p-adic density of pentatope numbers*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-good-prime-power-images-and-p-adic-density-of-pentatope-nu--c524d9c86455.
3. W. S. Chou, J. Gomez-Calderon, G. L. Mullen, *Value sets of Dickson polynomials over finite fields*, Journal of Number Theory 30 (1988), 334–344, DOI 10.1016/0022-314X(88)90006-6.
4. P. S. Bremser, J. Gomez-Calderon, *Value sets of Dickson polynomials over Galois rings*, Journal of Number Theory 38 (1991), 240–250, DOI 10.1016/0022-314X(91)90087-R.
