# A universal angular-information boundary layer for a noisy quarter-turn swimmer

## Finding

For a harmonically confined, four-direction run-and-tumble particle at the balanced turning-to-trap rate, the two Cartesian position coordinates may have zero covariance while retaining positive mutual information. The exact athermal angular information and its universal weak-thermal-noise crossover are as follows. Put \(a=v_0/\mu>0\), \(h=D/\mu\geq0\), and take the two independent stationary diagonal coordinates to be \(U,V\stackrel{\mathrm{iid}}{\sim}\mathrm{Unif}[-a,a]+N(0,h)\), with the Gaussian term interpreted as zero at \(h=0\). Define
\[
X_\theta=U\cos\theta+V\sin\theta,\qquad
Y_\theta=-U\sin\theta+V\cos\theta,
\qquad I_h(\theta)=I(X_\theta;Y_\theta).
\]
Here \(I\) is continuous mutual information in natural logarithmic units. For \(0\leq\theta\leq\pi/4\),
\[
\boxed{I_0(\theta)=\tan\theta+2\log\cos\theta.}
\]
With the natural quarter-period symmetries this completely determines the zero-noise angular law. It increases strictly from zero to \(1-\log2\); its small-angle onset is \(I_0(\theta)\sim\theta\), whereas its approach to the maximum is cubic:
\[
I_0(\pi/4)-I_0(\pi/4-\delta)=\tfrac43\delta^3+O(\delta^4)\quad(\delta\downarrow0).
\]

