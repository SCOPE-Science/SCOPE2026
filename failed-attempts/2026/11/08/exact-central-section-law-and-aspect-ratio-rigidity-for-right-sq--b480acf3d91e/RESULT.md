# Exact central-section law and aspect-ratio rigidity for right square antiprisms

## Finding

For every real \(h>0\), let \(K_h\) be the convex hull of the eight points
\[
 (1,0,h),\ (0,1,h),\ (-1,0,h),\ (0,-1,h),
 \qquad (\pm 2^{-1/2},\pm 2^{-1/2},-h),
\]
where all four independent choices of the two signs appear in the final group. This is the right square antiprism with equal base circumradii \(1\), square bases in planes \(z=\pm h\), and relative twist \(\pi/4\). Let \(U\) be Haar-uniform on the sphere and let \(N_h(U)\) count the sides of the nondegenerate central section \(K_h\cap U^\perp\).

**Theorem.** For every \(h>0\), \(N_h(U)\in\{6,8\}\) with probability one. Writing \(s=h^2\),
\[
 \Pr(N_h=8)=p(s)=\frac4\pi\left[
 \arccos\!\left(\frac{s}{1+s}\right)+
 \arccos\!\left(\frac{1/\sqrt2-s}{1+s}\right)\right]-3,
 \qquad \Pr(N_h=6)=1-p(s).
\]
The function \(p:(0,\infty)\to(0,1)\) is a strictly increasing bijection. Thus the probability of an octagonal central section determines the antiprism's height-to-base-radius ratio \(2h\), and hence its similarity class, inside this one-parameter family.

For the **uniform** square antiprism (all sixteen edges equal), \(h^2=\sqrt2/4\), giving
\[
 \Pr(N_h=8)=\frac8\pi\arccos\left(\frac{2\sqrt2-1}{7}\right)-3
 =0.327044097138468\ldots,
\]
while the complementary hexagon probability is \(0.672955902861532\ldots\).

## Assumptions and scope

The sampling measure is the rotation-invariant probability distribution on **unoriented planes through the origin**, equivalently uniform sphere normals modulo antipodes. No independent offset is sampled. Exceptional planes through vertices or containing polyhedron edges have sphere measure zero; all polygon-side claims are almost-sure, not assertions about these exceptional planes. The positive-parameter family consists of congruent regular square bases with the specified relative twist and common centered axis, up to similarity. The theorem does not apply to arbitrarily distorted or tapered antiprisms.

## Proof

**1. Geometry and the section-side count.** A generic central plane contains no vertex and meets each edge either transversely in one point or not at all. Convexity implies that the section is a convex polygon and that each cut edge contributes exactly one section vertex. Thus its number of sides is the number of edges with opposite endpoint signs under the linear functional \(x\mapsto U\cdot x\). The edge graph consists of four edges around each square and eight joining the two squares. Each vertex has degree four.

**2. Exhaustive two-type lemma.** At the regular metric parameter \(h_0=2^{1/4}/2\), multiply all coordinates by two. The resulting top vertices are \((\pm2,0,t),(0,\pm2,t)\) and the bottom vertices are \((\pm t^2,\pm t^2,-t)\), where \(t^4=2\) and \(t>0\). All eight vertices have the same squared norm \(4+t^2\). Their orthogonality great circles on the unit normal sphere have no triple intersections: all 56 three-vertex determinants are nonzero in the exact number field \(\mathbb Q[t]/(t^4-2)\). Therefore the eight circles have precisely \(2\binom82=56\) intersection points, \(8\cdot14=112\) open arcs, and, by Euler's identity, exactly \(112-56+2=58\) sign chambers.

For completeness, enumerate the four sectors near both antipodal intersections of every pair of circles. At an intersection \(x=\pm(v_i\times v_j)\), use the infinitesimal normal \(x+\epsilon(\sigma_i v_i+\sigma_jv_j)\), where \(\sigma_i,\sigma_j\in\{\pm1\}\) and \(\epsilon>0\) is sufficiently small. The two chosen vertex signs equal \(\sigma_i,\sigma_j\), since all vertices have equal norm and are nonparallel; the other six are determined by the nonzero exact signs of their dot products with \(x\). This produces **58 distinct feasible sign chambers**. Every one is accounted for because 58 is also the Euler upper count. The full reproducible sign-chamber list in `CHAMBERS.txt`, together with the exact number-field checker in `antiprism.py`, classifies **24 chambers with six cut edges** and **34 with eight cut edges**; none has any other cut-edge count. Exact signs are computed by rational enclosures for the positive root of \(t^4=2\), not by floating-point tests. This is an exhaustive finite combinatorial certificate, not a random sample.

For arbitrary \(h>0\), the invertible linear transformation \(\operatorname{diag}(1,1,h/h_0)\) maps \(K_{h_0}\) to \(K_h\) and bijects central planes. It preserves section polygons and their numbers of sides. Although this transformation does not preserve the Haar distribution of normals, it proves that the only almost-sure types remain six and eight at every positive height.

