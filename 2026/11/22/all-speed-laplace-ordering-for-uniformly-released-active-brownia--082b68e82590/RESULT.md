# All-speed Laplace ordering for uniformly released active Brownian searchers

## Finding

An active Brownian particle with a random initial position and direction escapes a completely absorbing bounded domain **faster in Laplace-transform order at every larger propulsion speed**, independently of the shape of the domain and of the angular-diffusion rate. In fact, its entire discounted mean survival family is a strict Stieltjes function of squared swimming speed. This is a global finite-speed statement, not a weak-activity expansion.

**Theorem.** Let \(G\subset\mathbb R^2\) be nonempty, bounded, connected, and have \(C^2\) boundary. Let \(D>0\), \(D_R\ge0\), and \(v\ge0\). Before first exit from \(G\), define
\[
 dX_t=v(\cos\Theta_t,\sin\Theta_t)\,dt+\sqrt{2D}\,dB_t,
 \qquad d\Theta_t=\sqrt{2D_R}\,dW_t\pmod{2\pi},
\]
where the Brownian drivers are independent. Start \(X_0\) uniformly on \(G\) and \(\Theta_0\) independently and uniformly on the circle. Write \(\tau_v=\inf\{t\ge0:X_t\notin G\}\), and for every \(q\ge0\) define
\[
 F_q(v)=\mathbb E\int_0^{\tau_v}e^{-qt}\,dt
 =\int_0^\infty e^{-qt}\Pr(\tau_v>t)\,dt.
\]
Thus \(F_0(v)=\mathbb E\tau_v\), while for \(q>0\), \(\mathbb E[e^{-q\tau_v}]=1-qF_q(v)\).

For **every** \(q\ge0\), there exists a finite positive Borel measure \(\nu_q\), supported in a bounded subset of \((0,\infty)\) (zero may be an accumulation point), such that, for all \(v\ge0\),
\[
 \boxed{\displaystyle F_q(v)=\int_{(0,\infty)}\frac{\nu_q(d\lambda)}{1+\lambda v^2}.}
\]
Its total mass is \(F_q(0)>0\). Consequently, for every integer \(n\ge1\) and every \(s\ge0\),
\[
 \boxed{\displaystyle
 (-1)^n\frac{d^n}{ds^n}F_q(\sqrt s)
 =n!\int_{(0,\infty)}\frac{\lambda^n\,\nu_q(d\lambda)}{(1+\lambda s)^{n+1}}>0.}
\]
In particular, if \(0\le v_1<v_2\), then
\[
 F_q(v_2)<F_q(v_1)\quad(q\ge0),\qquad
 \mathbb E[e^{-q\tau_{v_2}}]>\mathbb E[e^{-q\tau_{v_1}}]\quad(q>0).
\]
Hence the exit times are strictly ordered in **Laplace-transform order** across all propulsion speeds, even though a fixed starting position or direction need not have this ordering.

There are two further exact global consequences. First, \(s\mapsto1/F_q(\sqrt s)\) is strictly increasing and concave. Second, with the strictly positive weak-swimming susceptibility
\[
 \chi_q=-\left.\frac{d}{ds}F_q(\sqrt s)\right|_{s=0}>0,
\]
every speed obeys the rational lower bound
\[
 \boxed{\displaystyle F_q(v)\ge\frac{F_q(0)}{1+v^2\chi_q/F_q(0)}.}
\]
Finally \(F_q(v)\to0\) as \(v\to\infty\), and therefore \(\tau_v\to0\) in probability. The same formulae remain valid when \(D_R=0\), i.e. for a frozen but initially uniform random heading.

## Assumptions and scope

Both spatial and angular averages are essential: the initial joint distribution is normalized Lebesgue measure on \(G\times S^1\). The entire spatial boundary is absorbing, not reflecting, sticky, or partially reactive. The orientation evolves by achiral rotational Brownian motion without an angular drift or position-dependent torque. The particle has positive translational diffusivity, while its rotational diffusivity may vanish. The time-discount parameter \(q\) is nonnegative and arbitrary. All formulae are exact at every finite speed and every discount, without taking a hydrodynamic or small-propulsion limit.

The Stieltjes measure is an operator spectral measure, not a probability distribution of first-passage times. Its support may approach zero, so the theorem makes no unspecified large-speed power-law claim. Laplace-transform ordering is weaker than first-order stochastic ordering: no inequality between \(\Pr(\tau_{v_1}>t)\) and \(\Pr(\tau_{v_2}>t)\) is asserted at every individual \(t\).

## Proof

