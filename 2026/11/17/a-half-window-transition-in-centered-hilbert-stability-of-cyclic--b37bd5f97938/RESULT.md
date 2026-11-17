# A half-window transition in centered-Hilbert stability of cyclic maximum filters

## Finding
For integers \(n\ge2\) and \(1\le w\le n\), consider the cyclic sliding-maximum operator
\[
(M_{n,w}x)_i=\max_{0\le j<w}x_{(i+j)\bmod n},\qquad 0\le i<n.
\]
For a real vector let \(\bar h=n^{-1}\sum_i h_i\), and set
\[
H_n(h)=\left(\sum_{i=0}^{n-1}(h_i-\bar h)^2\right)^{1/2}.
\]
Then the **exact attained two-input Lipschitz constant** is
\[
L_{n,w}=\sup_{H_n(x-y)>0}\frac{H_n(M_{n,w}x-M_{n,w}y)}{H_n(x-y)}
=\begin{cases}
\sqrt{w},&2w\le n,\\
\sqrt{2w(n-w)/n},&2w\ge n.
\end{cases}
\]
The two branches coincide when \(2w=n\). In particular \(L_{n,1}=1\), \(L_{n,n}=0\), and \(L_{n,w}>1\) for every \(2\le w<n\). For fixed \(n\), the largest constant occurs at \(w=\lceil n/2\rceil\), with squared value \(2\lceil n/2\rceil\lfloor n/2\rfloor/n\) (which equals \(n/2\) in even dimensions). Thus the largest two-input amplification grows on the order of \(\sqrt n\). The formula changes branch at the half-window threshold.

## Assumptions and scope
The entries of \(x,y\) are arbitrary real numbers; all indices are cyclic modulo \(n\); every window consists of exactly \(w\) consecutive sites. The seminorm is the centered, unweighted Euclidean seminorm; the ratio excludes constant input differences. Constant-shift equivariance of the maximum filter makes the map well defined on the quotient by constants. No ordering or nonnegativity assumption is imposed on inputs.

## Proof
**1. Coordinate-selector chambers.** Off the finite collection of coordinate-tie hyperplanes, each window has a unique maximizing coordinate. On such a chamber \(M_{n,w}\) agrees with a copying map \((B_\sigma h)_i=h_{\sigma(i)}\). Write \(c_j=|\sigma^{-1}(j)|\); thus \(\sum_jc_j=n\). Every site belongs to exactly \(w\) of the cyclic windows, so \(c_j\le w\). In addition the unique globally largest site is selected in all \(w\) windows containing it, hence one multiplicity equals \(w\).

For any copying map with multiplicities \(c_j\), its output centered energy is
\[
H_n(B_\sigma h)^2=\min_{a\in\mathbb R}\sum_j c_j(h_j-a)^2.
\]
Its input energy is \(H_n(h)^2=\min_a\sum_j(h_j-a)^2\).

**2. Short windows.** If \(2w\le n\), then
\[
H_n(B_\sigma h)^2\le\sum_jc_j(h_j-\bar h)^2\le w\,H_n(h)^2.
\]
The inequality holds for every chamber, hence by continuity and finite piecewise linearity for all input pairs.

For sharpness choose \(p=0\), \(q=w\). Since \(2w\le n\), the families of windows containing \(p\) and \(q\) are disjoint. Take a baseline with \(x_p=4\), \(x_q=2\), and all other entries distinct in \((0,1)\). Then exactly \(w\) outputs copy \(p\) and exactly \(w\) outputs copy \(q\). Perturb by \(\varepsilon(e_p-e_q)\), for sufficiently small \(\varepsilon>0\). The input difference has squared centered energy \(2\varepsilon^2\); the output difference has squared centered energy \(2w\varepsilon^2\). This attains \(\sqrt w\).

