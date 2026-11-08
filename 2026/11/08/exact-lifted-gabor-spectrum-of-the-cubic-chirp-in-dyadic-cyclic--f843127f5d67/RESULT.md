# Exact lifted Gabor spectrum of the cubic chirp in dyadic cyclic dimensions

## Finding
For every integer \(k\ge1\), put \(N=2^k\) and \(g(x)=\exp(2\pi i x^3/N)\) on \(\mathbb Z/N\mathbb Z\). Let \(T_u g(x)=g(x+u)\), \(M_v g(x)=\exp(2\pi i vx/N)g(x)\), and let \(\mathcal L\) be the **complex-linear**, full-data Gabor intensity lifting
\[
\mathcal L(H)_{u,v}=\langle H,(M_vT_u g)(M_vT_u g)^*\rangle_{HS},\qquad (u,v)\in(\mathbb Z/N\mathbb Z)^2.
\]
Its exact complex rank and nullity are
\[
\operatorname{rank}\mathcal L=\frac{N^2+2}{3},\qquad \dim\ker\mathcal L=\frac{2(N^2-1)}3.
\]
All nonzero singular values (Hilbert--Schmidt domain and Euclidean codomain; **unnormalized** window) are
\[
N^{3/2}\quad\text{with multiplicity }2,
\qquad
\sqrt N\,2^{(k+t+1)/2}\quad\text{with multiplicity }4^{k-t-1},\quad t=0,\ldots,k-2.
\]
No other singular values occur. The condition number on the orthogonal complement of the kernel is exactly \(\sqrt{N/2}\), interpreted as \(1\) when \(N=2\). An explicit Weyl basis of the nullspace is characterized by the zero conditions below.

## Assumptions and scope
Indices \(x,u,v,a,b\) are residue classes modulo \(N\). The phase \(\exp(2\pi i x^3/N)\) is independent of the integer representative. A Weyl operator is \(M_bT_a\) with translation as defined above. The inner product is the standard complex Hilbert--Schmidt product. Zero singular values are counted with multiplicity. For \(a\ne0\), \(t=v_2(a)\) denotes its unique valuation between \(0\) and \(k-1\). This is a theorem about the complex-linear operator on **all** complex matrices, not a complete nonlinear phase-retrieval classification.

Define the unnormalized self-ambiguity
\[
A(a,b)=\sum_{x\bmod N}\overline{g(x)}g(x+a)\exp(-2\pi i bx/N).
\]
For \(a=0\), it is nonzero precisely at \(b=0\), with magnitude \(N\). For \(a\ne0\) of valuation \(0\le t\le k-2\), it is nonzero precisely when \(b\equiv3a^2\pmod {2^{t+1}}\), and then
\[
|A(a,b)|=2^{(k+t+1)/2}.
\]
For the remaining shift \(a=N/2\), it is nonzero at precisely one modulation,
\[
b\equiv3a^2+N/2\pmod N,
\]
with magnitude \(N\). These conditions include the boundary case \(k=1\).

## Proof
**Step 1: Reduction to a quadratic Gauss sum.** Expanding the cubic difference gives exactly
\[
A(a,b)=e^{2\pi i a^3/N}\sum_{x\bmod N}e^{2\pi i(3ax^2+(3a^2-b)x)/N}.
\]
Write \(B=3a^2-b\). Suppose first that \(a\ne0\), with \(3a=2^t c\) where \(c\) is odd. Translating \(x\) by \(2^{k-t}\) in the summand establishes vanishing unless \(2^t\mid B\); when this divisibility holds, the quadratic sum is \(2^t\) times the primitive sum at modulus \(2^{k-t}\), with odd quadratic coefficient \(c\).

**Step 2: Primitive dyadic Gauss sums, including the exceptional final digit.** For any odd \(c\), the sum
\[
G_m(c,d)=\sum_{x\bmod 2^m}e^{2\pi i(cx^2+dx)/2^m}
\]
obeys the following exact modulus laws. If \(m\ge2\), shifting \(x\mapsto x+2^{m-1}\) cancels terms whenever \(d\) is odd. For even \(d=2e\), the substitution \(x\mapsto x-c^{-1}e\) completes the square; thus its magnitude is that of \(G_m(c,0)\). Squaring the latter magnitude and introducing \(h=x-y\) yields
\[
|G_m(c,0)|^2=\sum_{h\bmod2^m}e^{2\pi ich^2/2^m}\sum_{y\bmod2^m}e^{2\pi i(2chy)/2^m}=2^{m+1}.
\]
Indeed, because \(c\) is odd, only \(h=0,2^{m-1}\) contribute, and both quadratic phases equal one for \(m\ge2\). Hence \(|G_m(c,d)|=2^{(m+1)/2}\) exactly for even \(d\), and zero otherwise. If \(m=1\), direct evaluation gives \(G_1(c,d)=1+(-1)^{c+d}\), so its magnitude is two exactly when \(d\) is odd and zero otherwise. Combining these cases with Step 1 proves all of the stated ambiguity conditions and magnitudes.

