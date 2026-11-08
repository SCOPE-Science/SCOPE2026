# The first distance-law kink counts systoles on a closed hyperbolic surface

## Finding
Let \(S\) be a connected, closed, orientable hyperbolic surface of constant Gaussian curvature \(-1\), area \(A\), and systole length \(\ell>0\). Let \(k\) be the number of distinct **unoriented** closed geodesics of length \(\ell\). For independent area-uniform points \(X,Y\in S\), let \(F(r)=\Pr(d_S(X,Y)\le r)\), and set \(r_0=\ell/2\).

For some \(\eta>0\), one has the exact identity
\[
F(r)=\frac{2\pi(\cosh r-1)}{A}\qquad (0\le r\le r_0)
\]
and the one-sided expansion
\[
F(r_0+\varepsilon)=\frac{2\pi(\cosh(r_0+\varepsilon)-1)}{A}
-\frac{2\pi k\ell}{A^2}\varepsilon^2+O_S(\varepsilon^3)
\quad(0<\varepsilon<\eta).
\]
In particular, \(F\) is continuously differentiable at \(r_0\), has second derivatives from both sides, and their **negative jump** is precisely
\[
F''(r_0+)-F''(r_0-)=-\frac{4\pi k\ell}{A^2}.
\]
The complete two-point distance law thus determines \(A\), \(\ell\), and \(k\), by
\[
A=\frac{\pi}{\lim_{r\downarrow0}F(r)/r^2},\qquad
\ell=2\inf\{r>0:F(r)<2\pi(\cosh r-1)/A\},\qquad
k=-\frac{A^2}{4\pi\ell}[F''(r_0+)-F''(r_0-)].
\]
The coefficient of the first deviation is universal: it depends only on area, systolic length, and the number of shortest geodesics, not on their mutual intersection pattern.

## Assumptions and scope
All distances are intrinsic geodesic distances. Probability is normalized Riemannian area on both factors of \(S\times S\). A closed hyperbolic surface has genus at least two and \(A=4\pi(g-1)\). Its shortest noncontractible closed geodesics are primitive; there are finitely many of a given bounded length. Each unoriented shortest closed geodesic is counted exactly once in \(k\), even if some distinct shortest geodesics intersect. All asymptotics hold for each **fixed** surface, not uniformly across degenerating hyperbolic metrics. No claim is made about the entire closed-geodesic length spectrum or recovery of the metric.

## Proof
**1. A two-sheet counting window.** Write \(S=\Gamma\backslash\mathbb H^2\) for a torsion-free cocompact subgroup of orientation-preserving hyperbolic isometries, and use a fundamental domain \(\mathcal F\). Every pair of distinct points of any \(\Gamma\)-orbit is separated by at least \(\ell\), since any nontrivial deck transformation has translation length at least \(\ell\). There exists \(\eta_1>0\) such that for \(r<\ell/2+\eta_1\), every hyperbolic radius-\(r\) disk contains at most two points of any orbit. Indeed, otherwise, after sending the disk centers to a fixed point and passing to a compactness subsequence as \(r\downarrow\ell/2\), three points in a disk of radius \(\ell/2\) would be pairwise separated by \(\ell\). Each pair would necessarily be antipodal endpoints of a diameter, which is impossible for three distinct points.

Put \(B(r)=2\pi(\cosh r-1)\), the hyperbolic disk area, and \(L(r,d)\) the area of overlap of two radius-\(r\) hyperbolic disks with center separation \(d\), setting \(L(r,d)=0\) for \(d\ge2r\). In the two-sheet window, the projection of \(B_r(\widetilde x)\) to \(S\) has no fibers of cardinality exceeding two. Counting the extra occurrence of each doubly covered point as a pair yields
\[
A^2 F(r)=A B(r)-\frac12\int_{\mathcal F}
\sum_{\gamma\in\Gamma\setminus\{1\}}
L(r,d(\widetilde x,\gamma\widetilde x))\,d\widetilde x.
\tag{1}
\]
This formula also shows \(F(r)=B(r)/A\) for \(r\le r_0\).

**2. Localization to shortest closed geodesics.** Because the closed-geodesic length spectrum is locally finite, shrink \(\eta_1\) so that \(2r\) lies below the translation length of every deck element except conjugates of the primitive length-\(\ell\) transformations and their inverses. Each primitive unoriented systolic geodesic gives exactly two oriented conjugacy classes, with equal orbital integrals. Unfolding the \(\Gamma\)-conjugacy sum to the cyclic quotient by its primitive element turns (1) into
\[
A^2F(r)=A B(r)-k I_{\ell}(r),
\qquad
I_{\ell}(r)=\ell\int_{-\infty}^{\infty}
L\bigl(r,d_{\ell}(t)\bigr)\cosh t\,dt,
\tag{2}
\]
where \(t\) is signed Fermi distance from a geodesic axis and
\[
d_{\ell}(t)=2\operatorname{arsinh}\bigl(\sinh(\ell/2)\cosh t\bigr).
\tag{3}
\]
The area element on the cyclic quotient is \(\cosh t\,ds\,dt\), with \(s\) modulo \(\ell\). Neither disjointness of shortest geodesics in \(S\) nor embeddedness of all their collars is required: (2) is obtained on their cyclic covers, and the two-sheet counting identity handles intersections.

