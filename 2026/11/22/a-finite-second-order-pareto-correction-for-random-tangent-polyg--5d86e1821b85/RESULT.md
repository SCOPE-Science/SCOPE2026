# A finite second-order Pareto correction for random tangent polygons

## Finding
Fix an integer \(n\ge4\). Choose \(n\) independent uniform contact points on the unit circle and intersect the \(n\) tangent half-planes containing the disk. Condition on the event \(B_n\) that their intersection is bounded, and let \(A_n\) denote its Euclidean area (also half its perimeter). Then, as \(t\to\infty\) with \(n\) fixed,
\[
\boxed{\Pr(A_n>t\mid B_n)=\frac{C_n}{t}+\frac{D_n}{t^2}+o(t^{-2}),}
\]
where
\[
 p_n=1-\frac{n}{2^{n-1}},\qquad
 C_n=\frac{n(n-1)}{\pi\,2^{n-2}p_n},
\]
\[
 \boxed{D_n=C_n\left[\frac{n-2}{\pi}
 +(n-1)(n-2)\int_0^1(1-u)^{n-3}\tan\!\left(\frac{\pi u}{2}\right)\,du\right]>0.}
\]
The quadrilateral has the explicit constant
\[
 \boxed{\Pr(A_4>t\mid B_4)=\frac6{\pi t}
 +\frac{72\log2+12}{\pi^2t^2}+o(t^{-2}).}
\]
Unlike the previously determined three-tangent law, the first correction for every fixed \(n\ge4\) has **no logarithmic enhancement**. The transition at four sides is caused by the finite mean of the residual area left when one normal gap approaches a semicircle.

## Assumptions and scope
The contact angles are independent and uniform on \([0,2\pi)\). Their cyclic spacings, divided by \(2\pi\), form \(Y=(Y_1,\ldots,Y_n)\sim\operatorname{Dirichlet}(1,\ldots,1)\). The boundedness event is \(B_n=\{\max_iY_i<1/2\}\), and the area is defined only on this event. A tangent gap equal to a semicircle has probability zero. This is a **fixed-side-count, large-area-threshold** theorem: the error is not uniform as \(n\to\infty\). The parameter \(t\) is in units of area for a disk of radius one.

## Proof
**1. Exact geometry and spacings.** Write \(G_i=2\pi Y_i\) for the normal-angle gaps. The intersection is bounded exactly when every \(G_i<\pi\), since its outward normals then are not all contained in a semicircle. On this event every tangent line supports a polygon side. Two successive tangents with normal gap \(G_i\) have matching tangent-segment lengths \(\tan(G_i/2)\); summing and using the unit-incircle identity (area equals semiperimeter),
\[
 A_n=\sum_{i=1}^n\tan(G_i/2).
\]
Because at most one Dirichlet coordinate can exceed \(1/2\), and \(Y_i\sim\operatorname{Beta}(1,n-1)\),
\[
 \Pr(B_n)=1-n\Pr(Y_1>1/2)=1-n2^{-(n-1)}=p_n>0.
\]

**2. Conditional residual geometry.** Choose an index \(i\), write its gap as \(G_i=\pi-\delta\), and let \(U=(U_j)_{j\ne i}\) be the other \(n-1\) gaps divided by their total \(\pi+\delta\). The Dirichlet splitting property gives
\[
 U\sim\operatorname{Dirichlet}(1,\ldots,1)\quad\text{in dimension }n-1,
\]
independently of \(\delta\). At \(\delta=0\), define the finite or infinite residual
\[
 R_0(U)=\sum_{j\ne i}\tan\!\left(\frac{\pi U_j}{2}\right).
\]
Since a coordinate of \(U\) has the \(\operatorname{Beta}(1,n-2)\) law, a union bound on the tangent singularity gives
\[
 \Pr(R_0>r)=O_n(r^{-(n-2)})\quad(r\to\infty).
\]
Thus \(\mathbb ER_0\) exists precisely for \(n\ge4\), with
\[
 \mu_n:=\mathbb ER_0=(n-1)(n-2)
 \int_0^1(1-u)^{n-3}\tan\!\left(\frac{\pi u}{2}\right)du.
\]
Also, \(\mathbb E[R_0^2\mathbf 1_{R_0\le r}]=O_n(1+\log r)\) for \(n=4\), and \(O_n(1)\) for \(n\ge5\).

