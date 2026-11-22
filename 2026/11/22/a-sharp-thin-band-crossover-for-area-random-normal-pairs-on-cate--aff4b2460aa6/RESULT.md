# A sharp thin-band crossover for area-random normal pairs on catenoids

## Finding
Let \(a>0\) and \(b>0\). On the symmetric truncated catenoid
\[
\Sigma_{a,b}=\{(a\cosh v\cos u,a\cosh v\sin u,av):0\le u<2\pi,\ -b\le v\le b\},
\]
choose two points independently with probability proportional to the induced surface-area measure. Write \(N_1,N_2\) for their consistently oriented unit normals and \(T_b=N_1\cdot N_2\). The complete law is independent of \(a\), is even in \(T_b\), and has the uniformly convergent Legendre density
\[
q_b(t)=\frac12\sum_{\ell=0}^{\infty}(2\ell+1)\,\alpha_\ell(b)^2P_\ell(t),\qquad -1\le t\le1,
\]
where \(P_\ell\) is the degree-\(\ell\) Legendre polynomial and
\[
\alpha_\ell(b)=\frac1{H(b)}\int_{-\tanh b}^{\tanh b}\frac{P_\ell(z)}{(1-z^2)^2}\,dz,
\quad H(b)=b+\tfrac12\sinh(2b).
\]
All odd coefficients vanish. In particular, for every *fixed* \(b>0\) the two endpoint probabilities are linear:
\[
\Pr(T_b>1-\varepsilon)\sim \Pr(T_b<-1+\varepsilon)\sim c(b)\varepsilon,
\qquad c(b)=\frac{20b+15\sinh(2b)+3\sinh(4b)+\tfrac13\sinh(6b)}{32H(b)^2}.
\]
In contrast, as the symmetric band becomes thin, its parallel-normal tail admits a **sharp critical window**: for every fixed \(s>0\),
\[
\boxed{\lim_{b\downarrow0}\frac{\Pr(T_b>1-b^2s)}{b}=F(s)}
\]
with the nontrivial, positive crossover profile
\[
F(s)=\frac1{4\pi}\int_{-2}^{2}(2-|w|)\sqrt{(2s-w^2)_+}\,dw,
\]
where \((x)_+=\max\{x,0\}\). Put \(r=\sqrt{2s}\). Then
\[
F(s)=\begin{cases}
\displaystyle \frac{s}{2}-\frac{(2s)^{3/2}}{6\pi},&0<s\le2,\\[6pt]
\displaystyle \frac{4\sqrt{r^2-4}+2r^2\arcsin(2/r)-\frac23\bigl(r^3-(r^2-4)^{3/2}\bigr)}{4\pi},&s\ge2.
\end{cases}
\]
It interpolates rigorously between \(F(s)\sim s/2\) as \(s\downarrow0\) and \(F(s)\sim\sqrt{2s}/\pi\) as \(s\to\infty\). The transition at \(s=2\) records the maximal scaled vertical normal separation across the band. The same limit holds for the antiparallel tail by exact symmetry.

There is also a unique **second-moment isotropy height** \(b_*=1.08865949248265\ldots\), specified by \(\sinh(2b_*)=4b_*\), at which
\[
\mathbb E[T_b^2]=\frac13.
\]
This is the strict global minimum over \(b>0\). The value \(1/3\) is the spherical-uniform second moment even though the catenoid normal measure omits both polar caps. Moreover, every value strictly between \(1/3\) and \(1/2\) is attained at exactly two different positive half-heights. These are complementary consequences of the same explicit normal-pair law.

## Assumptions and scope
The truncation is symmetric about the neck plane. The surfaces include their boundary circles, which have zero surface area. Sampling means **area-uniform independent surface points**, not uniform parameter samples or curvature-weighted Gauss-map samples. The unit normals use \(N(u,v)=(\operatorname{sech}v\cos u,\operatorname{sech}v\sin u,-\tanh v)\); simultaneous reversal changes no dot products. Throughout, \(a>0\), \(b>0\), and \(-1\le T_b\le1\). Constants in the fixed-band tail may depend on \(b\). The critical-window limit holds for each fixed \(s>0\), without claiming a uniform error bound over all \(s\) or a uniform joint limit as \(b\to\infty\).

## Proof
**1. Exact Gauss-map pushforward.** Differentiating the parametrization yields \(\lvert X_u\times X_v\rvert=a^2\cosh^2v\). Consequently, \(u\) is uniform on \([0,2\pi)\), independent of \(v\), and the latter has density \(\cosh^2v/H(b)\) on \([-b,b]\). Under \(z=-\tanh v\), \(dz=-\operatorname{sech}^2v\,dv\); the latitude variable is supported in \([-\tanh b,\tanh b]\) with density
\[
w_b(z)=\frac{\mathbf1_{\{|z|\le\tanh b\}}}{H(b)(1-z^2)^2}.
\]
This is a probability density because its integral is exactly \(H(b)/H(b)=1\). Conditionally on \(z\), the azimuth is uniform. The normal distribution is antipodally symmetric.

**2. Distribution and endpoints.** The standard spherical-harmonic addition theorem, applied to two independent axisymmetric spherical measures, gives
\(\mathbb E[P_\ell(T_b)]=\alpha_\ell(b)^2\).
The density reconstruction follows from Legendre completeness. For each fixed \(b>0\), the support interval for \(z\) is strictly inside \((-1,1)\); integration by parts using
\((2\ell+1)P_\ell=P'_{\ell+1}-P'_{\ell-1}\)
and the classical interior \(P_\ell=O_b(\ell^{-1/2})\) estimate gives \(\alpha_\ell=O_b(\ell^{-3/2})\). Thus the displayed density series converges absolutely and uniformly. Parseval at \(t=1\) yields
\[
q_b(1)=\sum_{\ell\ge0}\frac{2\ell+1}{2}\alpha_\ell^2=\int_{-1}^1w_b(z)^2\,dz=\frac{1}{H(b)^2}\int_{-b}^{b}\cosh^6v\,dv.
\]
Expanding \(\cosh^6v\) gives the stated expression \(c(b)\). Uniform continuity then implies \(\Pr(T_b>1-\varepsilon)=c(b)\varepsilon+o_b(\varepsilon)\). Antipodal symmetry handles \(t=-1\).

