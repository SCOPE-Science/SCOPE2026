# An interior-to-boundary collision bifurcation obstructing two Blaschke similarity tests

## Finding
For real \(0<a<1\), let
\[
b_a(z)=\frac{z-a}{1-az},\qquad \Psi_a(z)=\bigl(z^2,b_a(z)^3\bigr),\qquad c_a=\frac{1-a^2}{\sqrt3 a},\quad a_*=2-\sqrt3.
\]
The two-coordinate finite Blaschke map \(\Psi_a:\overline{\mathbb D}\to\overline{\mathbb D}^2\) is unramified (its coordinate derivatives never vanish simultaneously), but it fails injectivity for every \(a\). All distinct-point collision pairs, counted as unordered pairs, are:

* \(0<a<a_*\): exactly \(\{iy,-iy\}\) with \(y=(c_a-\sqrt{c_a^2-4})/2\in(0,1)\), an interior collision;
* \(a=a_*\): exactly \(\{i,-i\}\), the boundary transition;
* \(a_*<a<1\): exactly two boundary pairs \(\{z_+,-z_+\}\) and \(\{z_-,-z_-\}\), where \(z_\pm=(\pm\sqrt{4-c_a^2}-ic_a)/2\).

Consequently the pair is never a uniform strong test collection, nor a uniform test collection, for similarity to contractions on the closed disc. This gives an exact phase diagram for how a smallest-degree pair of nontrivial, jointly unramified inner-function tests can fail by global collisions.

## Assumptions and scope
The parameter \(a\) is real and strictly between zero and one. The domain includes the closed unit disc. The term *collision* means an unordered pair of distinct points in the domain having identical images under both coordinate functions. A uniform similarity test collection is understood in the sense of Badea, Theorem 7.3 (2026): uniform control of an operator's similarity constant from those of the coordinate-function calculi for arbitrary bounded Hilbert-space operators with spectrum in the closed disc. No statement is made about local spectral restrictions excluding collision points.

## Proof
First, \((z^2)'=2z\). Since \(b_a'(z)=(1-a^2)/(1-az)^2\), the derivative of \(b_a^3\) vanishes only at \(z=a\). Because \(a\ne0\), the coordinate derivatives never vanish together, including on the boundary.

Suppose \(\Psi_a(z)=\Psi_a(w)\), with \(z\ne w\). Equality of squares forces \(w=-z\), with \(z\ne0\). The nonvanishing automorphism values \(b_a(z)\) and \(b_a(-z)\) need special care at zeros: if one vanishes, both would have to, forcing simultaneously \(z=a\) and \(-z=a\), impossible for \(a>0\). Thus their ratio is well-defined, and equality of their cubes means
\[
\frac{b_a(z)}{b_a(-z)}=\omega\quad\text{or}\quad\omega^2,\qquad\omega=e^{2\pi i/3}.
\]
(The ratio cannot be one for a distinct-point pair, since \(b_a\) is injective.) Substitution gives
\[
-a z^2-(1-a^2)z+a=\omega\bigl(-a z^2+(1-a^2)z+a\bigr).
\]
Using \((1+\omega)/(\omega-1)=-i/\sqrt3\), this is the quadratic
\[
z^2+ic_a z-1=0.
\]
For \(\omega^2\), the equation is \(z^2-ic_a z-1=0\). Since \(\omega^2=\omega^{-1}\), negation interchanges the two quadratics. Thus the unordered collision pairs are exactly the roots of the first quadratic that belong to the closed unit disc, identified with their negatives.

If \(c_a>2\), the first quadratic has roots \(-iy\) and \(-i/y\), where \(y=(c_a-\sqrt{c_a^2-4})/2\in(0,1)\); only \(-iy\) is in the closed disc, giving one interior pair. If \(c_a=2\), it has the double root \(-i\), giving the sole boundary pair \(\{i,-i\}\). If \(0<c_a<2\), it has the two distinct unit-modulus roots \(z_\pm=(\pm\sqrt{4-c_a^2}-ic_a)/2\), giving precisely two distinct boundary pairs. Solving \(c_a=2\) in \(a\in(0,1)\) yields \(a_*=2-\sqrt3\). Monotonicity of \(c_a\) in \(a\) gives the asserted parameter ranges.

Finally, Badea's exact test-collection characterization (Theorem 7.3) says a finite Blaschke tuple is a uniform test collection on the closed disc exactly when it is both injective there and jointly unramified. The noninjectivity just established rules out both uniform ordinary and strong testing. Alternatively, for every displayed collision \(z\ne w\), triangular operators with eigenvalues \(z,w\) and arbitrarily poorly conditioned eigenvectors provide the obstruction directly, exactly as in the necessity proof of that theorem.

## Verification
The proof enumerates every possible distinct-point fiber: equality of the first coordinate leaves only \(w=-z\); the second condition reduces to two explicitly solved quadratic equations interchanged by negation. The signs in the quadratic follow by directly multiplying out the Möbius factors. The critical equation \(c_a=2\) has exactly one solution in \((0,1)\), namely \(2-\sqrt3\). Interior, double-boundary and two-boundary cases exhaust all positive \(c_a\). The conclusion about uniform tests uses the published necessary-and-sufficient criterion, not numerical sampling.

## Relationship to prior work
Badea (2026, arXiv:2611.01703v1, §§7 and Example 7.5) establishes the abstract injective/unramified criterion and constructs a *three*-function test tuple built from \(z^2\), \(z^3\) and a shifted squared Blaschke factor. The present result analyzes the distinct *two*-function family \((z^2,b_a^3)\): it explicitly classifies all its collision fibers and the interior-to-boundary transition. It does not claim novelty for the abstract implication from noninjectivity to failure of uniform testing. Dritschel–Estévez–Yakubovich (2017, arXiv:1510.08350v2, §3.5 and Corollary 19) give earlier sufficient spectral-testing criteria, without the stated parameter-dependent collision classification.

## Limitations
The contribution is an exact one-parameter classification for this particular pair; it is not a classification of all pairs of finite Blaschke products. The abstract failure of uniform testing is an established consequence of the existing test-collection theorem. Exact coverage by older equivalent treatments of this specific rational map remains possible; publication-priority verification by a human is advisable. The interval endpoints \(a=0,1\) are excluded: at zero the joint derivative vanishes, while at one the Möbius map degenerates. No quantitative universal similarity constant is asserted.

## References
1. C. Badea, *Transfer of similarity to Hilbert space contractions through inner functions: a proof of Douglas's conjecture*, arXiv:2611.01703v1, first public 1 November 2026, especially Theorem 7.3 and Example 7.5. https://arxiv.org/html/2611.01703v1
2. M. A. Dritschel, D. Estévez and D. Yakubovich, *Tests for complete K-spectral sets*, arXiv:1510.08350v2 (2017), §3.5 and Corollary 19. https://arxiv.org/pdf/1510.08350