**3. Quantitative exclusion of simultaneous large gaps.** If \(A_n>t\), at least one summand exceeds \(t/n\). On \(B_n\), this implies, for at least one index \(i\),
\[
 0<\delta_i:=\pi-G_i<2\arctan(n/t)<2n/t.
\]
Set \(b_t=t^{2/3}\). For a specified \(i\), the probability that \(0<\delta_i<2n/t\) and \(R_0>b_t\) is
\[
 O_n(t^{-1}b_t^{-(n-2)})
 =O_n(t^{-1-2(n-2)/3})=o(t^{-2}).
\]
Here the \(O(t^{-1})\) factor comes from the bounded marginal density of \(G_i\), and \(R_0\) is independent of \(G_i\). The union over the finitely many indices remains \(o(t^{-2})\).

On the complementary, *good* sector \(R_0\le b_t\), the other gaps are uniformly bounded away from \(\pi\) by a multiple of \(1/b_t\). Therefore, for all \(0<\delta<2n/t\) and all sufficiently large \(t\), the polygon is bounded, no second gap satisfies \(\pi-G_j<2n/t\), and exactly one index labels each rare event. This prevents double-counting at order \(t^{-2}\).

**4. Moving threshold and its averaged error.** For fixed \(U\) in the good sector, the exact area near the large gap is
\[
 F(\delta,U)=\cot(\delta/2)+R_\delta(U),\qquad
 R_\delta(U)=\sum_{j\ne i}\tan\!\left(\frac{(\pi+\delta)U_j}{2}\right).
\]
For \(0<\delta<2n/t\), the inequality \(R_0\le b_t=o(t)\) gives the uniform bounds
\[
 \cot(\delta/2)=\frac2\delta+O(\delta),\qquad
 |R_\delta-R_0|\le C_n\delta(1+R_0^2).
\]
These follow by differentiating the tangent terms and noting that their distance to a tangent pole remains a fixed fraction of its initial distance. Differentiating \(F\) gives \(\partial_\delta F=-2/\delta^2+O_n(1+R_0^2)<0\) in the threshold region for large \(t\). Consequently \(F(\delta,U)>t\) there is exactly \(0<\delta<\delta_*(U,t)\), where direct substitution and the mean-value theorem yield the uniform expansion
\[
 \delta_*(U,t)=\frac2t+\frac{2R_0(U)}{t^2}
 +O_n\left(\frac{1+R_0(U)^2}{t^3}\right).
\]
Its error has expected size \(O_n(t^{-3}(1+\log t))=o(t^{-2})\) over the good sector, by Step 2. Replacing the truncated mean of \(R_0\) by \(\mu_n\) causes only \(o(t^{-2})\) after multiplication by \(t^{-2}\); Step 3 already controls the excluded sector.

**5. Exact gap density and coefficient extraction.** Because \(Y_i\) has density \((n-1)(1-y)^{n-2}\), the density of \(\delta=\pi-G_i\) near zero is
\[
 q_n(\delta)=\frac{n-1}{2\pi}
 \left(\frac12+\frac{\delta}{2\pi}\right)^{n-2}
 =q_n(0)\left(1+\frac{n-2}{\pi}\delta+O_n(\delta^2)\right),
 \quad q_n(0)=\frac{n-1}{2\pi2^{n-2}}.
\]
Using Step 4 and averaging over \(U\), the unconditional probability that the large-gap event is labelled by this specified index is
\[
 \begin{aligned}
 \mathbb E_U\int_0^{\delta_*(U,t)}q_n(\delta)d\delta
 &=\frac{2q_n(0)}t
 +\frac{2q_n(0)}{t^2}\left(\mu_n+\frac{n-2}{\pi}\right)+o(t^{-2}).
 \end{aligned}
\]
There are exactly \(n\) mutually exclusive good labels, and excluded events have probability \(o(t^{-2})\). Multiplying by \(n\) and dividing by \(p_n\) proves both displayed coefficients.