**3. Long windows.** Suppose \(2w>n\) and write \(r=n-w\). Let \(p\) be the globally maximal input coordinate, so \(c_p=w>n/2\). For any real \(h\), write \(R=\max_jh_j-\min_jh_j\). The output energy is a convex function of \(h\): it is the positive-semidefinite quadratic form
\[
H_n(B_\sigma h)^2=\sum_j c_jh_j^2-\frac1n\left(\sum_jc_jh_j\right)^2.
\]
Its maximum on the box bounded by the smallest and largest coordinates of \(h\) occurs at a binary vertex. On a binary vertex with the high set of total copying multiplicity \(t\), the energy is \(t(n-t)R^2/n\). Since one copying multiplicity is \(w>n/2\), necessarily \(t\le r\) or \(t\ge w\). Therefore \(t(n-t)\le wr\) and
\[
H_n(B_\sigma h)^2\le\frac{wr}n R^2.
\]
For any real input, the two extreme coordinates alone imply
\[
H_n(h)^2=\min_a\sum_j(h_j-a)^2\ge\min_a\bigl[(\min h-a)^2+(\max h-a)^2\bigr]=R^2/2.
\]
Consequently \(H_n(B_\sigma h)^2\le2wr\,H_n(h)^2/n\), and the piecewise-linear argument again gives the global two-input bound. When \(w=n\), all outputs equal the global maximum and the seminorm vanishes identically.

For sharpness when \(n/2<w<n\), take \(p=0\) and \(q=n-w\). The \(n-w\) cyclic windows avoiding \(p\) all contain \(q\). Choose a baseline with \(x_p=4\), \(x_q=2\), and all other entries distinct in \((0,1)\); then \(p\) is copied exactly \(w\) times and \(q\) exactly \(r=n-w\) times. Perturb by \(\varepsilon(e_p-e_q)\). The output difference takes values \(+\varepsilon\) at \(w\) sites and \(-\varepsilon\) at \(r\) sites. Its squared centered energy is \(4wr\varepsilon^2/n\), while the input squared energy is \(2\varepsilon^2\). This attains the long-window bound.

**4. Passage across ties and nonexpansivity classification.** A line segment between any two inputs meets finitely many selector chambers; summing their quotient-seminorm estimates gives the same bound on the whole segment, with boundary segments handled by continuity. For \(2\le w\le n/2\), the squared constant \(w\) exceeds one. For \(n/2<w<n\), the squared constant \(2w(n-w)/n\) is at least \(2(n-1)/n>1\) when \(n>2\). The endpoint cases were established above.

## Verification
The supplementary file `verify_hilbert.py` uses exact rational arithmetic for two-input tests and sharp two-peak witnesses. It also exhausts all strict coordinate orders through dimension seven, testing the copy-map estimates along two-site directions. Its diagnostic output includes 812314 such chamber tests, 5292 rational two-input inequalities, and 171 exact attaining examples. These are finite corroborations, not a substitute for the proof covering every dimension and window size.

## Relationship to prior work
Mathematical morphology's dilation is a maximum over neighborhoods; graph morphology and its lattice/adjunction structure are surveyed in Najman and Cousty, *A graph-based mathematical morphology reader* (arXiv:1404.7748v1, 30 April 2014), especially Section 3. Cousty, Najman, Dias, and Serra, *Morphological filtering on graphs* (2013), concerns graph-morphological operators, adjunctions, openings, and denoising; the available bibliographic abstract does not assert a centered-Hilbert two-input norm. Previous results on finite-window morphology in weighted path total variation address a different seminorm. The present theorem calculates a sharp quotient-Hilbert perturbation modulus of the cyclic real-valued maximum filter, including the nontrivial half-window transition. The relevant prior works do not, from the material inspected, imply the stated sharp centered-Hilbert formula.

## Limitations
The theorem assumes a fixed contiguous cyclic window and unweighted centered Euclidean variation. It does not treat general irregular incidence systems, weighted mean/variance seminorms, multivariate max ordering, or compositions of different-width filters. An inaccessible full text of the 2013 graph-morphology paper leaves a residual bibliographic-priority risk.

## References
1. Laurent Najman and Jean Cousty, *A graph-based mathematical morphology reader*, arXiv:1404.7748v1, first posted 30 April 2014, https://arxiv.org/html/1404.7748v1.
2. Jean Cousty, Laurent Najman, Fabio Dias, and Jean Serra, *Morphological filtering on graphs*, *Computer Vision and Image Understanding* 117(4) (2013), 370–385, DOI:10.1016/j.cviu.2012.08.016. Full text not inspected.
