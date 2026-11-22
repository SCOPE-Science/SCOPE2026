# Kurtosis determines nonlinear critical clustering in a three-player Gaussian resource game

## Finding
For a three-player proportional-resource Gaussian location game with a finitely supported, symmetric resource law of positive variance \(v\) and fourth central moment \(\mu_4\), set its common Gaussian competitive-reach variance to the *linear critical value* \(\sigma^2=v/2\). Write \(\kappa=\mu_4/v^2\) for raw kurtosis. In a neighborhood of the symmetric strategy profile, the reduced two-dimensional dynamics are
\[
\dot z=\frac{13-12\kappa}{27v^2}\|z\|^2z+O(\|z\|^5).
\]
Consequently, the symmetric equilibrium is locally asymptotically stable if \(\kappa>13/12\), but Lyapunov unstable if \(1\le\kappa<13/12\), even though the full Jacobian has exactly the same zero transverse eigenvalues in both regimes. For \(\kappa>13/12\), every nonstationary trajectory on the local center manifold has the sharp critical relaxation law
\[
\lim_{t\to\infty}\sqrt{t}\,\|z(t)\|=\sqrt{\frac{27v^2}{2(12\kappa-13)}}.
\]
The threshold is attained from either side by finite symmetric resource laws; no conclusion is claimed at \(\kappa=13/12\).

For example, the equally weighted two-point resource distribution at \(-1,1\) has \((v,\kappa)=(1,1)\) and a nonlinearly unstable critical equilibrium. The law with masses \((1/6,2/3,1/6)\) at \((-\sqrt3,0,\sqrt3)\) has \((v,\kappa)=(1,3)\) and a locally asymptotically stable critical equilibrium. Both have the same variance and hence the same linear critical Gaussian reach \(\sigma^2=1/2\).

## Assumptions and scope
Let \(B\) be a positive, finitely supported probability measure on the real resource-trait line, symmetric under \(b\mapsto-b\), with \(v=\mathbb E_B[b^2]>0\) and \(\mu_4=\mathbb E_B[b^4]\). Three players select scalar positions \(x_i\) in a common interval whose interior contains zero and the support of \(B\). Let
\[
f_i(x_i,b)=\exp\!\left(-\frac{(x_i-b)^2}{2\sigma^2}\right),\quad G_i(x,b)=\frac{f_i(x_i,b)}{\sum_{j=1}^3f_j(x_j,b)},\quad u_i(x)=\mathbb E_B[G_i(x,b)].
\]
The continuous-time learning rule is unprojected own-payoff gradient ascent \(\dot x_i=\partial_{x_i}u_i(x)\) in the interior. Only local trajectories near \(x_1=x_2=x_3=0\) are considered, so boundary projection is irrelevant. Time is normalized exactly as in this gradient rule. Denote \(m=(x_1+x_2+x_3)/3\), \({\bf1}=(1,1,1)^\top\), and \(z=x-m{\bf1}\), so \(\sum_i z_i=0\) and \(\|z\|\) is the ordinary Euclidean norm. The origin is the unique symmetric Nash profile for these kernels, but no assertion is made about other, nonsymmetric equilibria far from zero.

## Proof
**1. Exact vector field and linearization.** Differentiating the Gaussian allocation gives
\[
\dot x_i=\frac{1}{\sigma^2}\mathbb E_B\big[G_i(1-G_i)(b-x_i)\big].
\]
At the origin, all \(G_i=1/3\). By direct differentiation, or by decomposing the permutation-symmetric Jacobian, the eigenvalue on the common-position mode \(\operatorname{span}\{{\bf1}\}\) is \(-2/(9\sigma^2)\), and the double eigenvalue on \(E=\{z:\sum_i z_i=0\}\) is
\[
\lambda_\perp=\frac{1}{9\sigma^2}\left(\frac{v}{\sigma^2}-2\right).
\]
At \(\sigma^2=v/2\), the common mode has eigenvalue \(-4/(9v)\) and \(E\) is the two-dimensional center eigenspace.

**2. Invariant exact branch and cubic coefficient.** Since \(B\) is reflection symmetric and the players are exchangeable, the line \(x=(a,-a,0)\) is invariant. Put \(\theta=1/\sigma^2\). Along it the resource share for player one is
\[
p_a(b)=\frac{e^{\theta ab}}{2\cosh(\theta ab)+e^{\theta a^2/2}},
\quad\dot a=\theta\,\mathbb E_B[(b-a)p_a(b)(1-p_a(b))].
\]
A Taylor expansion at \(a=0\), with all odd resource moments vanishing, yields the exact local series
\[
\dot a=\frac{\theta(v\theta-2)}9a+\frac{\theta^2(1+6v\theta-3\mu_4\theta^2)}{54}a^3+O(a^5).
\]
At \(\theta=2/v\), this is
\[
\dot a=\frac{2(13-12\kappa)}{27v^2}a^3+O(a^5).
\]
The full series coefficient is independently reconstructed symbolically by `CHECK.py` from the exact allocation formula; no fitted normal form or trajectory data is used for it.

