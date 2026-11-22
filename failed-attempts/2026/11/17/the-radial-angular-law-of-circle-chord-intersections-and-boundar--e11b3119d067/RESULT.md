# The radial–angular law of circle-chord intersections and boundary-angle uniformization

## Finding

Let four points be sampled independently with normalized arclength measure on the unit circle. Join the first two and the last two by chords. Let \(X\) be the intersection of the two supporting lines, \(R=\|X\|\), and \(\Theta\in(0,\pi)\) the angle between the unoriented line normals modulo \(\pi\), defined precisely below. On the event \(R<1\), the intersection lies in both chord segments.

For \(0<r<1\), put
\[
L(r)=-\log(1-r^2),\qquad
K_r(t)=\int_0^\pi \frac{da}{\sqrt{1-r^2\cos^2a}\sqrt{1-r^2\cos^2(a+t)}}.
\]
The conditional angular density at intersection radius \(r\) is exactly
\[
\boxed{f_r(t)=\frac{r^2\sin t}{2\pi L(r)}K_r(t),\quad 0<t<\pi.}
\]
In particular, the conditional crossing-angle law undergoes a rigorous transition from a sine density at the disk center to uniform at the boundary:
\[
\lim_{r\downarrow0}\|f_r-\tfrac12\sin(\cdot)\|_{L^1(0,\pi)}=0,
\qquad
\boxed{\lim_{r\uparrow1}\|f_r-\tfrac1\pi\|_{L^1(0,\pi)}=0.}
\]
Thus the second convergence holds in **total variation**, not merely weakly. The **joint** density of the intersection radius and marked chord angle, with respect to \(dr\,dt\), before conditioning on intersection, is
\[
\boxed{j(r,t)=\frac{2r\sin t}{\pi^3}K_r(t),\quad 0<r<1,\quad0<t<\pi.}
\]
The already-known radial marginal is \(\int_0^\pi j(r,t)dt=-4\log(1-r^2)/(\pi^2r)\), so its mass is exactly \(1/3\). The scalar marginal and its dilogarithmic CDF are prior results, not the novelty claim.

## Assumptions and scope

All four endpoints are mutually independent and uniform on \(S^1\). Degenerate coincident or parallel lines have probability zero. For each unoriented chord line, take its normal angle \(\alpha\in[0,\pi)\), and use the signed offset \(p\in(-1,1)\) so that the line equation is \(x\cos\alpha+y\sin\alpha=p\). For the two lines, define \(\Theta=(\beta-\alpha)\bmod\pi\in(0,\pi)\). This convention distinguishes the two supplementary crossing angles; their interchange corresponds to \(t\mapsto\pi-t\). It is invariant under simultaneous rotation in distribution. For a geometric *acute* intersection angle, push forward by \(t\mapsto\min(t,\pi-t)\). The density is symmetric about \(\pi/2\), so its acute-angle density is \(2f_r(t)\) on \((0,\pi/2)\).

The formula for a conditional law given \(R=r\) means the continuous regular conditional density on \((0,1)\). For any measurable \(E\subseteq(0,1)\times(0,\pi)\), \(\Pr((R,\Theta)\in E)=\iint_E j(r,t)\,dr\,dt\). No claim about intersections outside the disk or nonuniform endpoint sampling is made.

## Proof

**1. Line coordinates and their law.** The chord determined by two uniform circle points has a normal angle \(\alpha\) uniform on \([0,\pi)\). Rotation invariance makes this angle independent of the signed distance \(p\), whose density on \((-1,1)\) is \(1/(\pi\sqrt{1-p^2})\). To see the latter directly, write the endpoints as \(e^{i(m\pm v)}\). Their line is \(x\cos m+y\sin m=\cos v\). Reducing the normal modulo \(\pi\) only reverses the signed distance when needed; the angular difference is uniform, yielding the displayed arcsine density. The two chords' line coordinates \((\alpha,p)\) and \((\beta,q)\) are independent.

