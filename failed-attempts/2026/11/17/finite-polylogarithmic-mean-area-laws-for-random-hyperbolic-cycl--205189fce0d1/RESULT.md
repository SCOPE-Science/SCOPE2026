# Finite polylogarithmic mean-area laws for random hyperbolic cyclic polygons

## Finding

Fix an integer \(n\ge3\). Choose \(n\) independent points uniformly by hyperbolic arclength on a geodesic circle of radius \(R>0\) in the curvature-\(-1\) hyperbolic plane. Let \(A_{n,R}\) be the hyperbolic area of their geodesic convex hull; all sampled points are hull vertices almost surely. Put \(z=\tanh^2(R/2)\). For \(0<z<1\), write \(\operatorname{Li}_s(z)=\sum_{m=1}^{\infty}z^m/m^s\). Then

\[
\boxed{\mathbb E A_{n,R}=2n(n-1)\sum_{j=0}^{\lfloor(n-3)/2\rfloor}\frac{(-1)^j(n-2)!}{(n-2-2j)!(2\pi)^{2j+1}}\operatorname{Li}_{2j+2}(z).}
\]

In particular, \(\mathbb E A_{3,R}=6\operatorname{Li}_2(z)/\pi\) and \(\mathbb E A_{4,R}=12\operatorname{Li}_2(z)/\pi\). For every fixed \(n\), this expectation is strictly increasing from \(0\) to \((n-2)\pi\) as \(R\) increases from \(0\) to infinity. It therefore determines the radius uniquely, given \(n\). As \(R\to\infty\),

\[
\boxed{(n-2)\pi-\mathbb E A_{n,R}=\frac{4n(n-1)}{\pi}R e^{-R}+O_n(e^{-R}).}
\]

For triangles, the sharper form is

\[
\pi-\mathbb E A_{3,R}=\frac{24}{\pi}e^{-R}(R+1-\log 4)+O(Re^{-2R}).
\]

## Assumptions and scope

The metric has constant Gaussian curvature \(-1\). The circle is centered at a fixed point, and its probability measure is normalized intrinsic arclength, so polar angles are iid uniform on \([0,2\pi)\). The hull is the geodesically convex polygon with these boundary vertices; its area is not the Euclidean disk-model area. The sample is almost surely nondegenerate. The symbol \(n\) is fixed in the stated large-radius expansion, which is not uniform for growing \(n\). The polylogarithm is defined by its absolutely convergent positive-real series for \(0<z<1\).

## Proof

Work in the Poincaré disk. The geodesic circle of hyperbolic radius \(R\) is the Euclidean circle of radius \(r=\tanh(R/2)\), and set \(z=r^2\). In circular order, let the successive positive polar gaps be \(g_1,\ldots,g_n\), with \(\sum_jg_j=2\pi\). Their normalized vector is \(\operatorname{Dirichlet}(1,\ldots,1)\), and one normalized gap has density \((n-1)(1-x)^{n-2}\) for \(0<x<1\).

Define, for \(0<g<2\pi\),

\[
f_z(g)=\arctan\!\left(\frac{1-z}{1+z}\cot\frac g2\right)\in(-\pi/2,\pi/2).
\]

To obtain the interior angle at a vertex, conjugate by an isometry so that the vertex is \(r>0\) on the real axis. The disk automorphism \(\varphi_r(w)=(w-r)/(1-rw)\) maps that vertex to zero and preserves angles. For the next vertex \(re^{ig}\), the tangent direction is \(\arg\varphi_r(re^{ig})=\pi-f_z(g)\) as a continuously lifted angle. For the preceding vertex at polar gap \(h\) in the reverse direction, the tangent is \(\pi+f_z(h)\). Hence the interior angle is \(f_z(g)+f_z(h)\); this lies in \((0,\pi)\) because adjacent gaps are positive with sum strictly below \(2\pi\). Thus hyperbolic Gauss–Bonnet gives the exact geometric identity

\[
A_{n,R}=(n-2)\pi-2\sum_{i=1}^n f_z(g_i).
\]

Since \(0<z<1\), the principal argument expansion for \(\log(1-ze^{ig})\) gives the absolutely convergent Fourier identity

\[
f_z(g)=\frac{\pi-g}{2}-\sum_{m\ge1}\frac{z^m\sin(mg)}m.
\]

For a single gap \(G=2\pi X\), where \(X\sim\operatorname{Beta}(1,n-1)\), the expectation of the linear term is \(\pi/2-\pi/n\). Consequently the linear parts cancel the Gauss–Bonnet constant exactly, leaving

