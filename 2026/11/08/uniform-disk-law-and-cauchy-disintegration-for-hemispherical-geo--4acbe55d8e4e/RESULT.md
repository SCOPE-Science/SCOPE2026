# Dimension rigidity for orthogonal projections of hemispherical geodesic midpoints

## Finding

Let \(d\ge2\) be an integer and let \(X,Y\) be independent points sampled by normalized surface area on the upper hemisphere of the unit sphere \(S^{d-1}\subset\mathbb R^d\). Let \(M=(X+Y)/\|X+Y\|\) be the shorter-geodesic midpoint, and let \(U=(M_1,\ldots,M_{d-1})\) be its orthogonal projection. **The law of \(U\) is uniform by Euclidean volume on the unit \((d-1)\)-ball if and only if \(d=3\).** More precisely, if \(\sigma_{d-1}\) is the surface area of \(S^{d-1}\), the projected density has a representative continuous at the center with value \(4/\sigma_{d-1}\). In dimensions other than three this is incompatible with uniformity, whatever the shape of the density away from the center.

The sufficiency in dimension three is the previously known midpoint area density proportional to height [1]. Below we rederive it and give conditional formulas to make the three-dimensional case explicit; the novelty claim is the dimension-rigidity theorem, not the disk marginal, a standalone geodesic-length law, or the midpoint–lune construction.

## Assumptions and scope

Sampling is by surface measure, not by volume in a solid hemisphere or isotropic-line measure. Orthogonal projection is meant literally. The boundary of the hemisphere and coincidences or antipodes have probability zero. Density assertions are almost everywhere unless a representative is specified. The construction uses ordered endpoints. Exchanging the endpoints negates the tangent direction.

## Proof of the pole-density obstruction

First take independent surface-uniform endpoints on the full sphere. Away from the coincident and antipodal sets let \(T=\tfrac12\arccos(X\cdot Y)\), and use the orthonormal pair \((M,V)\), where
\[
X=\cos T\,M+\sin T\,V,\qquad Y=\cos T\,M-\sin T\,V.
\]
At almost every fixed \(T\in(0,\pi/2)\), the joint distribution of the pair \((M,V)\) is the unique \(O(d)\)-invariant probability measure on the space of ordered orthonormal pairs; orthogonal transformations are transitive on this space. Thus \(M\) is surface-uniform and \(V\), conditional on \(M=m\), is uniform on the tangent unit sphere (two equally likely tangent directions when \(d=2\)). The distribution of \(T\) is independent of this pair.

Let \(z=m_d\). The event that both endpoints lie in the upper hemisphere has unconditional probability \(1/4\) and is equivalent to \(z\cos T\ge |V_d|\sin T\). On the upper open hemisphere, write \(A(m)\) for its probability under the stated conditional law of \(T,V\). A density representative for the conditioned midpoint relative to spherical area is \(4A(m)/\sigma_{d-1}\). The inequality \(|V_d|\le\sqrt{1-z^2}\) gives the bounds
\[
\Pr\big\{\sqrt{1-z^2}\,\sin T\le z\cos T\big\}\le A(m)\le1.
\]
As \(z\to1\), the indicator in the lower bound tends to one for every \(T\in(0,\pi/2)\). Dominated convergence yields \(A(m)\to1\) and \(A(e_d)=1\). This also proves continuity at the pole without relying on continuity of a chosen tangent frame. In the upper-hemisphere coordinates \(u=(m_1,\ldots,m_{d-1})\), the surface element is \(du/z\). The projected density is consequently \(4A(m)/(\sigma_{d-1}z)\) on the open ball; in particular it is continuous at \(u=0\) with value \(4/\sigma_{d-1}\).

If the ball law were uniform, its constant density would be \(1/\kappa_{d-1}\), where \(\kappa_{d-1}=\pi^{(d-1)/2}/\Gamma((d+1)/2)\). Almost-everywhere equality with that constant and continuity at the center force \(\sigma_{d-1}/\kappa_{d-1}=4\). Writing
\[
r(d)=\frac{\sigma_{d-1}}{\kappa_{d-1}}=2\sqrt\pi\,\frac{\Gamma((d+1)/2)}{\Gamma(d/2)},
\]
one has \(r(2)=\pi\), \(r(3)=4\), \(r(4)=3\pi/2>4\), and \(r(d+2)=\frac{d+1}{d}r(d)>r(d)\). Hence among integers \(d\ge2\) the condition holds exactly at three. The calculation below proves sufficiency, completing the theorem.

## The known dimension-three marginal and an explicit disintegration