**2. Jacobian for the intersection.** At a fixed pair of distinct normals the intersection location \(X=(x,y)\) satisfies
\[
p=x\cos\alpha+y\sin\alpha,\qquad q=x\cos\beta+y\sin\beta.
\]
The absolute determinant of \((x,y)\mapsto(p,q)\) is \(|\sin(\beta-\alpha)|\). Since the normal-angle difference modulo \(\pi\) is uniform and independent of the first normal, conditional on \((\alpha,\Theta)=(a,t)\) the spatial density at \(x\), for \(\|x\|<1\), is
\[
\frac{\sin t}{\pi^2\sqrt{1-(x\cdot n_a)^2}\sqrt{1-(x\cdot n_{a+t})^2}},
\quad n_a=(\cos a,\sin a).
\]
Multiplying by the normal-angle density \(1/\pi^2\) and integrating \(a\in[0,\pi)\), the joint density per unit planar area and per unit \(dt\) is
\[
\frac{\sin t}{\pi^4}\int_0^\pi\frac{da}{\sqrt{1-(x\cdot n_a)^2}\sqrt{1-(x\cdot n_{a+t})^2}}.
\]
Rotational invariance lets us take \(x=(r,0)\); integrating its polar direction produces the radial Jacobian \(2\pi r\) and proves the stated \(j(r,t)\). For \(\|X\|<1\), both intersections lie inside the unit disk and hence inside the complete chord segments, as required.

**3. Exact normalization and conditional density.** The classical Karamata law, in the exact analytic formulation of Bortolotto–Souza (2025), gives
\[
\Pr(R\le r)=\frac{2}{\pi^2}\operatorname{Li}_2(r^2),\qquad 0\le r\le1,
\]
where \(\operatorname{Li}_2(z)=\sum_{n\ge1}z^n/n^2\). Differentiating for \(0<r<1\) gives the known density
\[
h(r)=\frac{4L(r)}{\pi^2 r}.
\]
At \(r=1\) its integrated mass is \(2\operatorname{Li}_2(1)/\pi^2=1/3\). Dividing \(j(r,t)\) by \(h(r)\) gives \(f_r(t)\), a nonnegative density integrating to one for every \(0<r<1\). Equivalently, the change-of-variables calculation and the known radial identity give the exact angular convolution identity
\[
\int_0^\pi\sin t\,K_r(t)\,dt=\frac{2\pi L(r)}{r^2}.
\]
This identity is not assumed for the new marked law; it provides a check on the normalization.

**4. Center limit.** For \(r\downarrow0\), the two factors in the integrand defining \(K_r(t)\) converge to one uniformly over \((a,t)\), so \(K_r(t)\to\pi\) uniformly. Since \(L(r)/r^2\to1\), \(f_r(t)\to\frac12\sin t\) uniformly on \([0,\pi]\), hence in \(L^1\).

**5. Boundary singularities.** Fix \(t\in(0,\pi)\) and write \(\epsilon=1-r^2\). On the circle of normal angles modulo \(\pi\), the integrand defining \(K_r(t)\) has two distinct singular neighborhoods as \(\epsilon\downarrow0\): \(a=0\) modulo \(\pi\) and \(a=-t\) modulo \(\pi\). Outside fixed disjoint neighborhoods it stays bounded. In the first neighborhood,
\[
\frac1{\sqrt{1-r^2\cos^2a}}=\frac{1+o(1)}{\sqrt{\epsilon+a^2}}
\]
when \(a\) is simultaneously small and \(\epsilon\to0\), while the other factor tends to \(1/\sin t\). The integral of the singular first factor over a fixed symmetric small neighborhood equals \(\log(1/\epsilon)+O(1)\). For complete rigor, first choose a neighborhood radius \(\eta>0\), bound the nonsingular factor between its extrema on that neighborhood, divide by \(\log(1/\epsilon)\), let \(\epsilon\downarrow0\), then send \(\eta\downarrow0\). The resulting coefficient is \(1/\sin t\). The neighborhood at \(a=-t\) contributes the same. Therefore, for every fixed \(t\in(0,\pi)\),
\[
\boxed{\lim_{r\uparrow1}\frac{K_r(t)}{L(r)}=\frac{2}{\sin t}.}
\]
Substitution yields \(f_r(t)\to1/\pi\) pointwise for almost every \(t\). Since each \(f_r\) is a nonnegative density and \(1/\pi\) also has unit integral, Scheffé's lemma implies \(\|f_r-1/\pi\|_1\to0\), completing the total-variation assertion. No uniform convergence near \(t=0\) or \(t=\pi\) is asserted.

