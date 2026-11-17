# Sharp cubic deep-hole tails for orthogonal joins of regular spherical polygons

## Finding
Let \(p,q\geq3\) be integers and let \(\mathcal V_{p,q}\subset S^3\subset\mathbb R^4\) be the union of the vertices of a regular \(p\)-gon and a regular \(q\)-gon, both of circumradius one and placed in orthogonal two-planes through the origin. For an area-uniform direction \(X\in S^3\), write
\[
T_{p,q}(X)=\max_{v\in\mathcal V_{p,q}}\langle X,v\rangle.
\]
Put \(\theta=\pi/p\), \(\phi=\pi/q\), \(a=\cos\theta\), \(b=\cos\phi\), and \(c=ab/\sqrt{a^2+b^2}\). Then **the complete probability law** for \(0\leq t\leq1\) is
\[
\boxed{\mathbb P(T_{p,q}(X)\leq t)=\frac{pq}{\pi^2}\int_0^\theta\int_0^\phi\left[\min\{1,t^2\sec^2 u\}-\max\{0,1-t^2\sec^2 v\}\right]_+\,dv\,du.}
\]
Here \([z]_+=\max\{z,0\}\). In particular, \(T_{p,q}\geq c\) everywhere, with equality at precisely \(pq\) directions; equivalently the geodesic spherical covering radius is \(\rho=\arccos c\). The principal quantitative result is the **sharp near-worst-direction probability**
\[
\boxed{\mathbb P(T_{p,q}(X)\leq c+\varepsilon)=C_{p,q}\varepsilon^3+O_{p,q}(\varepsilon^4),\qquad C_{p,q}=\frac{pq(a^2+b^2)^{7/2}}{3\pi^2a^4b^4\sin\theta\sin\phi}.}
\]
Equivalently, with \(D_{p,q}(X)=\min_{v\in\mathcal V_{p,q}}\arccos\langle X,v\rangle\), the probability of being within angular distance \(\delta\) of the worst possible coverage error is \(C_{p,q}\sin^3\rho\,\delta^3+O_{p,q}(\delta^4)\). The covering-radius calculation alone is not claimed as novel; the complete law and exact cubic coefficient are the claimed contribution.

For the volume-maximizing nine-vertex four-polytope (the orthogonal square–pentagon join), \((p,q)=(4,5)\), there are exactly \(20\) deepest spherical directions; \(c=0.5324073960238528\ldots\) and \(C_{4,5}=25.091388158818\ldots\). In the cross-polytope case \((p,q)=(4,4)\), \(c=1/2\) and \(C_{4,4}=512/(3\pi^2)\).

## Assumptions and scope
The domain is all fixed integer pairs \(p,q\geq3\), with regular Euclidean polygons of unit circumradius in **orthogonal** two-dimensional subspaces. Probability refers to normalized Riemannian surface area on the *entire* unit three-sphere. All inequalities include coincident/tied nearest vertices; boundary ties have zero measure except at specified extremal directions. The error \(O_{p,q}(\varepsilon^4)\) permits a constant and a sufficiently small interval depending on the fixed pair. No claim is made for nonorthogonal, nonregular, or random vertex configurations.

## Proof
**1. Haar factorization and angular nearest vertices.** Fix orthogonal coordinates \(\mathbb R^4=\mathbb R^2\oplus\mathbb R^2\). Almost surely every \(X\in S^3\) has the representation
\[
X=(\sqrt W\cos\Phi,\sqrt W\sin\Phi,\sqrt{1-W}\cos\Psi,\sqrt{1-W}\sin\Psi).
\]
The three variables \(W,\Phi,\Psi\) are independent; \(W\) is uniform on \([0,1]\), and \(\Phi,\Psi\) are each uniform on \([0,2\pi)\). One proof is to normalize four independent standard Gaussians: the sums of squares in each two-coordinate plane are independent exponentials with the same scale, so their ratio is \(\operatorname{Beta}(1,1)\), while the two polar angles are independent uniforms. Let \(U\) be the circular angular distance from \(\Phi\) to the nearest \(p\)-gon vertex and \(V\) the corresponding distance for the \(q\)-gon. Then \(U,V,W\) are independent, with \(U\) uniform on \([0,\theta]\), \(V\) uniform on \([0,\phi]\). Therefore
\[
T_{p,q}(X)=\max\{\sqrt W\cos U,\sqrt{1-W}\cos V\}.
\]
Conditioning on \(U=u,V=v\), the event \(T_{p,q}\leq t\), for \(t\geq0\), is equivalent to the interval constraint
\[
\max\{0,1-t^2\sec^2v\}\leq W\leq\min\{1,t^2\sec^2u\}.
\]
Because \(W\) is uniform, the interval length is exactly the positive-part expression in the finding. Averaging over the independent uniform angular deviations proves the complete CDF formula.

