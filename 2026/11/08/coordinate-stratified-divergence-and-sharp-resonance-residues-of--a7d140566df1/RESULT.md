# Coordinate-stratified divergence and sharp resonance residues of Fourier mean bodies of cubes

## Finding
For every integer \(n\ge2\), let \(Q_n=[-1,1]^n\). For \(p>0\), its Fourier mean body is specified by
\[
\rho_{F_pQ_n}(u)^p=\frac{p}{2^n}\int_0^\infty |\widehat{\mathbf1_{Q_n}}(ru)|^2r^{p-1}\,dr,
\qquad u\in S^{n-1},
\]
with the integral and radius permitted to be infinite. Use the Fourier transform convention \(\widehat f(\xi)=\int f(x)e^{-i\langle x,\xi\rangle}\,dx\). For every unit direction \(u\), let \(S=\{j:u_j\ne0\}\), \(k=|S|\), and list its positive nonzero absolute coordinates as \(a_1,\ldots,a_k\). Then **the precise directional finiteness criterion** is
\[
\rho_{F_pQ_n}(u)<\infty\quad\Longleftrightarrow\quad 0<p<2k.
\]
Thus, at every \(p>0\), the entire set of directions of infinite radius is exactly the union of coordinate subspheres supported on at most \(\min\{n,\lfloor p/2\rfloor\}\) coordinates. In particular it is empty for \(p<2\), and it is the whole sphere for \(p\ge2n\).

For \(R>0\), define the truncated radial power
\[
H_{p,u}(R)=\frac p{2^n}\int_0^R|\widehat{\mathbf1_{Q_n}}(ru)|^2r^{p-1}\,dr.
\]
For each real \(\lambda\), set
\[
C_\lambda(a)=\sum_{\substack{\varepsilon\in\{-1,1\}^k\\ \sum_j\varepsilon_ja_j=\lambda}}\prod_{j=1}^k\varepsilon_j,
\qquad M(a)=4^{-k}\sum_\lambda C_\lambda(a)^2.
\]
Only finitely many \(C_\lambda\) are nonzero, and \(M(a)>0\). The complete critical and supercritical leading terms are
\[
H_{2k,u}(R)=\frac{2k\,2^nM(a)}{\prod_{j=1}^ka_j^2}\log R+O_{u,n}(1),
\]
\[
H_{p,u}(R)\sim\frac{p\,2^nM(a)}{(p-2k)\prod_{j=1}^ka_j^2}R^{p-2k}\quad(p>2k).
\]
The critical residue has the **sharp universal bound**
\[
0<M(a)\le\frac{\binom{2k}{k}}{4^k},
\]
and equality holds precisely when \(a_1=\cdots=a_k\) (automatically for \(k=1\)). Off the finite arrangement of resonance hyperplanes \(\sum_j\sigma_ja_j=0\) with \(\sigma_j\in\{-1,0,1\}\), not all zero, the residue is exactly \(M(a)=2^{-k}\).

The first genuinely three-frequency level has a complete five-value spectrum:
\[
\left\{M(a_1,a_2,a_3):a_j>0\right\}
=\left\{\frac3{32},\frac18,\frac5{32},\frac3{16},\frac5{16}\right\}.
\]
After sorting \(a_1\le a_2\le a_3\), these five values correspond, respectively, to all distinct with \(a_3=a_1+a_2\); all distinct without this additive equality; exactly two equal with \(a_3=a_1+a_2\); exactly two equal without it; and all three equal. Thus an additive frequency resonance can **decrease** the critical residue below its generic value, whereas equality of frequencies increases it.

## Assumptions and scope
All dimensions \(n\ge2\), all real \(p>0\), and every Euclidean unit direction are included. Coordinates can be zero or have arbitrary signs; only their positive absolute values enter the formulas. The estimates are pointwise in a fixed direction, not uniform as a direction approaches a resonance hyperplane or a coordinate subspace. The constants in the logarithmic remainder may depend on the direction. For \(p\ge 2k\), the full radial integral is infinite, so asymptotics concern its explicit finite-radius truncation rather than a finite radial value.

## Proof
**1. Exact reduction.** Coordinatewise integration gives
\[
\widehat{\mathbf1_{Q_n}}(ru)=2^n\prod_{j=1}^n\frac{\sin(ru_j)}{ru_j},
\]
where a zero coordinate contributes the limiting factor \(1\). Therefore, writing \(f_a(r)=\prod_{j=1}^k\sin^2(a_jr)\),
\[
H_{p,u}(R)=\frac{p\,2^n}{\prod_ja_j^2}\int_0^R f_a(r)r^{p-2k-1}\,dr.
\]
Near \(r=0\), \(f_a(r)=r^{2k}\prod_ja_j^2+O(r^{2k+2})\), so the integrand is locally integrable for every \(p>0\).

**2. Exact mean and noncancellation.** Expand
\[
\prod_{j=1}^k\sin(a_jr)=(2i)^{-k}\sum_{\varepsilon\in\{-1,1\}^k}\left(\prod_j\varepsilon_j\right)e^{ir\sum_j\varepsilon_ja_j}.
\]
The constant Fourier coefficient of its squared absolute value is exactly \(M(a)=4^{-k}\sum_\lambda C_\lambda(a)^2\); every other coefficient has nonzero frequency. Consequently
\[
\int_0^R f_a(r)\,dr=M(a)R+O_a(1).
\]
The nonzero trigonometric polynomial \(\prod_j\sin(a_jr)\) has a positive squared-mean coefficient, hence \(M(a)>0\). Expanding each squared sine separately also yields the alternative exact resonance formula
\[
M(a)=2^{-k}\sum_{\substack{\sigma\in\{-1,0,1\}^k\\ \sum_j\sigma_ja_j=0}}(-1/2)^{|\{j:\sigma_j\ne0\}|}.
\]

