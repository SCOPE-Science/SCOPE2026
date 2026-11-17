# Exact edge-gluing volumes for triangular-book graph elliptopes

## Finding

Let \(B_n\), for every integer \(n\ge1\), be the graph with two adjacent hub vertices \(a,b\) and \(n\) other vertices \(u_1,\ldots,u_n\), each adjacent to both hubs and to no other vertex. Thus \(B_n\) consists of \(n\) triangles sharing the edge \(ab\), and it has \(2n+1\) edges. Define \(C_n\) as the \((2n+1)\)-dimensional Euclidean coordinate volume of its cut polytope and \(E_n\) as the volume of its projected graph elliptope, both in the same \(0/1\) edge coordinates.

The exact volumes are
\[
\boxed{C_n=2^n\operatorname B(n+1,n+1)=\frac{2^n(n!)^2}{(2n+1)!},}
\]
\[
\boxed{E_n=\left(\frac{\pi}{2}\right)^n
\operatorname B\!\left(\frac n2+1,\frac n2+1\right).}
\]
The first formula was already known for suspensions of stars; the second is the formula established here. Their volume ratio is
\[
\boxed{\frac{E_n}{C_n}
=\left(\frac{\pi}{4}\right)^n
\frac{\operatorname B(n/2+1,n/2+1)}{\operatorname B(n+1,n+1)}
=\sqrt2\left(\frac\pi2\right)^n
\left(1-\frac{3}{8n}+O(n^{-2})\right).}
\]
Consequently, the ratio has exact exponential growth base \(\pi/2\), despite the fact that all the constituent pages are triangles. For instance, at \(n=1\) the familiar triangle ratio is \(3\pi^2/16\); at \(n=2\), it is \(5\pi^2/16\). By contrast, vertex-gluing rather than edge-gluing \(n\) triangles produces the product ratio \((3\pi^2/16)^n\). These two gluing operations therefore have different exponential volume-gap bases.

## Assumptions and scope

For a finite simple graph \(G=(V,F)\), the cut polytope \(\operatorname{Cut}(G)\subset\mathbb R^F\) is the convex hull of the vectors \((\mathbf 1_{\{\sigma_v\ne\sigma_w\}})_{vw\in F}\) over all assignments \(\sigma_v\in\{-1,1\}\). The graph elliptope in these coordinates is
\[
\mathcal I(G)=\left\{\left(\frac{1-\langle z_v,z_w\rangle}{2}\right)_{vw\in F}:
\|z_v\|=1\ \text{for all }v\in V,\ z_v\in\mathbb R^N\text{ for some finite }N\right\}.
\]
The volumes in the theorem are ordinary Lebesgue volumes in the specified edge coordinates, not intrinsically renormalized volumes and not volumes in full symmetric-matrix space. Both bodies are full-dimensional for every \(n\ge1\). The beta function is \(\operatorname B(s,t)=\int_0^1 u^{s-1}(1-u)^{t-1}\,du\). All asymptotics hold as the integer \(n\to\infty\).

## Proof

**1. Exact fiber description for the elliptope.** Work first in correlation coordinates. Denote the hub correlation by \(t=\langle z_a,z_b\rangle\) and the two correlations involving page vertex \(u_i\) by \(x_i=\langle z_a,z_{u_i}\rangle\) and \(y_i=\langle z_b,z_{u_i}\rangle\). For \(-1<t<1\), the local Gram matrix of the triangle \((a,b,u_i)\) is positive semidefinite exactly when
\[
x_i^2-2tx_i y_i+y_i^2\le1-t^2.
\]
This is an ellipse of area \(\pi\sqrt{1-t^2}\). Importantly, all these local conditions are **jointly sufficient**, not merely necessary: take \(z_a=e_0\), \(z_b=te_0+\sqrt{1-t^2}e_1\), and for each page put
\[
z_{u_i}=x_i e_0+\frac{y_i-tx_i}{\sqrt{1-t^2}}e_1+\rho_i e_{i+1},\qquad
\rho_i^2=1-x_i^2-\frac{(y_i-tx_i)^2}{1-t^2}\ge0.
\]
The orthogonal residual directions make every vertex vector a unit vector and realize all prescribed edge correlations simultaneously. Hence the full \(2n\)-dimensional fiber at \(t\) is exactly the Cartesian product of \(n\) identical ellipses. The exceptional sections \(t=\pm1\) have measure zero.

**2. Exact fiber description for cuts.** A mixture of binary cuts is a distribution of spins \((A,B,U_1,\ldots,U_n)\in\{-1,1\}^{n+2}\). For fixed hub correlation \(t=\mathbb E(AB)\), each page triple must satisfy
\[
|x_i+y_i|\le1+t,\qquad |x_i-y_i|\le1-t,
\]
where \(x_i=\mathbb E(AU_i)\), \(y_i=\mathbb E(BU_i)\). Conversely, given any page pairs obeying these inequalities for the same \(-1<t<1\), prescribe the common hub-pair law
\[
\Pr(A=a,B=b)=\frac{1+tab}{4},\qquad a,b\in\{-1,1\},
\]
and, conditionally on \((A=a,B=b)\), choose the \(U_i\) independently with conditional means
\[
\mathbb E(U_i\mid A=a,B=b)=\frac{x_i a+y_i b}{1+tab}.
\]
The two page inequalities are exactly what makes the last conditional means lie in \([-1,1]\). This construction realizes every prescribed edge correlation, proving that the global cut fiber is the product of the local parallelograms. A change of variables \((x_i,y_i)\mapsto(x_i+y_i,x_i-y_i)\) shows that each parallelogram has correlation-coordinate area \(2(1-t^2)\).

