# A sharp area-density cusp for isotropic affine sections of prolate spheroids

## Finding

For the solid prolate spheroid
\[
E_{b,r}=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2/r^2\le b^2\},\qquad b>0,\quad r>1,
\]
choose an unoriented affine plane from the Euclidean-motion-invariant measure on planes conditioned on intersecting the spheroid. Write \(A\) for its section area and \(X=A/(\pi b^2)\). Let
\[
k=\sqrt{r^2-1},\qquad h(s)=\sqrt{1+k^2s^2},\qquad H=\int_0^1h(s)\,ds
=\frac12\left(r+\frac{\operatorname{arsinh}k}{k}\right).
\]
The complete distribution has support \([0,r]\) and survival law
\[
\Pr(X>x)=\frac1H\int_0^1h(s)\sqrt{\left(1-\frac{x h(s)}r\right)_+}\,ds,\quad 0<x<r.
\]
Here \(y_+=\max\{y,0\}\). Its density is continuous in the interior, real analytic on each of \((0,1)\) and \((1,r)\), but has a **unique interior square-root cusp** at \(x=1\):
\[
f_r(1-\varepsilon)=f_r(1)-\frac{r^3}{H(r^2-1)}\sqrt\varepsilon+O_r(\varepsilon),\quad
f_r(1+\varepsilon)=f_r(1)+O_r(\varepsilon).
\]
Thus \(f_r\) is not \(C^1\) at \(x=1\), and its derivative diverges from the left. In unnormalized area units, this cusp is exactly at \(A=\pi b^2\); the upper endpoint is \(\pi b^2r\). Therefore the area distribution of unlabelled cuts determines both \(b=\sqrt{A_{\mathrm{cusp}}/\pi}\) and \(r=A_{\mathrm{max}}/A_{\mathrm{cusp}}\).

An additional exact identity is \(\mathbb E[X]=2r/(3H)\). The ratio \(\mathbb E[A]/A_{\mathrm{max}}=2/(3H)\) is strictly decreasing with \(r\), providing a second, cusp-free theoretical determination of aspect ratio from area alone when its upper support endpoint is known.

## Assumptions and scope

An unoriented plane is identified by its unit normal \(u\in S^2/\{\pm1\}\) and signed offset \(t\), with invariant measure proportional to \(d\sigma(u)\,dt\). Conditioning requires the plane to intersect the *solid* spheroid. The major symmetry axis is along \(z\); rotating and translating the body do not change the law. The aspect ratio satisfies \(r>1\), strictly excluding the ball, whose density has different regularity. All distributional statements are exact population-level statements; no assertions about mixtures of sizes/shapes or finite observations are made. Intersections tangent to the boundary have measure zero.

## Proof

**1. Plane sampling and slice geometry.** The half-width in normal direction \(u\) is \(b h(s)\), where \(s=|u_z|\). Before conditioning, \(s\) is uniform on \([0,1]\). A plane with this normal intersects the body iff \(|t|\le b h(s)\). Consequently, after conditioning, \(s\) has density \(h(s)/H\); given \(s\), \(v=t/(b h(s))\) is uniform on \([-1,1]\) and independent of \(s\). This width bias is essential to the Crofton rather than central-plane law.

The affine map \((\xi,\eta,\zeta)\mapsto (b\xi,b\eta,br\zeta)\) sends the unit ball to the spheroid. Restricting the quadratic form to the plane, or using the determinant-of-restriction identity, gives its ellipse area as
\[
A=\pi b^2\frac{r}{h(s)}(1-v^2),\qquad X=\frac{r}{h(s)}(1-v^2).
\]
Since \(v\) is uniform on \([-1,1]\), \(\Pr(1-v^2>z)=\sqrt{1-z}\) for \(0\le z\le1\). Integrating the condition \(X>x\) against the width-biased normal density proves the survival formula. It also yields \(\mathbb E[X]=(r/H)\int_0^1h(s)(2/3)/h(s)\,ds=2r/(3H)\).

**2. Density.** Differentiate the survival formula under the integral sign, justified by its integrable inverse-square-root endpoint. For \(0<x<r\), define
\[
s_*(x)=\begin{cases}1,&0<x\le1,\\
\sqrt{\dfrac{r^2/x^2-1}{r^2-1}},&1<x<r.
\end{cases}
\]
Then
\[
f_r(x)=\frac1{2rH}\int_0^{s_*(x)}\frac{h(s)^2}{\sqrt{1-xh(s)/r}}\,ds.
\]
Substitute \(h=\sqrt{1+k^2s^2}\) to obtain
\[
f_r(x)=\frac1{2rH k}\int_1^{\min(r,r/x)}\frac{h^3\,dh}{\sqrt{h^2-1}\sqrt{1-xh/r}}.
\tag{1}
\]
The integral is finite at \(x=1\): the lower endpoint behaves as \((h-1)^{-1/2}\), and the upper as \((r-h)^{-1/2}\). Dominated convergence after a square-root endpoint reparametrization proves continuity. Away from \(x=1\), the same reparametrizations give an analytic integrand on a fixed compact interval: for \(x>1\) use \(h=1+(r/x-1)\sin^2\theta\); for \(x<1\) the upper limit stays fixed and the radicand remains positive at \(h=r\). Hence there are no other interior singularities.

