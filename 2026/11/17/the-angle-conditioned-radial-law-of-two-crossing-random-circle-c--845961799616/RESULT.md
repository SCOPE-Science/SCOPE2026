# The angle-conditioned radial law of two crossing random circle chords

## Finding

Draw four independent arclength-uniform points on the Euclidean unit circle; pair the first two and the last two as chords, and condition on the event that the two **segments** cross. This event has probability \(1/3\). Let \(R\in[0,1]\) be the Euclidean distance of their intersection from the circle center, and let \(\Theta\in(0,\pi/2)\) be the acute angle between the two chord lines. The following is a complete conditional distribution theorem for the radial crossing position, rather than an unconditional radial marginal.

For \(0<t<\pi/2\), put \(a=t\), \(b=\pi-t\), \(s=\sin t\). Conditional on \(\Theta=t\), let \(U,V\) be **independent** uniform random variables on \([-1,1]\). Then
\[
\boxed{\ 1-R^2\ \stackrel{d}{=}\
 \frac{(\cos(aU)-\cos a)(\cos(bV)-\cos b)}{\sin^2 a}\ } .
\]
The angular marginal, which is previously known, is
\[
 f_\Theta(t)=\frac{12t(\pi-t)}{\pi^3},\qquad 0<t<\pi/2.
\]
Define \(M_k(z)=\int_0^1(\cos(zu)-\cos z)^k\,du\). For **every** positive integer \(k\), the conditional radial-deficiency moment is
\[
\boxed{\ \mathbb E[(1-R^2)^k\mid\Theta=t]
 =\frac{M_k(t)M_k(\pi-t)}{\sin^{2k}t}.\ }
\]
These moments are finite elementary trigonometric sums. In particular,
\[
\boxed{\ \mathbb E[R^2\mid\Theta=t]
 =1-\left(\frac1t-\cot t\right)
       \left(\frac1{\pi-t}+\cot t\right).\ }
\]
At a right-angle crossing this equals \(1-4/\pi^2\); as \(t\downarrow0\), it tends to \(2/3\). The distribution has sharp, **angle-dependent** tails: for every fixed \(0<t<\pi/2\),
\[
\boxed{\ \Pr(R\le r\mid\Theta=t)
  =\frac{\pi\sin t}{2t(\pi-t)}r^2+O_t(r^4)
 \quad(r\downarrow0),\ }
\]
and
\[
\boxed{\ \Pr(R\ge1-\varepsilon\mid\Theta=t)
 =\frac{2\varepsilon}{t(\pi-t)}\log\frac1\varepsilon+O_t(\varepsilon)
 \quad(\varepsilon\downarrow0).\ }
\]
An exact one-dimensional conditional CDF, for \(0\le r\le1\), is
\[
 \Pr(R\le r\mid\Theta=t)=\frac1{t(\pi-t)}
 \int_{1-r^2(1-\cos t)}^1
 \frac{\arccos\left(-\cos t+
 \frac{(1-r^2)\sin^2t}{z-\cos t}\right)}{\sqrt{1-z^2}}\,dz,
\]
with the endpoint values obtained continuously. In particular the law is continuous and supported on the entire interval \([0,1]\).

## Assumptions and scope

All four endpoints are independent and uniform under normalized circular arclength. Chords are closed line **segments**, and the crossing event requires their unique interior intersection; endpoints and tangencies have probability zero. The acute angle \(\Theta\) between the two unoriented chord lines lies strictly between \(0\) and \(\pi/2\) almost surely on crossing. Conditional laws at an exact angle mean the explicit continuous regular conditional version constructed by the proof. The exact CDF and asymptotic tails are stated for each **fixed** interior angle, not uniformly down to zero. The marginal density for \(\Theta\), the unconditional radial law, and the four-gap Dirichlet distribution are not claimed as new.

## Proof

1. Four distinct circle points admit three pairings into two chords. Exactly one pairing crosses, hence the event probability is \(1/3\). Once crossing has been imposed, the conditional law of the four unordered endpoints remains that of four independent circular uniform points, with the unique crossing pairing.

