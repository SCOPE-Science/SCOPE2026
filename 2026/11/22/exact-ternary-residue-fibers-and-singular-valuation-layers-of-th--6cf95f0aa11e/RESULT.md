# Exact ternary residue fibers and singular valuation layers of the third Narayana column

## Finding

For integers \(n\ge3\), let the third Narayana column be
\[
F(n)=N(n,3)=\frac1n\binom n3\binom n2=\frac{n(n-1)^2(n-2)}{12}.
\]
Use the same integer-valued polynomial for \(n=0,1,2\), where it vanishes. For every integer \(k\ge1\), the **least** period of \(F(n)\bmod3^k\) is \(3^{k+1}\). For each target \(y\in\mathbb Z/3^k\mathbb Z\), let \(M_k(y)\) count its occurrences in any consecutive index block of that length. Define
\[
R_m(z)=\#\{u\in\mathbb Z/3^m\mathbb Z:u^2\equiv z\pmod{3^m}\},\qquad R_0(z)=1.
\]
Then the **complete fiber law**, for every target and every depth, is
\[
\boxed{M_k(y)=\begin{cases}2,&3\nmid y,\\
2+3R_{k-1}(-4y/3),&3\mid y.
\end{cases}}
\]
Here \(y/3\) denotes the unique residue modulo \(3^{k-1}\) obtained from a representative divisible by three; the expression is independent of that choice. In particular every residue occurs, and the output is not uniform.

The fiber-size histogram is explicit. Put \(m=k-1\). For each integer \(0\le r\le\lfloor(m-1)/2\rfloor\), exactly \(3^{m-2r-1}\) targets have fiber size \(2+6\cdot3^r\). The zero target has size \(2+3^{1+\lfloor m/2\rfloor}\). Every other target has size two. These alternatives are mutually exclusive (with the middle range empty when \(m=0\)). For instance, the distributions (fiber size : number of targets) at \(k=1,3,5\) are, respectively, \((2:2,5:1)\), \((2:23,8:3,11:1)\), and \((2:212,8:27,20:3,29:1)\).

The nonuniform contribution comes from a single quadratic critical branch. Its target support in \(\mathbb Z_3\) is exactly \(-\tfrac34\mathbb Z_3^2\), a set of Haar measure \(1/8\). The complete natural-density law of the valuations is, for \(j\ge0\),
\[
\boxed{\Pr(\nu_3(F(n))=j)=\frac{4}{3^{j+2}}+
\begin{cases}\frac{2}{3^{r+2}},&j=2r+1\ (r\ge0),\\0,&j\text{ even}.
\end{cases}}
\]
The probability denotes the limiting density of nonnegative index integers, excluding the finitely many polynomial zeros. The displayed density at \(j=0\) is \(4/9\), and the densities sum to one.

## Assumptions and scope

The claim concerns the ordinary Narayana triangle, not the unrelated Narayana-cows recurrence. Indices \(n\ge3\) define genuine triangle entries; the polynomial extension at \(n=0,1,2\) has three zero values and is used only to describe whole periods. All congruences have modulus a positive power of three, and all claims are unconditional for every such power. The valuation of zero is treated as infinite and its three exceptional initial indices do not affect limiting densities. Haar measure is normalized by \(\mu(\mathbb Z_3)=1\).

## Proof

**Branch decomposition.** For \(t\in\mathbb Z_3\), substitution gives identities in \(\mathbb Z_3\):
\[
\begin{aligned}
F(3t)&=t\,(3t-1)^2(3t-2)/4=:G_0(t),\\
F(3t+2)&=t\,(3t+2)(3t+1)^2/4=:G_2(t),\\
F(3t+1)&=-\tfrac34t^2(1-9t^2)=:G_1(t).
\end{aligned}
\]
The two first expressions are polynomials with coefficients in \(\mathbb Z_3\) and reduce to \(t\) and \(-t\), respectively, modulo three. Therefore, for \(a\in\{0,2\}\) and all \(s,t\in\mathbb Z_3\), their divided differences have the form \((G_a(t)-G_a(s))/(t-s)=\varepsilon_a+3H_a(s,t)\) with \(\varepsilon_a\) a unit and \(H_a\in\mathbb Z_3[s,t]\). Consequently
\[
\nu_3(G_a(t)-G_a(s))=\nu_3(t-s),
\]
so each is an isometry and induces a bijection on every \(\mathbb Z/3^k\mathbb Z\).

**Singular branch.** For each \(t\in\mathbb Z_3\), Hensel's lemma gives the unique \(u(t)\in1+3\mathbb Z_3\) such that \(u(t)^2=1-9t^2\). In fact \(u(t)\in1+9\mathbb Z_3\). For every \(s,t\),
\[
(u(t)-u(s))(u(t)+u(s))=-9(t-s)(t+s).
\]
As the second factor on the left is a three-adic unit, \(u(t)-u(s)\in9(t-s)\mathbb Z_3\). Thus \(\phi(t)=t\,u(t)\) satisfies \(\phi(t)-\phi(s)=(t-s)(1+3w)\) for some \(w\in\mathbb Z_3\) and is also an isometry. Its reduction modulo \(3^h\) is injective, hence bijective, for every \(h\), and therefore \(\phi\) is a bijection of \(\mathbb Z_3\). The singular branch has the exact normal form
\[
G_1(t)=-\frac34\phi(t)^2.
\]
This is a genuine conjugation of the critical branch to a scaled square map, not a mere lowest-order approximation.

