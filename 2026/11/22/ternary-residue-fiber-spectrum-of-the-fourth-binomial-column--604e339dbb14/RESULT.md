# Ternary residue-fiber spectrum of the fourth binomial column

## Finding

Put \(F(n)=\binom{n}{4}=n(n-1)(n-2)(n-3)/24\), with the continuous integer-valued extension to \(\mathbb Z_3\). For each integer \(k\ge1\) and each residue \(y\pmod{3^k}\), define
\[
N_k(y)=\#\{0\le n<3^{k+1}: F(n)\equiv y\pmod{3^k}\}.
\]
The sequence \(F(n)\bmod 3^k\) has **least** positive period \(3^{k+1}\), and all residues occur. Write \(m=k-1\); if \(3\mid y\), let \(z_y\) be the residue of \(y/3-128^{-1}\) modulo \(3^m\), with the unique residue modulo \(1\) used when \(m=0\). Define \(R_m(z)=\#\{w\pmod{3^m}:w^2\equiv z\pmod{3^m}\}\), where \(R_0=1\). Then
\[
\boxed{N_k(y)=2+3\,\mathbf1_{3\mid y}R_m(z_y).}
\]
In particular the **entire fiber-size histogram** is explicit. Exactly one residue has fiber size \(2+3^{\lfloor m/2\rfloor+1}\); for each integer \(0\le j\le\lfloor(m-1)/2\rfloor\), exactly \(3^{m-2j-1}\) residues have fiber size \(2+6\cdot3^j\); all other residues have fiber size \(2\). These fiber sizes are distinct, including when \(m=0\), when the middle collection is empty.

The three-adic map has exactly two inverse images for every target outside \(\frac3{128}+3(\mathbb Z_3)^2\); exactly four inverse images for every target in that set other than \(3/128\); and exactly three inverse images at the sole critical target \(3/128\). The output of a Haar-uniform three-adic input has density \(2/3\) everywhere off an enhancement set of Haar measure \(1/8\). On a shell \(y=3/128+3z\) with \(\nu_3(z)=2j\) and \(z/3^{2j}\equiv1\pmod3\), its Haar Radon–Nikodym density is \(2/3+2\cdot3^j\) for every integer \(j\ge0\). This density is unbounded but integrable; the singleton critical target has measure zero.

## Assumptions and scope

All index variables are nonnegative ordinary integers for the periodic finite counts. For inverse fibers and Haar statements, inputs and outputs range over \(\mathbb Z_3\), with normalized Haar probability measure. A square in \(\mathbb Z_3\) includes zero. The exact formula concerns fixed-column binomial values, not general row-wise binomial distributions. \(128^{-1}\) is the inverse of \(128\) in \(\mathbb Z_3\) or modulo the displayed power of three. The integer \(k\) is arbitrary and positive.

## Proof

**Two invertible residue branches.** Let \(t\in\mathbb Z_3\). Direct expansion gives
\[
\begin{aligned}
F(3t+1)&=\frac{27t^4}{8}-\frac{9t^3}{4}-\frac{3t^2}{8}+\frac t4,\\
F(3t+2)&=\frac{27t^4}{8}+\frac{9t^3}{4}-\frac{3t^2}{8}-\frac t4.
\end{aligned}
\]
Their divided differences are congruent respectively to \(1/4\) and \(-1/4\pmod3\). All polynomial coefficients belong to \(\mathbb Z_3\); consequently each map is a three-adic isometry, bijective modulo every power of three and hence bijective on \(\mathbb Z_3\). At each finite level, these two branches contribute exactly one preimage each to every target.

**Singular branch and global square conjugacy.** The third branch is
\[
F(3t)=3G(t),\qquad G(t)=\frac{9t^4-18t^3+11t^2-2t}{8}.
\]
Setting \(u=2t-1\), polynomial algebra gives the exact identity
\[
G(t)=\frac1{128}+u^2\frac{9u^2-10}{128}.
\]
For every \(u\in\mathbb Z_3\), the second factor \(A(u)=(9u^2-10)/128\) lies in \(1+3\mathbb Z_3\). By Hensel's lemma it has a unique square root \(s(u)\in1+3\mathbb Z_3\). Moreover
\[
s(u)-s(v)=\frac{9(u-v)(u+v)}{128(s(u)+s(v))},
\]
so \(\nu_3(s(u)-s(v))\ge\nu_3(u-v)+2\), because the denominator is a unit. Thus \(w(u)=u s(u)\) satisfies \(\nu_3(w(u)-w(v))=\nu_3(u-v)\), and \(w(u)\equiv u\pmod3\). It induces a permutation at every finite level and a bijective isometry on \(\mathbb Z_3\). Therefore the singular branch is exactly
\[
F(3t)=\frac3{128}+3w(2t-1)^2.
\]
This identity is global, not a formal approximation near the critical point.

**Finite counts.** Every residue class modulo \(3^{k+1}\) has a unique expression \(3t+a\), with \(a=0,1,2\) and \(t\pmod{3^k}\). On the first two isometric branches the target count is one each. On the branch \(a=0\), if \(3\nmid y\) there are no solutions. Otherwise the square equation must hold modulo \(3^{k-1}\); since \(w\) permutes residues modulo \(3^k\), each root modulo \(3^{k-1}\) has precisely three lifts. This proves the boxed exact formula.

For \(m\ge1\), the elementary complete root classification for \(w^2\equiv z\pmod{3^m}\) is: \(R_m(0)=3^{\lfloor m/2\rfloor}\); if \(\nu_3(z)=2j<m\), then \(R_m(z)=2\cdot3^j\) if the leading unit is \(1\pmod3\), and zero otherwise; for odd valuation it is zero. For each \(j\), the number of such nonzero-square target residues is \(3^{m-2j-1}\). Translation by \(128^{-1}\) and scaling by three inject these \(z\)-classes into output classes \(y\pmod{3^k}\). This proves the entire fiber histogram, including its exceptional zero-square class. Each fiber is positive because the isometric branches already contribute two.

**Sharp period.** The decompositions show that shifting an index by \(3^{k+1}\) leaves its output unchanged modulo \(3^k\). But the shift by \(3^k\) changes the value at \(n=1\): the first isometric branch has input \(t\) shifted by \(3^{k-1}\) and hence value changed with exact three-adic valuation \(k-1\). Since the least period divides any period, the least period must be \(3^{k+1}\).

**Infinite fibers and density.** The two isometric branches contribute exactly two preimages at every target, and the singular branch reduces to the square-map fibers, which are zero, one or two according as \((y/3-1/128)\) is a nonsquare, zero or a nonzero square, with that branch available only for \(3\mid y\). The set \((\mathbb Z_3)^2\) has Haar measure \(\sum_{j\ge0}3^{-2j-1}=3/8\), so the enhancement set has measure \(1/8\). The square map has output density \(2\cdot3^j\) on a nonzero-square shell of valuation \(2j\), as follows from its two inverse branches with Jacobian norm \(3^{-j}\). The weight \(1/3\) of the singular input branch cancels the factor three from scaling the output by three. The two other branches contribute uniform output density \(2/3\). The added density integrates to \(\sum_{j\ge0}(2/9)3^{-j}=1/3\), proving normalization and the asserted integrable, unbounded density.

## Verification

The standalone `check.py` reconstructs all residue counts independently from ordinary integer binomial coefficients for \(1\le k\le8\), compares them with the explicit square-root formula, checks the claimed least-period obstruction, and verifies both singular-branch polynomial identities in \(4000\) modular equality tests. All cases pass. `check_output.txt` records the actual run. These checks are finite corroboration; the all-level claims follow from the preceding algebra and three-adic isometry proof.

Examples of fiber-size histograms, expressed as \(\{\text{fiber size}:\text{number of output residues}\}\), are \(\{2:2,5:1\}\) for \(k=1\), \(\{2:23,8:3,11:1\}\) for \(k=3\), and \(\{2:212,8:27,20:3,29:1\}\) for \(k=5\).

## Relationship to prior work

Sun and Zhang, *Binomial coefficients and the ring of p-adic integers* (first arXiv version 16 December 2008, arXiv:0812.3089), proved three-adic density/surjectivity for this fourth column: their Theorem 1.1 applies since \(3\le4<6\). That result is acknowledged as known and is strictly weaker than the present exact finite fiber histogram, three inverse-fiber classification, and full Haar pushforward law. Their explicit lifting argument provides one surjective branch but does not state the singular square decomposition or multiplicity law.

Published results indexed under *Exact good-prime-power images and p-adic density of pentatope numbers* treat the same polynomial for primes \(p\ge7\), not the ramified denominator prime \(3\); an indexed *Exact ternary residue images of the sixth binomial polynomial* concerns the different sixth column. Their titles are not used as novelty proofs. General work on binomial distributions and three-adic square maps provides background, and stronger previously unnoticed general theorems could conceivably imply the specialization. The actual literature comparisons and access limits are detailed in the accompanying review.

## Limitations

This result only concerns the prime three and the fourth fixed binomial column; it does not assert a corresponding formula for all primes or columns. The three-adic law does not count ordinary integer square values. Historical priority remains subject to examination of broader fixed-column residue-distribution papers and inaccessible full texts, especially potentially dominating general theorems.

## References

1. Zhi-Wei Sun and Wei Zhang, *Binomial coefficients and the ring of p-adic integers*, arXiv:0812.3089 (first public version 2008-12-16), *Proceedings of the American Mathematical Society* 139 (2011), 1569–1577. https://arxiv.org/abs/0812.3089
2. G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, *Journal of the London Mathematical Society* 64 (2001), 523–547. https://doi.org/10.1112/S0024610701002630
3. Published finding indexed as *Exact good-prime-power images and p-adic density of pentatope numbers*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-good-prime-power-images-and-p-adic-density-of-pentatope-nu--c524d9c86455
4. Published finding indexed as *Exact ternary residue images of the sixth binomial polynomial*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-residue-images-of-the-sixth-binomial-polynomial--2c5deda1b9d1
