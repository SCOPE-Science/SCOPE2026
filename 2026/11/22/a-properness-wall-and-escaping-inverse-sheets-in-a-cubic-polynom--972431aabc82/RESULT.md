# A properness wall and escaping inverse sheets in a cubic polynomial plane map

## Finding

Consider the canonical cubic member of a published planar polynomial-map family,
\[
 F_{b,M}(x,y)=\bigl(y,\ y^2(x^3-3x)+bx+M\bigr),
 \qquad (x,y)\in\mathbb R^2,\quad b,M\in\mathbb R.
\]
For a target \((u,v)\), put \(w=v-M\). Its entire real inverse fiber is determined by
\[
 P_{u,b,w}(x)=u^2x^3+(b-3u^2)x-w=0,\qquad y=u.
\]
The sign \(b=0\) is a sharp **global properness and inverse-sheet transition**:

1. For \(b>0\), \(F_{b,M}\) is proper and surjective, has oriented topological degree \(-1\), and has precisely two ordinary cusp values \((\pm\sqrt{b/3},M)\). For \(|u|\le\sqrt{b/3}\), every target has exactly one distinct real preimage (including the cusp values). For \(|u|>\sqrt{b/3}\), define
   \[
   E_b(u)=2u^2\left(1-\frac{b}{3u^2}\right)^{3/2}>0.
   \]
   There are respectively three, two, or one distinct preimages when \(|w|<E_b(u)\), \(|w|=E_b(u)\), or \(|w|>E_b(u)\). The two-preimage cases contain one simple and one double inverse root; at each cusp target the sole inverse root is triple.

2. For \(b<0\), \(F_{b,M}\) is surjective but **not proper**. Every target with \(u=0\) has exactly one inverse, and every target with \(u\ne0\) has three, two, or one according as \(|w|<E_b(u)\), \(|w|=E_b(u)\), or \(|w|>E_b(u)\), with the same formula for \(E_b(u)\). There are no finite cusp values. As \(u\to0\),
   \[
   E_b(u)\sim\frac{2(-b)^{3/2}}{3\sqrt3\,|u|},
   \]
   and for each fixed \(w\) two of the three inverse branches satisfy
   \[
   x_\pm(u,w)=\pm\frac{\sqrt{-b}}{|u|}+\frac{w}{-2b}+O_{b,w}(|u|),
   \]
   while the third tends to \(w/b\). The expansion is uniform when \(w\) ranges in a fixed bounded set. Thus two inverse sheets diverge to spatial infinity while their image targets approach the regular target line \(u=0\).

3. At \(b=0\), the entire source line \(y=0\) collapses to \((0,M)\). This target has infinitely many inverse points, all other targets on \(u=0\) have none, and every target with \(u\ne0\) has three, two, or one distinct inverse points according as \(|w|<2u^2\), \(|w|=2u^2\), or \(|w|>2u^2\). The two fold-value curves \(v=M\pm 2u^2\) meet tangentially at the collapsed value.

The above count is of **distinct real affine inverse points**; critical inverse points are not counted with multiplicity. The transition concerns one-step inverse geometry, not forward basins or existence of a chaotic attractor.

## Assumptions and scope

All assertions concern the full map \(\mathbb R^2\to\mathbb R^2\), with arbitrary real \(b,M\), and all real target points. The cubic \(x^3-3x=2T_3(x/2)\) is the normalized odd Chebyshev cubic; it is a natural two-turning-point specialization of the source's arbitrary polynomial \(f(x)\). Proper means that preimages of compact subsets of \(\mathbb R^2\) are compact. A cusp means an ordinary semicubical Whitney cusp of the critical-value curve. A fold denotes a nondegenerate smooth critical point with one zero Jacobian direction.

## Proof

**Scalar reduction and root census.** Since the first output is \(u=y\), the remaining inverse equation is \(P_{u,b,w}(x)=0\). When \(u\ne0\), set \(h=1-b/(3u^2)\); then
\[
 P(x)=u^2(x^3-3hx)-w,\qquad P'(x)=3u^2(x^2-h).
\]
If \(h\le0\), the polynomial is strictly increasing (including the borderline cubic inflection), hence has one distinct real zero for each \(w\). If \(h>0\), its strict local maximum at \(-\sqrt h\) and minimum at \(+\sqrt h\) have heights respectively \(E=2u^2h^{3/2}\) and \(-E\) before subtracting \(w\). The intermediate-value theorem and strict monotonicity on each of the three derivative-sign intervals give exactly the stated counts and multiplicities. At \(u=0\), the polynomial reduces to \(bx-w\); this gives one root if \(b\ne0\), and all or no roots according to \(w=0\) if \(b=0\).

