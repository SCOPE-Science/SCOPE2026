# Heterogeneous critical-reciprocity states are spectrally unstable under reactive-game gradient learning

## Finding

Consider the finite-population, simultaneous, projected gradient-ascent update of the infinitely repeated prisoner's dilemma with reactive strategies, including self-play, as defined below. The full population contains \(N\ge 2\) players with possibly unequal positive learning rates. Every interior strategy profile satisfying \(p_i-q_i=c/b\) for each agent is a fixed point. If the forgiveness coordinates \(q_i\) are not all identical, that fixed point is linearly unstable for **every choice of strictly positive learning rates**. More precisely, its \(2N\)-dimensional update Jacobian has exactly two eigenvalues different from \(1\), given explicitly by

\[
\mu_\pm=1+\frac{C}{2}\left(S\pm\sqrt{S^2+16\alpha\sigma_w^2}\right),
\qquad \mu_+>1,\quad\mu_-<1,
\]

and its other \(2N-2\) eigenvalues equal \(1\) (algebraic multiplicity). Here \(\alpha=c/b\), \(C=b\bar\eta/(1-\alpha^2)^2\), \(S=2(1+\alpha)\bar q_w-(1-\alpha^2)\), and \(\bar q_w,\sigma_w^2\) are respectively the learning-rate-weighted mean and variance of the \(q_i\). The result distinguishes a continuum of exact stationary learning profiles from dynamically robust stationary profiles. It asserts local linear instability, not their global basins or the eventual learning outcome.

## Assumptions and scope

Fix \(N\ge2\), benefit \(b>c>0\), and \(0<\varepsilon<1/2\) such that \(\alpha=c/b<1-2\varepsilon\). Each agent \(i\in\{1,\ldots,N\}\) has a reactive strategy \((p_i,q_i)\in[\varepsilon,1-\varepsilon]^2\) and an arbitrary fixed learning rate \(\eta_i>0\). Let \(r_i=p_i-q_i\), and for two distinct argument slots write the long-run pairwise payoff

\[
\pi_{ij}=\frac{b(q_i r_j+q_j)-c(q_j r_i+q_i)}{1-r_i r_j}.
\]

The model's gradient treats the first argument as the learner's strategy and the second argument as the opponent's strategy, even when the two argument slots are populated with the same agent's strategy (self-play). The two first-argument gradient components are

\[
 g^p_{ij}=\frac{(b r_j-c)(q_i r_j+q_j)}{(1-r_i r_j)^2},\qquad
 g^q_{ij}=\frac{(b r_j-c)(1-q_j-p_i r_j)}{(1-r_i r_j)^2}.
\]

The simultaneous update is \((p_i^+,q_i^+)=\operatorname{Proj}_{[\varepsilon,1-\varepsilon]^2}[(p_i,q_i)+(\eta_i/N)\sum_{j=1}^N(g^p_{ij},g^q_{ij})]\). Projections are coordinatewise. The result concerns an interior point with \(p_i=q_i+\alpha\), \(\varepsilon<q_i<1-\varepsilon-\alpha\). The two-variable symbols in the gradients are ordinary partial derivatives of the ordered pairwise payoff; on the diagonal the resulting \(g_{ii}\) is then differentiated as part of the full population map when forming its Jacobian.

Define \(s=1-\alpha^2>0\), \(E=\sum_{i=1}^N\eta_i\), \(w_i=\eta_i/E\), \(\bar\eta=E/N\), \(\bar q_w=\sum_i w_i q_i\), \(\sigma_w^2=\sum_i w_i(q_i-\bar q_w)^2\), \(C=b\bar\eta/s^2\), and \(S=2(1+\alpha)\bar q_w-s\). In particular, \(\sigma_w^2>0\) exactly when the forgiveness coordinates are nonconstant, because all rates are positive.

## Proof

**Fixed-point condition.** At an interior profile with every \(r_j=\alpha\), each gradient numerator has the factor \(b\alpha-c=0\). Therefore all gradients vanish, and the projection acts as the identity locally. Thus every such profile is a fixed point.

**Linearization.** Write first-order perturbations \(\delta r_j=\delta p_j-\delta q_j\). Differentiating the displayed gradients at the fixed profile, all derivatives of factors other than \(b r_j-c\) vanish by multiplication with that zero factor. Since \(r_i r_j=\alpha^2\), the infinitesimal changes of the two strategy updates are

\[
 \delta p_i^+-\delta p_i=\frac{b\eta_i}{Ns^2}\sum_j(\alpha q_i+q_j)\,\delta r_j,
\]
\[
 \delta q_i^+-\delta q_i=\frac{b\eta_i}{Ns^2}\sum_j(s-q_j-\alpha q_i)\,\delta r_j.
\]

Subtracting gives the reduced reciprocity map \(\delta r^+=(I_N+M)\delta r\), where

\[
 M_{ij}=\frac{b\eta_i}{Ns^2}\left(2\alpha q_i+2q_j-s\right).
\]

This is a rank-at-most-two matrix: it is the sum of one column vector times the all-ones row and another column vector times the row of \(q_j\). In the full \(2N\)-coordinate space, the Jacobian is \(J=I_{2N}+UV\), where \(V\) maps the strategy perturbations to \((\delta r_j)\). Its nonzero departure-from-identity eigenvalues coincide, including algebraic multiplicities, with the nonzero eigenvalues of \(VU=M\); this follows from \(\det(\lambda I-UV)=\lambda^{N}\det(\lambda I-VU)\) in this dimension.

