# A unique Poisson–periodic crossover for memory-dependent wildlife disturbance

## Finding

**Theorem (a sharp cadence reversal and an event-burden threshold).** Fix a memory-decay rate \(\gamma>0\), response sensitivity \(\kappa>0\), and probabilities \(\alpha,\beta>0\) with \(\alpha+\beta\leq1\). Each disturbance event at time \(t\) has conditional probability
\[
q(M(t^-))=\alpha+\beta e^{-\kappa M(t^-)}
\]
of causing a flight response, where the pre-event memory is the exponentially discounted count of earlier events,
\[
M(t^-)=\sum_{s<t}e^{-\gamma(t-s)}.
\]
Compare two stationary event calendars with the *same* positive mean frequency \(\lambda\): a homogeneous Poisson process and an equally spaced deterministic process with period \(1/\lambda\) and a randomized initial phase. Let \(R_{\mathrm P}(\lambda)\) and \(R_{\mathrm D}(\lambda)\) denote their respective long-run expected numbers of responses per unit time. Put
\[
J(\kappa)=\int_0^\kappa\frac{1-e^{-u}}u\,du.
\]
Then the response rates are exactly
\[
R_{\mathrm P}(\lambda)=\lambda\bigl[\alpha+\beta e^{-\lambda J(\kappa)/\gamma}\bigr],
\qquad
R_{\mathrm D}(\lambda)=\lambda\left[\alpha+\beta\exp\!\left(-\frac{\kappa}{e^{\gamma/\lambda}-1}\right)\right].
\]
There is precisely one \(\lambda_c>0\) at which they agree. It is \(\lambda_c=\gamma/y_c\), where \(y_c\) is the unique positive solution of
\[
\frac{y_c}{e^{y_c}-1}=\frac{J(\kappa)}{\kappa}.
\]
Their strict ordering reverses exactly once:
\[
0<\lambda<\lambda_c\implies R_{\mathrm P}(\lambda)<R_{\mathrm D}(\lambda),
\qquad
\lambda>\lambda_c\implies R_{\mathrm P}(\lambda)>R_{\mathrm D}(\lambda).
\]
The crossover is independent of \(\alpha\) and \(\beta\); it decreases strictly with \(\kappa\), and satisfies
\[
\lambda_c\sim\frac{2\gamma}{\kappa}\quad(\kappa\downarrow0),
\qquad
\lambda_c\sim\frac{\gamma}{\log\kappa}\quad(\kappa\to\infty).
\]
Further, increasing the *Poisson* event frequency decreases the expected number of responses per unit time on a nonempty open frequency interval if and only if
\[
\frac{\alpha}{\beta}<e^{-2}.
\]
If this condition holds, the Poisson response rate has exactly two stationary points: first a strict local maximum and then a strict local minimum. Otherwise it is strictly increasing (at equality its derivative vanishes at one point without changing sign). In the two-extremum case, writing \(c=J(\kappa)/\gamma\), their frequencies are
\[
\frac{1-W_0(-e\alpha/\beta)}c
\quad\text{and}\quad
\frac{1-W_{-1}(-e\alpha/\beta)}c,
\]
where \(W_0\) and \(W_{-1}\) are the two real branches of Lambert's \(W\) function.

## Assumptions and scope

The same local population and same physical event type are compared at each frequency. Every event increases memory by exactly one; memory otherwise decays exponentially. The response law is a stipulated history-dependent Bernoulli probability, not an estimated biological law. Response marks do not feed back on subsequent event times or memory. The Poisson event clock is independent of the pre-event state. The deterministic calendar has a uniform random phase to be stationary, and its responses are sampled just *before* memory jumps. The infinite-past stationary memory is well-defined. Events and responses are counted per unit time, not weighted by flight duration, energy, mortality, or off-site displacement. All inequalities concern expectations, not sample-path orderings.

## Proof

