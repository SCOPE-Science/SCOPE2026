# Sharp fixed-area first-order width regularization by an asymmetric triangular corner cut

## Finding

For a compact convex planar body \(K\), let \(W_K(u)\) be the length of its orthogonal projection on a line of uniformly random unoriented direction \(u\), and define the coefficient of variation
\[
\delta(K)=\frac{\sqrt{\mathbb E W_K^2-(\mathbb E W_K)^2}}{\mathbb E W_K}.
\]
Let \(T\) be the unit-side equilateral triangle, and truncate one vertex at fractions \(s,t\) of its two incident side lengths. Set \(s=\varepsilon\sqrt r\), \(t=\varepsilon/\sqrt r\), where \(r>0\) is *fixed* and \(\varepsilon\downarrow0\); the removed area is exactly \(\sqrt3\varepsilon^2/4\). Then
\[
\delta(T_{\varepsilon,r})=\delta_0-C(r)\varepsilon+O_r(\varepsilon^2),
\qquad
\delta_0=\sqrt{\frac{\pi(2\pi+3\sqrt3)}{36}-1}.
\]
The positive first-order decrease \(C(r)\) is maximized **at precisely two reciprocal ratios** \(r=r_*\) and \(r=r_*^{-1}\), where
\[
 r_*=\frac{\sin(2\pi/3-\theta_*)}{\sin\theta_*}
 \approx2.28062656213330,
 \qquad \theta_*\approx0.452676127273466.
\]
Here \(\theta_*\) is the unique solution in \((0,\pi/6)\) of the following explicit equation, with \(L=\pi/3\), \(A=2L+\sqrt3\), and \(Q(\theta)=A(1-\cos\theta)+\theta\cos\theta-(1+\sqrt3\theta)\sin\theta\):
\[
 2Q'(\theta)\sin\theta\sin(2L-\theta)
 =Q(\theta)\sin(2L-2\theta).
\]
The sharp leading decrease coefficient, measured per \(\sqrt{st}\), is
\[
 C_* =\frac{\kappa_0}{3\delta_0}\,
 \frac{\sqrt3\,Q(\theta_*)}{2A\sqrt{\sin\theta_*\sin(2L-\theta_*)}}
 \approx0.033215170664713,
 \qquad \kappa_0=\frac{\pi A}{12}.
\]
The optimum is genuinely asymmetric: the equal-arm corner cut has zero first-order benefit. Up to the dihedral symmetries of the triangle, all six placements (three vertices, two arm orderings) are equivalent. This is a sharp *fixed-ratio first-order* theorem; it makes no uniform remainder claim when \(r\) varies with \(\varepsilon\).

## Assumptions and scope

Take \(T=\operatorname{conv}\{(0,0),(1,0),(1/2,\sqrt3/2)\}\). Cut the origin by the segment joining \((s,0)\) and \((t/2,\sqrt3t/2)\), and retain the resulting convex quadrilateral. All asymptotics hold for each fixed \(r\in(0,\infty)\), for sufficiently small \(\varepsilon>0\) so that \(0<s,t<1\). The area normalization is exact and does not mean that the two cut lengths are equal. All projections use Haar-uniform direction on the circle, so the coefficient is invariant under reflection and rotation.

## Proof

