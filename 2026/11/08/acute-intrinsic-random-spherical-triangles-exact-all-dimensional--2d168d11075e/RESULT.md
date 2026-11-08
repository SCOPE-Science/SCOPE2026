# Acute intrinsic random spherical triangles: exact all-dimensional law and sharp convergence to one eighth

## Finding

Let \(d\ge3\) be an integer, and let \(X,Y,Z\) be independent uniform points on the unit sphere \(S^{d-1}\subset\mathbb R^d\). Except on null events, the shorter great-circle arcs form a nondegenerate spherical geodesic triangle. Let \(E_d\) mean that all three intrinsic angles, measured between the tangent vectors of these arcs, lie in \((0,\pi/2)\). Put
\[
c_n=\frac{\Gamma(n/2)}{\sqrt\pi\Gamma((n-1)/2)},\qquad
 g_d(u)=c_d(1+u^2)^{-d/2}\quad (u\ge0),
\]
and \(h_d(w)=c_{d-1}(1-w^2)^{(d-4)/2}\) for \(0<w<1\). Then the exact, absolutely convergent integral is
\[
\boxed{\mathbb P(E_d)=\frac18-2\int_0^\infty\!g_d(u)\int_0^1\!h_d(w)\int_0^{uw}\!g_d(v)\,dv\,dw\,du.}
\]
Equivalently the inner integral is \(\frac12 I_{u^2w^2/(1+u^2w^2)}(\frac12,\frac{d-1}2)\), making this an explicit two-dimensional integral. Always \(0<\mathbb P(E_d)<1/8\). Furthermore
\[
\boxed{\mathbb P(E_d)=\frac18-\frac{1}{\sqrt2\,\pi^{3/2}\sqrt d}+O(d^{-3/2})}\qquad(d\to\infty).
\]
For \(d\ge5\), writing \(\delta_d=1/8-\mathbb P(E_d)\) and \(L_d=2c_d^2c_{d-1}/(d-2)^2\), there are effective all-dimension bounds
\[
\boxed{L_d\left(1-\frac{2}{3(d-4)}\right)\le\delta_d\le L_d.}
\]

## Assumptions and scope

The ambient dimension \(d\) is an integer at least three. The points \(X,Y,Z\) are independent, each uniformly distributed on the unit sphere \(S^{d-1}\) by normalized surface measure. Every side means the shorter ambient great-circle arc, and each vertex angle means its *intrinsic Riemannian angle* in the tangent plane to the sphere. These are not the Euclidean angles of the straight-edge chord triangle in \(\mathbb R^d\). Antipodal pairs, coincidences, and tangentially degenerate configurations have probability zero.

## Proof

**1. Three scalar variables.** Fix \(X\) by rotational invariance and set \(a=X\cdot Y\), \(b=X\cdot Z\), \(c=Y\cdot Z\). The independent coordinates \(a,b\) have density \(c_d(1-t^2)^{(d-3)/2}\), \(-1<t<1\). The normalized tangent projections of \(Y\) and \(Z\) onto \(X^\perp\) are independent and uniform on \(S^{d-2}\); their inner product \(w\) is independent of \(a,b\) and has density \(c_{d-1}(1-w^2)^{(d-4)/2}\) on \((-1,1)\). Thus
\[
c=ab+\sqrt{1-a^2}\sqrt{1-b^2}\,w.
\]

**2. Characterization of the acute event.** The angle at \(X\) is acute precisely when \(c>ab\), equivalently \(w>0\). At \(Y\) and \(Z\) the respective acute-angle inequalities are \(b>ac\) and \(a>bc\). These three inequalities force \(a,b>0\): if \(a>0>b\), then \(b>ac\) implies \(c<b/a<ab\), contradicting \(c>ab\); the other opposite-sign case is symmetric. If \(a,b<0\), the first inequality implies \(c>ab>0\), while the last two imply \(|b|<|a|c\) and \(|a|<|b|c\), giving \(1<c^2<1\), impossible. Boundary cases are null. Conversely, when \(a,b>0\), put
\[
u=\frac{a}{\sqrt{1-a^2}},\qquad v=\frac{b}{\sqrt{1-b^2}}.
\]
Then the three inequalities are exactly \(0<w<\min(u/v,v/u)\).

**3. Exact integral.** The variables \(u,v\) have independent positive-side densities \(g_d(s)=c_d(1+s^2)^{-d/2}\) on \((0,\infty)\), each with total mass \(1/2\). The variable \(w\) likewise has positive-side density \(h_d\) of mass \(1/2\). Hence the region \(u,v,w>0\) has mass \(1/8\). Its rejected subset is \(w>\min(u/v,v/u)\). By symmetry in \(u,v\), this is twice the region \(0<v<uw\) (when \(u\ge v\)); the latter inequality with \(w<1\) already implies \(u>v\). Integrating proves the displayed formula. The incomplete-beta reduction follows from substituting \(z=v^2/(1+v^2)\). The omitted region has strictly positive but strictly smaller mass than \(1/8\), proving the strict bounds.

