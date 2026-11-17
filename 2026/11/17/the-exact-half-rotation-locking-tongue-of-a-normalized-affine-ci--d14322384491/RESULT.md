# The exact half-rotation locking tongue of a normalized affine circle map

## Finding
For \(0<\alpha<1\), \(\theta\in\mathbb R/(2\pi\mathbb Z)\) and \(z\in\mathbb S^1\), define the analytic orientation-preserving circle diffeomorphism
\[
F_{\alpha,\theta}(z)=\frac{e^{i\theta}z+\alpha}{|e^{i\theta}z+\alpha|}.
\]
Set
\[
q=1-\alpha^2,\qquad \delta_*(\alpha)=\arcsin\frac{1-\sqrt q}{2},
\]
and let \(d_{\mathbb S^1}(\theta,\pi)\in[0,\pi]\) be angular distance modulo \(2\pi\). The **number of distinct orbits of least period two** is exactly
\[
N_2(\alpha,\theta)=\begin{cases}
2&d_{\mathbb S^1}(\theta,\pi)<\delta_*(\alpha),\\
1&d_{\mathbb S^1}(\theta,\pi)=\delta_*(\alpha),\\
0&d_{\mathbb S^1}(\theta,\pi)>\delta_*(\alpha).
\end{cases}
\]
Inside the strict tongue one orbit is attracting and the other repelling. At either boundary the sole period-two orbit is neutral, with two-step angular multiplier exactly \(1\). This gives the exact full angular width
\[
2\delta_*(\alpha)=\frac{\alpha^2}{2}+\frac{\alpha^4}{8}+O(\alpha^6)
\quad(\alpha\downarrow0),
\]
with limit \(\pi/3\) as \(\alpha\uparrow1\).

For a noncentral angle \(\theta\ne\pi\) in the tongue, write \(c=\cos\theta<0\). The two orbits correspond to positive roots \(P_-\le P_+\) of
\[
Q(P)=P^2+(2+\alpha^2-4c^2)P+q=0,
\]
where equality holds only at the tongue boundary. Their exact two-step multipliers are
\[
\mu(P)=1+\frac{(q-P^2)(q+3P)}{4P^3};
\]
for the strict interior \(\mu(P_+)<1<\mu(P_-)\). At the center \(\theta=\pi\), the repelling orbit \(\{1,-1\}\) has multiplier \(q^{-1}\), and the attracting orbit \(\{\alpha/2\pm i\sqrt{1-\alpha^2/4}\}\) has multiplier \((1-\alpha^2/2)^2\).

## Assumptions and scope
The translation vector can be rotated to the positive real axis: complex multiplication by a unit vector conjugates any planar rotation plus nonzero translation of norm \(\alpha\) to this formula. We require \(0<\alpha<1\); it ensures the denominator never vanishes on the unit circle and the induced map is a smooth orientation-preserving diffeomorphism. The count includes only genuine period-two orbits, not fixed points, and counts an unordered pair \(\{z,F(z)\}\) once. The angular multiplier means the derivative of the second iterate in a positively oriented angular coordinate.

## Proof
Write \(\rho=e^{i\theta}\), \(c=\cos\theta\). Suppose \(z,w\in\mathbb S^1\) are a genuine two-cycle. Put \(t=|\rho z+\alpha|>0\) and \(u=|\rho w+\alpha|>0\). The cycle equations are
\[
tw=\rho z+\alpha,\qquad uz=\rho w+\alpha.
\]
First suppose \(\rho\ne-1\). Eliminating gives, with \(P=tu\),
\[
z=\frac{\alpha(t+\rho)}{P-\rho^2},\qquad
w=\frac{\alpha(u+\rho)}{P-\rho^2}.
\]
The denominator cannot vanish for \(\rho\ne\pm1\) (because \(P>0\)); for \(\rho=1\), if \(P=1\) both numerator equations would force \(0=\alpha(t+1)\), impossible. Thus it is nonzero for any actual cycle considered here. From \(|z|=|w|=1\),
\[
(t-u)(t+u+2c)=0.
\]
If \(t=u\), the displayed expressions force \(z=w\), which contradicts primitiveness. Therefore
\[
t+u=-2c>0,\quad c<0,\quad 0<P=tu\le c^2.
\]
The relation \(t^2+2ct=-P\) shows \(|t+\rho|^2=1-P\). The unit-norm equation hence reduces exactly to
\[
|P-\rho^2|^2=\alpha^2(1-P),
\]
which, on expanding \(\cos(2\theta)=2c^2-1\), is \(Q(P)=0\).

Conversely, fix \(c<0\) and any root \(P\) of \(Q\) in \((0,c^2)\). Put
\[
t=-c+\sqrt{c^2-P},\qquad u=-c-\sqrt{c^2-P}
\]
and reconstruct \(z,w\) using the displayed fractions. Both \(t,u\) are strictly positive; the quadratic identity gives \(|z|=|w|=1\). Direct substitution yields \(tw=\rho z+\alpha\), \(uz=\rho w+\alpha\). As \(t\ne u\), this is a primitive two-cycle. Interchanging \(t,u\) only interchanges its two points. If \(P=c^2\), the construction has \(t=u\), and would force a fixed point, not a primitive cycle; this possibility is excluded because, for \(|c|<1\),
\[
Q(c^2)=(1-c^2)(3c^2+q)>0.
\]
For \(\theta=0\), \(c>0\) already excludes primitive cycles. For \(\theta=\pi\), solve separately below.