**Period and fibers.** Every branch depends only on \(t\bmod3^k\) when reduced modulo \(3^k\). Hence \(3^{k+1}\) is an index period. The residue sequence modulo three over indices \(0\le n<9\) is \((0,0,0,1,0,2,2,0,1)\), of least period nine. Every period at depth \(k\) must therefore be divisible by nine. If \(T\) is such a period, \(F(T)\equiv F(0)=0\pmod{3^k}\), but for \(3\mid T\), the defining polynomial gives \(\nu_3(F(T))=\nu_3(T)-1\), since \(T-1\) and \(T-2\) are units. Therefore \(3^{k+1}\mid T\), proving sharpness.

Within one period, the indices \(3t\) and \(3t+2\), each with \(t\) running over \(\mathbb Z/3^k\mathbb Z\), contribute exactly one solution to every target. The branch \(3t+1\) contributes none unless \(3\mid y\). For \(y=3z\), its condition is \(\phi(t)^2\equiv-4z\pmod{3^{k-1}}\). Since \(\phi\) is a bijection at every level, and every solution modulo \(3^{k-1}\) has three lifts to \(t\bmod3^k\), its contribution is exactly \(3R_{k-1}(-4z)\). This proves the all-target formula, including \(k=1\).

**Square-root spectrum.** For \(m\ge1\), if \(z\equiv0\pmod{3^m}\), there are \(3^{\lfloor m/2\rfloor}\) roots. If \(\nu_3(z)=2r<m\), there are \(2\cdot3^r\) roots exactly when \(z/3^{2r}\equiv1\pmod3\); there are none when its unit is two modulo three or its valuation is odd. This follows by factoring off \(3^{2r}\) and applying unique Hensel lifting to the two unit square roots, with \(3^r\) choices of excess digits. For any fixed \(r\) in the stated range, precisely \(3^{m-2r-1}\) targets \(z\bmod3^m\) have the required valuation and square unit. Together with the single zero target, this gives the complete fiber histogram.

**Limit law.** Under uniform indices, each of the three branches has weight \(1/3\). The two isometric branches send Haar measure to Haar measure, contributing \(2/3\) of the total uniform law. The third pushes Haar measure forward by \(-\tfrac34\phi(t)^2\); its image is \(-\tfrac34\mathbb Z_3^2\). The square set has measure \(\sum_{r\ge0}\frac13 3^{-2r}=3/8\), and scaling by three reduces Haar measure by a factor of three, giving image measure \(1/8\). The two regular branches contribute \((2/3)(2/3)3^{-j}=4/3^{j+2}\) to each finite valuation level \(j\). The critical branch has valuation \(1+2r\) exactly when \(\nu_3(t)=r\), with probability \((1/3)(2/3)3^{-r}=2/3^{r+2}\), proving the displayed density law. Periodicity at each depth justifies passage from Haar probabilities to natural densities.

## Verification

A standalone Python 3 standard-library checker is included as `verify.py`. Run `python3 verify.py` to compare the theorem with independent exact evaluations of \(\frac1n\binom n3\binom n2\) for \(3\le n<250\), all fiber counts for \(1\le k\le8\), the two finite bijections at each depth, and failures of the next shorter candidate period. It returns `PASS 10119 exact assertions`. A separate direct finite histogram calculation at \(1\le k\le6\) also matched the predicted fiber-size spectra. These tests are finite corroboration only; the unrestricted result rests on the proof above.

## Relationship to prior work

Bóna and Sagan (2005) give a Kummer-theorem criterion for prime divisibility of arbitrary Narayana entries (Theorem 1.2), and explicitly distinguish this from determining finer prime-power information (their Comments, part I). That criterion determines whether an entry vanishes modulo a prime but does not determine target-by-target counts modulo every power of three, sharp periods, or the singular-square density. Checcoli and D'Adderio (2013) analyze perfect powers of integer Narayana entries and Pell-equation parametrizations at fixed column indices. Their integer-square criterion and even their fixed-third-column discussion do not determine the distribution of all congruence targets.

Indexed related research on complete valuation polynomials for rows \(n=mp^r\) concerns varying column indices within special rows; it does not imply a fixed third-column residue histogram for all row indices. Another indexed classification treats perfect-square entries in fixed square-index columns \(b=c^2\ge4\), excluding the nonsquare index \(b=3\) here. Existing local-square residue laws for binomial columns concern different polynomials; the repeated root in the present Narayana polynomial prevents an affine identification with the fourth binomial column (which has four distinct roots). The classification of quadratic roots is classical and is not claimed as original; the specific full Narayana fiber and valuation law is the claim.

## Limitations

This does not classify other Narayana columns, other primes, or integer perfect-power values. General polynomial \(p\)-adic mapping principles underlie the method; a broader historical treatment might subsume the explicit result even without its wording. An exhaustive historical novelty proof is not available. The exact theorem has been checked against accessible primary literature and indexed neighboring results but has not been independently audited.

## References

1. M. Bóna and B. E. Sagan, *On divisibility of Narayana numbers by primes*, arXiv:math/0505382, first publicly posted 2005-05-18, especially Theorem 1.2 and Section 3. https://arxiv.org/abs/math/0505382 .
2. S. Checcoli and M. D'Adderio, *Perfect powers in Catalan and Narayana numbers*, arXiv:1306.5929, first publicly posted 2013-06-25, especially Section 3. https://arxiv.org/html/1306.5929v1 .
3. *Exact valuation polynomials and a geometric limit for dilated Narayana rows*, public RESULT.md, 2026-10-26, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-valuation-polynomials-and-a-geometric-limit-for-dilated-na--bde71f25e69e/RESULT.md .
4. *Finite square-index columns of Narayana numbers: exact divisor parametrization and sharp maxima*, public RESULT.md, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-finite-square-index-columns-of-narayana-numbers-exact-divisor-pa--4e47d093953c/RESULT.md .
