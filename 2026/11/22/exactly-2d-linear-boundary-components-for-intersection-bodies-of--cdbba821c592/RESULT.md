# Exactly \(2d\) linear boundary components for intersection bodies of cubes

## Finding

**Theorem.** Let \(d\ge2\), \(Q_d=[-1,1]^d\subset\mathbb R^d\), and let its intersection body be defined by the radial function
\[
\rho_{IQ_d}(v)=\mathcal H^{d-1}(Q_d\cap v^\perp),\qquad \|v\|_2=1.
\]
Then the complete list of facets of \(IQ_d\) is
\[
F_i^\pm=\left\{x\in\mathbb R^d:x_i=\pm2^{d-1},\quad\sum_{j\ne i}|x_j|\le2^{d-1}\right\},\quad i=1,\dots,d.
\]
Every one is a \((d-1)\)-dimensional crosspolytope (an interval in dimension two). There are no other flat \((d-1)\)-dimensional patches, and **the real algebraic boundary has exactly \(2d\) irreducible linear components**. In particular this proves the equality conjectured, after the previously known lower bound, in [1, Section 6].

The same count and facet classification hold for every *origin-centered parallelotope* \(P=AQ_d\) with \(A\in GL_d(\mathbb R)\), using the affine covariance
\[
I(AQ_d)=|\det A|A^{-T}(IQ_d).
\]
The theorem is a single structural classification, not an assertion about the nonlinear components of the algebraic boundary.

## Assumptions and scope

All volumes and hyperplane measures are ordinary Euclidean measures; \(\mathcal H^{d-1}\) is Hausdorff \((d-1)\)-measure. The intersection body is centered at the origin and is full dimensional. Its *real algebraic boundary* means the \(\mathbb R\)-Zariski closure of its Euclidean boundary. A linear component means an irreducible component that is a full affine hyperplane, not an algebraic factor introduced by clearing denominators. The classification is for every integer dimension \(d\ge2\), not merely the previously enumerated low dimensions. Translated parallelotopes with the origin away from their symmetry center are not included.

## Proof

**1. Density and exact boundary parametrization.** Let \(U_1,\dots,U_d\) be independent uniform random variables on \([-1,1]\), and let \(f_u\) denote the density at zero of \(\sum_j u_jU_j\) for \(u\ne0\). The coarea formula gives
\[
f_u(0)=\frac{\mathcal H^{d-1}(Q_d\cap u^\perp)}{2^d\|u\|_2}.
\]
Since \(f_{tu}(0)=t^{-1}f_u(0)\) for \(t>0\), the map
\[
X(u)=2^d f_u(0)u,\qquad u\in\mathbb R^d\setminus\{0\},
\]
parametrizes \(\partial IQ_d\) radially and satisfies \(X(tu)=X(u)\). The body \(IQ_d\) is convex, by the classical Busemann theorem for centered symmetric convex bodies; convexity can also be used just to identify the sets below as its facets.

**2. The facets exist and are exactly crosspolytopes.** Fix \(i\) with \(u_i>0\), and write \(S=\sum_{j\ne i}u_jU_j\). Conditioning on \(S\) yields the identity
\[
u_i f_u(0)=\tfrac12\Pr\{|S|\le u_i\}.
\]
(The equality at an endpoint does not matter because the distribution of \(S\) is continuous unless \(S\equiv0\), in which case the identity holds directly.) Therefore \(X_i(u)\le2^{d-1}\), with equality exactly when \(u_i\ge\sum_{j\ne i}|u_j|\). The assertion about equality uses the fact that a sum of nondegenerate independent uniform variables has a strictly positive density throughout the interior of its support. Changing signs gives \(|X_i(u)|\le2^{d-1}\), and equality exactly for \(|u_i|\ge\sum_{j\ne i}|u_j|\). For such a direction,
\[
X(u)=\frac{2^{d-1}}{|u_i|}u.
\]
The radial images of these closed dominance cones are precisely the claimed \(F_i^\pm\), since their coordinate ratios range over the closed unit \(\ell_1\)-ball in the remaining \(d-1\) coordinates. These are genuine exposed facets with nonempty relative interiors.

**3. The polynomial-denominator obstruction.** It remains to exclude a *different* hyperplane component. Coordinate sign changes preserve the cube and its intersection body, so on any prescribed open sign orthant we may write all \(u_j>0\). Set \(T=\sum_j u_j\). Repeated convolution of the interval densities (equivalently, inclusion-exclusion for the sum of independent uniforms on \([0,u_j]\)) gives the exact truncated-power identity
\[
f_u(0)=\frac{1}{2(d-1)!\prod_j u_j}
\sum_{J\subseteq[d]}(-1)^{|J|}
\left(\frac T2-\sum_{j\in J}u_j\right)_+^{d-1}.
\tag{1}
\]
To derive it, note that the density of the sum of independent uniforms on \([0,u_j]\) is obtained by applying the finite difference operators \(1-\tau_{u_j}\) to \(t_+^{d-1}/((d-1)!\prod u_j)\), then substitute the change of variables \(U_j=2V_j/u_j-1\). The factor \(1/2\) in (1) is the Jacobian at zero.

Delete from the positive orthant the finitely many hyperplanes \(T/2=\sum_{j\in J}u_j\). On each resulting nonempty open chamber \(C\), each positive-part choice is fixed, so (1) becomes
\[
f_u(0)=\frac{P_C(u)}{2(d-1)!\prod_j u_j},
\]
where \(P_C\) is a homogeneous real polynomial of degree \(d-1\). Its values are positive on \(C\).

