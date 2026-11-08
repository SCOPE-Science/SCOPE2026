# Sharp full-silhouette probability and optimal height for regular polygonal pyramids

## Finding
Let \(n\ge5\) be an integer. Let \(P_{n,h}\subset\mathbb R^3\) be the right pyramid whose base is the regular \(n\)-gon of circumradius one in the horizontal plane, and whose apex is \((0,0,h)\), with \(h>0\). Orthogonally project onto a Haar-uniform unoriented plane, and let \(N_{n,h}\) be the number of vertices in the projected convex polygon. Put
\[
 c_n=\cos(\pi/n),\qquad t=\frac{h}{\sqrt{h^2+c_n^2}}.
\]
Then the probability of retaining **all \(n+1\) original vertices as vertices of the planar shadow** is exactly
\[
 \boxed{p_n(h):=\Pr(N_{n,h}=n+1)=\frac n\pi\left[2\arcsin\!\left(t\sin\frac\pi n\right)-\arcsin\!\left(t\sin\frac{2\pi}n\right)\right].}
\]
For each \(n\ge5\), this probability has exactly one maximizing height, namely
\[
 \boxed{h_n^*=\frac{c_n}{\sqrt{3c_n^2-1}}.}
\]
The maximum is explicitly
\[
 \boxed{p_n(h_n^*)=\frac n\pi\left[2\arcsin\!\left(\frac{\tan(\pi/n)}{\sqrt3}\right)-\arcsin\!\left(\frac{2\sin(\pi/n)}{\sqrt3}\right)\right].}
\]
As the number of sides grows,
\[
 \boxed{h_n^*\longrightarrow\frac1{\sqrt2},\qquad n^2p_n(h_n^*)\longrightarrow\frac{2\pi^2}{3\sqrt3}.}
\]
More precisely, for each fixed \(h>0\),
\[
 \boxed{\lim_{n\to\infty}n^2p_n(h)=\frac{\pi^2h}{(1+h^2)^{3/2}}.}
\]
All results use the same circumradius-one normalization; scaling the entire pyramid does not change the probabilities. For a general base circumradius \(R\), multiply each displayed optimal height by \(R\).

## Assumptions and scope
The regular base has vertices \(b_j=(\cos(2\pi j/n),\sin(2\pi j/n),0)\) for \(j=0,\ldots,n-1\). The pyramid is the convex hull of those vertices and the apex. A randomly selected plane is Haar-uniform on the Grassmannian of unoriented Euclidean two-planes in \(\mathbb R^3\). Its unit normal is Haar-uniform on the sphere modulo antipodes. Projected vertices mean distinct planar extreme points, not multiplicities of preimages. Degenerate viewing directions, at which supporting face normals are perpendicular to the view, form a spherical null set and can be discarded for probability statements. No nonuniform view weighting, perspective projection, or arbitrary polygonal base is included.

## Proof
**Silhouette criterion and a contiguous block.**  Let \(c=\cos(\pi/n)>0\). Orient the \(n\) side-facet outward normals, omitting their common harmless positive normalization, as
\[
 f_j=(h\cos\phi_j,h\sin\phi_j,c),\quad \phi_j=(2j+1)\pi/n,
\]
while the base-facet outward normal is \(b=(0,0,-1)\). (The side-face equation is \(\langle f_j,x\rangle=hc\).) For a generic viewing normal \(u\), a three-dimensional edge projects to a planar shadow edge exactly when the scalar products with \(u\) of its two incident outward facet normals have opposite signs: this is equivalent to the edge normal cone intersecting \(u^\perp\) in a ray. Genericity also ensures no two distinct polytope edges merge into one projected edge.

