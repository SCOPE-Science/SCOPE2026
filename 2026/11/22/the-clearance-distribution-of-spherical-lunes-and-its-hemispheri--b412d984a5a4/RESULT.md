# Marked near-incenter limits and the hemispherical crossover for spherical lunes

## Finding

Let \(d\ge3\), let \(0<a\le\pi/2\), and sample a point uniformly by surface area from the lune of opening \(2a\) on the round unit sphere \(S^{d-1}\). Let \(D\) be its spherical distance to the boundary. Write \(U\) for the angular offset to the closer boundary longitude, \(Q\) for squared radius in the longitude plane, \(k=(d-2)/2\), and \(E_\varepsilon=\{D>a-\varepsilon\}\). The following limits resolve the angular and transverse parts of near-maximal clearance.

* At fixed \(a<\pi/2\), set \(V=(a-U)/\varepsilon\) and \(W=(1-Q)/(2\varepsilon\cot a)\). Given \(E_\varepsilon\), \((V,W)\) converges in total variation to the density
  \[
  k(k+1)w^{k-1}\mathbf1_{\{0\le v\le1,\;0<w<1-v\}}.
  \]
  Thus the limiting barycentric coordinates are Dirichlet\((1,k,1)\). The event probability is asymptotic to \((2\cot a)^k\varepsilon^{k+1}/[a(k+1)]\).
* In the window \(a=\pi/2-\lambda\varepsilon\), \(\lambda\ge0\), retain \(V=(a-U)/\varepsilon\) and set \(W=(1-Q)/\varepsilon^2\). Put \(H_\lambda(v)=(1-v)(2\lambda+1+v)\) and \(J_\lambda=\int_0^1 H_\lambda(v)^k\,dv\). Conditionally on \(E_\varepsilon\) the limiting joint density in total variation is
  \[
  \frac{k}{J_\lambda}\,w^{k-1}\mathbf1_{\{0\le v\le1,\;0<w<H_\lambda(v)\}}.
  \]
  The event probability divided by \(\varepsilon^{2k+1}\) tends to \(2J_\lambda/\pi\). Both limits are uniform for \(\lambda\) in compact subsets of \([0,\infty)\).

At \(\lambda=0\) the exponent is \(d-1\), and the constant is \(\Gamma(d/2)/[\sqrt\pi\,\Gamma((d+1)/2)]\). As \(\lambda\to\infty\), \(J_\lambda\sim (2\lambda)^k/(k+1)\); in the critical limiting law, replacing \(W\) by \(W/(2\lambda)\) recovers the Dirichlet limit. The claim is about conditioning one point near the incenter, not about a new exact spherical-cap intersection area or the distance between random points.

## Proof

Write the first two coordinates as \(\sqrt Q(\cos\phi,\sin\phi)\), with \(0\le\phi\le 2a\); then \(U=\min(\phi,2a-\phi)\). If the angular separation to a face is at most \(\pi/2\), projection to its great hyperplane and normalization stays on that bounding hemisphere, giving distance \(\arcsin(\sqrt Q\sin\delta)\) for separation \(\delta\). Otherwise the maximum inner product with a face point is achieved on the ridge and the distance is \(\arcsin(\sqrt Q)\): the projected ray coordinate is negative and is maximized under the face constraint by setting that coordinate to zero. The nearer longitude has separation \(U\le\pi/2\) and therefore yields \(\sin D=\sqrt Q\sin U\). Zero projected length can be handled by continuity. At a hemisphere the two faces are the two halves of a single great sphere.

In a normalized Gaussian representation, azimuth is independent of the first two squared coordinates' sum and the sum of the remaining squares. Conditioning azimuth to be in the wedge gives \(U\) uniform on \([0,a]\), independent of \(Q\sim\operatorname{Beta}(1,k)\). Thus \(Z=1-Q\) has density \(k z^{k-1}\) on \((0,1)\). The boundary of the event in the coordinates \(u,z\) is exactly
\[
 a-\varepsilon<u\le a,\qquad 0<z<1-\frac{\sin^2(a-\varepsilon)}{\sin^2u}.
\]

