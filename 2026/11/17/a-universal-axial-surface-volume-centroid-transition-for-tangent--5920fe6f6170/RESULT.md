# A universal axial surface–volume centroid transition for tangential frusta

## Finding

Let \(d\ge2\) be an integer and \(m=d-1\). For every convex \(m\)-polytope \(B\subset\mathbb R^m\) circumscribed about a ball of radius \(R>0\) centered at the origin, form the right homothetic frustum
\[
K_{a,H}=\{(s x,zH):x\in B,\ 0\le z\le1,\ s=1-(1-a)z\},
\qquad 0<a<1,\quad H>0.
\]
Let \(c_V\) denote the centroid of uniform \(d\)-dimensional volume and \(c_S\) the centroid of the **entire** boundary, including both end caps, with ordinary Euclidean surface-area measure. A centroid's axial coordinate is its final coordinate. Define
\[
I_j(a)=\int_0^1[1-(1-a)z]^j\,dz,\qquad
J_j(a)=\int_0^1z[1-(1-a)z]^j\,dz,
\]
\[
v=J_m/I_m,\quad \ell=J_{m-1}/I_{m-1},\quad
T_d(a)=\frac{v(1+a^m)-a^m}{m I_{m-1}(\ell-v)},\quad
h_d(a)=\sqrt{T_d(a)^2-(1-a)^2}.
\]
The fractions are well defined and \(T_d(a)>1-a\). For every height, the **complete and exclusive** axial sign classification is
\[
\operatorname{sgn}((c_S)_z-(c_V)_z)
=\operatorname{sgn}(H/R-h_d(a)).
\]
The height threshold depends on \(d\) and \(a\) but not on the combinatorial or metric shape of \(B\) beyond its inradius. The same calculation applies to a ball as base, giving circular conical frusta in arbitrary dimension. No assertion is made that the full centroid vectors coincide when their axial components coincide.

The continuous taper-endpoint laws are
\[
h_d(0)=\sqrt{d^2-1},\qquad
h_d(a)=4-2(1-a)+O_d((1-a)^2)\quad(a\uparrow1).
\]
For \(d=2\), the exact expression \(h_2(a)=\sqrt{(a+3)(3a+1)}\) is strictly increasing. In every dimension \(d\ge3\),
\[
h_d'(0+)=-\sqrt{d^2-1}<0,\qquad
\lim_{a\uparrow1}h_d'(a)=2>0.
\]
Consequently each such dimension has at least one global minimizer at a strict intermediate taper; its critical height is smaller than at either endpoint. Uniqueness of the minimizer is **not** asserted.

## Assumptions and scope

The base is a full-dimensional bounded convex polytope with all facets tangent to the same inscribed Euclidean sphere of radius \(R\); the homothety is about its incenter, and the segment joining corresponding incenter positions is perpendicular to the base. Both complete-boundary and volume distributions have constant density in their intrinsic measures. The smaller base has positive radius ratio \(a\in(0,1)\), not necessarily a polygon with any symmetry. The asserted equality concerns **only axial coordinates**, since an asymmetric base may have nonzero transverse centroid. Formulas at \(a=0\) and \(a=1\) are parameter limits, with the prism case described separately.

## Proof

**1. Volume and surface moments.** Write \(b=1-a\) and \(t=H/R\), and put \(s(z)=1-bz\). The \(m\)-volume of the horizontal slice is \(|B|s(z)^m\), hence
\[
(c_V)_z/H=\frac{J_m}{I_m}=v.
\]
Since every base facet has supporting distance \(R\) from the incenter, the divergence theorem yields \(R\,\mathcal H^{m-1}(\partial B)=m|B|\). Under the ruled frustum construction, a lateral hypersurface strip at normalized height \(z\) has area
\[
R\sqrt{t^2+b^2}\,\mathcal H^{m-1}(\partial B)\,s(z)^{m-1}\,dz
=m|B|\sqrt{t^2+b^2}\,s(z)^{m-1}\,dz.
\]
Each facet has the same slant multiplier because its support plane is tangent to the common sphere. The lower cap has area \(|B|\) at zero height, and the upper cap has area \(a^m|B|\) at height \(H\). It follows that
\[
\frac{(c_S)_z}{H}=
\frac{a^m+m\sqrt{t^2+b^2}\,J_{m-1}}
{1+a^m+m\sqrt{t^2+b^2}\,I_{m-1}}
=\frac{a^m+U\sqrt{t^2+b^2}\,\ell}
{1+a^m+U\sqrt{t^2+b^2}},\quad U=mI_{m-1}.
\]
The identical formulas for a Euclidean ball base follow from its surface-to-volume identity and radial slope.

**2. Existence, positivity, and sign.** Because \(s\) is strictly decreasing, weighting the probability distribution proportional to \(s^{m-1}\) by the extra factor \(s\) strictly decreases its mean in \(z\). Thus \(\ell-v>0\). Also \(v(1+a^m)-a^m>0\): multiplying by \(I_m\), this is \(J_m-a^m(I_m-J_m)>0\), because \(J_m>a^m/2\) and \(I_m-J_m<1/2\). Rearrangement of the two centroid formulae gives
\[
\operatorname{sgn}((c_S)_z-(c_V)_z)
=\operatorname{sgn}\left(U(\ell-v)\sqrt{t^2+b^2}-[v(1+a^m)-a^m]\right),
\]
which is the sign of \(\sqrt{t^2+b^2}-T_d(a)\).

