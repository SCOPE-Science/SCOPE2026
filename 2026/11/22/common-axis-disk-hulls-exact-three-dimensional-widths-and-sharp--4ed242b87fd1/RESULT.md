# Common-axis disk hulls: exact three-dimensional widths and sharp high-dimensional laws

## Finding
For every integer \(m\ge2\), in \(\mathbb R^{m+1}\) with orthonormal coordinates \((x_0,x_1,\ldots,x_m)\), define \(m\) unit disks
\[
D_j=\{x:x_k=0\ (k\notin\{0,j\}),\quad x_0^2+x_j^2\le1\},\qquad 1\le j\le m,
\]
and their convex hull \(K_m=\operatorname{conv}(D_1\cup\cdots\cup D_m)\). Let \(U\) be uniform on the sphere \(S^m\), and let \(W_m\) be the Euclidean width of \(K_m\) perpendicular to \(U\). Then
\[
\boxed{W_m=2\sqrt{U_0^2+\max_{1\le j\le m}U_j^2},\qquad
2/\sqrt m\le W_m\le2.}
\]

For the classical hull of two centered perpendicular disks (\(m=2\)), put \(s=\sqrt{1-w^2/4}\). Its **complete** width distribution is
\[
\boxed{\mathbb P(W_2\le w)=\frac4\pi\left[\arctan\sqrt{1-2s^2}-s\arccos\left(\frac{s}{\sqrt{1-s^2}}\right)\right]}
\quad(\sqrt2\le w\le2).
\]
The cumulative distribution is zero for \(w<\sqrt2\), one for \(w>2\), and is continuous at both endpoints. Its interior density is
\[
\boxed{f_2(w)=\frac{w}{\pi\sqrt{1-w^2/4}}
\arccos\left(\frac{\sqrt{4-w^2}}{w}\right),\qquad\sqrt2<w<2.}
\]
In particular,
\[
\mathbb E W_2^2=\frac83\left(1+\frac1\pi\right),\quad
\mathbb P(W_2\le\sqrt2+\varepsilon)\sim\frac{2^{11/4}}{3\pi}\varepsilon^{3/2},\quad
\mathbb P(W_2>2-\varepsilon)\sim2\sqrt\varepsilon.
\]

Both endpoint laws have exact coefficients in every dimension. Define
\[
A_m=\frac{\Gamma((m+1)/2)m^{m-1/4}}{\pi^{m/2}\sqrt{m-1}\,\Gamma(m+1/2)}.
\]
For every **fixed** integer \(m\ge2\), as \(\varepsilon\downarrow0\),
\[
\boxed{\mathbb P(W_m\le2/\sqrt m+\varepsilon)
=A_m\varepsilon^{m-1/2}+O_m(\varepsilon^{m+1/2}),}
\]
\[
\boxed{\mathbb P(W_m>2-\varepsilon)
=m\varepsilon^{(m-1)/2}+O_m(\varepsilon^{m/2}).}
\]
The two exponents differ by \(m/2\) because a narrow direction is an isolated, partly singular minimizer, whereas maximum-width directions form \(m\) intersecting circles.

Finally let \(G\) have the standard Gumbel law \(\Pr(G\le x)=e^{-e^{-x}}\), and let \(Z\) be an independent standard normal variable. With
\[
a_m=2\log m-\log\log m-\log\pi,
\]
the typical width has the non-Gumbel mixed limit
\[
\boxed{\frac{mW_m^2/4-a_m}{2}\ \Longrightarrow\ G+\frac{Z^2}{2}\qquad(m\to\infty).}
\]
This high-dimensional statement and the fixed-dimensional endpoint laws are distinct limiting regimes.

## Assumptions and scope
The disks all have radius one and share the same diameter along the \(x_0\)-axis; their two-dimensional spanning planes are pairwise orthogonal transverse to that axis. The ambient dimension equals \(m+1\). The convex hull, **not** a Minkowski sum or union, is studied. The direction is Haar-uniform on the unit sphere, and width means the distance between opposite supporting hyperplanes orthogonal to that direction. Scaling every generating disk by \(r>0\) multiplies widths and their endpoints by \(r\). The error constants in the two endpoint formulas depend on fixed \(m\), without claims of uniformity in a simultaneous high-dimensional boundary limit.

## Proof
**1. Support and width.** Projection of a unit vector \(u\in S^m\) onto the plane spanned by \(e_0,e_j\) has norm \(\sqrt{u_0^2+u_j^2}\). This is the support function of \(D_j\). Taking the maximum of the disk supports gives \(h_{K_m}(u)=\max_j\sqrt{u_0^2+u_j^2}\). Central symmetry gives \(h_{K_m}(-u)=h_{K_m}(u)\), hence the displayed width formula. Since \(\max_j u_j^2\ge(1-u_0^2)/m\), the squared half-width is at least \(1/m+(1-1/m)u_0^2\ge1/m\). Equality requires \(u_0=0\) and every \(|u_j|=1/\sqrt m\). The half-width is at most one, with equality exactly on one of the coordinate circles in the \(e_0,e_j\) planes.