By antipodal symmetry choose \(u_z>0\), so the base-facet scalar product is negative. A side-facet scalar product is negative just when
\[
 h\sqrt{u_x^2+u_y^2}\cos(\phi_j-\psi)+cu_z<0,
\]
where \(\psi\) is the azimuth of the horizontal part of \(u\). Because the right-hand threshold for the cosine is strictly negative, the negative side-facet indices form an empty set or one cyclically contiguous block of length strictly less than a half-circle. Let \(m\) be their number. When \(m=0\), all \(n\) base edges are silhouettes and no lateral edge is, so \(N=n\). When \(m\ge1\), precisely \(n-m\) base edges and precisely two lateral edges are silhouettes, so \(N=n-m+2\). In particular \(N=n+1\) if and only if \(m=1\).

**Exact singleton probability.**  Represent \(u\) by a standard three-dimensional Gaussian \(G/\|G\|\), conditioned on \(G_z>0\). Write
\[
 t=\frac{h}{\sqrt{h^2+c^2}},\quad \alpha=\arcsin t,\quad
 \varphi_k=2\arcsin\!\left(t\sin\frac{k\pi}{n}\right)\quad(k=1,2).
\]
The angle between two normalized side-facet outward normals whose indices differ by \(k\) is exactly \(\varphi_k\), because their dot product is \(1-2t^2\sin^2(k\pi/n)\). The normal makes angle \(\alpha\) with the upward vertical. For each index \(j\), set \(E_j=\{\langle f_j,G\rangle<0\}\). The normal-sign arcsine identity for centered Gaussian pairs and triples gives
\[
 \Pr(E_j\mid G_z>0)=\frac\alpha\pi,
 \qquad
 \Pr(E_j\cap E_{j+k}\mid G_z>0)=\frac{2\alpha-\varphi_k}{2\pi}\quad(k=1,2).
\]
For clarity, the triple-sign formula used here is
\[
 \Pr(X_1>0,X_2>0,X_3>0)
 =\frac18+\frac1{4\pi}\sum_{1\le i<j\le3}\arcsin\bigl(\operatorname{Corr}(X_i,X_j)\bigr)
\]
for any nondegenerate centered Gaussian triple. It follows by expanding \(\prod_i(1+\operatorname{sgn}X_i)/8\), observing that odd sign moments vanish under central symmetry, and applying the standard Gaussian sign-correlation identity \(\mathbb E[\operatorname{sgn}X_i\operatorname{sgn}X_j]=2\arcsin(\rho_{ij})/\pi\). For the present triple \((G_z,-\langle f_j,G\rangle,-\langle f_{j+k},G\rangle)\), the three correlations equal \(-\sqrt{1-t^2},-\sqrt{1-t^2},\cos\varphi_k\), giving the displayed pair probability.

For \(n\ge5\), the side-normal azimuthal step \(\delta=2\pi/n\) is strictly less than \(\pi/2\). If both neighbors of \(j\) have negative scalar product, their average is \(h\cos\delta\,x+cz<0\), where \(x\) is the viewing direction's horizontal coordinate along the middle normal and \(z>0\); hence \(x<0\) and the middle scalar product \(hx+cz\) is also negative. Therefore \(E_{j-1}\cap E_{j+1}\subset E_j\). The event that \(j\) is the only negative side facet is exactly \(E_j\setminus(E_{j-1}\cup E_{j+1})\), since the negative block is contiguous. Inclusion-exclusion and the pair formulas give its probability as
\[
 \frac\alpha\pi-2\frac{2\alpha-\varphi_1}{2\pi}+\frac{2\alpha-\varphi_2}{2\pi}
 =\frac{\varphi_1-\varphi_2/2}{\pi}.
\]
The \(n\) possible unique indices are disjoint, proving the exact formula for \(p_n(h)\).