Suppose the image \(X(C)\) lies in some affine hyperplane \(\ell(x)=1\), with \(\ell\) a nonzero linear functional. Then
\[
2^d\ell(u)f_u(0)=1\quad(u\in C),
\]
so polynomial identity on the nonempty open set \(C\) gives
\[
\ell(u)P_C(u)=\frac{(d-1)!}{2^{d-1}}\prod_{j=1}^d u_j
\quad\text{identically on }\mathbb R^d.
\tag{2}
\]
Unique factorization in the real polynomial ring forces the nonzero linear polynomial \(\ell\) to be a scalar multiple of **one coordinate** \(u_i\): it must divide the square-free product on the right. This is the crucial obstruction to a slanted planar patch.

In that event (2) requires \(u_if_u(0)\) to be constant throughout \(C\). But for the other coordinates fixed and positive, the conditional identity from step 2 is strictly increasing in \(u_i\) throughout the interval
\[
0<u_i<\sum_{j\ne i}u_j,
\]
because the density of \(S\) is positive on its entire open support. Since \(C\) is open, this is incompatible with constancy at any nondominant direction. Thus \(C\) must lie in the dominance cone \(u_i>\sum_{j\ne i}u_j\); there \(f_u(0)=1/(2u_i)\), and \(\ell(X(u))=1\) forces \(\ell(x)=x_i/2^{d-1}\). Sign changes yield only the \(2d\) coordinate hyperplanes already found.

**4. Why this also classifies algebraic boundary components.** The above open chambers, over all coordinate orthants, are finitely many semialgebraic cones. On each, \(X(u)\) is rational, and its image has dimension \(d-1\) because radial projection gives a homeomorphism between a spherical open chamber and the corresponding open boundary patch. The real-Zariski closure of a rational image of a nonempty open part of affine space is irreducible: a product of two polynomials cannot vanish identically on that image unless one polynomial does. Images of the omitted hyperplane-arrangement walls have semialgebraic dimension at most \(d-2\). Consequently every \((d-1)\)-dimensional irreducible component of the algebraic boundary, in particular every hyperplane component, is the Zariski closure of at least one open chamber image. Step 3 shows such a component is a hyperplane only in one of the \(2d\) coordinate cases. Hence there are exactly \(2d\) linear irreducible components, not merely \(2d\) known exposed faces.

**5. Affine covariance.** For \(A\in GL_d(\mathbb R)\), the \((d-1)\)-Jacobian of \(A\) on the hyperplane perpendicular to \(A^Tv\) is \(|\det A|\|v\|_2/\|A^Tv\|_2\). Substitution in the radial definition gives \(\rho_{I(AK)}(v)=|\det A|\rho_{IK}(A^Tv)\), using homogeneous extension of the radial function. This is exactly \(I(AK)=|\det A|A^{-T}IK\). Invertible affine-linear images preserve the number and dimension of algebraic components and carry the stated facets to those of a centered parallelotope. \(\square\)

## Verification

The analytic proof is all-dimensional. The accompanying standalone \`verify.py\` independently evaluates the exact rational density (1) in dimensions two through seven, checks the dominance characterization and component offsets for rational normals, and compares the coarea normalization against explicit three-dimensional polygon sections obtained from cube-edge intersections. The script uses only Python's standard library; run \`python verify.py\`. It passed 7,741 deterministic exact or geometric assertions. These finite checks are diagnostic only and are not substituted for unique factorization or the semialgebraic dimension argument.

## Relationship to prior work

Berlow, Brandenburg, Meroni and Shankar [1], Proposition 6.1, established **at least** \(2d\) linear components of the algebraic boundary of \(IQ_d\) and explicitly conjectured **exactly** \(2d\). Their computations addressed dimensions at most five. Their subsequent correction [2] changed the normalization of some formulas and supplied corrected lower-dimensional examples; the present independent density normalization is consistent with the corrected coordinate facet offsets \(4\) in dimension three and \(8\) in dimension four. Brandenburg and Meroni [3] study translated polytopes and convexity conditions, not the all-dimensional count. The truncated-power density formula and Busemann convexity theorem are classical ingredients, not claimed as discoveries here. The contribution is the all-dimensional *exclusion* of every other linear algebraic boundary component, including the exact crosspolytope facet sets.

## Limitations

This does not enumerate or give degrees for the nonlinear algebraic boundary components, nor classify the facets of intersection bodies of arbitrary centrally symmetric polytopes or off-center parallelotopes. The priority comparison includes accessible published source texts and indexed research summaries; a previously unindexed equivalent proof cannot be ruled out. No independent audit has been performed.

## References

[1] K. Berlow, M.-C. Brandenburg, C. Meroni and I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996 (first public posting 2021-10-12), Beiträge zur Algebra und Geometrie 63 (2022), 419–439. https://arxiv.org/abs/2110.05996 ; https://doi.org/10.1007/s13366-022-00621-7 . See Section 6, Proposition 6.1 and following conjecture.

[2] Same authors, *Correction to: Intersection bodies of polytopes*, Beiträge zur Algebra und Geometrie 63 (2022), 441–443. https://doi.org/10.1007/s13366-022-00638-y .

[3] M.-C. Brandenburg and C. Meroni, *Intersection Bodies of Polytopes: Translations and Convexity*, arXiv:2302.11764 (first public posting 2023-02-23), Journal of Algebraic Combinatorics 60 (2024), 127–143. https://arxiv.org/abs/2302.11764 .
