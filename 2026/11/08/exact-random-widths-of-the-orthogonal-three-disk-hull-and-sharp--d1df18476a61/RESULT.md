# Exact random widths of the orthogonal three-disk hull and sharp hyperdisk endpoint laws

## Finding
For each integer \(d\ge3\), let
\[
H_d=\operatorname{conv}\!\left(\bigcup_{j=1}^{d}\{x\in\mathbb R^d:x_j=0,\ \|x\|_2\le1\}\right).
\]
This is a centrally symmetric full-dimensional convex body: in three dimensions it is the convex hull of the three unit disks in the coordinate planes. Let \(U\) be Haar-uniform on the unit sphere \(S^{d-1}\), and let \(W_d=h_{H_d}(U)+h_{H_d}(-U)\) be its random directional Euclidean width. Then
\[
W_d=2\sqrt{1-\min_{1\le j\le d}U_j^2}\quad\text{almost surely},
\qquad 2\sqrt{1-1/d}\le W_d\le2.
\]
In \(d=3\), set \(a=2\sqrt{2/3}\), and for \(a\le w\le2\) set \(t=\sqrt{1-w^2/4}\). The **complete width distribution** is
\[
\boxed{\mathbb P(W_3\le w)=-2-3t+\frac{12}{\pi}\left[t\arcsin\!\left(\frac{t}{\sqrt{1-t^2}}\right)+\arctan\!\sqrt{1-2t^2}\right].}
\]
The distribution function is zero below \(a\) and one above \(2\); the inverse trigonometric functions take their principal real branches.

In every dimension \(d\ge3\), both endpoint laws have explicit sharp constants:
\[
\boxed{\mathbb P(W_d\le 2\sqrt{1-1/d}+\varepsilon)
\sim \frac{d^{d-1/2}(d-1)^{(d-1)/2}\Gamma(d/2)}{\pi^{d/2}(d-1)!}\,\varepsilon^{d-1}}
\quad(\varepsilon\downarrow0),
\]
\[
\boxed{\mathbb P(W_d>2-\varepsilon)
\sim\frac{2d\Gamma(d/2)}{\sqrt\pi\Gamma((d-1)/2)}\,\sqrt\varepsilon}
\quad(\varepsilon\downarrow0).
\]
Finally, as \(d\to\infty\),
\[
\boxed{d^3(2-W_d)\ \Longrightarrow\ \frac{\pi}{2}E^2,\qquad E\sim\operatorname{Exp}(1).}
\]
In particular, the three-dimensional lower endpoint has quadratic probability growth with constant \(9\sqrt3/(2\pi)\), while its upper-tail constant is \(3\).

## Assumptions and scope
The Euclidean radii of every generating coordinate hyperdisk equal one; all disks have the same center, and \(\operatorname{conv}\) denotes convex **hull**, not Minkowski sum. The viewed direction is a single uniform unit vector, or equivalently an unoriented line. Width is the distance between opposite supporting hyperplanes perpendicular to that direction, not planar projected area. The law holds for every real \(w\), for all integers \(d\ge3\), with the interval cases specified above. In the endpoint asymptotics, \(d\) is fixed before \(\varepsilon\downarrow0\); the last limit separately takes \(d\to\infty\).

## Proof
**1. Support-function reduction.** For the unit Euclidean ball in \(\{x:x_j=0\}\), its support in direction \(u\in S^{d-1}\) is \(\sqrt{1-u_j^2}\), by orthogonal projection and Cauchy–Schwarz. The support of a convex hull of a union is the maximum of the supports. Since each generating ball is centrally symmetric, \(h_{H_d}(-u)=h_{H_d}(u)\). Therefore
\[
W_d(u)=2\max_j\sqrt{1-u_j^2}=2\sqrt{1-\min_j u_j^2}.
\]
The sphere condition \(\sum_j u_j^2=1\) implies \(0\le\min_j u_j^2\le1/d\), and both extremal values are realized. This proves the support identity and the exact width range.