2. Distinguish one of the four sampled endpoints **uniformly among those four** and rotate it to polar angle zero. List the other endpoints counterclockwise; let \(g_1,g_2,g_3,g_4>0\) be the successive circular angular gaps, summing to \(2\pi\). The normalized gap vector has distribution \(\operatorname{Dirichlet}(1,1,1,1)\). (Always starting at the point having the smallest *absolute* polar angle would not give this distribution.) The crossing chords connect vertices at cyclic indices \(0,2\) and \(1,3\).

3. Set \(A=(g_1+g_3)/2\in(0,\pi)\) and \(B=\pi-A=(g_2+g_4)/2\). The angle between the corresponding **directed** chords is \(A\); the usual unoriented acute angle is \(\Theta=\min(A,B)\). Dirichlet aggregation gives \(A/\pi\sim\operatorname{Beta}(2,2)\), whence \(f_A(a)=6a(\pi-a)/\pi^3\). Folding the symmetric density gives \(f_\Theta\). Conditional on \(A=a\), the two independent group splits are uniforms: write \(g_1=a(1+U)\), \(g_3=a(1-U)\), \(g_2=b(1+V)\), and \(g_4=b(1-V)\), with independent \(U,V\sim\operatorname{Unif}[-1,1]\).

4. Choose oriented normals to the chord lines at the mid-arc angles. Their signed offsets from the origin are
\[
 d_1=\cos((g_1+g_2)/2)=-\sin((aU+bV)/2),\qquad
 d_2=\cos((g_2+g_3)/2)=-\sin((-aU+bV)/2).
\]
Their oriented normal difference is \(a\). Solving the two linear equations for the intersection gives
\[
 R^2=\frac{d_1^2+d_2^2-2d_1d_2\cos a}{\sin^2a}.
\]
Elementary product-to-sum identities yield the exact **pointwise** factorization
\[
 1-R^2=\frac{(\cos(aU)-\cos a)(\cos(bV)-\cos b)}{\sin^2 a}.
\]
Cycling the distinguished starting endpoint by one vertex exchanges \(a\) and \(b\) and swaps the two independent cosine factors. Its product law is therefore invariant under \(a\mapsto\pi-a\), proving the displayed formula conditional on the acute angle \(t\).

5. For \(0<z<\pi\), the variable \(X_z=\cos(zU)-\cos z\), \(U\sim\operatorname{Unif}[-1,1]\), has support \([0,1-\cos z]\), cumulative distribution
\[
 \Pr(X_z\le x)=1-\frac{\arccos(\cos z+x)}{z},
\quad 0\le x\le1-\cos z,
\]
and interior density \(f_z(x)=[z\sqrt{1-(\cos z+x)^2}]^{-1}\). The independence of \(X_a,X_b\) proves the moment product. Since \(\mathbb E X_z=\sin z/z-\cos z\), the first-moment formula follows. Integrating \(\Pr(X_b\ge(1-r^2)\sin^2a/X_a)\) against \(f_a\), with the substitution \(z=X_a+\cos a\), gives the exact conditional CDF as written. The endpoint values follow from the supports and continuity of the factors.

6. The moments are elementary: expanding a positive integer power and using the binomial expansion of cosine gives
\[
 M_k(z)=\sum_{j=0}^k\binom kj(-\cos z)^{k-j}2^{-j}
 \sum_{\ell=0}^j\binom j\ell
 \operatorname{sinc}((j-2\ell)z),
 \qquad\operatorname{sinc}(w)=\begin{cases}\sin w/w,&w\ne0,\\1,&w=0.\end{cases}
\]
This is a finite exact expression for every fixed integer \(k\ge1\).

7. For the **center tail**, the maximum deficiency \(1-R^2=1\) occurs only at \(U=V=0\). A Taylor expansion there gives
\[
 R^2=\frac{a^2}{4\sin^2(a/2)}U^2
      +\frac{b^2}{4\sin^2(b/2)}V^2
      +O_a((U^2+V^2)^2).
\]
The joint density of \((U,V)\) is \(1/4\); the leading ellipse has area \(2\pi r^2\sin a/(ab)\). Multiplication by \(1/4\) proves the coefficient \(\pi\sin a/(2ab)\). The analytic even local Jacobian yields the \(O_a(r^4)\) remainder. Only one preimage of the origin is present in the open square.

