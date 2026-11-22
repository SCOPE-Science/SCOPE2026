# Fourth-root equilibrium onset and a fold wedge on the conservative sine-flow cylinders

## Finding

The conservative unforced boundary of the Ramar sine-driven three-dimensional vector field has two independent first integrals away from a degenerate axis. Its invariant circular cylinders admit a codimension-two local equilibrium transition with an explicit fourth-root law and a sharp two-pair fold wedge. The distinct fourth-root exponent is a property of the specific trigonometric coupling, rather than a claim about general Hamiltonian systems.

Fix \(b,k>0\). Define \(g_0=kb^2/3\), \(\delta=g-g_0\), \(\varepsilon=R^2-kb^2\), and \(h=2kb^2/45>0\). There are neighborhoods of \((\delta,\varepsilon)=(0,0)\) and the lower cylinder pole in which the following statements hold for \(g>0\):

* At \(\delta=0\) and \(\varepsilon>0\), exactly two off-axis equilibria near the lower pole have \(x\)-coordinates
  \[
  x_\pm=\pm\left(\frac{45\varepsilon}{2kb^2}\right)^{1/4}(1+O(\varepsilon^{1/2})),
  \quad z_\pm=-b+\frac b6 x_\pm^2+O(x_\pm^4),\quad y_\pm=0.
  \]
  They are hyperbolic saddles **within the invariant cylinder**. At \(\delta=0\), \(\varepsilon<0\), there are none nearby.
* For \(\delta<0\) sufficiently close to zero, a unique fold of off-axis equilibria occurs at
  \[
  \varepsilon_f(\delta)=-\frac{45}{8kb^2}\delta^2+O(|\delta|^3).
  \]
  For \(\varepsilon_f(\delta)<\varepsilon<0\), there are exactly **two symmetric pairs** of nearby off-axis equilibria: the inner pair consists of elliptic centers on the cylinder; the outer pair consists of hyperbolic saddles. For \(\varepsilon<\varepsilon_f(\delta)\) sufficiently near the fold there are no nearby off-axis equilibria; at the fold there is one degenerate symmetric pair. For \(\varepsilon>0\) sufficiently close to zero there is one nearby saddle pair.
* For \(\delta>0\) sufficiently close to zero, \(\varepsilon>0\) gives exactly one nearby saddle pair and \(\varepsilon<0\) gives none. All counts are **local near the lower pole**; no global equilibrium census is asserted.

The lower axial equilibrium at \((x,y,z)=(0,0,-R/\sqrt k)\) is a cylinder saddle for \(R<b\sqrt{k}\) and a cylinder center for \(R>b\sqrt{k}\). The upper axial equilibrium at \((0,0,R/\sqrt k)\) is a cylinder center for every \(R>0\). At the equality \(R=b\sqrt{k}\), the lower pole is nonhyperbolic and its linear type does not decide stability.

## Assumptions and scope

The real autonomous differential equation is
\[
\dot x=-kyz,\qquad \dot y=b\sin x+xz,\qquad \dot z=gxy,
\qquad b,g,k>0.
\]
It is the exactly specified \(a=c=d=0\) limit of the Ramar flow \(\dot x=ax-kyz\), \(\dot y=b\sin x+xz\), \(\dot z=gxy-cz+d\). This statement concerns the conservative limit and does not assert chaotic behavior or persistence under nonzero damping, growth or forcing.

For initial data with \(R^2=gx(0)^2+kz(0)^2>0\), \(R\) is fixed along the trajectory; \(R\) indexes a different invariant cylinder, not an independent dynamical coordinate. The local neighborhood is taken jointly in \(\delta\), \(\varepsilon\) and \(x\), with the negative-\(z\) branch; all \(O(\cdot)\) terms have fixed \(b,k>0\).

## Proof

