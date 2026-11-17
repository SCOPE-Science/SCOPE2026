# Exact incenter and phase laws for boundary-uniform ideal hyperbolic triangles

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) carry the Poincaré metric of constant curvature \(-1\). Choose three independent points on \(\partial\mathbb D\), each uniformly distributed in Euclidean angle. The ideal hyperbolic triangle they determine has a unique hyperbolic incenter \(Z\). Relative to Euclidean planar area \(dx\,dy\), its exact density is

\[
 f_Z(z)=\frac{3\sqrt 3}{\pi^2(1+|z|^2+|z|^4)},\qquad |z|<1.
\]

Equivalently, the complete distribution of \(U=|Z|^2\) is

\[
 \Pr(U\le u)=\frac6\pi\left[\arctan\!\left(\frac{1+2u}{\sqrt3}\right)-\frac\pi6\right],\qquad 0\le u\le1.
\]

The density of \(U\) is strictly decreasing. Consequently \(\Pr(U\le u)>u\) for every \(0<u<1\): the incenter is strictly more concentrated toward the Euclidean disk center than a uniformly area-sampled point. In particular,

\[
 \mathbb E|Z|^2=\frac{3\sqrt3\log3}{2\pi}-\frac12.
\]

For the hyperbolic radial distance \(D=d_{\mathbb H}(0,Z)=2\operatorname{artanh}|Z|\),

\[
 \Pr(D>T)=\frac{4\sqrt3}{\pi}e^{-T}+O(e^{-2T})\qquad(T\to\infty).
\]

There is also a joint orientation law. Condition on the three *labelled* sampled boundary points being positively cyclically ordered. With \(\omega=e^{2\pi i/3}\), write their unique oriented parametrization as

\[
 \zeta_j=\frac{Z+e^{it}\omega^j}{1+\overline Z e^{it}\omega^j},\qquad j=0,1,2,\quad t\in[0,2\pi).
\]

Then, conditionally on \(Z=z\), the orientation \(t\) has density

\[
 f_{t\mid Z=z}(t)=\frac{1-|z|^6}{2\pi\,|1+\overline z^{\,3}e^{3it}|^2}.
\]

This is a threefold Poisson kernel; for nonzero \(z\), its third angular Fourier coefficient relative to \(\arg z\) is \(-|z|^3\). No orientation law is claimed to be invariant under arbitrary disk automorphisms, since the sampling measure is Euclidean boundary-uniform rather than Möbius-invariant.

## Assumptions and scope

Three labelled ideal vertices are independent and uniform in Euclidean boundary angle. Coincident vertices occur with probability zero. All distances to triangle sides and all incircles are hyperbolic. In the joint law, conditioning on positive cyclic order (probability \(1/2\)) fixes the orientation and the labelling of the first vertex. The density of \(Z\), the squared-radius distribution and its consequences do not depend on ordering or labelling. The Poincaré metric has line element \(2|dz|/(1-|z|^2)\).

## Proof

**1. Parametrization by incenter and orientation.** Every positively oriented triple of distinct boundary points is the unique image of \((1,\omega,\omega^2)\) under an orientation-preserving disk automorphism. The equilateral ideal triangle has incenter at zero, and disk automorphisms are hyperbolic isometries; hence its image incenter is \(z\) if the automorphism is

\[
 G_{z,t}(w)=\frac{z+e^{it}w}{1+\overline z e^{it}w}.
\]

Thus \((z,t)\mapsto(\zeta_0,\zeta_1,\zeta_2)\) is a smooth bijection between \(\mathbb D\times[0,2\pi)\) (with the angle endpoints identified) and the positively cyclically ordered triples. Its inverse is the Möbius normalization sending the ordered cubic roots of unity to the triple. The uniqueness also follows from the sharp three-transitivity of disk automorphisms on positively ordered boundary triples.

**2. Three-angle Jacobian.** Let \(\theta_j=\arg\zeta_j\). Direct logarithmic differentiation yields

\[
 d\theta_j=\operatorname{Im}\left(\frac{dz+i e^{it}\omega^jdt}{z+e^{it}\omega^j}-\frac{e^{it}\omega^j d\overline z+i\overline z e^{it}\omega^jdt}{1+\overline z e^{it}\omega^j}\right).
\]

The absolute determinant of these three one-forms relative to \((dx,dy,dt)\) is

\[
 J(z,t)=\frac{6\sqrt3(1-|z|^2)}{|1+\overline z^{\,3}e^{3it}|^2}.
\]

For clarity, this determinant can also be obtained without expanding all its entries. The three-point measure \(d\theta_0d\theta_1d\theta_2/\prod_{i<j}|\zeta_i-\zeta_j|\) is invariant under disk automorphisms, and in the above center/orientation coordinates is \(2\,dx\,dy\,dt/(1-|z|^2)^2\); the factor \(2\) comes from evaluating the determinant at \(z=0\), where the three rows are \((-2\sin(t+2\pi j/3),\,2\cos(t+2\pi j/3),\,1)\) and the absolute determinant is \(6\sqrt3\). The boundary chord product obeys

\[
 \prod_{i<j}|\zeta_i-\zeta_j|=\frac{3\sqrt3(1-|z|^2)^3}{|1+\overline z^{\,3}e^{3it}|^2},
\]

