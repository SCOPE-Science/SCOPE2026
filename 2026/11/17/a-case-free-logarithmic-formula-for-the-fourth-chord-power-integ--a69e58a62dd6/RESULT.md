# A case-free logarithmic formula for the fourth chord-power integral of every Euclidean triangle

## Finding
For every nondegenerate Euclidean triangle \(T\) with side lengths \(a,b,c\), area \(A\), and semiperimeter \(s=(a+b+c)/2\), there is a single elementary, symmetric, non-piecewise formula for its fourth chord-power integral \(I_4(T)\).

For every cyclicly ordered triple \((r,p,q)\in\{(a,b,c),(b,c,a),(c,a,b)\}\), put
\[
z_{r;p,q}=\frac{p^2+q^2-r^2}{2pq},\qquad
H_r(p,q)=\frac{r^3-p^3}{3}+\frac{pz_{r;p,q}}2\left[(q-pz_{r;p,q})r+p^2z_{r;p,q}+p^2(1-z_{r;p,q}^2)\log\frac{s}{s-q}\right].
\]
Then
\[
\boxed{I_4(T)=\frac{4A^2}{5}\sum_{(r,p,q)}\left[\frac{H_r(p,q)}{q^2}+\frac{H_r(q,p)}{p^2}\right].}
\]
Here the second term \(H_r(q,p)\) uses exactly the same opposite side \(r\), and the logarithm inside it is \(\log(s/(s-p))\). The formula has no acute/obtuse or side-order cases. In particular, for an equilateral triangle of side \(\ell>0\),
\[
I_4(T)=\ell^5\left(\frac9{40}+\frac{27}{160}\log3\right).
\]

## Assumptions and scope
The kinematic measure \(dg\) on unoriented affine lines is normalized by \(dg=d\phi\,dh\) for the normal angle \(0\le\phi<\pi\) and signed normal offset \(h\in\mathbb R\). For a line \(g\) meeting the triangle, let \(\sigma_T(g)\) be the length of its segment in \(T\). By definition
\[
I_4(T)=\int_{\{g:g\cap T\ne\emptyset\}}\sigma_T(g)^4\,dg.
\]
Only positive, strictly triangle-inequality side triples are admitted. Heron's formula gives \(A^2=s(s-a)(s-b)(s-c)>0\); thus all logarithms have positive arguments. The result concerns the line-kinematic fourth chord moment, not the fourth moment of distances between independently sampled boundary or interior points.

## Proof
Every line through the interior of \(T\) joins points in the relative interiors of two distinct sides, up to a set of line measure zero. Group chords according to the unique vertex shared by those sides. At a vertex with adjacent side lengths \(p,q\), opposite side \(r\), and angle \(\theta\), set \(z=\cos\theta=(p^2+q^2-r^2)/(2pq)\). Parametrize the two chord endpoints by their distances \(t\in[0,p]\), \(u\in[0,q]\) from the vertex. Their separation is \(\sigma(t,u)=\sqrt{t^2+u^2-2ztu}\).