**3. Thin-band crossover.** Set \(x_i=z_i/b\). As \(b\downarrow0\), these variables converge in density to independent uniform variables on \([-1,1]\), and their densities are uniformly bounded on a fixed interval. Let \(\delta\in[-\pi,\pi]\) be the difference of the two independent azimuths. For fixed \(s>0\), the event \(T_b>1-b^2s\) forces \(\delta=O_s(b)\). Put \(y=\delta/b\). Uniformly on compact \(x_1,x_2,y\)-sets,
\[
\frac{1-T_b}{b^2}=\frac{(x_1-x_2)^2+y^2}{2}+o(1).
\]
The joint density of \(x_1,x_2\) tends to \(1/4\) on the square and the azimuth measure becomes \(b\,dy/(2\pi)\). The scaled event converges, except on its measure-zero quadratic boundary, to
\(\{(x_1,x_2,y)\in[-1,1]^2\times\mathbb R:(x_1-x_2)^2+y^2<2s\}\).
Since the condition bounds \(y\), dominated convergence applies. Integrating \(y\) first gives
\[
\lim b^{-1}\Pr(T_b>1-b^2s)=\frac1{4\pi}\int_{[-1,1]^2}\sqrt{(2s-(x_1-x_2)^2)_+}\,dx_1dx_2.
\]
The difference \(w=x_1-x_2\) has unnormalized fiber length \(2-|w|\), giving exactly \(F(s)\). Elementary antiderivatives of \((2-w)\sqrt{2s-w^2}\) yield the displayed two branches. Their small- and large-\(s\) asymptotics follow directly; in particular, \(F(s)\sim\sqrt{2s}/\pi\) is the arcsine tail of the limiting equatorial normal circle.

**4. Isotropic second-moment height.** Write \(S(b)=\frac12\sinh(2b)\) and \(m(b)=\mathbb E[z^2]\). The exact area integrals give
\[
m(b)=\frac{S(b)-b}{S(b)+b},\qquad
\mathbb E[T_b^2]=m(b)^2+\frac{(1-m(b))^2}{2}.
\]
Since \(\frac{d}{db}(S(b)/b)>0\) for \(b>0\), \(m(b)\) grows strictly from \(0\) to \(1\). The strictly convex quadratic in \(m\) has its unique minimum \(1/3\) at \(m=1/3\), equivalent to \(S(b)=2b\) or \(\sinh(2b)=4b\). Strict monotonicity on each side of the minimum, together with endpoint values \(1/2\) and \(1\), proves the two-to-one assertion.

## Verification
The accompanying `checker.py` independently integrates the Gauss-map latitude density, checks the second Legendre moment, compares the endpoint coefficient with numerical quadrature, checks the crossover integral against both explicit branches, and compares the small-band finite-parameter probability with \(bF(s)\). It reports 33 successful numerical comparisons. These checks test the algebra and asymptotic normalization but do not replace the analytical proof. Running the script requires Python 3, NumPy and SciPy.

## Relationship to prior work
The classical catenoid, its Gauss map and its variational geometric characterizations are well established. Bernstein and Mettler (2013, Sections 1, 3–5) study minimal-surface entropy differentials and the catenoid's geometric characterization, not two independently area-sampled normals or thin-band parallel-normal probabilities. Apostol and Mnatsakanian (2015) study volume/surface-area relations for catenoids and related surfaces; their accessible abstract does not report a two-normal distribution, but its full text was not available for direct exclusion. Existing normal-pair calculations for embedded circular ring tori concern a different Gauss-map pushforward and do not imply this nonuniform catenoid-belt law or its small-band crossover. The normal-coordinate formula itself is standard; the assessment here concerns the paired-law reconstruction, sharp crossover and unique second-moment isotropy height, not a new catenoid parametrization.

## Limitations
This result gives no new rigidity theorem for arbitrary minimal surfaces, no area-sampling claim for full noncompact catenoids (whose total area is infinite), and no independent certification of historical priority. The finite-band density has a convenient convergent spectral expression rather than a claimed elementary closed form. The width \(b\) is dimensionless vertical half-height measured in neck radii; uniform sampling in the parameter \(v\) would produce a different law. The finite numerical checks are not substitutes for the proof.

## References
1. J. Bernstein and T. Mettler, *Characterizing classical minimal surfaces via the entropy differential*, arXiv:1301.1663, first publicly posted 2013-01-08. https://arxiv.org/abs/1301.1663 . Sections 1, 3, 4 and 5 were inspected in full-text HTML.
2. T. M. Apostol and M. A. Mnatsakanian, *Volume/Surface Area Relations for n-Dimensional Spheres, Pseudospheres, and Catenoids*, American Mathematical Monthly 122 (2015), 745–756, doi:10.4169/amer.math.monthly.122.8.745 . Bibliographic and abstract information: https://authors.library.caltech.edu/records/sr05v-hf474 .
3. M. do Carmo, *Differential Geometry of Curves and Surfaces*, 1976, catenoid example and first fundamental form (classical reference). See https://docenti.ing.unipi.it/griff/files/dC.pdf .
4. Spherical harmonic addition theorem and Legendre orthogonality (classical); the identities needed are given explicitly in the proof above.
