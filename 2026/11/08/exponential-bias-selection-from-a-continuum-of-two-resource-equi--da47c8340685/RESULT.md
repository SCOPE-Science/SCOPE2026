# Exponential bias selection from a continuum of two-resource equilibria

## Finding

Consider the unit-mass nonatomic population game specified below, with two resources and a unit-strength *popularity subsidy*. For every positive logit-noise level \(\sigma>0\) and cost offset \(\delta\in(-1,1)\), its noisy equilibrium has a **unique** first-resource mass \(q_\sigma(\delta)\), explicitly

\[
\boxed{q_\sigma(\delta)=\frac12+\frac\delta4-
\frac\sigma2\operatorname{arsinh}\!\left(e^{1/\sigma}\sinh\frac\delta{2\sigma}\right).}
\]

At \(\delta=0\), this mass equals \(1/2\) for every \(\sigma>0\), yet the zero-noise, zero-offset game has an entire continuum of pure Nash equilibria, indexed by every first-resource mass in \([0,1]\). In the joint limit with \(\delta_\sigma\to0\) of one eventually fixed nonzero sign and

\[
-\sigma\log |\delta_\sigma|\longrightarrow\alpha\in[0,+\infty],
\]

the first-resource mass has the sharp **exponential-bias selection law**

\[
\boxed{\lim_{\sigma\downarrow0}q_\sigma(\delta_\sigma)
=\begin{cases}
\tfrac12\min\{\alpha,1\},&\delta_\sigma>0,\\
1-\tfrac12\min\{\alpha,1\},&\delta_\sigma<0.
\end{cases}}
\]

In particular, every equilibrium mass \(s\in[0,1]\) of the unperturbed pure game is selectable by a sequence of offsets tending to zero. With the concrete positive offset \(\delta_\sigma=e^{-\alpha/\sigma}\), for fixed \(0<\alpha\le1\) the sharper expansion holds:

\[
q_\sigma(\delta_\sigma)=\frac\alpha2+\frac\sigma2\log\sigma+o(\sigma).
\]

For fixed \(\alpha>1\), the central selection has exponentially small displacement:

\[
q_\sigma(e^{-\alpha/\sigma})=\frac12-
\frac14e^{-(\alpha-1)/\sigma}(1+o(1)).
\]

## Assumptions and scope

The players have characteristics \(x\in[0,1]\) distributed uniformly with Lebesgue mass one, and choose one of two resources. Write \(q\) for the mass choosing resource 1. After an immaterial common baseline shift, individual costs are

\[
C_1(x;q,\delta)=1+x+\delta-q,\qquad
C_2(x;q)=1-x+q.
\]

Thus \(C_1-C_2=2(x-q)+\delta\). These costs arise from base costs \(1+x+\delta\), \(2-x\), and congestion interactions \(-q\), \(-(1-q)\). The interactions model affinity rather than standard repulsive congestion. We take \(\delta\in(-1,1)\) to keep nonnegative base costs, and independent Gumbel choice shocks with positive scale \(\sigma\). The resulting conditional probability of selecting resource 1 is

\[
p_\sigma(x;q,\delta)=\frac{1}{1+\exp((2(x-q)+\delta)/\sigma)}.
\]

A noisy equilibrium is a measurable mixed allocation with \(q=\int_0^1p_\sigma(x;q,\delta)\,dx\). At \(\sigma=0\), a pure equilibrium assigns almost every characteristic to its cheaper resource. Endpoints and ties concern Lebesgue-null sets only. The formula refers to these fixed-point equilibria, not to a stochastic finite-player evolutionary chain.

## Proof

**1. Existence and uniqueness for positive noise.** Put

\[
F_{\sigma,\delta}(q)=\int_0^1p_\sigma(x;q,\delta)\,dx.
\]

The integral lies strictly between zero and one. Differentiating under the integral and integrating the derivative in \(x\) gives

\[
F'_{\sigma,\delta}(q)
=p_\sigma(0;q,\delta)-p_\sigma(1;q,\delta)\in(0,1).
\]

Therefore \(F_{\sigma,\delta}(q)-q\) decreases strictly, with opposite signs at \(q=0\) and \(q=1\); exactly one noisy equilibrium exists. Symmetry under exchange of resources gives \(q_\sigma(-\delta)=1-q_\sigma(\delta)\).

**2. Exact closed form.** Direct integration yields

\[
F_{\sigma,\delta}(q)=\frac\sigma2
\log\frac{1+\exp((2q-\delta)/\sigma)}
{1+\exp((2q-\delta-2)/\sigma)}.
\]

Set \(z=\exp(2q/\sigma)\), \(r=\exp(\delta/\sigma)\), and \(a=\exp(-2/\sigma)\). Exponentiating the fixed-point equation gives the quadratic

\[
az^2+(r-1)z-r=0.
\]

Its unique positive root can be parametrized by

\[
z=\exp\!\left(\frac1\sigma+\frac\delta{2\sigma}+u\right),
\quad
\sinh u=-e^{1/\sigma}\sinh\!\left(\frac\delta{2\sigma}\right).
\]

Solving for \(u\) proves the displayed \(\operatorname{arsinh}\) formula. No asymptotic approximation is involved in this identity.

**3. Pure equilibria at zero noise and zero bias.** If resource 1 has mass \(s\), its cost is no greater precisely for \(x\le s\). Therefore the partition \([0,s]\) to resource 1 and \((s,1]\) to resource 2 is self-consistent for every \(s\in[0,1]\). Conversely any pure Nash allocation coincides almost everywhere with this threshold allocation for its own mass, so these are *all* pure equilibria.

