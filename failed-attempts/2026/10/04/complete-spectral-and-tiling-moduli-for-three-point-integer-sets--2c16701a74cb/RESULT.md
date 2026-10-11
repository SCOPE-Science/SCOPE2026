# Complete spectral and tiling moduli for three-point integer sets
## Finding
Let \(A=\{a_0,a_1,a_2\}\subset\mathbb Z\) have three distinct points. Define
\[
g=\gcd(a_1-a_0,a_2-a_0)>0,\qquad u=\frac{a_1-a_0}g,\qquad v=\frac{a_2-a_0}g.
\]
Then \(A\) is spectral if and only if it tiles \(\mathbb Z\), and these equivalent properties hold exactly when
\[
\{u\bmod 3,v\bmod 3\}=\{1,2\}.
\]
When this condition holds, every normalized spectrum \(\Gamma\subset\mathbb R/\mathbb Z\) with \(0\in\Gamma\) is uniquely
\[
\Gamma_{r,s}=\left\{0,\frac{3r+1}{3g},\frac{3s+2}{3g}}\right\},\qquad 0\le r,s<g,
\]
so there are exactly \(g^2\) normalized spectra. Every translational tiling complement is uniquely
\[
T=-a_0+\bigcup_{r=0}^{g-1}\bigl(r+g(c_r+3\mathbb Z)\bigr),\qquad c_r\in\{0,1,2\},
\]
so there are exactly \(3^g\) complements, each \(3g\)-periodic. Thus the recent rationality theorem for finite integer spectral pairs has, at cardinality three, an exact denominator bound and a complete moduli description on both the spectral and tiling sides.

## Assumptions and scope
A normalized spectrum means a three-element subset \(\Gamma\subset\mathbb R/\mathbb Z\) containing \(0\) such that the three exponential vectors \( (e^{2\pi i a\gamma})_{a\in A} \), for \(\gamma\in\Gamma\), are pairwise orthogonal. A tiling complement is a set \(T\subset\mathbb Z\) for which every integer has exactly one representation as \(a+t\) with \(a\in A\) and \(t\in T\). The count \(g^2\) is for normalized spectra; arbitrary spectra are obtained by a common frequency translation. No claim is made for sets with more than three points or for higher-dimensional tilings.

