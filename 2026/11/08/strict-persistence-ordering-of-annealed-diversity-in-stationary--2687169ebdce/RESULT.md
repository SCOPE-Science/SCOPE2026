# Strict persistence ordering of annealed diversity in stationary Markov stick breaking

## Finding

Consider the stationary refresh-or-retain stick-breaking construction in the next section. For each real \(q>1\), define its annealed power sum by
\[
M_q(\rho)=\mathbb E\!\left[\sum_{j\geq1}W_j^q\right].
\]
For every non-point-mass break distribution supported on \((0,1)\), the function \(\rho\mapsto M_q(\rho)\) is **strictly decreasing** on \([0,1]\), with the exact integral formula
\[
\boxed{M_q(\rho)=
\frac{\displaystyle\int\frac{v^q}{1-\rho(1-v)^q}\,\mu(dv)}
{\displaystyle\int\frac{1-(1-v)^q}{1-\rho(1-v)^q}\,\mu(dv)}.}
\]
In particular, the annealed probability that \(k\geq2\) conditionally independent species samples have identical labels is strictly decreasing with persistence \(\rho\), for every integer \(k\geq2\).

For \(0<q<1\), the same formula holds and \(M_q(\rho)\) is **strictly increasing** on \([0,1]\), provided
\[
\int\frac{v^q}{1-(1-v)^q}\,\mu(dv)<\infty.
\]
For \(q=1\), the power sum is identically one. Thus, all finite annealed power sums are ordered across the full refresh-to-retain range, with the direction reversing at order one. This does not assert the ordering of the expected logarithm of a power sum (expected Rényi entropy).

The expected **Shannon entropy** is also strictly increasing with \(\rho\), assuming \(\int|\log v|\,\mu(dv)<\infty\). More precisely, with \(h(v)=-v\log v-(1-v)\log(1-v)\),
\[
\boxed{\mathbb E\!\left[-\sum_{j\geq1}W_j\log W_j\right]
=\frac{\displaystyle\int\frac{h(v)}{1-\rho(1-v)}\,\mu(dv)}
{\displaystyle\int\frac{v}{1-\rho(1-v)}\,\mu(dv)}.}
\]
Here all logarithms are natural. The strict inequalities hold even though every model in the family has exactly the same one-time marginal break distribution \(\mu\).

## Assumptions and scope

Fix a Borel probability \(\mu\) supported on \((0,1)\) and not concentrated at one point, and \(0\leq\rho\leq1\). Start \(V_1\sim\mu\). Given \(V_j=v\), set \(V_{j+1}=v\) with probability \(\rho\) and otherwise sample a new independent value from \(\mu\). Its stationary transition kernel is
\[
P_\rho(v,du)=\rho\,\delta_v(du)+(1-\rho)\,\mu(du).
\]
Put
\[
W_j=V_j\prod_{i=1}^{j-1}(1-V_i),\qquad j\geq1.
\]
The weights are nonnegative and sum to one almost surely: if \(\rho=1\), a positive fixed \(V_1\) is repeated forever; if \(\rho<1\), independent refreshes with values bounded away from zero recur infinitely often. No density or beta-law assumption is required. For species sampling, assign the weights to distinct abstract labels (or independent atoms from a diffuse base distribution).

The power-sum conclusion for \(q>1\) requires no moment assumptions beyond the preceding scope. The \(0<q<1\) endpoint result requires the displayed integrability condition, and finite expected Shannon entropy on the closed parameter interval requires the stated logarithmic moment condition. Every strict comparison concerns distinct \(\rho_1<\rho_2\) with the *same* \(\mu\).

## Proof

