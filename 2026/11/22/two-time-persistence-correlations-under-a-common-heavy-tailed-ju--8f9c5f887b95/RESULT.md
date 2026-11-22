# Two-time persistence correlations under a common heavy-tailed jump-rate clock

## Finding

Consider two distinct independent nearest-neighbour continuous-time symmetric walks on the nonnegative integers, each absorbed on reaching zero, but both using the **same** time-dependent, nonnegative total jump rate. The two underlying unit-rate walks and their jumps are independent conditional on that rate history. Let their positive integer initial positions be \(x_1,x_2\), their absorption times be \(T_1,T_2\), and their common rate be independently resampled every fixed interval \(\tau>0\), with rate \(\Lambda\) satisfying
\[
\mathbb E e^{-u\Lambda}=\frac{1}{1+u^\alpha},\qquad 0<\alpha\le1.
\]

For every fixed observation-time ratio \(c\ge1\), as \(t\to\infty\),
\[
\Pr(T_1>t,\ T_2>ct)
\sim\frac{2x_1x_2}{\pi}\tau^{1/\alpha-1}
J_\alpha(c)t^{-1/\alpha},
\]
where \(J_\alpha(c)=\mathbb E[S_1^{-1/2}S_c^{-1/2}]\) for the standard positive \(\alpha\)-stable subordinator \(S\), defined by \(\mathbb E e^{-uS_v}=e^{-vu^\alpha}\). It has the explicit convergent one-dimensional representation
\[
J_\alpha(c)=\frac{\Gamma(1/\alpha)}{\pi\alpha}\,
2\int_0^{\pi/2}\left[1+(c-1)\cos^{2\alpha}\theta\right]^{-1/\alpha}\,d\theta.
\]
At \(\alpha=1\), interpret the limiting subordinator as the deterministic clock \(S_v=v\).

For comparison, give the second walker an **independent** rate history of the same law. Each one-walker survival probability remains identical, but the large-time joint-survival ratio of the common-clock model to this independent-clock comparator is
\[
\boxed{R_\alpha(c)=\frac{\alpha\Gamma(1/\alpha)}{\Gamma(1/(2\alpha))^2}
 c^{1/(2\alpha)}\,2\int_0^{\pi/2}
 [1+(c-1)\cos^{2\alpha}\theta]^{-1/\alpha}\,d\theta.}
\]
For \(0<\alpha<1\), \(R_\alpha(c)>1\) for every finite \(c\ge1\), and \(\lim_{c\to\infty}R_\alpha(c)=1\). For \(\alpha=1\), \(R_1(c)=1\) for every \(c\ge1\). At the half-stable index, two distinct, physically observable time ratios give the exact values
\[
R_{1/2}(1)=\frac\pi2,\qquad \boxed{R_{1/2}(2)=\frac43}.
\]
The new result is the **unequal-time** profile \(c>1\), including its exact double-time constant, not the already-known equal-time value.

## Assumptions and scope

The lattice is \(\mathbb Z_{\ge0}\), with zero absorbing. Each underlying operational-time process jumps right or left at equal probability, with unit **total** jump rate; thus the operational-time variance is one per unit time. The actual physical-time rate is common and piecewise constant, independently redrawn every \(\tau\). The conditional jump noises of the two walks are independent, including across observation times. The first event is \(\{T_1>t\}\), and the second is \(\{T_2>ct\}\), **not** a two-time survival event for one walker. The parameter \(c\) is fixed as \(t\to\infty\), and \(x_1,x_2,\tau\) do not scale with time. No statement is made for \(c\) growing with \(t\), for correlated conditional jump noises, or for deterministic-rate comparisons with different marginal laws.

## Proof

**1. Time-change representation and operational survival.** Put \(A_t=\int_0^t\Lambda_s\,ds\). Conditional on the common rate history, each walk is a standard rate-one killed symmetric continuous-time walk observed at operational time \(A_t\), independently of the other. Denote its survival function by \(q_x(a)\). The standard reflection/spectral representation or the continuous-time local central limit theorem gives, for each fixed integer \(x\ge1\),
\[
q_x(a)\sim x\sqrt{\frac{2}{\pi a}}\quad(a\to\infty),
\qquad 0\le q_x(a)\le C_x\min(1,a^{-1/2}).
\]
Consequently \(\Pr(T_1>t,T_2>ct)=\mathbb E[q_{x_1}(A_t)q_{x_2}(A_{ct})]\).

**2. Joint stable-clock limit and justified moment passage.** Put \(b_t=\tau^{1-1/\alpha}t^{1/\alpha}\). The exact rate Laplace transform and independence of different refresh periods imply, for \(u,v\ge0\),
\[
\lim_{t\to\infty}\mathbb E\exp\left(-\frac{uA_t+vA_{ct}}{b_t}\right)
=\exp\bigl(-(u+v)^\alpha-(c-1)v^\alpha\bigr).
\]
This is the joint Laplace transform of \((S_1,S_c)\). Fractional final refresh intervals have vanishing normalized contributions; when \(\alpha=1\), the law of large numbers gives \((1,c)\).

