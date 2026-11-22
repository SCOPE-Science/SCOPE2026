# Eighteen cubic, quartic, and quintic intersection-body components of a centered square pyramid

## Finding

Let
\[
P=\operatorname{conv}\{(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,-1),(0,0,4)\}\subset\mathbb R^3.
\]
Its five vertices have arithmetic mean the origin, which is strictly inside the right square pyramid. Define the intersection body \(IP\) by the radial function \(\rho_{IP}(\theta)=\operatorname{area}(P\cap\theta^\perp)\) for unit vectors \(\theta\in S^2\). The complex Zariski closure of its real topological boundary has **exactly 18 distinct absolutely irreducible hypersurface components**: eight cubics, two quartics, and eight quintics. Consequently, its squarefree algebraic boundary has degree \(8\cdot3+2\cdot4+8\cdot5=72\) and has no linear component.

The full degree classification is given by the following rule. For a normal \(u=(x,y,z)\) with \(z\ne0\), write \(p=x+y\), \(q=x-y\). Away from the four planes \(p=\pm z\) and \(q=\pm z\), its boundary branch is a cubic if both \(|p/z|>1\) and \(|q/z|>1\), a quartic if both \(|p/z|<1\) and \(|q/z|<1\), and a quintic if exactly one of these two inequalities exceeds one. The same classification holds for either sign of \(z\). All 18 real sectors determine distinct irreducible complex components.

## Assumptions and scope

The standard Euclidean scalar product and Euclidean \(2\)-dimensional section area are used. The chosen origin is the *arithmetic mean of the five vertices*, not the volume centroid of the pyramid. The claim is about this one centrally based, right square pyramid and its invertible linear images centered at their transformed vertex means, not about arbitrary translations or all five-vertex polytopes. An intersection body need not be convex, but it is a star body here since the origin lies in the interior of \(P\).

For any nonzero \(u\in\mathbb R^3\), use the homogeneous extension \(\rho_{IP}(u)=\operatorname{area}(P\cap u^\perp)/\|u\|\), so that \(u\in\partial IP\) exactly when \(\rho_{IP}(u)=1\). Algebraic boundary means the smallest complex algebraic set containing the real boundary, with its squarefree hypersurface components. This is a different invariant from the number of polygonal section types or the number of facets of \(P\).

## Proof

**1. Exact rational radial function.** Label the vertices in the displayed order by \(v_1,\ldots,v_5\), and let \(h_i=u\cdot v_i\). Triangulate the pyramid into the two tetrahedra with vertex indices \((1,2,3,5)\) and \((1,3,4,5)\). Each has Euclidean volume \(10/3\).

For a tetrahedron with four distinct real vertex heights \(a_1,\ldots,a_4\), the height \(H\) of a point sampled uniformly by volume has probability density
\[
 f_H(t)=3\sum_{i=1}^4\frac{(a_i-t)_+^2}{\prod_{j\ne i}(a_i-a_j)},\qquad (s)_+=\max(s,0).
\]
Here is a derivation, so no unproved spline identity is required. The barycentric coordinates are uniformly distributed on the three-simplex. Repeated elementary integration of their exponential integral yields
\[
 \mathbb E[e^{sH}]=\frac{6}{s^3}\sum_{i=1}^4\frac{e^{sa_i}}{\prod_{j\ne i}(a_i-a_j)}\quad(s>0).
\]
Indeed, integration of the last barycentric coordinate and induction on the number of vertices give the divided-difference identity, starting with the elementary integral along a segment. The displayed proposed density has the same bilateral Laplace transform because \(\int_{-\infty}^{a}e^{st}(a-t)^2dt=2e^{sa}/s^3\); uniqueness of transforms of integrable distributions proves the density formula. Coincident heights follow by continuity.

The coarea identity \(\operatorname{area}(T\cap u^\perp)/\|u\|=\operatorname{vol}(T)f_H(0)\) for each tetrahedron therefore yields
\[
 \rho_{IP}(u)=10\sum_{T\in\{(1,2,3,5),(1,3,4,5)\}}
 \ \sum_{i\in T:\,h_i>0}\frac{h_i^2}{\prod_{j\in T\setminus\{i\}}(h_i-h_j)}.\tag{1}
\]
In this formula the heights are explicitly
\[
(h_1,h_2,h_3,h_4,h_5)=(p-z,-q-z,-p-z,q-z,4z).\tag{2}
\]
The rational expression from (1) is valid on every open region in which the signs of these five heights are fixed; apparent height-collision poles are resolved by continuity. It is homogeneous of degree \(-1\).

**2. All normal sectors.** On \(z>0\), the four base-vertex sign planes become the four lines \(p/z=\pm1\), \(q/z=\pm1\); these form a Cartesian \(3\times3\) grid of nine open sectors. The apex has positive height. On \(z<0\) the apex has negative height, and there is another grid of nine. These are all connected components of the complement of the five vertex-height planes: no additional sectors occur at \(z=0\). There are \(18\) sectors in all.

Reduce the appropriate sum in (1), without fixing a scale, to a coprime fraction \(\rho_{IP}(u)=10N_C(u)/D_C(u)\), where \(N_C,D_C\in\mathbb Q[x,y,z]\) are homogeneous, and \(\deg D_C=\deg N_C+1\). The exact table `CERTIFICATE.json` lists all 18 reduced numerator–denominator pairs and a rational witness normal in every sector. The standalone program `checker.py` independently reconstructs these entries from (1) by symbolic rational reduction and checks the entire table. The resulting exhaustive table is:

| Region in either half-space | Sectors per half-space | Degree of \(D_C\) | Degree of \(N_C\) |
|---|---:|---:|---:|
| Both \(|p/z|>1\), \(|q/z|>1\) | 4 | 3 | 2 |
| Both \(|p/z|<1\), \(|q/z|<1\) | 1 | 4 | 3 |
| Exactly one of \(|p/z|,|q/z|\) exceeds 1 | 4 | 5 | 4 |

The checker enumerates one explicit rational point in every sector, computes all eighteen numerators and denominators exactly, and verifies their coprimality and degree. It also verifies, by exact cross multiplication, that all \(\binom{18}{2}=153\) pairs of reduced rational branch functions are distinct. Thus the table is a finite exhaustive algebraic calculation, not a sample of signs or numerical interpolation.

**3. Irreducibility and distinctness.** The corresponding real boundary patch is cut out by
\[
 F_C(x,y,z)=D_C(x,y,z)-10N_C(x,y,z)=0.\tag{3}
\]
Let \(d=\deg D_C\), so \(\deg N_C=d-1\). Homogenizing (3) by \(w\) gives \(D_C-10wN_C\). Because \(\gcd(N_C,D_C)=1\), this is a primitive degree-one polynomial in \(w\) over the UFD \(\mathbb C[x,y,z]\), and is irreducible over \(\mathbb C[x,y,z,w]\) by Gauss's lemma. As it is not divisible by \(w\), its dehomogenization \(F_C\) is absolutely irreducible too. If two such irreducible equations defined the same hypersurface, they would differ by a nonzero scalar. Comparing their homogeneous top-degree and next-degree parts would then force \(N_C/D_C=N_{C'}/D_{C'}\), contrary to the 153 exact pairwise checks. They are therefore all different.

Every open normal sector gives an open two-dimensional boundary patch via the radial parametrization \(u\mapsto\rho_{IP}(u/\|u\|)u/\|u\|\). Such a patch is Zariski dense in its irreducible algebraic surface (an irreducible complex surface cannot contain a full open real surface patch in a lower-dimensional algebraic subset). Normal directions on the separating planes arise as limits by continuity; they contribute at most one-dimensional real patches and hence no additional hypersurface components. Consequently the entire algebraic boundary is exactly the union of the eighteen surfaces (3), with degree multiset \(\{3^8,4^2,5^8\}\) and sum of degrees 72.

## Verification

Run `python checker.py` alongside `CERTIFICATE.json` with the dependencies in `requirements.txt`. It derives the nine normal-direction sectors on each side of \(z=0\), tests 18 coprime homogeneous rational functions, verifies the degree multiset and all 153 pairwise inequalities, and independently obtains 180 Euclidean section areas from the eight original pyramid edges by constructing their planar convex hulls. The direct areas agree with (1) within a relative tolerance of \(2\times10^{-8}\). As a simple independent exact check, the horizontal slice at \(z=0\) is a square of side \(8/5\), so \(\rho_{IP}(0,0,1)=64/25\), and this agrees with (1). Numerical section checks are corroboration; the all-direction result follows from the exact derivation and the exhaustive symbolic certificate.

## Relationship to prior work

Berlow, Brandenburg, Meroni and Shankar [1] proved semialgebraicity and a general upper bound on component degrees, and calculated specific cube, regular tetrahedron, icosahedron and a four-dimensional polytope example. Their Example 5.8 shows the vertex-centered tetrahedron has cubic and quartic components; their bound for the eight-edge square pyramid is six, whereas the highest actual degree here is five. This five-vertex example therefore exhibits three distinct nonlinear component degrees, a variety not present in the vertex-barycenter-centered tetrahedron. Brandenburg and Meroni [2] developed translation-dependent and convexity results; their inspected statements do not give this degree classification. The companion mathematical software [3] implements the general algorithm, with documented cube examples; it is not an already stated square-pyramid census. The present result is a specific exact application and irreducibility/degree certification, not a claim to have invented the general semialgebraic framework.

## Limitations

The classification concerns the specified vertex-barycenter-centered pyramid, not the translation to the volume centroid or all square pyramids. Its proof is exact, but it has not received an independent mathematical audit. The novelty comparison uses the inspected primary texts, supplied computational notebooks and accessible mathematical records; equivalent unpublished or unindexed calculations may exist. The formula treats exceptional normal directions by continuity and does not describe the scheme structure of intersections between different components.

## References

[1] K. Berlow, M.-C. Brandenburg, C. Meroni, I. Shankar, *Intersection Bodies of Polytopes*, first public preprint 2021-10-12, https://arxiv.org/abs/2110.05996 ; Beiträge zur Algebra und Geometrie 63 (2022), 419–439, https://doi.org/10.1007/s13366-022-00621-7.

[2] M.-C. Brandenburg, C. Meroni, *Intersection Bodies of Polytopes: Translations and Convexity*, first public preprint 2023-02-23, https://arxiv.org/abs/2302.11764 ; Journal of Algebraic Combinatorics 60 (2024), 127–143, https://doi.org/10.1007/s10801-024-01328-9.

[3] MATHREPO, *Intersection Bodies of Polytopes* companion mathematical software and worked examples, https://mathrepo.mis.mpg.de/intersection-bodies/ (accessed 2026-11-20 UTC).