To see \(T_d(a)>b\) **strictly**, integrate by parts:
\[
mbI_{m-1}=1-a^m,\qquad mbJ_{m-1}=I_m-a^m.
\]
At the formal collapsed-height value \(t=0\), the surface centroid formula is \((c_S)_z/H=I_m/2\), whereas the volume formula is \(J_m/I_m\). Let \(X\) be a random variable on \([0,1]\) with \(\mathbb P(X\ge z)=s(z)^m\) for \(0\le z<1\), and a terminal atom of size \(a^m\) at \(1\). Its first two moments are \(\mathbb E X=I_m\) and \(\mathbb E X^2=2J_m\). Since \(0<a<1\), \(X\) is nondegenerate; hence \(2J_m>I_m^2\). Thus the collapsed-height surface value is strictly smaller than the volume value. Equivalently \(T_d(a)>b\), proving a unique strictly positive crossing at \(t=h_d(a)\). Strict monotonicity of the square root completes the trichotomy.

**3. Endpoints and dimensional bifurcation.** At \(a=0\), the elementary values \(I_j=1/(j+1)\) and \(J_j=1/[(j+1)(j+2)]\) give \(T_d(0)=d\), so \(h_d(0)=\sqrt{d^2-1}\). This is the known pyramidal boundary–volume balancing threshold, cited as prior work below. For \(d=2\), direct integration gives \(T_2(a)=2(1+a)\), and therefore \(h_2(a)^2=(3+a)(1+3a)\).

For \(d\ge3\), put \(m=d-1\ge2\). Direct differentiation of the defining integrals at \(a=0\) gives \(I_j'(0)=I_j(0)\) and \(J_j'(0)=2J_j(0)\) for every integer \(j\ge1\). Consequently \(v'(0)=v(0)\), \(\ell'(0)=\ell(0)\), \(U'(0)=U(0)\), while \((a^m)'|_{a=0}=0\). Taking the logarithmic derivative of \(T_d\) shows \(T_d'(0)=-T_d(0)=-d\), and differentiating its square-root formula gives \(h_d'(0+)=-\sqrt{d^2-1}\).

Finally write \(b=1-a\downarrow0\). Binomial integration yields, for every fixed integer \(j\ge0\),
\[
I_j=1-\frac j2b+\frac{j(j-1)}6b^2+O_j(b^3),\quad
J_j=\frac12-\frac j3b+\frac{j(j-1)}8b^2+O_j(b^3).
\]
Including the next coefficient in these finite polynomials and substituting into \(T_d\) gives
\[
\ell-v=\frac b{12}+\frac{b^2}{24}+O_d(b^3),\quad
v(1+a^m)-a^m=\frac{mb}{3}-\frac{m(m-1)b^2}{6}+O_d(b^3),
\]
\[
mI_{m-1}=m\left(1-\frac{m-1}{2}b+O_d(b^2)\right),\quad
T_d(a)=4-2b+O_d(b^2).
\]
Since \(h_d=\sqrt{T_d^2-b^2}\), the same two leading terms hold for \(h_d\). The functions are algebraic/analytic near both parameter endpoints after cancellation of removable factors, so the differentiated remainder estimates are valid. As \(h_d'(a)\) is negative immediately after zero and positive just before one, its global minimum on the compact extended interval occurs at an interior point; its value is strictly below both endpoint values.

## Verification

The accompanying `verify.py` independently evaluates the defining integrals by exact rational polynomial integration, checks the sign of the centroid displacement at positive heights on both sides of the predicted threshold, and checks the endpoint identities, three-dimensional closed form, and limiting expansions over multiple dimensions. It is executable using the Python standard library alone. These checks are finite consistency tests; the statements for all dimensions and all frusta are proved by the symbolic argument above.

## Relationship to prior work

Tokmachev (2026) studies convex-order comparisons between random interior and boundary points for bodies with coincident centroids; that result does not determine the axial center-of-mass crossing of tapered frusta when the two centroids are generally distinct. The global sharp centroid-distance inequality of Myroshnychenko, Ryabogin, Tatarko and Yaskin (2026) applies to all convex bodies, but does not give the present frustum-specific equality threshold or the dimension-dependent taper response. The pyramidal endpoint \(a=0\) is already covered by the published result “Sharp dimension-six transition for boundary–volume centroid separation in tangential-base pyramids”; only the strict-taper all-dimensional transition, its base-shape universality and taper phase behavior are put forward here as new. Classical conical-frustum centroid formulas determine individual solid or lateral-shell centroids, not this complete-boundary crossing theorem.

## Limitations

This is an **axial** centroid comparison, not full-vector equality or a universal centroid distance bound. The base must be tangential with a common incenter; unrelated homothetic bases need not have a common slant multiplier. At exactly \(a=1\), a prism's axial surface and volume centroids always agree, so the finite near-prism critical-height limit is a singular parameter limit and not a prism threshold. The existence, but not uniqueness or exact location, of interior taper minimizers is proved. Historical originality remains provisional in the presence of possible unindexed engineering centroid formulas; no independent external mathematical audit was performed.

## References

- A. S. Tokmachev, “Inequalities for convex functions of random points inside and on the boundary of convex bodies,” arXiv:2607.08869v1 (July 9, 2026), https://arxiv.org/abs/2607.08869.
- S. Myroshnychenko, D. Ryabogin, K. Tatarko, and V. Yaskin, “The sharp bound on the distance between the centers of mass of a convex body and its boundary,” arXiv:2611.11635v1 (November 8, 2026), https://arxiv.org/html/2611.11635v1. This manuscript is cited for comparison only and postdates the November 8, 2026 00:00 UTC literature cutoff.
- “Sharp dimension-six transition for boundary–volume centroid separation in tangential-base pyramids,” publicly archived earlier result, https://github.com/published-finding corpus/2026 (pyramidal endpoint only).
- Wolfram MathWorld, “Conical Frustum,” https://mathworld.wolfram.com/ConicalFrustum.html (classical solid-frustum formulas).
