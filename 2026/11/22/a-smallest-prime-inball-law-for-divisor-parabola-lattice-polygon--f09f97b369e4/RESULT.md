# A smallest-prime inball law for divisor-parabola lattice polygons

## Finding
For every integer \(h\ge2\), set
\[
B_h=\operatorname{conv}\bigl(\{(0,-1)\}\cup
\{(\pm a,a^2):a\in\mathbb N,\ a\mid h\}\bigr).
\]
Write \(p=p(h)\) for the least prime factor of \(h\), and set \(d=h/p\), \(m=h+d\) and \(s=\sqrt{1+m^2}\). The largest inscribed Euclidean disk of \(B_h\) is unique. Its exact radius and center are
\[
\boxed{\quad r_h=\frac{h(h+d)}{1+\sqrt{1+(h+d)^2}},
\qquad z_h=(0,h^2-r_h).\quad}
\]
It touches **exactly three polygon edges**: the top horizontal edge, and the two edges from \((\pm d,d^2)\) to \((\pm h,h^2)\). Every other facet is strictly farther from its center. In particular, the inball only depends on the greatest positive divisor \(h\) and its immediate predecessor \(d\), not on the other divisors.

For every composite \(h\), an arbitrary deletion of a symmetric selection of the intermediate divisor vertices \((\pm a,a^2)\) with \(1<a<d\) leaves the same unique disk. If \(\tau(h)\) is the number of positive divisors, this gives exactly \(2^{\tau(h)-3}\) distinct embedded polygons sharing that inball (among this deletion family).

The geometric defect from half the length \(2h\) of the top edge has the exact form
\[
\boxed{\quad h-r_h=\frac{p}{p+1}
\left(1-\frac{1}{\sqrt{1+(h+h/p)^2}+h+h/p}\right).\quad}
\]
It differs from \(p/(p+1)\) by less than \(1/(2h)\), uniformly over all \(h\ge2\). Thus the complete limit spectrum is
\[
\boxed{\left\{\lim_{j\to\infty}(h_j-r_{h_j}):
 h_j\to\infty,\ \text{limit exists}\right\}
=\left\{\frac{p}{p+1}:p\text{ prime}\right\}\cup\{1\}.}
\]
For any fixed prime \(p\), convergence to \(p/(p+1)\) is equivalent to the least prime divisor of \(h_j\) being eventually \(p\). Convergence to \(1\) is equivalent to those least prime divisors tending to infinity.

## Assumptions and scope
The polygons use the usual Euclidean metric and are precisely the divisor-parabola polygons introduced by Hofscheier and Nill in arXiv:2611.08819v1, Lemma 4.1. All divisors in the vertex prescription are positive, and both signs are used for each positive divisor. The radius is that of a freely centered **Euclidean disk**, not an origin-centered disk, an affine-invariant ellipse, or a lattice inscribed disk. Only \(h\ge2\) is claimed. For the deletion statement \(h\) is composite, so \(1<d<h\); vertices for \(1,d,h\) must be retained.

## Proof
**1. Facets and the three proposed contacts.** List the positive divisors as
\(1=d_1<d_2<\cdots<d_k=h\), and write \(d=d_{k-1}=h/p\). The exact irredundant facet list supplied by the cited polygon construction is
\[
y\le h^2,\qquad y\ge\pm 2x-1,\qquad
y\ge\pm(d_i+d_{i+1})x-d_id_{i+1}\quad(1\le i<k).
\]
Indeed, the last inequalities are the equations of the consecutive chords of the strictly convex parabola \(y=x^2\), with their reflections. Define, for \(a,b>0\),
\[
R_h(a,b)=\frac{h^2+ab}{1+\sqrt{1+(a+b)^2}}.
\]
The top supporting line and either chord line of slope magnitude \(a+b\), if both are tangent to a disk with center on the vertical axis, force that disk's radius to be \(R_h(a,b)\). Take the terminal chord \((d,h)\), and set \(r=R_h(d,h)\), \(c=h^2-r\). Then the candidate disk centered at \((0,c)\) is tangent to the top line and both terminal-chord lines, because
\[
h^2-c=r,\qquad \frac{c+dh}{\sqrt{1+(d+h)^2}}=r.
\]

**2. No intermediate chord cuts this disk.** For all \(h\ge2\), and every \(u,v\ge1\) with \(v\le h/2\), the function \(u\mapsto R_h(u,v)\) is strictly decreasing. Write \(w=u+v\) and \(S=\sqrt{1+w^2}\). Differentiation gives
\[
\operatorname{sgn}(\partial_u R_h(u,v))
=\operatorname{sgn}\bigl((v^2-h^2)w+v(1+S)\bigr).
\]
For \(w\ge2\), \(1+S<2w\). Therefore the sign is negative, since
\[
(v^2-h^2)w+v(1+S)<w(v^2+2v-h^2)
\le w\left(h-\frac{3h^2}{4}\right)<0.
\]
By symmetry the function is also strictly decreasing in \(v\) whenever \(u\le h/2\). Every nonterminal consecutive pair \((a,b)\) has \(1\le a<b\le d\le h/2\). Consequently
\[
R_h(a,b)\ge R_h(d,d)>R_h(d,h)=r.
\]
The exceptional bottom edges from \((0,-1)\) to \((\pm1,1)\) correspond to the same comparison with \((a,b)=(1,1)\) and are strictly slack. For the candidate center \((0,c)\), the distance to a lower supporting chord line is \((c+ab)/\sqrt{1+(a+b)^2}\); this exceeds \(r\) exactly when \(R_h(a,b)>r\). Thus every other facet is strictly slack. The candidate disk lies in the polygon, touches exactly those three facets, and has a positive radius. Each contact lies in the relative interior of its edge, since every other facet is slack and the contained disk reaches the supporting line.

