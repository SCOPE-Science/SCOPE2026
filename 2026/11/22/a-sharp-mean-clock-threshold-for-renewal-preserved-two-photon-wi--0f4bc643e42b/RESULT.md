# A sharp mean-clock threshold for renewal-preserved two-photon Wigner negativity

## Finding

For a lossy optical mode independently re-prepared in the two-photon state at arbitrary positive, independent, identically distributed renewal times, the stationary phase-averaged Wigner function can be negative **for some renewal law of a given mean** if and only if the dimensionless mean re-preparation interval is smaller than a universal constant. The unique maximizing feasibility protocol is a deterministic interval, understood with equilibrium-renewal (uniform-phase) sampling. Specifically, set
\[
\mu=\gamma\mathbb ET,\qquad
\varphi(t)=\frac{2(1-e^{-t})(1+e^{-2t})}{1+e^{-t}}.
\]
There exists exactly one positive \(\mu_\star\) such that \(\mu_\star=\varphi(\mu_\star)\), and
\[
\mu_\star=1.130359548845188\ldots.
\]
For **all** positive finite-mean renewal waiting laws, the stationary Wigner function is everywhere nonnegative whenever \(\mu\ge\mu_\star\). For each \(0<\mu<\mu_\star\), a deterministic wait \(T=\mu/\gamma\) produces a strictly Wigner-negative annulus. At fixed \(\mu\), the deterministic wait uniquely maximizes the exact Wigner-negativity feasibility witness defined in the proof. This last extremality is for that witness and the existence of Wigner negativity, not an assertion about integrated Wigner negative volume or a pointwise ordering of entire Wigner functions.

## Assumptions and scope

Consider one zero-temperature bosonic mode, subject between re-preparation events to the normalized single-photon attenuation Lindbladian
\[
\dot\rho=\gamma\left(a\rho a^\dagger-\tfrac12\{a^\dagger a,\rho\}\right),\qquad\gamma>0.
\]
At independent renewal times, the complete density matrix is instantaneously re-prepared as \(\lvert2\rangle\langle2\rvert\), regardless of its previous state. Waiting times \(T_1,T_2,\ldots\) are independent, identically distributed, strictly positive almost surely, independent of loss noise, and have \(0<\mathbb ET<\infty\). The stationary state is defined by observing the equilibrium-renewal process at a random time, not by sampling always immediately before a synchronized periodic pulse. Consequently deterministic cycles are sampled with uniformly random phase. There are no imperfect preparations, thermal photons, multiphoton loss or preparation-time costs in the model.

Write \(u=|\alpha|^2\) for the squared radial phase-space coordinate; the Wigner normalization is \(W(\alpha)=(2/\pi)e^{-2u}P(u)\). Define
\[
A=\mathbb E(1-e^{-\gamma T}),\quad
B=\mathbb E(1-e^{-2\gamma T}),\quad
\Phi(A,B)=\frac{4A^2}{B}-4A+2B.
\]
All expressions are finite and \(0<A<B<2A\).

## Proof

**1. Renewal occupation and attenuated photon populations.** Let \(L\) be the age since the most recent preparation under the equilibrium-renewal law. Renewal reward gives
\[
\mathbb Ef(L)=\frac{\mathbb E\int_0^T f(t)\,dt}{\mathbb ET}.
\]
For \(k=1,2\), \(m_k=\mathbb E e^{-k\gamma L}=(1-\mathbb E e^{-k\gamma T})/(k\mu)\); hence \(m_1=A/\mu\), \(m_2=B/(2\mu)\). During a loss-only interval of age \(t\), setting \(\eta=e^{-\gamma t}\), the number-state probabilities are \((p_0,p_1,p_2)=((1-\eta)^2,2\eta(1-\eta),\eta^2)\). Thus the stationary density matrix is diagonal, with
\[
\bar p_0=1-2m_1+m_2,\qquad\bar p_1=2m_1-2m_2,\qquad\bar p_2=m_2.
\]

**2. Exact Wigner condition and annulus.** The Laguerre formula \(W_{|n\rangle}(\alpha)=(2/\pi)e^{-2u}(-1)^nL_n(4u)\) gives
\[
P(u)=1+(8u-4)m_1+(8u^2-16u+4)m_2.
\]
Because \(B>A>0\), its vertex \(u_*=1-A/B\) belongs to \((0,1/2)\), and completing the square yields
\[
\boxed{\min_{u\ge0}P(u)=P(u_*)=1-\frac{\Phi(A,B)}{\mu}.}
\]
Therefore \(W\) is negative somewhere exactly when \(\Phi(A,B)>\mu\). Moreover \(P(0)=\mathbb E(1-2e^{-\gamma L})^2>0\), while \(P(u)\to\infty\) for \(u\to\infty\). Its negative set, when present, is exactly a single open annulus, bounded by the two strictly positive roots of \(P\).

