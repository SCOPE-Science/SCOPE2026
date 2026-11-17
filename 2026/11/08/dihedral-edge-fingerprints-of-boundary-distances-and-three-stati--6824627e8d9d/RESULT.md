# A global second moment resolves local-distance ambiguity for rectangular boxes

## Finding

Let \(P\) be a rectangular box with unknown positive edge lengths \(a,b,c\). Draw independent points \(X,Y\) uniformly from its surface area, and let \(F(r)=\Pr(\|X-Y\|\le r)\). Write \(s_1=a+b+c\), \(s_2=ab+bc+ca\), \(s_3=abc\), and \(S=2s_2\). Define the two local coefficients
\[
 c_2=\lim_{r\downarrow0} F(r)/r^2,\qquad c_3=\lim_{r\downarrow0}(F(r)-c_2r^2)/r^3,
\]
and the global second moment \(M_2=\mathbb E\|X-Y\|^2\).

**Theorem (one-statistic completion).** The triple \((c_2,c_3,M_2)\) determines the unordered three edge lengths uniquely, including repeated lengths. More precisely,
\[
 c_2=\frac{\pi}{S},\qquad c_3=\frac{8(\pi-2)s_1}{3S^2},\qquad
 M_2=\frac{s_1^2s_2-2s_2^2+2s_1s_3}{6s_2}.
\]
The reconstruction is explicit:
\[
 S=\frac\pi{c_2},\quad s_2=S/2,\quad
 s_1=\frac{3S^2 c_3}{8(\pi-2)},\quad
 s_3=\frac{6s_2M_2-s_1^2s_2+2s_2^2}{2s_1},
\]
and \(\{a,b,c\}\) is the multiset of positive roots of \(u^3-s_1u^2+s_2u-s_3=0\).

The need for *one additional independent scalar statistic* is sharp in the following natural sense: for every noncubic box there is a local continuum of noncongruent positive boxes with the same entire sufficiently-short-distance CDF, hence no collection of statistics determined by that local CDF alone can recover the box. The global second moment breaks all those ambiguities.

## Proof

**1. Previously known local law.** The established surface-distance theorem for rectangular boxes states that, for \(0\le r<\min(a,b,c)\),
\[
 F(r)=\frac{\pi r^2}{S}+\frac{8(\pi-2)s_1r^3}{3S^2}+\frac{3(1-\pi)r^4}{S^2}.
\]
The universal polyhedral dihedral-edge expansion and this exact local box polynomial were published earlier (*The exact short Euclidean surface-pair law and its dihedral bending coefficient*, 2026-10-25; and *Dihedral-edge law for short surface-chord distances and locally indistinguishable boxes*, 2026-11-02). They are **inputs**, not claimed contributions. Their coefficients recover \(s_2=S/2\) and \(s_1\) but leave \(s_3\) undetermined.

**2. Compute the global moment directly.** Translate the box to its center. Symmetry gives \(\mathbb E X=0\), so \(M_2=2\mathbb E\|X\|^2\). For its first coordinate \(x\), the two faces perpendicular to the \(x\)-axis have total area \(2bc\) and fixed \(x^2=a^2/4\). The four other faces have total area \(2a(b+c)\) and uniform first-coordinate second moment \(a^2/12\). Thus
\[
\mathbb E x^2=\frac{a^2bc/2+a^3(b+c)/6}{S}.
\]
Summing this expression cyclically, multiplying by two, and using
\[
\sum_{\mathrm{cyc}} a^3(b+c)=s_1^2s_2-2s_2^2-s_1s_3,\qquad
\sum_{\mathrm{cyc}}a^2bc=s_1s_3,
\]
gives the asserted formula for \(M_2\).

**3. Inversion and minimality.** Since \(S>0\), \(s_1>0\), and \(\pi-2>0\), the formulas in the finding reconstruct \(s_2,s_1,s_3\) without division by zero. Vieta's theorem then uniquely gives the unordered side lengths, including equal roots.

For noncubic positive triples the map \((a,b,c)\mapsto(s_1,s_2)\) has Jacobian rows \((1,1,1)\) and \((b+c,a+c,a+b)\), which are linearly independent. Its level sets are therefore local one-dimensional manifolds of positive triples. Quotienting by the finite permutation group still leaves a continuum of noncongruent shapes with identical \(s_1,s_2\) and hence identical sufficiently short-distance laws. Thus two local invariants cannot generally distinguish boxes. The independently measured global second moment recovers the missing \(s_3\), proving the stated sharp completion. \(\square\)

## Motivation and limits

A short-distance surface-pair histogram determines only surface area and total edge-length sum, and published work exhibits continuous families of locally indistinguishable boxes. Determining a *minimal additional natural observable* is an inverse-probability question. The global second moment is a direct distance statistic of exactly the same sampling experiment and supplies the third elementary symmetric invariant.

No general polyhedral-edge coefficient, local quartic law, or local nonidentifiability phenomenon is newly claimed here. The reconstruction assumes the object is known to be a rectangular box. It concerns extrinsic Euclidean distance between independent surface-uniform samples, not intrinsic geodesics or volume-uniform points. No uniform noise-conditioning guarantee or classification of nonbox shapes is asserted. Historical priority of this mixed local/global statistic remains a best-of-knowledge judgment.
