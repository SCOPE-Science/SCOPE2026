# An area-weighted facet-rank law and logarithmic boundary-tail anomaly for parking-function polytopes

## Finding
Fix \(t\ge0\). The Euclidean surface-area distribution across the facets of a generalized parking-function polytope converges to a universal *discrete* distribution: its mass on the \(n\) coordinate-minimum facets tends to
\[
\beta=\frac{1}{1+\alpha}=0.6178166125895\ldots,
\qquad
\alpha=\sum_{k\ge1}\frac{e^{-k}k^{k-3/2}}{k!}=0.6186032871609\ldots.
\]
The mass on upper facets indexed by \(k\) coordinates tends to
\[
 p_k=\beta\frac{e^{-k}k^{k-3/2}}{k!},\qquad k\ge1.
\]
Thus \(p_k\sim\beta/(\sqrt{2\pi}\,k^2)\), the limiting facet-rank distribution has infinite mean, and the prelimit mean satisfies
\[
\mathbb E K_n=\frac{\beta}{\sqrt{2\pi}}\log n+O_t(1).
\]
These limits are independent of the fixed parking parameter \(t\). In particular, only \(n\) of exponentially many facets retain a strictly positive fraction of all Euclidean boundary area.

## Assumptions and scope
For \(n\ge2\), let \(P_{n,t}\subset\mathbb R^n\) be the convex hull of all permutations of the vectors
\[
(\underbrace{0,\dots,0}_{j},\,t+j,\,t+j+1,\dots,t+n-1),\qquad 0\le j\le n.
\]
For \(t=0\), duplicate vertex descriptions are merged. This is the translate and \(1/b\) homothety of the generalized parking-function polytope with positive integer data \(a,b\) and \(t=(a-1)/b\). The convex-geometric definition extends the family to every fixed real \(t\ge0\). Write \(V_m(t)=\operatorname{vol}_m(P_{m,t})\), with \(V_0(t)=1\), \(V_1(t)=t\); the lower-dimensional \(m=1\) convention is the parameter-compatible interval length used by the facet decomposition. For \(n\ge2\), the body has positive volume, including when \(t=0\).

Its facets have two categories. Exactly \(n\) *lower facets* lie at \(x_i=0\). Upper facets are specified by \(\sum_{i\in I}x_i\le |I|t+|I|(2n-|I|-1)/2\), indexed by nonempty \(I\subseteq[n]\), with \(|I|=k\). For \(t=0\), the formal \(k=n-1\) upper sets have zero \((n-1)\)-area and are not facets; zero contributions are harmless. Define the random variable \(K_n\) by sampling a boundary point according to normalized Euclidean area, then assigning \(K_n=0\) on a lower facet and \(K_n=k\) on an upper \(k\)-subset facet. Ridges have measure zero. The dimension and the rank both grow, while \(t\) stays fixed; no uniform-in-growing-\(t\) conclusion is claimed.

## Proof
**Exact boundary decomposition.** The inequality and product-face decompositions follow from the elementary vertex description and the facet classification in Hanada–Lentfer–Vindas-Meléndez. On \(x_i=0\), the remaining coordinates have precisely the vertex/inequality description of \(P_{n-1,t+1}\), hence total lower area is
\[
L_n(t)=nV_{n-1}(t+1).
\]
On the upper facet indexed by a fixed \(k\)-set, the selected coordinates form the regular permutahedron on \((t+n-k,\ldots,t+n-1)\); the other coordinates independently form \(P_{n-k,t}\). These factors lie in orthogonal coordinate subspaces. By the weighted spanning-tree formula for the regular permutahedron, its intrinsic \((k-1)\)-volume is \(A_k=\sqrt{k}\,k^{k-2}=k^{k-3/2}\) (for \(k=1\), \(A_1=1\)). The upper rank-\(k\) total area therefore is
\[
U_{n,k}(t)=\binom nk A_k V_{n-k}(t).
\]
Consequently, for \(n\ge2\),
\[
S_n(t)=L_n(t)+\sum_{k=1}^nU_{n,k}(t),
\quad
\Pr(K_n=0)=\frac{L_n(t)}{S_n(t)},
\quad
\Pr(K_n=k)=\frac{U_{n,k}(t)}{S_n(t)}.
\]
The facet product computation can also be checked directly from the defining inequalities by restricting to equality, including the potentially degenerate \(t=0\) case.

