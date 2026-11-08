# Exact edge-clearance law and first clipping singularity of Euclidean hypercubes

## Finding

For every integer \(d\ge3\), let \(Q_d=[0,s]^d\) with \(s>0\), let \(E_d\) be its union of one-dimensional edges (its geometric 1-skeleton), and let \(X\) be uniform by volume on \(Q_d\). Put \(h=s/2\) and \(T_d=\operatorname{dist}(X,E_d)/h\). Write \(\omega_j=\pi^{j/2}/\Gamma(j/2+1)\) for the unit \(j\)-ball volume and
\[
 a_d=\frac{d\omega_{d-1}}{2^{d-1}},\qquad
 b_d=d\int_{\{y\in[0,\infty)^{d-1}:\|y\|_2\le1\}}\max_i y_i\,dy.
\]
The exact small-clearance law is
\[
 F_d(t):=\Pr(T_d\le t)=a_dt^{d-1}-b_dt^d,\qquad 0\le t\le1.
\]
For \(1<t<\sqrt2\), its exact first-clipping continuation is
\[
 F_d(t)=a_dt^{d-1}-b_dt^d+
 \frac{d(d-1)\omega_{d-2}}{2^{d-2}}
 \int_1^t (v-1)(t^2-v^2)^{(d-2)/2}\,dv.
\]
In particular, with \(\varepsilon\downarrow0\),
\[
 F_d(1+\varepsilon)-\bigl[a_d(1+\varepsilon)^{d-1}-b_d(1+\varepsilon)^d\bigr]
 =K_d\varepsilon^{(d+2)/2}+O_d(\varepsilon^{(d+4)/2}),
 \quad K_d=\frac{4(d-1)\omega_{d-2}}{(d+2)2^{(d-2)/2}}>0.
\]
Thus \(F_d\) is of class \(C^{\lceil(d+2)/2\rceil-1}\) but not \(C^{\lceil(d+2)/2\rceil}\) at \(t=1\); the singularity marks the geometric transition at half the side length.

The distance support is \([0,\sqrt{d-1}]\), and its upper endpoint satisfies the sharp universal law
\[
 \Pr\bigl(T_d>\sqrt{d-1}-\varepsilon\bigr)
 \sim\frac{(d-1)^{(d-2)/2}}{(d-1)!}\varepsilon^d.
\]
The squared distance has the exact expectation
\[
 \mathbb E[\operatorname{dist}(X,E_d)^2]
 =\frac{s^2}{4}\frac{d(d-1)}{3(d+2)}.
\]
For a three-dimensional cube the **complete** distribution, not only its first interval, is elementary:
\[
 F_3(t)=\begin{cases}
 0,&t<0,\\
 \frac{3\pi}{4}t^2-\sqrt2\,t^3,&0\le t\le1,\\
 3t^2\bigl(\arcsin(1/t)-\pi/4\bigr)-\sqrt2\,t^3+(2t^2+1)\sqrt{t^2-1},&1<t<\sqrt2,\\
 1,&t\ge\sqrt2.
 \end{cases}
\]
In particular, \(\Pr(T_3>\sqrt2-\varepsilon)\sim\varepsilon^3/\sqrt2\) and \(\mathbb E[\operatorname{dist}(X,E_3)^2]=s^2/10\).

The classical union-volume formula for three perpendicular cylinders already implies the **low-clearance cubic polynomial** in dimension three. It is included for continuity of the distribution, not asserted as independently new. The scope of the contribution is the complete cubic edge-clearance distribution, the general-dimensional exact first clipping correction and its sharp differentiability order, and the all-dimensional upper-endpoint law.

## Assumptions and scope

Here edges are **closed finite line segments** of the cube, including endpoints. The metric is ordinary Euclidean distance in the ambient \(\mathbb R^d\), not graph distance along edges. The sample is independent-coordinate volume-uniform. All dimensional claims require integer \(d\ge3\). Formulas are normalized by the half-side length \(h=s/2\). No assertion is made about non-cubic rectangular boxes, nonuniform sampling, arbitrary polytope skeleta, or the entire middle profile in dimensions \(d>3\).

## Proof