**2. Exact \(m=2\) distribution.** Write \(Y=|U_1|\), \(Z=|U_2|\). The identity \(W_2=2\sqrt{1-\min(Y^2,Z^2)}\) converts \(W_2\le w\) into \(Y\ge s\) and \(Z\ge s\). For a uniform direction on \(S^2\), each absolute coordinate is uniform on \([0,1]\). Conditional on \(Y=y\), the coordinate \(Z\) equals \(\sqrt{1-y^2}|\sin\Phi|\), where \(\Phi\) is uniform on \([0,2\pi)\). For \(0\le s\le1/\sqrt2\), define \(Q(s)=\Pr(Y\ge s,Z\ge s)\). The two boundary contributions, equal by symmetry, give
\[
Q'(s)=-\frac4\pi\arccos\left(\frac{s}{\sqrt{1-s^2}}\right),
\qquad Q(1/\sqrt2)=0.
\]
One may equivalently integrate \(\frac2\pi\arccos(s/\sqrt{1-y^2})\) over \(s\le y\le\sqrt{1-s^2}\). Differentiating the claimed closed expression and checking its boundary value proves the CDF. The chain rule with \(ds/dw=-w/(4s)\) proves the density. Taylor expansion of the integral at \(s=1/\sqrt2\) gives the lower \(3/2\) power, and expansion at \(s=0\) gives the upper square-root power. For the second moment, write \(\min(U_1^2,U_2^2)=(U_1^2+U_2^2-|U_1^2-U_2^2|)/2\). In the rotationally invariant \((U_1,U_2)\) plane,
\[
\mathbb E(U_1^2+U_2^2)=\frac23,\qquad
\mathbb E|U_1^2-U_2^2|=\frac23\cdot\frac2\pi=\frac4{3\pi}.
\]
Thus \(\mathbb E W_2^2=4[1-1/3+2/(3\pi)]\), as claimed.

**3. Exact all-dimensional lower coefficient.** Set \(Y_j=U_j^2\) for \(0\le j\le m\). These squares follow the Dirichlet law with all parameters \(1/2\), density
\[
C_m\prod_{j=0}^m y_j^{-1/2},\qquad
C_m=\frac{\Gamma((m+1)/2)}{\pi^{(m+1)/2}},\quad\sum y_j=1.
\]
Let \(\delta=w^2/4-1/m\). The event \(W_m\le w\) is
\[
y_0+\max_{1\le j\le m}y_j\le1/m+\delta.
\]
Put \(a=y_0\). Feasibility forces \(0\le a\le m\delta/(m-1)\). Set \(b=1/m+\delta-a\), \(z_j=b-y_j\) for \(1\le j\le m\). Then \(z_j\ge0\) and \(\sum_jz_j=m\delta-(m-1)a\). The simplex volume in the first \(m-1\) coordinates is exactly \([m\delta-(m-1)a]^{m-1}/(m-1)!\). Uniformly in this region, all \(y_j=1/m+O_m(\delta)\) for \(j\ge1\), so their density factor is \(m^{m/2}(1+O_m(\delta))\). Therefore
\[
\begin{aligned}
\Pr(W_m\le w)&=\frac{C_m m^{m/2}}{(m-1)!}(1+O_m(\delta))\\
&\quad\cdot\int_0^{m\delta/(m-1)}a^{-1/2}[m\delta-(m-1)a]^{m-1}\,da\\
&=\frac{\Gamma((m+1)/2)m^{(3m-1)/2}}{\pi^{m/2}\sqrt{m-1}\,\Gamma(m+1/2)}
\delta^{m-1/2}(1+O_m(\delta)).
\end{aligned}
\]
For \(w=2/\sqrt m+\varepsilon\), \(\delta=\varepsilon/\sqrt m+\varepsilon^2/4\). Substitution yields \(A_m\) and the stated error. This is an analytic simplex integration, not a finite count.

**4. Exact all-dimensional upper coefficient.** Let \(w=2-\varepsilon\) and \(\delta=1-w^2/4=\varepsilon-\varepsilon^2/4\). Since \(u_0^2+\max_j u_j^2=1-\min_j\sum_{k\ne j,\ k\ge1}u_k^2\), the event \(W_m>w\) is the union of the \(m\) events
\[
E_j=\left\{\sum_{1\le k\le m,\ k\ne j}U_k^2<\delta\right\}.
\]
The sum in \(E_j\) has the \(\operatorname{Beta}((m-1)/2,1)\) law, so \(\Pr(E_j)=\delta^{(m-1)/2}\) exactly. For any distinct \(i,j\), the intersection \(E_i\cap E_j\) forces \(\sum_{k=1}^mU_k^2<2\delta\); this sum is \(\operatorname{Beta}(m/2,1/2)\), whose lower tail is \(O_m(\delta^{m/2})\). Finite inclusion-exclusion hence gives \(m\delta^{(m-1)/2}+O_m(\delta^{m/2})\), proving the upper formula.