**Step 1: stationary Poisson memory.** For a Poisson process of rate \(\lambda\) on the real line, the pre-event history has the same law as the process on the negative half-line seen from an independent time (the Poisson independent-increments/Palm property). It is finite almost surely because
\[
\mathbb E M(t^-)=\lambda\int_0^\infty e^{-\gamma v}\,dv=\lambda/\gamma<\infty.
\]
The established Laplace functional of a Poisson process, applied to the nonnegative exponential kernel, yields
\[
\begin{aligned}
\mathbb E e^{-\kappa M(t^-)}
&=\exp\!\left[-\lambda\int_0^\infty\bigl(1-e^{-\kappa e^{-\gamma v}}\bigr)\,dv\right]\\
&=\exp\!\left[-\frac\lambda\gamma\int_0^\kappa\frac{1-e^{-u}}u\,du\right]
=e^{-\lambda J(\kappa)/\gamma}.
\end{aligned}
\]
The Poisson compensation formula then gives the claimed long-run expected response rate. This Laplace functional is prior standard mathematics, not a newly claimed lemma.

**Step 2: periodic memory.** Immediately before each deterministic event, the infinite past contributes
\[
M_{\mathrm D}=\sum_{j=1}^\infty e^{-j\gamma/\lambda}
=\frac1{e^{\gamma/\lambda}-1}.
\]
Substituting into \(q\), then multiplying by the event rate \(\lambda\), proves the second exact response-rate expression.

**Step 3: unique reversal.** Since \(0<(1-e^{-u})/u<1\) for \(u>0\), one has \(0<J(\kappa)<\kappa\). The log ratio of the two *habituation-dependent* response terms is
\[
\log\frac{e^{-\lambda J(\kappa)/\gamma}}
{\exp(-\kappa/(e^{\gamma/\lambda}-1))}
=\frac\lambda\gamma\left[\kappa h(\gamma/\lambda)-J(\kappa)\right],
\qquad h(y)=\frac{y}{e^y-1}.
\]
For \(y>0\), the derivative of \(h\) has numerator \(e^y(1-y)-1<0\); the latter expression starts at zero and has derivative \(-ye^y<0\). Thus \(h\) is strictly decreasing from \(1\) to \(0\). As \(\lambda\) increases, \(\gamma/\lambda\) decreases, so \(h(\gamma/\lambda)\) strictly increases from zero to one, passing \(J(\kappa)/\kappa\) exactly once. The common positive multiplier \(\lambda\beta\) and common baseline \(\lambda\alpha\) preserve the resulting strict comparisons of total rates.

**Step 4: sensitivity and asymptotics.** The identity
\[
\frac{J(\kappa)}\kappa
=\int_0^1\frac{1-e^{-\kappa v}}{\kappa v}\,dv
\]
is strictly decreasing in \(\kappa\), because its integrand strictly decreases with \(\kappa\) for every \(v>0\). Since \(h\) is strictly decreasing, \(y_c\) strictly increases with \(\kappa\), and \(\lambda_c\) strictly decreases. For small \(\kappa\), expansions \(J(\kappa)/\kappa=1-\kappa/4+O(\kappa^2)\) and \(h(y)=1-y/2+O(y^2)\) imply \(y_c\sim\kappa/2\). For large \(\kappa\), splitting the integral defining \(J\) at one shows \(J(\kappa)=\log\kappa+O(1)\). The relation \(h(y_c)=J(\kappa)/\kappa\), together with \(h(y)\sim ye^{-y}\) for large \(y\), gives \(y_c/\log\kappa\to1\): for each fixed \(0<\epsilon<1\), inserting \((1\pm\epsilon)\log\kappa\) into \(h\) sandwiches the target for all sufficiently large \(\kappa\). The two displayed crossover asymptotics follow.

**Step 5: exact response-burden threshold.** Differentiate the Poisson response rate, with \(x=c\lambda\):
\[
R'_{\mathrm P}(\lambda)=\alpha+\beta e^{-x}(1-x).
\]
The function \(e^{-x}(1-x)\) decreases from one to its unique minimum \(-e^{-2}\) at \(x=2\), then increases to zero from below. Consequently the derivative is negative on a nonempty interval exactly when \(\alpha/\beta<e^{-2}\), with exactly the two zeros and extremum types stated. Rearranging the zero equation as \(-(x-1)e^{-(x-1)}=-e\alpha/\beta\) gives the real Lambert-\(W\) expressions. At the boundary \(\alpha/\beta=e^{-2}\), the derivative is nonnegative with only an isolated zero, proving strict monotonicity despite horizontal tangency. This exhausts all positive parameter cases.

