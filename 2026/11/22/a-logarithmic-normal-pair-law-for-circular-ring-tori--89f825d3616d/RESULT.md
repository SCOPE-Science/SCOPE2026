# A logarithmic normal-pair law for circular ring tori

## Finding
For any embedded circular ring torus, let two surface-area-uniform points be sampled independently and let \(T\) be the Euclidean dot product of their outward unit Gauss normals. The **entire** distribution of \(T\) is the same for every major-to-minor radius ratio. Its precise Legendre coefficients and endpoint density laws are
\[
\mathbb E[P_{2k+1}(T)]=0,\qquad
\mathbb E[P_{2k}(T)]=\left(\frac{\binom{2k}{k}}{4^k}\right)^4\quad (k\ge0),
\]
\[
f_T(t)=\frac{1}{\pi^2}\log\frac1{1-|t|}+O(1)
\quad\text{as }t\to\pm1,
\]
where \(f_T\) is the density on \((-1,1)\). Equivalently, for the angle \(\Theta=\arccos T\),
\[
\Pr(\Theta<\varepsilon)
\sim\Pr(\pi-\Theta<\varepsilon)
\sim \frac{\varepsilon^2}{\pi^2}\log\frac1\varepsilon
\quad(\varepsilon\downarrow0).
\]
These are sharp leading constants, not merely logarithmic orders. The variance of the normal dot product is exactly \(3/8\). The normalized *one-point* Gauss image and its radius-ratio invariance were already derived by Horn (1983); the contribution here is the complete **independent normal-pair angular law**, its spectrum and sharp two-sided logarithmic rare-event constants.

An exact density representation for \(-1<t<1\) is
\[
 f_T(t)=\frac12+\sum_{k=1}^{\infty}\frac{4k+1}{2}
 \left(\frac{\binom{2k}{k}}{4^k}\right)^4P_{2k}(t).
\]
This Legendre series converges absolutely on compact subintervals of \((-1,1)\). A nonnegative integral representation, useful for independent verification, is
\[
 f_T(t)=\frac1{\pi^3}\int_{-1}^{1}\int_{-1}^{1}
 \frac{\mathbf 1\{(t-xy)^2<(1-x^2)(1-y^2)\}}
 {\sqrt{1-x^2}\sqrt{1-y^2}
 \sqrt{(1-x^2)(1-y^2)-(t-xy)^2}}\,dx\,dy.
\]

## Assumptions and scope
Choose arbitrary fixed real radii \(R>r>0\). Equip the embedded surface
\[
 X(u,v)=((R+r\cos u)\cos v,(R+r\cos u)\sin v,r\sin u),
 \qquad 0\le u,v<2\pi
\]
with its Euclidean area measure, normalized to total probability one. The outward normal is \(N(u,v)=(\cos u\cos v,\cos u\sin v,\sin u)\). Draw two independent points in this measure. Their normals are oriented outwards, and \(T=N_1\cdot N_2\). All assertions hold for every such \(R,r\) without a limit in the aspect ratio. The density statement concerns \(-1<t<1\) and the endpoint limits are one-sided.

## Proof
**1. Normal pushforward.** The area element is \(r(R+r\cos u)\,du\,dv\) and the total area is \(4\pi^2Rr\). For a given \(z=\sin u\in(-1,1)\), the two values of \(u\) have opposite cosines, so their area weights sum to \(2Rr\). Consequently \(Z=N_z\) has density \(1/(\pi\sqrt{1-z^2})\) on \((-1,1)\), while the azimuth is independent and uniform. This is also Horn's normalized extended Gaussian image. In particular, the normal law, and hence its independent pair law, does not depend on \(R/r\). Writing \(Z_j\) for two arcsine-distributed latitudes and \(\Delta\) for an independent uniform azimuth difference gives
\[
 T=Z_1Z_2+\sqrt{1-Z_1^2}\sqrt{1-Z_2^2}\cos\Delta.
\]
Conditioning on \(Z_1,Z_2\) immediately proves the displayed positive density integral and normalization.

**2. All spherical harmonic moments.** Let \(P_\ell\) denote the standard Legendre polynomial normalized by \(P_\ell(1)=1\). The spherical-harmonic addition formula, followed by independent expectation, and axial symmetry (which kills all nonzero azimuthal modes), gives
\[
 \mathbb E[P_\ell(N_1\cdot N_2)]
 =\bigl(\mathbb E[P_\ell(Z)]\bigr)^2.
\]
The arcsine measure is the projection of uniform arclength on a great circle; equivalently one may integrate the generating function for \(P_\ell\) on that circle. The standard great-circle integral yields
\[
 \frac1\pi\int_{-1}^1\frac{P_{2k}(z)}{\sqrt{1-z^2}}\,dz
 =P_{2k}(0)^2=\left(\frac{\binom{2k}k}{4^k}\right)^2,
\]
with every odd integral zero. This establishes the exact fourth-power Legendre coefficient formula. Since \(P_2(t)=(3t^2-1)/2\), the second moment \(\mathbb E[T^2]=3/8\) follows.

