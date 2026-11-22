# Two endpoint width laws and marked caliper limits for the oloid

## Finding

Let \(C_1=\{(\cos s,\sin s,0):0\le s<2\pi\}\) and \(C_2=\{(0,1+\cos s,\sin s):0\le s<2\pi\}\). Their convex hull \(K=\operatorname{conv}(C_1\cup C_2)\) is the unit oloid. For a uniform random unit normal \(U\in S^2\), let \(W=h_K(U)+h_K(-U)\) be its orthogonal projection length (caliper width).

**Theorem.** Its directional widths have exact range \([\sqrt2,3]\), with precisely four oriented minimizers \((\pm1/\sqrt2,0,\pm1/\sqrt2)\) (independent signs) and two maximizers \((0,\pm1,0)\). As \(\varepsilon\downarrow0\),

\[
\Pr\{W\le\sqrt2+\varepsilon\}
=\frac{2\sqrt2}{\pi}\varepsilon^2+O(\varepsilon^3),
\qquad
\Pr\{W\ge3-\varepsilon\}
=\frac{\varepsilon}{2}+\frac{\varepsilon^2}{64}+O(\varepsilon^3).
\]

The extreme-direction laws are marked, not merely scalar. Around each lower minimizer write
\[
U=(\sqrt{1-y^2}\cos\theta,y,\sqrt{1-y^2}\sin\theta),
\quad \theta_k=\frac\pi4+\frac{k\pi}{2},\quad k=0,1,2,3.
\]
Conditioned on \(W\le\sqrt2+\varepsilon\), each \(k\) has limiting probability \(1/4\), and the pair \((\sqrt2(\theta-\theta_k)/\varepsilon,y/\varepsilon)\) converges, including its conditional density in total variation, to the uniform law on \([-1,1]^2\). In this limit the probability that the two opposing support planes are borne by **different** generating circles tends to \(1/2\); the other half are supported by one generating circle.

Conditioned on \(W\ge3-\varepsilon\), the signs of the near-polar \(y\) coordinate have limiting probability \(1/2\) each. In either hemisphere the scaled coordinates \((x/\sqrt\varepsilon,z/\sqrt\varepsilon)\) converge in total variation to the uniform law on the unit disk \(\{(X,Z):X^2+Z^2\le1\}\). Opposing support planes are then borne by different generating circles with probability approaching one.

## Assumptions and scope

All Euclidean lengths use generating-circle radius one. Uniform direction means normalized spherical surface area, with \(U\) and \(-U\) both counted; \(W\) is a width rather than a chord length. The asymptotic remainder constants concern this fixed oloid. All limits are for positive \(\varepsilon\) tending to zero. The names of the generating circles are fixed by the displayed coordinate model; rigid motions and uniform rescaling give equivalent geometric statements.

## Proof

**Exact support reduction.** For \(u=(x,y,z)\in S^2\), the two circles separately have supports
\[
h_{C_1}(u)=A:=\sqrt{x^2+y^2}=\sqrt{1-z^2},
\qquad h_{C_2}(u)=y+B,
\quad B:=\sqrt{y^2+z^2}=\sqrt{1-x^2}.
\]
Because the support function of a convex hull is the maximum of its constituents,
\[
h_K(u)=\max(A,y+B),\qquad h_K(-u)=\max(A,-y+B).
\]
The elementary identity \(\max(a,b+t)+\max(a,b-t)=a+b+\max(|a-b|,|t|)\) therefore gives the global, exact, piecewise-analytic formula
\[
\boxed{\;W(u)=A+B+\max\{|A-B|,|y|\}
=\max\{2A,2B,A+B+|y|\}.\;}
\tag{1}
\]
This formula includes the switching loci and needs no approximation to the developable surface.

**Complete extrema.** Since \(\min(x^2,z^2)\le(1-y^2)/2\),
\[
W\ge2\max(A,B)=2\sqrt{1-\min(x^2,z^2)}
\ge\sqrt{2+2y^2}\ge\sqrt2.
\]
Equality forces \(y=0\), \(x^2=z^2=1/2\); all four possibilities attain it by (1). Conversely, formula (1) gives \(W=\max\{2A,2B,A+B+|y|\}\le3\). Since \(2A,2B\le2\), equality at three forces \(A=B=|y|=1\), hence \(x=z=0\). Both polar directions attain three. Compactness excludes all other limiting sources for either tail.

**Lower-tail local geometry.** Parametrize the sphere away from the polar points by
\[
(x,y,z)=(\sqrt{1-y^2}\cos\theta,y,\sqrt{1-y^2}\sin\theta).
\]
Its **exact** area element is \(\mathrm d\sigma=\mathrm d\theta\,\mathrm dy\). Around any of the four lower minimizers put \(t=\theta-\theta_k\). Direct Taylor expansion of the two square roots, uniform in the four charts, gives
\[
A+B=\sqrt2+O(t^2+y^2),\qquad
|A-B|=\sqrt2|t|+O(t^2+y^2).
\]
Consequently
\[
W-\sqrt2=\max(\sqrt2|t|,|y|)+O(t^2+y^2).\tag{2}
\]
The linear positive maximum is bounded below by a positive multiple of \(\sqrt{t^2+y^2}\). Thus for small enough deficit \(\varepsilon\), the event lies in four disjoint \(O(\varepsilon)\)-size charts. After \(s=\sqrt2t/\varepsilon\), \(v=y/\varepsilon\), its local indicator tends almost everywhere and in \(L^1\) to \(\boldsymbol1_{\{|s|\le1,|v|\le1\}}\). The \(O(\varepsilon^2)\) uniform expansion error in (2) shifts its rectifiable boundary by \(O(\varepsilon)\) in scaled coordinates, giving an \(O(\varepsilon^3)\) correction to probability. Each chart contributes
\[
\frac1{4\pi}\frac{\varepsilon^2}{\sqrt2}\operatorname{area}([-1,1]^2)
=\frac{\varepsilon^2}{\pi\sqrt2},
\]
and four charts yield \(2\sqrt2\varepsilon^2/\pi\). Uniform original area density and convergence of scaled sets in measure give the asserted total-variation conditional limit and equal weights. Outside switching loci of zero area, (1) shows that supports lie on different circles exactly when \(|y|>|A-B|\). On the limiting square this becomes \(|v|>|s|\), a region of exactly half its area.