**3. Reduction in all transverse directions.** The finite-support vector field is analytic, permutation-equivariant and odd under simultaneous strategy reflection \(x\mapsto-x\). An equivariant local center manifold for the two-dimensional space \(E\) can therefore be chosen odd and has common-mode component \(m=h(z)=O(\|z\|^3)\). Since the linearization preserves the splitting \(\operatorname{span}\{{\bf1}\}\oplus E\) and vanishes on \(E\), substituting \(h\) does not change the cubic transverse term. The reduced cubic vector polynomial is odd and permutation-equivariant. On \(E\), every such cubic projected to \(E\) is a scalar multiple of \(\|z\|^2z\): using \(\sum z_i=0\), one has \(z_i^3=(\sum_jz_j^2)z_i/2+(\sum_jz_j^3)/3\), and permutation-equivariant cubic combinations reduce to this form after removing the common component. Evaluating at \(z=(a,-a,0)\), whose squared norm is \(2a^2\), determines the scalar coefficient to be half the one in Step 2. Odd symmetry eliminates even Taylor orders. Hence
\[
\dot z=\alpha\|z\|^2z+O(\|z\|^5),\qquad\alpha=\frac{13-12\kappa}{27v^2}.
\]

**4. Nonlinear critical classification.** If \(\alpha<0\), the center-manifold radial derivative satisfies \(\dot r=\alpha r^3+O(r^5)<0\) for sufficiently small \(r=\|z\|>0\). Integrating \(d(r^{-2})/dt=-2\alpha+O(r^2)\) gives \(r(t)\sqrt t\to(-2\alpha)^{-1/2}\). The negative common-mode eigenvalue and the center-manifold stability theorem imply local asymptotic stability of the full equilibrium. If \(\alpha>0\), the invariant line of Step 2 contains arbitrarily close positive initial values with \(\dot a>0\), proving Lyapunov instability of the full equilibrium. The zero-cubic boundary \(\alpha=0\) requires higher-order analysis and is excluded.

## Verification
Execute `python CHECK.py` in an environment with Python 3, NumPy, SymPy and SciPy. It checks four symbolic Taylor coefficients directly from the allocation fractions; reproduces the normalized critical coefficient; compares the all-direction cubic projection against independent finite sums for the two explicit resource laws; verifies strategy-reflection symmetry; and integrates the exact three-player gradient equations for local behavior and the stable example's predicted inverse-square-root amplitude. The two-point example moves away from the critical equilibrium; the three-point example approaches it. These numerical checks corroborate but do not establish infinite-time claims, which are proved above.

## Relationship to prior work
Lovett and Fu (arXiv:2611.17148, first publicly posted 2026-11-12) introduce this proportional Gaussian influencer game and prove its linear threshold \(\sigma^2=(N-2)v/(N-1)\), with a three-player pitchfork in their studied bimodal resource family. Their stated Jacobian criterion leaves the equality case nonhyperbolic. The present result classifies the critical *nonlinear* behavior for every finite symmetric resource law using its fourth moment, exposes both stability outcomes at exactly the same variance and reach, and establishes the sharp attracting-side rate. Earlier ecological niche-competition work (notably Pigolotti et al. and Dieckmann–Doebeli) studies different Lotka–Volterra or evolutionary-branching laws and supports the broader motivation that resource/kernel shape can affect clustering, but does not directly imply this three-player proportional-payoff cubic coefficient. The originating article's supplementary section on bifurcations was not independently accessible in this assessment, so an unrecognized equivalent supplemental calculation remains a priority risk.

## Limitations
The result is local and deterministic; it does not classify global attractors or stochastic learning. It requires exactly three symmetric Gaussian competitors with a finitely supported, reflection-symmetric resource distribution and common reach. The stable critical \(t^{-1/2}\) law is asserted for nonstationary center-manifold trajectories; exceptional strong-stable trajectories may converge exponentially. At \(\kappa=13/12\) the cubic vanishes, and the theorem does not determine stability. A fourth-moment sign criterion need not survive asymmetric resources, different kernels, or other player counts. No independent mathematical validation is claimed.

## References
1. M. Lovett and F. Fu, *Learning Dynamics of the Influencer's Game in Resource Landscapes*, arXiv:2611.17148v1 (public 2026-11-12), https://arxiv.org/abs/2611.17148 ; main article including model equations (1)–(7), Theorems 3–6, and Gaussian stability Corollary 9.
2. S. Pigolotti, C. López, E. Hernández-García and K. H. Andersen, *How Gaussian competition leads to lumpy or uniform species distributions*, arXiv:0802.3274 (2008), https://arxiv.org/abs/0802.3274 . The analyzed Lotka–Volterra overlap-competition system is distinct from the proportional allocation game.
3. U. Dieckmann and M. Doebeli, *On the origin of species by sympatric speciation*, Nature 400 (1999), 354–357, https://doi.org/10.1038/22521 . Context for evolutionary branching under resource competition, not an equivalence claim.