**Unique optimal shape.**  Set \(x=\pi/n\), \(a=\sin x\), and \(c=\cos x\). The height parameter \(t=h/\sqrt{h^2+c^2}\) is strictly increasing from zero to one. The probability is \(n/\pi\) times \(g(t)=2\arcsin(at)-\arcsin(2act)\). Its derivative has the sign of
\[
 \frac1{\sqrt{1-a^2t^2}}-\frac c{\sqrt{1-4a^2c^2t^2}},
\]
which, by squaring its positive terms and clearing positive denominators, has exactly the sign of \(1-3c^2t^2\). Since \(c\ge\cos(\pi/5)>1/\sqrt3\), exactly one turning point occurs in \((0,1)\), at \(t^*=1/(\sqrt3c)\). The probability is strictly increasing before and strictly decreasing afterward; thus this is its unique global maximizer. Converting \(t^*\) back to \(h\) yields the stated height and maximum.

**Large-side limits.**  At fixed \(t\) in a compact subinterval of \((0,1)\), Taylor expansion at \(x=0\) gives
\[
 2\arcsin(t\sin x)-\arcsin(t\sin 2x)=t(1-t^2)x^3+O(x^5).
\]
For fixed positive \(h\), \(c_n\to1\), hence \(t\to h/\sqrt{1+h^2}\); multiplying by \(n/\pi\) proves the fixed-height limit. At the unique optimal height, \(t_n^*=1/(\sqrt3c_n)\to1/\sqrt3\), yielding the sharp maximum constant \(\pi^2(1/\sqrt3)(2/3)=2\pi^2/(3\sqrt3)\) and the optimal-height limit. The Taylor remainder is uniform in a neighborhood of the limiting \(t\), justifying its substitution by \(t_n^*\).

## Verification
Run the standalone checker using `python3 verify.py` with NumPy, SciPy and mpmath installed. It reconstructs two-dimensional orthogonal projections and computes their convex hulls without using the facet-sign derivation, comparing empirical maximal-vertex frequencies with the exact law for four different side counts and three heights each. It also checks strict local optimality, the critical-parameter identity, and high-precision convergence of the maximum to its stated constant. The successful test output ends `ALL_REGULAR_PYRAMID_FULL_SHADOW_CHECKS_PASSED`. The analytical arguments above, not finite samples, establish the all-dimension results.

## Relationship to prior work
Black and Criado (arXiv:2406.06936, initial version June 11, 2024) study average sizes of random projections of general fixed polytopes, proving geometric upper and lower bounds, not an exact full-silhouette law or an optimal-height classification for these pyramids. Their open-access journal text was inspected, including its main statements and proof approach. A separately published exact law for **right rectangular** pyramids already establishes the five-vertex case and its height optimum; that result covers the square-base instance corresponding to \(n=4\), which is therefore **excluded** from this finding. A polygonal pyramid with \(n\ge5\) has more silhouette types, so its maximal-vertex probability cannot be inferred just from the expected vertex count or the rectangular-pyramid formula. The present assessed contribution is the all-\(n\ge5\) exact singleton normal-cone probability, sharp unique optimal height, and sharp \(n^{-2}\) law. Existing general Gaussian sign and normal-cone principles are credited as methods, not claimed as discoveries.

## Limitations
The base must be a regular polygon of at least five sides and the apex must lie directly over its center. The theorem does not determine the entire shadow vertex-count distribution for all \(n\), the behavior under nonuniform viewing directions, or the optimal shape among all polygonal pyramids. It concerns orthogonal, not perspective, projections. The originality comparison is based on the inspected sources and relevant searches and is not an exhaustive historical-priority certification; an equivalent result indexed under a different description remains possible. No independent audit has been carried out.

## References
1. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936 (first posted June 11, 2024), https://arxiv.org/abs/2406.06936 ; open-access full text, *Discrete & Computational Geometry*, published October 31, 2026, https://link.springer.com/article/10.1007/s00454-026-00880-4 .
2. *Exact five-vertex shadow law and unique height optimum for right rectangular pyramids*, publicly accessible mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-five-vertex-shadow-law-and-unique-height-optimum-for-right--2273575e8a0a . This treats the excluded four-sided-base case.
3. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464 (March 12, 2012), https://arxiv.org/abs/1203.2464 . Background on Haar-random polytope shadows of cubes and regular tetrahedra; not a polygonal-pyramid law.