## Verification

The independently executable `checker.py` computes \(J\) both from an alternating Taylor series and composite Simpson integration; verifies the crossover signs for randomized \(\kappa,\gamma\); verifies the two turning points, monotonicity boundary, and a numerical example; and simulates stationary Poisson memory histories without relying on the analytic Laplace formula. Running `python3 checker.py` passed 1,236 deterministic assertions and 28,000 stochastic-history draws. These finite numerical checks corroborate the formulas but do **not** establish the all-parameter theorem; that relies on the five analytic proof steps above.

For \(\gamma=\kappa=1\), \(\alpha=0.01\), and \(\beta=0.5\), direct evaluation gives \(J(1)\approx0.796599599297\) and \(\lambda_c\approx2.279008229727\). At frequency \(\lambda=0.5\), the Poisson and periodic expected response rates are approximately \(0.172865173451\) and \(0.218779107741\), respectively; at \(\lambda=5\), they are approximately \(0.096574259365\) and \(0.077313755635\). The Poisson-only stationary points occur at frequencies approximately \(1.327628549271\) and \(6.768458109866\).

## Relationship to prior work

Van der Kolk and coauthors (2019/2020, 2024) measured aircraft-related shorebird disturbance, emphasized differences between rare and predictable repeated overflights, and established the empirical relevance of frequency-dependent tolerance. Those studies do not specify the Poisson shot-memory and equal-mean periodic comparison made here; their qualitative observations are prior art and are not claimed anew. Olson and Andrews (2024) state the established general Laplace-functional identity for Poisson shot noise and study a matrix generalization; the identity used in Step 1 is therefore attributed to existing theory. The claim assessed here is the *combined exact unique traffic-cadence crossover, sensitivity asymptotics, and a positive-baseline frequency-response phase boundary* in the specified ecological response model, not the classical Poisson formula. West and Grigolini (2010) studied a different, power-law/renewal statistical habituation model; only partial publicly accessible passages were available for comparison, leaving some residual historical risk.

## Limitations

This is a phenomenological benchmark, not a prediction about a particular shorebird species, airspace, or field site. Exponential memory, uniform increment sizes, Poisson versus perfectly periodic arrivals, and the exponential response rule are assumptions. The ecological study identifies habituation and site selection as possible distinct mechanisms; this theorem addresses the former only. Flight response probability is not a complete measure of disturbance severity or population impact. Mixed aircraft types, variable stimulus amplitudes, diurnal forcing, memory reinforcement, displacement, and feedback on traffic are outside scope. Literature comparisons support a provisional novelty assessment, not a proof that no similar theorem exists in all published work; no independent external validation is claimed.

## References

1. H.-J. van der Kolk, C. J. Smit, A. M. Allen, B. J. Ens, and M. van de Pol. “Frequency-dependent tolerance to aircraft disturbance drastically alters predicted impact on shorebirds.” *Ecology Letters* 27 (2024), e14452. First published 10 June 2024. https://doi.org/10.1111/ele.14452
2. H. van der Kolk et al. “Cumulative energetic costs of military aircraft, recreational and natural disturbance in roosting shorebirds.” *Animal Conservation* 23 (2020), 359–372; first online 8 November 2019. https://doi.org/10.1111/acv.12546
3. N. R. Olson and J. G. Andrews. “A Matrix Exponential Generalization of the Laplace Transform of Poisson Shot Noise.” arXiv:2406.05212 (posted 7 June 2024), especially Section I-A on the classical Laplace functional. https://arxiv.org/abs/2406.05212
4. B. J. West and P. Grigolini. “Habituation and 1/f-noise.” *Physica A* 389 (2010), 5706–5718. https://doi.org/10.1016/j.physa.2010.08.033