**Generating functions.** Put \(f_m(t)=V_m(t)/m!\), \(F_t(z)=\sum_{m\ge0}f_m(t)z^m\), and
\[
g(z)=\sum_{j\ge1}\frac{j^{j-1}}{j!}z^j,
\qquad g(z)=ze^{g(z)},
\qquad H(z)=\sum_{k\ge1}\frac{A_k}{k!}z^k.
\]
The known parking-volume recursion (equivalently, the exponential generating function in the cited generalized-parking-polytope paper) gives
\[
F_t(z)=\frac{\exp((t-1/2)g(z))}{\sqrt{1-g(z)}}.
\]
For clarity, in that paper the volume generating function is an exponential of \(\frac12\int z(g'(z))^2\,dz + t g(z)\). Since \(z(g')^2\,dz=g(1-g)^{-1}\,dg\), the integral is \(-g-\log(1-g)\); this proves the displayed form with \(F_t(0)=1\). The identity \(zF_{t+1}(z)=g(z)F_t(z)\) then gives, coefficient by coefficient,
\[
\frac{L_n(t)}{n!}=[z^n]g(z)F_t(z),
\quad
\frac{U_{n,k}(t)}{n!}=\frac{A_k}{k!}[z^{n-k}]F_t(z),
\quad
\frac{S_n(t)}{n!}=[z^n](g(z)+H(z))F_t(z).
\]
The last identity includes the natural boundary convention in dimension one but is used here only for \(n\ge2\).

**Coefficient and convolution estimates.** The tree-function singularity at \(\rho=e^{-1}\) is
\[
g(z)=1-\sqrt{2(1-z/\rho)}+O(1-z/\rho).
\]
For fixed \(t\ge0\), standard square-root transfer therefore yields
\[
f_m(t)=C_t\rho^{-m}m^{-3/4}(1+O_t(m^{-1/2})),
\quad
C_t=\frac{\exp(t-1/2)}{2^{1/4}\Gamma(1/4)},\qquad m\to\infty.
\]
For \(m=0\), use the exact value \(f_0=1\). The coefficient weights obey, by Stirling,
\[
 \frac{A_k\rho^k}{k!}=\frac{1+O(k^{-1})}{\sqrt{2\pi}\,k^2},\qquad
 \frac{k^{k-1}\rho^k}{k!}=\frac{1+O(k^{-1})}{\sqrt{2\pi}\,k^{3/2}}.
\]
Both kernels are summable at \(\rho\), with \(H(\rho)=\alpha\) and \(g(\rho)=1\). For any fixed \(k\), \(f_{n-k}/f_n\to\rho^k\). To justify passage to the *whole* convolution, split at \(k=n/2\). For \(k\le n/2\), the asymptotic coefficient bounds yield \(f_{n-k}/f_n\le C_t\rho^k\). For \(k>n/2\), with \(m=n-k\), \(f_{n-k}/f_n\le C_t\rho^k n^{3/4}(m+1)^{-3/4}\). Consequently the upper-kernel tail has relative size
\[
O_t\!\left(n^{3/4}\sum_{m<n/2}\frac{(m+1)^{-3/4}}{(n-m)^2}\right)=O_t(n^{-1}),
\]
and the tree-kernel tail has relative size \(O_t(n^{-1/2})\). Dominated convergence gives
\[
\frac{L_n(t)}{n!f_n(t)}\to 1,\quad
\frac{\sum_kU_{n,k}(t)}{n!f_n(t)}\to\alpha,\quad
\frac{S_n(t)}{n!f_n(t)}\to1+\alpha.
\]
The asserted complete limiting distribution follows; the sum of its masses equals \(\beta(1+\alpha)=1\).