which gives the displayed \(J\). This is a finite-dimensional change-of-variables identity, not a stochastic limit.

**3. Joint law and marginal.** On positive cyclic order, the angular density of the original labelled triple is \(2/(2\pi)^3=1/(4\pi^3)\). Thus

\[
 f_{Z,t}(z,t)=\frac{3\sqrt3(1-|z|^2)}{2\pi^3|1+\overline z^{\,3}e^{3it}|^2}.
\]

The elementary Poisson integral

\[
 \int_0^{2\pi}\frac{dt}{|1+\overline z^{\,3}e^{3it}|^2}=\frac{2\pi}{1-|z|^6}
\]

implies

\[
 f_Z(z)=\frac{3\sqrt3}{\pi^2}\frac{1-|z|^2}{1-|z|^6}=\frac{3\sqrt3}{\pi^2(1+|z|^2+|z|^4)}.
\]

The opposite cyclic orientation gives the same marginal by exchanging two labels. Dividing the joint density by this marginal proves the conditional orientation kernel.

**4. Radial integration and geometric consequences.** In polar coordinates, \(U=|Z|^2\) has density \(3\sqrt3/[\pi(1+u+u^2)]\), \(0<u<1\). Its integral is the claimed arctangent formula, normalized by \(\int_0^1(1+u+u^2)^{-1}du=\pi/(3\sqrt3)\). The density is strictly decreasing; any strictly decreasing probability density on \((0,1)\) has distribution function strictly above the uniform CDF there. Integration of \(u/(1+u+u^2)\) yields the moment.

Finally, \(1-\tanh^2(T/2)=4e^{-T}+O(e^{-2T})\) and the squared-radius density extends continuously to \(u=1\), where its value is \(\sqrt3/\pi\). Taylor expansion of the survival function at this endpoint gives the exponential tail with the stated remainder. The conditional Poisson kernel has the claimed Fourier coefficient by the ordinary Poisson-kernel identity.

## Verification

The standalone `verify.py` implements three independent diagnostics: finite-difference differentiation of the geometric parametrization; numerical quadrature for normalization, the exact moment and the large-distance coefficient; and an independent Cartesian complex-linear reconstruction of the incenter from directly simulated random boundary triples. The last test does not use the incenter density or the Jacobian and checks the empirical distribution against the exact CDF with a fixed seed. It additionally tests the conditional third Fourier coefficient. The successful diagnostics were `JACOBIAN_FINITE_DIFFERENCES_OK`, `NORMALIZATION_MOMENT_HYPERBOLIC_TAIL_OK`, `CARTESIAN_MOBIUS_INVERSION_AND_POISSON_PHASE_OK`, and `IDEAL_HYPERBOLIC_INCENTER_CHECKS_OK`.

## Relationship to prior work

Curien and Werner (2011 preprint; 2013 publication) identify ideal hyperbolic triangles with the disk Möbius group and derive its infinite, invariant Haar measure using hyperbolic center and orientation. Their model is an invariant random *triangulation*, rather than a single triangle with three independent Euclidean-angle-uniform boundary vertices. The invariant measure and group coordinates are antecedents, not new claims here. The result above explicitly pushes a finite, non-invariant independent-boundary sampling law through the center map and evaluates its resulting density and full radial distribution.

Horváth (2014) studies hyperbolic triangle centers and incircles, but does not state the distribution of a center of an ideal triangle under iid boundary sampling. Hertrich-Jeromin, King and O'Hara (2013) study Möbius geometry of Euclidean triangle centers and ideal tetrahedra in three-dimensional hyperbolic space, a different configuration. No previously inspected full text asserts the displayed law for this random ideal-triangle model. Historical priority outside these sources is not fully resolved.

## Limitations

The uniform measure on boundary angles is tied to the selected disk center and is not invariant under the full hyperbolic isometry group. The result is specific to three ideal vertices and does not describe a finite-radius hyperbolic-vertex sampling law, random hyperbolic tessellations, or centers of more general ideal polygons. The stated exponential tail concerns distance of the triangle incenter from the chosen origin; the **incircle's own hyperbolic radius** is a deterministic constant for every ideal triangle and is not the random variable here. No claim of independent mathematical certification or exhaustive historical priority is made.

## References

1. N. Curien and W. Werner, *The Markovian hyperbolic triangulation*, arXiv:1105.5089 (first submitted 2011-05-25); J. Eur. Math. Soc. 15 (2013), 1309–1341. https://arxiv.org/abs/1105.5089 ; https://doi.org/10.4171/JEMS/393 . Relevant material: §2.1, marked ideal triangles, group coordinates and Haar measure.
2. Á. G. Horváth, *On the hyperbolic triangle centers*, arXiv:1410.6735 (first submitted 2014-10-24). https://arxiv.org/abs/1410.6735 . Relevant material: §1.3.4 on incircles and triangle centers.
3. U. Hertrich-Jeromin, A. King and J. O'Hara, *On the Möbius geometry of Euclidean triangles*, Elemente der Mathematik 68 (2013), 96–114. https://doi.org/10.4171/EM/228 . Relevant material: introduction and Möbius center constructions.
