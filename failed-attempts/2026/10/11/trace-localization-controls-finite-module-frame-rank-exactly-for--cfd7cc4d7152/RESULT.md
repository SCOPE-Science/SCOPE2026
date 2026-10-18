# Trace localization controls finite module-frame rank, exactly for rectangular matrix Morita modules
## Finding
Let \(Z\) be an \(A\)-\(B\) imprimitivity bimodule with unital \(B\), let \(\tau:B\to\mathbb C\) be a faithful finite trace, and let \(\iota_\tau:Z\to\operatorname{Loc}_\tau(Z)\) denote localization with
\[
\|\iota_\tau z\|_{\operatorname{Loc}}^2=\tau(\langle z,z\rangle_B).
\]
Let \(m_{\mathrm{pf}}(Z)\) be the least length of a finite Parseval right module frame, meaning the least integer \(m\ge1\) for which there are \(w_1,\ldots,w_m\in Z\) satisfying
\[
\sum_{i=1}^m\langle w_i,w_i\rangle_B=1_B.
\]
Then
\[
\sqrt{\frac{\tau(1_B)}{m_{\mathrm{pf}}(Z)}}\le \|\iota_\tau\|\le \sqrt{\tau(1_B)}.
\]
Equivalently,
\[
m_{\mathrm{pf}}(Z)\ge \left\lceil\frac{\tau(1_B)}{\|\iota_\tau\|^2}\right\rceil.
\]
Both constants are uniformly sharp. For the standard \(M_r(\mathbb C)\)-\(M_s(\mathbb C)\) imprimitivity bimodule \(M_{r,s}(\mathbb C)\), equipped on the right with \(\langle X,Y\rangle=X^*Y\) and with \(\tau=c\operatorname{Tr}_s\), one has
\[
\|\iota_\tau\|=\sqrt{c\min\{r,s\}},\qquad
m_{\mathrm{pf}}=\left\lceil\frac sr\right\rceil
=\left\lceil\frac{\tau(1)}{\|\iota_\tau\|^2}\right\rceil.
\]
Thus localization distortion yields a quantitative obstruction to how short a finite Parseval module frame can be, and the obstruction is exact on every rectangular matrix Morita module.

## Assumptions and scope
The coefficient algebra \(B\) is unital and \(\tau\) is a bounded faithful finite trace. The module is an imprimitivity bimodule, so the finite Parseval-frame identity above is available in the finitely generated projective setting. No commutativity, separability, or normalization \(\tau(1_B)=1\) is assumed. The statement concerns the Banach-space operator norm of the canonical localization map; it does not assert that the displayed lower bound is an equality for arbitrary Hilbert \(C^*\)-modules.

For matrices, \(M_{r,s}(\mathbb C)\) carries its usual right \(M_s(\mathbb C)\)-module structure. The module norm is the operator norm because
\[
\|X\|_Z^2=\|X^*X\|.
\]
The localization norm induced by \(c\operatorname{Tr}_s\) is \(\sqrt c\) times the Hilbert--Schmidt norm.

## Proof
For the upper bound, positivity in a unital \(C^*\)-algebra gives
\[
0\le \langle z,z\rangle_B\le \|z\|_Z^2 1_B.
\]
Applying the positive functional \(\tau\) yields
\[
\|\iota_\tau z\|_{\operatorname{Loc}}^2
=\tau(\langle z,z\rangle_B)
\le \tau(1_B)\|z\|_Z^2,
\]
which proves \(\|\iota_\tau\|\le\sqrt{\tau(1_B)}\).

For the lower bound, choose a shortest Parseval frame \(w_1,\ldots,w_m\), where \(m=m_{\mathrm{pf}}(Z)\). Taking \(\tau\) in the frame identity gives the exact energy identity
\[
\sum_{i=1}^m\|\iota_\tau w_i\|_{\operatorname{Loc}}^2=\tau(1_B).
\]
Hence some \(j\) satisfies
\[
\|\iota_\tau w_j\|_{\operatorname{Loc}}^2\ge\frac{\tau(1_B)}m.
\]
Each summand \(\langle w_i,w_i\rangle_B\) is positive and their sum is \(1_B\), so \(0\le\langle w_i,w_i\rangle_B\le1_B\) and therefore \(\|w_i\|_Z\le1\). Consequently
\[
\|\iota_\tau\|\ge
\frac{\|\iota_\tau w_j\|_{\operatorname{Loc}}}{\|w_j\|_Z}
\ge\sqrt{\frac{\tau(1_B)}m}.
\]
Rearranging and using integrality gives the ceiling inequality.

The upper constant is sharp already for \(Z=B\) with its standard self-equivalence structure: the vector \(1_B\) has module norm \(1\) and localization norm \(\sqrt{\tau(1_B)}\).