**Upper-tail and its second coefficient.** Near \(y=\pm1\), set \(r^2=x^2+z^2\) and \(y=\pm\sqrt{1-r^2}\). Since \(|y|>|A-B|\) throughout sufficiently small polar neighborhoods, (1) reduces to
\[
W=\sqrt{1-x^2}+\sqrt{1-z^2}+\sqrt{1-r^2}.
\]
Writing \(x=r\cos\phi\), \(z=r\sin\phi\) and \(s=r^2\), uniformly in \(\phi\) we obtain
\[
3-W=s+c(\phi)s^2+O(s^3),\qquad
c(\phi)=\frac{1+\cos^4\phi+\sin^4\phi}{8}.
\tag{3}
\]
The boundary of the polar tail has \(s_\varepsilon(\phi)=\varepsilon-c(\phi)\varepsilon^2+O(\varepsilon^3)\). Spherical area in each polar chart is \((1-s)^{-1/2}\,\mathrm dx\,\mathrm dz\); summing the two poles and dividing by \(4\pi\) gives the exact local integration rule
\[
\Pr(W\ge3-\varepsilon)
=\frac1{2\pi}\int_0^{2\pi}\left(1-\sqrt{1-s_\varepsilon(\phi)}\right)\mathrm d\phi.
\]
The average of \(c(\phi)\) is \(7/32\), because each fourth-power trigonometric average is \(3/8\). Expanding the square root gives
\[
\Pr(W\ge3-\varepsilon)
=\frac\varepsilon2+\left(\frac18-\frac12\cdot\frac7{32}\right)\varepsilon^2+O(\varepsilon^3)
=\frac\varepsilon2+\frac{\varepsilon^2}{64}+O(\varepsilon^3).
\]
Finally, (3) shows that the scaled polar event converges in area to \(X^2+Z^2\le1\). Since the rescaled sphere density tends uniformly to one, the normalized restrictions converge in total variation to the uniform disk law; symmetry supplies weights \(1/2\) for the two poles. This completes the proof.

## Verification

The accompanying standalone `check.py` derives widths independently from sampled support points on each generator circle, checks the global support identity on random directions, and numerically integrates the exact lower and upper tail events without using the asymptotic coefficients to generate them. It tests convergence to \(2\sqrt2/\pi\) and to the second upper coefficient \(1/64\). To replay in a Python environment with NumPy and SciPy, run `python check.py` in the extracted artifact directory. Its finite diagnostics do not replace any global or asymptotic proof step, which is supplied above.

## Relationship to prior work

The oloid and its developable geometry are classical. Finch's arXiv:1211.4514 (first public November 19, 2012), especially its related-topics section, discusses the oloid among convex hulls of orthogonal circles and computes mean widths for other disk configurations. Bäsel and Dirnböck's arXiv:1503.07399 (first public February 25, 2015) addresses the extended oloid and contacting quadrics. Bäsel's arXiv:1604.07245 (first public April 25, 2016), especially Sections 3–4, computes **the mean width of the oloid** and sets up a directional support integration; this known integral and the old support-function framework are not claimed as new here. Nash, Pir, Sottile and Ying's arXiv:1612.09382 (first public December 30, 2016) classifies convex hulls, face lattices, and algebraic boundaries of circle pairs, including the oloid. The distinct statement here is the two endpoint probability expansions, the second high-tail term, and the marked conditional limiting contact laws. The inspected source material does not explicitly give or logically imply those coefficients via any quoted theorem, although they can be derived from a suitable directional support formula by the new local analysis; historical priority is not independently certified.

## Limitations

No full closed distribution function for \(W\), no stability estimates uniform across deformations of the two generating circles, and no distribution for non-isotropic directions are proved. The oloid is assumed to have exactly the classical unit-radius and center-separation geometry. The numerical checker is finite evidence, not an exhaustive or formal proof. The historical literature inspection was concentrated on the identified primary and nearest structural works; older unindexed treatments could affect priority. No independent mathematical audit was performed.

## References

1. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first submitted 2012-11-19. https://arxiv.org/abs/1211.4514
2. U. Bäsel and H. Dirnböck, *The extended oloid and its inscribed quadrics*, arXiv:1503.07399, first submitted 2015-02-25. https://arxiv.org/abs/1503.07399
3. U. Bäsel, *The mean width of the oloid and integral geometric applications of it*, arXiv:1604.07245, first submitted 2016-04-25. https://arxiv.org/abs/1604.07245
4. E. D. Nash, A. F. Pir, F. Sottile and L. Ying, *Convex Hull of Two Circles in R3*, arXiv:1612.09382, first submitted 2016-12-30. https://arxiv.org/abs/1612.09382
5. H. Dirnböck and H. Stachel, *The Development of the Oloid*, Journal for Geometry and Graphics 1 (1997), 105–118. https://www.researchgate.net/publication/250312099_The_Development_of_the_Oloid
