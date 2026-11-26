# Complete central-section polygon law and unique pentagon optimum for equilateral triangular prisms

## Finding
Let \(T\subset\mathbb R^2\) be an equilateral triangle of circumradius \(R>0\), centered at the origin, and let \(P_h=T\times[-h,h]\) be the right prism with half-height \(h>0\). For an unoriented Haar-uniform plane through the origin, let \(N_h\) be the number of vertices of its intersection with \(P_h\). Put \(t=h/R\), and define
\[
\gamma(t)=\arccos\!\left(\frac{t^2+1/2}{1+t^2}\right),\qquad
\beta(t)=\arccos\!\left(\frac{t^2-1/2}{1+t^2}\right),
\qquad
\mu(t)=\frac6\pi(\arctan t+\beta(t)).
\]
Then, for every \(t>0\), the section has exactly \(3\), \(4\), or \(5\) vertices almost surely, with the **complete exact distribution**
\[
\begin{aligned}
\Pr(N_h=3)&=p_3(t)=1-\frac3\pi\gamma(t),\\
\Pr(N_h=4)&=p_4(t)=5-\mu(t)-2p_3(t),\\
\Pr(N_h=5)&=p_5(t)=\mu(t)-4+p_3(t).
\end{aligned}
\]
The probability of a **pentagonal central section** has precisely one global maximizing aspect ratio \(t_*\in(0,\infty)\). It is the unique positive solution of
\[
1+\frac{t}{\sqrt{4t^2+3}}-\frac{2\sqrt3\,t}{\sqrt{4t^2+1}}=0.
\]
Numerically, \(t_*=0.53146955106361\ldots\), corresponding to total-height-to-base-side ratio \(2t_*/\sqrt3=0.61368817674533\ldots\); the maximum pentagon probability is \(p_5(t_*)=0.38515580567418\ldots\). Moreover \(p_3\) is strictly increasing, with limits \(0\) and \(1\) at \(t=0\) and \(t=\infty\). Thus a sharp intermediate prism height optimizes pentagonal sections while very thin prisms favor quadrilateral sections and very tall prisms favor triangles.

## Assumptions and scope
The prism is closed, Euclidean, right, and has a nondegenerate equilateral base. The section plane passes through the center of mass \((0,0,0)\) and is sampled by choosing a unit normal uniformly on \(\mathbb S^2\), identifying opposite normals. The probabilities concern the number of **genuine polygon vertices**, rather than the number of polygon sides counted with multiplicity. Planes through a vertex or an entire prism edge form a measure-zero exceptional set. The result is not a claim about random translated planes, noncentral sections, arbitrary triangular bases, or planar silhouettes.

## Proof
**1. Face and edge incidence.** Write the three planar base vertices as \(r_i=R(\cos(2\pi i/3),\sin(2\pi i/3))\), for \(i=0,1,2\), so \(\sum_i r_i=0\). The six prism vertices are \(v_i^\pm=(r_i,\pm h)\). By reversing the normal if necessary, assume its vertical component is positive. Put \(s=h u_3>0\) and \(x_i=\langle u_{1:2},r_i\rangle\), so \(\sum_i x_i=0\). Let \(k_+\) count the positive numbers \(x_i+s\) and \(k_-\) count the positive numbers \(x_i-s\). We have \(k_+\ge k_-\), \(1\le k_+\le3\), and \(0\le k_-\le2\). The pairs \((1,0)\) and \((3,2)\) cannot occur: the former would force two \(x_i<-s\) while the remaining \(x_j<s\), contradicting \(\sum_i x_i=0\); the latter is the sign-reversed argument. Thus the possibilities are exactly \((1,1),(2,2),(2,1),(2,0),(3,1),(3,0)\).

A plane cuts two edges of one of the triangular end faces exactly when that face has both positive and negative vertex signs. It cuts exactly \(k_+-k_-\) of the three vertical edges. Consequently
\[
N_h=2\mathbf1_{\{k_+\in\{1,2\}\}}+2\mathbf1_{\{k_-\in\{1,2\}\}}+k_+-k_-.
\]
The listed pairs give, respectively, \(4,4,5,4,4,3\) vertices. In particular, the section is triangular exactly when all top vertices are on one side and all bottom vertices are on the other:
\[
N_h=3\quad\Longleftrightarrow\quad s>\max_i|x_i|.
\]
All equivalences hold outside the excluded measure-zero degeneracies.

**2. Spherical area of the triangular-section normal cone.** In the upper hemisphere, the last condition is the intersection of the six strict hemispheres \(h u_3>\pm\langle r_i,u_{1:2}\rangle\). The corresponding cone has a regular spherical hexagon as its intersection with the unit sphere. Adjacent bounding planes have outward normals at angle \(\gamma(t)\), since the six horizontal normals \(\pm r_i\) occur at successive angles \(\pi/3\), and
\[
\cos\gamma(t)=\frac{h^2+R^2/2}{h^2+R^2}=\frac{t^2+1/2}{t^2+1}.
\]
Each spherical interior angle equals \(\pi-\gamma(t)\). The spherical excess formula gives area \(\Omega(t)=6(\pi-\gamma(t))-4\pi=2\pi-6\gamma(t)\). The upper and lower triangular-section normal cones have equal area. Dividing their combined area by \(4\pi\) gives \(p_3(t)=\Omega(t)/(2\pi)=1-3\gamma(t)/\pi\), as asserted. Differentiation yields
\[
p_3'(t)=\frac{6t}{\pi(1+t^2)\sqrt{4t^2+3}}>0.
\]

