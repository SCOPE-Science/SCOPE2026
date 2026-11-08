# A sharp Pareto area law for bounded random circle-circumscribing polygons

## Finding

Fix an integer \(n\ge3\). Choose \(n\) independent uniform points on the circumference of the Euclidean unit disk, and form the intersection \(P_n\) of the \(n\) supporting half-planes tangent at those points and containing the disk. Let \(B_n\) denote the event that \(P_n\) is bounded, and write \(A_n=\operatorname{area}(P_n)\) on that event. Then

\[
\Pr(B_n)=1-\frac{n}{2^{n-1}}>0,
\qquad
\lim_{t\to\infty}t\Pr(B_n, A_n>t)
=\frac{n(n-1)}{2^{n-2}\pi}.
\]

In particular, the **conditional** area has the sharp Pareto tail

\[
\boxed{\displaystyle
\Pr(A_n>t\mid B_n)\sim
\frac{n(n-1)}{\pi(2^{n-2}-n/2)}\,\frac1t
=\frac{2n(n-1)}{\pi(2^{n-1}-n)}\,\frac1t.}
\]

For every real \(q>0\),
\[
\mathbb E[A_n^q\mid B_n]<\infty \quad\Longleftrightarrow\quad 0<q<1.
\]

Thus conditioning on a genuine bounded circumscribing polygon does **not** make its mean area finite, for any finite sample size. For \(n=3\), the unconditioned joint tail constant is \(3/\pi\) and the conditional tail constant is \(12/\pi\). Since its inradius is one, the polygon's perimeter equals \(2A_n\) on \(B_n\); this is the same area theorem under deterministic rescaling, not a separate result.

## Assumptions and scope

The contact points are independent and exactly uniform in angle. Tangent lines and support half-planes are taken at **all** selected points; no outer truncation, sample-size limit, or approximation is used. The random intersection is unbounded outside \(B_n\), so area is deliberately defined only on \(B_n\). All claims hold for every fixed integer \(n\ge3\); the asymptotic variable \(t\to\infty\) is the area threshold, not \(n\). A disk of radius \(R>0\) gives the same normalized theorem for \(A_n/R^2\).

## Proof

