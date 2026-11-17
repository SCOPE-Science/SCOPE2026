# Exact Gaussian angle spectrum and collision condensation for friendship graphical zonotopes

## Finding
For every integer \(m\ge1\), let \(F_m\) be the friendship graph formed from \(m\) triangles with one common hub and otherwise disjoint vertices. Form its canonical Euclidean graphical zonotope
\[
Z_m=\sum_{\{i,j\}\in E(F_m)}[e_i,e_j]\subset\mathbb R^{2m+1},
\]
with the inherited Euclidean metric on the affine hyperplane of coordinate sum \(3m\). It has \(6^m\) vertices, corresponding to acyclic orientations of the triangles.

The complete multiset of normalized Gaussian vertex-normal-cone solid angles is as follows. Choose nonnegative integers \(a,b,c\) with \(a+b+c=m\). At precisely
\[
M_m(a,b,c)=2^m\frac{m!}{a!b!c!}
\]
vertices (counting types separately even when their angles coincide), the normalized solid angle equals
\[
\alpha_m(a,b,c)=\frac{(2a+c)!(2b+c)!}{2^{a+b}(2m+1)!}.
\]
Here \(a\) counts triangles whose two leaves are below the hub, \(b\) counts triangles whose two leaves are above it, and \(c\) counts triangles with the hub between its leaves in the objective-coordinate order.

For two independent isotropic Gaussian objective directions, let \(C_m\) be the probability that they expose the same vertex. Then
\[
C_m=\sum_{a+b+c=m}M_m(a,b,c)\alpha_m(a,b,c)^2
=\int_0^1\!\int_0^1Q(u,v)^m\,du\,dv,
\]
where
\[
Q(u,v)=\frac{u^2v^2+(1-u)^2(1-v)^2}{2}+2u(1-u)v(1-v).
\]
Its sharp asymptotic is
\[
\boxed{\lim_{m\to\infty}2^{m+1}m^2C_m=1.}
\]
Thus the angular collision probability exceeds its uniform-vertex benchmark \(6^{-m}\) by a factor asymptotic to \(3^m/(2m^2)\). In addition, conditional on a collision, the two hub quantiles concentrate in equal proportions near \((0,0)\) and \((1,1)\); around either corner their inward distances, multiplied by \(m\), tend jointly to independent exponential variables of rate \(2\).

## Assumptions and scope
The graph is simple, has vertex set \(\{0,1,\ldots,2m\}\), hub \(0\), and triangles \(\{0,2j-1,2j\}\) for \(1\le j\le m\). The segment \([e_i,e_j]\) is the usual closed segment between standard coordinate vectors, with no extra edge weights. A normal-cone angle is the probability that a standard Gaussian vector in the ambient space, equivalently its orthogonal projection into the affine direction space, exposes that vertex. The center-of-mass direction is irrelevant because all vertices lie in the same affine hyperplane. Zero-probability tied objective values may be discarded. The theorem is exact for all finite \(m\ge1\); its asymptotic and conditional limits refer to \(m\to\infty\).

## Proof
The support function of \(Z_m\) is a sum of the support functions of its edge segments. At a generic objective \(g\), each segment chooses the endpoint with the larger objective coordinate. Thus vertex normal-cone interiors are exactly the regions of the graphical hyperplane arrangement, indexed by acyclic orientations. An orientation of this graph is acyclic precisely when each of its \(m\) triangular restrictions is a transitive tournament, because distinct triangles intersect only at the hub. Each restriction has six possible orders, giving \(6^m\) orientations.

Let \(G_0,G_1,\ldots,G_{2m}\) be independent standard normals. Apply their common continuous distribution function \(\Phi\) to obtain independent uniforms. Conditionally on the hub quantile \(U=\Phi(G_0)=u\), two designated leaves are both below the hub in a particular order with probability \(u^2/2\); both above it in a particular order with probability \((1-u)^2/2\); and straddle it in a particular orientation with probability \(u(1-u)\). All distinct triangle blocks are conditionally independent. An orientation with counts \((a,b,c)\) therefore has angle
\[
\int_0^1\left(\frac{u^2}{2}\right)^a\left(\frac{(1-u)^2}{2}\right)^b\bigl(u(1-u)\bigr)^cdu
=\frac{(2a+c)!(2b+c)!}{2^{a+b}(2m+1)!},
\]
using the integer beta integral. There are \(m!/(a!b!c!)\) allocations of triangle types and two specific local orders within each type, proving the stated multiplicity. These multiplicities total \(6^m\); the solid angles sum to one because every generic direction has exactly one exposed vertex.