**1. Exact reduction to order statistics.** For \(X=(X_1,\ldots,X_d)\), define face gaps \(G_i=\min\{X_i,s-X_i\}\). An edge parallel to coordinate \(j\) has unrestricted coordinate \(j\), and its other coordinates are endpoints. Its closest point to \(X\) therefore has squared distance \(\sum_{i\ne j}G_i^2\). Minimizing over \(j\) removes the largest gap. Because the \(G_i/h\) are independent uniform random variables on \([0,1]\), if \(0<U_{(1)}<\cdots<U_{(d)}<1\) are their ordered values, then almost surely
\[
 T_d^2=\sum_{i=1}^{d-1}U_{(i)}^2.
\]
The order-statistic joint density is exactly \(d!\) on the increasing simplex. Integrating the largest coordinate first yields
\[
 F_d(t)=d!\int_{0\le u_1\le\cdots\le u_{d-1}\le1}
 \bigl(1-u_{d-1}\bigr)
 \mathbf1_{\{\sum_{i=1}^{d-1}u_i^2\le t^2\}}
 \,du_1\cdots du_{d-1}.
\]
Ties and endpoint coincidences have probability zero and do not change the result.

**2. Exact short-radius law.** If \(0\le t\le1\), the upper coordinate bound is redundant on the ball of radius \(t\). By permutation symmetry, its ordered nonnegative sector occupies \(1/(d-1)!\) of the positive-orthant ball. Separating the constant and maximal-coordinate terms, then scaling the integral by \(t\), gives precisely \(a_dt^{d-1}-b_dt^d\) with the coefficients stated above. This is an exact identity throughout the closed interval, not a Taylor approximation.

**3. First clipping and regularity.** Analytically continue the **untruncated** ordered-ball integral, including its factor \((1-u_{d-1})\), to radii just above one. Its value is still \(a_dt^{d-1}-b_dt^d\). The actual integral must omit the region \(u_{d-1}>1\), where the integrand has become negative. Therefore the actual distribution is the polynomial continuation **plus** the integral of \((u_{d-1}-1)\) over that omitted region. For \(1<t<\sqrt2\) and \(v=u_{d-1}\ge1\), every remaining coordinate is at most \(\sqrt{t^2-v^2}<1\le v\). Thus ordering with respect to \(v\) is automatic, while the remaining \(d-2\) variables occupy \(1/(d-2)!\) of a positive-orthant ball. Their volume is \(\omega_{d-2}(t^2-v^2)^{(d-2)/2}/[2^{d-2}(d-2)!]\). Multiplication by \(d!\) proves the stated clipping integral.

Put \(t=1+\varepsilon\), \(v=1+z\). Uniformly for \(0\le z\le\varepsilon\), \(t^2-v^2=2(\varepsilon-z)[1+O(\varepsilon)]\). Therefore the clipping integral equals its prefactor times
\[
 2^{(d-2)/2}\int_0^\varepsilon z(\varepsilon-z)^{(d-2)/2}dz\,[1+O_d(\varepsilon)].
\]
The beta integral is \(4\varepsilon^{(d+2)/2}/[d(d+2)]\), yielding exactly \(K_d\). The coefficient is nonzero; a one-sided power \(\varepsilon_+^{(d+2)/2}\) proves the asserted finite differentiability, including even dimensions where the power is integral and the corresponding derivative jumps.

**4. Three dimensions.** In dimension three the ordered-pair density after integrating the largest coordinate is \(6(1-v)\,du\,dv\) on \(0<u<v<1\). Hence
\[
 F_3(t)=6\int_0^{\min(t,1)}(1-v)\min\{v,\sqrt{t^2-v^2}\}\,dv.
\]
Split this integral at \(v=t/\sqrt2\) (with the upper endpoint clipped at one) and integrate elementary polynomials and circular arcs. This gives the displayed piecewise formula, including continuity at both transition points. For \(d=3\), \(a_3=3\pi/4\) and \(b_3=\sqrt2\), since polar integration over a quadrant yields \(\int_{B_2^+}\max(y_1,y_2)dy=\sqrt2/3\).