**3. Sharp extremality for every renewal law.** The map \(\Phi(A,B)=4A^2/B-4A+2B\) is convex for \(B>0\), since the quadratic-over-linear term is convex; explicitly its Hessian is
\[
\nabla^2\Phi=\frac8B
\begin{pmatrix}1&-A/B\\-A/B&(A/B)^2\end{pmatrix}\succeq0.
\]
Thus Jensen's inequality followed by the substitution \(z=e^{-t}\) gives
\[
\Phi(A,B)\le\mathbb E\Phi(1-e^{-\gamma T},1-e^{-2\gamma T})
=\mathbb E\varphi(\gamma T).
\]
The function \(\varphi\) is strictly concave on \((0,\infty)\). Indeed, with \(z=e^{-t}\in(0,1)\),
\[
\varphi''(t)=\frac{-4z}{(1+z)^3}\left(2z^4+5z^3+3z^2-3z+1\right)<0,
\]
where the bracket is strictly positive because \(3z^2-3z+1=3(z-1/2)^2+1/4>0\). A second Jensen inequality proves the **sharp universal bound**
\[
\boxed{\Phi(A,B)\le\mathbb E\varphi(\gamma T)\le\varphi(\mu).}
\]
The final inequality is strict for every non-deterministic positive waiting law by strict concavity, while all equalities hold for the deterministic law \(T=\mu/\gamma\). Hence deterministic re-preparation is the unique maximizer of \(\Phi\) at fixed mean, which is exactly the Wigner-negativity existence witness in step 2.

**4. Universal threshold.** We have \(\varphi(0)=0\), \(\varphi'(0^+)=2\), and \(\varphi(t)\to2\) as \(t\to\infty\). Strict concavity implies that \(\varphi(t)/t\) is strictly decreasing from 2 to 0. Therefore a unique \(\mu_\star>0\) solves \(\varphi(\mu_\star)=\mu_\star\). The sharp bound in step 3 shows that no renewal law of mean \(\mu\ge\mu_\star\) produces Wigner negativity. For every smaller mean, the deterministic law attains \(\Phi=\varphi(\mu)>\mu\), producing a negative annulus. At equality the deterministic Wigner polynomial has a single double zero at positive radius and every non-deterministic clock has a strictly positive polynomial minimum.

For deterministic \(T=\mu/\gamma\), the annulus has squared-radius center \(u_*=e^{-\mu}/(1+e^{-\mu})\) and endpoints
\[
u_\pm=u_*\pm\sqrt{\frac{\varphi(\mu)-\mu}{4(1-e^{-2\mu})}},
\]
whenever \(0<\mu<\mu_\star\).

## Verification

The standalone `verify.py` recomputes the nontrivial algebra in SymPy, derives the concavity expression, checks the Hessian and Poisson special case, independently integrates the equilibrium-age Wigner polynomial for randomized finite-support renewal laws, checks the universal bound and annulus conditions, and solves the unique threshold numerically. Running `python verify.py` produced `PASS: 1983 algebraic and numerical checks; threshold=1.130359548845188; period-0.9 example verified`. These finite checks corroborate the closed analytic argument rather than substituting for the all-clock proof.

As one concrete comparison, take \(\gamma=1\) and common mean \(\mathbb ET=0.9\). Deterministic waits have \(P(u_*)\approx-0.0925298706\), while exponential waits with the same mean have \(P(u_*)\approx0.1254451919\); the former stationary Wigner density is negative on an annulus, the latter is nonnegative everywhere. The known exponential-clock two-photon threshold corresponds to \(r/\gamma\) satisfying \(r^3/\gamma^3-r/\gamma-2=0\), or mean \(\gamma\mathbb ET\approx0.6572981061\), which is strictly below the optimal deterministic mean threshold.

## Relationship to prior work

Chabaud, Emeriau and Grosshans establish operational witnesses for Wigner negativity, not renewal-clock feasibility thresholds. Malpani and collaborators derive photon-loss evolution and convolution of Wigner functions for related photon-added Fock states, without optimizing renewal re-preparation intervals. Liu develops general semi-Markov quantum resetting counting-statistics machinery, but does not classify Wigner negativity for an attenuating two-photon mode with fixed mean re-preparation time. Li and collaborators provide physically relevant Fock-state stabilization and Wigner tomography using cascaded autonomous photon addition, a different restoration mechanism. The two-photon **Poisson** threshold is also stated in [*Parity-dependent Wigner negativity threshold under Poisson Fock-state resets*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-parity-dependent-wigner-negativity-threshold-under-poisson-fock--66df55b3ec78/RESULT.md); the exponential specialization here reproduces it and is not claimed as new. The contribution here is the strict convexity–concavity inequality over *all* positive finite-mean renewal laws and the resulting sharp fixed-mean feasibility boundary.

## Limitations

The theorem addresses the sign of the equilibrium phase-averaged stationary Wigner density, not mean photon count, nonclassical depth, integrated negative volume, a time-resolved Floquet phase, physical apparatus constraints or optimal nonideal correction. Its deterministic-clock extremality does not imply pointwise Wigner ordering or maximization of integrated negativity. No claim is made for multiphoton starting states beyond exactly two photons, finite-temperature loss, partial resetting, or arbitrary correlated reset clocks. A broad existing mathematical result on optimization of renewal mixtures could potentially imply the convexity–concavity step; publication-priority uniqueness is not independently certified.

## References

1. U. Chabaud, P.-E. Emeriau and F. Grosshans, *Witnessing Wigner Negativity*, first public 2021-02-11, https://arxiv.org/abs/2102.06193.
2. P. Malpani, K. Thapliyal, J. Banerji and A. Pathak, *Enhancement of non-Gaussianity and nonclassicality of photon added displaced Fock state: A quantitative approach*, first public 2021-09-24, https://arxiv.org/abs/2109.12145.
3. F. Liu, *Semi-Markov Processes in Open Quantum Systems. II. Counting Statistics with Resetting*, first public 2023-08-04, https://arxiv.org/abs/2308.02214.
4. S. Li et al., *Autonomous Stabilization of Fock States in an Oscillator against Multiphoton Losses*, first public 2023-08-16, https://arxiv.org/abs/2308.08296.