**1. First variation.** Write the oriented unit triangle edges as \(c\), \(a\), \(b\) in cyclic order, with successive angles separated by \(2\pi/3\). For a vector \(v\) of argument \(\varphi\), write \(X_v(\omega)=|v|\max\{\sin(\varphi-\omega),0\}\), where \(\omega\) is uniform on \([0,2\pi)\). Then \(W_T=X_a+X_b+X_c\). The cut replaces the two shortened edges by the chord \(e=sc+tb\), and hence **exactly**
\[
 W_{T_{s,t}}=W_T-sX_c-tX_b+X_e.
\]
Linearity in positive vector scaling is understood as \(X_{sv}=sX_v\). For oriented vectors with smaller angular difference \(\phi\in[0,\pi]\), direct integration of positive sine halves gives
\[
 \mathbb E X_v=\frac{|v|}{\pi},\qquad
 \mathbb E(X_vX_w)=\frac{|v||w|}{4\pi}V(\phi),
 \quad V(\phi)=(\pi-\phi)\cos\phi+\sin\phi.
\]
In particular, \(\mathbb EW_T=3/\pi\), \(\mathbb EW_T^2=3A/(4\pi)\), and \(\kappa_0:=\mathbb EW_T^2/(\mathbb EW_T)^2=\pi A/12\). Let \(\theta\in[0,2\pi/3]\) be the unsigned angle of \(e\) away from \(c\) toward \(b\), and \(\ell=|e|=\sqrt{s^2+t^2-st}\). In the fundamental sector \(0\le\theta\le L\), direct substitution into the three correlations yields
\[
 \frac{\mathbb E(W_TX_e)}{\mathbb EW_T^2}
   =\frac{\ell}{3A}\{(A-\theta)\cos\theta+(1+\sqrt3\theta)\sin\theta\}
   =\frac\ell3\left(1-\frac{Q(\theta)}A\right).
\]
The two original edge directions have the corresponding ratio \(1/3\). Therefore, expanding the quotient defining \(\kappa=1+\delta^2\) for fixed \(r\),
\[
 \kappa(T_{\varepsilon,r})=\kappa_0
 \left(1-\frac{2\ell Q(\theta)}{3A}+O_r(\varepsilon^2)\right),
 \qquad
 \delta(T_{\varepsilon,r})=\delta_0-
 \frac{\kappa_0\ell Q(\theta)}{3\delta_0 A}+O_r(\varepsilon^2).
\]
The sine rule applied to the triangle of vectors \(sc,tb,e\) gives
\[
 \frac{s}{t}=\frac{\sin(2L-\theta)}{\sin\theta},\qquad
 \frac{\ell}{\sqrt{st}}=\frac{\sqrt3}{2\sqrt{\sin\theta\sin(2L-\theta)}}.
\]
Thus \(C(r)=\kappa_0G(\theta)/(3\delta_0)\), where
\[
 G(\theta)=\frac{\sqrt3\,Q(\theta)}{2A\sqrt{\sin\theta\sin(2L-\theta)}}.
\]
The other half-sector is the reflected image and gives \(C(r)=C(1/r)\).

**2. Positivity and reduction to half a sector.** Let \(c=L/2=\pi/6\) and \(x=\theta-c\). A trigonometric identity gives
\[
 Q(c+x)=A-(2+\sqrt3L)\cos x-2x\sin x.
\]
This is even in \(x\), with \(Q(0)=Q(L)=0\). For \(0<x<c\), writing \(f(x)=x\cos x-\sqrt3c\sin x\) gives
\[
 Q(c+x)=2\int_x^c f(u)\,du>0,
\]
because \(u\cot u\) is strictly decreasing and \(c\cot c=\sqrt3c\). Hence \(Q>0\) throughout \((0,L)\). For \(0<\theta<c\), comparison of the denominator at \(\theta\) and \(L-\theta\) gives
\[
 \sin\theta\sin(2L-\theta)-\sin(L-\theta)\sin(L+\theta)
 =\tfrac12\{\cos(2L-2\theta)-\cos(2\theta)\}<0.
\]
As \(Q(\theta)=Q(L-\theta)\), it follows that \(G(\theta)>G(L-\theta)\). Every global maximizer therefore belongs to \((0,c)\).

