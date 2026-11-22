# A sixty-degree diameter transition and a cubic-to-quartic law for random points in circular sectors

## Finding

For \(0<\theta<\pi\), let \(S_\theta\subset\mathbb R^2\) be the radius-one closed circular sector of aperture \(\theta\). Let \(X,Y\) be two independent points uniformly distributed with respect to Euclidean area on \(S_\theta\), and let \(D=\lVert X-Y\rVert_2\). The geometric diameter is
\[
M_\theta=\max\{1,2\sin(\theta/2)\}.
\]
For every **fixed** \(0<\theta<\pi\), the exact sharp leading near-diameter probability is
\[
\Pr(D>M_\theta-\varepsilon)\sim
\begin{cases}
\displaystyle -\frac{8\log(\cos\theta)}{3\theta^2}\,\varepsilon^3,&0<\theta\le\pi/3,\\[5pt]
\displaystyle \frac{4}{3\theta^2\sin^2\theta}\,\varepsilon^4,&\pi/3<\theta<\pi.
\end{cases}
\]
The transition at \(\pi/3\) is singular: the exponent changes from three to four immediately above the threshold, while at equality the tip-to-arc maximizing configurations retain the cubic contribution. For every fixed real \(\lambda\) in the critical aperture window \(\theta_\varepsilon=\pi/3+\lambda\varepsilon\),
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-3}
\Pr_{\theta_\varepsilon}(D>M_{\theta_\varepsilon}-\varepsilon)
=\frac{24\log2}{\pi^2}\left(1-\frac{\sqrt3}{2}\max\{\lambda,0\}\right)_+^3,
\]
where \(z_+=\max\{z,0\}\). At and beyond \(\lambda=2/\sqrt3\), this scale-three limit vanishes; a separate rim contribution of order \(\varepsilon^4\) remains.