For two independent Gaussian directions, their hub quantiles \(U,V\) are independent uniforms. Conditional on \((U,V)=(u,v)\), a single triangle has matching orientation with probability equal to the sum of products of its six local probabilities in the two directions, namely \(Q(u,v)\). Different triangle blocks again match independently, so integrating \(Q(u,v)^m\) proves the exact collision integral. The finite sum is the same probability by partitioning on the common exposed vertex.

Write \(r(u)=u(1-u)\) and let \(p(u)\) be the six-component vector of local orientation probabilities. Its squared norm is
\[
\|p(u)\|_2^2=\frac12-2r(u)+3r(u)^2\le\frac12,
\]
with equality only for \(u\in\{0,1\}\). Since \(Q(u,v)=p(u)\cdot p(v)\), Cauchy--Schwarz gives \(Q(u,v)\le1/2\). Equality is possible only when the two vectors coincide at the same endpoint, i.e. only at \((u,v)=(0,0)\) and \((1,1)\). At either corner, in inward local coordinates \(s,t\ge0\),
\[
Q=\frac12-s-t+O((s+t)^2).
\]
On compact sets away from these two corners the strict inequality yields exponentially smaller contributions. Near either corner, substitute \(s=x/m,t=y/m\). Then
\[
\bigl(2Q(x/m,y/m)\bigr)^m\longrightarrow e^{-2(x+y)}.
\]
For sufficiently small fixed corner neighborhoods, a uniform bound of the form \(2Q\le e^{-\kappa(s+t)}\), for some \(\kappa>0\), provides an integrable dominator after rescaling. Dominated convergence makes each corner contribute
\[
\frac{2^{-m}}{m^2}\int_0^\infty\!\int_0^\infty e^{-2(x+y)}\,dx\,dy
=\frac{2^{-m}}{4m^2}(1+o(1)).
\]
There are two equal corners. This proves \(C_m\sim2^{-m}/(2m^2)\). The same localized integral, with bounded continuous test functions of the scaled inward hub coordinates, proves the stated equal-mixture and independent rate-two exponential conditional limit.

## Verification
The standalone `check_friendship.py` has no third-party dependencies and uses exact Python rational arithmetic. Run `python3 check_friendship.py`. It enumerates all \((2m+1)!\) permutations for each \(1\le m\le4\) independently of the beta-integral derivation, constructs the corresponding triangle-orientation keys, and verifies every individual cone count against the theorem. It then computes the collision probability a second way by summing squared empirical cone frequencies and compares that rational number to the factorial-sum formula. It reports respectively \(1/6\), \(7/200\), \(167/19600\), and \(23/9800\) for \(m=1,2,3,4\), with \(\sum M_m\alpha_m=1\). The finite enumeration tests, but does not substitute for, the all-dimensional proof and asymptotic Laplace argument.

## Relationship to prior work
Padrol, Pilaud and Poullot (2021 preprint; journal article 2023) develop the graphical-zonotope normal fan and deformation cones; in particular, their normal-cone/acyclic-orientation correspondence is foundational here. Iriarte (2014 preprint) proves the general correspondence between a graphical-arrangement region's normalized spherical measure and the linear-extension count of its orientation poset, and studies orientations with maximal such counts. These general correspondences imply that individual angles can in principle be counted by generic linear-extension enumeration. The current statement supplies the explicit all-parameter windmill angle multiset, a finite exact collision law, and the sharp rare-collision asymptotic and conditional localization. These additional statements were not found in the inspected pertinent source text. Known analogous angular collision phenomena for stars, double stars and complete-bipartite graphical zonotopes involve different graphs and are not asserted here to be new in their own settings.

## Limitations
This is a normalized Gaussian normal-cone angle statement for the specified canonical Euclidean graphical zonotope, not a general formula for arbitrary edge weights, nonisotropic objectives or windmills with larger clique blocks. The theorem gives the aggregate collision probability and its conditional extreme-hub law; it does not claim higher-order collision distributions. Priority remains provisional because an unindexed equivalent specific windmill classification could exist.

## References
- A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, first posted 2021-11-24, arXiv:2111.12422, https://arxiv.org/abs/2111.12422; journal DOI: https://doi.org/10.1007/s00454-023-00586-x.
- B. Iriarte, *Graph Orientations and Linear Extensions*, first posted 2014-05-19, arXiv:1405.4880, https://arxiv.org/abs/1405.4880, especially Proposition 5.2 and Theorem 5.3.
- K. Stinson, D. Gleich, P. Constantine, *A randomized algorithm for enumerating zonotope vertices*, arXiv:1602.06620, https://arxiv.org/abs/1602.06620 (probabilistic motivation for sampling vertex normal cones).