\[
\mathbb E A_{n,R}=2n(n-1)\sum_{m\ge1}\frac{z^m}{m}\int_0^1(1-x)^{n-2}\sin(2\pi mx)\,dx.
\]

For integer \(p\ge1\) and \(a=2\pi m\), write \(I_p(a)=\int_0^1(1-x)^p\sin(ax)\,dx\). Two integrations by parts, using \(\sin a=0\) and \(\cos a=1\), yield \(I_p(a)=a^{-1}-p(p-1)a^{-2}I_{p-2}(a)\), where \(I_0(a)=0\) and \(I_1(a)=a^{-1}\). Iteration gives

\[
I_p(2\pi m)=\sum_{j=0}^{\lfloor(p-1)/2\rfloor}\frac{(-1)^jp!}{(p-2j)!(2\pi m)^{2j+1}}.
\]

Substituting \(p=n-2\) and summing \(\sum_{m\ge1}z^m/m^{2j+2}=\operatorname{Li}_{2j+2}(z)\) proves the stated finite formula.

For strict monotonicity, use the Klein disk, where these geodesic polygons are Euclidean convex hulls. For fixed sample directions, the Klein radii of their vertices are \(s=\tanh R\), so the polygon is \(sQ\) for the fixed nondegenerate Euclidean polygon \(Q\) inscribed in the unit circle. Hyperbolic area in Klein coordinates is \(\int_{sQ}(1-|x|^2)^{-3/2}\,dx=s^2\int_Q(1-s^2|y|^2)^{-3/2}\,dy\). This is strictly increasing in \(s\in(0,1)\). It vanishes as \(s\downarrow0\). As \(s\uparrow1\), all vertices become ideal and the angle formula gives area \((n-2)\pi\) for each nondegenerate sample. Bounded convergence yields the asserted limiting mean.

Finally set \(\delta=1-z=\operatorname{sech}^2(R/2)=4e^{-R}+O(e^{-2R})\). The standard expansion from differentiating the defining series is \(\operatorname{Li}_2(1)-\operatorname{Li}_2(1-\delta)=\delta(1-\log\delta)+O(\delta^2|\log\delta|)\). For every integer \(s\ge4\), the same difference is \(O(\delta)\) because \(\operatorname{Li}'_s(1)=\zeta(s-1)<\infty\). Thus the sole logarithmic contribution comes from the \(j=0\) term, with coefficient \(n(n-1)/\pi\). Inserting \(\delta=4e^{-R}+O(e^{-2R})\) gives the fixed-\(n\) leading law. For \(n=3\), there are no higher polylogarithms, yielding the stated second constant and error.

## Verification

The included standalone `check_area.py` evaluates the finite polylogarithm formula using a convergent series with a certified elementary remainder bound, verifies its independent Fourier-gap integral representation numerically, and checks the triangular area formula against the hyperbolic law of cosines. Monte Carlo simulations are corroborative only, not a proof. The proof above is analytic and does not rely on finite enumeration or numerical fitting.

## Relationship to prior work

Bao and Chen (2014) provide deterministic hyperbolic triangle-area formulas in disk/half-plane coordinates, with applications to Lambert and Saccheri quadrilaterals. Horváth (2014, original arXiv release) treats hyperbolic triangle centers and records Gauss–Bonnet/hyperbolic trigonometry. Those sources furnish geometric background but do not establish finite-sample random cyclic polygon mean areas or the polylogarithmic formula. Related investigations into random hyperbolic circle triangles address acuteness or inradius, rather than these area expectations. A separate spherical fixed-latitude random-triangle mean is expressed through a negative-argument dilogarithm; it is not a theorem about the hyperbolic all-\(n\) model. The possibility of an older unstated equivalent integral or curvature-continuation identity remains a priority risk.

## Limitations

This theorem is about fixed-\(n\) means under independent angular-uniform sampling, not the full area distribution, higher moments, arbitrary radii, nonuniform angular laws, or joint large-\(n\), large-\(R\) asymptotics. The comparisons made cannot establish definitive historical novelty, and there has been no independent audit.

## References

1. H. Bao and X. Chen, *A New Hyperbolic Area Formula of a Hyperbolic Triangle and Its Applications*, Journal of Mathematics (2014), article 838497, first published August 13, 2014, https://doi.org/10.1155/2014/838497.
2. Á. G. Horváth, *On the hyperbolic triangle centers*, arXiv:1410.6735v1, first publicly submitted October 24, 2014, https://arxiv.org/abs/1410.6735.
3. Classical hyperbolic Gauss–Bonnet area formula and Poincaré/Klein disk transformations; also summarized in the two primary sources above.