**2. Sharp covering and equality directions.** For positive \(A,B\), the function \(\max\{rA,\sqrt{1-r^2}B\}\), \(0\leq r\leq1\), is minimized uniquely where its two arguments agree, at \(r=B/\sqrt{A^2+B^2}\), and its minimum is \(AB/\sqrt{A^2+B^2}\). This minimum is strictly increasing in \(A\) and \(B\). Since \(A=\cos U\geq a\) and \(B=\cos V\geq b\), the global minimum is \(c=ab/\sqrt{a^2+b^2}\). Equality requires \(U=\theta\), \(V=\phi\), and \(W=b^2/(a^2+b^2)\). The angular deviations are maximal exactly at the \(p\) and \(q\) polygon edge-bisector angles, respectively, giving precisely \(pq\) directions in \(S^3\).

**3. Sharp cubic tail.** Because \(c<\min\{a,b\}\), choose \(0<\varepsilon\) sufficiently small that \(t=c+\varepsilon<\min\{a,b\}\). Then the truncations in the CDF are inactive *throughout* the angle rectangle, so its integrand reduces to
\[
\left[t^2(\sec^2u+\sec^2v)-1\right]_+.
\]
At \(t=c\), the expression in brackets is nonpositive and vanishes only at \((u,v)=(\theta,\phi)\). Set \(x=\theta-u\geq0\), \(y=\phi-v\geq0\). Taylor expansion at the unique corner gives
\[
t^2(\sec^2u+\sec^2v)-1
=\frac{2\varepsilon}{c}-Ax-By+O_{p,q}(\varepsilon^2+\varepsilon(x+y)+(x+y)^2),
\]
where
\[
A=\frac{2c^2\sin\theta}{a^3}>0,\qquad B=\frac{2c^2\sin\phi}{b^3}>0.
\]
As \(\sec^2\) increases strictly with its argument in both given ranges, positivity forces \(x+y=O_{p,q}(\varepsilon)\). Rescale \(x=\varepsilon\xi\), \(y=\varepsilon\eta\). The positive-part map is 1-Lipschitz; on the uniformly bounded rescaled support, replacing the integrand by its first-order affine part changes the integral by \(O_{p,q}(\varepsilon^4)\). The elementary triangular tent integral is
\[
\int_{\xi,\eta\geq0}\left[\frac2c-A\xi-B\eta\right]_+\,d\eta\,d\xi
=\frac{(2/c)^3}{6AB}.
\]
Multiplying by \(pq\varepsilon^3/\pi^2\), and substituting \(c=ab/\sqrt{a^2+b^2}\), yields
\[
\frac{pq}{\pi^2}\frac{(2/c)^3}{6AB}=
\frac{pq(a^2+b^2)^{7/2}}{3\pi^2a^4b^4\sin\theta\sin\phi}=C_{p,q}.
\]
This proves the sharp coefficient and the order-four remainder. Since \(\cos(\rho-\delta)=c+\sin\rho\,\delta+O(\delta^2)\), substitution gives the angular formulation.

**4. Independent exact cross-polytope specialization.** When \(p=q=4\), the eight points are exactly the signed standard basis vectors of \(\mathbb R^4\), so \(T(X)=\max_i|X_i|\). Its deepest directions are the \(16\) sign patterns of \((1/2,1/2,1/2,1/2)\). In the tangent three-plane at one such direction, the leading constraints \(T\leq1/2+\varepsilon\) are \(z_i\leq\varepsilon\) and \(\sum_i z_i=0\). Writing \(w_i=\varepsilon-z_i\geq0\) gives \(\sum_i w_i=4\varepsilon\), a regular three-simplex of Euclidean three-volume \((4\varepsilon)^3\sqrt4/3!=64\varepsilon^3/3\). Dividing the total volume of all \(16\) copies by \(\operatorname{area}(S^3)=2\pi^2\) yields the independent coefficient \(512/(3\pi^2)\), agreeing with the theorem.

## Verification
A standalone standard-library script `verify.py` recomputes the constants for seven polygon pairs, integrates the exact near-tail formula with independent one-variable quadrature at two positive excesses, checks the independently derived cross-polytope coefficient, and compares the full two-angle formula against direct normalized-Gaussian sampling for three pairs. All packaged checks pass. Numerical integrations and random experiments test finite instances and do **not** replace the preceding proof for all \(p,q\).

## Relationship to prior work
Medgyes proves that the nine-vertex maximal-volume polytope on \(S^3\) is precisely the orthogonal regular square–pentagon free sum. His paper, in particular Lemma 3.2 and its proof, gives the regular-join vertex and facet structure; its main theorem concerns Euclidean four-volume, not the Haar distribution of nearest spherical vertices. Prior results on the inradius of orthogonal polygon joins already imply the covering-radius value here. Existing exact nearest-direction laws for other spherical configurations do not yield the stated all-pair integral or constant by immediate specialization. The contribution claimed here is the complete statistical law and its exact nonzero local cubic coefficient, not volume maximality or the elementary radius.

## Limitations
The formula assumes equal circumradii and orthogonal planes, and the error estimate is asymptotic for each fixed pair rather than uniform as both polygon counts diverge. The CDF is an explicit elementary double integral rather than a claim of a globally elementary antiderivative. The reported originality is based on comparisons with accessible records and literature; it is not a proof of historical priority. Independent review has not been performed.

## References
1. Csaba Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1 (first public 2026-11-06), https://arxiv.org/html/2611.10078v1.