**Critical values and cusps.** The derivative is
\[
 DF=\begin{pmatrix}0&1\\3y^2(x^2-1)+b&2y(x^3-3x)\end{pmatrix},
\qquad \det DF=-[b+3y^2(x^2-1)].
\]
For \(u\ne0\) the critical points have \(x=\pm\sqrt h\), and their images are precisely \(v=M\mp E_b(u)\). At these points \(P''=6u^2x\ne0\), so they are ordinary folds. For \(b>0\) the only additional critical values occur at \(u=\pm\sqrt{b/3}\), \(x=0\), \(v=M\). On the positive-\(u\) critical curve the local parameter \(x\) yields
\[
 u(x)=\sqrt{\frac b{3(1-x^2)}}=\sqrt{b/3}\bigl(1+\tfrac12x^2+O(x^4)\bigr),
 \quad v(x)=M-\frac{2b x^3}{3(1-x^2)}=M-\frac{2b}3x^3+O(x^5).
\]
The coefficient of the quadratic horizontal displacement and of the cubic vertical displacement are nonzero; the negative-\(u\) critical curve is identical with the first coordinate sign reversed. Hence there are exactly two ordinary semicubical cusps. If \(b<0\), then \(h>1\) at every \(u\ne0\), so no critical point has \(x=0\) and all critical values are folds. If \(b=0\), the additional critical line \(y=0\) collapses, as asserted.

**Properness and escape.** If \(b>0\), a bounded sequence of target first coordinates forces \(y\) bounded. If \(|x|\ge2\), \(x^3-3x\) has the sign of \(x\), so
\[
 |y^2(x^3-3x)+bx+M|\ge b|x|-|M|.
\]
Bounded outputs therefore force \(x\) bounded. Continuity then gives compact preimages of compact sets. Surjectivity follows from the odd-degree scalar polynomial (or the linear equation when \(u=0\)). At every regular target, the local orientation signs sum to \(-1\): the derivative signs of the inverse cubic, ordered by increasing root, are \((+)\) in the one-root case and \((+,-,+)\) in the three-root case, while \(\det DF=-P'(x)\). The proper map thus has degree \(-1\).

If \(b<0\), choose \(u\ne0\), \(w=0\); the inverse roots are
\[
 x=0,\qquad x=\pm\sqrt{3-b/u^2}.
\]
As \(u\to0\) the latter diverge while all outputs \((u,M)\) remain bounded, proving nonproperness. For a general fixed \(w\), multiply the cubic equation by \(|u|\) after putting \(z=|u|x\):
\[
 z^3+(b-3u^2)z-w|u|=0.
\]
At \(|u|=0\), its three roots are the distinct simple numbers \(0,\pm\sqrt{-b}\). The implicit function theorem, with derivatives \(b\) and \(-2b\), gives \(z_0=w|u|/b+O(u^2)\) and \(z_\pm=\pm\sqrt{-b}+w|u|/(-2b)+O(u^2)\), uniformly for bounded \(w\). Dividing by \(|u|\) proves the expansions. The formula for \(E_b\) gives its inverse-\(|u|\) asymptotic directly. When \(b=0\), the entire line \(y=0\) has image \((0,M)\), so the map is nonproper. All remaining assertions follow from the scalar root census.

## Verification

The standalone standard-library script `check.py` checks the exact discriminant identity, critical-value formula, cusp parametrization, inverse-root patterns on rational sample points, and the three distinct escape branches. These finite checks are **not** substitutes for the all-parameter analytic proof above.

## Relationship to prior work

Wei, Zhang, Zhang and Grebogi introduce the family \((x,y)\mapsto(y,f(x)y^2+bx+M)\) and investigate symbolic horseshoes and locally singular geometry. Their analysis includes collapse points for lower-degree specializations and an explicit rational inverse when \(f\) is linear. In the examined complete article, no global sign-of-\(b\) properness classification or two-escaping-sheet law is provided for the canonical cubic \(f(x)=x^3-3x\). Ordinary folds and semicubical cusps are classical local singularity types; this finding does not claim those general facts as new. Its distinct contribution is the global **same-family** threshold relating properness, whole-plane inverse-fiber counts, cusp topology, and loss of two inverse sheets at infinity. Related published inverse-sheet classifications for other dynamical families do not imply this polynomial parameter threshold.

## Limitations

No conclusion is asserted for the forward orbit dynamics, entropy, attractiveness, or Smale horseshoes of this particular coefficient choice. The real inverse counts are not complex algebraic intersection counts. The classification is for the canonical Chebyshev cubic, not every arbitrary polynomial in the originating family. Formal independent mathematical validation and exhaustive priority checking beyond the inspected sources have not been performed; equivalent global polynomial-map literature could affect publication priority. The earliest verified day-level public-source date is 2024-11-03; an undated-to-day secondary posting lists January 2024 but does not establish an exact earlier public day.

## References

1. Z. Wei, L. Zhang, X. Zhang and C. Grebogi, *A class of non-invertible chaotic polynomial maps and Smale horseshoes of new types*, Discrete and Continuous Dynamical Systems B 30 (2025), 2258–2276. DOI: https://doi.org/10.3934/dcdsb.2024163 . Verified early-online date: 2024-11-03 at https://abdn.elsevierpure.com/en/publications/a-class-of-non-invertible-chaotic-polynomial-maps-and-smale-horse/ .
2. Open-access full text of the same article: https://www.researchgate.net/publication/385910515_A_class_of_non-invertible_chaotic_polynomial_maps_and_Smale_horseshoes_of_new_types .
