# Three-level lattice overlaps and a dimension-sharp Fourier-energy cusp for corner-truncated hypercubes

## Finding
For each integer \(d\ge3\) and real parameter \(0<a<1\), define the corner-truncated hypercube
\[
P_{d,a}=\{x\in[-1,1]^d:\textstyle\sum_{i=1}^d|x_i|\le d-a\}.
\]
Define its integer-lattice periodization \(W_{d,a}(u)=\sum_{n\in\mathbb Z^d}\mathbf1_{P_{d,a}}(u+n)\) on \([0,1)^d\), using boundaries modulo null sets, and put \(h=(a-\tfrac12)_+=\max(a-\tfrac12,0)\). For uniform \(u\in[0,1)^d\), the entire multiplicity distribution is
\[
\begin{aligned}
\Pr\{W=2^d-2\}&=\frac{2^d}{(d-1)!}h^d=:p_2,\\
\Pr\{W=2^d-1\}&=\frac{2^d}{d!}a^d-\frac{2^{d+1}}{(d-1)!}h^d=:p_1,\\
\Pr\{W=2^d\}&=1-\frac{2^d}{d!}a^d+\frac{2^d}{(d-1)!}h^d=:p_0.
\end{aligned}
\]
No other values occur almost everywhere. The levels \(2^d\) and \(2^d-1\) occur on sets of positive measure for all \(0<a<1\); the level \(2^d-2\) occurs on a set of positive measure if and only if \(a>1/2\). In particular, simultaneous loss of three lattice translates is impossible in *every* dimension, however large.

With integer-frequency transform \(F_{d,a}(k)=\int_{P_{d,a}}e^{-2\pi i k\cdot x}\,dx\), the exact total nonconstant Fourier energy is
\[
\boxed{\sum_{k\in\mathbb Z^d\setminus\{0\}}|F_{d,a}(k)|^2=\frac{2^d}{d!}a^d-\left(\frac{2^d}{d!}a^d\right)^2+\frac{2^{d+1}}{(d-1)!}(a-\tfrac12)_+^d.}
\]
As a function of \(a\), this energy is \(C^{d-1}\) but not \(C^d\) at \(a=1/2\); its right-minus-left derivative jump of order \(d\) equals \(2^{d+1}d\). The sharp upper limit of the double-loss fraction is \(\sup_{0<a<1}p_2=1/(d-1)!\). Thus the nonanalytic Fourier-energy onset has precisely dimension-dependent order, even though the number of possible overlap levels never grows with dimension.

## Assumptions and scope
All integrals are unnormalized Lebesgue integrals. The torus \(\mathbb R^d/\mathbb Z^d\) has normalized Haar measure represented by Lebesgue measure on \([0,1)^d\). The parameter restriction \(0<a<1\) ensures the \(2^d\) corner simplices removed from \([-1,1]^d\) have disjoint interiors. No lattice other than \(\mathbb Z^d\), no unequal-corner clipping, and no other clipping depths are asserted. The statement concerns the sum of squared integer Fourier coefficients, not their individual zeros or an exponential orthogonal basis.