**3. Integrability and asymptotics.** If \(p<2k\), boundedness of \(f_a\) gives convergence at infinity. If \(p=2k\), separating the constant coefficient of \(f_a\) yields \(M(a)\int_1^Rdr/r=M(a)\log R\); each nonconstant exponential contributes a bounded term by integration by parts or Dirichlet's test. If \(p>2k\), put \(\delta=p-2k>0\). The constant coefficient contributes \(M(a)R^\delta/\delta+O(1)\) while each nonzero-frequency term is \(o(R^\delta)\) by integration by parts. Since \(M(a)>0\), the integral diverges at and above \(2k\). This proves all directional thresholds and leading constants. Counting supported coordinates gives the geometric filtration of infinite directions.

**4. Sharp residue bound and rigidity.** The arithmetic–geometric mean inequality gives, pointwise,
\[
f_a(r)\le \frac1k\sum_{j=1}^k\sin^{2k}(a_jr).
\]
Each summand has time mean \(\binom{2k}{k}/4^k\), so their means give the asserted upper bound. If some \(a_i\ne a_j\), then for sufficiently small positive \(r\) the values \(\sin^2(a_ir)\) are not all equal, making the nonnegative trigonometric-polynomial gap strictly positive somewhere. A nonzero, nonnegative finite trigonometric polynomial has strictly positive time mean: otherwise its bounded squared mean would be zero, contradicting the sum of squares of its nonzero Fourier coefficients. Hence equality is impossible unless all \(a_j\) coincide. When they coincide, the product is \(\sin^{2k}(a_1r)\), attaining the binomial mean. Outside the resonance hyperplanes, all nonzero \(\sigma\) have nonzero dot product with \(a\), so only \(\sigma=0\) survives and \(M(a)=2^{-k}\).

**5. Exhaustive three-frequency classification.** For \(k=3\), the only possible nontrivial zero-frequency relations in the ternary formula involve exactly two or three nonzero \(\sigma_j\). A pair relation occurs if and only if the corresponding positive frequencies are equal and contributes \(1/16\) per equal pair. A three-term relation occurs if and only if the largest frequency equals the sum of the other two and contributes \(-1/32\). Thus
\[
M(a_1,a_2,a_3)=\frac18+\frac{E(a)}{16}-\frac{T(a)}{32},
\]
where \(E(a)\) is the number of equal unordered coordinate pairs and \(T(a)\) is the indicator that the largest equals the sum of the other two. Positivity excludes \(T=1\) when all three are equal. The possible combinations are exactly the five values and cases stated in the finding.

## Verification
The standalone script `verify.py` independently computes the critical coefficient by grouped signed sums and by the ternary expansion using exact rational arithmetic. It exhaustively checks all positive integer triples with entries at most \(12\), including the complete three-frequency classification. It checks positivity, the sharp upper bound and its equality condition for all positive integer tuples with entries at most \(4\) and lengths one through six. Independent periodic numerical integration on representative integer tuples checks the trigonometric means. Run `python verify.py` with Python 3 standard library. The script reports `FOURIER_CUBE_CRITICAL_RESIDUES_OK 7198`. The infinite-dimensional quantifiers and asymptotics follow from the analytic proof, not these finite checks.

## Relationship to prior work
Langharst, Manui and Zvavitch introduced Fourier mean bodies, proved the cube's global compactness threshold \(p(Q_n)=2\), and displayed the exact product integral used above (their Definition 2, Theorem 5, Section 5, equation (142)). The present theorem does **not** claim those ingredients. Its additional statements resolve, for each individual cube direction, the exact support-dependent finiteness threshold; the logarithmic and polynomial divergence coefficients; the sign-resonance arithmetic; sharp maximal coefficient and equality; and the full first three-frequency spectrum. These conclusions use elementary trigonometric-polynomial averaging applied to that established integral; the result is a detailed evaluation of that specific geometric operator, not a new general Fourier averaging theorem.

## Limitations
This concerns axis-aligned cubes, or their trivial coordinatewise affine rescalings, not arbitrary convex bodies. It does not solve convexity or injectivity questions for Fourier mean bodies. The leading terms are for each fixed direction and are not uniform near coordinate-support changes or resonance hyperplanes. The formula for \(M\) is finite but potentially exponential in the number of active coordinates; no general closed classification of its minimum for \(k\ge4\) is asserted. Prior harmonic-analysis treatments of finite products of trigonometric functions may yield analogous coefficient identities. Historical priority beyond the checked sources therefore remains provisional. Independent validation has not been performed.

## References
1. D. Langharst, A. Manui and A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117, first posted 2026-01-27, version 2 posted 2026-06-30. Definition 2, Theorem 5 and Section 5, especially equation (142). https://arxiv.org/html/2601.20117v2 ; https://arxiv.org/abs/2601.20117 .
2. The algebraic identities for squared sine products and the time means of finite trigonometric polynomials are used with explicit derivations above; no independent novelty is claimed for those identities.
