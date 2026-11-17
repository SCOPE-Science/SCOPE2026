# Boundary-sampled polygon deficits: a joint corner law and an inverse angle signature

## Finding
Let \(K\) be a planar convex polygon with \(m\ge3\) genuine vertices, perimeter \(P\), and interior angles \(\theta_i\in(0,\pi)\). Let \(K_n\) be the convex hull of \(n\) independent arclength-uniform points of \(\partial K\). For independent unit-mean exponential variables \(E_i,F_i\), as \(n\to\infty\),
\[
\left(\frac{n^2\,[A(K)-A(K_n)]}{P^2},\;\frac{n\,[P-L(K_n)]}{P}\right)
\Rightarrow
\left(\frac12\sum_{i=1}^m\sin\theta_i E_iF_i,\;
\sum_{i=1}^m\big[E_i+F_i-\sqrt{E_i^2+F_i^2-2E_iF_i\cos\theta_i}\big]\right).
\]
Here \(A\) is Euclidean area and \(L\) perimeter. Convergence extends to every fixed mixed nonnegative integer moment. In particular,
\[
\lim_{n\to\infty}\frac{n^2}{P^2}\mathbb E[A(K)-A(K_n)]
=\frac12\sum_i\sin\theta_i,
\qquad
\lim_{n\to\infty}\frac{n^4}{P^4}\operatorname{Var}(A(K)-A(K_n))
=\frac34\sum_i\sin^2\theta_i.
\]
More sharply, for a constant \(c_K>0\),
\[
\mathbb E[A(K)-A(K_n)]
=\frac{P^2}{2(n+1)(n+2)}\sum_i\sin\theta_i+O_K(e^{-c_K n}).
\]
Set \(T=\frac12\sum_i\sin\theta_i E_iF_i\). Its complete Laplace transform is
\[
\mathbb E[e^{-sT}]=\prod_{i=1}^m\int_0^\infty\frac{e^{-u}}{1+(s/2)u\sin\theta_i}\,du,\qquad s\ge0.
\]
For a known \(m\), the distribution of \(T\) determines precisely the unordered multiset \(\{\sin\theta_i\}_{i=1}^m\). Consequently, for triangles it determines the similarity class, by the sine rule. Finally, Jensen's inequality gives the sharp angular extremum
\[
\frac12\sum_i\sin\theta_i\le\frac m2\sin\frac{2\pi}{m},
\]
with equality precisely for equiangular polygons (for triangles, equilateral).

## Assumptions and scope
All polygons are compact, convex, full-dimensional, and listed without artificial collinear vertices. Distances on the boundary are arclength, sampled independently and uniformly. Polygonal edges have strictly positive lengths. The two deficits are nonnegative. The number \(m\) and polygon \(K\) are fixed while \(n\to\infty\); no joint growth of \(m\) with \(n\) is asserted. Exponentials for distinct vertices and between the two adjacent sides of a vertex are independent. The inverse-angle conclusion is conditioned on knowing the number of genuine vertices; in general it does not recover their cyclic order or edge lengths.

## Proof
**1. Corner decomposition.** Let vertex \(v_i\) have incoming and outgoing edge lengths \(a_i,b_i>0\). Write \(X_{i,n}\) and \(Y_{i,n}\) for the arclength from \(v_i\) to its nearest sampled point on the incoming and outgoing edge, respectively; if an edge is empty, use its full length. On the event \(G_n\) that each edge has at least two samples, the convex hull connects those nearest points across each original vertex and retains each sampled edge's intervening straight segment. Its exact missing region is the union of nonoverlapping corner triangles. Thus
\[
A(K)-A(K_n)=\frac12\sum_i\sin\theta_i\,X_{i,n}Y_{i,n}.
\]
The straight replacement chord is \(\sqrt{X_{i,n}^2+Y_{i,n}^2-2X_{i,n}Y_{i,n}\cos\theta_i}\), yielding
\[
P-L(K_n)=\sum_i\left(X_{i,n}+Y_{i,n}-\sqrt{X_{i,n}^2+Y_{i,n}^2-2X_{i,n}Y_{i,n}\cos\theta_i}\right).
\]
For an edge of length \(\ell\), the chance it contains fewer than two points is \((1-\ell/P)^n+n(\ell/P)(1-\ell/P)^{n-1}\). A finite union bound gives \(\mathbb P(G_n^c)=O_K(e^{-c n})\) for some \(c>0\).

**2. Joint corner-gap limit.** Fix nonnegative thresholds for the \(2m\) scaled gaps, and choose \(n\) so large that the corresponding short intervals along the polygonal sides do not overlap. For total scaled threshold length \(r\), the joint upper-tail probability that all the relevant boundary intervals avoid all \(n\) samples equals \((1-r/n)^n\), tending to \(e^{-r}\). Therefore
\[
\left(\frac{nX_{i,n}}P,\frac{nY_{i,n}}P\right)_{i=1}^m\Rightarrow(E_i,F_i)_{i=1}^m.
\]
The continuous mapping theorem and Step 1 prove the displayed joint limit. For each individual gap \(Z\) and \(0\le t\le n\), \(\mathbb P(nZ/P>t)\le e^{-t}\) using the interval-avoidance formula (and the clipped-edge convention). This uniform exponential-tail bound controls all fixed moments of polynomial functions of the gaps by Hölder's inequality. On \(G_n^c\), geometric deficits are bounded above by \(A(K)\) and \(P\), so their rescaled fixed moments contribute at most a polynomial in \(n\) times \(\mathbb P(G_n^c)\). Uniform integrability follows. Since \(\mathbb E(EF)=1\) and \(\operatorname{Var}(EF)=4-1=3\), the mean and variance limits follow.