## Proof
**1. Corner decomposition and periodization.** The complement of \(P_{d,a}\) inside \([-1,1]^d\) is the disjoint union, up to boundaries, of \(2^d\) simplices of edge depth \(a\), one at each sign vertex. Each has volume \(a^d/d!\). Fix \(u\in(0,1)^d\) away from all boundaries. The original cube has precisely \(2^d\) representatives \(u+n\), obtained by independently selecting \(n_i\in\{-1,0\}\). For each binary choice \(\varepsilon\in\{0,1\}^d\), the deficit of its representative from the corresponding cube corner is \(S_\varepsilon(u)=\sum_i y_{i,\varepsilon_i}\), where \(y_{i,0}=u_i\) and \(y_{i,1}=1-u_i\). That representative is removed precisely when \(S_\varepsilon(u)<a\). Write \(L(u)=\#\{\varepsilon:S_\varepsilon(u)<a\}\). Then \(W(u)=2^d-L(u)\).

**2. The triangle-free obstruction.** Suppose two distinct choices \(\varepsilon,\eta\) are removed. Let \(r\) be their Hamming distance. At every differing coordinate, their deficits add to \(1\); at agreeing coordinates, their deficits add to a nonnegative number. Consequently \(S_\varepsilon(u)+S_\eta(u)\ge r\). Since the left side is strictly below \(2a<2\), one must have \(r=1\). Thus all removed binary words would have to be pairwise adjacent in the hypercube graph. This graph has no triangles, so \(L(u)\le2\). This is a genuinely dimension-independent restriction, not a consequence of two-dimensional planar geometry.

**3. Exact double-loss volume.** Each hypercube edge joins two choices differing in exactly one coordinate, say the first. The shared \(d-1\) deficits are independent uniform variables on \([0,1]\), and we write their sum as \(s\). Both endpoints are removed exactly when \(u_1+s<a\) and \(1-u_1+s<a\), i.e. when \(0\le s<h\) and \(1-a+s<u_1<a-s\). For \(0\le s<h<1/2\), the sum of the shared deficits has density \(s^{d-2}/(d-2)!\). Hence an individual edge represents a set of volume
\[
\int_0^h(2h-2s)\frac{s^{d-2}}{(d-2)!}\,ds=\frac{2h^d}{d!}.
\]
When \(a\le1/2\), this value is zero. The \(d2^{d-1}\) distinct edge events are pairwise disjoint up to null sets, since three removed representatives are impossible. Therefore \(p_2=d2^{d-1}(2h^d/d!)=2^dh^d/(d-1)!\).

**4. The remaining masses and sharp support.** Each individual corner has deletion probability \(a^d/d!\), so \(\mathbb E L=2^da^d/d!\). Because \(L\in\{0,1,2\}\), this expectation is \(p_1+2p_2\), giving the displayed \(p_1\); normalization gives \(p_0\). For positive measure of \(L=0\), take \(u_i\) near \(1/2\) for every coordinate: the sum of every deficit is close to \(d/2>1>a\). For positive measure of \(L=1\), take every coordinate near zero, so only the all-small-deficit word is removed. A pair can be removed on an open set exactly when \(a>1/2\), by taking one coordinate near \(1/2\) and all others near zero. The probability \(p_2\) increases strictly with \(a\) above \(1/2\), and its supremum as \(a\uparrow1\) is \(2^d(1/2)^d/(d-1)!=1/(d-1)!\).

**5. Fourier identity.** The Fourier coefficients of \(W\) on the unit torus are exactly \(F_{d,a}(k)\): substitute \(x=u+n\) and use \(e^{-2\pi ik\cdot n}=1\) for integer \(k,n\). By Parseval and the preceding distribution,
\[
\sum_{k\ne0}|F_{d,a}(k)|^2=\int W(u)^2du-\left(\int W(u)du\right)^2=\operatorname{Var}(L).
\]
Now \(L^2=L+2\mathbf1_{\{L=2\}}\), whence \(\operatorname{Var}(L)=\mathbb EL+2p_2-(\mathbb EL)^2\). Substituting the exact expressions yields the boxed identity. Its only nonsmooth summand at \(a=1/2\) is \(2^{d+1}(a-1/2)_+^d/(d-1)!\); it is \(C^{d-1}\), with \(d\)-th derivative jump \(2^{d+1}d\). This establishes every assertion.

## Verification
A standalone finite mesh checker (`clipped_hypercube_check.py`) enumerates which of the \(2^d\) translates lose their corner for each sampled point of the unit torus. It checks the exact three-level support and approximates the predicted masses and Fourier-energy variance for dimensions \(2,3,4\), across five depths in each dimension. It also checks the known planar formula at one depth. All 15 mesh cases passed. This finite test is independent corroboration, not a substitute for the all-dimensional geometric and Parseval proof.

## Relationship to prior work
Lev and Liu, *Spectrality of polytopes and equidecomposability by translations* (first publicly posted 2019-02-03, arXiv:1902.00876; primary MSC 42B10), studies Fourier transforms of polytopes and necessary geometric conditions for spectrality. Its Theorems 1.1 and 1.2 and Section 4 on flag-measure Fourier asymptotics do not state the present lattice-covering multiplicity distribution or a closed Fourier-energy formula. Lev and Matolcsi, *The Fuglede conjecture for convex domains is true in all dimensions* (first posted 2019-04-28, arXiv:1904.12262), develops spectrality-to-weak-tiling implications but does not compute these specific integer-translate overlap distributions.

A previously recorded result on corner-clipped **planar squares** proves the special \(d=2\) formula and additionally classifies planar integer-frequency Fourier zeros. The present claim is expressly restricted to \(d\ge3\) and does not reclaim that planar finding. New content is the all-dimensional triangle-free overlap obstruction, exact \(d\)-dimensional volume distribution, factorial double-overlap suppression, and \(C^{d-1}\)-but-not-\(C^d\) Fourier energy onset. General Fourier-transform machinery for arbitrary polytopes, including Diaz, Le and Robins (arXiv:1602.08593), is acknowledged; the full earlier text was not available for a decisive comparison, so historical priority is qualified.

## Limitations
No individual integer Fourier coefficient, Fourier zero set, spectral-set property, basis of exponentials, or optimizing lattice is classified. In particular, the total nonconstant energy does not identify which coefficients vanish. This is an exact theorem for this one natural family of uniformly corner-truncated cubes; it is not an assertion of originality for Parseval's identity or for general polytopal Fourier transforms. Equivalently phrased older multicover formulas remain a historical-priority risk. The finite numerical checks verify only sampled points and dimensions, whereas the proof covers all stated dimensions and continuous clipping depths.

## References
1. N. Lev and B. Liu, *Spectrality of polytopes and equidecomposability by translations*, arXiv:1902.00876, first publicly posted 2019-02-03. https://arxiv.org/abs/1902.00876
2. N. Lev and M. Matolcsi, *The Fuglede conjecture for convex domains is true in all dimensions*, arXiv:1904.12262, first publicly posted 2019-04-28. https://arxiv.org/abs/1904.12262
3. R. Diaz, Q.-N. Le and S. Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593, first publicly posted 2016-02-27. https://arxiv.org/abs/1602.08593
