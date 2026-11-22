# The exposure-depth phase transition in social-action count evidence

## Finding

**Theorem (sharp count-order reversal).** Let the hidden state be \(\omega\in\{L,H\}\), with prior probabilities strictly between zero and one. Suppose a potential predecessor independently chooses the observable affirmative action with probability \(p_\omega\), with \(0<p_L<p_H<1\). A state-independent opportunity flag \(J\) is absent with probability \(\eta\in[0,1)\). If \(J=0\), there are no predecessors. If \(J=1\), the unobserved number of predecessors is Poisson with mean \(\lambda>0\). Conditional on this number, their actions are independent. The decision maker sees only the affirmative count \(K\), not \(J\) or the number of unobserved negative actions.

Put \(r=p_H/p_L>1\) and \(\theta=\lambda(p_H-p_L)\). The likelihood ratio \(B_k=\Pr(K=k\mid H)/\Pr(K=k\mid L)\) is strictly increasing for every \(k\ge1\). It is nondecreasing on the entire count domain \(\{0,1,2,\ldots\}\) if and only if either \(\theta\le\log r\), or \(\theta>\log r\) and \(\eta\le\eta_c\), where

\[
\eta_c=\frac{(r-1)e^{-\lambda p_H}}{1-r e^{-\theta}+(r-1)e^{-\lambda p_H}}\in(0,1).
\]

For \(\theta>\log r\) and \(\eta>\eta_c\), there is exactly one downward adjacent likelihood-ratio step, from count zero to count one; all further steps increase strictly. The strict downward step means that observing exactly one affirmative action supports \(H\) *less* than observing zero affirmative actions, for every positive prior. Despite this failure of monotone likelihood ratios, \(K\mid H\) strictly first-order stochastically dominates \(K\mid L\).

Fix \(0<\eta<1\) and \(p_L<p_H\). As exposure \(\lambda\) increases, a single sharp transition from global monotone likelihood ratio to a zero-to-one reversal occurs at the unique \(\lambda_c>\log r/(p_H-p_L)\) satisfying

\[
 e^{\lambda_c p_H}-r e^{\lambda_c p_L}=(r-1)\frac{1-\eta}{\eta}.
\]

The transition depth decreases strictly as \(\eta\) increases, and as \(\eta\downarrow0\) it satisfies

\[
\lambda_c=\frac{\log((r-1)/\eta)}{p_H}+o(1).
\]

Recording the one-bit exposure flag \(J\) restores a monotone likelihood-ratio count rule within the eligible stratum \(J=1\); \(J=0\) has an uninformative deterministically zero count. No equilibrium or strategic behavior claim is made.

## Assumptions and scope

All five model parameters are fixed and known for this identification experiment, with \(\lambda>0\), \(0<p_L<p_H<1\), and \(0\le\eta<1\). The opportunity flag and the number of potential predecessors, when the flag is one, are independent of the hidden state. All conditional decisions are independent Bernoulli trials given the state and predecessor count. Both states have positive prior probabilities. The observer records the integer \(K\ge0\); it is the count of observable affirmative actions, not the number of attempts or a consecutive-run statistic. No strategic feedback, correlated actions, or state-dependent exposure is allowed. The ``more informative'' comparison is between posteriors for *exactly* \(K=0\) and \(K=1\), not between the events \(K=0\) and \(K\ge1\).

## Proof

**Thinning and likelihoods.** Conditional on \(J=1\) and state \(\omega\), thinning \(N\sim\operatorname{Poisson}(\lambda)\) by independent probability \(p_\omega\) gives \(K\sim\operatorname{Poisson}(\lambda p_\omega)\). Thus with \(a_\omega=e^{-\lambda p_\omega}\),

\[
 f_\omega(0)=\eta+(1-\eta)a_\omega,\qquad
 f_\omega(k)=(1-\eta)a_\omega\frac{(\lambda p_\omega)^k}{k!},\quad k\ge1.
\]

Every mass is positive because \(\eta<1\). Consequently

\[
 B_0=\frac{\eta+(1-\eta)e^{-\lambda p_H}}{\eta+(1-\eta)e^{-\lambda p_L}},\qquad
 B_k=e^{-\theta}r^k,\quad k\ge1.
\]

This proves strict increase for positive counts. Also \(B_0<1\); for \(\eta=0\), \(B_0=e^{-\theta}\), and for \(0<\eta<1\) it lies strictly between \(e^{-\theta}\) and \(1\). If \(\theta\le\log r\), \(B_1=re^{-\theta}\ge1>B_0\), giving strict global increase. If \(\theta>\log r\), the sign of \(B_0-B_1\), after multiplying by the positive denominator, equals the sign of

\[
 \eta(1-r e^{-\theta})-(1-\eta)(r-1)e^{-\lambda p_H}.
\]

The coefficient \(1-r e^{-\theta}\) is positive. Solving the linear inequality in \(\eta\) proves the threshold \(\eta_c\), including equality and strict sides; the formula has numerator positive and denominator larger by \(1-r e^{-\theta}>0\). No second downward step is possible because \(B_{k+1}/B_k=r>1\) for all \(k\ge1\). Bayesian posterior odds are prior odds multiplied by \(B_k\), so the same comparisons apply to posterior beliefs for every nondegenerate prior.

**Unique exposure threshold.** For fixed \(0<\eta<1\), multiplying the preceding sign expression by \(e^{\lambda p_H}>0\) shows that the reversal occurs precisely when

\[
 F(\lambda):=e^{\lambda p_H}-r e^{\lambda p_L}>(r-1)(1-\eta)/\eta.
\]

Here \(F(0)=1-r<0\) and, for \(\lambda>0\),