Now take \(Z=M_{r,s}(\mathbb C)\) and \(\tau=c\operatorname{Tr}_s\). For every matrix \(X\),
\[
\|\iota_\tau X\|_{\operatorname{Loc}}=\sqrt c\,\|X\|_{\mathrm{HS}},
\qquad
\|X\|_Z=\|X\|_{\mathrm{op}}.
\]
A matrix of rank at most \(d=\min\{r,s\}\) satisfies
\[
\|X\|_{\mathrm{HS}}\le\sqrt d\,\|X\|_{\mathrm{op}},
\]
and equality is attained by a rank-\(d\) partial isometry. Hence
\[
\|\iota_\tau\|=\sqrt{cd}.
\]

It remains to compute the minimal Parseval-frame length. If \(X_1,\ldots,X_k\in M_{r,s}(\mathbb C)\) satisfy \(\sum_iX_i^*X_i=I_s\), then
\[
s=\operatorname{rank}(I_s)\le\sum_{i=1}^k\operatorname{rank}(X_i^*X_i)\le kr,
\]
so \(k\ge\lceil s/r\rceil\). Conversely partition \(\mathbb C^s\) into \(k=\lceil s/r\rceil\) mutually orthogonal coordinate subspaces, each of dimension at most \(r\). For each block choose a partial isometry \(X_i:\mathbb C^s\to\mathbb C^r\) whose initial projection is the corresponding block projection. Then \(\sum_iX_i^*X_i=I_s\), proving
\[
m_{\mathrm{pf}}=\left\lceil\frac sr\right\rceil.
\]
Finally, since \(\tau(1)=cs\) and \(\|\iota_\tau\|^2=c\min\{r,s\}\), the ceiling formula becomes exactly \(\lceil s/r\rceil\) in both regimes \(r<s\) and \(r\ge s\).

## Verification
The proof uses only positivity of the \(C^*\)-valued inner product, the finite Parseval identity, rank subadditivity, and the singular-value identity relating Hilbert--Schmidt and operator norms. Boundary cases were checked explicitly: for \(r\ge s\), one partial isometry gives a one-element Parseval frame and \(\|\iota_\tau\|^2=cs=\tau(1)\); for \(r<s\), the frame-length lower bound is the rank obstruction \(kr\ge s\). Scaling the trace by any \(c>0\) scales all localization norms by \(\sqrt c\), consistently on both sides.

No computation or finite enumeration is used as a substitute for proof. The arbitrary-module estimate is an inequality only; the exact formulas are asserted only for the rectangular matrix Morita family.

## Relationship to prior work
Bytchenkoff, Lamando, and Luef establish in Proposition 2.2 that a unital coefficient algebra in an equivalence bimodule yields a finite frame with \(\sum_i\langle w_i,w_i\rangle_B=1_B\), and Theorem 2.4 constructs the trace localization Hilbert space and its dense embedding. Their paper uses these ingredients to build Banach Gelfand triples and kernel theorems. The present finding combines the two structures quantitatively: trace mass distributed over a shortest Parseval frame forces a lower bound on localization distortion, and the matrix Morita family makes the resulting integer obstruction exact.

Frank and Larson develop the general theory of normalized tight module frames and their reconstruction properties, but do not study trace-localization distortion. Austad and Enstad study localization of Heisenberg modules and finite generators in the same broad Hilbert-module setting, but the inspected result concerns the concrete Heisenberg-module embedding and Gabor-frame generators, not the general frame-rank inequality or the rectangular matrix exactness above.

Semantic searches of the published published-finding corpus collection for GNS/localization norms, module-frame cardinality, Morita-equivalence generator number, and rectangular matrix imprimitivity modules found no statement that implies the displayed general inequality together with the exact matrix classification. The closest localization result found there concerns completeness boundaries for arbitrary-state localizations, not embedding distortion versus finite frame length.

## Limitations
The lower estimate may be non-sharp for a general imprimitivity bimodule; only the universal sharpness and the exact rectangular matrix family are proved. The result does not classify minimal frames beyond their length, does not treat unbounded traces, and does not claim that localization norm alone determines frame length outside the matrix family. An older equivalent observation may exist in finite-index, quasi-basis, or Morita-dimension language; the inspected literature and database searches did not locate one.

## References
1. D. Bytchenkoff, A. Lamando, F. Luef, *Banach Gelfand Triples with Kernel Theorems via Equivalence Bimodules*, arXiv:2609.37780v1, 2026. In particular Proposition 2.2 and Theorem 2.4.
2. M. Frank, D. R. Larson, *Frames in Hilbert C*-modules and C*-algebras*, arXiv:math/0010189; Journal of Operator Theory 48 (2002), 273--314.
3. A. Austad, U. Enstad, *Heisenberg Modules as Function Spaces*, Journal of Fourier Analysis and Applications 26 (2020), article 24, doi:10.1007/s00041-020-09729-7.