**3. Exact density series.** Legendre orthogonality with the probability density on \([-1,1]\) gives its degree-\(\ell\) coefficient as \((2\ell+1)\mathbb E[P_\ell(T)]/2\). With \(b_k=\binom{2k}k/4^k\), the coefficient of \(P_{2k}\) is \(c_k=(4k+1)b_k^4/2\). By Stirling's formula,
\[
 c_k=\frac2{\pi^2 k}+O(k^{-2}).
\]
For any compact \(I\subset(-1,1)\), the standard Legendre estimate \(|P_n(\cos\theta)|\le C(n\sin\theta)^{-1/2}\) shows absolute and locally uniform convergence of \(\sum_{k\ge1}c_kP_{2k}(t)\). Moreover, integration of the same Legendre estimate gives \(\int_{-1}^1 |P_{2k}(t)|\,dt=O(k^{-1/2})\); thus \(\sum_k\|c_kP_{2k}\|_{L^1(-1,1)}<\infty\). The series is therefore an actual \(L^1\) density. Orthogonality gives exactly the computed polynomial moments, including total mass one. Since measures on \([-1,1]\) are uniquely determined by their polynomial moments, the series coincides almost everywhere with the preceding conditional probability density. Its locally uniform representative is the density asserted here.

**4. Sharp endpoint logarithms.** Set \(t=\cos\theta\) with \(\theta\downarrow0\), and put \(K=\lfloor1/\theta\rfloor\). For \(k\le K\), the derivative bound \(|P_n'|\le n(n+1)/2\) on \([-1,1]\) yields \(P_{2k}(\cos\theta)=1+O(k^2\theta^2)\). Hence
\[
 \sum_{k\le K}\frac{P_{2k}(\cos\theta)}{k}
 =\log\frac1\theta+O(1).
\]
For \(k>K\), the preceding Legendre estimate yields
\[
 \sum_{k>K}\frac{|P_{2k}(\cos\theta)|}{k}
 \le C\theta^{-1/2}\sum_{k>K}k^{-3/2}=O(1).
\]
Because \(\sum|c_k-2/(\pi^2k)|<\infty\), this proves
\[
 f_T(\cos\theta)=\frac2{\pi^2}\log\frac1\theta+O(1)
 =\frac1{\pi^2}\log\frac1{1-\cos\theta}+O(1).
\]
Every odd Legendre coefficient vanishes, so \(f_T(-t)=f_T(t)\). Thus the same logarithm holds at \(-1\). Integrating over \(t\in(\cos\varepsilon,1)\), where \(1-\cos\varepsilon\sim\varepsilon^2/2\), gives the sharp angle-tail formula. All error terms here are for a fixed universal normal law, with no geometric parameter in the constants.

## Verification
Run `python checks/verify.py` from the directory containing this file. That self-contained checker requires Python, NumPy, SciPy and SymPy. It tests nine exact arcsine–Legendre moment identities, directly samples the correct surface-area measure at three aspect ratios, and compares the spectral density at two shrinking polar angles against the predicted leading logarithm. The included output was checked when the files were assembled; finite tests are **not** the infinite proof, which consists of the identities and bounds above.

## Relationship to prior work
Horn's *Extended Gaussian Images* (MIT AI Memo 740, July 1983; IEEE 1984) derives the torus's area-weighted normal image \(G(\xi,\eta)=2Rr\sec\eta\), identifies its polar singularities, and states that equal-area tori have equal extended Gaussian images. These one-point results, including shape invariance, are **not new claims** here. The present independent two-point dot-product spectrum and the sharp near-parallel and near-antiparallel logarithmic coefficients are additional operations on that known image; neither appears in the inspected torus sections of Horn's memoir. Pérez-Saborid (2008) supplies the generic spherical-harmonic addition framework used in the derivation, but does not evaluate this toroidal probability law. Petrou (1997) studies normal-pair angular histograms alongside chord lengths for surface characterization, rather than this analytical toroidal law. A published torus chord-moment study concerns the Euclidean separation of two surface points, which differs from their normal-angle distribution.

## Limitations
No claim is made that the single-normal Gauss image or its radius invariance was first discovered here. The novel-status assessment is restricted to the paired harmonic spectrum and endpoint sharpness; unindexed or inaccessible older directional-statistics literature could contain an equivalent calculation. The result requires independently sampled **area-uniform** points on a smooth embedded circular ring torus and outwards-oriented normals. It does not cover spindle or horn tori, sampling uniformly in a parameter, correlated point pairs, arbitrary toroidal deformations or inference of the radius ratio from this pair statistic. The displayed spectral density is an interior formula; it diverges integrably at the endpoints. No independent mathematical audit has been conducted.

## References
- B. K. P. Horn, *Extended Gaussian Images*, MIT Artificial Intelligence Memo 740, July 1983, especially §§6.3–6.4, https://www.cs.jhu.edu/~misha/Papers/Horn83.pdf; later *Proceedings of the IEEE* **72** (1984), 1671–1686, DOI:10.1109/PROC.1984.13073.
- M. Pérez-Saborid, *The coordinate-free approach to spherical harmonics*, first posted June 20, 2008, arXiv:0806.3367, especially the spherical-harmonic addition formula, https://arxiv.org/abs/0806.3367.
- M. Petrou, *3D Surface Roughness Quantification*, BMVC 1997, practical normal-pair/chord-angle histogram method, archived material timestamped July 1, 1997, https://bmva-archive.org.uk/bmvc/1997/papers/066/node3.htm.
- E. W. Weisstein, *Torus*, MathWorld, classical surface area element, https://mathworld.wolfram.com/Torus.html.