**3. Expected section complexity.** For two nonzero vectors \(a,b\in\mathbb R^3\), a Haar-uniform plane through the origin separates their endpoints with probability \(\angle(a,b)/\pi\): the separating normals form two spherical lunes, with combined area \(4\angle(a,b)\). Every edge crossing corresponds to one genuine section vertex almost surely. The three vertical prism edges have endpoint angle \(2\arctan t\); the six end-face edges have endpoint angle \(\beta(t)\). Thus
\[
\mathbb E[N_h]=\frac{3(2\arctan t)+6\beta(t)}\pi=\mu(t).
\]
Because the only polygon types are \(3,4,5\), the equations \(p_3+p_4+p_5=1\) and \(3p_3+4p_4+5p_5=\mu\) yield \(p_5=\mu-4+p_3\) and \(p_4=5-\mu-2p_3\). This proves the entire probability law.

**4. Optimal height.** Direct differentiation of these exact expressions gives
\[
p_5'(t)=\frac{6}{\pi(1+t^2)}\left[1+\frac{t}{\sqrt{4t^2+3}}-\frac{2\sqrt3\,t}{\sqrt{4t^2+1}}\right].
\]
Let the bracket be \(F(t)\). Then
\[
F'(t)=\frac3{(4t^2+3)^{3/2}}-\frac{2\sqrt3}{(4t^2+1)^{3/2}}<0
\]
for all \(t\ge0\), since the first numerator is smaller and its denominator larger. Also \(F(0)=1\) and \(\lim_{t\to\infty}F(t)=3/2-\sqrt3<0\). The intermediate value theorem and strict monotonicity therefore give exactly one critical point, with \(p_5\) strictly increasing before it and strictly decreasing after it. The numerical values above are reproducible by one-dimensional root finding in `checker.py`; uniqueness and global optimality are analytical.

## Verification
Run `python checker.py` with NumPy and SciPy. It evaluates the exact probability formulas at five different aspect ratios, generates independent standard-normal orientation vectors, counts intersections using all nine actual prism edges, and compares empirical frequencies against the expressions. It also checks the mean identity, normalization, the unique positive root numerically, the strict negative derivative of \(F\) on a dense scale-spanning grid, and the strict numerical inequality for sampled off-optimum aspect ratios. The checker successfully passed all its assertions on the saved package; its finite computations are consistency checks, not substitutes for the spherical-excess, edge-angle, and monotonicity proofs.

## Relationship to prior work
Ambrus, *Critical central sections of the cube* (arXiv:2107.14778, 2021), analyzes volume-critical central hyperplane sections of cubes, especially in dimensions three and four. Its main theorems concern critical directions for section volume, not the number of vertices of Haar-random central sections of triangular prisms. Konstantinova and Shchur, *Algorithm for Density of Angle Distribution in Random Sections of Polyhedron* (2023 preprint / 2024 journal), explicitly include triangular-prism examples in a numerical study of random section-angle densities. The available description does not establish the present **orientation-uniform, centroid-fixed polygon-type distribution**, or the analytical unique-height extremum; full text could not be inspected. Heerten, Hübner, and Thäle, *Vertex number of the typical cell in a tri-directional Poisson line tessellation* (arXiv:2309.12771, 2023), give polygon-count probabilities for a different planar random-line model, not these fixed-solid central sections.

## Limitations
This theorem concerns the specified orientation-Haar distribution only. It does not determine random section areas, edge lengths, interior angles, or offsets; it does not treat non-equilateral or oblique prisms. The verified theorem is analytic, while the decimal approximations use numerical root solving. Related numerical random-plane studies create a residual bibliographic risk because their complete content was unavailable; no claim of exhaustive worldwide novelty is made. The mathematical argument and checker have not undergone independent external validation.

## References
1. G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778 (first public version July 30, 2021), especially Theorems 1–3, DOI-linked published version in *Proceedings of the American Mathematical Society*.
2. L. N. Shchur and E. P. Konstantinova, *Algorithm for Density of Angle Distribution in Random Sections of Polyhedron*, SSRN 4485810, DOI:10.2139/ssrn.4485810 (2023); *Expert Systems with Applications* **235** (2024), 121195, DOI:10.1016/j.eswa.2023.121195.
3. N. Heerten, J. Hübner, and C. Thäle, *Vertex number of the typical cell in a tri-directional Poisson line tessellation*, arXiv:2309.12771 (September 22, 2023).
