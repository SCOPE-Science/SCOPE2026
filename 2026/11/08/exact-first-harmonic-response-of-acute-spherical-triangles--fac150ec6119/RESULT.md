# Exact first-harmonic response of acute spherical triangles

## Finding

Let \(\sigma\) be normalized area on the unit two-sphere \(S^2\), let \(X,Y,Z\) be independent with law \(\sigma\), and let \(E\) be the event that the three interior angles of the geodesic triangle with the *shorter* great-circle arcs between these points are all strictly acute. The exact cosine-weighted moment is

\[
\mathbb E_\sigma[\mathbf1_E(X\cdot Y)]=\frac{\pi-2}{64}.
\]

The uniform acute probability is the **previously known** value \(p_0=1/(2\pi)-1/8\). Consequently the newly evaluated conditional pair cosine is

\[
\mathbb E_\sigma[X\cdot Y\mid E]=\frac{\pi(\pi-2)}{8(4-\pi)}.
\]

For any unit axis \(u\in S^2\) and any \(-1\le\varepsilon\le1\), define the dipole probability measure \(d\sigma_{\varepsilon,u}(x)=(1+\varepsilon u\cdot x)\,d\sigma(x)\). For *three independent* points with this same nonuniform law, the complete, non-asymptotic acute probability is

\[
\boxed{\mathbb P_{\varepsilon,u}(E)=\frac1{2\pi}-\frac18+\frac{\pi-2}{64}\varepsilon^2.}
\]

Thus its minimum within the dipole family is uniquely attained at \(\varepsilon=0\). For the von Mises–Fisher density \(f_{\kappa,u}(x)=(\kappa/\sinh\kappa)e^{\kappa u\cdot x}\) relative to \(\sigma\), with its continuous value at \(\kappa=0\), two distinct sampling conventions obey

\[
\mathbb P_{\mathrm{three\ iid}}(E)=p_0+\frac{\pi-2}{64}\kappa^2+O(\kappa^4),
\]
\[
\mathbb P_{\mathrm{pinned}}(E)=p_0+\frac{\pi-2}{32}\kappa+O(\kappa^2),
\]

where “pinned” means the first vertex equals \(u\) and only the other two are independent von Mises–Fisher samples. In particular the pinned model has a strictly positive *exact initial slope*, not merely a numerically observed increase.

## Assumptions and scope

All angles are **intrinsic spherical interior angles** determined by the minor arcs; they are not the three central angular distances between pairs of points. Degenerate, right-angled, and antipodal configurations have \(\sigma^3\)-measure zero. The dipole formula holds for every real \(\varepsilon\) in the full positivity interval \([-1,1]\), with no small-parameter hypothesis. Both von Mises–Fisher formulas are local statements as real \(\kappa\to0\), not global monotonicity statements. The event \(E\) and its probability are unchanged by common rotations or common antipodal reflection.

## Proof

**1. Condition on a side.** The spherical separation \(d=\arccos(X\cdot Y)\) has density \(\frac12\sin d\) on \((0,\pi)\). Rotational invariance permits the coordinates

\[
X=(c,-s,0),\quad Y=(c,s,0),\quad c=\cos(d/2),\quad s=\sin(d/2),
\]
\[
Z=(\cos\lambda\cos t,\cos\lambda\sin t,\sin\lambda),
\quad-\pi/2<\lambda<\pi/2,\quad-\pi<t<\pi.
\]

The conditional surface element for \(Z\) is \(\cos\lambda\,d\lambda\,dt/(4\pi)\). At \(X\) the interior angle is acute precisely when \((Y-\cos d\,X)\cdot Z>0\), and similarly at \(Y\). These two inequalities give \(|t|<d/2\). The angle at \(Z\) is acute precisely when

\[
\cos d>\cos^2\lambda\bigl(\cos^2t-\sin^2(d/2)\bigr).
\]

Within the wedge \(|t|<d/2\), this is impossible for \(d\ge\pi/2\): the factor in parentheses is at least \(\cos d\), and multiplying it by \(\cos^2\lambda\in[0,1]\) cannot make it smaller than the nonpositive \(\cos d\). For \(0<d<\pi/2\), the admissible latitude is characterized by

\[
|\sin\lambda|>
\sqrt{\frac{\sin^2(d/2)-\sin^2t}{\cos^2t-\sin^2(d/2)}}.
\]

After integrating the latitude and using evenness in \(t\), the conditional acute probability is exactly

\[
A(d)=\frac1\pi\int_0^{d/2}
\left(1-\sqrt{\frac{\sin^2(d/2)-\sin^2t}{\cos^2t-\sin^2(d/2)}}\right)dt
\quad(0<d<\pi/2),
\]

and \(A(d)=0\) for \(\pi/2\le d<\pi\). Therefore, for \(j\in\{0,1\}\),

\[
M_j=\mathbb E_\sigma[\mathbf1_E(X\cdot Y)^j]
=\frac12\int_0^{\pi/2}\sin d\,(\cos d)^j A(d)\,dd.
\]

Here \(M_0=p_0\) and \(M_1\) is the desired moment. These are exact integrals, not sampling estimates.

**2. Evaluate both moments.** Split the integrand of \(A(d)\) into its leading \(1\) and subtractive square-root terms. The leading contributions to \((M_0,M_1)\) are \((1/(4\pi),1/32)\). In the subtracted term set \(x=\sin(d/2)\), interchange the \(x\) and \(t\) integrations, and use \(y=\sin t\). At fixed \(t\in[0,\pi/4]\), the inner integrals are