The narrow-sector cubic coefficient increases strictly with \(\theta\). The wide-sector quartic coefficient has a unique global minimum on \((\pi/3,\pi)\), attained at the unique \(\theta_*\in(\pi/2,\pi)\) satisfying \(\tan\theta_*=-\theta_*\), numerically \(\theta_*=2.028757838110434\ldots\). Hence the quartic coefficient does not uniquely determine a wide-sector opening; distinct wide apertures share it above the minimum (subject to the coefficient's range).

The rare-event configurations also have explicit limiting shapes. In the wide sector let \(u=1-R_X\), \(v=1-R_Y\), \(t=\theta-|\Phi_X-\Phi_Y|\), and \(s=\sin(\theta/2)\), \(c=\cos(\theta/2)\). Conditioned on \(D>M_\theta-\varepsilon\),
\[
\left(\frac{su}{\varepsilon},\frac{sv}{\varepsilon},\frac{ct}{\varepsilon},1-\frac{s(u+v)+ct}{\varepsilon}\right)
\Longrightarrow\operatorname{Dirichlet}(1,1,2,1).
\]
The two ordered endpoint configurations have asymptotic probability \(1/2\) each. In the narrow sector, after choosing which point is near the tip, the normalized tip deficit, rim deficit and remaining slack converge conditionally (given the endpoint-angle difference) to \(\operatorname{Dirichlet}(2,1,1)\), and the angular-difference mark has density proportional to \((\theta-\delta)\sec^2\delta\), for \(0<\delta<\theta\).

## Assumptions and scope

The domain is a **planar, unglued Euclidean sector**, not a circular cone with its radial boundaries identified. The sampling is independent, exactly uniform in planar area; there is no atom on the radial sides, arc, or tip. The radius is normalized to one; for a physical radius \(R>0\), replace \(\varepsilon\) with \(\varepsilon/R\). The aperture is restricted to \((0,\pi)\), so the sector is convex. All fixed-angle asymptotics are pointwise in \(\theta\). The displayed critical window holds for each fixed finite \(\lambda\), not uniformly over unbounded \(\lambda\).

Polar coordinates have \(R_X,R_Y\) independent with density \(2r\) on \((0,1)\), and \(\Phi_X,\Phi_Y\) independent uniform on \((0,\theta)\). Thus \(\Delta=|\Phi_X-\Phi_Y|\) is independent of the radii and has the **triangular** density
\[
 f_\Delta(\delta)=\frac{2(\theta-\delta)}{\theta^2},\qquad0<\delta<\theta.
\]
The cosine rule gives \(D^2=R_X^2+R_Y^2-2R_XR_Y\cos\Delta\).

## Proof

**Diameter and localization.** At fixed \(\delta\), the squared distance is separately convex in both radii, so its maximum over the radial unit square occurs at one of its four corners. Increasing \(\delta\) cannot decrease distance. The corner values are the tip-to-rim distance \(1\) and the two outer-arc endpoint distance \(2\sin(\theta/2)\), hence the diameter formula. The complete maximizing sets consist of all tip-to-outer-arc pairs if \(\theta<\pi/3\), the two ordered arc-endpoint pairs if \(\theta>\pi/3\), and both sets at equality. Compactness localizes any near-diameter event to these sets. The two distinct maximizing types have disjoint neighborhoods at the critical angle.

**Tip-to-rim law.** Fix \(0<\theta\le\pi/3\). In either ordered tip/rim neighborhood put \(R_X=\varepsilon U\), \(R_Y=1-\varepsilon V\). Uniformly in both angles,
\[
 D=1-\varepsilon\left(V+U\cos(\Phi_X-\Phi_Y)\right)+O(\varepsilon^2(U+V)^2).
\]
Since \(\cos(\Phi_X-\Phi_Y)\ge\cos\theta\ge1/2\), the event confines the rescaled radial coordinates to a common bounded set. The two ordered cases together have limiting measure \(8\varepsilon^3 U\,dU\,dV\,d\phi\,d\psi/\theta^2\). After dominated convergence, the integrated radial simplex gives \(1/[6\cos^2(\phi-\psi)]\). Consequently
\[
 \lim_{\varepsilon\downarrow0}\frac{\Pr(\text{tip-to-rim near-maximal})}{\varepsilon^3}
 =\frac{4}{3\theta^2}\int_0^\theta\!\int_0^\theta\sec^2(\phi-\psi)\,d\phi\,d\psi
 =-\frac{8\log\cos\theta}{3\theta^2},
\]
using \(\int_0^\theta\!\int_0^\theta\sec^2(\phi-\psi)\,d\phi\,d\psi=-2\log\cos\theta\). The angle-mark density is the normalized double-integral integrand \((\theta-\delta)\sec^2\delta\), and the conditional radial Dirichlet limit follows by replacing \(U\cos\delta\) and \(V\) with simplex coordinates (whose density is proportional to the first coordinate).

**Two rim endpoints.** Fix \(\pi/3\le\theta<\pi\) and define \(s=\sin(\theta/2)>0\), \(c=\cos(\theta/2)>0\). Near the ordered rim endpoints put \(R_X=1-\varepsilon U\), \(R_Y=1-\varepsilon V\), \(\Delta=\theta-\varepsilon T\). Taylor expansion gives
\[
 D=2s-\varepsilon(sU+sV+cT)+O(\varepsilon^2(U+V+T)^2).
\]
All three linear coefficients are positive; hence the relevant rescaled coordinates remain uniformly bounded. The two radial densities contribute \(4\varepsilon^2\), while the triangular angular density contributes \(2\varepsilon^2T/\theta^2\). Therefore
\[
 \lim_{\varepsilon\downarrow0}\frac{\Pr(\text{rim-to-rim near-maximal})}{\varepsilon^4}
 =\frac8{\theta^2}\int_{\substack{U,V,T\ge0\\s(U+V)+cT<1}}T\,dU\,dV\,dT
 =\frac{1}{3\theta^2s^2c^2}
 =\frac4{3\theta^2\sin^2\theta}.
\]
The \(T\)-weight on this simplex yields the four-dimensional Dirichlet vector with parameters \((1,1,2,1)\), as stated. The two possible orders of the endpoint angles are symmetric.

**At the critical aperture.** The tip-to-rim and rim-to-rim maximizing sets are disjoint, and the latter contributes only \(O(\varepsilon^4)\) when \(\theta=\pi/3\). The tip term thus determines the cubic coefficient at the critical aperture. Now set \(\theta=\pi/3+\lambda\varepsilon\). Uniformly on bounded \(\lambda\),
\[
 M_\theta=1+\frac{\sqrt3}{2}\max\{\lambda,0\}\varepsilon+O(\varepsilon^2).
\]
The tip/rim local event is therefore \(V+U\cos(\phi-\psi)<h+o(1)\), where \(h=1-\sqrt3\max\{\lambda,0\}/2\). For \(h>0\), rescale \(U,V\) by \(h\); the weighted radial simplex volume is homogeneous of degree three and yields \(C_{\rm tip}(\pi/3)h^3\). For \(h\le0\), no positive first-order tip volume remains. The rim-endpoint probability is \(O(\varepsilon^4)\) throughout the bounded window; this also follows directly by the same local coordinate bounds. This proves the stated critical profile including its zero branch.

**Coefficient monotonicity and identifiability.** The identity
\[
 -\frac{\log\cos\theta}{\theta^2}
 =\int_0^1(1-t)\sec^2(\theta t)\,dt
\]
shows strict increase in \(\theta\in(0,\pi/3]\). For the rim coefficient, the derivative of its logarithm is \(-2/\theta-2\cot\theta\). It is negative up to the unique root of \(\theta\cot\theta=-1\), equivalently \(\tan\theta=-\theta\), which lies in \((\pi/2,\pi)\); it is positive thereafter. Uniqueness follows since \(\theta\cot\theta\) is strictly decreasing on \((\pi/2,\pi)\), from zero toward minus infinity. Thus the wide-sector coefficient has the claimed sole minimum.

**Exact distributional disintegration.** At any fixed radii \(r,s>0\), define \(a=\arccos((r^2+s^2-q^2)/(2rs))\) when \(|r-s|<q<r+s\). The full exact survival probability is
\[
 \Pr(D>q)=4\int_0^1\!\int_0^1 rs\,G_\theta(q;r,s)\,dr\,ds,
\]
where \(G_\theta=1\) for \(q\le|r-s|\), \(G_\theta=0\) for \(q\ge r+s\), and otherwise \(G_\theta=(1-a/\theta)_+^2\). This exact identity is a reproducibility check, not a separate novelty claim.

## Verification

The supplied standard-library program `sector_verifier.py` independently integrates the exact conditional angular survival formula over localized radial domains. It checks representative narrow and wide apertures and decreasing deficits, corner cases of the angular CDF, analytic coefficient identities, and the unique wide-coefficient minimum. Execution: `python sector_verifier.py`. The last replay returned `SECTOR_CHECKS_OK 88`. The wide-angle finite-deficit evaluations converge more slowly than the small-angle ones; the chosen loose finite-deficit tolerance of nine percent is diagnostic and is **not** a certified error bound. The infinite asymptotic claims follow from the localization and dominated-convergence arguments above, not from these numerical tests.

## Relationship to prior work

The well-studied *circular sector line-picking* problem concerns the very same sampling object, but the inspected MathWorld account tabulates mean distances at selected apertures rather than the diameter tail or its sixty-degree transition. Bäsel's two papers derive full random-distance distributions in right triangles and regular polygons; their results do not cover curved sectors. A publicly available theorem titled *Sharp upper-distance tails at the tip–rim transition of a finite flat cone* provides a geometrically adjacent case, but its **conical intrinsic metric identifies the radial edges**, and its shorter-angle law is uniform at its maximum; the planar sector has an unglued boundary and a triangular angular-gap density that **vanishes** at the endpoint. Its transition is at a different aperture and its wide regime has a different exponent. No same-object formula or stronger statement implying the sharp sector laws was identified in the inspected records. These comparisons do not certify comprehensive historical uniqueness.

## Limitations

The sector is convex with opening strictly less than \(\pi\). The fixed-aperture laws are not uniform as \(\theta\to\pi\) or \(\theta\to0\), and the critical-window result is pointwise for finite \(\lambda\). There is no claim about nonuniform area measures, higher-dimensional cones, other sector shapes, the flat disk, or global historical priority. Numerical quadrature cannot establish the infinite asymptotics, nor does the result establish the complete elementary CDF for every aperture.

## References

1. E. W. Weisstein, *Circular Sector Line Picking*, MathWorld, https://mathworld.wolfram.com/CircularSectorLinePicking.html (online object-and-mean-distance reference, no precisely verified first-posting date).
2. U. Bäsel, *The distribution function of the distance between two random points in a right-angled triangle*, arXiv:1208.6228, first posted 2012-08-30, https://arxiv.org/abs/1208.6228.
3. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted 2012-04-12, https://arxiv.org/abs/1204.2707.
4. *Sharp upper-distance tails at the tip–rim transition of a finite flat cone*, public mathematical research record, 2026-11-02, identifier `published-finding corpus/2026:b319e1ca315a` (related but nonidentical intrinsic metric).
