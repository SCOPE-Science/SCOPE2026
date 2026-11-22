# Adaptive squared-loss threshold localization: a unique nonmedian follow-up and a fourth-order feedback gain

## Finding

Let \(X\) be uniform on \([0,1]\). A threshold query at \(u\in[0,1]\) returns the bit \(\mathbf 1_{\{X\ge u\}}\), independently flipped with probability \(p\in(0,1/2)\); different flips are independent conditional on \(X\). A squared-error-optimal estimate after the queries is the posterior mean. Fix the **first** threshold at \(1/2\), and permit the second threshold to depend on the first observed bit. Write \(e=1-2p\in(0,1)\).

**Theorem.** The unique optimal feedback rule for the second threshold places it at \(1/2+d_e\) after a positive first reply and \(1/2-d_e\) after a negative first reply. The displacement \(d_e\in(0,1/2)\) is the unique root there of
\[
P_e(d)=8e^2(e+1)d^3-12e^3d^2+(4e^3-2e^2+4e-4)d+e(1-e)=0.
\]
For every \(0<e<1\), this squared-loss-optimal follow-up is **strictly closer to the original midpoint** than the posterior-median (entropy-optimal) threshold:
\[
0<d_e<\frac{e}{2(1+e)}.
\]
In the high-noise, weak-channel limit \(e\downarrow0\),
\[
d_e=\frac e4-\frac{e^3}{8}+O(e^4).
\]
Denote the maximum variance explained by this two-stage midpoint-first rule by \(I_{\rm ad}(e)\), and the maximum explained variance among **all two thresholds chosen nonadaptively** by \(I_{\rm par}^*(e)\), where both use their exact posterior-mean decoders. Then
\[
I_{\rm ad}(e)=\frac{e^2}{8}-\frac{3e^4}{32}+O(e^5),\qquad
I_{\rm par}^*(e)=\frac{e^2}{8}-\frac{e^4}{8}+o(e^4),
\]
so the optimal nonadaptive two-query Bayes risk exceeds that attained by this explicit adaptive policy by
\[
R_{\rm par}^*(e)-R_{\rm ad}(e)=\frac{e^4}{32}+o(e^4)>0
\]
for all sufficiently small positive \(e\). The theorem makes **no claim** that the first midpoint is optimal among all adaptive two-stage designs.

## Assumptions and scope

The prior is uniform on the closed interval \([0,1]\), the two noisy threshold bits have equal known flip probability \(p\in(0,1/2)\), their flips are independent, and loss is squared error in the unknown location. The first query is constrained to \(u_1=1/2\). The feedback policy may choose any measurable second threshold \(u_2(Y_1)\in[0,1]\), then uses \(\widehat X=\mathbb E[X\mid Y_1,Y_2]\). In the nonadaptive comparator, both threshold locations may be **arbitrary** in \([0,1]\), without reflection or distinctness constraints; their two responses are drawn from the same independent flip channel, and estimation again uses the posterior mean. All risk statements average over the prior and both channel flips. The expressions concern the exactly-two-query experiment, not a large-budget asymptotic in query count.

## Proof

**1. Conditional second-stage information.** Encode a response as \(+1\) or \(-1\), and a truthful query as \(S_u(X)=2\mathbf 1_{\{X\ge u\}}-1\). Since \(\Pr(Y=\pm1\mid X)=(1\pm e S_u(X))/2\), the first midpoint response takes either sign with probability \(1/2\). Given \(Y_1=+1\), the posterior density is \(f_+(x)=1-e\) for \(0\le x<1/2\) and \(f_+(x)=1+e\) for \(1/2<x\le1\), with posterior mean \(\mu_+=1/2+e/4\). The negative-response case is its reflection.

For any posterior density \(f\), let \(q(u)=\Pr_f(X\ge u)\) and \(C(u)=\operatorname{Cov}_f(X,\mathbf 1_{\{X\ge u\}})\). Direct two-outcome conditioning gives the variance of the conditional mean after the next noisy query as
\[
\mathcal I_f(u)=\frac{4e^2 C(u)^2}{1-e^2(2q(u)-1)^2}.
\]
Indeed the two answer probabilities are \((1\pm e(2q-1))/2\), while the corresponding centered first moments are \(\pm eC\). The denominator is positive for \(0<e<1\).