\[
J_j(t)=\int_{\sin t}^{1/\sqrt2}
 x(1-2x^2)^j\sqrt{\frac{x^2-\sin^2t}{1-x^2-\sin^2t}}\,dx.
\]

Writing \(k=1-2\sin^2t=\cos2t\) and substituting \(x^2=\sin^2t+k\sin^2\phi\), \(0\le\phi\le\pi/4\), yields

\[
J_0(t)=k\left(\frac\pi8-\frac14\right),\qquad
J_1(t)=k^2\left(\frac14-\frac\pi{16}\right).
\]

The subtracted contributions are \((2/\pi)\int_0^{\pi/4}J_j(t)dt\). Using \(\int_0^{\pi/4}\cos2t\,dt=1/2\) and \(\int_0^{\pi/4}\cos^22t\,dt=\pi/8\), the two subtractions are respectively \(1/8-1/(4\pi)\) and \((4-\pi)/64\). Thus

\[
M_0=\frac1{2\pi}-\frac18,\qquad M_1=\frac1{32}-\frac{4-\pi}{64}=\frac{\pi-2}{64}.
\]

The first value is a known baseline; the second is the focal weighted result.

**3. Derive the exact dipole law.** Expand

\[
\mathbb P_{\varepsilon,u}(E)=\mathbb E_\sigma\left[\mathbf1_E
\prod_{T\in\{X,Y,Z\}}(1+\varepsilon u\cdot T)\right].
\]

All odd-degree terms vanish because the common antipodal reflection preserves \(E\) and reverses each linear factor. For any pair, rotational invariance of the rank-two tensor gives

\[
\mathbb E_\sigma[\mathbf1_E(u\cdot X)(u\cdot Y)]
=\frac13\mathbb E_\sigma[\mathbf1_E(X\cdot Y)]=M_1/3.
\]

There are three pairs. No higher-degree terms exist in the three-factor product, proving \(p_0+M_1\varepsilon^2\) **for every** \(|\varepsilon|\le1\). Positivity of \(M_1\) proves the unique minimum.

**4. Differentiate Fisher models.** Uniformly in \(x\in S^2\), the normalized von Mises–Fisher density is \(1+\kappa u\cdot x+O(\kappa^2)\). When \(X=u\) is pinned, the derivative of the two-factor product at zero is \(u\cdot Y+u\cdot Z\), whose acute-event expectation is \(2M_1\). In the three-iid model, expand the three-factor Fisher density to order \(\kappa^2\); after averaging the squared linear statistic \(\bigl(u\cdot(X+Y+Z)\bigr)^2\) under the rotationally invariant acute event, its coefficient is \(M_1\). Common antipodal reflection makes the three-iid probability an even analytic function of \(\kappa\), improving the remainder to \(O(\kappa^4)\). All interchange steps are justified by bounded spherical coordinates and analytic normalization near zero.

## Verification

The companion `verify.py` uses only the Python standard library. It independently evaluates the original two-dimensional conditional probability integral by midpoint quadrature and estimates both the unweighted and weighted events by fixed-seed Monte Carlo. It also checks the full dipole probability for a nonzero parameter and the pinned Fisher initial slope by likelihood differentiation. Execute `python verify.py`; a successful run prints `ACUTE_SPHERE_CHECK_OK`. Finite numerical tolerances provide corroboration only; the proof above establishes the exact identities.

## Relationship to prior work

Maeda (2008) treats the uniform spherical-triangle *type probabilities*; the exact baseline \(p_0\) is not asserted to be new. Li, Cooper and Eum (dated May 27, 2013) explicitly set up a pinned von Mises–Fisher sampling experiment and report a numerical probability-versus-concentration curve, including its increase from the uniform limit; their inspected paper does not evaluate its exact initial slope. The present result supplies that initial slope and, independently, a new cosine-weighted uniform moment and a complete all-parameter law for a normalized first-spherical-harmonic (dipole) perturbation. Le's earlier shape-density work is related but uses uniform sampling from a spherical cap rather than a dipole perturbation. Published formulae on acute-triangle probabilities are acknowledged and not presented as new.

## Limitations

No assertion is made about global monotonicity of the von Mises–Fisher probability at arbitrary concentration, about random triangles in other dimensions, or about general nonuniform densities. The dipole family is nonnegative precisely over \(|\varepsilon|\le1\). Historical originality is provisional: some early spherical shape-density and type-classification papers were not available in full text. The proof and numerical checks have not received an independent audit.

## References

- Yoichi Maeda, *Seven Types of Random Spherical Triangle in \(S^n\) and Their Probabilities*, in *Computational Geometry and Graph Theory*, Lecture Notes in Computer Science 4535, 119–126 (2008), DOI: 10.1007/978-3-540-89550-3_13.
- Shunji Li, Paul Cooper, Saewon Eum, *Random Triangles on a Sphere*, document dated May 27, 2013; accessible text: https://studyres.com/doc/15663418/random-triangles-on-a-sphere (especially §§2.7–2.8 and 3.1–3.5).
- Huiling Le, *Random spherical triangles II: Shape densities*, *Advances in Applied Probability* 21 (1989), 581–594, DOI: 10.2307/1427637.