**Exact reduced spectrum.** Let \(a_i=b\eta_i/(Ns^2)\) and \(H=\sum_i a_i=C\). Factor \(M\) into two columns \(a_i(2\alpha q_i-s)\), \(2a_i\), and two rows \(1\), \(q_j\). The resulting \(2\times2\) matrix has trace

\[
 \operatorname{tr}(M)=H\,[2(1+\alpha)\bar q_w-s]=CS
\]

and determinant

\[
 \det_2(M)=4\alpha\left[(\sum_i a_iq_i)^2-(\sum_i a_i)(\sum_i a_iq_i^2)\right]
 =-4\alpha C^2\sigma_w^2.
\]

Because \(\alpha>0\), \(C>0\), and \(\sigma_w^2>0\), this determinant is strictly negative. Its two real roots have opposite signs, and are exactly \(\lambda_\pm=C(S\pm\sqrt{S^2+16\alpha\sigma_w^2})/2\). Therefore \(J\) has the stated two multipliers \(1+\lambda_\pm\), with \(\mu_+>1\), and the other \(2N-2\) multipliers are \(1\). The rank is exactly two in the nonconstant case. A real eigenvector for \(\mu_+\) gives arbitrarily small perturbations expanding under linearization, so the fixed point is Lyapunov unstable by the discrete-time linear instability theorem. All computations occur in an interior neighborhood where projection is inactive, completing the proof.

## Verification

A standalone exact-arithmetic script `CHECK.py` reconstructs the original four-dimensional update at an admissible two-agent profile: \(\varepsilon=1/20\), \(b=1\), \(c=1/2\), \((q_1,q_2)=(1/10,3/10)\), \((\eta_1,\eta_2)=(1/5,2/5)\), and \((p_1,p_2)=(3/5,4/5)\). It differentiates the original gradient expressions, not merely the derived rank-two matrix, and confirms that the fixed-point residual vanishes. The exact Jacobian in state order \((p_1,q_1,p_2,q_2)\) is

\[
 \begin{pmatrix}
 77/75 &-2/75 &14/225 &-14/225\\
 8/75 &67/75 &16/225 &-16/225\\
 4/45 &-4/45 &29/25 &-4/25\\
 8/45 &-8/45 &8/75 &67/75
 \end{pmatrix},
\]

with exact multipliers \(1,1,(222-\sqrt{265})/225,(222+\sqrt{265})/225\). The script also checks the weighted-moment formula and independent rational rank-two examples. These finite checks corroborate the derivation; the all-\(N\) statement is proved analytically above.

## Relationship to prior work

Wolfe and Plotkin (2026) introduce exactly the ordered reactive-strategy payoff, gradient-ascent rule, self-play convention, and stationary reciprocity threshold used here. Their fixed-point factor \(b r_j-c\) immediately implies that all-critical-reciprocity profiles have zero gradients; that fixed-point observation is **not** presented as new. Their principal results and supplementary no-recovery theorem concern convergence to defection or generous reciprocity, boundary stationary distributions, and homogeneous learner dynamics. The additional result proved here is the *complete rank-two linearization and strictly positive unstable eigenvalue for every heterogeneous interior critical-reciprocity state*, including arbitrary positive learning-rate variation. This is not implied by the factorization without the nonconstant-forgiveness weighted-variance calculation. Other accounts of asymmetry in repeated games use different update laws or accessible abstracts and cannot rule out an equivalent broader stability theorem.

## Limitations

The result concerns finite populations with the exact simultaneous first-argument payoff-gradient update and self-play used above. It does not automatically apply to gradients that differentiate both roles of self-play, stochastic learning, payoff sampling, asynchronous learning, or a boundary fixed point where projection is active. Instability of the stationary state does not characterize every orbit or the eventual level of cooperation. The \(2N-2\) unit multipliers are neutral at linear order; no claim is made about their nonlinear center dynamics. At identical forgiveness coordinates the variance vanishes and the strict two-sided eigenvalue conclusion cannot be inferred. The second multiplier \(\mu_-<1\) need not have modulus below one at arbitrarily large learning rates. An equivalently general prior spectral theorem may exist outside the inspected literature; the claim has not been independently audited.

## References

1. James P. Wolfe and Joshua B. Plotkin, *Multi-Agent Learning of Reactive Strategies in Iterated Games*, arXiv:2610.15054v1, first posted 2026-10-10. https://arxiv.org/abs/2610.15054 . Model and gradient equations in Section II; comparisons to homogeneous learning and supplementary results in the full preprint.
2. Yuma Fujimoto and Kunihiko Kaneko, *Emergence of Exploitation as Symmetry Breaking in Iterated Prisoner's Dilemma*, arXiv:1905.06602 (2019). https://arxiv.org/abs/1905.06602 . Related asymmetric learning; only abstract-level material was accessible in this comparison.
3. Alex McAvoy, Yuma Mori and Joshua B. Plotkin, *Selfish optimization and collective learning in populations*, arXiv:2111.07776 (2021). https://arxiv.org/abs/2111.07776 . Related optimization-based evolutionary learning; abstract-level comparison only.
