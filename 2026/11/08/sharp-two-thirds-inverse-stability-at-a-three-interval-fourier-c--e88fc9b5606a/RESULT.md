# Sharp two-thirds inverse stability at a three-interval Fourier collision

## Finding

For fixed \(L>0\) and \(d>3L\), set
\[
\Omega_{u,v}=[0,L]\cup[d+u,d+u+L]\cup[2d+v,2d+v+L],\qquad f_{u,v}=\mathbf1_{\Omega_{u,v}}.
\]
Let \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx\), \(I_{u,v}(\xi)=|\widehat{f_{u,v}}(\xi)|^2\), and \(E(u,v)=\|I_{u,v}-I_{0,0}\|_{L^2(\mathbb R)}\). For all \(|u|,|v|<L/20\), there exist constants \(0<c_L\le C_L\), independent of \(d\), with
\[
\boxed{c_L\bigl(|v|+|u-v/2|^{3/2}\bigr)\le E(u,v)\le C_L\bigl(|v|+|u-v/2|^{3/2}\bigr).}
\]
The exponent \(2/3\) is sharp for recovering the two adjacent gaps from squared Fourier intensity in a neighborhood of the arithmetic-progression geometry. In the pure split direction \(u=\varepsilon\), \(v=0\), \(0<|\varepsilon|<L/20\), the exact identity is
\[
\boxed{\|I_{\varepsilon,0}-I_{0,0}\|_2^2=8|\varepsilon|^3.}
\]
Consequently \(\max\{|u|,|v-u|\}\le C'_L E(u,v)^{2/3}\) for sufficiently small \(E(u,v)\), and no larger inverse Hölder exponent is possible at the base point for these geometric gap parameters.

## Assumptions and scope

All intervals have the known, common length \(L>0\). Their left endpoints are \(0\), \(d+u\), \(2d+v\), with \(d>3L\) and \(|u|,|v|<L/20\); hence the components remain disjoint. Squared (not unsquared) Fourier magnitude is observed on the entire real frequency axis in the \(L^2\) metric. The baseline \(u=v=0\) has two coincident adjacent-distance values, causing a double autocorrelation peak. Translation and reflection of the entire set leave the magnitude invariant; the statement concerns the ordered gap parameters around this fixed baseline, not arbitrary unknown-length unions or all-pairs uniform stability.

## Proof

**1. Exact autocorrelation splitting.** Put \(K_L(t)=(L-|t|)_+\). If the left endpoints are \(a_0,a_1,a_2\), convolution with the reflection obeys
\[
f*\widetilde f=3K_L+\sum_{i<j}\bigl(K_L(\cdot-(a_j-a_i))+K_L(\cdot+(a_j-a_i))\bigr),\quad\widetilde f(t)=\overline{f(-t)}.
\]
For our left endpoints the three positive pair distances are \(d+u\), \(d+v-u\), and \(2d+v\). Write \(s=u-v/2\) and use translations \(T_hK_L(t)=K_L(t-h)\). The positive-lag difference consists of
\[
A=T_{v/2+s}K_L+T_{v/2-s}K_L-2K_L,
\qquad B=T_vK_L-K_L,
\]
with \(A\) located at \(d\) and \(B\) located at \(2d\). Their negative-lag mirrors are disjoint from them and from each other because \(d>3L\) and \(|u|,|v|<L/20\). The Fourier transform of the autocorrelation is \(I\). Plancherel therefore gives the exact identity
\[
E(u,v)^2=2\|A\|_2^2+2\|B\|_2^2.\tag{1}
\]

**2. The cusp-splitting identity.** Define \(D_sK_L=T_sK_L+T_{-s}K_L-2K_L\). When \(0<|s|<L/2\), \(D_sK_L\) consists of three nonoverlapping triangular tents centered at \(-L\), \(0\), and \(L\), with heights \(|s|\), \(2|s|\), and \(|s|\), respectively (the central tent has negative sign). A triangular tent of height \(H\) and half-width \(h\) has squared \(L^2\) norm \(2hH^2/3\). Thus
\[
\boxed{\|D_sK_L\|_2^2=4|s|^3}\tag{2}
\]
including \(s=0\) by continuity.

**3. Separation of the two geometric directions.** Since \(K_L\) is absolutely continuous with \(\|K_L'\|_2=\sqrt{2L}\),
\[
\|T_hK_L-K_L\|_2\le\sqrt{2L}|h|.
\]
On a linear-slope segment of length \(L-|v|\), the difference \(T_vK_L-K_L\) has magnitude \(|v|\), so
\[
\sqrt{L-|v|}|v|\le\|B\|_2\le\sqrt{2L}|v|.\tag{3}
\]
Also \(A=T_{v/2}D_sK_L+2(T_{v/2}K_L-K_L)\), so (2) and the translation estimate imply
\[
2|s|^{3/2}-\sqrt{2L}|v|\le\|A\|_2\le2|s|^{3/2}+\sqrt{2L}|v|.\tag{4}
\]
The upper estimate, (3), and (1) yield \(E\le C_L(|v|+|s|^{3/2})\). Conversely, as \(|v|<L/20\), (1) and (3) imply \(|v|\le E/\sqrt{2(19L/20)}\). Equations (1) and (4) then imply \(2|s|^{3/2}\le E/\sqrt2+\sqrt{2L}|v|\), hence \(|v|+|s|^{3/2}\le E/c_L\) for a positive \(c_L\). This proves the two-sided statement uniformly in \(d>3L\).

**4. Optimal exponent.** With \(v=0\) and \(u=\varepsilon\), (1) and (2) yield \(E^2=2\cdot4|\varepsilon|^3=8|\varepsilon|^3\). The adjacent gaps become \(d+\varepsilon\) and \(d-\varepsilon\), so their error is exactly \(|\varepsilon|\). If an inverse exponent \(\gamma>2/3\) held with a uniform constant at this baseline, it would imply \(|\varepsilon|\le C(2\sqrt2|\varepsilon|^{3/2})^\gamma\), impossible as \(\varepsilon\to0\). Finally \(\max\{|u|,|v-u|\}\le |s|+|v|/2\), and for \(E\le1\), the lower estimate controls \(|s|\) by a constant times \(E^{2/3}\) and \(|v|\) by a constant times \(E\le E^{2/3}\). This proves the recovery exponent.

## Verification

`python3 CHECK.py` uses exact rational arithmetic to integrate the square of the piecewise-linear autocorrelation difference (via its breakpoints and trapezoid-polynomial integral), without assuming (1)--(2) as a computational identity. It checks the exact \(8|\varepsilon|^3\) law for three rational interval lengths and several positive shifts, plus nontrivial two-parameter perturbations. The unrestricted claim is supported by the preceding analytic proof; finite checks are corroborative, not an infinite proof.

## Relationship to prior work

Xia and Xu (arXiv:2606.19855, first publicly posted June 18, 2026) study Fourier phase retrieval for finite interval unions. Their reported uniqueness and stability theorem for one or two components does not imply local optimal stability at the first equal-width three-component distance collision; their nonuniqueness examples for three or more components do not imply the present local estimate. Ranieri and collaborators (arXiv:1308.3058) analyze sparse-signal uniqueness under collision-free support differences, whereas this construction has a repeated difference at baseline and supplies a quantitative inverse modulus at that collision. Novikov and White (arXiv:2011.00619) study multidimensional sparse-support recovery, not this one-dimensional equal-interval sharp exponent. The present result isolates the cusp geometry of a *double autocorrelation peak* and computes its sharp local inverse power. Older covariogram or B-spline translation-stability formulations might contain an equivalent calculation; no unconditional publication priority is claimed.

## Limitations

Only the anchored, fixed-width, three-interval family near one equally spaced baseline is covered. The estimate is not a globally uniform inverse modulus over arbitrary interval unions, does not assert all-pairs local bi-Hölder stability, and concerns full, noiseless, continuous squared Fourier intensity measured in \(L^2\). It gives no reconstruction algorithm, finite-frequency sampling guarantee, or error bound under unknown interval lengths. The proof of the analytical theorem is internal; independent verification has not been performed.

## References

1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855 (first posted 2026-06-18), https://arxiv.org/abs/2606.19855.
2. Juri Ranieri, Amina Chebira, Yue M. Lu and Martin Vetterli, *Phase Retrieval for Sparse Signals: Uniqueness Conditions*, arXiv:1308.3058, https://arxiv.org/abs/1308.3058.
3. S. Novikov and S. White, *Support Recovery for Sparse Multidimensional Phase Retrieval*, arXiv:2011.00619, https://arxiv.org/abs/2011.00619.