\[
 F'(\lambda)=p_H(e^{\lambda p_H}-e^{\lambda p_L})>0.
\]

Further, \(F(\lambda)\to\infty\) as \(\lambda\to\infty\), while \(F(\log r/(p_H-p_L))=0\). Therefore exactly one \(\lambda_c\) exists beyond the displayed lower bound. The right-hand threshold \((r-1)(1-\eta)/\eta\) decreases strictly with \(\eta\), so \(\lambda_c\) decreases strictly. As \(\eta\downarrow0\), the defining equation forces \(\lambda_c\to\infty\); writing it as \(e^{\lambda_c p_H}(1-r e^{-\lambda_c(p_H-p_L)})=(r-1)(1-\eta)/\eta\) and taking logarithms gives the stated asymptotic.

**Stochastic ordering and extra observation.** Couple both states with the same \(J\), \(N\), and independent uniforms \(U_i\) for the predecessor decisions. Define \(K_\omega=\sum_{i=1}^N\mathbf1\{U_i<p_\omega\}\) on \(J=1\), and zero otherwise. Then \(K_H\ge K_L\) almost surely, with strict stochastic inequalities for every finite positive threshold \(k\), since \(\Pr(J=1,N\ge k)>0\) and positive-probability uniform configurations force \(K_H\ge k>K_L\). The means are \(\mathbb E[K_\omega]=(1-\eta)\lambda p_\omega\). If \(J\) is recorded, on \(J=1\) the zero count has likelihood ratio \(e^{-\theta}\), followed by \(e^{-\theta}r^k\) at every \(k\ge1\), a globally increasing sequence. On \(J=0\) the count is identically zero in both states, so its likelihood ratio is one. This proves the qualified one-bit remedy.

**Exact counterexample.** Set \(p_L=1/4\), \(p_H=3/4\), \(\lambda=4\log2\), and \(\eta=3/4\). The two conditional Poisson zero masses are \(1/2\) and \(1/8\). Direct substitution gives

\[
 \eta_c=\frac12,\quad B_0=\frac{25}{28},\quad B_1=\frac34,\quad B_2=\frac94.
\]

Both conditional means increase strictly from \(\log2/4\) to \(3\log2/4\), confirming the distinct likelihood-ratio and stochastic-order statements.

## Verification

The standalone `checker.py` relies only on the Python standard library. Run `python checker.py` in the extracted package directory. It checks the exact witness using rational arithmetic and performs deterministic parameter checks of the explicit threshold, positive-count likelihood formulas, and sign cases. The proof above is analytic and covers all stated real parameter values; finitely many numerical tests are not used to justify the universal quantifiers. Check that the code is extracted from the same record as this manuscript before replay.

## Relationship to prior work

Partial aggregate-action observability and unobservable non-actions are directly motivated by Cavatorta, Guarino and Huck (2023/2024), who study strategic sequential social learning with unknown position. Guarino, Harmgart and Huck (2011) prove cascade and belief monotonicity statements for a finite, endogenous game; in particular their Proposition 2 concerns increases *within* an up-cascade. Neither model is the present nonstrategic, independent Bernoulli opportunity process with a structural-zero flag. The zero-inflated Poisson marginal formula itself is standard, and He, Xue and Shi (2010) and Haslett and colleagues (2021/2022) study its statistical modelling. No novelty is asserted for the marginal formula or generic Poisson thinning. The assessed claim is the complete, exact two-parameter likelihood-ratio phase boundary, its unique exposure-depth crossover despite stochastic dominance, and the specific observed-flag remedy under this social-observation interpretation. Literature coverage is not exhaustive and precedence from general discrete-family ordering theory remains an explicit risk.

## Limitations

This is a stylized inferential result, not an equilibrium theorem, not a causal claim that observed positive actions discourage adoption, and not an empirically estimated social behavior law. The trigger assumes a *state-independent* chance of no exposure and independent homogeneous decisions. State-dependent exposure, correlated predecessors, strategic cascades, uncertain model parameters, or informative selection into observation can change the threshold or eliminate it. The recovery statement is only a monotone-likelihood-ratio comparison conditional on a recorded exposure bit, not identification of unknown parameters or finite-sample optimality. The standard zero-inflated Poisson algebra makes this a narrowly scoped structural observation rather than a claim of a new general stochastic-order theorem. Historical mathematical priority cannot be guaranteed from a bounded literature inspection. Independent external validation has not been performed.

## References

1. Cavatorta, E., Guarino, A., and Huck, S. (2023), *Social Learning with Partial and Aggregate Information: Experimental Evidence*, CEPR Discussion Paper 18461, first public version 14 September 2023. https://cepr.org/index.php/publications/dp18461 ; lawful accepted manuscript https://discovery.ucl.ac.uk/id/eprint/10190721/1/CGH_Accepted_Version.pdf
2. Guarino, A., Harmgart, H., and Huck, S. (2011), *Aggregate information cascades*, publicly readable author manuscript https://www.homepages.ucl.ac.uk/~uctpagu/Aggregate_Cascades.pdf
3. He, X., Xue, H., and Shi, N.-Z. (2010), *Sieve Maximum Likelihood Estimation for Doubly Semiparametric Zero-Inflated Poisson Models*, *Journal of Multivariate Analysis* 101:2026–2038. https://pmc.ncbi.nlm.nih.gov/articles/PMC2909790/
4. Haslett, J., Parnell, A. C., Hinde, J., and de Andrade Moral, R. (2022), *Modelling Excess Zeros in Count Data: A New Perspective on Modelling Approaches*, first published 7 November 2021. https://doi.org/10.1111/insr.12479