## Proof
Translate \(A\) by \(-a_0\); this changes neither spectrality nor the classification of spectra, and it translates every tiling complement by \(a_0\). We therefore study \(A'=gB\) with \(B=\{0,u,v\}\) and \(\gcd(u,v)=1\).

For a frequency difference \(\delta\in\mathbb R/\mathbb Z\), orthogonality is equivalent to
\[
1+z^u+z^v=0,\qquad z=e^{2\pi i g\delta},\qquad |z|=1.
\]
Three unit complex numbers can sum to zero only when they are the vertices of a regular triangle, hence
\[
\{z^u,z^v\}=\{\omega,\omega^2\},\qquad \omega=e^{2\pi i/3}.
\]
Thus \(z^{3u}=z^{3v}=1\). Bézout's identity and \(\gcd(u,v)=1\) give \(z^3=1\). A zero exists precisely when \(u\) and \(v\) represent the two nonzero classes modulo \(3\). Under that condition the complete zero set on the unit circle is
\[
Z_A=\left\{\delta:\ g\delta\equiv\frac13\text{ or }\frac23\pmod 1\right\}.
\]
If \(\Gamma=\{0,\alpha,\beta\}\) is normalized, then \(\alpha\), \(\beta\), and \(\alpha-\beta\) must all lie in \(Z_A\). The first two conditions place \(\alpha\) and \(\beta\) among the two residue families
\[
\frac{3r+1}{3g},\qquad \frac{3s+2}{3g}.
\]
The third condition holds exactly when the two chosen points come from opposite families. This proves the displayed formula for \(\Gamma_{r,s}\), its converse, uniqueness, and the count \(g^2\). Because three nonzero orthogonal vectors in a three-dimensional space form a basis, no further completeness condition is needed.

For tilings first take the primitive set \(B\). If the modular condition holds, \(B\) contains one representative of every residue class modulo \(3\), so each \(c+3\mathbb Z\) is a tiling complement. Conversely suppose \(B+S=\mathbb Z\) is an exact tiling. After translating \(B\), write it inside \(\{0,1,\ldots,L\}\) with both endpoints present. If \(s(n)=1_S(n)\), exact tiling gives a finite recurrence
\[
\sum_{b\in B}s(n-b)=1.
\]
The length-\(L\) binary state determines the next bit because the coefficient at the left endpoint is one, and determines the previous bit because the coefficient at the right endpoint is one. Hence the state evolution is a bijection on a finite set of occurring states, so \(S\) is periodic; let \(P\) be a period.

Passing to \(\mathbb Z/P\mathbb Z\), exact tiling gives \(\widehat{1_B}(k)\widehat{1_S}(k)=0\) for every nonzero frequency. The unit-circle argument above shows that the mask of primitive \(B\) vanishes only at \(\omega\) and \(\omega^2\). Therefore the discrete Fourier transform of \(1_S\) is supported only at frequencies \(0\), \(P/3\), and \(2P/3\). Fourier inversion makes \(1_S\) three-periodic. Its density is \(1/3\), so exactly one residue class modulo \(3\) occurs: \(S=c+3\mathbb Z\).

Finally let \(A'=gB\). Any complement \(T'\) decomposes independently over residues modulo \(g\). For each \(0\le r<g\), define
\[
S_r=\{k\in\mathbb Z:r+gk\in T'\}.
\]
Exact tiling by \(gB\) is equivalent, residue by residue, to \(B+S_r=\mathbb Z\). Hence \(S_r=c_r+3\mathbb Z\) with a unique \(c_r\in\{0,1,2\}\). This gives the stated formula, and all \(3^g\) choices plainly tile. Undoing the initial translation yields the formula with \(-a_0\).

## Verification
A standard-library verifier exhaustively checks the spectral parametrization for \(1\le g\le 6\) and every coprime pair \(u,v\) in a bounded symmetric range satisfying the modular condition. It also exhaustively enumerates complements in \(\mathbb Z/(3g)\mathbb Z\) for \(1\le g\le 6\), confirming exactly \(3^g\) complements and the predicted one-choice-per-residue structure. These finite checks are sanity checks only; the infinite statements are proved above by the unit-circle and finite-state/Fourier arguments.

## Relationship to prior work
Fu and Song (arXiv:2607.19858, first posted 2026-07-22) prove that every normalized finite spectral pair \(A\subset\mathbb Z\) has rational spectrum and use this to complete the reduction of one-dimensional Fuglede to finite cyclic analogues. Their accessible abstract states rationality, not an exact denominator or a cardinality-three moduli count. The result here sharpens that conclusion for three-point sets to denominators dividing \(3g\), and simultaneously classifies all normalized spectra and all integer tiling complements.

The congruence condition itself is not claimed as new. Three-digit spectral-measure literature already features the primitive condition \(\{u,v\}\equiv\{\pm1\}\pmod 3\); for example Wang, Yin and Zhang give it in their characterization of three-element Cantor-Moran measures. The contribution assessed here is the complete finite-pair parametrization and the paired tiling-complement classification with exact counts.

## Limitations
The full text of arXiv:2607.19858 was not available during this review; its abstract and bibliographic records were inspected, together with targeted searches for three-point specializations. Older three-digit spectral-measure papers were compared at the level of accessible abstracts and theorem summaries. Consequently there remains a literature risk that an equivalent cardinality-three parametrization or the exact counts \(g^2\) and \(3^g\) appear under different notation in a source not surfaced by those searches. The proof given here is self-contained and does not rely on the recent rationality theorem.

## References
1. Xiao-Ye Fu and Zi-Jian Song, *Rational Spectra for Finite Hadamard Pairs and Bounded Spectral Sets on the real line*, arXiv:2607.19858 (first posted 2026-07-22), DOI 10.48550/arXiv.2607.19858.
2. Cong Wang, Feng-Li Yin and Min-Min Zhang, *Spectrality of Cantor-Moran measures with three-element digit sets*, Forum Mathematicum 36 (2024), 429-445, DOI 10.1515/forum-2023-0114.
3. Yan-Song Fu and Cong Wang, *Spectra of a class of Cantor-Moran measures with three-element digit sets*, Journal of Approximation Theory 261 (2021), 105494, DOI 10.1016/j.jat.2020.105494.
