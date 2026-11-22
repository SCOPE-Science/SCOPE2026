# Sharp corner-power trichotomy for planar Bergman Berezin transforms

## Finding
Let \(\Omega\subset\mathbb C\) be a bounded simply connected polygon and let \(0\in\partial\Omega\) be a vertex of interior angle \(\theta\in(0,2\pi)\). Rotate coordinates so that near zero \(\Omega\) is precisely the sector \(0<\arg z<\theta\). Put \(p=\pi/\theta\), choose \(\delta>0\) so small that the only boundary in \(|z|<2\delta\) consists of the two incident straight sides, and define the nonnegative measurable symbol
\[
g_\sigma(w)=|w|^\sigma\mathbf1_{\{|w|<\delta\}},\qquad \sigma\in\mathbb R.
\]
For the (unweighted) analytic Bergman kernel \(K_\Omega\), define the possibly infinite Berezin integral
\[
\mathfrak B_\Omega g(z)=\frac{1}{K_\Omega(z,z)}\int_\Omega |K_\Omega(z,w)|^2g(w)\,dA(w),\quad z\in\Omega,
\]
where \(dA\) is ordinary Euclidean area measure. Then the following is a **complete sharp trichotomy**, uniformly for \(\varphi\) in every compact subinterval of \((0,\theta)\), as \(r\downarrow0\) with \(z=re^{i\varphi}\):

1. For \(-2p<\sigma<2p\),
\[
\mathfrak B_\Omega g_\sigma(re^{i\varphi})=r^\sigma\big[M_{p,\sigma}(\varphi)+o(1)\big],\quad
M_{p,\sigma}(\varphi)=\frac{4\sin^2(p\varphi)}\pi\int_{\mathbb H}\frac{|v|^{\sigma/p}}{|e^{ip\varphi}-\overline v|^4}\,dA(v).
\]
The finite, positive response \(M_{p,\sigma}\) is universal: it is independent of the remaining geometry of \(\Omega\) and of \(\delta\).
2. At \(\sigma=2p\),
\[
\mathfrak B_\Omega g_{2p}(re^{i\varphi})\sim4p\sin^2(p\varphi)\,r^{2p}\log(1/r).
\]
3. For \(\sigma>2p\), choose any conformal map \(F:\Omega\to\mathbb H\) that extends to the corner with \(F(0)=0\) and has the locally normalized form \(F(w)=c w^p(1+O(|w|^p))\), \(c>0\). Define \(h_\sigma(v)=g_\sigma(F^{-1}(v))\). Then
\[
\mathfrak B_\Omega g_\sigma(re^{i\varphi})=C_{\Omega,\delta,\sigma}\sin^2(p\varphi)\,r^{2p}+o(r^{2p}),
\qquad C_{\Omega,\delta,\sigma}=\frac{4c^2}\pi\int_{\mathbb H}\frac{h_\sigma(v)}{|v|^4}\,dA(v)\in(0,\infty).
\]
The displayed coefficient is independent of the choice of such conformal map \(F\). For every \(\sigma\le-2p\), the Berezin integral is infinite at **every** interior evaluation point.

Moreover, the middle-regime profile is genuinely angular for \(\sigma\ne0\): it is reflection-symmetric, tends to \(1\) at either side of the sector, and at the angular bisector satisfies \(M_{p,\sigma}(\theta/2)>1\). Writing \(s=\sigma/p\), its bisector coefficient has the exact small-exponent expansion
\[
M_{p,ps}(\theta/2)=1+\left(\frac{\pi^2}{8}-\log2\right)s^2+O(s^4),\quad s\to0.
\]

## Assumptions and scope
The vertex is a genuine straight-sided polygonal corner; no convexity assumption is made. All powers are of Euclidean distance to that corner. The indicator cutoff ensures support strictly near the corner. The Berezin expression is an extended nonnegative integral; for symbols not in \(L^1(\Omega)\) it is **not** being asserted to represent a bounded Toeplitz operator. No statement is made for tangential approaches whose angle approaches either incident side simultaneously with the radius.