The exact Jacobian of the map from endpoint parameters to normal angle and offset is
\[
dg=\frac{tu\sin^2\theta}{\sigma(t,u)^3}\,dt\,du.
\]
Consequently this vertex's contribution equals
\[
I_4^{(r)}=\sin^2\theta\int_0^p\int_0^q tu\sqrt{t^2+u^2-2ztu}\,du\,dt.
\]
The integrand \(f(t,u)=tu\sigma(t,u)\) is homogeneous of degree three. Euler's identity implies \(\partial_t(tf)+\partial_u(uf)=5f\). Integrating over the parameter rectangle and using vanishing contributions on the two coordinate axes yields
\[
I_4^{(r)}=\frac{\sin^2\theta}{5}\left[p^2\int_0^q u\sqrt{p^2+u^2-2zpu}\,du+q^2\int_0^p t\sqrt{q^2+t^2-2zqt}\,dt\right].
\]
For \(P,Q>0\), \(-1<z<1\), the elementary antiderivative, obtained by the substitution \(w=u-Pz\), evaluates
\[
\int_0^Q u\sqrt{P^2+u^2-2Pzu}\,du
=\frac{R^3-P^3}{3}+\frac{Pz}{2}\left[(Q-Pz)R+P^2z+P^2(1-z^2)\log\frac{Q-Pz+R}{P(1-z)}\right],
\]
where \(R=\sqrt{P^2+Q^2-2PQz}\). Here \(R=r\) by the cosine law. Factoring the two positive expressions using \(2s=r+p+q\) gives
\[
\frac{q-pz+r}{p(1-z)}=\frac{s}{s-q}.
\]
Therefore the first boundary integral is \(H_r(p,q)\), and the second is \(H_r(q,p)\). Since \(pq\sin\theta=2A\), the displayed contribution becomes \(\frac{4A^2}{5}[H_r(p,q)/q^2+H_r(q,p)/p^2]\). Adding the three vertices proves the stated formula.

For \(a=b=c=\ell\), each local cosine is \(1/2\), every logarithm is \(\log 3\), and direct substitution gives the stated equilateral value. Homogeneity of \(dg\) and of chord length confirms degree five in \(\ell\).

## Verification
The accompanying `verify_chord_i4.py` reproduces the side-length formula independently against numerical quadrature in normal-angle/offset coordinates. For a fixed normal, its three vertex projections are sorted. The chord length is linear in offset on either side of the intermediate vertex projection, and its fourth-power offset integral is exactly the fourth power of the intermediate chord length times the total projected width divided by five. This calculation uses neither the vertex endpoint Jacobian nor the closed formula. Eight diverse triangles (equilateral, obtuse, right, slender, and near-degenerate) agree to the stated numerical tolerance. Four additional algebraic/homogeneity checks confirm the equilateral specialization.

## Relationship to prior work
Martirosyan and Sargsyan (2026, arXiv:2605.24616) give a symmetric logarithmic formula for the **second** kinematic chord moment, explicitly record the classical \(I_0,I_1,I_3\) values, and cite the known fifth moment; their local endpoint calculation supplies the common chord Jacobian and a useful first-power boundary integral. The present result evaluates the **fourth** moment, whose radial-length weight yields a different asymmetric pair of boundary integrals at every vertex, and eliminates all case distinctions.

Ciccariello (2010, arXiv:1006.1496) develops a complete **piecewise** isotropic triangle correlation function, from which many chord moments are in principle recoverable by further integration. Thus the novelty asserted here is the explicit uniform, case-free fourth-moment expression, not the first existence or computability of the distribution. Gates (1982) studies recognition by odd chord moments, including the fifth moment, rather than giving this fourth-moment expression. Related fourth-distance moments of random point pairs use a different sampling measure and do not imply the present kinematic identity.

## Limitations
This proves no new optimal-shape inequality, triangle-recognition theorem, or extension to other polygons. The formula is an elementary consequence of the kinematic Jacobian, homogeneity, and one-dimensional integration. The full triangle chord-length distribution was known previously, and its exact moment may be derivable from published piecewise expressions; an independent historical priority determination is not claimed. Numerical quadrature is only a cross-check, not the proof. The logarithmic formula is mathematically valid for every nondegenerate triangle but may suffer floating-point cancellation in extremely degenerate shapes.

## References
1. M. Martirosyan and R. Sargsyan, *A Closed Form for the Chord-Power Integral \(I_2\) of a Triangle*, arXiv:2605.24616 (first public version 2026-05-23), https://arxiv.org/abs/2605.24616.
2. S. Ciccariello, *The isotropic correlation function of plane figures: the triangle case*, arXiv:1006.1496 (2010), https://arxiv.org/abs/1006.1496.
3. J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873–879, DOI:10.2307/3213843.
