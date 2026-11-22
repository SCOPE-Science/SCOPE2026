# Strict stochastic area order and a threefold arcsine limit for Chapple–Poncelet triangles

## Finding
For every \(0<d<1\), choose one vertex \(P_\theta=(\cos\theta,\sin\theta)\) with \(\theta\sim\operatorname{Uniform}[0,2\pi)\) on the unit circle, and close the unique Chapple–Poncelet triangle tangent to the inner circle of center \((d,0)\) and radius \(r=(1-d^2)/2\). Let \(J_d\) be its Euclidean area. This note establishes an **exact full cumulative distribution function**, **strict pointwise and stochastic decrease as \(d\) increases**, and a **threefold arcsine limit as \(d\downarrow0\)**. It does not claim the already known pointwise area formula or area extrema as new.

Set \(w=1+d^2-2d\cos\theta\), \(u=\sqrt{w-r^2}\), and
\[
J_d(\theta)=r u\left(1+\frac{4r}{r^2+u^2}\right).
\]
This is the classical deterministic formula. Write
\[
\begin{aligned}
j_-(d)&=\frac{1+d}{4}\big((1-d)(3+d)\big)^{3/2},\\
j_+(d)&=\frac{1-d}{4}\big((1+d)(3-d)\big)^{3/2}.
\end{aligned}
\]
For \(j_-<y<j_+\), define \(u_1<u_2<u_3\) to be the three positive roots in the geometric range of
\[
u^3-(y/r)u^2+(r^2+4r)u-(y/r)r^2=0.
\]
Define \(\Theta_d(u)=\arccos[(1+d^2-r^2-u^2)/(2d)]\). Then
\[
\boxed{\Pr(J_d\le y)=\frac{\Theta_d(u_1)+\Theta_d(u_3)-\Theta_d(u_2)}{\pi}.}
\]
The CDF is zero for \(y\le j_-\) and one for \(y\ge j_+\). The area has no atoms for \(0<d<1\). For \(0<d_1<d_2<1\) and every \(\theta\),
\[
\boxed{J_{d_2}(\theta)<J_{d_1}(\theta).}
\]
In particular \(J_{d_2}\) is strictly smaller in first-order stochastic order, and \(\mathbb E\phi(J_{d_2})<\mathbb E\phi(J_{d_1})\) for every strictly increasing continuous \(\phi\) with finite expectations.
Finally, putting \(m_d=(j_++j_-)/2\), \(s_d=(j_+-j_-)/2\),
\[
\boxed{(J_d-m_d)/s_d\ \Longrightarrow\ Z,\qquad \Pr(Z\in dz)=\frac{\mathbf1_{(-1,1)}(z)}{\pi\sqrt{1-z^2}}\,dz.}
\]

## Assumptions and scope
The outer circle is Euclidean and fixed at unit radius. The inner circle is strictly inside, and Euler's bicentric relation is exactly satisfied. The sample is **uniform in the starting vertex's outer-circle angle**, rather than uniform in tangent length, area, or an invariant poristic parameter. Both tangent orientations lead to the same unordered triangle. The singular concentric endpoint \(d=0\) is used only as a limiting family; the degenerate endpoint \(d=1\) is excluded. Distances, radii and areas are nondimensionalized by outer radius.

## Proof
**1. Classical area reduction and exact pushforward.** For a vertex \(P_\theta\), the length of either tangent to the inner circle is \(u=\sqrt{|P_\theta-(d,0)|^2-r^2}\). The tangent lengths of the other vertices, or the classical relation of Radić, give \(J_d=r u(1+4r/(r^2+u^2))\). The variable \(\theta\) folded to \([0,\pi]\) is uniform, and \(u\) increases strictly from \(u_-=\sqrt{(1-d)^2-r^2}\) to \(u_+=\sqrt{(1+d)^2-r^2}\). Differentiation of the rational expression \(j(u)\) gives precisely two simple stationary points inside this interval:
\[
b=\frac{2r u_+}{(1+d)^2},\qquad c=\frac{2r u_-}{(1-d)^2},\qquad u_-<b<c<u_+.
\]
The three consecutive branches of \(j(u)\) are increasing, decreasing, increasing. The endpoint values are \(j(u_-)=j_-\), \(j(u_+)=j_+\); the interior local minimum equals \(j_-\) and the interior local maximum equals \(j_+\). For each interior level \(y\), three roots, respectively in \((u_-,b)\), \((b,c)\), \((c,u_+)\), partition the sublevel set into \([u_-,u_1]\cup[u_2,u_3]\). Push the uniform folded angle forward to obtain the displayed CDF. The monotone smooth branches imply absence of atoms.

**2. Strict monotonicity certificate.** Put \(c_\theta=\cos\theta\) and \(x=(1+c_\theta)/2\in[0,1]\). With \(W=1+d^2-2dc_\theta\), note the exact identity
\[
J_d^2=r^2(W-r^2)(W+4r)^2/W^2.
\]
Exact differentiation and cancellation yield
\[
\frac{\partial}{\partial d}\log(J_d^2)=-\frac{8d\,P(d,x)}{(1-d^2)W(3-d^2-2dc_\theta)(3+6d^2-d^4-8dc_\theta)}.
\]
All denominator factors are strictly positive for \(0<d<1\), \(-1\le c_\theta\le1\), as follows from \(W\ge(1-d)^2\) and the equivalent positive geometric expressions \(3-d^2-2dc_\theta=W+2(1-d^2)\) and \(3+6d^2-d^4-8dc_\theta=4(W-r^2)\). Here \(P\) is the polynomial specified equivalently by
\[
\begin{aligned}
P(d,x)=-[&20c_\theta^3d^3-4c_\theta^3d+4c_\theta^2d^6-12c_\theta^2d^4-40c_\theta^2d^2\\
&+c_\theta d^7-19c_\theta d^5+31c_\theta d^3+35c_\theta d\\
&-d^8+5d^6+7d^4-21d^2-6],\quad c_\theta=2x-1.
\end{aligned}
\]
For an exact positivity certificate let \(B_{ij}\) be the following rational grid, with \(i=0,\dots,8\) and \(j=0,\dots,3\):