**4. Uniform high-dimensional estimate.** For \(d\ge5\), define \(U_+\) and \(W_+\) as positive-side random variables with *unnormalized* densities \(g_d\) and \(h_d\), respectively; an expectation of their product denotes the corresponding product integral, not a conditional probability. The elementary inequality \(0\le1-(1+t^2)^{-d/2}\le dt^2/2\) yields, for every \(z\ge0\),
\[
0\le c_d z-\int_0^z g_d(v)\,dv\le \frac{dc_d}{6}z^3.
\]
The exact one-sided moments are
\[
\begin{aligned}
\int_0^\infty u g_d(u)\,du&=\frac{c_d}{d-2}, &
\int_0^1w h_d(w)\,dw&=\frac{c_{d-1}}{d-2},\\
\int_0^\infty u^3g_d(u)\,du&=\frac{2c_d}{(d-2)(d-4)},&
\int_0^1 w^3h_d(w)\,dw&=\frac{2c_{d-1}}{d(d-2)}.
\end{aligned}
\]
They follow by elementary beta integrations. Substitute \(z=uw\) into the exact defect integral. The leading integral is
\[
2c_d\frac{c_d}{d-2}\frac{c_{d-1}}{d-2}=L_d.
\]
The upper bound on its error is exactly
\[
\frac{dc_d}{3}\cdot\frac{2c_d}{(d-2)(d-4)}\cdot\frac{2c_{d-1}}{d(d-2)}
=\frac{2L_d}{3(d-4)}.
\]
This proves the explicit two-sided inequalities. Stirling's gamma-ratio formula gives \(c_d=\sqrt{d/(2\pi)}(1+O(d^{-1}))\) and \(c_{d-1}=\sqrt{d/(2\pi)}(1+O(d^{-1}))\). Therefore \(L_d=1/(\sqrt2\pi^{3/2}\sqrt d)+O(d^{-3/2})\); the finite-dimensional error bound is itself \(O(d^{-3/2})\), proving the sharp claimed expansion.

## Verification

The standalone script `acute_dimension_check.py` numerically evaluates the exact integral using an independently implemented regularized-incomplete-beta reduction and performs a direct vector-sampling test of all three intrinsic tangent-dot-product inequalities. It compares the \(d=3\) value against the classical \(1/(2\pi)-1/8\) and compares several higher-dimensional values with Monte Carlo. The proof above does not rely on simulation. Approximate values include \(p_3=0.03415494309\), \(p_5=0.06068076694\), \(p_{16}=0.09204765693\), and \(p_{128}=0.11372439115\). For \(d=256\), the scaled defect is about \(0.127277\), close to its limit \(1/(\sqrt2\pi^{3/2})\approx0.12698727\). Checkable gamma-moment identities and a uniform error inequality constitute the analytic certificate.

## Relationship to prior work

Finch and Jones, *Random Spherical Triangles* (arXiv:1009.5329; first public 2010-09-27), treat the classical two-sphere and focus on spherical area/perimeter distributions, not an arbitrary-ambient-dimension acute-triangle law. Cai, Fan, and Jiang, *Distributions of Angles in Random Packing on Spheres* (arXiv:1306.0256; first public 2013-06-02), study the angles between radial position vectors as the number of sampled points increases, rather than intrinsic vertex angles of a fixed triangle. The known two-sphere acute probability \(1/(2\pi)-1/8\) is **not claimed as new**. The claimed contribution is the all-dimensional exact conditional integral together with its nonzero sharp first-order high-dimensional correction and effective bounds.

## Limitations

The event uses intrinsic shorter-geodesic angles, not chord-triangle angles; mixing these leads to different probabilities. Strict monotonicity of the acute probability in dimension is not claimed. The finite-dimensional integral need not simplify to elementary functions. The literature comparison is necessarily incomplete: specialized older works could conceivably contain an equivalent joint-angle formula. Independent mathematical and historical review has not been performed.

## References

1. Steven R. Finch and Antonia J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, initially public 2010-09-27, https://arxiv.org/abs/1009.5329.
2. Tony Cai, Jianqing Fan, and Tiefeng Jiang, *Distributions of Angles in Random Packing on Spheres*, arXiv:1306.0256, initially public 2013-06-02, https://arxiv.org/abs/1306.0256. Full published text: https://fan.princeton.edu/document/626.