**3. Sharp cusp.** In (1), the weight \(h^3/[2rHk\sqrt{h^2-1}]\) is smooth and positive near \(h=r\), where it equals
\[
W(r)=\frac{r^2}{2H(r^2-1)}.
\]
Put \(h=r-y\) and \(x=1-\varepsilon\). Since \(1-(1-\varepsilon)(r-y)/r=\varepsilon+y/r+O(\varepsilon y)\), replacing the smooth weight by \(W(r)\) over a small fixed endpoint interval introduces at most an \(O_r(\varepsilon)\) difference. The singular endpoint integral satisfies
\[
\int_0^\delta\!\left(\frac1{\sqrt{\varepsilon+y/r}}-\frac1{\sqrt{y/r}}\right)dy
=-2r\sqrt\varepsilon+O_r(\varepsilon).
\]
The remaining part of (1) is analytic in \(\varepsilon\). Therefore
\[
f_r(1-\varepsilon)-f_r(1)
=-2rW(r)\sqrt\varepsilon+O_r(\varepsilon)
=-\frac{r^3}{H(r^2-1)}\sqrt\varepsilon+O_r(\varepsilon).
\]
For \(x=1+\varepsilon\), the moving upper limit \(r/x\) is handled by \(h=1+(r/x-1)\sin^2\theta\), leaving an analytic integral in \(x\) near 1 from the right. Thus \(f_r(1+\varepsilon)=f_r(1)+O_r(\varepsilon)\). The positive coefficient of \(\sqrt\varepsilon\) means the left derivative diverges, while the right derivative is finite.

**4. Inverse identification.** At fixed \(s\), \(0\le X\le r/h(s)\le r\); the upper support endpoint \(r\) is approached for \(s\to0,v\to0\). The only interior loss of differentiability is the cusp \(X=1\). Undoing \(X=A/(\pi b^2)\) gives the two recoverable geometric invariants stated above. Finally, \(H'(r)>0\) because \(h(s)\) increases strictly for all \(s>0\), so \(2/(3H)\) is strictly decreasing in \(r\).

## Verification

Execute `python check_spheroid_cusp.py` with NumPy and SciPy. The standalone checker (i) generates independent invariant hitting planes by orientation rejection and uniform conditional offsets, (ii) recomputes the ellipse section area directly from the quadratic form restricted to an orthonormal plane basis, (iii) compares empirical survival and mean with the exact integral at three aspect ratios, (iv) independently compares analytic density with numerical differences of the survival law, and (v) numerically verifies convergence to the sharp one-sided cusp coefficient. These calculations corroborate, but do not replace, the proof.

## Relationship to prior work

Cruz-Orive's classical stereological treatment of spheroid sections (1976) and DeHoff's earlier random-section study (1962) address the general size/shape information available from elliptical cuts. Their relevance is substantial: a complete joint law of section-ellipse semiaxes can in principle be marginalized to an area distribution. The specific sharply quantified nonanalyticity and its location as an **area-only** shape marker, rather than general joint-shape inversion, are the targeted contribution here. Cruz-Orive's full 1976 article could not be inspected, so its precise implication for this cusp remains a historical-priority risk.

Makarenko, Fletcher and Shukurov (2014) analyze the *filamentarity* (an area-perimeter shape functional) of isotropic ellipsoid sections and report a cusp for that distinct statistic. Their full article does not state the present area-density singularity and coefficient. Baaske, Ballani and Illgen (2016) develop inference from spheroid elliptical profiles under a fixed vertical-section sampling design; their preprint does not give this invariant-affine-plane area-only cusp theorem. Haar-distributed *central* section statistics and planar *projections* have different sampling laws.

## Limitations

The claim is for a fixed, non-spherical prolate spheroid, exactly Crofton-sampled cutting planes, and an ideal population distribution. It is not an inference algorithm with statistical sample-complexity guarantees. General pre-existing stereological joint-distribution identities might provide an alternative derivation or subsume the marginal distribution; independent historical-priority confirmation remains outstanding. Numerical verification is finite and not a proof of analyticity or asymptotic orders.

## References

1. L.-M. Cruz-Orive, *Particle size-shape distributions: The general spheroid problem. I. Mathematical model*, Journal of Microscopy 107 (1976), 235–253. DOI: 10.1111/j.1365-2818.1976.tb02446.x (full text unavailable at review).
2. R. T. DeHoff, *The determination of the size distribution of ellipsoidal particles from measurements made on random plane sections*, Transactions of the Metallurgical Society of AIME 224 (1962), 474–477 (bibliographic record only).
3. I. Makarenko, A. Fletcher and A. Shukurov, *3D morphology of a random field from its 2D cross-section*, Monthly Notices of the Royal Astronomical Society: Letters 447 (2015), L55–L59; online December 11, 2014. DOI: 10.1093/mnrasl/slu169.
4. M. Baaske, F. Ballani and A. Illgen, *On the estimation of parameters of a spheroid distribution from planar sections*, arXiv:1609.06697 (2016).