**2. Exact three-dimensional law.** Put \(M=\min_{1\le j\le3}|U_j|\), and \(S(t)=\mathbb P(M\ge t)\) for \(0\le t\le1/\sqrt3\). For Haar-uniform \(U\in S^2\), the variable \(|U_1|\) is uniform on \([0,1]\), while, conditioned on \(|U_1|=s\), the other two coordinates have the representation \(\sqrt{1-s^2}(\cos\theta,\sin\theta)\) for a uniform \(\theta\in[0,2\pi)\). For \(s\le1/\sqrt3\), the fraction of such angles for which both remaining absolute coordinates are at least \(s\) is
\[
1-\frac4\pi\arcsin\left(\frac{s}{\sqrt{1-s^2}}\right).
\]
All three coordinates are exchangeable, so the disjoint first-crossing decomposition of the event \(\{M<t\}\) gives
\[
S'(t)=-3\left[1-\frac4\pi\arcsin\left(\frac{t}{\sqrt{1-t^2}}\right)\right]
\quad (0<t<1/\sqrt3),\qquad S(0)=1.
\]
A direct differentiation verifies
\[
\int_0^t\arcsin\left(\frac{s}{\sqrt{1-s^2}}\right)ds
=t\arcsin\left(\frac{t}{\sqrt{1-t^2}}\right)
+\arctan\sqrt{1-2t^2}-\frac\pi4.
\]
Integration yields the stated \(S(t)\); \(S(1/\sqrt3)=0\). Since \(W_3\le w\) is equivalent to \(M\ge\sqrt{1-w^2/4}\), this proves the full distribution including endpoint values.

**3. General-dimensional sharp lower endpoint.** Set \(Y_j=U_j^2\). By the standard Gaussian representation of Haar measure, \((Y_1,\ldots,Y_d)\) has the \(\operatorname{Dirichlet}(1/2,\ldots,1/2)\) distribution, with density relative to \(dy_1\cdots dy_{d-1}\):
\[
f(y)=\frac{\Gamma(d/2)}{\pi^{d/2}}\prod_{j=1}^d y_j^{-1/2},
\quad y_d=1-\sum_{j=1}^{d-1}y_j.
\]
For \(b_d=2\sqrt{1-1/d}\) and \(w=b_d+\varepsilon\), put
\[
\delta=\frac1d-\left(1-\frac{w^2}{4}\right)
=\sqrt{\frac{d-1}{d}}\,\varepsilon+\frac{\varepsilon^2}{4}.
\]
The event \(W_d\le w\) is the translated simplex \(Y_j\ge1/d-\delta\) for all \(j\). In the \(d-1\) independent coordinates its volume is exactly \((d\delta)^{d-1}/(d-1)!\). Its diameter shrinks to zero at \(y_j=1/d\), where the Dirichlet density is continuous and equals \(\Gamma(d/2)d^{d/2}/\pi^{d/2}\). Multiplying this density by the volume and inserting the exact \(\delta\) expansion gives the displayed lower constant. This is a full-dimensional local-volume argument, not an enumeration.

**4. General-dimensional sharp upper endpoint.** For \(w=2-\varepsilon\), define \(t=\sqrt{1-w^2/4}=\sqrt{\varepsilon-\varepsilon^2/4}\). The event \(W_d>w\) is \(\min_j|U_j|<t\). The marginal density of one coordinate at zero is \(c_d=\Gamma(d/2)/(\sqrt\pi\Gamma((d-1)/2))\); consequently \(\mathbb P(|U_1|<t)=2c_dt+o(t)\). For fixed \(d\ge3\), any two-coordinate joint marginal has at worst a locally integrable singularity at the origin (for \(d=3\), its density is proportional to \((1-x^2-y^2)^{-1/2}\), bounded near the origin). Hence intersections of two distinct coordinate-small events contribute \(O_d(t^2)=o(t)\). Finite inclusion–exclusion yields \(\mathbb P(W_d>w)=2dc_dt+o(t)\), and the second sharp constant follows.