**5. The mixed large-dimensional limit.** Let \(Z_0,Z_1,\ldots,Z_m\) be independent standard normal variables, so that \(U_j=Z_j/(\sum_{k=0}^m Z_k^2)^{1/2}\) is uniform on \(S^m\). Then
\[
\frac{mW_m^2}{4}=\frac{Z_0^2+\max_{1\le j\le m}Z_j^2}{m^{-1}\sum_{k=0}^mZ_k^2}.
\]
The denominator equals \(1+O_{\Pr}(m^{-1/2})\) while the numerator is \(O_{\Pr}(\log m)\); replacing the denominator by one has \(o_{\Pr}(1)\) error. The Gaussian-squared tail satisfies \(\Pr(Z_1^2>t)\sim\sqrt{2/\pi}\,t^{-1/2}e^{-t/2}\). Consequently for \(a_m=2\log m-\log\log m-\log\pi\),
\[
m\Pr(Z_1^2>a_m+2x)\longrightarrow e^{-x},
\]
and independence gives \((\max_j Z_j^2-a_m)/2\Longrightarrow G\). For every \(m\), \(Z_0^2\) is independent of the maximum over \(j\ge1\). Joint convergence followed by Slutsky's theorem gives the independent convolution \(G+Z^2/2\).

## Verification
Run `python verify_width.py` from the same directory using Python 3, NumPy and SciPy. It independently integrates the two-coordinate spherical conditional distribution at 51 values; differentiates the claimed CDF numerically at 51 values; numerically optimizes over every generating disk at 36 sampled directions; checks the full CDF and exact second moment against 500,000 Haar-sphere samples; independently integrates six small-simplex events across dimensions two through four; and compares five quantiles from a 12,000-sample, dimension-2500 simulation against the mixed limiting law. The checker prints `COMMON_AXIS_DISK_WIDTH_CHECKS_OK` if all tests pass. This is numerical diagnostic evidence; the preceding proof, not the checker, establishes all infinite and limiting claims.

## Relationship to prior work
Finch's *Convex Hull of Two Orthogonal Disks* (arXiv:1211.4514, initially posted in 2012) analyzes exactly the centered \(m=2\) convex body, giving volume, area and its mean width through support integrals. The deterministic support formula is therefore not claimed to be new. Finch does not state a width CDF, density, exact second moment, the sharp lower and upper distribution edges, or the higher-dimensional common-axis family. A separate publicly available study titled *Exact random widths of the orthogonal three-disk hull and sharp hyperdisk endpoint laws* considers **coordinate hyperdisks** \(\{x_j=0,\|x\|\le1\}\), not the radius-one two-dimensional disks all meeting along a single axis; its support depends on the smallest absolute coordinate, while this family's support depends on a **largest** transverse coordinate plus a distinguished axis. Its fixed-dimensional exponents and large-dimensional exponential-squared limit therefore do not imply the present formulas. Another study titled *A one-dimensional derivative law for orthogonal-disk mean width* concerns **separated** two-disk hulls and expectations rather than their full width distribution. The standard Dirichlet distribution of spherical coordinate squares and the Gaussian maximum limit are openly used as known mathematical ingredients; only their combined geometric exact formulas and constants are assessed here as contributions.

## Limitations
The complete elementary distribution is established only for two disks; in arbitrary dimension the theorem gives the complete support range, both sharp distribution-edge asymptotics and a mixed high-dimensional limit, not an elementary full CDF. Disks must share one central diameter, have equal radius and be pairwise orthogonal in the transverse directions. The findings concern directional Euclidean widths, not projected surface areas, random chord lengths, or arbitrary disk configurations. Historical priority remains uncertain: an older distribution-of-the-maximum formula specialized to symmetric Dirichlet vectors may imply part of these statements without discussing disk hulls. No independent mathematical audit has been conducted.

## References
1. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first publicly posted 2012-11-19 (version 3 dated 2016-03-12), especially §§1 and 1.2. https://arxiv.org/pdf/1211.4514
2. U. Bäsel, *The mean width of the oloid and integral geometric applications of it*, arXiv:1604.07245, first posted 2016-04-25; the oloid is a separated-circle configuration. https://arxiv.org/abs/1604.07245
3. *Exact random widths of the orthogonal three-disk hull and sharp hyperdisk endpoint laws*, published mathematical result dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-random-widths-of-the-orthogonal-three-disk-hull-and-sharp--d1df18476a61
4. *A one-dimensional derivative law for orthogonal-disk mean width*, published mathematical result dated 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-dimensional-derivative-law-for-orthogonal-disk-mean-width--6e52fbc79bdf
5. Standard background: the Gaussian-sphere representation, Dirichlet distribution of squared coordinates, the beta distribution of projection norms and the classical Gumbel extreme-value limit.