8. For the **outer tail**, \(X_a\) and \(X_b\) have smooth strictly positive densities at zero:
\[
 f_a(0)=\frac1{a\sin a},\qquad f_b(0)=\frac1{b\sin a}.
\]
For any two independent bounded nonnegative variables having such densities, splitting the product integral at a small fixed cutoff gives
\[
 \Pr(X_aX_b\le\delta)=f_a(0)f_b(0)\,\delta\log(1/\delta)+O_a(\delta).
\]
Here \(1-R^2=X_aX_b/\sin^2a\). Substituting \(\delta=(2\varepsilon-\varepsilon^2)\sin^2a\) yields the stated logarithmic tail coefficient, with all constants depending only on the fixed angle.

## Verification

The standalone `verify.py` runs without third-party packages. It checks the factorization against 3000 direct Cartesian intersections of four independently sampled circle points, conditional mixed-moment factorizations against independent two-dimensional numerical quadrature, conditional CDFs against separate randomized sampling, the near-center and near-boundary coefficients, and the known unconditional consistency identity \(\mathbb E R^2=6/\pi^2\). A completed execution printed `PASS 3057 tests`; these finite tests do not replace the proof for every angle and radius. Run from the extracted package directory with `python verify.py`.

## Relationship to prior work

Bortolotto and Souza, *Intersections of random chords of a circle* (arXiv:2504.12866v1, 17 April 2025), Theorem 1, determine the **unconditional radial law** of the intersection of two endpoint-uniform chord *lines* (including intersections outside the disk). Conditional on the intersection being inside the disk, their result yields \(\Pr(R\le r)=6\operatorname{Li}_2(r^2)/\pi^2\). It does not present the acute-angle-conditioned radial distribution or its two fixed-angle tail laws in the examined theorem and proof sections; their unconditional distribution does not determine the joint distribution with angle.

The published research record *Conditional area law for random cyclic quadrilaterals at a fixed diagonal angle* (2026-10-25, identifier `e05b854129e9`) treats the **area of the cyclic quadrilateral** conditioned on the same acute angle. Its proof uses the same Dirichlet split and gives an independent-cosine representation for **area**, which is a sum of the two cosine variables. The present invariant \(1-R^2\) is a **product of shifted** cosine variables. Neither its conditional product distribution nor the two local radial tails is a statement of that record, although the shared gap coordinates greatly simplify this derivation. The marginal angle density and the elementary gap decomposition are explicitly prior; the new claim is the radius-conditioned product law and quantitative radial tails, not those inputs.

Bortolotto and Ramos, *On extremal problems associated with random chords on a circle* (Mathematika 71 (2025), article e70024), optimize crossing probabilities over endpoint distributions and analyze an unconditional near-boundary event. The examined introduction and main results do not address the angle-conditioned crossing radius. Koroleva and Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons* (arXiv:1301.1360), address extrema of random polygon areas/perimeters, not the crossing location given the diagonal angle.

## Limitations

The theorem applies to unit-circle **arclength-uniform endpoints** and the crossing chord-pair conditional law. It does not assert analogous formulas for uniform-disk endpoints, uniform-midpoint chords, an ellipse sampled by arclength, independent random lines without the crossing condition, or nonuniform endpoint laws. The fixed-angle error terms are not uniform at angle zero. The CDF is an exact one-dimensional integral, not a claimed elementary antiderivative. The equality \(\mathbb E R^2=6/\pi^2\), the angle marginal, and Dirichlet independence are prior or consistency facts. Historical priority remains provisional, particularly because other unindexed geometric-probability sources may treat an equivalent joint distribution.

## References

1. C. Bortolotto and V. Souza, *Intersections of random chords of a circle*, arXiv:2504.12866v1 (first public 17 April 2025), Theorem 1 and Section 2, https://arxiv.org/abs/2504.12866.
2. C. Bortolotto and J. P. G. Ramos, *On extremal problems associated with random chords on a circle*, Mathematika 71 (2025), e70024, first online 1 September 2025, https://doi.org/10.1112/mtk.70024.
3. *Conditional area law for random cyclic quadrilaterals at a fixed diagonal angle*, published research record, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-conditional-area-law-for-random-cyclic-quadrilaterals-at-a-fixed--e05b854129e9.
4. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1 (7 January 2013), https://arxiv.org/abs/1301.1360.