**1. Killed resolvent.** On the real Hilbert space \(H=L^2(G\times S^1,dx\,d\theta/(2\pi|G|))\), with scalar product \(\langle\cdot,\cdot\rangle\), define the nonnegative symmetric operator and the transport operator
\[
 A_q=qI-D\Delta_x-D_R\partial_\theta^2,
 \qquad B=(\cos\theta,\sin\theta)\cdot\nabla_x,
\]
with homogeneous spatial Dirichlet conditions and periodic angular conditions. Let \(\lambda_1>0\) be the first Dirichlet eigenvalue of \(-\Delta_x\). For \(q\ge0\), \(A_q\) is strictly positive selfadjoint and \(A_q\ge(q+D\lambda_1)I\). These assertions include \(D_R=0\), where the angular coordinate is a parameter. The killed backward generator is \(-A_q+qI+vB\). By the Markov resolvent formula and Fubini, its discounted expected survival function is the Dirichlet solution \(u_{q,v}=(A_q-vB)^{-1}{\bf1}\). Therefore
\[
 F_q(v)=\langle{\bf1},(A_q-vB)^{-1}{\bf1}\rangle.
\]
The drift is bounded and the symmetric Dirichlet form is coercive, so this inverse exists for every real \(v\), not only perturbatively.

**2. A bounded skew-adjoint symmetrization.** Define
\[
 K_q=A_q^{-1/2}BA_q^{-1/2},\qquad z_q=A_q^{-1/2}{\bf1}.
\]
The range of \(A_q^{-1/2}\) belongs to the spatial Dirichlet form domain, and the form inequality \(D\|\nabla_xA_q^{-1/2}f\|^2\le\|f\|^2\) gives the operator bound
\[
 \|K_q\|\le\frac1{\sqrt{D(q+D\lambda_1)}}.
\]
Integration by parts in \(x\), together with the zero spatial trace, gives \(\langle f,Bg\rangle=-\langle Bf,g\rangle\) on the form domain: the heading field is spatially divergence-free. Thus \(K_q^*=-K_q\) as an everywhere-defined bounded operator. The form factorization, justified first on smooth functions and then by form closure, yields
\[
 F_q(v)=\langle z_q,(I-vK_q)^{-1}z_q\rangle.
\]
Since \(K_q\) is real skew-adjoint, the real scalar equals its average with its transpose:
\[
 \begin{aligned}
 F_q(v)&=\tfrac12\langle z_q,[(I-vK_q)^{-1}+(I+vK_q)^{-1}]z_q\rangle\\
 &=\langle z_q,(I+v^2K_q^*K_q)^{-1}z_q\rangle.
 \end{aligned}
\]
This identity holds for every real speed because the spectrum of a bounded skew-adjoint operator lies on the imaginary axis.

**3. Exact positive measure, and why its support excludes zero.** Write \(C_q=K_q^*K_q=-K_q^2\). This is bounded, selfadjoint and nonnegative. Let \(E_q\) be its spectral projections and set \(\nu_q(S)=\langle z_q,E_q(S)z_q\rangle\). The spectral theorem gives the displayed Stieltjes integral, with mass \(\|z_q\|^2=F_q(0)\).

The measure has no atom at zero. Indeed, if \(K_qh=0\), then \(Bf=0\) with \(f=A_q^{-1/2}h\) in the spatial \(H_0^1\) form domain. For almost every fixed heading, \(f\) is constant on almost every line segment of \(G\) parallel to that heading. Every such component is bounded and its zero-extended \(H^1\) representative has zero trace at both ends, so it vanishes. Hence \(f=0\), and injectivity of \(A_q^{-1/2}\) gives \(h=0\). Thus \(\ker K_q=\ker C_q=\{0\}\), whence \(\nu_q(\{0\})=0\). Moreover \(\|z_q\|>0\), so \(\nu_q((0,\infty))=F_q(0)>0\).

**4. Global strict derivative signs and high-speed limit.** The spectral support is bounded by \(\|K_q\|^2\). Dominated differentiation of the integral for every integer \(n\ge1\) gives the exact derivative formula. Strict positivity follows from its strictly positive integrand on the support of the nonzero measure, with no atom at zero. The dominated-convergence theorem yields \(F_q(v)\to0\) as \(v\to\infty\). For \(q=0\), Markov's inequality then gives \(\Pr(\tau_v>\varepsilon)\le F_0(v)/\varepsilon\to0\) for each \(\varepsilon>0\).

For \(q>0\), the elementary identity \(\mathbb E[e^{-q\tau_v}]=1-qF_q(v)\) translates strict decrease of discounted survival into strict increase of the first-passage Laplace transform; hence all-speed Laplace ordering.