For \(u=1/2+d\), \(0\le d\le1/2\), the positive-response posterior satisfies
\[
q_+(d)=(1+e)(1/2-d),\qquad
C_+(d)=\frac{(1+e)(1/2-d)(1+2d-e)}{4}.
\]
Write \(J_e(d)=4e^2C_+(d)^2/[1-e^2(2q_+(d)-1)^2]\). The first midpoint query explains \(e^2/16\) of the original variance, hence a positive- or negative-response optimal follow-up explains a further \(\max_{0\le d\le1/2}J_e(d)\) on average.

**2. No optimizer lies on the wrong side of the first midpoint.** For \(d\in(0,1/2)\), computing the integrals also for \(u=1/2-d\) and cancelling factors gives
\[
\mathcal I_{f_+}(1/2+d)-\mathcal I_{f_+}(1/2-d)
=\frac{d e^3(1-2d)^2\,[1-e^2+2d+2d(1-2d)e^4]}{2A_1 A_2 A_3 A_4},
\]
where
\[
\begin{aligned}
A_1&=1+e-2de,&A_2&=1-e+2de,\\
A_3&=1+e^2+2de(1-e),&A_4&=1+e^2-2de(1+e).
\end{aligned}
\]
Every numerator factor is positive. So are the four denominator factors: for the only less-obvious one, \(A_4\ge1-e>0\) because \(2d\le1\). Thus every strictly submidpoint candidate is dominated by its reflected supermidpoint candidate. Neither endpoint is informative, whereas the derivative of \(J_e\) at \(d=0\) is positive, so the optimum is strictly supermidpoint.

**3. Existence and uniqueness of the second-stage optimizer.** Exact differentiation factors as
\[
J_e'(d)=
\frac{-e^2(2d-1)(1+e)(1+2d-e)P_e(d)}{4(1-e+2de)^2(1+e^2-2de(1+e))^2}.
\]
All factors other than \(P_e(d)\) have positive sign for \(0<d<1/2\), so the derivative has precisely the sign of the displayed cubic. Set \(z=2d\). Its degree-three Bernstein coefficients on \(z\in[0,1]\), in increasing index, are
\[
 b_0=e(1-e),\quad
 b_1=\frac{2e^3-4e^2+5e-2}{3},\quad
 b_2=\frac{e^3-5e^2+7e-4}{3},\quad
 b_3=-(2-e)(1-e).
\]
Here \(b_0>0\), \(b_2<0\), and \(b_3<0\) throughout \(0<e<1\); for \(b_2\), note that the defining numerator increases on \((0,1)\) and is \(-1\) at \(e=1\). Thus, regardless of the sign of \(b_1\), the coefficient sequence has exactly one sign variation. Substituting \(z=v/(1+v)\) into the Bernstein expression and multiplying by \((1+v)^3\) yields a cubic in \(v>0\) with the same coefficient signs (apart from positive binomial factors). Descartes' rule of signs gives at most one root in \(z\in(0,1)\). Since \(P_e(0)=e(1-e)>0\) and \(P_e(1/2)=-(2-e)(1-e)<0\), such a root exists, is unique, and gives the unique maximum.

The posterior-median displacement is \(d_m=e/[2(1+e)]\). Exact substitution gives \(P_e(d_m)=e(e-1)/(1+e)^2<0\). The unique sign change in the previous paragraph therefore implies \(0<d_e<d_m\); by reflection this proves the entire optimal feedback policy. Expanding the cubic around \((e,d)=(0,0)\), whose derivative in \(d\) is \(-4\), yields \(d_e=e/4-e^3/8+O(e^4)\). Substitution in the exact \(J_e\) formula gives \(I_{\rm ad}(e)=e^2/16+J_e(d_e)=e^2/8-3e^4/32+O(e^5)\).