**6. The quadrilateral and the side-count transition.** When \(n=4\), the residual coordinate has beta density \(2(1-u)\). Integration by parts gives
\[
 \int_0^1(1-u)\tan\!\left(\frac{\pi u}{2}\right)du
 =-\frac2\pi\int_0^1\log\cos\!\left(\frac{\pi u}{2}\right)du
 =\frac{2\log2}{\pi}.
\]
Thus \(\mu_4=12\log2/\pi\), \(p_4=1/2\), \(C_4=6/\pi\), and \(D_4=(72\log2+12)/\pi^2\). For \(n=3\), by contrast, \(U=(u,1-u)\) with uniform \(u\), so \(R_0=2/\sin(\pi u)\) and \(\Pr(R_0>r)\sim4/(\pi r)\). Its truncated mean diverges as \((4/\pi)\log r\); multiplying this by the known leading coefficient \(C_3=12/\pi\) reproduces the known logarithmic coefficient \(48/\pi^2\) as a consistency check, not as a new triangle theorem. The finite-mean expansion of Steps 3–5 is invalid at \(n=3\). \(\square\)

## Verification
A standalone checker in `verify.py` (Python 3; dependencies listed in `requirements.txt`) computes the beta residual integral for three fixed side counts, checks the quadrilateral identity against \((72\log 2+12)/\pi^2\), and independently reconstructs the polygon area by tangent-line intersections and the shoelace formula in 600 samples. Its randomized low-discrepancy conditional extreme-gap quadrature compares the scaled second coefficient at large finite thresholds with the theorem, and reports the bounded omitted-residual sector. On the packaged version, it returned `ALL_CHECKS_PASSED`. These finite computations are diagnostic, not an infinite proof; the threshold and error estimates above establish the asymptotic claim.

## Relationship to prior work
Fodor, Hug, and Ziebarth (2014, arXiv:1409.8105, first public 2014-09-29; primary MSC 52A22) study the volume of random circumscribed polytopes with outer truncation in a large-number-of-half-spaces regime. The present fixed-side-count, conditioned, *large-area* asymptotic is not implied by their expectation and variance estimates. Finch (2011, arXiv:1101.3931) analyzes the exact three-tangent circle model and a side-length distribution; it does not provide the four-or-more-tangent second coefficient. Xu (2015) studies the same randomly circumscribed circle polygons, but only an abstract was accessible, leaving a genuine historical-priority risk. Wang, Li, and Xu (2023) analyze Dirichlet polygon approximations and large-side-count Gaussian/extrapolation limits, not fixed-side-count area tails.

The exact \(C_n/t\) leading Pareto coefficient and conditional Dirichlet rare-shape law were already established for all fixed side counts and symmetric Dirichlet laws in previously published findings. A separate known three-tangent result has second term \((48\log t-12)/(\pi^2t^2)\). **Neither result implies the displayed finite second-order coefficient for \(n\ge4\)**: the leading-tail theorem has no rate and the triangle's divergent residual moment precludes substitution at four sides. The contribution here is the complete positive coefficient for each fixed \(n\ge4\), with explicit quadrilateral evaluation and a rigorous finite-versus-infinite residual-moment explanation for the boundary at four sides. Absence of an identical search result is not a proof of global uniqueness.

## Limitations
The theorem concerns independent uniform circle-contact points and a fixed number of sides at least four, conditioned on boundedness. It does not cover unequal contact-angle laws, noncircular support curves, random tangent offsets, uniformity in side count, or the third-order coefficient. The priority assessment is provisional, particularly because the 2015 primary article's complete text was inaccessible. Independent mathematical validation has not been performed.

## References
1. F. Fodor, D. Hug, I. Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105 (first public 2014-09-29; primary MSC 52A22), https://arxiv.org/abs/1409.8105.
2. S. R. Finch, *Three Random Tangents to a Circle*, arXiv:1101.3931 (first public 2011-01-20), https://arxiv.org/abs/1101.3931.
3. W.-Q. Xu, *Random circumscribing polygons and approximations of π*, *Statistics & Probability Letters* 106 (2015), 52–57, https://doi.org/10.1016/j.spl.2015.06.026.
4. S. Wang, Z. Li, W.-Q. Xu, *Nonlinear random extrapolation estimates of π under Dirichlet distributions*, *Journal of Numerical Analysis and Approximation Theory* 52 (2023), 273–294, https://ictp.acad.ro/jnaat/journal/article/view/1360/1463.
5. *A universal Pareto tail and Dirichlet shape limit for random tangent polygons*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-universal-pareto-tail-and-dirichlet-shape-limit-for-random-tan--916694c780b2.
6. *A sharp logarithmic second correction for random tangent-triangle area tails*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-logarithmic-second-correction-for-random-tangent-triangl--a518cd59e8fe.