**4. Singular joint limit.** For positive \(\delta_\sigma\to0\), put \(t_\sigma=\delta_\sigma/(2\sigma)>0\). The exact identity reads

\[
q_\sigma(\delta_\sigma)
=\frac12+\frac{\delta_\sigma}4
-\frac\sigma2\operatorname{arsinh}\left(e^{1/\sigma}\sinh t_\sigma\right).
\]

If \(-\sigma\log\delta_\sigma\to\alpha\in[0,+\infty]\), then

\[
\sigma\log\sinh t_\sigma\longrightarrow-\alpha
\]

in the extended real sense. Indeed, if \(t_\sigma\le1\), use \(t\le\sinh t\le t\sinh(1)\) and \(\sigma\log\sigma\to0\); if \(t_\sigma>1\), then \(\sigma\log\sinh t_\sigma=\delta_\sigma/2+O(\sigma)\to0\), which can occur only with \(\alpha=0\). As \(\operatorname{arsinh}(u)=\log(u+\sqrt{1+u^2})\) for \(u>0\), one has

\[
\sigma\operatorname{arsinh}\left(e^{1/\sigma}\sinh t_\sigma\right)
\longrightarrow\max\{1-\alpha,0\}.
\]

For \(\alpha=+\infty\), this follows using the same expression and the bound \(\operatorname{arsinh}(u)\le u\). Substitution proves the positive-offset limit. Reflection gives the negative-offset limit.

For \(\delta_\sigma=e^{-\alpha/\sigma}\) with \(0<\alpha\le1\), the argument of \(\operatorname{arsinh}\) tends to infinity and equals \(e^{(1-\alpha)/\sigma}(1+o(1))/(2\sigma)\). Thus its inverse hyperbolic sine is \((1-\alpha)/\sigma-\log\sigma+o(1)\); this gives the stated second-order term. For \(\alpha>1\), the argument tends to zero and is \(e^{-(\alpha-1)/\sigma}(1+o(1))/(2\sigma)\), giving the exponentially small displacement.

**5. Complete attainability.** To obtain a target \(s\in(0,1/2)\), choose \(\delta_\sigma=e^{-2s/\sigma}\); for \(s\in(1/2,1)\), choose \(\delta_\sigma=-e^{-2(1-s)/\sigma}\). Choose \(\delta_\sigma=\sqrt\sigma\) or \(-\sqrt\sigma\) for the endpoints \(s=0\) or \(s=1\), and choose zero bias for \(s=1/2\). These offsets tend to zero, and the selection law gives the desired limits. This completes the proof.

## Verification

The included `verification.py` uses the Python standard library and has been executed successfully. It compares twenty exact-form equilibria against independent bisection of the integrated fixed-point balance, nine directly numerically integrated logit fixed points, and nine small-noise/reflection and second-order checks. The output ends in `ALL CHECKS PASS`. These finite checks detect transcription and numerical mistakes but do not establish the asymptotic assertions; the preceding argument supplies that proof.

## Relationship to prior work

Dupont, Petit and Séguret (2026), Remark 2.3, present the unbiased unit-strength affinity game as an example with infinitely many pure equilibria, and their equation (3.12) provides the Gumbel logit response. Their general uniqueness theorem assumes nondecreasing congestion interactions, whereas the present affinity interaction is decreasing, and they do not derive the explicit noisy-equilibrium curve or the joint exponential-bias selection law. Standard logit-equilibrium research studies noisy choice and equilibrium selection, but the result here concerns this exact continuum equilibrium set under *jointly vanishing deterministic asymmetry and noise*, including the exponential scale that selects every threshold.

## Limitations

The result is exact for the specified uniform nonatomic two-resource affinity game. It does not assert an equilibrium-selection law for arbitrary cost densities, more resources, repulsive congestion, non-Gumbel shocks, finite strategic populations, or dynamic adjustment. The fixed-point formula assumes the positive-noise logit model. Literature searches cannot rule out unindexed equivalent results; the comparison with some broader equilibrium-selection papers is limited by access to abstracts or inaccessible full texts.

## References

1. A. Dupont, Q. Petit and A. Séguret, *Non-Potential Congestion Games with a Continuum of Players*, arXiv:2610.18035v1, first public October 13, 2026. https://arxiv.org/abs/2610.18035 . Relevant: Remark 2.3, equation (3.12), Theorem 2.1.
2. S. P. Anderson, J. K. Goeree and C. A. Holt, *The Logit Equilibrium: A Perspective on Intuitive Behavioral Anomalies*, Southern Economic Journal 69 (2002), 21–47. https://doi.org/10.1002/j.2325-8012.2002.tb00476.x . General logit-equilibrium background.
3. H. Carlsson and M. Ganslandt, *Noisy Equilibrium Selection in Coordination Games*, Economics Letters 60 (1998), 23–34. https://ideas.repec.org/a/eee/ecolet/v60y1998i1p23-34.html . Context for noise-proof selection among a continuum of equilibria.
4. R. Lahkar, S. Mukherjee and S. Roy, *Equilibrium Selection via Stochastic Evolution in Continuum Potential Games*, discussion paper (2023), revised preprint (2024). https://www.ashoka.edu.in/research/equilibrium-selection-via-stochasticevolution-in-continuum-potential-games/ . A different stochastic-evolution selection framework.
