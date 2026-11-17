# First two Steiner coefficients of layered order polytopes forget layer sizes

## Finding

Let \(P=A_1\oplus\cdots\oplus A_r\) be the ordinal sum of \(r\ge2\) antichains with **every** cardinality \(a_i=|A_i|\ge2\). Set \(n=\sum_i a_i\) and \(k=r-1\). In the canonical unit-coordinate Euclidean realization \(K=\mathcal O(P)\),

\[
\operatorname{Vol}_n(K)=\frac{\prod_i a_i!}{n!},\qquad
\frac{\operatorname{Area}_{n-1}(\partial K)}{\operatorname{Vol}_n(K)}=n(2+k\sqrt2),
\]

and the second intrinsic volume is

\[
\boxed{\frac{V_{n-2}(K)}{\operatorname{Vol}_n(K)}
=n(n-1)\left(\frac12+\frac{k\sqrt2}{2}+\frac{k\sqrt3}{6}+\frac{k(k-1)}4\right).}
\]

Consequently the coefficients through quadratic order in the outer-parallel-volume expansion, **after division by the original volume**, are independent of the individual layer sizes. In particular,

\[
\frac{\operatorname{Vol}_n(K+tB_n)}{\operatorname{Vol}_n(K)}
=1+n(2+k\sqrt2)t
+\pi n(n-1)\left(\frac12+\frac{k\sqrt2}{2}+\frac{k\sqrt3}{6}+\frac{k(k-1)}4\right)t^2+O_K(t^3).
\]

For example, the profiles \((2,2,4)\) and \((2,3,3)\), both with eight coordinates and three layers, have respectively \(18\) and \(20\) facets, yet identical normalized surface area and second intrinsic volume.

## Assumptions and scope

An ordinal sum places every element of the earlier antichain below every element of each later antichain; elements within a layer are incomparable. The order polytope is the set of all \(x\in[0,1]^n\) satisfying \(x_u\le x_v\) whenever \(u<v\) in the poset. Its geometry is measured using the *ambient standard Euclidean metric*, not an affine-equivalent realization or a normalized lattice metric. The condition \(a_i\ge2\) is essential: singleton layers introduce additional ridge incidences and invalidate the stated universal formula. Surface area is the sum of ordinary \((n-1)\)-dimensional Hausdorff measures of facets. Intrinsic volumes use the Steiner convention

\[
\operatorname{Vol}_n(K+tB_n)=\sum_{j=0}^n\kappa_jV_{n-j}(K)t^j,
\qquad\kappa_1=2,\ \kappa_2=\pi.
\]

## Proof

**1. Facets, triangulation, and volume.** The facets, all irredundant, are the bottom walls \(L_u:x_u=0\), \(u\in A_1\); the top walls \(U_v:x_v=1\), \(v\in A_r\); and the adjacent-layer equality walls \(E_{i;u,v}:x_u=x_v\), where \(u\in A_i\), \(v\in A_{i+1}\), \(1\le i<r\). Their outward unit normals are respectively \(-e_u\), \(e_v\), and \((e_u-e_v)/\sqrt2\). The order-simplex triangulation is indexed by independently permuting the elements within every layer. It comprises exactly \(\prod_i a_i!\) coordinate-order simplices, each of volume \(1/n!\), establishing the asserted volume.

**2. Facet measures.** In a coordinate-order simplex, a boundary equality is described by tying its participating coordinates. A tie block of size \(s\) has Euclidean Jacobian \(\sqrt{s}\). Elementary simplex-volume integration, or counting permutations compatible with each designated tie and multiplying by this Jacobian, yields the following facet measures divided by the full volume:

\[
\frac{\operatorname{Area}(L_u)}{\operatorname{Vol}(K)}=\frac{n}{a_1},\quad
\frac{\operatorname{Area}(U_v)}{\operatorname{Vol}(K)}=\frac{n}{a_r},\quad
\frac{\operatorname{Area}(E_{i;u,v})}{\operatorname{Vol}(K)}=\frac{n\sqrt2}{a_i a_{i+1}}.
\]

Summing over \(a_1\) bottom, \(a_r\) top, and \(a_i a_{i+1}\) walls at each interface gives \(n(2+k\sqrt2)\).

**3. Exhaustive ridge incidences.** A ridge is a codimension-two face. Because all layers have at least two coordinates, a pair of distinct facet equalities produces a ridge precisely in these cases: (i) two bottom walls, two top walls, or one of each; (ii) a boundary wall and an edge-equality wall, unless they use the same coordinate at the adjacent interface; (iii) two equalities at the same interface sharing exactly one endpoint; or (iv) equalities at different interfaces that have no shared coordinate. Disjoint equalities at one interface force four coordinates to tie, hence codimension at least three. Equalities at consecutive interfaces sharing their middle coordinate force every coordinate of that intermediate layer to tie as well, again codimension at least three. The excluded boundary-edge pairs similarly force at least three coordinate ties. All listed compatible pairs admit strictly ordered remaining coordinates and create exactly two independent constraints. In particular, no higher-dimensional face is miscounted as a ridge.