**6. An independent integral check.** Conditional on two chords crossing, the four points appear in alternating circular order. Their four normalized gaps have Dirichlet \((1,1,1,1)\) law; the angle \(\Theta/\pi\), or its supplement, is the sum of two opposite gaps and hence has Beta \((2,2)\) law. Consequently its *global* conditional density is \(6t(\pi-t)/\pi^3\) and \(\mathbb E[\cos(2\Theta)\mid R<1]=-3/\pi^2\). This ancillary elementary check is consistent with integrating the joint density and is not itself presented as the new contribution.

## Verification

The accompanying `check_chord.py` recreates independent endpoint samples and compares the predicted total crossing probability, globally integrated angular moment, and several thin-shell radial-angle moments. It independently evaluates the one-dimensional convolution by deterministic quadrature, confirms numerical normalization of \(f_r\), and displays pointwise approach toward the uniform boundary density. The executable test is finite and does not substitute for the mathematical proof; in particular, convergence in total variation follows from Step 5 and Scheffé's lemma, not from a histogram. Run with Python, NumPy, and SciPy as listed in `requirements.txt`.

## Relationship to prior work

David and Fix (1964) studied intersections of random circle chords. Their publisher-verified publication date is December 1, 1964; the complete text was not accessible during this comparison. Bortolotto and Souza (arXiv 2025) derive the radial intersection distribution, including the dilogarithmic formula used in Step 3, and compare random line sampling rules. Their accessible primary text addresses the unmarked location distribution, not the displayed marked radial-angular density or its total-variation boundary-angle theorem. Barahona Torres, Manrique-Mirón and Treviño-Aguilar (2019) prove a sine law for a different chord model: one chord connects **area-uniform disk points**, the other is horizontal with uniformly random height; it is not the present pair of independently endpoint-uniform circular chords. A separate published study of ellipse chord-crossing angle statistics concerns an **unconditional** squared-sine moment varying with axis ratio; no spatially conditioned law is asserted in its available summary.

The classical crossing probability \(1/3\), the dilogarithmic radial marginal, and the elementary global Beta angle law are explicitly excluded from the assessed novelty. The contribution being assessed is the **marked joint density and the nontrivial center-to-boundary total-variation transition**. A known scalar location or scalar angle marginal does not logically determine their joint distribution. The comparison remains subject to an archival-priority risk because David–Fix's full paper could not be examined.

## Limitations

This is a conditional statement at radii strictly inside the unit disk; no claim is made about arbitrary intersections of the extended lines outside it, unequal circles, other chord sampling mechanisms or explicit rate of convergence. The definition of the marked angle matters; using the acute angle requires the stated folding transformation. The 1964 paper was inaccessible in full, so historical novelty is provisional. Numerical finite sampling cannot prove the infinite-limit statements. Independent external mathematical review has not been performed.

## References

1. F. N. David and Evelyn Fix, *Intersections of Random Chords of a Circle*, Biometrika 51 (1964), 373–379, DOI: 10.1093/biomet/51.3-4.373 (publisher date 1964-12-01).
2. Cynthia Bortolotto and Victor Souza, *Intersections of Random Chords of a Circle*, arXiv:2504.12866 (first public version 2025-04-17), especially Theorem 1 and Section 4.
3. J. I. H. Barahona Torres, P. C. Manrique-Mirón, E. Treviño-Aguilar, *Angle Distribution of Two Random Chords in the Disc: A Sine Law*, arXiv:1911.05576 (first public version 2019-11-13), Theorem 2.1 (different sampling model).