**3. Optimality and uniqueness.** Let a disk with center \((x,y)\) and radius \(\rho\ge0\) lie in the polygon. Its distances to the top and the two terminal-chord lines imply
\[
\rho\le h^2-y,
\qquad \rho\sqrt{1+m^2}+m|x|\le y+dh.
\]
Adding gives \(\rho(1+\sqrt{1+m^2})+m|x|\le h^2+dh\), hence \(\rho\le r\). Equality forces \(x=0\), and then both distance inequalities must be equalities, forcing \(y=h^2-r\). The inball is unique. For any symmetric deletion of other divisor vertices retaining \(1,d,h\), the new lower facets again have endpoint parameters at most \(d\) except for the retained terminal chord. The preceding strict comparison applies unchanged, so the same disk remains uniquely maximal. Each retained parabola point is an extreme point because of strict convexity, so choices of subsets give exactly \(2^{\tau(h)-3}\) distinct polygons.

**4. Arithmetic limit spectrum and rigidity.** As the largest proper divisor is \(d=h/p\), put \(m=h(1+1/p)\) and \(s=\sqrt{1+m^2}\). Rationalizing gives \(r_h=h(s-1)/m\), hence the exact identity
\[
h-r_h=\frac{h}{m}(1+m-s)
=\frac{p}{p+1}\left(1-\frac1{s+m}\right).
\]
Because \(s+m>2m\ge2h\),
\[
0<\frac{p}{p+1}-(h-r_h)<\frac1{2h}.
\]
For a sequence \(h_j\to\infty\), the defect has the same limits as \(p(h_j)/(p(h_j)+1)\). Prime values \(p/(p+1)\) are isolated in this increasing set, with sole accumulation point \(1\). Therefore a limit below one equals \(p/(p+1)\) exactly when \(p(h_j)=p\) eventually; the limit one occurs exactly when \(p(h_j)\to\infty\). Every fixed-prime value is realized by \(h_j=p^j\), and one is realized by increasing primes. This proves the full spectrum and both equivalences.

## Verification
The independent standard-library program `verify_inball.py` recomputes the divisor lists and the proposed exact-algebraic radius to 65-digit decimal precision. Running it from the saved package passed 1,999 integer cases \(2\le h\le2000\), 15,517 lower-facet comparisons, and all terminal contact-foot interior checks. An independent linear-programming check of the unrestricted disk-center inequalities for \(2\le h\le150\) also matched the formula, as did 591 tests of deletion subpolygons; these LP checks are supplemental and are not needed to reproduce the packaged checker. No finite experiment is used in place of the preceding all-integer monotonicity proof or the exact spectral argument.

Reproduce the embedded test with `python3 verify_inball.py`; it requires only the Python standard library.

## Relationship to prior work
Hofscheier and Nill, arXiv:2611.08819v1 (first publicly posted 2026-11-06), introduce \(B_h\) as building blocks in a construction of reflexive polytopes with extremely many facets. Their Lemma 4.1 supplies exactly the facet description used here. That paper does **not** claim the inradius, center uniqueness, three-contact principle, deletion rigidity or arithmetic inradius-defect spectrum in its inspected sections. The separately published study *Sharp normalized area spectrum and lattice-point rigidity for divisor-parabola polygons* determines boundary lattice counts, area and area-limit spectra of the same \(B_h\), not their Euclidean inballs. An additional polar-area result determines \(\operatorname{area}(B_h^\circ)\), also a different invariant. Generic Chebyshev-center linear programming applies to every polygon, but does not itself supply this three-facet closed form or prime-factor rigidity. The novelty claim concerns this precise geometric/arithmetic classification, not the classical disk-center algorithm or the earlier facet enumeration.

## Limitations
This is a result about the planar divisor-parabola **building blocks**, not the Euclidean inradii of the higher-dimensional reflexive polytopes assembled from them. The inball formula does not imply that these polygons are tangential to circles along all edges; on the contrary, exactly three edges are tangent. The normalized area and lattice-point spectra are existing results and are not repeated as new claims. Historical priority remains provisional against unindexed notes or an unrecognized reformulation of a generic parametric Chebyshev-center theorem. Independent external mathematical audit has not been performed.

## References
1. J. Hofscheier and B. Nill, *Reflexive polytopes can have doubly exponentially many vertices*, arXiv:2611.08819v1 (2026-11-06), especially Lemmas 3.2 and 4.1 and Section 4. https://arxiv.org/html/2611.08819v1
2. *Sharp normalized area spectrum and lattice-point rigidity for divisor-parabola polygons* (2026-11-17), complete proof at https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-sharp-normalized-area-spectrum-and-lattice-point-rigidity-for-di--488d2a44055d/RESULT.md . Used for overlap comparison, not for the inradius proof.
3. T. Benham, *chebycenter(A,b,r0)*, MATLAB File Exchange (original release 2012), https://www.mathworks.com/matlabcentral/fileexchange/34987-chebycenter-a-b-r0 . Cited only as a representative generic polytope inball procedure, not as a theorem specialized to \(B_h\).
