# A one-dimensional compact obstruction to density of disconnected spectral classes

## Finding

A one-dimensional compact metrizable space can have continuum many connected components, yet its commutative continuous-function algebra has a nonempty open set of elements with connected spectrum. Explicitly, let

\[
K=[-1,1]\cup i[-1,1]\subset\mathbb C,\qquad
Y=\text{the middle-thirds Cantor set},\qquad
X=K\times Y,\qquad A=C(X,\mathbb C).
\]

Set \(f_0(z,y)=z\). For every \(g\in A\),

\[
\|g-f_0\|_\infty<\frac12\quad\Longrightarrow\quad
\sigma_A(g)=g(X)\text{ is connected}.
\]

For each positive integer \(n\), write \(\mathcal C_n(A)\) for the functions whose spectra have at least \(n\) connected components, and let \(\mathcal C_\infty(A)=\bigcap_{n\ge1}\mathcal C_n(A)\). Then \(\mathcal C_\infty(A)\ne\varnothing\) and the spectral depth \(d_\sigma(A)=\infty\), while every \(\mathcal C_n(A)\) with \(n\ge2\) is non-dense in \(A\). The zero-dimensional density guarantee from [1, Proposition 4.6] therefore cannot be extended universally even to covering dimension one.

## Assumptions and scope

The compact planar cross \(K\) consists of two closed unit segments meeting at their common midpoint. The set \(Y\subset[0,1]\) is the standard perfect, totally disconnected Cantor set, and \(X\) has the product topology. Every function belongs to the full unital complex \(C^*\)-algebra \(A\), with no analyticity or smoothness restriction. All norms are uniform norms. The assertion about nearby spectra uses the strict inequality \(\|g-f_0\|_\infty<1/2\); no optimality of this particular radius is asserted.

A compact metric space has covering dimension at most \(1\) when each finite open cover has an open refinement of order at most \(2\). Since \(K\) is a finite one-dimensional graph and \(Y\) is zero-dimensional, the standard product inequality for covering dimension gives \(\dim(X)\le\dim(K)+\dim(Y)=1\). The closed subspace \(K\times\{y\}\subset X\) contains an interval for any \(y\in Y\), so \(\dim(X)\ge1\); hence \(\dim(X)=1\). The connected components of \(X\) are exactly the fibers \(K\times\{y\}\), because each fiber is connected and any connected subset has singleton projection onto totally disconnected \(Y\).

## Proof

**Pairwise crossing lemma.** Fix two (not necessarily distinct) points \(y,y'\in Y\), and suppose \(\delta=\|g-f_0\|_\infty<1/2\). Define two paths

\[
H(t)=g(t,y)=t+a(t),\qquad
V(s)=g(is,y')=is+b(s),\qquad -1\le t,s\le1.
\]

Here \(a,b\) are continuous and \(|a(t)|\le\delta\), \(|b(s)|\le\delta\). On the compact square \(Q=[-1,1]^2\) consider the continuous map

\[
F(t,s)=\bigl(\operatorname{Re}(b(s)-a(t)),\ \operatorname{Im}(a(t)-b(s))\bigr).
\]

Both coordinates of \(F\) have absolute value at most \(2\delta<1\), so \(F(Q)\subseteq Q\). By Brouwer's fixed-point theorem there are \((t_*,s_*)\in Q\) with \(F(t_*,s_*)=(t_*,s_*)\). The two coordinate equalities are exactly

\[
t_*-is_*=b(s_*)-a(t_*),\quad\text{hence}\quad H(t_*)=V(s_*).
\]

Thus the horizontal arm of the image of one fiber intersects the vertical arm of the image of every other fiber. In particular, the sets

\[
S_y=g(K\times\{y\})\qquad (y\in Y)
\]

are all connected, and \(S_y\cap S_{y'}\ne\varnothing\) for every pair \(y,y'\). Their union \(g(X)=\bigcup_{y\in Y}S_y\) is connected: if it admitted a separation into two nonempty relatively open pieces, each connected \(S_y\) would lie entirely in one piece, while a pair of pieces would require two disjoint fiber images, contradicting pairwise intersection. Since \(X\) is compact, this union is also compact.

**Spectrum identification.** For each \(g\in C(X,\mathbb C)\), a scalar \(\lambda\) lies outside \(g(X)\) precisely when \(1/(\lambda-g)\) is a continuous inverse of \(\lambda1-g\); if \(\lambda=g(x)\) at some \(x\), no inverse exists. Consequently \(\sigma_A(g)=g(X)\). The preceding crossing argument proves the claimed connected-spectrum ball.

**Depth and non-density.** The continuous function \(h(z,y)=y\) has \(\sigma_A(h)=Y\), whose connected components are its uncountably many individual points. Therefore \(h\in\mathcal C_\infty(A)\), and every finite spectral class is nonempty. But the nonempty open ball \(\{g:\|g-f_0\|_\infty<1/2\}\) is disjoint from \(\mathcal C_2(A)\), hence from every \(\mathcal C_n(A)\) for \(n\ge2\). This proves non-density. Finally, [1, Proposition 4.6] proves that every spectral class is dense for an infinite totally disconnected compact Hausdorff space, which includes every infinite zero-dimensional compact metric space. Since \(X\) is one-dimensional, the universal dimension bound is sharp.

## Verification

The key inequality is \(\|F(t,s)\|_{\ell_\infty(\mathbb R^2)}\le2\delta<1\), which establishes the required self-map condition on the *entire* square before applying Brouwer's theorem. The fixed-point equations recover intersection of the two actual paths even for different fibers. Neither an enumeration of fibers nor a limit passage is needed. The dimension argument uses standard compact-metric covering dimension facts. The proof is analytic and topological; no finite computation or experimental certificate is used or needed.

## Relationship to prior work

Bračič and Kandić [1] introduce the spectral classes and depth, prove the density theorem for totally disconnected compact spaces (Proposition 4.6), and exhibit non-density for an algebra of functions on infinitely many two-dimensional disks (Example 4.9), by proving a common disk lies in all nearby fiber images. The present example differs in three linked aspects: its base space is compact; its connected fibers are one-dimensional crosses with no interior in the plane; and the crossing principle proves pairwise overlap of *different* fiber images, without any common planar disk. The topological crossing principle and Brouwer fixed point are classical and are not themselves claimed as new. The companion paper [2] studies infinite/cardinal spectral depth, and revisits the disk construction; its stated results do not give this dimension-one stability example. The new conclusion is a sharp dimensional boundary for the density phenomenon, not a new general fixed-point theorem.

## Limitations

No classification of all compact metric spaces for which disconnected spectral classes are dense is established. The radius \(1/2\) is a proved uniform lower bound for the stable connected-spectrum neighborhood and is not asserted to be optimal. This theorem concerns full commutative complex continuous-function algebras, not arbitrary function subalgebras or noncommutative operator algebras. The dimension-zero statement is a universal sufficiency result, not a converse for individual one-dimensional spaces.

## References

[1] J. Bračič and M. Kandić, *On operators with many spectral components*, arXiv:2611.12208v1, first public version 9 November 2026, especially Propositions 4.5–4.6 and Example 4.9. https://arxiv.org/abs/2611.12208

[2] J. Bračič and M. Kandić, *On operators with infinitely many spectral components*, arXiv:2611.14394v1, first public version 10 November 2026, particularly Sections 3 and 6. https://arxiv.org/abs/2611.14394

[3] Brouwer's fixed-point theorem and the covering-dimension product inequality for compact metric spaces, used only in their standard classical forms.
