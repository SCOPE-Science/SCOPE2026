# A cubic observability barrier for censored two-channel absorption

## Finding

Consider the outcome-dependent exponential first-trajectory model described below. Even when the exact times and absorbing labels of all completed trajectories are recorded, a short deadline creates a **cubic**, rather than linear, statistical-information penalty for estimating the eventual fraction of one absorbing outcome when both conditional absorption rates are unknown.

More precisely, writing \(p=\Pr(X=1)\), \(\lambda_j\) for the conditional exponential rate given \(X=j\), and \(B\) for a common observation deadline, the efficient per-trajectory Fisher information for \(p\), after allowing \(\lambda_0,\lambda_1\) to vary, is

\[
\mathcal I_{p\mid\lambda_0,\lambda_1}(B)
=\frac{B^3}{12}\left(\frac{\lambda_0^3}{1-p}+\frac{\lambda_1^3}{p}\right)+O(B^4),\qquad B\downarrow0.
\]

With the two rates fixed and known, by contrast, the information is

\[
\mathcal I_{p}^{\mathrm{known}}(B)
=B\left(\frac{\lambda_0}{1-p}+\frac{\lambda_1}{p}\right)+O(B^2).
\]

The unknown-rate penalty is thus precisely quadratic in the deadline. For every fixed positive deadline, the full three-parameter model is identifiable and its information matrix is positive definite. As \(B\to\infty\), efficient information tends to the complete-data value \(1/[p(1-p)]\).

The cubic order also has a **global testing consequence**: hold both initial marked absorption intensities \(a_0=(1-p)\lambda_0\) and \(a_1=p\lambda_1\) fixed, and compare any two distinct priors \(p,p'\in(0,1)\), with conditional rates changed to \(a_0/(1-p),a_1/p\) and \(a_0/(1-p'),a_1/p'\), respectively. If \(P_{p,B}\) and \(P_{p',B}\) are the two censored-observation distributions, then