## Proof
**Conformal transport and corner expansion.** Conformal invariance of the unweighted analytic Bergman kernel gives, for \(u=F(z)\),
\[
\mathfrak B_\Omega g(z)=\frac{4(\operatorname{Im}u)^2}\pi\int_{\mathbb H}\frac{g(F^{-1}(v))}{|u-\overline v|^4}\,dA(v).\tag{1}
\]
Indeed \(K_{\mathbb H}(u,v)=-[\pi(u-\overline v)^2]^{-1}\) and \(K_{\mathbb H}(u,u)=[4\pi(\operatorname{Im}u)^2]^{-1}\). Straightening the two edges by \(w\mapsto w^p\), then applying Schwarz reflection, gives the local conformal expansion \(F(w)=c w^p+O(|w|^{2p})\), \(F'(w)=cpw^{p-1}(1+O(|w|^p))\). This holds uniformly on closed interior subsectors.

**Finite threshold.** Near \(v=0\), \(|F^{-1}(v)|^\sigma\asymp|v|^{\sigma/p}\), while for any fixed interior \(u\) the denominator in (1) tends to \(|u|^4>0\). The radial integral is comparable to \(\int_0^\varepsilon t^{1+\sigma/p}\,dt\), finite precisely if \(\sigma>-2p\). Away from the corner the symbol is bounded and compactly supported in the local sector, proving both the finiteness and global-divergence assertions.

**Universal Mellin range.** Set \(z=re^{i\varphi}\), \(u=cr^p(e^{ip\varphi}+o(1))\), and rescale \(v=cr^p\xi\) in (1). Multiplying by \(r^{-\sigma}\), the integrand converges to \(4\sin^2(p\varphi)|\xi|^{\sigma/p}/[\pi|e^{ip\varphi}-\overline\xi|^4]\). This is integrable near \(0\) if \(\sigma>-2p\) and at infinity if \(\sigma<2p\). On every compact interior angular interval the denominator has a positive uniform lower bound locally; the conformal corner bounds and the \(|\xi|^{-4}\) far tail permit dominated convergence. Terms from outside the corner neighborhood are \(O(r^{2p})\), which are negligible for \(\sigma<2p\). This proves the first regime, including uniformity.

**Critical logarithm.** For \(\sigma=2p\), divide the \(v\)-integral into \(|v|\lesssim r^p\), \(r^p\ll|v|\ll1\), and the remaining bounded region. The two outer terms contribute \(O(r^{2p})\) once a fixed comparison scale is chosen; on the intermediate region \(h_{2p}(v)\sim|v|^2/c^2\), \(|u-\overline v|^{-4}\sim|v|^{-4}\). Thus the angular integral is \(\pi\) and the radial contribution is
\[
\frac{4c^2r^{2p}\sin^2(p\varphi)}\pi\frac\pi{c^2}\int_{r^p}^{\varepsilon}\frac{dt}{t}
\sim4p\sin^2(p\varphi)r^{2p}\log(1/r).
\]
To make the comparison fully rigorous, first fix a sufficiently small outer scale and a sufficiently large inner ratio, use the displayed uniformly small relative errors on the intervening annulus, and then let these comparison parameters approach their limits. The omitted endpoint annuli have \(O(r^{2p})\) or an arbitrarily small fraction of the leading logarithm.

**Saturation.** If \(\sigma>2p\), \(h_\sigma(v)|v|^{-4}\) is integrable near zero (its radial exponent is \(\sigma/p-3>-1\)). Divide (1) by \(r^{2p}\) and use dominated convergence, separating a small disk around \(v=0\) to justify the uniform bound. The third formula follows. Möbius changes of the half-plane chart fixing \(0\) preserve its coefficient, either directly from (1) or from its interpretation as the unique limit.

**Angular contrast and exact local variance.** Reflection \(v\mapsto-\overline v\) proves angular symmetry. As \(\varphi\downarrow0\), the normalized half-plane Bergman probability concentrates at the boundary point \(1\); splitting off small neighborhoods of \(0\) and infinity and using the strict Mellin strip proves \(M_{p,\sigma}(\varphi)\to1\). At the bisector, use the disk coordinate \(q=(v-i)/(v+i)\). The normalized Berezin probability at \(i\) becomes uniform area probability in \(\mathbb D\), so
\[
M_{p,ps}(\theta/2)=\frac1\pi\int_{\mathbb D}\left|\frac{1+q}{1-q}\right|^s\,dA(q).
\]
The logarithm \(X(q)=\operatorname{Re}\log[(1+q)/(1-q)]\) has a symmetric nondegenerate law under \(q\mapsto-q\), so strict Jensen yields the claimed \(>1\) for nonzero \(s\). Moreover \(X=2\sum_{n\ge1,\,n\;\mathrm{odd}}\operatorname{Re}(q^n)/n\); orthogonality of disk monomials gives
\[
\mathbb E X^2=2\sum_{n\ge1,\,n\;\mathrm{odd}}\frac1{n^2(n+1)}=\frac{\pi^2}4-2\log2.
\]
Taylor expansion of the finite exponential moment for \(|s|<2\) completes the assertion.

## Verification
The accompanying `CHECK.py` performs finite high-precision quadrature diagnostics for the sector \(\theta=\pi/2\), confirms the symmetry of the exact Mellin integral, checks convergence in the middle regime, and tests the sharp logarithmic and saturated leading constants. These numerical diagnostics are sanity checks, not substitutes for the analytic dominated-convergence, conformal-mapping and Mellin proofs above. Direct reproduction: `python CHECK.py` with Python 3, NumPy and SciPy.

## Relationship to prior work
Taskinen (2021 online) establishes boundedness/Carleson/Berezin equivalences on polygonal Bergman spaces under an angle hypothesis, using weighted Forelli–Rudin estimates; it does not state this complete homogeneous corner-power asymptotic or the two critical exponents, universal angular profile and critical coefficient. Mannersalo (2018 preprint) gives generalized Toeplitz boundedness criteria using Whitney squares on polygons rather than a sharp Berezin corner response. The conformal Bergman-kernel transformation and Schwarz–Christoffel corner expansion are standard inputs and are not claimed new. The contribution assessed here is the full sharp local trichotomy including logarithmic resonance and exact angular response.

## Limitations
This is an analytic asymptotic theorem for one polygonal corner and localized power symbols, not a general boundedness criterion for arbitrary symbols, weighted Bergman spaces, or smoothly curved corners. Historical priority is provisional. No independent mathematical audit has been performed.

## References
- J. Taskinen, *Berezin transform and Toeplitz operators on polygonal domains*, Complex Variables and Elliptic Equations 67 (2022), 773–787; first available online 2021-09-23. https://doi.org/10.1080/17476933.2021.1978437
- P. Mannersalo, *Toeplitz operators on Bergman spaces of polygonal domains*, arXiv:1808.03308, first posted 2018-08-09. https://arxiv.org/abs/1808.03308
- K. Zhu, *Operator Theory in Function Spaces*, second edition, AMS, 2007, for classical Bergman kernels and Forelli–Rudin estimates.