**Logarithmic mean.** Exactly,
\[
\mathbb E K_n=\frac{n!}{S_n(t)}\sum_{k=1}^n k\frac{A_k}{k!}f_{n-k}(t).
\]
For \(k\le n/2\), the same coefficient estimate and Stirling imply
\[
 k\frac{A_k}{k!}\frac{f_{n-k}(t)}{f_n(t)}
 =\frac{1}{\sqrt{2\pi}\,k}(1-k/n)^{-3/4}
 +O_t(k^{-2}+n^{-1/2}k^{-1}).
\]
The sum of the leading term is \((2\pi)^{-1/2}\log n+O(1)\): the correction from replacing \((1-k/n)^{-3/4}\) by one costs only \(O(1)\). The terms \(k>n/2\) contribute \(O_t(1)\), since \(k A_k/k!=O(\rho^{-k}/k)\) and the same \(m=n-k\) bound applies. As the denominator is \((1+\alpha+o(1))n!f_n\), the logarithmic coefficient is \(\beta/\sqrt{2\pi}\). In fact, the subleading denominator error is \(O_t(n^{-1/2})\), obtained by the preceding explicit split and the summable-kernel comparison, so it does not spoil the stated additive \(O_t(1)\) remainder. This proves the claim.

## Verification
The companion `verify_surface_rank.py` reconstructs both sides of the exact facet formula independently: it generates all vertices for \(n=2,3,4\), triangulates the convex hull, computes the Euclidean \((n-1)\)-area of each triangulation simplex by its Gram determinant, and compares against the formula for \(t\in\{0,1/2,1,2\}\). It checks the volume recursion, the limit normalization, and the Stirling tail numerically. All 12 convex-hull comparisons passed. These finite checks are evidence of implementation accuracy, not a substitute for the infinite-dimensional proof above. Python 3 with NumPy and SciPy is sufficient to reproduce them.

## Relationship to prior work
Amanbayeva and Wang introduced the classical parking-function convex hull and enumerated its combinatorial data and volume. Hanada, Lentfer and Vindas-Meléndez generalized it to \((a,b,\ldots,b)\), explicitly identified its facet product decomposition and Euclidean-volume generating function; those ingredients are **not claimed new**. Later combinatorial studies classify further face structure, not this area-weighted facet-rank distribution. Earlier metric investigations determined inballs, dihedral-angle spectra, Gaussian width fluctuations, and vertex covariance of related parking-function bodies. Those statements do not directly imply the exact surface-area generating function together with its summable rank tail and logarithmic mean. A logarithmic facet phenomenon in tree graphical zonotopes shares probabilistic vocabulary but has different Euclidean bodies and observables.

## Limitations
The theorem requires fixed \(t\) as \(n\to\infty\) and does not claim uniformity when \(t\) grows with \(n\). Its rank law weights geometric boundary *area*, not uniformly counted facets or randomly exposed facets. Numerical constants are approximations to absolutely convergent series. The source comparison does not establish an exhaustive priority search: unindexed or unpublished equivalents could exist. No independent mathematical audit has been performed.

## References
- A. Amanbayeva and D. Wang, *The Convex Hull of Parking Functions of Length n* (first public version 2021-04-17), https://arxiv.org/abs/2104.08454.
- M. Hanada, J. Lentfer, and A. R. Vindas-Meléndez, *Generalized parking function polytopes* (first public version 2022-12-13), https://arxiv.org/abs/2212.06885; *Annals of Combinatorics* (online 2023), https://doi.org/10.1007/s00026-023-00671-1.
- *Combinatorics of Generalized Parking-Function Polytopes* (2025), https://doi.org/10.1007/s00454-025-00770-1.