**4. The comparison is against unrestricted nonadaptive threshold pairs.** For a fixed nonadaptive pair \(t,u\in[0,1]\), put \(S_v(x)=2\mathbf 1_{\{x\ge v\}}-1\), \(m_v=\mathbb ES_v=1-2v\), \(A_v=\operatorname{Cov}(X,S_v)=v(1-v)\), \(k=\mathbb E[S_tS_u]=1-2|t-u|\), and \(B=\operatorname{Cov}(X,S_tS_u)\). For \(y,z\in\{-1,+1\}\), the probability of reply pair \((y,z)\) is \([1+e(ym_t+zm_u)+e^2 yz k]/4\); its centered first moment is \([e(y A_t+z A_u)+e^2 yz B]/4\). Therefore its explained variance is exactly
\[
I_{\rm par}(t,u,e)=\frac14\sum_{y,z\in\{-1,+1\}}
\frac{[e(yA_t+zA_u)+e^2 yz B]^2}
{1+e(ym_t+zm_u)+e^2 yz k}.
\]
For \(|e|<1\), all denominators are uniformly bounded away from zero on the compact parameter square. Consequently its Taylor expansion at \(e=0\) is uniform in \(t,u\), and invariance under simultaneous response sign-flips makes it even in \(e\):
\[
I_{\rm par}(t,u,e)=e^2[A_t^2+A_u^2]+e^4G(t,u)+O(e^6),
\]
where \(G\) is continuous. The leading term has the **unique** maximizer \((t,u)=(1/2,1/2)\), because \(A_v=v(1-v)\) has a unique maximum at \(1/2\). Thus every maximizing pair converges to \((1/2,1/2)\) as \(e\downarrow0\). The exact repeated-midpoint information is \(I_{\rm par}(1/2,1/2,e)=e^2/[8(1+e^2)]\), hence \(G(1/2,1/2)=-1/8\). Uniformity, convergence of optimizers, and the fact that their leading \(e^2\) term never exceeds \(e^2/8\) give \(\limsup_{e\downarrow0}(I_{\rm par}^*(e)-e^2/8)/e^4\le-1/8\). The repeated-midpoint choice supplies the matching lower bound. Therefore \(I_{\rm par}^*(e)=e^2/8-e^4/8+o(e^4)\). Subtracting from the adaptive expansion yields the asserted positive fourth-order feedback gain. As Bayes risk equals \(\operatorname{Var}(X)-\text{explained variance}=1/12-I\), the stated risk comparison follows.

## Verification

The standalone `verify.py`, runnable with Python 3.10+ and no third-party packages, independently computes outcome probabilities and first moments by interval integration. It checks the second-stage polynomial root, a grid of posterior-noise designs, strict median inequality, mirror dominance, the published closed form for mirror-symmetric parallel queries, and weak-channel expansions. Run `python verify.py` in the directory containing this document; `verification_output.txt` records the actual finite check output. These calculations are supplementary finite tests; analytic uniqueness and the unrestricted asymptotic parallel bound follow from the explicit arguments above rather than enumeration.

## Relationship to prior work

Jedynak, Frazier and Sznitman analyze Bayesian noisy twenty questions under **entropy loss** and show the optimality of posterior-median querying for a binary symmetric channel. Their results are not squared-error results, and the strict nonmedian inequality above shows why the entropy-optimal second threshold cannot optimize the present loss. Variani et al. study **nonadaptive dyadic query families** and asymptotic MSE rates; they do not address an exact two-query feedback optimum. Zhou and Hero analyze **excess-resolution probability** and nonasymptotic/second-order channel-coding bounds for noisy twenty questions, not the present finite-horizon squared-error objective.

A published two-parallel-query theorem gives a unique explicit threshold for **nonadaptive mirrored pairs** under the same uniform prior and bit-flip noise. It neither permits the second threshold to depend on the first response nor establishes the unrestricted nonadaptive comparison used here. The present proof independently derives the latter comparison's weak-channel coefficient for **all** threshold pairs. These conclusions are confined to the inspected works; unlocated exact finite-horizon Bayesian design precedents may exist.

## Limitations

The first threshold is fixed at the midpoint; neither global first-threshold optimality nor the globally optimized two-query adaptive Bayes risk is asserted. The positive gap against the nonadaptive optimum is proved asymptotically for sufficiently high noise, not for every flip probability. The polynomial and median gap are exact for every \(0<e<1\) only within the midpoint-first policy class. The model excludes measurement-dependent or correlated errors, nonuniform priors, general query sets, and more than two questions. No claim of exhaustive historical publication priority or independent proof validation is made.

## References

1. L. Zhou and A. Hero, *Resolution Limits of Noisy 20 Questions Estimation*, first public arXiv submission 2019-09-27, arXiv:1909.12954, https://arxiv.org/abs/1909.12954 .
2. B. Jedynak, P. Frazier and R. Sznitman, *Twenty Questions with Noise: Bayes Optimal Policies for Entropy Loss*, publicly accessible author PDF, https://people.orie.cornell.edu/pfrazier/pub/2011_JedynakFrazierSznitman_20questions.pdf .
3. E. Variani, K. Lahouel, A. Bar-Hen and B. Jedynak, *Non-Adaptive Policies for 20 Questions Target Localization*, first posted 2015-04-22, arXiv:1504.05996, https://arxiv.org/abs/1504.05996 .
4. *Noise-calibrated thresholds for two parallel binary location queries*, publicly deposited mathematical result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-noise-calibrated-thresholds-for-two-parallel-binary-location-que--dedce94eaa8e/RESULT.md .