| \(i\) | \(j=0\) | \(j=1\) | \(j=2\) | \(j=3\) |
|---|---|---|---|---|
| 0 | 6 | 6 | 6 | 6 |
| 1 | 79/8 | 191/24 | 97/24 | 17/8 |
| 2 | 223/14 | 214/21 | 33/14 | 3/7 |
| 3 | 351/14 | 263/21 | 47/42 | 0 |
| 4 | 268/7 | 512/35 | 12/35 | 0 |
| 5 | 394/7 | 334/21 | 0 | 0 |
| 6 | 552/7 | 320/21 | 0 | 0 |
| 7 | 104 | 32/3 | 0 | 0 |
| 8 | 128 | 0 | 0 | 0 |

Direct rational polynomial expansion verifies
\[
P(d,x)=\sum_{i=0}^{8}\sum_{j=0}^3B_{ij}\binom8i d^i(1-d)^{8-i}\binom3j x^j(1-x)^{3-j}.
\]
Every coefficient is nonnegative; the \(i=0\) row is strictly positive, so for every \(0<d<1\) and all \(0\le x\le1\), \(P(d,x)>0\). Therefore the logarithmic derivative is strictly negative at every admissible \((d,\theta)\). Couple the two random areas by the same \(\theta\) to conclude strict first-order stochastic order, as claimed.

**3. Threefold limit.** Elementary Taylor expansion of the exact area, uniform in \(\theta\), gives
\[
J_d(\theta)=\frac{3\sqrt3}{4}-\sqrt3d^2-\frac{\sqrt3}{9}d^3\cos(3\theta)+O(d^4).
\]
The exact extrema similarly give \(m_d=3\sqrt3/4-\sqrt3d^2+O(d^4)\) and \(s_d=(\sqrt3/9)d^3+O(d^5)\). Thus \((J_d-m_d)/s_d=-\cos(3\theta)+O(d)\) uniformly. If \(\theta\) is uniform on \([0,2\pi)\), then \(-\cos(3\theta)\) has the arcsine density on \((-1,1)\), proving weak convergence.

## Verification
Run `python verify.py` with Python 3.10+ and SymPy. The supplied standalone checker verifies **36 rational Bernstein interpolation identities** (an exact polynomial equality by degree bounds), the symbolic logarithmic derivative identity, **600 direct Euclidean tangent-construction comparisons**, **45 independently sampled angular CDF quadratures**, **15 monotonicity comparisons** and **15 small-offset angular-harmonic diagnostics**. Numerical quadrature checks corroborate but do not replace the proofs above. The inequalities are established by an exact Bernstein rational certificate. No external or infinite computerized certification is claimed.

## Relationship to prior work
Radić (2003) proves poristic triangle parameter relations; Radić (2004) gives the pointwise area function and its extrema. These results are **premises, not claimed discoveries**. László (2019) integrates this classical area formula against a tangent-length variable to give integral area inequalities; the inspected text does not impose uniform outer-circle angular sampling, derive the cubic-branch CDF, prove strict stochastic ordering across circle offsets, or obtain the normalized threefold arcsine limit. Avksentyev and Protasov (2016) study invariant measures for Poncelet-type dynamics; an invariant measure is not automatically the specified outer arclength measure. Closely related probability studies on arbitrary random cyclic triangles and deforming ovals use different sampling ensembles. The precise combination of a complete uniform-angle law, a globally strict order and a threefold degeneration is the new claim. Originality remains contingent on broader historical review.

## Limitations
The CDF is specified by three ordered cubic roots rather than a single expression in elementary real radicals. Claims do not concern the porism-invariant sampling measure, arbitrary nested conics, or nonsymmetric different distributions of starting points. The exact pointwise area/extremal results are explicitly previously known. The result has self-review only; independent validation and exhaustive historical priority checks are not performed.

## References
- M. Radić, “Some Relations Concerning Triangles and Bicentric Quadrilaterals in Connection with Poncelet's Closure Theorem,” *Math. Maced.*, 1 (2003), 35–58. https://im-pmf.weebly.com/uploads/5/8/9/8/58988609/mirko_radic.pdf
- M. Radić, “Extreme Areas of Triangles in Poncelet's Closure Theorem,” *Forum Geometricorum*, 4 (2004), 23–26; first public date 2004-02-23. Full text in collected journal: https://mathematicalolympiads.wordpress.com/wp-content/uploads/2012/08/forum-geometricorum-all-volumes.pdf
- L. László, “An inequality for the areas of Poncelet triangles,” *Ann. Univ. Sci. Budapest., Sect. Comput.*, 49 (2019), 317–323. https://ac.inf.elte.hu/Vol_049_2019/doi/317_49.pdf
- E. Avksentyev and V. Protasov, “Universal measure for Poncelet-type theorems,” arXiv:1610.00276 (2016). https://arxiv.org/abs/1610.00276