For any \(h>0\), let \(f_{a,h}\) denote the density of \(\mathrm{Unif}[-a,a]+N(0,h)\), and define its Fisher information for translation by \(J_h=\int_{\mathbb R}(f'_{a,h})^2/f_{a,h}\,dx\). Then the sharp infinitesimal angular behavior is instead quadratic:
\[
\boxed{I_h(\theta)=\left[\left(\frac{a^2}{3}+h\right)J_h-1\right]\theta^2+o(\theta^2),\qquad \theta\to0.}
\]
The coefficient is strictly positive. In addition, \(\operatorname{Cov}(X_\theta,Y_\theta)=0\) at every angle, but \(I_h(\theta)>0\) whenever \(\sin(2\theta)\ne0\). At every such angle, adding independent positive thermal noise strictly lowers the mutual information.

For the sharp small-noise transition put \(\varepsilon=\sqrt h/a\), and let \(\phi\) and \(\Phi\) denote the standard normal density and cumulative distribution. Define for \(t\geq0\)
\[
G_t(z)=\begin{cases}
\frac{1}{2t}\int_{-t}^t\Phi(w-z)\,dw,&t>0,\\
\Phi(-z),&t=0,
\end{cases}
\qquad
\mathcal H(t)=-\int_{\mathbb R}G_t(z)\log G_t(z)\,dz.
\]
Both integrals converge, with \(0<G_t(z)<1\). The **universal boundary-layer law** is
\[
\boxed{\lim_{\varepsilon\downarrow0}
\frac{I_{a^2\varepsilon^2}(\varepsilon t)}{\varepsilon}
=F(t):=2[\mathcal H(t)-\mathcal H(0)]\quad\text{for each fixed }t\geq0.}
\]
Here \(F(t)>0\) for \(t>0\) and its sharp limiting regimes are
\[
\boxed{\lim_{t\downarrow0}\frac{F(t)}{t^2}=\frac{K}{3},\qquad
\lim_{t\to\infty}\frac{F(t)}t=1,\qquad
K=\int_{\mathbb R}\frac{\phi(z)^2}{\Phi(-z)}\,dz=0.9031972855686\ldots.}
\]
Thus the singular linear athermal cusp is smoothed over angular scale \(\theta\asymp\sqrt{\mu D}/v_0\). Equivalently,
\[
\boxed{\lim_{h\downarrow0}\sqrt h\,J_h=K/a,\qquad
\left(\frac{a^2}{3}+h\right)J_h-1\sim\frac{Ka}{3\sqrt h}.}
\]
These assertions concern equal-turning-rate, stationary position information; they do not concern trajectory entropy production.

## Assumptions and scope

The planar active particle has harmonic restoring rate \(\mu>0\), propulsion speed as normalized below \(v_0>0\), equal clockwise/counterclockwise quarter-turn rates \(\gamma>0\), and independent isotropic translational Brownian diffusivity \(D\geq0\). In the equivalent independent diagonal coordinates its equations are \(dU=(-\mu U+v_0 S_U)dt+\sqrt{2D}\,dB_U\) and \(dV=(-\mu V+v_0 S_V)dt+\sqrt{2D}\,dB_V\), where \(S_U,S_V\) independently switch signs at rate \(\gamma\). The theorem fixes the physically distinguished ratio \(\gamma/\mu=1\), so the athermal stationary telegraph laws are exactly uniform. For the displayed information results the coordinates \((X_\theta,Y_\theta)\) may represent any common rotation of the two diagonal axes. All random variables are at stationarity, and all angles are real. Mutual information is in nats; it is finite also in the athermal compact-support case. No claims are made for unequal turn rates, arbitrary trap anisotropy, or nonstationary observations.

## Proof

**1. Stationary product law and the exact athermal entropy.** The stationary athermal one-dimensional confined telegraph density is proportional to \((1-(u/a)^2)^{\gamma/\mu-1}\) on \((-a,a)\). At \(\gamma=\mu\) the density is uniform. The independent thermal Ornstein--Uhlenbeck responses add independent Gaussians with variance \(h=D/\mu\); hence the stated independent, identically distributed product law follows. Orthogonal rotation has determinant one, so joint differential entropy is \(2H(U)\). The two rotated marginal laws agree by exchangeability and symmetry, giving \(I_h(\theta)=2[H(U\cos\theta+V\sin\theta)-H(U)]\).

At zero thermal noise and \(0\leq\theta\leq\pi/4\), put \(A=a\cos\theta\geq B=a\sin\theta\). The convolution of the independent \(\mathrm{Unif}[-A,A]\) and \(\mathrm{Unif}[-B,B]\) laws is a trapezoid: its density equals \(1/(2A)\) on \(|x|\leq A-B\), and \((A+B-|x|)/(4AB)\) on \(A-B<|x|<A+B\). Direct integration yields \(H(U\cos\theta+V\sin\theta)=\log(2A)+B/(2A)\), including the limiting endpoints. This proves the boxed angular law. Differentiation gives \(dI_0/d\theta=(1-\tan\theta)^2\); its maximum and the two local asymptotics follow from Taylor expansion. Exchangeability, reflection, and sign reversals give the angular symmetries.

**2. Nonzero-noise information and its angular Hessian.** For \(h>0\), \(f_{a,h}\) is smooth, positive, even, and has Gaussian tails. Writing \(r=f'_{a,h}/f_{a,h}\), the score of the rotated joint density at \(\theta=0\) is \(S(x,y)=-y r(x)+x r(y)\). The derivatives of both marginal densities vanish at \(\theta=0\). Since \(\int xr(x)f(x)dx=-1\), and with \(\sigma^2=a^2/3+h\), direct independence gives \(\mathbb ES^2=2(\sigma^2J_h-1)\). The second-order expansion of relative entropy yields \(I_h(\theta)=(\sigma^2J_h-1)\theta^2+o(\theta^2)\). The Cauchy--Schwarz information inequality says \(\sigma^2J_h\geq1\), with equality only for a Gaussian density; it is strict here because the fourth cumulant of \(U\) is \(-2a^4/15\).

Indeed, independence of \(U,V\) implies the exact mixed fourth cumulant
\[
\operatorname{cum}(X_\theta,X_\theta,Y_\theta,Y_\theta)
=-\frac{a^4}{15}\sin^2(2\theta).
\]
It is nonzero for nonaxis angles, ruling out coordinate independence despite zero covariance. To compare two diffusivities \(h_2>h_1\), represent \((X_\theta,Y_\theta)\) at \(h_2\) as the pair at \(h_1\) plus independent Gaussian noise of variance \(h_2-h_1\) in each coordinate. The data-processing inequality lowers mutual information. Strictness follows from the strict convexity of relative entropy under the everywhere-positive Gaussian transition kernel: equality would require a constant input likelihood ratio, i.e. initial coordinate independence, contrary to the displayed cumulant.

**3. Singular angular layer.** Write \(\sigma=a\varepsilon\). A marginal at angle \(\varepsilon t\) has the form \(W=A L+\sigma(Z+bT)\), where \(L,T\) are independent uniform variables on \([-1,1]\), \(Z\) is standard normal, \(A=a\cos(\varepsilon t)\), and \(b=a\sin(\varepsilon t)/\sigma\to t\). For fixed \(b\geq0\), define \(G_b(z)=\mathbb P(Z+bT>z)\). The density of \(A L+\sigma(Z+bT)\) is the difference of the two translated edge-survival functions divided by \(2A\). Away from the two endpoints \(\pm A\) it approaches the constant density \(1/(2A)\). With rescaling \(x=A+\sigma z\), the right-edge density divided by that constant converges to \(G_b(z)\); the left edge is its reflection. The Gaussian tail bounds permit dominated convergence in the entropy integral after subtraction of \(\log(2A)\), yielding the precise boundary-entropy lemma
\[
H(A L+\sigma(Z+bT))=\log(2A)+\frac{\sigma}{A}\mathcal H(b)+o(\sigma/A)
\]
whenever \(\sigma/A\downarrow0\) and \(b\) tends to a fixed nonnegative value. For \(\theta=0\), use \(A=a,b=0\). At \(\theta=\varepsilon t\), \(\log(A/a)=O(\varepsilon^2)\) and \(b\to t\). Subtracting the two marginal entropies as in step 1 gives the displayed limit \(F(t)\). The integrals defining \(\mathcal H\) converge since their integrands vanish at both tails at least Gaussian-fast apart from an integrable linear factor.

**4. Scaling-function limits and Fisher singularity.** For \(t>0\), \(G_t(z)=\mathbb E\Phi(tT-z)\). Strict concavity of \(q\mapsto-q\log q\), followed by integration over \(z\), gives \(\mathcal H(t)>\mathcal H(0)\). The symmetric averaging expansion is \(G_t(z)=G_0(z)+(t^2/6)G_0''(z)+O(t^4)\) in the required Gaussian-weighted integrals. Integration by parts gives \(\mathcal H(t)-\mathcal H(0)=(K/6)t^2+o(t^2)\), using \(G_0'=-\phi\) and \(K=\int\phi^2/G_0\). To see the large-\(t\) limit, put \(z=tu\): the function \(G_t(tu)\) converges to the piecewise-linear tail \(\min(1,\max(0,(1-u)/2))\), and dominated convergence with Gaussian tail controls shows \(\mathcal H(t)/t\to\int_{-1}^1-\frac{1-u}{2}\log\frac{1-u}{2}\,du=1/2\). Hence \(F(t)/t\to1\).

Finally \(f_{a,h}(x)=[\Phi((x+a)/\sqrt h)-\Phi((x-a)/\sqrt h)]/(2a)\). Its two boundary layers are at \(x=\pm a+O(\sqrt h)\). At the right edge \(f_{a,h}(a+\sqrt h z)\sim G_0(z)/(2a)\) and \(f'_{a,h}(a+\sqrt h z)\sim-\phi(z)/(2a\sqrt h)\). Integrating \((f')^2/f\) over both edges gives \(\sqrt h J_h\to K/a\); the interior and distant tails have negligible contribution by Gaussian bounds. The final Fisher-coefficient asymptotic follows.

## Verification

The accompanying standalone `verify.py` recomputes the analytic trapezoid law by one-dimensional entropy quadrature, checks the angular identities and mixed fourth-cumulant polynomial, independently reconstructs the smoothed uniform and trapezoid marginals, evaluates the Fisher coefficient, the limiting constant and scaling function, and compares finite-noise information to both the small-angle and boundary-layer predictions. These numerical checks test examples and limiting trends; the continuum claims are proved analytically above. Run with Python 3, NumPy and SciPy: `python verify.py`.

## Relationship to prior work

Smith, Le Doussal, Majumdar and Schehr [1] established the physically relevant four-orientation harmonic model, its rotated-coordinate factorization and its exact athermal and diffusive stationary position distributions. The product-uniform law at balanced rates is **prior work**, not the novelty claimed here. Frydel [2] gave complementary beta-convolution and diffusion analysis of trapped active particles. The generic identity relating rotation and mutual information is standard in independent-component analysis [3]. The present claim is the *explicit angular-information law together with the sharp nonanalytic-to-analytic weak-noise crossover*, including the boundary-layer integral and Fisher coefficient, neither of which is asserted to be a new derivation of the underlying position law. No assertion of independent publication-priority certification is made.

## Limitations

The result is confined to stationary, equal-rate four-direction dynamics at \(\gamma/\mu=1\). The weak-noise limit is pointwise for each fixed scaled angle \(t\), not uniform across all growing \(t\). The maximum is proved in the athermal case only, and no general optimum in angle at positive thermal noise is claimed. The Fisher and entropy limits are analytic continuum statements, not finite-grid extrapolations. Generic entropy convolution identities and potentially unindexed information-theoretic treatments may imply portions of the result; detailed external independent review remains outstanding.

## References

1. N. R. Smith, P. Le Doussal, S. N. Majumdar, G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445 (first posted 2022-07-21). https://arxiv.org/abs/2207.10445
2. D. Frydel, *Positing the problem of stationary distributions of active particles as third-order differential equation*, arXiv:2207.08695 (first posted 2022-07-18). https://arxiv.org/abs/2207.08695
3. E. G. Miller and J. W. Fisher III, *ICA Using Spacings Estimates of Entropy* (2003), https://people.cs.umass.edu/~elm/papers/ICA_CONF.pdf
