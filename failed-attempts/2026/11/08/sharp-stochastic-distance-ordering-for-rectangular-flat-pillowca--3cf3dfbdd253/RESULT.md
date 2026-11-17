# Sharp stochastic distance ordering for rectangular flat pillowcases

## Finding

Let \(a,b>0\), let \(T_{a,b}=\mathbb R^2/(a\mathbb Z\oplus b\mathbb Z)\) carry its intrinsic Euclidean flat metric, and let the **flat pillowcase** \(P_{a,b}=T_{a,b}/\{z\sim-z\}\) carry the induced intrinsic quotient metric and normalized area measure. For independent area-uniform \(X,Y\in P_{a,b}\), write \(F_{a,b}(r)=\Pr\{d(X,Y)\le r\}\). Define \(A=\max(a,b)/2\), \(B=\min(a,b)/2\), and \(R=\sqrt{A^2+B^2}\). For \(r\ge0\), set

\[
J_{A,B}(r)=\begin{cases}
\pi r^2/4,&0\le r\le B,\\
\big[B\sqrt{r^2-B^2}+r^2\arcsin(B/r)\big]/2,&B<r\le A,\\
\big[A\sqrt{r^2-A^2}+B\sqrt{r^2-B^2}+r^2(\arcsin(A/r)+\arcsin(B/r)-\pi/2)\big]/2,&A<r<R,\\
AB,&r\ge R.
\end{cases}
\]

Then the complete geodesic-distance law is

\[
\boxed{F_{a,b}(r)=1-\left(1-\frac{J_{A,B}(r)}{AB}\right)^2\quad(r\ge0),\qquad F_{a,b}(r)=0\quad(r<0).}
\]

**Sharp all-threshold shape ordering.** If \(ab=s^2\) is fixed and \(a\ne b\), then

\[
F_{a,b}(r)\le F_{s,s}(r)\quad\text{for every real }r,
\]

with **strict inequality exactly for** \(\min(a,b)/2<r<\sqrt{a^2+b^2}/2\), and equality outside that interval. Consequently the square pillowcase uniquely minimizes (under fixed quotient area) every strictly increasing expected loss of distance for which the expectation is finite, and all nontrivial upper-tail quantiles are no smaller for a nonsquare rectangle. In particular it uniquely minimizes mean geodesic distance and all positive distance moments.

**Sharp far-distance law.** At the maximum possible distance \(R=\sqrt{a^2+b^2}/2\),

\[
\boxed{\Pr\{d(X,Y)>R-\varepsilon\}\sim \frac{4(a^2+b^2)^2}{a^4b^4}\varepsilon^4\qquad(\varepsilon\downarrow0).}
\]

The spherical-cone points of the quotient have cone angle \(\pi\), and the quotient area is \(ab/2\). The identity \(F_{a,b}=1-(1-H_{a,b})^2\), where \(H_{a,b}\) is the two-point flat-torus distance CDF, in fact holds for **every** flat torus \(\mathbb R^d/\Lambda\) quotiented by central inversion, in any positive dimension \(d\).

## Assumptions and scope

The pillowcase is the metric quotient by the isometric involution \(z\mapsto-z\), including its four cone points, with geodesics measured intrinsically and normalized \(2\)-dimensional area. Points are independent and uniform; finite sampling, extrinsic distances in an embedding, and nonrectangular shape optimization are not claimed. Swapping \(a,b\) makes the same isometry class. All formulas include \(a=b\) and endpoint radii by continuity.

## Proof

**1. Quotient and Haar independence.** Write \(q:T_{a,b}\to P_{a,b}\). If \(U,V\) are independent Haar-uniform torus points, \(q(U),q(V)\) are independently uniform on the quotient. For every \(u,v\in T_{a,b}\), the metric quotient formula gives

\[
d_P(q(u),q(v))=\min\{d_T(u-v,0),\ d_T(u+v,0)\}.
\]

The homomorphism \((u,v)\mapsto(u-v,u+v)\) from \(T_{a,b}^2\) onto itself is surjective: any pair \((z,w)\) admits solutions to \(2u=z+w\) and \(2v=w-z\) since multiplication by \(2\) is surjective on a flat torus. The pushforward of Haar probability under a surjective compact-group homomorphism is Haar probability, hence the two coordinate images are *independent* uniform torus points. Consequently, if \(H(r)=\Pr\{d_T(U,0)\le r\}\),

\[
\Pr(d_P(X,Y)>r)=[1-H(r)]^2.
\]

This argument is dimension-free and applies to arbitrary full-rank Euclidean lattices; no independence of the original sample points after quotienting is assumed beyond the two independent Haar lifts.

**2. Exact torus CDF.** Every torus point has a unique minimal-displacement representative, up to a zero-area boundary, in the centered fundamental rectangle \([-A,A]\times[-B,B]\). This representative is uniform there. Thus \(H(r)=4J_{A,B}(r)/(4AB)=J_{A,B}(r)/(AB)\), where \(J\) is the Euclidean area of the intersection of the radius-\(r\) disk with \([0,A]\times[0,B]\). Integrate horizontal slices \(\min(B,\sqrt{(r^2-x^2)_+})\) on \(0\le x\le A\). Elementary antiderivatives \(\int\sqrt{r^2-x^2}\,dx=[x\sqrt{r^2-x^2}+r^2\arcsin(x/r)]/2\) give exactly the displayed four branches. The quotient identity completes the CDF proof.