**3. Exact Haar expectation.** If \(a,b\) are nonzero vectors making Euclidean angle \(\theta\in[0,\pi]\), then the probability that \(U\cdot a\) and \(U\cdot b\) have opposite signs for Haar-uniform \(U\in S^2\) is \(\theta/\pi\). This follows by projecting \(U\) radially to the plane they span and measuring the two angular arcs on which the signs differ.

Every vertex of \(K_h\) has squared norm \(1+h^2\). The eight base-square edges join vectors whose inner product is \(h^2\). The eight lateral edges join vectors whose inner product is \(1/\sqrt2-h^2\). Linearity of expectation therefore gives
\[
 \mathbb E N_h=\frac8\pi\left[
 \arccos\left(\frac{h^2}{1+h^2}\right)+
 \arccos\left(\frac{1/\sqrt2-h^2}{1+h^2}\right)\right].
\]
Since the two-type lemma gives \(\mathbb E N_h=6+2\Pr(N_h=8)\), rearrangement yields the claimed exact probability formula.

**4. Strict monotonicity and endpoints.** Put \(c=1/\sqrt2\) and \(s=h^2\). Differentiation gives
\[
 \frac{\pi}{4}(1+s)p'(s)
 =\frac{\sqrt{1+c}}{\sqrt{1-c+2s}}-\frac1{\sqrt{1+2s}}>0.
\]
The last inequality follows upon squaring positive terms, since \((1+c)(1+2s)-(1-c+2s)=2c(1+s)>0\). Moreover, \(\lim_{s\downarrow0}p(s)=0\) and \(\lim_{s\to\infty}p(s)=1\), directly from the arccosine formula. Continuity and strict increase establish the claimed bijection and inverse shape determination.

**5. Equilateral lateral triangles.** The top and bottom square edges have squared length \(2\). Every lateral edge has squared length \(2-\sqrt2+4h^2\). These are all equal exactly when \(h^2=\sqrt2/4\). Substitution into the general formula, using \(\sqrt2/(4+\sqrt2)=(2\sqrt2-1)/7\), gives the uniform-antiprism specialization.

## Verification

Run `python antiprism.py` using the Python standard library. It constructs the eight vertices and sixteen edges in the ring \(\mathbb Z[t]/(t^4-2)\), determines signs using certified rational fourth-root intervals, asserts nonvanishing of every three-vertex determinant, exhausts all 58 feasible sign chambers, and checks that their cut-edge counts are six or eight in exactly 24 and 34 cases. Its independent spherical-excess calculation integrates all 58 areas to \(4\pi\) within stated numerical accuracy; that integration is a secondary check, not the exact proof.

Run `python independent_check.py` and `python family_check.py` with NumPy and SciPy installed for floating-point checks. The first samples 300,000 Haar normals for the uniform antiprism and constructs 300 actual planar convex hull sections. The second samples 100,000 normals at each of five positive height ratios and checks the closed formula. Random tests are not exhaustive and do not substitute for the finite exact sign computation or analytical expectation and derivative arguments.

## Relationship to prior work

Hartley, Pellicer and Williams (2012) classify minimal regular abstract covers of prisms and antiprisms; their relevant sections study polytope combinatorics and monodromy, not Haar probabilities for geometric central slices. General inverse section investigations by Goodey and Weil (1992) concern random affine-flat sections and mean bodies, a different sampling measure and invariant. Published exact central-section laws for a regular icosahedron and rectangular boxes concern different solids and do not imply a right square antiprism's aspect-ratio law. The edge-crossing expectation is elementary; the asserted contribution is its combination with an exhaustive section-type classification and the resulting *global* invertible one-parameter probability law. A separate problem about planes through three surface-uniform antiprism points uses a different, non-Haar distribution and does not entail this theorem.

## Limitations

The theorem describes only central planes and one parametrized family, up to similarity. It does not recover a general polyhedron from one section statistic. The finite checker is an exact exhaustiveness argument after the displayed geometric reduction, not an automated formal proof. Numerical probabilities are approximations to the exact expressions, without certified decimal error intervals. Literature priority is provisional pending independent review; the present inspection does not rule out an unindexed equivalent theorem or table.

## References

- M. I. Hartley, D. Pellicer and G. Williams, *Minimal covers of the prisms and antiprisms*, arXiv:1206.6119v1 (first public version 2012-06-26), especially Sections 1 and 5. https://arxiv.org/abs/1206.6119
- P. Goodey and W. Weil, *The determination of convex bodies from the mean of random sections*, Mathematical Proceedings of the Cambridge Philosophical Society **112** (1992), 419–430, DOI:10.1017/S0305004100071085. https://doi.org/10.1017/S0305004100071085
- *Exact Haar polygon-type law for central icosahedron sections*, publicly indexed published-finding corpus record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f
- *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, publicly indexed published-finding corpus record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4