Substitute \(u=a-\varepsilon v\), \(z=s_\varepsilon w\) with the relevant scale \(s_\varepsilon\) of the theorem. This gives the unnormalized density \((k\varepsilon/a)s_\varepsilon^k w^{k-1}\) below the graph of
\[
 H_\varepsilon(v)=\frac{\sin(u+a-\varepsilon)\sin(\varepsilon(1-v))}{s_\varepsilon\sin^2u},\qquad 0\le v\le1.
\]
For fixed \(a<\pi/2\), taking \(s_\varepsilon=2\varepsilon\cot a\) gives uniform convergence to \(1-v\). For \(a=\pi/2-\lambda\varepsilon\), the numerator is \(\sin(\varepsilon(2\lambda+1+v))\sin(\varepsilon(1-v))\) and the denominator is \(\varepsilon^2\cos^2(\varepsilon(\lambda+v))\). Thus convergence to \(H_\lambda\) is uniform on compact \(\lambda\)-ranges and \(v\in[0,1]\).

Integrating in \(w\) gives probability \((\varepsilon/a)s_\varepsilon^k\int_0^1 H_\varepsilon(v)^k\,dv\). For the joint densities before normalization, their integrated absolute difference (omitting the common prefactor) is exactly \(k^{-1}\int_0^1|H_\varepsilon(v)^k-H(v)^k|\,dv\). This tends to zero, uniformly on compact critical ranges; the normalizer there is bounded away from zero by \(J_0/k\). This proves total-variation convergence also when \(0<k<1\) and the density is unbounded near \(w=0\). For fixed opening \(\int_0^1(1-v)^k\,dv=1/(k+1)\). At \(\lambda=0\), \(J_0=\frac12 B(1/2,k+1)\), giving the stated constant. For large \(\lambda\), \(H_\lambda/(2\lambda)\to1-v\) uniformly, proving both matching formulas by the same integral argument. In the actual asymptotic overlap \(h=\pi/2-a\to0\), \(\varepsilon/h\to0\), the factored numerator divided by \(2h\varepsilon\sin^2 u\) likewise converges uniformly to \(1-v\).

## Prior work and scope

The unmarked survival function is an existing equal-cap intersection area with a change of variables. In García-Portugués, Navarro-Esteban and Cuesta-Albertos, *On a projection-based class of uniformity tests on the hypersphere*, Bernoulli 29 (2023), 181–204, [doi:10.3150/21-BEJ1454](https://doi.org/10.3150/21-BEJ1454), equation (9) and Proposition 2 give the normalized area \(A(\theta,x)\) of two inequalities of the form \(n_i\cdot X\le x\). Take the two outward unit normals, \(\theta=\pi-2a\), \(x=-\sin t\), and divide by \(A(\theta,0)=a/\pi\). The joint statement proved here concerns scaled angular and radial coordinates, not that scalar area reparametrization. The same prior paper cites Lee and Kim's 2014 cap-intersection formulas. Lassak and Musielak, arXiv:1607.00132, study lune thickness and reduced spherical bodies, not this conditioning. The marked limits do not cover other spherical cells or other sampling measures, and are at fixed dimension. Historical priority of the marked limits is provisional.

## Reproducibility

The proof is analytic. One numerical check uses the Cartesian projection density \(\frac{k}{\pi}(1-x^2-y^2)^{k-1}\) on the unit disk in the longitude plane. After rotating to the wedge midpoint, the survival region is \(x\ge \sin(t)/\sin(a)+|y|\cot(a)\) inside that disk. Integrating vertical slices for \(|y|\le\sin(a-t)\) at fixed openings and in the critical window tests the prefactors by a calculation separate from the angular threshold. Exact evaluation of a finite set of cases is not needed for the limits.