**5. Upper tail in every dimension.** The distance is maximized at the cube center, where all normalized gaps equal one, yielding \(\sqrt{d-1}\). Set \(V_i=1-U_i\); order them decreasingly \(V_{[1]}\ge\cdots\ge V_{[d]}\). The tail event is equivalent, after scaling by \(\varepsilon\), to the asymptotic simplex condition \(\sum_{i=1}^{d-1}V_{[i]}<\sqrt{d-1}\,\varepsilon+O_d(\varepsilon^2)\). The bounded-coordinate constraints become irrelevant in this shrinking neighborhood. Integrating the smallest gap \(V_{[d]}\) first and removing the ordering of the others leaves \(d\) times the integral of their minimum over the positive simplex. For \(m=d-1\) and \(L>0\), layer cake gives
\[
 \int_{\{y_i\ge0,\sum_{i=1}^{m}y_i\le L\}}\min_i y_i\,dy
 =\int_0^{L/m}\frac{(L-mz)^m}{m!}\,dz
 =\frac{L^{m+1}}{m(m+1)!}.
\]
Taking \(L=\sqrt{d-1}\,\varepsilon\), multiplying by \(d\), and applying a bounded-domain scaling limit yields the sharp coefficient \((d-1)^{(d-2)/2}/(d-1)!\). The omitted quadratic terms alter only the relative \(o(1)\) factor.

**6. Exact second moment.** Since the sum of the \(d\) squared normalized gaps has expectation \(d/3\), and the maximum of \(d\) independent uniforms has squared expectation \(d/(d+2)\),
\[
 \mathbb E[T_d^2]=\frac d3-\frac d{d+2}=\frac{d(d-1)}{3(d+2)}.
\]
Multiplication by \(h^2=s^2/4\) completes the statement.

## Verification

The supplied `check.py` tests the three-dimensional closed form against an independent one-dimensional order-statistic quadrature, directly samples point-to-edge distances, checks the exact second moment and positive clipping coefficient, and evaluates the general-dimensional clipping integrals for dimensions three through eight. It verifies the geometric nearest-edge identity against direct enumeration of actual finite cube edges. Use `python check.py` after installing the dependencies listed in `requirements.txt`. These numerical checks corroborate finite cases and do not replace the all-dimensional analytic arguments.

## Relationship to prior work

Steinmetz-cylinder inclusion–exclusion supplies the low-radius cubic polynomial for the three-dimensional case: it does not by itself provide the finite-cube first-clipping continuation or the all-dimensional endpoint and regularity laws. Mathai, Moschopoulos and Pederzoli (1999) treat distances between random points in cubes. Tong and Pan (arXiv initial public version 21 January 2016) treat two-point distance distributions in planar polygonal regions, not distances from a random point to the fixed geometric 1-skeleton of a higher-dimensional cube. The Hildebrand and collaborators' intersecting-cylinder reports are relevant to the classical unbounded cylinder integrals; their inaccessible complete text leaves a residual risk concerning earlier equivalent volume formulations. The earliest exactly dated **verified public posting among the directly inspected primary papers** is the arXiv version of 21 January 2016; the classical works cited above are older but their first-publication days were not verified.

## Limitations

Novelty is a best-knowledge assessment, not proof of priority. The short-radius cubic identity in dimension three is explicitly known. The complete report of Hildebrand et al. (2012) and the entire 1999 cube-distance paper were not available for material full-text inspection, although their catalogued topics differ. The full distribution in dimensions greater than three beyond the first clipping interval is not evaluated here. The source date is a precisely verified public posting date of a related predecessor, not a claimed creation or journal-publication date for this finding. Independent peer or formal verification has not occurred.

## References

1. F. Tong and J. Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407v1 (first publicly submitted 21 January 2016), https://arxiv.org/html/1602.03407v1.
2. A. M. Mathai, P. G. Moschopoulos and G. Pederzoli, *Distance between random points in a cube*, Statistica 59(1) (1999), pp. 61–81, https://rivista-statistica.unibo.it/article/view/1104.
3. P. Bourke, *Intersecting cylinders*, original exposition dated December 2003, https://www.paulbourke.net/geometry/cylinders/.
4. A. J. Hildebrand, L. Kong, A. Turner and A. Uppal, *Applications of n-dimensional Integrals: Random Points, Broken Sticks and Intersecting Cylinders*, Illinois Geometry Lab project report (dated 11 December 2012); bibliographic record https://oeis.org/A349580.