Moment convergence is essential, rather than an unjustified invocation of weak convergence. For every \(p>0\) and all sufficiently large \(t\), the negative moment \(\mathbb E[(A_t/b_t)^{-p}]\) is uniformly bounded. Indeed use
\[
\mathbb E[(A_t/b_t)^{-p}]=\frac{1}{\Gamma(p)}\int_0^\infty u^{p-1}\mathbb E e^{-uA_t/b_t}\,du;
\]
for complete refresh intervals the Laplace transform is \([1+(u\tau/b_t)^\alpha]^{-\lfloor t/\tau\rfloor}\), with bounded integral converging to \(\Gamma(p/\alpha)/(\alpha\Gamma(p))\). In particular, for a fixed \(\delta>0\), the product bound \(A_{ct}\ge A_t\) and \(q_{x_1}(A_t)q_{x_2}(A_{ct})\le C(A_t)^{-1}\) give uniform integrability of \(b_tq_{x_1}(A_t)q_{x_2}(A_{ct})\). Therefore
\[
\lim_{t\to\infty}b_t\Pr(T_1>t,T_2>ct)
=\frac{2x_1x_2}{\pi}\mathbb E[S_1^{-1/2}S_c^{-1/2}].
\]
The same argument gives the marginal \(\Pr(T_i>t)\sim x_i\sqrt{2/\pi}\,b_t^{-1/2}M_\alpha(1/2)\), where
\[
M_\alpha(p)=\mathbb E S_1^{-p}=\frac{\Gamma(p/\alpha)}{\alpha\Gamma(p)}.
\]

**3. The mixed moment is a single integral.** For \(0<\alpha\le1\), Mellin's integral applied to both negative half-powers yields
\[
J_\alpha(c)=\frac1\pi\int_0^\infty\!\int_0^\infty
\frac{\exp[-(u+v)^\alpha-(c-1)v^\alpha]}{\sqrt{uv}}\,du\,dv.
\]
Substitute \(u=wv\), integrate the radial variable \(v\), and use \(w=\tan^2\theta\) to obtain precisely the displayed angular integral. The integrals are absolutely convergent and positive. Dividing by the independent-clock marginal product, which has negative-moment constant \(M_\alpha(1/2)^2c^{-1/(2\alpha)}\), gives \(R_\alpha(c)\).

**4. Strict enhancement, decorrelation, and two exact constants.** When \(0<\alpha<1\), the random variable \(S_1\) is nondegenerate, and \(S_c=S_1+Z\) with \(Z\ge0\) independent of \(S_1\). Both \(s\mapsto s^{-1/2}\) and \(s\mapsto\mathbb E[(s+Z)^{-1/2}]\) decrease strictly. Their covariance is therefore strictly positive (apply the independent-copy identity for covariance). This proves \(R_\alpha(c)>1\). For \(c\to\infty\), the normalized clock \(S_c/c^{1/\alpha}\) converges jointly with \(S_1\) to an **independent** copy of \(S_1\). The previous negative-moment bound and the independent increment \(S_c-S_1\) justify uniform integrability; the ratio tends to one. For \(\alpha=1\), \(S_c=c\) deterministically, proving exact equality.

For \(c=1\), the angular integral is \(\pi\). For \(\alpha=1/2,c=2\), its integrand becomes \(2/(1+\cos\theta)^2\), and the tangent half-angle substitution evaluates it to \(4/3\). Since \(\frac{\alpha\Gamma(1/\alpha)}{\Gamma(1/(2\alpha))^2}c^{1/(2\alpha)}=1\) at these parameters, \(R_{1/2}(2)=4/3\).

## Verification

The independent standard-library program `CHECK.py` numerically integrates the angular kernel, verifies the exact values at \(c=1,2\) for \(\alpha=1/2\), verifies deterministic-clock normalization at \(\alpha=1\), and checks representative positive enhancements. Run `python3 CHECK.py` in the same directory. This numerical program checks formula consistency; the infinite-time limits, strict inequalities, and exact constants rely on the analytical argument above.

## Relationship to prior work

Levit and Reuveni (2026, arXiv:2609.26925) prove the one-walker first-passage transition and tail asymptotics for the same independently refreshed Mittag-Leffler rate law. Arutkin and Reuveni (2023, arXiv:2302.07041) introduce the doubly stochastic continuous-time random walk and the integrated-rate representation. An equal-time multiwalker shared-clock survival law, including the \(\pi/2\) enhancement at \(\alpha=1/2\), is also prior to this calculation. Those results do not state the **asynchronous observation** survival profile, its full one-dimensional integral, or the exact \(4/3\) double-time ratio, which depend on a genuinely joint two-time stable-clock transform. The negative-power moment identity itself is standard and is not claimed as new.

## Limitations

This is an asymptotic claim for fixed time ratio and fixed starting positions, not an exact finite-time ratio or a universal comparison among different models. The asymptotic clock laws allow infinite-mean rates when \(\alpha<1\). Positivity is shown for every finite \(c\), but no monotonicity of \(R_\alpha(c)\) in \(c\) is asserted. Previously unindexed work on multitime stable-subordinator moments might imply the closed-form integral; that publication-priority uncertainty remains. No independent external audit is claimed.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925 (first posted September 22, 2026), https://arxiv.org/abs/2609.26925.
2. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, arXiv:2302.07041 (first posted February 14, 2023), https://arxiv.org/abs/2302.07041.
3. Standard positive-stable subordinator and Mellin–Laplace fractional moment identities, used in the proof with their derivation spelled out above.