**4. Aggregate ridge-measure identities.** Let \(H_{n-2}\) denote the \((n-2)\)-dimensional Hausdorff measure, and normalize all ridge sums by \(n(n-1)\operatorname{Vol}(K)\). The complete partition into angle classes is

| Ridge class | Normalized total measure | Exterior normal angle |
|---|---:|---:|
| Boundary–boundary | \(2\) | \(\pi/2\) |
| Boundary–equality | \(2k\sqrt2\) | \(\pi/2\) |
| Same-interface equalities sharing one endpoint | \(k\sqrt3\) | \(\pi/3\) |
| Different-interface equalities, with distinct middle coordinates when adjacent | \(k(k-1)\) | \(\pi/2\) |

Here the identity in the last line is \(2\binom{k}{2}=k(k-1)\). We justify each value by summing the exact face measures. Two designated boundary coordinates have relative tie measure \(n(n-1)/(a_1(a_1-1))\) at the bottom, analogously at the top, and \(n(n-1)/(a_1a_r)\) for opposite boundaries. After summation they contribute \(\tfrac12+\tfrac12+1=2\). A compatible boundary–equality pair at one interface has a two-coordinate tie block and Jacobian \(\sqrt2\); the ordered-coordinate multiplicities cancel its layer factors, giving \(n(n-1)\sqrt2\) at the bottom and again at the top, for each of the \(k\) interfaces. Same-interface equalities sharing an endpoint tie three coordinates, with Jacobian \(\sqrt3\). Pairs sharing a lower endpoint and pairs sharing an upper endpoint each contribute \(n(n-1)\sqrt3/2\) per interface. Two separate equality blocks contribute Jacobian \(2\). At distinct nonadjacent interfaces their independent layer-order probabilities cancel all layer factors; at consecutive interfaces the distinct two middle coordinates occur in prescribed order with probability \(1/[a_{i+1}(a_{i+1}-1)]\), cancelling the corresponding number of choices. Thus each interface pair contributes \(2n(n-1)\), giving the last table entry. This establishes the table for all integer layer sizes at least two.

**5. Curvature and Steiner coefficient.** In a Euclidean convex polytope, the exterior angle of a ridge equals the angle between its two outward unit facet normals, and

\[
V_{n-2}(K)=\frac1{2\pi}\sum_{F\text{ ridge}}H_{n-2}(F)\,\phi_F.
\]

The outward normals of the shared-endpoint same-interface equalities have dot product \(1/2\), giving angle \(\pi/3\); all other incident pairs in the table are orthogonal, giving angle \(\pi/2\). Substitution gives

\[
\frac{V_{n-2}(K)}{\operatorname{Vol}(K)}
=\frac{n(n-1)}{2\pi}\left[
\bigl(2+2k\sqrt2+k(k-1)\bigr)\frac\pi2+k\sqrt3\frac\pi3\right],
\]

which simplifies to the claimed formula. The derivation proves the unrestricted theorem; finite computations are supplementary checks only.

## Verification

The standalone `verify_layered_order.py` independently constructs order-polytope vertices and all irredundant facet equations, selects actual codimension-two intersections by numerical affine rank, computes their Euclidean measures using intrinsic projected convex hulls, and sums the exterior normal angles. It also computes ordinary facet area directly, not by the counting identities. Running `python verify_layered_order.py` with NumPy and SciPy yields `LAYERED_STEINER_PASS profiles=16 ridges=1356 max_layers=5`. The 16 profiles include two through five layers and unequal layer sizes. This is finite corroboration only; the analytical facet/ridge partition and cancellation establish the general result.

## Relationship to prior work

Stanley's classical theory supplies order-polytope facets, simplex triangulation, and normalized volume. Ahmad, Fourier, and Joswig (first public preprint September 4, 2023) establish face-normal forms and \(f\)-vector inequalities for maximal ranked posets, a class including ordinal sums of antichains. Those statements concern affine-combinatorial face data and do not directly determine Euclidean facet measures, dihedral angles, or the volume-normalized second Steiner coefficient. Can and Hibi investigate toric codes from related order polytopes, not these Euclidean coefficients. The present calculation uses the classical triangulation but adds an explicit metric ridge classification and weighted exterior-angle sum. An exhaustive historical-priority guarantee is not asserted.

## Limitations

The formula applies only to the canonical coordinate realization and only when every layer has at least two elements. It does not claim equal unnormalized intrinsic volumes, equal full Steiner polynomials, or independence of general Euclidean metric deformations. The second-order term is exact; higher-order coefficients have not been classified. The claim has not undergone independent mathematical review.

## References

- Richard P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI: 10.1007/BF02187680.
- Ibrahim Ahmad, Ghislain Fourier, and Michael Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, initial preprint September 4, 2023, https://arxiv.org/html/2309.01626v2.
- Mahir Bilen Can and Takayuki Hibi, *Toric Codes from Order Polytopes*, arXiv:2102.03651, initial preprint February 6, 2021, https://arxiv.org/html/2102.03651v2.