**Step 1: a discounted Markov renewal equation.** Fix \(q>0\) and set \(A(v)=(1-v)^q\), \(f(v)=v^q\). Write \(F(v)\) for the conditional expected sum of powered weights when the current break equals \(v\), with the residual stick normalized to one, and let \(m=\int F\,d\mu\). Decomposing at the first break and the next refresh-or-retain decision gives
\[
F(v)=f(v)+A(v)\left[\rho F(v)+(1-\rho)m\right].
\]
For \(0\leq\rho<1\), define the analogous expected reward using only the first \(N\) breaks. These quantities increase with \(N\), and replacing their \(N-1\)-step terms by the larger \(N\)-step terms in the recurrence yields a uniform upper bound of the displayed integral-quotient form: its denominator is strictly positive and its numerator finite because \(f\leq1\) and \(1-\rho A\geq1-\rho\). Thus the infinite expected reward is finite, and monotone convergence justifies the equation. Solving gives
\[
F(v)=\frac{f(v)+(1-\rho)A(v)m}{1-\rho A(v)}.
\]
Integrate with respect to \(\mu\), rearrange, and use
\[
1-(1-\rho)\int\frac{A(v)}{1-\rho A(v)}\,\mu(dv)
=\int\frac{1-A(v)}{1-\rho A(v)}\,\mu(dv)>0
\]
to obtain the boxed expression for \(M_q(\rho)=m\). The integrals are finite when \(\rho<1\). If \(\rho=1\), then every break equals \(V_1=v\), so \(W_j=v(1-v)^{j-1}\) and the conditional powered sum is \(v^q/[1-(1-v)^q]\). This gives the same expression at the endpoint when its expectation is finite. For \(q>1\), the endpoint expectation is automatically bounded by one.