**1. Exact integrable reduction.** Direct differentiation proves
\[
P(x,y,z)=gx^2+kz^2,\qquad \dot P=2gx(-kyz)+2kz(gxy)=0.
\]
For \(P=R^2>0\), set
\[
x=\frac R{\sqrt g}\cos\theta,\qquad z=\frac R{\sqrt k}\sin\theta.
\]
The first and third differential equations give \(\dot\theta=\sqrt{gk}\,y\). Therefore
\[
\ddot\theta=b\sqrt{gk}\sin\!\left(\frac R{\sqrt g}\cos\theta\right)
+R^2\sin\theta\cos\theta.
\]
Define the smooth periodic primitive
\[
J_R(\theta)=\int_0^\theta\sin\!\left(\frac R{\sqrt g}\cos u\right)\,du.
\]
The integrand changes sign under \(u\mapsto u+\pi\), so its integral over any full period is zero; thus \(J_R\) is \(2\pi\)-periodic. The second first integral on each cylinder is
\[
H_R(\theta,y)=\frac{gk}{2}y^2-b\sqrt{gk}J_R(\theta)-\frac{R^2}{2}\sin^2\theta.
\]
Differentiating \(H_R\) and inserting the angular equation yields zero. Since \(J_R\) and \(\sin^2\theta\) are bounded on the circle, any fixed-energy trajectory has bounded \(y\); its \(x,z\) are already bounded by \(P\). Smoothness and standard continuation give complete flow. Every connected compact regular energy level on a cylinder is a circle on which the vector field is nowhere zero, hence carries periodic motion. This assertion deliberately excludes critical separatrix energy levels and the degenerate invariant axis \(R=0\), where all points \((0,y,0)\) are equilibria.