**3. Lens tangency.** Fix \(r_0>0\), put \(a=\tanh r_0\), and write \(r=r_0+\varepsilon\). The displacement expansion from (3) is
\[
d_{\ell}(t)=\ell+a t^2+O_{\ell}(t^4).
\tag{4}
\]
The geodesic curvature of a radius-\(r_0\) circle is \(\coth r_0=1/a\). Thus two such circles separated by \(2r-h\), for \(h\downarrow0\), bound a thin lens of area
\[
L(r,2r-h)=\frac43\sqrt{a}\,h^{3/2}
+O_{r_0}(h^{5/2}+\varepsilon h^{3/2}).
\tag{5}
\]
For a direct derivation, use Fermi coordinates \((u,v)\) around the geodesic joining the two centers: the metric is \(dv^2+\cosh^2v\,du^2\). The half-width of the overlap in \(u\) at height \(v\) equals
\(\operatorname{arcosh}(\cosh r/\cosh v)-d/2\), which is \(h/2-(\coth r_0)v^2/2\) to leading order. Integrating over both signs of \(u,v\) proves (5), including a locally uniform error.

The overlap in (2) is nonzero precisely on \(|t|=O(\sqrt\varepsilon)\). Equations (4)-(5), along with \(\cosh t=1+O(t^2)\), give
\[
I_\ell(r_0+\varepsilon)
=\frac43\ell\sqrt a
\int_{-\sqrt{2\varepsilon/a}}^{\sqrt{2\varepsilon/a}}
(2\varepsilon-a t^2)^{3/2}\,dt
+O_{\ell}(\varepsilon^3).
\]
Since
\[
\int_{-1}^1(1-u^2)^{3/2}\,du=\frac{3\pi}{8},
\]
the dependence on \(a\) cancels and
\[
I_\ell(r_0+\varepsilon)=2\pi\ell\varepsilon^2+O_\ell(\varepsilon^3).
\tag{6}
\]
The same changes of variables, with \(t=\sqrt\varepsilon\,u\), yield an expansion in integer powers starting with \(\varepsilon^2\), so the needed right second derivative exists. Substituting (6) in (2) proves the claimed expansion and jump.

**4. Recovery.** The quadratic small-radius coefficient \(\pi/A\) recovers the area. The deficit from the universal-cover disk law vanishes before \(r_0\) and is strictly positive for every sufficiently small \(r>r_0\), by (6). Hence the first deviation radius recovers \(\ell\). Finally the strictly negative second-derivative jump recovers the positive integer \(k\). This completes the proof.

## Verification
The accompanying standard-library script `verify_hyperbolic_systole.py` checks two distinct exact formulas for hyperbolic disk-lens area: (i) integration of Fermi-coordinate slices and (ii) a formula using hyperbolic triangle angles. It then evaluates the cyclic orbital integral for three systolic lengths, compares its \(\varepsilon^2\) coefficient with \(2\pi\ell\) by Richardson extrapolation, and checks the jump normalization. A successful invocation prints `HYPERBOLIC_SYSTOLE_CHECK_OK`. These finite numerical tests corroborate local calculations; the argument above, rather than a finite experiment, proves the uniform statements for each fixed compact surface.

## Relationship to prior work
The geodesic length-spectrum/conjugacy-class unfolding in step 2 is classical: Borthwick's 2010 *Spectral Theory on Hyperbolic Surfaces* slides give a general Selberg trace-formula orbital integral. That result is **not** claimed as new. Thomson's 2012 *Short Geodesics in Hyperbolic Manifolds* studies the systole as a geometric invariant and constructs manifolds with short systoles. Golubev and Kamber's 2017 preprint *Cutoff on Hyperbolic Surfaces* studies concentration of distances for finite-area hyperbolic quotients, with a different large-area regime and no first-systole jump coefficient in its inspected theorems. The present statement combines a near-injectivity two-sheet occupancy identity with a hyperbolic tangency integral to relate the **ordinary two-point shortest-distance CDF** to systolic multiplicity. Its historical priority is provisional because generic trace-formula machinery may permit an equivalent reformulation in other sources.

## Limitations
The coefficient is local at the **first** deviation and does not assert that later singularities reconstruct the complete length spectrum. The theorem assumes a closed, connected, orientable surface of constant curvature \(-1\), not a cusped surface, orbifold, higher-dimensional manifold, or arbitrary variable-curvature metric. All bounds are surface-dependent, and the limiting calculation does not give a noise-stability guarantee for estimating \(F''\) from finite samples. The full history of equivalent spectral-geometric formulations has not been exhaustively verified; independent mathematical review remains outstanding.

## References
1. S. A. Thomson, *Short Geodesics in Hyperbolic Manifolds*, Durham University thesis (2012), institutional public record deposited 2012-06-01, https://etheses.durham.ac.uk/id/eprint/3604/ ; freely readable thesis copy https://w3.impa.br/~mbel/tese/SAThomson-Thesis-2012.pdf .
2. D. Borthwick, *Spectral Theory on Hyperbolic Surfaces*, July 2010 lecture slides, https://math.dartmouth.edu/~specgeom/Borthwick_slides.pdf , particularly the cyclic-conjugacy orbital integral calculation.
3. K. Golubev and A. Kamber, *Cutoff on Hyperbolic Surfaces*, first public arXiv preprint 2017-12-29, https://arxiv.org/abs/1712.10149 .
