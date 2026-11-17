# A two-parameter endpoint–midpoint phase law for random parabolic tangent triangles

## Finding

Let \(p,q>0\), and sample \(T_1,T_2,T_3\) independently on \([-1,1]\) with density
\[
 f_{p,q}(t)=\frac{|t|^{q-1}(1-t^2)^{p-1}}{B(q/2,p)}\quad(-1<t<1).
\]
Draw the tangent lines \(\ell_t:y=2tx-t^2\) to \(y=x^2\) at the three sampled parameters. Let \(A\) denote the unsigned Euclidean area of their intersection triangle. Its maximum possible value is \(1/2\). Set \(d=2p+q/2\) and
\[
 K_{p,q}=\frac{6\,2^{2p-2+q/2}(4/3)^{2p}\,\Gamma(p)^2\Gamma(q/2)}{B(q/2,p)^3\,\Gamma(d+1)}.
\]
Then the sharp endpoint-area law is
\[
 \boxed{\Pr(A>1/2-\varepsilon)\sim K_{p,q}\varepsilon^{d}}
 \qquad(\varepsilon\downarrow0).
\]
The two independent sampling exponents govern distinct geometric scales: tangency parameters near both endpoints approach them at order \(\varepsilon\), whereas the central parameter approaches zero at order \(\sqrt\varepsilon\). In particular, changing a midpoint sampling exponent by one changes the upper-area tail exponent by one half, rather than by one.

There is a joint **total-variation** marked limit. Write the ordered parameters as \(a<b<c\), set
\[
 U_\varepsilon=\frac{3(a+1)}{4\varepsilon},\qquad
 V_\varepsilon=\frac{3(1-c)}{4\varepsilon},\qquad
 Y_\varepsilon=\frac{b}{\sqrt{2\varepsilon}},\qquad
 Z_\varepsilon=1-U_\varepsilon-V_\varepsilon-Y_\varepsilon^2.
\]
Conditionally on \(A>1/2-\varepsilon\), the joint law of \((U_\varepsilon,V_\varepsilon,Y_\varepsilon)\) converges in total variation to the density
\[
 \boxed{\frac{\Gamma(d+1)}{\Gamma(p)^2\Gamma(q/2)}u^{p-1}v^{p-1}|y|^{q-1}\,\mathbf1\{u>0,v>0,u+v+y^2<1\}.}
\]
Equivalently, in the limit, \((U,V,Y^2,1-U-V-Y^2)\) is \(\operatorname{Dirichlet}(p,p,q/2,1)\), and the sign of \(Y\) is an independent fair sign. The normalized deficit \((1/2-A)/\varepsilon\), under this conditioning, tends to \(\operatorname{Beta}(d,1)\). At \(p=q=1\) the coefficient specializes to \(32\sqrt2/45\); the distinct two-parameter exponent-and-mark law is the subject here, not the already available uniform-horizontal sampling distribution.

## Assumptions and scope

The family \(f_{p,q}\) is a normalized symmetric beta–Jacobi weight (its integral is one by substituting \(s=t^2\)). It may diverge integrably at the endpoints when \(p<1\) and at the midpoint when \(q<1\); these singularities are explicitly allowed. No sampling atoms occur. The lines form a nondegenerate triangle almost surely. All convergence statements are for fixed \(p,q>0\) and \(\varepsilon\downarrow0\); no uniformity as \(p\) or \(q\) vary is claimed. The total-variation convergence concerns the three displayed real-valued rescaled marks, not a weak or purely simulated limit.

## Proof

**Geometry and unique maximum.** Directly solving \(\ell_s\cap\ell_t\) gives \(((s+t)/2,st)\). A determinant of the three intersections yields the exact identity
\[
 A=\frac14(b-a)(c-b)(c-a).
\]
Write \(r=(c-a)/2\), \(w=(b-a)/(c-a)\); then \(A=2r^3w(1-w)\le1/2\), with equality only at the parameter triple \((-1,0,1)\). Thus \(\Delta=1/2-A<\varepsilon\) forces all three ordered parameters to their respective endpoint/midpoint positions.

**Uniform localization and scaling.** Put \(s=1-r=(a+1+1-c)/2\) and \(z=w-1/2\). The exact nonnegative decomposition
\[
 \Delta=\frac{1-(1-s)^3}{2}+2(1-s)^3 z^2
\]
forces \(s=O(\varepsilon)\) and \(z=O(\sqrt\varepsilon)\), with constants independent of \(p,q\). In particular \(a+1\) and \(1-c\) are each \(O(\varepsilon)\), and \(b=O(\sqrt\varepsilon)\). With the marks in the finding, one obtains uniformly on a compact enclosing region
\[
 \frac\Delta\varepsilon=U_\varepsilon+V_\varepsilon+Y_\varepsilon^2+O(\sqrt\varepsilon).
\]
Indeed \(s=2\varepsilon(U_\varepsilon+V_\varepsilon)/3\) and \(z=b/(2r)+((1-c)-(a+1))/(4r)\), so \(z=\sqrt{\varepsilon/2}\,Y_\varepsilon+O(\varepsilon)\). Hence the rescaled event indicators converge almost everywhere to \(u>0,v>0,u+v+y^2<1\).