**3. Fixed-area stochastic ordering and strictness.** Put \(AB=c^2\), \(A=c e^t\), \(B=c e^{-t}\) with \(t\ge0\). Let \(J_r(t)=\operatorname{area}([0,A]\times[0,B]\cap B(0,r))\). At radii away from the finite transition set, differentiation with respect to the rectangle edges gives

\[
J_r'(t)=A\min\{B,\sqrt{(r^2-A^2)_+}\}-B\min\{A,\sqrt{(r^2-B^2)_+}\}.
\]

For \(t>0\), this is \(0\) if \(r\le B\) or \(r\ge\sqrt{A^2+B^2}\), and negative if \(B<r<\sqrt{A^2+B^2}\): when \(B<r\le A\), the first term vanishes and the second is positive; when \(A<r<\sqrt{A^2+B^2}\), both square-root terms are unclipped and their squared difference has sign

\[
A^2(r^2-A^2)-B^2(r^2-B^2)=(A^2-B^2)(r^2-A^2-B^2)<0.
\]

The derivative is continuous across regimes wherever needed for monotonic integration. The functions \(B(t)\) and \(R(t)=\sqrt{A(t)^2+B(t)^2}\) decrease and increase respectively for \(t>0\). Therefore integrating from the square \(t=0\) to any nonsquare \(t>0\) gives \(J_r(t)\le J_r(0)\), strictly exactly when \(B(t)<r<R(t)\). Because \(u\mapsto1-(1-u)^2\) is strictly increasing on \([0,1)\), the same statement holds for \(F\). Integrating survival functions against any strictly increasing loss on the common bounded support (or using the induced strict first-order stochastic domination) establishes the claims on means and moments.

**4. High-distance boundary law.** In each of the four rectangle corners, set \(x=A-u\), \(y=B-v\) with \(u,v\ge0\). As \(\varepsilon\downarrow0\), the inequality \(x^2+y^2>(R-\varepsilon)^2\) is equivalent to \(Au+Bv<R\varepsilon+O(\varepsilon^2+u^2+v^2)\). The excluded area in each corner is \((R\varepsilon)^2/(2AB)+o(\varepsilon^2)\). Dividing the four-corner total by rectangle area \(4AB\), we get

\[
1-H(R-\varepsilon)=\frac{R^2}{2A^2B^2}\varepsilon^2+o(\varepsilon^2)=\frac{2(a^2+b^2)}{a^2b^2}\varepsilon^2+o(\varepsilon^2).
\]

Squaring this tail by Step 1 proves the fourth-order law. The maximum \(R\) is actually attained between images of suitable pairs of torus points (surjectivity in Step 1 allows both difference and sum displacements at a Voronoi corner), so it is the metric diameter, not merely the distribution's supremum.

## Verification

The standalone script `pillowcase_geodesic_check.py` evaluates all four CDF branches and directly samples 450,000 pairs in each of four rectangular quotient metrics. It checks nine interior CDF radii per geometry against empirical frequencies. In fifteen separate area-and-aspect configurations it checks non-strict CDF ordering on a grid of 300 radii. Three geometries and three small values of \(\varepsilon\) check convergence to the fourth-order tail coefficient. It reports `PILLOWCASE_GEODESIC_LAW_OK`. These finite computations corroborate the proof but do not replace the universal analytic argument.

As an additional normalization check, for \(0\le r\le\min(a,b)/2\) the formula simplifies **exactly** to \(F(r)=2\pi r^2/(ab)-\pi^2r^4/(a^2b^2)\), consistent with the cone-angle \(\pi\) geometry and area \(ab/2\).

## Relationship to prior work

Wu (2014) studies the flat pillowcase and its abelian branched covers through relative cohomology and affine-diffeomorphism actions, not intrinsic random pair-distance distributions. Silverman (1978) studies statistical distance processes on circles, tori and spheres; the accessible abstract does not resolve whether it contains a special quotient law. An October 2014 public discussion computes the ordinary flat square torus's radial distance CDF as a disk-square intersection area, a special input that is explicitly **not** claimed as new. Similarly, generic short-distance cone-surface expansions determine the leading quartic term near \(r=0\); the contribution here is the *complete* quotient law for all radii and lattices, the strict all-threshold shape theorem for rectangular pillows, and the fourth-order far-distance tail. The quotient factorization and monotone shape comparison are not consequences of a torus *CDF statement alone* without the independent sum-and-difference argument and the disk-rectangle comparison.

## Limitations

The exact quotient-distance factorization holds for arbitrary flat torus lattices and dimensions, but the closed elementary CDF and sharp square-optimality statement are restricted to rectangular planar lattices. This does not optimize over skew planar lattices or over other Euclidean cone surfaces, and no general distance-density recovery or robust estimation theorem is asserted. Historical priority might be affected by an unindexed discussion of two-point distances on flat pillowcase orbifolds, and the full text of Silverman (1978) was not accessible through the checked open source; no claim of independent mathematical certification is made.

## References

1. C. Wu, *The relative cohomology of abelian covers of the flat pillowcase*, arXiv:1402.6667 (first public version 2014-02-26), full preprint inspected, especially introduction and geometric construction of the flat pillowcase in §2.
2. B. W. Silverman, *Distances on circles, toruses and spheres*, *Journal of Applied Probability* **15** (1978), 136–143, DOI:10.2307/3213243 (abstract inspected; full technical comparison unavailable).
3. R. Israel, answer to *Random Distance on Torus*, Mathematics Stack Exchange, 2014-10-28, https://math.stackexchange.com/questions/995560/random-distance-on-torus (full short answer inspected; the centered-square disk-intersection observation is credited as known).
