# Strict isotropic-constant growth for intersections of regular arrays of disks

## Finding
Fix any integer \(n\ge3\). Let \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\), and for every \(0\le a<1\) set
\[
K_{n,a}=\bigcap_{j=0}^{n-1}\{x\in\mathbb R^2:\|x-av_j\|_2\le1\}.
\]
For a uniform area-distributed point \(X_{n,a}\) in \(K_{n,a}\), define the affine-invariant normalized covariance determinant
\[
L_{n,a}^4=\frac{\det\operatorname{Cov}(X_{n,a})}{\operatorname{area}(K_{n,a})^2}.
\]
**Theorem.** For every \(n\ge3\), the function \(a\mapsto L_{n,a}^4\) is continuous and strictly increasing on \([0,1)\). In particular, for \(0<a<1\), writing \(\alpha=\pi/n\),
\[
\boxed{\frac1{16\pi^2}<L_{n,a}^4<\frac{(1+\tan^2\alpha/3)^2}{16n^2\tan^2\alpha}.}
\]
The left equality occurs precisely at \(a=0\). The upper value is a sharp, unattained limit as \(a\uparrow1\): it is the isotropic constant of the regular \(n\)-gon with inradius one, which is the limit of \((1-a)^{-1}K_{n,a}\).

An exact finite-parameter profile is available. Define
\[
r_*=\sqrt{1-a^2\sin^2\alpha}-a\cos\alpha,\qquad
\beta=\arctan\!\left(\frac{r_*\sin\alpha}{a+r_*\cos\alpha}\right).
\]
Then the area \(A_{n,a}\) and the centroidal polar second moment \(J_{n,a}\) are
\[
\boxed{A_{n,a}=n(\beta-a\sin\beta),}
\]
\[
\boxed{J_{n,a}=\frac n2\bigl[(1+2a^2)\beta-(3a+a^3)\sin\beta+a^2\sin\beta\cos\beta\bigr],}
\]
and the full isotropic profile is \(L_{n,a}^4=J_{n,a}^2/(4A_{n,a}^4)\). The arctangent is the nonnegative principal value, well-defined for every specified \(n,a\).

## Assumptions and scope
All disks are closed Euclidean unit disks; all intersections are two-dimensional, contain the origin in their interiors, and are sampled by normalized planar Lebesgue area. All centers lie at the vertices of a regular \(n\)-gon with circumradius \(a\). The parameter \(a\) is the center radius divided by the disk radius, not an absolute length: similarity leaves \(L^4\) invariant. The family includes coincident centers at \(a=0\), but excludes the zero-area intersection at \(a=1\). The proof requires \(n\ge3\), because the rotational symmetry then forces scalar covariance; it does not claim the corresponding assertion for only two disk centers.

By \(n\)-fold rotational symmetry with \(n\ge3\), the centroid is the origin, the cross moment is zero, and \(\operatorname{Cov}(X_{n,a})=(J_{n,a}/(2A_{n,a}))I_2\). Here \(J_{n,a}=\int_{K_{n,a}}\|x\|^2\,dx\). Hence the normalization in the theorem is exactly \(J_{n,a}^2/(4A_{n,a}^4)\), not a perimeter-normalized mechanical inertia.

## Proof
**1. Exact radial reduction.** For a direction \(u_\theta=(\cos\theta,\sin\theta)\), set
\[
t(\theta)=-\min_{0\le j<n}\langle u_\theta,v_j\rangle.
\]
The nearest vertex direction to the antipode \(-u_\theta\) is within angle \(\pi/n\), so
\[
\cos(\pi/n)\le t(\theta)\le1.
\]
The function \(t(\theta)\) is continuous and nonconstant for every \(n\ge3\). A ray point \(r u_\theta\) belongs to every generating disk exactly when
\[
r^2-2ar\min_j\langle u_\theta,v_j\rangle+a^2\le1,
\]
or equivalently \(r^2+2at(\theta)r+a^2\le1\). Its positive endpoint is therefore
\[
\boxed{r_a(t)=\sqrt{1-a^2(1-t^2)}-at
=\frac{1-a^2}{\sqrt{1-a^2(1-t^2)}+at}.}
\]
All denominators are strictly positive for \(0\le a<1\), since \(t\ge\cos(\pi/n)>0\).