**Step 2: strict likelihood-ratio ordering.** Define
\[
R_q(v)=\frac{v^q}{1-(1-v)^q},\qquad
b_{q,\rho}(v)=\frac{1-(1-v)^q}{1-\rho(1-v)^q}.
\]
Then \(M_q(\rho)\) is the expectation of \(R_q\) under the probability measure proportional to \(b_{q,\rho}(v)\mu(dv)\). For \(\rho_2>\rho_1\),
\[
\frac{b_{q,\rho_2}(v)}{b_{q,\rho_1}(v)}
=\frac{1-\rho_1(1-v)^q}{1-\rho_2(1-v)^q}
\]
is **strictly decreasing** in \(v\in(0,1)\). Meanwhile direct differentiation yields
\[
R_q'(v)=\frac{qv^{q-1}\left[1-(1-v)^{q-1}\right]}{\left[1-(1-v)^q\right]^2}.
\]
Thus \(R_q\) is strictly increasing if \(q>1\), and strictly decreasing if \(0<q<1\). Applying the covariance identity
\[
\operatorname{Cov}(g(V),r(V))
=\tfrac12\mathbb E\left[(g(V)-g(V'))(r(V)-r(V'))\right],
\]
with \(V,V'\) independent under the first tilted law, proves the strict sign of the difference between the two expectations. Strictness follows because \(\mu\) is not a point mass and both tilting densities are everywhere positive. The integrability condition for \(q<1\) makes every endpoint comparison finite. For \(q=1\), the weights sum to one.

**Step 3: Shannon entropy.** The entropy chain rule for the first break gives the analogous renewal equation, this time with local reward \(f(v)=h(v)\) and residual discount \(A(v)=1-v\):
\[
F_H(v)=h(v)+(1-v)\bigl[\rho F_H(v)+(1-\rho)m_H\bigr].
\]
Its solution, by the same integration, yields the second boxed formula. The endpoint conditional entropy of the geometric weights is \(h(v)/v\), so \(\int|\log v|d\mu<\infty\) ensures finiteness; for \(\rho<1\) finiteness already follows from \(h(v)\leq\log2\). Under the tilted measure proportional to \(v/[1-\rho(1-v)]\,\mu(dv)\), the response is \(R_H(v)=h(v)/v\). A derivative calculation gives
\[
R_H'(v)=\frac{\log(1-v)}{v^2}<0.
\]
The likelihood-ratio tilt favors smaller \(v\) as \(\rho\) grows, so the expectation of this strictly decreasing response grows strictly. This completes the proof.

**Step 4: species interpretation.** Conditional on the weights, independent sampling from their countable labels puts all \(k\) samples at the same label with probability \(\sum_jW_j^k\). Averaging gives precisely \(M_k(\rho)\), so the strict ordering applies to every integer collision order \(k\geq2\).

## Verification

The standalone script `check.py` uses rational arithmetic to solve independent finite-state linear systems for three-, four- and two-state refresh chains and compares the solutions with the derived power-sum formula, checking strict ordering at five parameter values and three integer powers. Separate floating-point linear-system comparisons check both the fractional order \(q=1/2\) and the Shannon entropy formula and strict ordering. Exact exhaustive eight-step state-path enumeration supplies an independent prefix-and-residual enclosure at three persistence levels. Its standard-library verification run completed 4,625 exact rational and 3,080 floating-point assertions. These are finite checks of critical identities and do not prove the infinite theorem.

For the natural two-point example \(\mu=\frac12\delta_{1/4}+\frac12\delta_{3/4}\), the exact endpoint collision probabilities are
\[
M_2(0)=\frac5{11},\qquad M_2(1)=\frac{13}{35},
\]
which the verifier reproduces exactly. The analytic strict ordering applies to every intermediate persistence level, not just the endpoints.

## Relationship to prior work

Gil-Leyva, Lijoi, Mena and Prünster (2026), Section 5, introduced and studied the lazy Markov stick-breaking kernel above, including properness, interpolation between independent and completely dependent breaks, and clustering probabilities. Their discussion gives a comparison of tie probabilities at the two extreme parameter values for a beta-marginal family and numerical illustrations for intermediate parameters. The present theorem concerns an additional exact, universal, **strict order along the entire persistence continuum**, simultaneously for powered collision probabilities and expected Shannon entropy, for arbitrary stationary nondegenerate break laws. It does **not** claim the Markov construction, the endpoint models, standard entropy chain rules or the general renewal method as new.

Gil-Leyva and Mena (2020 preprint; 2023 journal article) studied *exchangeable* break lengths, a distinct form of dependence, and ordering of adjacent stick weights; their formulas at independent/fully dependent endpoints do not supply the strict interior-parameter diversity order for the stationary Markov refresh kernel. Rodríguez and Quintana (2014) gave species-partition expressions for the iid residual-allocation setting. Existing stochastic-ordering and weighted-integral techniques provide the proof tools, not a direct covering theorem among the inspected sources.

## Limitations

This is an **annealed** ordering, for expectations of functionals of random weights. It does not establish pathwise majorization, stochastic domination of the random Simpson index itself, monotonicity of expected Rényi entropy, or ordering of the full species-count distribution. The exact formulas require a time-homogeneous stationary refresh kernel; a general dependent, nonstationary Markov stick-breaking construction need not share them. The \(0<q<1\) closed-interval result and the Shannon result have the stated integrability restrictions. Historical-priority assessment is based on the cited accessible full texts and targeted searches, not proof of global uniqueness; an unlocated general ordering theorem remains a possible source of overlap.

## References

1. M. F. Gil-Leyva, A. Lijoi, R. H. Mena and I. Prünster, *Markov Stick-breaking Processes*, arXiv:2601.16561, first public version January 23, 2026, https://arxiv.org/abs/2601.16561, especially Section 5 and the appendices on clustering probabilities.
2. M. F. Gil-Leyva and R. H. Mena, *Stick-breaking processes with exchangeable length variables*, arXiv:2008.04475, first public version August 11, 2020, https://arxiv.org/abs/2008.04475, especially Section 4.
3. A. Rodríguez and F. A. Quintana, *On species sampling sequences induced by residual allocation models*, 2014, https://pmc.ncbi.nlm.nih.gov/articles/PMC4247178/, especially the iid length-variable species-partition formula.