**Step 3: Exact counts.** For \(0\le t\le k-2\), there are \(2^{k-t-1}\) shifts \(a\) with that valuation, and, per such shift, precisely \(2^{k-t-1}\) allowed modulations \(b\). The resulting multiplicity is \(4^{k-t-1}\). The origin and the one shift \(a=N/2\) supply two further nonzero coefficients, each of magnitude \(N\). Therefore
\[
\#\{(a,b):A(a,b)\ne0\}=2+\sum_{j=1}^{k-1}4^j=\frac{N^2+2}{3}.
\]
The other \(2(N^2-1)/3\) coefficients vanish.

**Step 4: Operator diagonalization and normalization.** The normalized Weyl matrices \(N^{-1/2}M_bT_a\) form an orthonormal basis of the Hilbert--Schmidt matrix space. Under conjugation by a time-frequency shift, each Weyl basis element acquires a unit-modulus character factor. Its measurement coefficient is the corresponding ambiguity coefficient, up to conjugation and phase. Orthogonality of the full \(N^2\)-point character table makes these image vectors mutually orthogonal with Euclidean norms \(\sqrt N\,|A(a,b)|\). Consequently each Weyl matrix is an eigenvector of \(\mathcal L^*\mathcal L\) with eigenvalue \(N|A(a,b)|^2\). This proves both the spectrum and the Weyl-basis kernel characterization. The smallest positive ambiguity modulus is \(\sqrt{2N}\) (for \(k=1\), this equals \(N\)); the largest is \(N\), giving the stated positive condition number.

## Verification
Run the independent arithmetic/numeric checker with `python check_dyadic_cubic.py` in an environment with Python 3 and NumPy. The script computes cyclotomic zero tests by the **exact** coefficient criterion \(c_j=c_{j+N/2}\) for every opposite pair of exponents (the cyclotomic polynomial is \(X^{N/2}+1\)); it checks the complete ambiguity-support and magnitude multiplicities for \(N=2,4,8,16,32,64,128\). It also directly computes complex ambiguity sums through \(N=32\) and directly diagonalizes the full lifted projector Gram matrix at \(N=2,4,8\). The emitted terminal marker is `DYADIC_CUBIC_GABOR_CERTIFICATE_PASS`. The unbounded theorem rests on Steps 1--4, not extrapolation from these tests.

## Relationship to prior work
Bojarovska and Flinth, *Phase Retrieval from Gabor Measurements* (first public preprint 19 March 2015), establish the Weyl/ambiguity diagonalization underlying the general Gabor lifting criterion (their Theorem 2.3) and specifically observe that the cubic Alltop window has unavoidable zero ambiguities (their Example 2.3). The general diagonalization and the mere existence of zeros are **not claimed as new**. The present result is the complete **dyadic** valuation-by-valuation ambiguity distribution and resulting exact projector-lift rank, singular spectrum and kernel. This is not implied by the existence-of-zeros statement alone. A later algebraic-perturbation study of Gabor windows observes systematic cubic-chirp zeros at prime-power moduli but its abstract does not supply an exact dyadic multiplicity theorem; its full text was not available for exhaustive comparison. Known odd-primary cubic-chirp calculations do not automatically include the exceptional modulus-two Gauss-sum cases used here.

## Limitations
The theorem applies only to unnormalized cubic-phase windows on cyclic groups of order a power of two, with the specified lifted **complex-linear** measurement map. It does not assert injectivity on all vectors up to phase, determine optimal recovery from partial measurements, or establish novelty against every older source under an alternative Fourier or coding formulation. Independent mathematical validation has not been performed.

## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (19 March 2015), Sections 2.2--2.4. https://arxiv.org/abs/1503.05800
2. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (9 September 2026), abstract. https://arxiv.org/abs/2609.09614
3. W. O. Alltop, *Complex sequences with low periodic correlations*, IEEE Transactions on Information Theory 26 (1980), 350--354, as cited in reference 1 (not independently inspected).