**2. A strict comonotone-covariance identity.** Write
\[
d_a(t)=\sqrt{1-a^2(1-t^2)},\quad q_a(t)=r_a(t)^2,\quad h_a(t)=\frac{\partial}{\partial a}\log q_a(t).
\]
Differentiating the positive implicit root (or the displayed radical) gives the two *exact* identities
\[
\frac{\partial}{\partial t}\log r_a(t)=-\frac a{d_a(t)},\qquad
\frac{\partial^2}{\partial a\partial t}\log r_a(t)=-\frac1{d_a(t)^3}.
\]
Thus for any \(0<a<1\), both \(q_a(t)\) and \(h_a(t)\) are strictly decreasing functions of \(t\), because \(\partial_t\log q_a=-2a/d_a<0\) and \(\partial_t h_a=-2/d_a^3<0\).

Let angular expectation \(\mathbb E_\theta\) mean integration over \([0,2\pi)\) against \(d\theta/(2\pi)\), and put \(M_p(a)=\mathbb E_\theta[r_a(t(\theta))^p]\) for \(p=2,4\). Polar integration, with no angular approximation, yields
\[
A_{n,a}=\pi M_2(a),\qquad J_{n,a}=\frac\pi2M_4(a),\qquad
L_{n,a}^4=\frac1{16\pi^2}\left(\frac{M_4(a)}{M_2(a)^2}\right)^2.
\]
Define a probability measure \(\nu_a\) on the angle circle by density \(q_a(t(\theta))/M_2(a)\) relative to uniform angle. Since \(\partial_a q_a=q_a h_a\), differentiation under the integral sign, valid on each compact subinterval of \([0,1)\), gives
\[
\frac d{da}\log\frac{M_4(a)}{M_2(a)^2}
=2\left[\frac{\mathbb E_{\nu_a}(q_a h_a)}{\mathbb E_{\nu_a}q_a}
-\mathbb E_{\nu_a}h_a\right]
=\frac{2\operatorname{Cov}_{\nu_a}(q_a,h_a)}{\mathbb E_{\nu_a}q_a}.
\]
This covariance is **strictly positive** for \(a>0\). Indeed, for two independent \(t,t'\) drawn from the induced nondegenerate distribution under \(\nu_a\),
\[
2\operatorname{Cov}_{\nu_a}(q_a,h_a)
=\mathbb E[(q_a(t)-q_a(t'))(h_a(t)-h_a(t'))]>0.
\]
Strict positivity follows because each bracket has the same strict sign whenever \(t\ne t'\), an event of positive probability: the angular parameter \(t(\theta)\) is nonconstant and the density of \(\nu_a\) is positive. Consequently \(M_4/M_2^2\), and therefore \(L^4\), strictly increases for \(0<a<1\). Continuity at \(a=0\), together with \(q_0\equiv1\), supplies strict increase on the closed-left half-open interval.

**3. Sharp endpoints.** At \(a=0\), \(K_{n,0}\) is the unit disk, with area \(\pi\), polar moment \(\pi/2\), and \(L_{n,0}^4=1/(16\pi^2)\). As \(a\uparrow1\), the exact radial expression gives the uniform limit
\[
\frac{r_a(t)}{1-a}=\frac{1+a}{d_a(t)+at}\longrightarrow\frac1t,
\quad\cos(\pi/n)\le t\le1.
\]
Uniform convergence holds since the denominator stays uniformly away from zero. The limiting radial body is the regular polygon
\[
P_n=\{x\in\mathbb R^2:\langle x,v_j\rangle\ge-1\ \text{for all }j\},
\]
whose inradius is one. Let \(\alpha=\pi/n\). On any of its \(n\) congruent angular sectors \(-\alpha\le\phi\le\alpha\), the radial function is \(\sec\phi\). Direct polar integration gives
\[
A(P_n)=\frac n2\int_{-\alpha}^{\alpha}\sec^2\phi\,d\phi=n\tan\alpha,
\]
\[
J(P_n)=\frac n4\int_{-\alpha}^{\alpha}\sec^4\phi\,d\phi
=\frac n2\tan\alpha\left(1+\frac{\tan^2\alpha}{3}\right).
\]
Substitution into \(J^2/(4A^4)\) gives the asserted sharp upper endpoint. Uniform radial convergence and positivity of area justify the limit of the normalized moment quotient. Strict monotonicity proves this endpoint is not reached for any finite \(a<1\).

**4. Independent exact circular-arc evaluation.** The boundary has \(n\) congruent arcs of radius one; their active generating centers are \(av_j\). The half-angle \(\beta\) of each active arc is determined by its meeting ray at angle \(\alpha\) from the opposite-center direction. Its endpoint radius is \(r_*\), and elementary right-triangle geometry gives the displayed arctangent formula. On one arc, with local parameter \(-\beta\le u\le\beta\), the outward unit normal is the radius-one vector, the boundary vector has squared norm \(1+a^2-2a\cos u\), and its outward normal flux \(x\cdot\nu\) equals \(1-a\cos u\).

Applying the divergence theorem to \(\operatorname{div}(x/2)=1\) and \(\operatorname{div}(\|x\|^2x/4)=\|x\|^2\) gives, respectively,
\[
A_{n,a}=\frac n2\int_{-\beta}^{\beta}(1-a\cos u)\,du,
\]
\[
J_{n,a}=\frac n4\int_{-\beta}^{\beta}(1+a^2-2a\cos u)(1-a\cos u)\,du.
\]
Elementary integration yields the exact displayed formulas for \(A_{n,a}\) and \(J_{n,a}\), independently of the strict-monotonicity calculation.

## Verification
The standalone program `verify.py` requires Python 3 and SymPy. Run `python verify.py` in the same folder as this document. It symbolically verifies the implicit radius equation, radical rationalization, and both critical logarithmic derivative identities. Separately, it evaluates the radial integrals from pointwise minimum over all generating disks and compares them with the boundary-arc formulas for seven polygon orders and six radii, including nearly degenerate intersections. It checks numerical strict ordering and polygon endpoint convergence as diagnostics. The performed run passed 151 symbolic and independent quadrature assertions. Finite sampling does not prove the quantified monotonicity; the proof is the covariance identity and strictly comonotone sign argument above.

## Relationship to prior work
Basit and Lángi, *Dowker-type theorems for disk-polygons in normed planes* (arXiv:2307.04026), investigate extremal disk-polygonal area and perimeter questions. A separate published result on *Unique optimal two-sided disk approximation within rotationally symmetric disk-polygons* explicitly uses this same family of regularly spaced disk centers and gives its radial root, but optimizes a weighted two-sided **area error** against a target disk; it does not state, bound, or order its normalized covariance determinant. The published *Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks* treats area of arbitrary arrangements and its stochastic fluctuations, not their polar second moments. The published *Polar moment and isotropic constant of regular Reuleaux odd-gons* computes the invariant for a discrete constant-width family rather than a strict order for all regular center radii. Bezdek's work on intersections of congruent balls concerns intrinsic volumes, which likewise do not determine the normalized covariance determinant. The exact low-level radial identity is an ingredient available in earlier literature, not presented as new; the all-radius strict covariance ordering, universal sharp endpoint hierarchy at fixed \(n\), and comonotone-score proof are the claims advanced here.

## Limitations
The theorem covers congruent Euclidean disks with equally spaced centers and \(n\ge3\). It does not cover arbitrary center placements, unequal radii, three-dimensional lenses or higher-dimensional ball intersections. The limiting polygon is obtained only after rescaling; at \(a=1\) the original intersection has zero area, so its isotropic constant is not defined. The normalizations are Euclidean and use area-uniform interiors, not boundary-uniform data. The claim is proved analytically, but the present novelty assessment cannot rule out inaccessible or unindexed historical mechanical-inertia calculations, including older studies of many-disk intersections. Independent mathematical audit has not been performed.

## References
1. B. Basit and Z. Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026 (first posted 8 July 2023). https://arxiv.org/abs/2307.04026
2. K. Bezdek, *On the intrinsic volumes of intersections of congruent balls*, arXiv:1810.11886. https://arxiv.org/abs/1810.11886
3. J. Kratky, *The area of intersection of n equal circular disks*, Journal of Physics A 11 (1978), DOI:10.1088/0305-4470/11/6/006. https://doi.org/10.1088/0305-4470/11/6/006
4. *Unique optimal two-sided disk approximation within rotationally symmetric disk-polygons*, publicly accessible mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-unique-optimal-two-sided-disk-approximation-within-rotationally--f77924764139/RESULT.md
5. *Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks*, publicly accessible mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-circular-gap-area-laws-and-gaussian-fluctuations-for-inter--1c25b18e16e8/RESULT.md
6. *Polar moment and isotropic constant of regular Reuleaux odd-gons*, publicly accessible mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-polar-moment-and-isotropic-constant-of-regular-reuleaux-odd-gons--43279757dfc9/RESULT.md