**3. Volume integration in common coordinates.** Convert every correlation \(s\) to its corresponding cut coordinate \(h=(1-s)/2\). Write the spine coordinate as \(h=(1-t)/2\), so \(0<h<1\). Each page's pairwise Jacobian has absolute determinant \(1/4\). Thus the elliptope fiber has area
\[
\frac\pi4\sqrt{1-t^2}=\frac\pi2\sqrt{h(1-h)},
\]
whereas the cut fiber has area
\[
\frac12(1-t^2)=2h(1-h).
\]
Fubini's theorem, with the spine coordinate integrated in the same \([0,1]\) units, gives
\[
E_n=\int_0^1\left[\frac\pi2\sqrt{h(1-h)}\right]^n\,dh,
\qquad
C_n=\int_0^1[2h(1-h)]^n\,dh.
\]
These are exactly the two stated beta integrals; for the cut integral, factorial evaluation yields \(2^n(n!)^2/(2n+1)!\).

**4. Sharp asymptotic and vertex-gluing contrast.** Simplifying with the gamma duplication identity yields
\[
\frac{E_n}{C_n}
=\left(\frac\pi2\right)^n
\frac{\Gamma(n/2+1)\Gamma(n+3/2)}
{\Gamma(n/2+3/2)\Gamma(n+1)}.
\]
For fixed \(a,b\) as \(z\to\infty\), the standard expansion
\[
\frac{\Gamma(z+a)}{\Gamma(z+b)}
=z^{a-b}\left[1+\frac{(a-b)(a+b-1)}{2z}+O(z^{-2})\right]
\]
shows that the final gamma quotient equals \(\sqrt2(1-3/(8n)+O(n^{-2}))\). Hence the exponential base and first correction are exact. If instead \(n\) triangle blocks meet only at one common vertex, their elliptopes and cut polytopes factor as products over disjoint edge sets: their ratio is \((E_1/C_1)^n=(3\pi^2/16)^n\), which differs from the edge-glued result.

## Verification

The stand-alone script `verify.py`, run with Python 3, `mpmath`, `numpy` and `scipy`, passed **2,216 deterministic assertions**. It evaluates both beta integrals independently by high-precision quadrature for \(1\le n\le23\), compares exact cut volumes with independent convex-hull enumeration for \(1\le n\le4\), constructs numerical positive-semidefinite Gram completions and binary-spin joint distributions from local fibers, and checks the first asymptotic correction at four larger dimensions. The tests are finite checks of the written formulas and boundary conventions; the all-dimensional conclusion rests on the preceding proof.

The first values are
\[
\begin{array}{c|ccc}
n&C_n&E_n&E_n/C_n\\\hline
1&1/3&\pi^2/16&3\pi^2/16\\
2&2/15&\pi^2/24&5\pi^2/16\\
3&2/35&3\pi^4/1024&105\pi^4/2048
\end{array}
\]

## Relationship to prior work

Avis, Devroye and Deza (2026) study cut and elliptope volumes in the same unit-cube edge coordinates and obtain exact formulas for cycles, where the elliptope-to-cut volume ratio converges to one. Their Table 2 records the **already known** cut volume for the suspension of an \(n\)-edge star, which is precisely the triangular book \(B_n\), and their Proposition 3.7 establishes a product law when graphs share at most one vertex. The present theorem treats sharing a full edge, for which the latter product law does not apply. Their Theorem 3.8 supplies a general coordinatewise cosine parameterization for graphs without a \(K_4\) minor; it is consistent with but does not state the resulting book-family elliptope-volume integral and exponential gap.

Lee and Skipper (2017/2018) derived the star Boolean-quadric volume and its cut-polytope transfer; their \(\mathscr Q(G)\) is a **linear** relaxation of a Boolean-quadric polytope, not the positive-semidefinite graph elliptope. Lee (2026) gives a series-parallel cut/Boolean-quadric volume algorithm, again distinct from a closed PSD elliptope volume. In addition, the previously derived \(K_{2,n}\) graph-elliptope volume treats the graph *without* the common hub edge and cannot alone determine the conditional slice and volume with that edge present. No claim is made that beta integrals, Gram completion, gamma asymptotics, or the cut-volume formula are new in isolation.

## Limitations

The formula addresses only the triangular book family and coordinate Lebesgue volume. It does not establish an exact PSD elliptope volume for arbitrary chordal or series-parallel graphs. The case \(n=1\) is an already-known triangle example, not a newly discovered special case. Published-source comparisons do not establish absolute historical priority; earlier equivalent identities under different cut/Boolean or PSD parameterizations may exist. The finite numerical checks do not independently certify the infinite statements. Independent mathematical validation has not been performed.

## References

1. D. Avis, L. Devroye, A. Deza, *On the volumes of the elliptope, metric polytope, and cut polytope*, arXiv:2604.16735 (first public version, 17 April 2026), https://arxiv.org/abs/2604.16735. Especially §3, Table 2, Proposition 3.7, Theorems 3.8–3.9.
2. J. Lee, D. Skipper, *Volume computation for sparse boolean quadric relaxations*, arXiv:1703.02444 (first public version, 4 March 2017), https://arxiv.org/abs/1703.02444. Especially §3 on stars and the covariance cut transfer.
3. J. Lee, *Exact volume computation for Boolean quadric polytopes of series-parallel graphs*, arXiv:2610.00734 (first public version, 30 September 2026), https://arxiv.org/abs/2610.00734. Series-parallel linear/integer volume algorithms, not PSD elliptope volumes.