**1. Circular spacings and the boundedness event.** Take the first labeled sample point as cyclic origin, rotate its angle to zero, and order the other \(n-1\) independent uniform angles around the circle. Let \(Y_1,\ldots,Y_n\) be the \(n\) successive positive angular gaps divided by \(2\pi\), including the final gap back to that chosen contact point. Then \(\sum_iY_i=1\) and
\[
(Y_1,\ldots,Y_n)\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
Indeed, the ordered \(n-1\) relative angles have constant joint density on their simplex and successive differences have unit Jacobian. **Anchoring at a sampled contact point is essential:** anchoring the order at a fixed external zero-angle instead would size-bias its wrapping gap. The geometric quantities do not depend on which sampled point starts the cyclic order. Each single gap has density \((n-1)(1-y)^{n-2}\) for \(0<y<1\). In particular, for \(0\le s\le1\),
\[
\Pr(Y_i>s)=(1-s)^{n-1},
\]
and, for two distinct indices and \(s_1+s_2\le1\),
\[
\Pr(Y_i>s_1,Y_j>s_2)=(1-s_1-s_2)^{n-1}.
\]
The second formula is a direct translation of the uniform simplex, so it is exact for all such parameters.

The support half-planes have bounded intersection exactly when the normal directions are not contained in a closed semicircle, equivalently when no successive angular gap is at least \(\pi\). Up to null endpoints,
\[
B_n=\{\max_iY_i<1/2\}.
\]
The events \(\{Y_i>1/2\}\) are pairwise disjoint, each with probability \(2^{-(n-1)}\). Consequently \(\Pr(B_n)=1-n2^{-(n-1)}\). For \(n\ge3\) this is strictly positive.

**2. Exact geometric area functional.** On \(B_n\), each selected tangent defines a genuine side of the circumscribed polygon. The two tangents whose contact directions have gap \(2\pi Y_i<\pi\) intersect at a point whose two tangent segments to the circle each have length \(\tan(\pi Y_i)\). Summing the two tangent lengths at each polygon vertex gives perimeter \(2\sum_i\tan(\pi Y_i)\). The inradius is exactly one and the area is inradius times semiperimeter, hence
\[
A_n=\sum_{i=1}^n \tan(\pi Y_i) \qquad\text{on }B_n.
\]
All terms are nonnegative there, and only gaps approaching \(1/2\) can make this area large.

**3. One-gap tail and negligible double extremes.** Define the nonnegative random variables \(T_i=\boldsymbol1_{B_n}\tan(\pi Y_i)\). For \(t>0\), put
\[
\delta_t=\frac{1}{\pi}\arctan(1/t),\qquad t\delta_t\longrightarrow\frac1\pi.
\]
Then \(\{T_i>t\}=B_n\cap\{1/2-\delta_t<Y_i<1/2\}\). The exact one-gap density gives
\[
\Pr(1/2-\delta<Y_i<1/2)
=(1/2+\delta)^{n-1}-2^{-(n-1)}.
\]
Any part of this strip excluded by \(B_n\) requires some \(Y_j\ge1/2\), \(j\ne i\). The two-gap simplex formula bounds the excluded mass by \((n-1)\delta^{n-1}\). Because \(n\ge3\), this is \(o(\delta)\). Therefore
\[
\lim_{t\to\infty}t\Pr(T_i>t)
=\frac{n-1}{2^{n-2}\pi}.
\]
For distinct \(i,j\), the event \(T_i>u,T_j>u\) forces both normalized gaps to exceed \(1/2-\delta_u\). Exactly,
\[
\Pr(T_i>u,T_j>u)
\le(2\delta_u)^{n-1}=O(u^{-(n-1)})=o(u^{-1}).
\]
This bound remains valid even when two nearly antipodal gaps occur simultaneously.

**4. From one extreme to their sum.** With \(T=\sum_iT_i\), obviously \(\max_iT_i\le T\). For every fixed \(0<\varepsilon<1/n\), if \(T>t\) and \(\max_iT_i\le(1-(n-1)\varepsilon)t\), then at least two of the \(T_i\) exceed \(\varepsilon t\). Thus
\[
\Pr(\max_iT_i>t)\le \Pr(T>t)
\le\Pr(\max_iT_i>(1-(n-1)\varepsilon)t)
+\sum_{i<j}\Pr(T_i>\varepsilon t,T_j>\varepsilon t).
\]
The double-exceedance sum is \(o(t^{-1})\), while finite inclusion-exclusion shows
\[
\Pr(\max_iT_i>t)\sim\frac{n(n-1)}{2^{n-2}\pi t}.
\]
Multiply the upper and lower bounds by \(t\), take the limit, then let \(\varepsilon\downarrow0\). Since \(T=A_n\) on \(B_n\) and \(T=0\) elsewhere, this proves the stated joint and conditional tail constants.

**5. Sharp moment threshold.** The identity
\[
\mathbb E[A_n^q\mid B_n]=q\int_0^\infty t^{q-1}\Pr(A_n>t\mid B_n)\,dt
\]
holds in the extended sense for \(q>0\). The tail is asymptotic to a strictly positive constant times \(1/t\). The integral at infinity therefore converges exactly for \(q<1\); the bounded interval contributes finitely. This proves the if-and-only-if criterion.

## Verification

The independent standard-library script `verify_tail.py` checks the exact simplex-strip and pair-overlap identities, evaluates the coefficient for several sample sizes, and uses a seeded, independently generated uniform-angular-gap simulation to compare high-threshold survival probabilities with the exact coefficient. The observed numerical checks are explicitly finite experiments: the proof of the tail and moment statements is the preceding analytic argument. Run with `python3 verify_tail.py` (Python 3.9 or newer, standard library only).

## Relationship to prior work

Böröczky--Fodor--Hug (arXiv:0901.3419) and Fodor--Hug--Ziebarth (arXiv:1409.8105, first publicly posted 2014-09-29) study approximation by random circumscribed half-spaces and work with outer truncation to control unbounded cells; their main results concern asymptotic mean widths, volumes, and variances under other sampling conditions. Xu (2015, DOI below) studies exactly the tangent-at-random-circle-points construction, recognizes the semicircle obstruction and potentially unbounded magnitudes, and proves large-sample approximation results. Wang--Li--Xu (2023, DOI below), inspected in accessible complete HTML text, explicitly writes the tangent-gap sum and studies concentration and normal approximations in the sample-size limit. These prior representations and limit statements are credited; the assessed assertion is the **fixed-sample, conditional, sharp \(1/t\) tail coefficient for all \(n\ge3\) together with the exact moment threshold**, which is not an implication of the cited large-sample asymptotics. The complete Xu (2015) primary text was not accessible during this comparison, so historical priority remains provisional.

## Limitations

The law addresses a disk, iid uniform contacts, and exactly fixed sample size. It does not supply a uniform-in-\(n\) error estimate for the displayed tail equivalence, a rate of convergence, or a general smooth-convex-body analogue. It does not say that the tangent model has finite expected area after conditioning: the theorem asserts the opposite. The historical-priority comparison cannot rule out an exact fixed-\(n\) tail theorem in material not available for inspection. No independent validation has been performed.

## References

- F. Fodor, D. Hug, I. Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105, first submitted 2014-09-29. https://arxiv.org/abs/1409.8105
- K. Böröczky, F. Fodor, D. Hug, *The mean width of random polytopes circumscribed around a convex body*, arXiv:0901.3419 (2009). https://arxiv.org/abs/0901.3419
- W.-Q. Xu, *Random circumscribing polygons and approximations of π*, Statistics & Probability Letters 106 (2015), 52–57. https://doi.org/10.1016/j.spl.2015.06.026
- S. Wang, Z. Li, W.-Q. Xu, *Nonlinear random extrapolation estimates of π under Dirichlet distributions*, Journal of Numerical Analysis and Approximation Theory 52 (2023), 273–294. https://doi.org/10.33993/jnaat522-1360