\[
\int\bigl(\sqrt{dP_{p,B}}-\sqrt{dP_{p',B}}\bigr)^2
=\frac{B^3}{12}\sum_{j=0}^1 a_j\bigl(\lambda_j(p)-\lambda_j(p')\bigr)^2+O(B^4).
\]

Consequently a number \(M(B)\) of independent short trajectories can consistently discriminate those two models only if \(M(B)B^3\to\infty\). In particular, splitting a fixed total first-trajectory observation budget \(M(B)B=C\) into ever shorter runs makes these alternatives asymptotically indistinguishable, **even with exact completion times**.

## Assumptions and scope

For each independent trajectory, a latent absorbing outcome \(X\in\{0,1\}\) is selected with \(\Pr(X=1)=p\in(0,1)\). Given \(X=j\), its absorption time \(T\) is exponential with an unknown finite rate \(\lambda_j>0\). Observation stops at the deterministic deadline \(B>0\): the record is \((X,T)\) if \(T\le B\), and only the fact \(T>B\) otherwise. Independent records come from separately initialized first trajectories; renewed trajectories within one observation window are not included. No equality or ordering of the rates is assumed.

For a single observation, the two marked event densities and the censoring mass are

\[
g_0(t)=(1-p)\lambda_0e^{-\lambda_0t},\quad
g_1(t)=p\lambda_1e^{-\lambda_1t},\quad 0<t\le B,
\]
\[
c(B)=(1-p)e^{-\lambda_0B}+pe^{-\lambda_1B}.
\]

Efficient Fisher information means the Schur complement of the two nuisance-rate coordinates in the ordinary three-parameter Fisher matrix. The \(O(\cdot)\) constants may depend on the fixed positive parameters; all stated expansions are locally uniform on compact subsets of the interior parameter space. The global Hellinger comparison holds at fixed distinct \(p,p'\) and fixed positive \(a_0,a_1\). The lower bound on \(M(B)\) is **necessary**, not a sufficient finite-sample or algorithmic guarantee.

## Proof

**1. Strict finite-deadline identifiability.** On each positive-length interval \((0,B)\), the observable event density is an exponential \(g_j(t)=a_je^{-\lambda_jt}\), where \(a_0=(1-p)\lambda_0\), \(a_1=p\lambda_1\). Its logarithmic slope determines \(\lambda_j\) and its positive intercept determines \(a_j\); the two intercepts then recover \(p=a_1/\lambda_1=1-a_0/\lambda_0\). More directly, a score vector with zero variance must vanish on both event intervals, forcing its constant and linear-in-time components to be zero for both labels. This determines the zero tangent vector, proving strictly positive Fisher information.

**2. Reparametrize by early-event intensities.** Use the smooth interior coordinates \((a_0,a_1,p)\), with \(\lambda_0=a_0/(1-p)\) and \(\lambda_1=a_1/p\). At fixed \(a_0,a_1\), put

\[
v_0=\partial_p\lambda_0=\frac{\lambda_0}{1-p},\qquad
v_1=\partial_p\lambda_1=-\frac{\lambda_1}{p}.
\]

A completed type-\(j\) event at time \(t\) has \(p\)-score \(-v_jt\), its corresponding \(a_j\)-score is \(1/a_j-t/p_j\), and its other \(a\)-score is zero, where \(p_0=1-p\), \(p_1=p\). Censoring has probability \(c(B)=1-(a_0+a_1)B+O(B^2)\), \(a_j\)-score \(-B+O(B^2)\), and \(p\)-score \(O(B^2)\).

Integrating the outer products of these scores against \(a_je^{-\lambda_jt}\,dt\), and adding the censoring mass, yields the following matrix-block expansions:

\[
I_{a_ja_k}(B)=\delta_{jk}\frac{B}{a_j}+O(B^2),\qquad
I_{pa_j}(B)=-\frac{v_jB^2}{2}+O(B^3),
\]
\[
I_{pp}(B)=\frac{B^3}{3}\sum_{j=0}^1a_jv_j^2+O(B^4).
\]

Thus \(I_{aa}^{-1}=B^{-1}\operatorname{diag}(a_0,a_1)+O(1)\), and the Schur complement is

\[
I_{pp}-I_{pa}I_{aa}^{-1}I_{ap}
=\left(\frac13-\frac14\right)B^3\sum_j a_jv_j^2+O(B^4).
\]

Since \(a_0v_0^2=\lambda_0^3/(1-p)\) and \(a_1v_1^2=\lambda_1^3/p\), the claimed coefficient follows. Efficient information is invariant under smooth nuisance reparametrization at fixed target \(p\).

**3. Rates known.** The event-label score is \(1/p\) for outcome 1, \(-1/(1-p)\) for outcome 0. Its event contribution to Fisher information is exactly

\[
\frac{1-e^{-\lambda_1B}}p+\frac{1-e^{-\lambda_0B}}{1-p}.
\]

The censored record contributes \((e^{-\lambda_1B}-e^{-\lambda_0B})^2/c(B)=O(B^2)\). This gives the linear law. When \(B\to\infty\), the record contains the outcome and full duration almost surely; conditional duration scores are orthogonal to the outcome score, so efficient information converges to \(1/[p(1-p)]\).

**4. Global indistinguishability.** Under fixed positive \(a_0,a_1\), both compared models have event densities \(a_je^{-\lambda_j(p)t}\). For each type, the difference of square roots is

\[
\sqrt{a_j}\bigl(e^{-\lambda_j(p)t/2}-e^{-\lambda_j(p')t/2}\bigr)
=-\frac{\sqrt{a_j}}2\bigl(\lambda_j(p)-\lambda_j(p')\bigr)t+O(t^2).
\]

Its integrated squared magnitude on \([0,B]\) is \(a_j(\lambda_j(p)-\lambda_j(p'))^2 B^3/12+O(B^4)\). Because the two total initial event intensities agree, their censoring probabilities differ by \(O(B^2)\); the squared difference of their square roots is therefore \(O(B^4)\). This proves the exact Hellinger leading term.

For probability measures \(P,Q\), write \(A(P,Q)=\int\sqrt{dP\,dQ}\). The squared-root distance in the statement equals \(2(1-A)\). Independent-product affinity is \(A(P,Q)^M\). The elementary bound \(\|P-Q\|_{\rm TV}\le\sqrt{1-A(P,Q)^2}\) implies that, whenever \(M(B)B^3\) remains bounded along a sequence, the product total-variation separation stays bounded strictly below one. Hence no test can distinguish the two fixed alternatives with both error probabilities tending to zero. Consistent estimation of \(p\) simultaneously at both alternatives would imply such a test, proving the claimed necessary divergence. If \(M(B)B=C\), then \(M(B)B^3=CB^2\to0\).

## Verification

The accompanying standalone `CHECK.py` evaluates the full three-parameter Fisher matrix by independent high-precision integrations and evaluates the Hellinger square-root distance directly from its two event densities and censoring probabilities. For three parameter sets (including equal conditional rates), the ratio of measured efficient information to the predicted cubic leading term approaches one as \(B\) decreases. For two fixed-intensity alternative pairs, the measured Hellinger distance divided by its claimed leading term also approaches one. The program reports all ratios and exits on assertion failure. The algebraic coefficient and the infinite-sequence distinction are proved above; finite experiments are supplementary consistency checks, not proofs.

## Relationship to prior work

Reia and Fontanari (arXiv:2611.12692v1, first submitted 2026-11-09) develop the same binary, outcome-dependent exponential first-trajectory sampling model, its finite-deadline selection bias and a warning that the eventual outcome probability is difficult to infer when the two conditional rates are unknown. Their full available text gives the censored event likelihood but does not state the cubic efficient-information coefficient or the matching two-alternative Hellinger indistinguishability threshold.

General competing-risks inference, including the mixture modeling of Larson and Dinse and Choi and Huang, provides broader parametric context, but available material did not establish this specific sharp short-deadline comparison. A 2026 result on hybrid-censored cause-specific hazards develops general operational Fisher information, rather than the present fixed-horizon, outcome-conditioned two-exponential model and its singular nuisance-profile asymptotics. General information formulas alone do not record the derived cubic coefficient or two-alternative lower bound. They remain relevant prior techniques, not evidence of global priority.

## Limitations

The theorem uses a strictly parametric two-outcome exponential-duration model, a common deterministic deadline and a complete record of event time when absorption occurs. It does not establish the same exponent for nonexponential conditional durations, trajectories with unknown observation mechanisms, dependent trajectory records or continuously restarted records. It does not assert a sufficient sample size for a particular estimator or finite-sample normal approximation. The quoted local Cramér–Rao interpretation applies to regular locally unbiased estimation; the Hellinger result separately establishes a nonparametric-in-estimator impossibility for the stated alternatives. Literature coverage is bounded by the sources inspected, and unindexed equivalent work is possible.

## References

1. S. M. Reia and J. F. Fontanari, *Renewal Bias in Parallel Simulations of Absorbing Processes*, arXiv:2611.12692v1 (2026-11-09). https://arxiv.org/html/2611.12692v1
2. M. G. Larson and G. E. Dinse, *A Mixture Model for the Regression Analysis of Competing Risks Data*, J. R. Stat. Soc. C 34 (1985), 201–211. https://doi.org/10.2307/2347464
3. S. Choi and X. Huang, *Maximum likelihood estimation of semiparametric mixture component models for competing risks data*, Biometrics 70 (2014), 588–598. https://doi.org/10.1111/biom.12167
4. N. Nurmukhamedova et al., *A Bernstein–von Mises Theorem for Parametric Competing Risks Under Hybrid Censoring*, Mathematics 14 (2026), 3277. https://doi.org/10.3390/math14183277