**Local density and sharp constant.** The ordered triple has joint density \(6f_{p,q}(a)f_{p,q}(b)f_{p,q}(c)\). In endpoint variables \(\alpha=a+1\), \(\beta=1-c\), the density has the precise local equivalent
\[
 6B(q/2,p)^{-3}\,2^{2p-2}\alpha^{p-1}\beta^{p-1}|b|^{q-1}.
\]
Changing variables \(\alpha=(4\varepsilon/3)u\), \(\beta=(4\varepsilon/3)v\), \(b=\sqrt{2\varepsilon}\,y\) gives the transformed density divided by \(\varepsilon^d\) converging almost everywhere to
\[
 6B(q/2,p)^{-3}2^{2p-2+q/2}(4/3)^{2p}u^{p-1}v^{p-1}|y|^{q-1}.
\]
For all sufficiently small \(\varepsilon\), the event is in a fixed bounded rectangle. The transformed density divided by its local monomial weight is uniformly bounded there (with the harmless convention at the measure-zero singular coordinate hyperplanes), because \(|a|,|c|\to1\) and \(b\to0\). Since \(p,q>0\), the monomial weight is integrable on the rectangle. Dominated convergence therefore applies.

Substitute \(z=y^2\) with both signs, obtaining the exact simplex integral
\[
 \int_{u,v>0,\,u+v+y^2<1}u^{p-1}v^{p-1}|y|^{q-1}\,du\,dv\,dy
 =\frac{\Gamma(p)^2\Gamma(q/2)}{\Gamma(d+1)}.
\]
This proves the stated exponent and coefficient. Dividing the rescaled unconditioned densities by their convergent event probabilities gives convergence in \(L^1\), hence total-variation convergence to the normalized density. The simplex Jacobian yields the Dirichlet-and-sign description. Finally, the sum of the first three coordinates of a \(\operatorname{Dirichlet}(p,p,q/2,1)\) vector has \(\operatorname{Beta}(d,1)\) law; the expansion for \(\Delta/\varepsilon\) and the continuous-mapping theorem establish the deficit mark.

## Verification

The included `check.py` independently calculates areas via pairwise tangent-line intersections, verifies the deterministic formula, checks the density normalization and the sharp coefficient against direct three-variable numerical quadrature in rescaled coordinates at several small thresholds for non-uniform weights, and samples the limiting Dirichlet marks. The numerical diagnostics are supportive, not proofs of the infinite limiting statements.

## Relationship to prior work

Kim and Shim (2014) and Kim and collaborators (2014) establish deterministic area identities for tangent triangles to a parabola. Their identities, also derived above, are not novel. A separately published exact **uniform-horizontal** random parabolic hull law, *Endpoint-driven Gamma and interior Gaussian fluctuations for random parabolic hulls* (2026), gives the complete distribution in the special case \(p=q=1\), for all sample sizes, through a beta–Dirichlet factorization. It therefore already covers the uniform case, including its upper tail as a consequence of that distribution. The claimed new content is the two-parameter boundary/midpoint singular-weight family, its tunable exact rare-event exponent, and its full conditional Dirichlet marked law. The general stochastic convex-hull limit theorems of Besau, Rosen and Thäle (2020) concern other sampling geometries and growing sample sizes. The usual local change-of-variables and beta-integral methods are not claimed as new.

## Limitations

The result pertains to one finite parabolic arc with two endpoints and the specified beta–Jacobi family, not arbitrary convex curves. It is a fixed-three-sample rare-event theorem, not a large-sample asymptotic. Its proof establishes an extremal-tail law and conditional local geometry, not the complete finite-threshold area distribution for nonuniform weights. An earlier treatment in non-indexed geometric probability literature could exist. No independent audit has been performed.

## References

1. D.-S. Kim and K.-C. Shim, *Area of triangles associated with a curve*, arXiv:1401.4751v1, publicly posted 2014-01-19. https://arxiv.org/abs/1401.4751
2. D.-S. Kim and collaborators, *Area of triangles associated with a curve II*, arXiv:1404.2969, publicly posted 2014-04-10. https://arxiv.org/abs/1404.2969
3. *Endpoint-driven Gamma and interior Gaussian fluctuations for random parabolic hulls*, published research record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-endpoint-driven-gamma-and-interior-gaussian-fluctuations-for-ran--77a979074148
4. F. Besau, D. Rosen and C. Thäle, *Random inscribed polytopes in projective geometries*, arXiv:2005.10502, posted 2020-05-21. https://arxiv.org/abs/2005.10502