**5. Large-dimensional law.** Let \(Z_1,\ldots,Z_d\) be independent standard Gaussians and \(U_j=Z_j/(\sum Z_i^2)^{1/2}\). As \(x\downarrow0\), \(\mathbb P(|Z_1|\le x)\sim\sqrt{2/\pi}\,x\); therefore
\[
\sqrt{\frac2\pi}\,d\min_j|Z_j|\ \Longrightarrow\ E\sim\operatorname{Exp}(1).
\]
Also \(\sum Z_j^2/d\to1\) in probability. Since \(2-2\sqrt{1-m^2}\sim m^2\) as \(m\to0\), continuous mapping and Slutsky's theorem give \(d^3(2-W_d)\Longrightarrow(\pi/2)E^2\).

## Verification
Run `python verify_width.py` with Python 3, NumPy, and SciPy. The checker compares the closed form with an independently integrated spherical-band formula at 81 interior points; verifies monotonicity and the three-dimensional sharp endpoint constants; numerically maximizes over 16,384 sampled points on each of the three generating disks for 30 independent directions; compares the law with 400,000 seeded Haar-sphere samples; and checks the predicted high-dimensional median scale at three dimensions. Its completed execution printed the three \(`*_CHECKS_PASSED`\) messages documented in `VERIFICATION.md`. These checks are finite/numerical and are not an infinite proof; the analytic argument above supplies the all-dimensional statements.

## Relationship to prior work
Chancelier and de Lara (2020) develop Euclidean top-\(k\) norms and their dual \(k\)-support balls; \(H_d\) is precisely the Euclidean \((d-1)\)-support unit ball. In particular, the identification of this convex body as a standard sparsity norm ball and the top-coordinate support identity are not claimed as new. Finch (2012) studies volume, area, and mean width of convex hulls of **two** orthogonal disks. A separately indexed geometric study of the convex hull of **three** mutually perpendicular disks calculates intrinsic volumes, boundary pieces, and Euclidean radii. General Dirichlet density and Gaussian extreme-order limits are also standard. The assessed contribution is the explicit three-disk **complete random width law** and its sharp endpoint expressions across dimensions, beyond previously catalogued deterministic mean widths or volume/radius invariants.

## Limitations
The exact elementary cumulative distribution is proved only in dimension three; a Dirichlet simplex integral gives an exact, generally non-elementary representation in every higher dimension. The fixed-dimensional edge laws and the limit in growing dimension are separate statements and not uniform estimates in the two parameters. Generators must be equal-radius centered unit Euclidean hyperdisks in coordinate hyperplanes; arbitrary radii, oblique planes, Minkowski sums, and planar shadow **areas** are not covered. A historical-equivalence risk remains from possible older treatments of symmetric \(\operatorname{Dirichlet}(1/2)\) minimum order statistics. No independent mathematical audit has been performed.

## References
1. Jean-Philippe Chancelier and Michel de Lara, *Orthant-Strictly Monotonic Norms, Generalized Top-k and k-Support Norms and the L0 Pseudonorm*, arXiv:2001.10441, first posted January 28, 2020; especially §3.1–3.2. https://arxiv.org/abs/2001.10441
2. Steven R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first posted November 19, 2012. https://arxiv.org/abs/1211.4514
3. Fulvio Gesmundo and Chiara Meroni, *The Geometry of Discotopes*, arXiv:2111.01241, first posted November 1, 2021. https://arxiv.org/abs/2111.01241 (studies Minkowski sums, distinct from convex hulls).
4. *Exact intrinsic volumes and boundary decomposition of the orthogonal three-disk hull*, public mathematical result indexed October 11, 2026; cited solely for its previously described intrinsic volumes, boundary and radii, not as a source for this width distribution.
5. The classical Gaussian-to-Dirichlet representation and one-dimensional Gaussian extreme-value law are used as standard probability facts.