In dimension three the full-sphere dot product is uniform on \([-1,1]\), so \(W=\sin^2 T=(1-X\cdot Y)/2\) is uniform on \([0,1]\) before conditioning. For \(0<z=m_3<1\) use the tangent frame \(e_1=(e_3^{\mathrm{std}}-zm)/\sqrt{1-z^2}\) and \(e_2=m\times e_1\), where \(e_3^{\mathrm{std}}=(0,0,1)\). With \(V=\cos\phi\,e_1+\sin\phi\,e_2\), the two endpoint heights are \(z\cos T\pm\sqrt{1-z^2}\cos\phi\sin T\). Their simultaneous nonnegativity is equivalent, up to null boundaries, to \(W<q(z,\phi)\), where
\[
q(z,\phi)=\frac{z^2}{z^2+(1-z^2)\cos^2\phi}.
\]
The full-sphere density relative to \(d\sigma(m)\,d\phi\,dw\) is \(1/(8\pi^2)\) on its support, so after conditioning it is \(1/(2\pi^2)\) on \(z>0\) and \(0<w<q(z,\phi)\), zero elsewhere.

Integrating over \(w\) and \(\phi\) gives the midpoint spherical density \(z/\pi\): the needed integral of \([z^2+(1-z^2)\cos^2\phi]^{-1}\) over \([0,2\pi)\) is \(2\pi/z\), by the substitution \(a=\tan\phi\) on each quadrant. Since \(d\sigma=du/z\), the projected density is the constant \(1/\pi\). Thus \(Z=M_3\) has density \(2z\), and \(Z^2\) and \(1-Z^2\) are both uniform.

Dividing the joint midpoint-angle density by \(z/\pi\) shows that given \(M=m\), the angle has density \(z/[2\pi(z^2+(1-z^2)\cos^2\phi)]\). This depends only on \(z\). The density of \(a=\tan\phi\) after reducing the angle modulo \(\pi\) is \(z/[\pi(1+z^2a^2)]\), the Cauchy density with scale \(1/z\). The two possible lifts to an angle modulo \(2\pi\) are equally likely; given \((z,\phi)\), \(W\) is uniform on \([0,q(z,\phi)]\). The same conditional angular density gives
\[
\mathbb E[\cos^2\phi\mid Z=z]=\frac{z}{1+z},\qquad
\mathbb E[\cos^2\phi]=\int_0^1\frac{2z^2}{1+z}\,dz=2\log2-1.
\]
For the first identity use \(\cos^2\phi/[z^2+(1-z^2)\cos^2\phi]=(1-z^2)^{-1}\big(1-z^2/[z^2+(1-z^2)\cos^2\phi]\big)\) and the preceding integral. The conditional law supplies a sampler: draw a uniform disk point, lift it to \(m\) with positive height, draw the Cauchy tangent variable and an independent fair choice of lift, and draw \(W\) uniformly up to \(q\). Reconstruct \(X,Y\) from \(T=\arcsin\sqrt W\) and \(V\) above.

## Prior coverage and verification

The accepted 2012 answer in [1] gives the midpoint spherical density proportional to \(\cos\theta\) and the polar-angle density proportional to \(\sin(2\theta)\) for the same normalized-sum model; \(\cos\theta=z\) makes this precisely the disk-uniform marginal after orthogonal projection. A separate answer on the same page identifies the uniform squared height numerically. The midpoint–lune Jacobian approach in [1] is also relevant to the disintegration calculation. Neither answer states the comparison between the center value \(4/\sigma_{d-1}\) and \(1/\kappa_{d-1}\) in arbitrary dimension. The halfsphere hull work [2] concerns sampling in the same region but has a different observable. Results on Euclidean straight chords in a solid hemisphere, as in [3], use a different sampling model.

The proof is analytic. The accompanying unchanged `check_midpoint.py` supplies finite Monte Carlo corroboration of the dimension-three sampling laws, including radius, midpoint-height and angle moments and checks of a factorized sampler. It also compares the pole-density criterion for ambient dimensions 2–25 and checks auxiliary length statistics not claimed as a result here. With NumPy installed it can be run as `python check_midpoint.py`; its success marker is `HEMISPHERE_GEODESIC_MIDPOINT_UNIFORM_DISK_AND_CAUCHY_OK`. These checks cannot certify the all-dimension assertion. The theorem concerns the stated surface-endpoint model and orthogonal projection only; it does not classify other caps, sampling weights, or projections.

## References

1. joriki, accepted answer to *Distribution of sum of two directions on hemisphere?*, Mathematics Stack Exchange, 25 May 2012 (UTC), [answer 149572](https://math.stackexchange.com/a/149572). See also Sasha's [answer 149366](https://math.stackexchange.com/a/149366), 24 May 2012 (UTC).
2. I. Bárány, D. Hug, M. Reitzner and R. Schneider, *Random points in halfspheres*, [arXiv:1505.04672](https://arxiv.org/abs/1505.04672).
3. W. Gille, *Chord Length Distributions of the Hemisphere*, *Journal of Mathematics and Statistics* **1** (2005), 24–28, [doi:10.3844/jmssp.2005.24.28](https://doi.org/10.3844/jmssp.2005.24.28).