**2. Pole types.** Let \(F(\theta)\) denote the right side of the angular second-order equation. At the lower pole \(\theta=3\pi/2\),
\[
F'(3\pi/2)=R(b\sqrt k-R),
\]
whereas at the upper pole \(\theta=\pi/2\),
\[
F'(\pi/2)=-R(b\sqrt k+R).
\]
The planar linearization in \((\theta,\dot\theta)\) has eigenvalues satisfying \(\lambda^2=F'(\theta_0)\). Strictly negative derivative gives an elliptic center by the local conserved Hamiltonian; strictly positive derivative gives a saddle. This proves the stated strict-inequality types.

**3. Scalar equation for off-axis equilibria.** On the local negative-\(z\) half cylinder, write
\[
z_R(x)=-\sqrt{\frac{R^2-gx^2}{k}},\qquad s(x)=\frac{\sin x}{x},\quad s(0)=1.
\]
Any non-pole equilibrium nearby has \(y=0\), \(x\ne0\), and must solve
\[
b\sin x+xz_R(x)=x\{bs(x)+z_R(x)\}=0.
\]
Since \(s(x)>0\) for small \(|x|\), this is exactly equivalent to
\[
R^2=\Phi(x),\qquad \Phi(x)=gx^2+kb^2s(x)^2.
\]
The Taylor series of \(s(x)^2\) is
\[
s(x)^2=1-\frac{x^2}3+\frac{2x^4}{45}-\frac{x^6}{315}+O(x^8).
\]
Thus, putting \(t=x^2\), the equilibrium equation is
\[
\varepsilon=G(t;\delta)
=\delta t+ht^2-\frac{kb^2}{315}t^3+O(t^4),\qquad t>0.
\]
The analytic remainder and its derivatives are uniform for small \(t,\delta\). In particular \(G_{tt}(0;0)=2h>0\). Shrink a fixed neighborhood so that \(G_{tt}>h>0\) there.

**4. Local root classification and degeneracy.** If \(\delta\ge0\), \(G_t(0;\delta)=\delta\) and strict convexity imply that \(G\) is strictly increasing for \(t>0\). Hence exactly one small positive root for each sufficiently small \(\varepsilon>0\), and none for \(\varepsilon<0\). At \(\delta=0\), solve \(\varepsilon=ht^2(1+O(t))\) to obtain \(t=(\varepsilon/h)^{1/2}(1+O(\varepsilon^{1/2}))\), giving the fourth-root formula for \(x=\pm\sqrt t\). Substituting \(z=-bs(x)\) yields its displayed expansion.

For \(\delta<0\), strict convexity and the implicit-function theorem applied to \(G_t(t;\delta)=0\) yield a unique critical point
\[
t_f(\delta)=-\frac{\delta}{2h}+O(\delta^2)>0.
\]
It is a strict minimum, whose height is
\[
G(t_f;\delta)=-\frac{\delta^2}{4h}+O(|\delta|^3)
=-\frac{45\delta^2}{8kb^2}+O(|\delta|^3).
\]
A horizontal line above this minimum but below zero meets the local strictly convex graph at exactly two positive \(t\)-values; at the minimum they coalesce, and below it there are none. Each positive \(t\) produces exactly two equilibria \(x=\pm\sqrt t\). For \(\varepsilon>0\), exactly one positive small root exists. These statements hold after choosing the local parameter neighborhood so both positive intersections are included.

**5. Local stability of each pair.** Let \(Q(x)=b\sin x+xz_R(x)\). At a nonzero equilibrium, differentiating the relation above and using \(z_R(x)=-bs(x)\) gives
\[
Q'(x)=\frac{x\Phi'(x)}{2kb\,s(x)}
=\frac{x^2G_t(x^2;\delta)}{kb\,s(x)}.
\]
On the lower half cylinder, \(dx/d\theta=-(R/\sqrt g)\sin\theta>0\). Therefore the sign of \(F'(\theta)\) agrees with \(G_t\): the positive-slope (outer) branch is hyperbolic and the negative-slope (inner) branch is elliptic. The Hamiltonian first integral makes the elliptic equilibria nonlinear centers on their cylinders. At the fold \(G_t=0\), the transverse linearization is degenerate, and no hyperbolicity is claimed.

## Verification

A self-contained symbolic/numerical diagnostic is supplied as `check.py`. It checks the Taylor coefficients, both pole derivatives, the derivative identity used for branch stability, the leading fourth-root coefficient and the local fold law on a sample of small parameters. The theorem's infinite and uniform local assertions are proved by the analytic and convexity arguments above, **not** by finite tests.

## Relationship to prior work

R. Ramar, *Design of a New Chaotic System with Sine Function: Dynamic Analysis and Offset Boosting Control* (2023), introduces and studies the full driven dissipative sine system. Its full paper treats chaos, parameter plots, fixed-point linearization, offset boosting and synchronization; the conservative cylinder reduction and codimension-two local fold/fourth-root equilibrium diagram above are not part of its stated findings. The first-integral reduction and the local equilibrium diagram are the claimed contributions; elementary facts about one-degree-of-freedom Hamiltonian systems and generic folds are not claimed as new.

## Limitations

Only the exactly unforced undamped boundary \(a=c=d=0\) is analyzed. All equilibrium counts and fourth-root/fold statements are local near the negative-\(z\) pole and near \(g=kb^2/3,\ R=b\sqrt k\). Equilibria elsewhere on the cylinder and global bifurcations are not counted. Stability means **within a fixed invariant cylinder**, not asymptotic attraction in the full three-dimensional conservative flow; no equilibrium is asserted to be a full-space sink. The computation does not establish persistence for \(a,c,d\ne0\), chaotic dynamics or novel generic bifurcation theory. Independent validation has not been performed.

## References

1. R. Ramar (2023), “Design of a New Chaotic System with Sine Function: Dynamic Analysis and Offset Boosting Control,” *Chaos Theory and Applications* **5**(2), 118–126. DOI: [10.51537/chaos.1223766](https://doi.org/10.51537/chaos.1223766), first public online July 28, 2023. Full paper: https://dergipark.org.tr/en/download/article-file/2850554.
2. Standard one-degree-of-freedom Hamiltonian regular-level and analytic fold arguments are used as general mathematical background, not as a claim of priority.