**3. Exponentially accurate mean.** For one vertex with adjacent lengths \(a,b\), the joint survival function for \(0\le x<a\), \(0\le y<b\) is
\[
\mathbb P(X_{i,n}>x,Y_{i,n}>y)=(1-(x+y)/P)^n.
\]
Integrating over the rectangle gives exactly
\[
\mathbb E[X_{i,n}Y_{i,n}]=\frac{P^2}{(n+1)(n+2)}
\left[1-(1-a/P)^{n+2}-(1-b/P)^{n+2}
+(1-(a+b)/P)^{n+2}\right].
\]
The last three terms are exponentially small. Replace the true deficit by its corner sum on \(G_n\). Their difference vanishes on \(G_n\) and is uniformly bounded on its complement; Step 1 finishes the expectation statement, after absorbing polynomial factors into a weaker exponential rate.

**4. Laplace transform, inversion, and shape.** Conditional on \(E_i=u\), \(\mathbb E[e^{-s c_i E_iF_i}\mid E_i=u]=(1+s c_i u)^{-1}\), where \(c_i=\frac12\sin\theta_i>0\). Independence yields the product formula. To recover \(\{c_i\}\), denote the largest coefficient by \(c_*\). The standard exponential-product estimate follows from AM–GM and one matching lower-tail event:
\[
\lim_{x\to\infty}\frac{\log\mathbb P(EF>x)}{\sqrt x}=-2.
\]
Indeed \(EF>x\) implies \(E+F>2\sqrt x\), and the event \(E,F>\sqrt x\) gives the matching lower bound. With independent \(G=\sum_i E_i\) and \(H=\sum_i F_i\), both Gamma\((m,1)\),
\[
c_*E_{i_*}F_{i_*}\le T\le c_*GH.
\]
Gamma tails have the same leading exponential decay as exponential tails; applying the preceding AM–GM argument and lower tail to \(GH\) gives
\[
\lim_{x\to\infty}\frac{\log\mathbb P(T>x)}{\sqrt x}=-\frac2{\sqrt{c_*}}.
\]
Thus the law fixes \(c_*\). Divide its Laplace transform by the known strictly positive factor \(\int_0^\infty e^{-u}/(1+s c_*u)\,du\) and repeat on the resulting law of the sum with one term removed. Induction recovers the full coefficient multiset. For \(m=3\), the three edge lengths are proportional to the sines of their opposing angles, hence the recovered multiset fixes a triangle up to similarity. Finally \(\sum_i\theta_i=(m-2)\pi\); strict concavity of sine on \((0,\pi)\) gives the sharp mean coefficient, with equality iff all angles equal.

## Verification
The accompanying standalone `check_corner_law.py` uses only the Python standard library. It reconstructs actual boundary-sampled convex hulls rather than substituting corner triangles, checks their area and perimeter against the exact corner identities, simulates the limiting exponential-product distribution, and tests mean, variance, finite-sample integration and the polygonal angle bound for three noncongruent test polygons. Running `python check_corner_law.py` prints `BOUNDARY_POLYGON_CORNER_LAW_CHECKS_PASSED`. Those tests are finite diagnostics: Steps 1–4 provide the proofs for all polygon orders and sample sizes in the theorem's scope.

## Relationship to prior work
Reitzner, Schütt and Werner prove asymptotic **expected** volume deficits for boundary-sampled simple polytopes; their work establishes the relevant research setting but not this joint planar deficit law, its exponential-product spectrum or its inverse angle classification. Prochno, Schütt, Sonnleitner and Werner prove the polygonal **Hausdorff** approximation law, which uses related vertex-gap geometry but a different observable (a maximum rather than an additive area or perimeter deficit). Groeneboom and Pardon study random convex hulls of samples from polygonal **interiors**, not arclength-uniform boundary sampling. The joint limiting law, all-moment statement, inverse angle signature and finite-sample refinement are the claims assessed here. Older or differently phrased laws may exist; the comparison is not a certification of historical priority.

## Limitations
The limit assumes fixed \(K\) and independent arclength-uniform boundary sampling. It does not establish convergence rates for the full two-dimensional distribution, recover cyclic angle order, or classify bodies outside polygons. The result does not claim a universal law independent of angles: the corner law depends on their sine and cosine values. The derived moment bounds are asymptotic. Independent audit has not been performed.

## References
1. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (initially 2019-11-14), *Discrete & Computational Geometry* 69 (2023), 453–504, DOI 10.1007/s00454-022-00460-2.
2. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff distance*, *Mathematische Annalen* 392 (2025), 4525–4542, DOI 10.1007/s00208-025-03186-7.
3. P. Groeneboom, *Convex hulls of uniform samples from a convex polygon*, arXiv:1109.3118 (2011). This source considers interior samples.
4. J. Pardon, *Central limit theorems for random polygons in an arbitrary convex set*, *Annals of Probability* 39 (2011), 881–903, DOI 10.1214/10-AOP568. This source considers interior samples.