The discriminant of \(Q\) is
\[
\Delta=(2+\alpha^2-4c^2)^2-4q.
\]
Since \(Q(c^2)>0\) and \(Q'(c^2)=3-q-2c^2>0\), the evaluation point \(c^2\) lies strictly to the right of the vertex. For \(c<0\), two roots are positive and in \((0,c^2)\) precisely when
\[
4c^2>2+\alpha^2+2\sqrt q=4-(1-\sqrt q)^2.
\]
At equality the roots coincide at \(P=\sqrt q\), which is still below \(c^2\); the converse construction yields one primitive orbit. With the reversed inequality there is no admissible root. This condition is equivalent to \(d_{\mathbb S^1}(\theta,\pi)<\arcsin((1-\sqrt q)/2)\), with equality giving the neutral boundary. To see completeness of the discriminant criterion, note the alternative discriminant branch \(4c^2\le 2+\alpha^2-2\sqrt q=(1-\sqrt q)^2\) has nonpositive root sum, so no positive roots.

For a point with forward normalization modulus \(t\), the angular derivative is
\[
F'_{\alpha,\theta}=\frac{t^2+q}{2t^2}>0.
\]
Thus for a cycle with \(P=tu\),
\[
\mu=\frac{(t^2+q)(u^2+q)}{4P^2}.
\]
Using \(t+u=-2c\), eliminating \(c^2\) with \(Q(P)=0\), and simplifying gives the exact factorization
\[
\mu-1=\frac{(q-P^2)(q+3P)}{4P^3}.
\]
The two distinct positive roots satisfy \(P_-P_+=q\), and hence \(P_-<\sqrt q<P_+\). Therefore the larger root yields an attracting orbit and the smaller root a repelling one. At the double root \(P=\sqrt q\) the multiplier is one.

Finally, at \(\theta=\pi\), \(F(z)=(\alpha-z)/|\alpha-z|\). It directly exchanges \(1,-1\), and also exchanges the two unit complex numbers \(z_\pm=\alpha/2\pm i\sqrt{1-\alpha^2/4}\), since \(|\alpha-z_\pm|=1\) and \(\alpha-z_\pm=z_\mp\). Exhaustiveness follows either by splitting the cycle equations into the cases \(t=u\) and \(t\ne u\), or by observing directly that a period-two point has either \(|\alpha-z|=1\) or \(z=\pm1\). Their multipliers, from the derivative formula, are respectively \((1-\alpha^2/2)^2\) and \((1-\alpha^2)^{-1}\). The angular width expansion follows by Taylor expansion of \(\sqrt{1-\alpha^2}\) and \(\arcsin\).

## Verification
The included standalone `verify.py` checks the key polynomial and multiplier identities symbolically using SymPy, evaluates the exact central and boundary cases, and reconstructs genuine two-cycles numerically at several interior angles. Run `python verify.py` from the extracted directory with SymPy and Python 3. The exact symbolic identities and algebraic proof establish all-parameter validity; finite numerical tests are diagnostic only.

## Relationship to prior work
Choudhuri, Faraco and Yadav [1] introduced this normalized affine rotation circle map in their setting and proved in their Proposition 7 that two distinct period-two orbits exist for a neighbourhood of the half-turn, along with a separate nonexistence region. Their Corollary 9 analyzes the exact half-turn. This theorem extends those **local and endpoint facts** to an exhaustive, sharp half-turn interval, including both boundaries and exact multipliers. Shah and Yadav [2, Theorem 7 and Remark 9] already obtained existence and the four-periodic-point phenomenon near the half-turn; those statements are not claimed as new. The present exact boundary formula and classification do not follow as stated from their local-neighbourhood existence result. General circle mode-locking theory motivates, but does not supply, the explicit formula for this normalized affine map. A distinct normalized affine sphere-map stationary-measure transition concerns a different higher-dimensional negative-axisymmetric family and does not imply this angular two-cycle count.

## Limitations
The result is for planar rigid rotations plus a nonzero translation with norm strictly below one. It does not count or classify prime periods greater than two, rotation numbers throughout the family, or global attraction basins. The boundary cycle has derivative one; no further higher-order classification of its parabolic drift is asserted. The complete text of the earlier 2016 preprint [2] and the 2022 preprint [1] was inspected; a 2022 published erratum to [2] was identified, but its full text was not available for comparison. Independent review and literature-priority determination remain outstanding.

## References
1. M. Choudhuri, G. Faraco, A. K. Yadav, *On the distality and expansivity of certain maps on spheres*, arXiv:2209.05236v1 (public 12 September 2022); *Dynamical Systems* 39 (2024), 166–181, doi:10.1080/14689367.2023.2248013. See Proposition 7 and Corollary 9. https://arxiv.org/abs/2209.05236
2. R. Shah, A. K. Yadav, *Dynamics of Certain Distal Actions on Spheres*, arXiv:1606.08797 (28 June 2016); *Real Analysis Exchange* 44 (2019), 77–88. See Theorem 7 and Remark 9. https://arxiv.org/abs/1606.08797
3. R. Shah, A. K. Yadav, *Errata: Dynamics of Certain Distal Actions on Spheres*, *Real Analysis Exchange* 47 (2022), 467–468, doi:10.14321/realanalexch.47.2.1654759107 (full text not inspected).