**3. Strict uniqueness, with a finite analytic sign certificate.** Set \(D(\theta)=\sin\theta\sin(2L-\theta)\) and
\[
 F(\theta)=2Q'(\theta)D(\theta)-Q(\theta)\sin(2L-2\theta).
\]
The sign of \(G'\) is the sign of \(F\). The quotient \(F(\theta)/\theta^2\) is strictly decreasing on \((0,c]\). Here is a reproducible, **all-real-angles** proof of that assertion, not a sampling argument. Trigonometric expansion gives
\[
\begin{aligned}
F(\theta)={}&-\tfrac52\theta\sin\theta-\tfrac{\sqrt3}{2}\theta\cos\theta
+\tfrac{2\pi}{3}\sin\theta
-(\tfrac{2\pi}{3}+\sqrt3)\sin(2\theta+\tfrac\pi3)\\
&+\sin(3\theta+\tfrac\pi6)
+(1+\tfrac{\sqrt3\pi}{3})\cos\theta.
\end{aligned}
\]
Put \(H(\theta)=\theta F'(\theta)-2F(\theta)\), so that \((F/\theta^2)'=H/\theta^3\). The coefficients of degrees \(0,1,2\) in its Maclaurin expansion vanish. Its coefficients of degrees \(3,\dots,9\) in order are
\[
\begin{aligned}
 h_3&=(\pi-4\sqrt3)/3,&
 h_4&=55/24-5\sqrt3\pi/12,\\
 h_5&=-\pi/4+103\sqrt3/40,&
 h_6&=-569/360+7\sqrt3\pi/60,\\
 h_7&=-57\sqrt3/56+\pi/24,&
 h_8&=389/896-17\sqrt3\pi/1344,\\
 h_9&=-17\pi/5184+9581\sqrt3/51840.
\end{aligned}
\]
The elementary rational bounds \(157/50<\pi<22/7\), \(173/100<\sqrt3<7/4\) imply
\[
 h_3<-5/4,\quad h_4<1/20,\quad h_5<15/4,\quad
 h_6,h_7<0,\quad h_8<1/2,\quad h_9<1/3.
\]
On \(0\le\theta\le c<11/21\), differentiating the displayed trigonometric formula bounds \(|F^{(10)}|<64000\) and \(|F^{(11)}|<186000\) (the largest trigonometric frequency is \(3\), and derivatives of \(\theta\sin\theta\) or \(\theta\cos\theta\) have absolute value at most \(\theta+m\) in order \(m\)). Hence \(|H^{(10)}|=|\theta F^{(11)}+8F^{(10)}|<10^6\). Taylor's theorem, including its uniform remainder, now proves for **every** \(0<\theta\le c\) that
\[
\begin{aligned}
\frac{H(\theta)}{\theta^3}
&<-\frac54+\frac\theta{20}+\frac{15\theta^2}{4}
  +\frac{\theta^5}{2}+\frac{\theta^6}{3}
  +\frac{10^6\theta^7}{10!}\\
&\le-\frac54+\frac{11/21}{20}+\frac{15(11/21)^2}{4}
  +\frac{(11/21)^5}{2}+\frac{(11/21)^6}{3}
  +\frac{10^6(11/21)^7}{10!}< -0.16<0.
\end{aligned}
\]
Consequently \(F/\theta^2\) is strictly decreasing on \((0,c]\). Its left-end limit is \(\sqrt3\pi/2-9/4>0\), while \(F(c)=-Q(c)\sin L<0\) because \(Q(c)=(2-\sqrt3)(L-1)>0\) and \(Q'(c)=0\). There is exactly one zero \(\theta_*\in(0,c)\). It is the unique maximum in the left half-sector, and the strict reflection comparison makes it the unique maximum in the full fundamental sector. The reciprocal ratios result from the two orientations of the cap, completing the proof.

## Verification

Run `python verify.py` with Python 3 and SymPy. It checks the exact trigonometric identity, all seven Taylor coefficients, all rational sign inequalities, the uniform tenth-derivative remainder bound, the endpoint equations, root bracketing, and four independent direct quadratures of the widths of the actual truncated quadrilateral. The Taylor-and-remainder proof, not the numerical quadratures or the root approximation, certifies the continuum of angles. The script printed `PASS` on the included source.

## Relationship to prior work

Akiyama and Kamae (arXiv:2201.06736, first submitted January 18, 2022) established that any sufficiently small **nonparallel** one-corner truncation decreases the width-deviation statistic, whereas a parallel corner truncation increases it. Their Section 6 gives the edge-correlation mechanism and first-variation sign but does not compare different cut-arm ratios at *equal removed area*, determine a globally optimal asymmetry, or prove uniqueness of that orientation. The result here sharpens their qualitative local perturbation statement along a natural equal-area family. It does not conflict with their minimum-deviation theorems for polygons or with existing local results for a perturbed square, whose base polygon and moduli are different.

## Limitations

The claimed optimality concerns the coefficient of \(\varepsilon\) for **fixed positive cut-arm ratio** \(r\). It does not claim finite-size optimality, a uniform second-order remainder as \(r\to0\) or \(r\to\infty\), or optimality among arbitrary simultaneous multi-corner deformations. The analytic root has been approximated numerically only to provide orientation and efficiency values; exact uniqueness does not rely on that approximation. Unindexed literature or equivalent earlier optimization calculations could affect priority.

## References

1. Shigeki Akiyama and Teturo Kamae, *Width deviation of convex polygons*, arXiv:2201.06736, version 1, public January 18, 2022. Full text: https://arxiv.org/html/2201.06736v1 . See Section 6, Lemmas 3 and 6 and Theorem 8.
2. Shigeki Akiyama and Teturo Kamae, *Width Deviation of Convex Polygons*, *Discrete & Computational Geometry* **71** (2024), 1403–1428, DOI:10.1007/s00454-023-00545-6 (later journal form of reference 1; not a different first-public source).