**5. Reciprocal concavity and the all-speed lower envelope.** Put \(f_q(s)=F_q(\sqrt s)\). Positivity and Cauchy–Schwarz in \(L^2(\nu_q)\) imply
\[
 (-f_q'(s))^2\le f_q(s)\,\frac{f_q''(s)}2.
\]
Therefore \((1/f_q)''=(2(f_q')^2-f_q f_q'')/f_q^3\le0\), while \((1/f_q)'=-f_q'/f_q^2>0\). Finally, normalize \(\nu_q\) by its total mass and apply Jensen's inequality to the convex function \(\lambda\mapsto(1+s\lambda)^{-1}\). Its mean spectral parameter is
\(\int\lambda\,\nu_q(d\lambda)/F_q(0)=\chi_q/F_q(0)\), yielding the rational lower envelope for every \(s\ge0\). The envelope matches the exact value and its first squared-speed derivative at \(s=0\).

**6. Independent small-speed normalization.** For \(D_R=0\), a one-dimensional analogue on \((-L,L)\), with fixed longitudinal velocity \(b\) and uniform spatial start, has the exact mean
\[
 \overline T(b)=\frac Lb\coth\left(\frac{bL}{D}\right)-\frac D{b^2}
 =\frac{L^2}{3D}-\frac{b^2L^4}{45D^3}+O(b^4).
\]
Taking \(b=v\cos\theta\) and averaging over a uniform planar heading gives the coefficient \(-L^4/(90D^3)\), which also follows from the operator formula \(-\|K_0z_0\|^2\). The interval is a one-dimensional consistency check, not a substitute for the planar theorem.

## Verification

The standalone `verify.py` can be run with Python 3, NumPy, SciPy and mpmath. It creates symmetric Dirichlet diffusion matrices plus exactly skew discrete propulsion matrices at two rotational-diffusion values and three independent exponential-discount rates. For seven propulsion speeds in each setting, it compares the nonsymmetric resolvent against the symmetric Stieltjes resolvent, checks strict derivative signs through order five, and verifies reciprocal concavity. As a separate model-specific normalization, it integrates the exact one-dimensional fixed-drift exit-time formula over uniform headings and checks its quadratic speed coefficient. An actual run reported **`PASS: 415 deterministic assertions`**.

The checks are finite dimensional or numerical. They neither establish the infinite-dimensional spectral representation nor prove strict positivity for infinitely many derivatives. Those conclusions are supplied by steps 1–5, including the nonstandard kernel argument.

## Relationship to prior work

Di Trapani, Franosch and Caraglio [1] derive a full time-dependent propagator and first-passage distribution for a **disk** using a spectral expansion. Their model is a natural starting point, but the inspected model, result and conclusion sections do not state an all-domain, every-discount, all-speed Laplace ordering or a strictly positive Stieltjes measure in squared speed. The propagator in principle determines the distributions; the new claim is an analytic global *ordering* and all-derivative *shape* property, not the existence of a propagator.

Marcotte, Doering, Thiffeault and Young [2] investigate integrated exit times for diffusion under incompressible advection and optimize flow fields. Their passive-flow energy comparison is an important antecedent to the skew-adjoint step. The inspected analysis does not state the all-speed discounted active-particle Laplace ordering or strict Stieltjes hierarchy. The known zero-speed upper bound is strictly weaker than a pairwise comparison between any two nonzero speeds.

Iyaniwura and Peng [3] derive active-Brownian mean-exit equations and demonstrate that some **fixed-start** mean times can increase with speed. Their pointwise behavior is compatible with the theorem, which requires uniform spatial and angular starting data. Published analyses of weak-activity susceptibility and of weak-swimming chirality response additionally establish small-propulsion or frequency derivatives, not these global discounted-speed derivatives. Avellaneda and Vergassola [4] and Pavliotis [5] use related antisymmetric resolvent and Stieltjes tools for **effective diffusivity**; those papers are credited for the general spectral technique, not claimed as directly new here.

No matching all-speed discounted first-passage ordering was identified in the comparisons performed, but negative searches do not certify publication priority. The possibility that a broader known antisymmetric-resolvent result implicitly implies this specialization is explicitly retained as a risk.

## Limitations

The theorem is for *complete* spatial absorption, uniformly sampled initial position and heading, constant propulsion magnitude and independent achiral angular diffusion. It does not imply first-order stochastic ordering, any particular tail decay, or local mean-time monotonicity. It is not asserted for reflecting or partially reactive boundaries, position-dependent torques, chirality, spatially variable swimming speed, or nonuniform release. The spectral technique is classical; scientific novelty is restricted to the all-speed discounted first-passage comparison and its strict global consequences for this model. Independent mathematical validation and definitive publication-priority assessment have not been performed.

## References

1. F. Di Trapani, T. Franosch and M. Caraglio, *Active Brownian Particles in a Circular Disk with an Absorbing Boundary* (arXiv:2306.12702v1, 22 June 2023), https://arxiv.org/html/2306.12702v1; Phys. Rev. E 107, 064123 (2023).
2. F. Marcotte, C. R. Doering, J.-L. Thiffeault and W. R. Young, *Optimal Heat Transfer and Optimal Exit Times* (arXiv:1710.00646v1, 2 October 2017), https://arxiv.org/abs/1710.00646.
3. S. A. Iyaniwura and Z. Peng, *Mean First Passage Time of Active Brownian Particles in Two Dimensions* (arXiv:2506.15813v1, 18 June 2025), https://arxiv.org/html/2506.15813v1.
4. M. Avellaneda and M. Vergassola, *Stieltjes Integral Representation of Effective Diffusivities in Time-Dependent Flows*, Phys. Rev. E 52, 3249 (1995), https://doi.org/10.1103/PhysRevE.52.3249.
5. G. A. Pavliotis, *Asymptotic Analysis of the Green–Kubo Formula* (arXiv:1002.4103, 22 February 2010), https://arxiv.org/abs/1002.4103.
6. G. Iyer, A. Novikov, L. Ryzhik and A. Zlatoš, *Exit Times of Diffusions with Incompressible Drift*, SIAM J. Math. Anal. 42 (2010), https://doi.org/10.1137/090776895.
