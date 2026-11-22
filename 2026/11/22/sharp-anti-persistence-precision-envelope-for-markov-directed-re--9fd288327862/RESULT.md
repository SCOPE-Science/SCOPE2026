# Sharp anti-persistence precision envelope for Markov-directed renewal transport

## Finding

Consider complete-cycle transport with a stationary binary Markov orientation process and independent, identically distributed cycle lengths and reward magnitudes. Write \(m\) for mean orientation, \(\rho\) for its one-step centered autocorrelation, \(a=\mathbb E R\), \(b=\mathbb E N\), and \(d=\operatorname{Var}(R-aN/b)\). The exact time-asymptotic current variance is

\[
\sigma^2(\rho)=\frac{(1-m^2)\left[\operatorname{Var}(R)+a^2\frac{1+\rho}{1-\rho}\right]+m^2d}{b}.
\]

At every fixed nonzero mean orientation \(0<|m|<1\), among *all* irreducible stationary two-state Markov orientations having this mean, the exact minimum is

\[
\boxed{\sigma^2_{\min}=\frac{(1-m^2)[\operatorname{Var}(R)+|m|a^2]+m^2d}{b}.}
\]

The minimum is attained by always switching away from the minority orientation and switching away from the majority orientation with probability \((1-|m|)/(1+|m|)\). It therefore remains sharp for arbitrarily correlated bounded reward-duration pairs, provided those pairs are independent across cycles and independent of the entire orientation chain.

Consequently, a marginal-sign reversal-information bound valid for independent orientations does **not** extend to Markov-correlated orientations without a memory correction. With deterministic unit cycles and stationary sign probabilities \(3/4,1/4\), the maximizing anti-persistent orientation matrix is

\[
P=\begin{pmatrix}2/3&1/3\\1&0\end{pmatrix}.
\]

The mean current is \(1/2\), the asymptotic variance is \(3/8\), and their precision ratio equals \(2/3\). In contrast, substituting the same one-time sign law into the independent-orientation reversal-information bound gives only \((\sqrt3-1)/2<2/3\). This is a boundary counterexample outside that bound's published independence assumptions, not a contradiction within its stated domain.

## Assumptions and scope

Let \((N_i,R_i)_{i\ge1}\) be independent copies of a random pair such that \(0<n_-\le N_i\le n_+<\infty\) and \(0\le R_i\le r_+<\infty\), with deterministic positive constants. The two components of each pair may be dependent. Let \((X_i)_{i\ge1}\) be an irreducible stationary homogeneous Markov chain on \(\{-1,+1\}\), independent of the *entire* sequence of pairs, with \(m=\mathbb E X_i\) satisfying \(0<|m|<1\). Define \(T_n=\sum_{i=1}^nN_i\), \(\nu(t)=\max\{n:T_n\le t\}\), and the complete-cycle current \(J(t)=\sum_{i=1}^{\nu(t)}X_iR_i\). No current is credited for the unfinished final cycle.

The Markov chain is assumed aperiodic, which is automatic for the minimizing transition matrix when \(m\ne0\). Define \(\rho=\operatorname{Cov}(X_i,X_{i+1})/(1-m^2)\), so \(-1<\rho<1\). The current rate is \(j=\lim_{t\to\infty}\mathbb E J(t)/t=ma/b\) and \(\sigma^2=\lim_{t\to\infty}\operatorname{Var}(J(t))/t\). A nonzero \(a\) is needed only to interpret positive-current precision; the variance theorem also covers \(a=0\).

## Proof

**1. Two-state orientation covariance.** The centered function \(X_i-m\) spans the one-dimensional nonconstant eigenspace of any stationary two-state transition matrix. Its eigenvalue is \(\rho=1-p_{+-}-p_{-+}\). Hence \(\operatorname{Cov}(X_i,X_{i+k})=(1-m^2)\rho^k\) for every integer \(k\ge0\).

**2. Exact variance decomposition under renewal stopping.** Conditional on all durations and rewards, the number \(\nu(t)\) and the reward sequence are fixed, while the orientations retain their stationary Markov law. Therefore

\[
\begin{split}
\operatorname{Var}J(t)={}&m^2\operatorname{Var}\left(\sum_{i\le\nu(t)}R_i\right)\\
&+(1-m^2)\mathbb E\left[\sum_{i\le\nu(t)}R_i^2+2\sum_{k\ge1}\rho^k\sum_{i\le\nu(t)-k}R_iR_{i+k}\right].
\end{split}
\]

By the strong law and the boundedness assumptions, \(\nu(t)/t\to1/b\) almost surely and in mean. For any fixed \(k\), the stationary \(k\)-dependent sequence \((R_iR_{i+k})_i\) obeys the strong law with mean \(a^2\); bounded convergence yields

\[
\lim_{t\to\infty}\frac1t\mathbb E\sum_{i\le\nu(t)-k}R_iR_{i+k}=\frac{a^2}{b}.
\]

Likewise the diagonal reward-square contribution converges to \(\mathbb E R^2/b\). The bound \(\nu(t)\le t/n_-\), together with \(|\rho|<1\), justifies interchanging the limit and the geometrically weighted sum over \(k\).

For the variance of the unsigned renewal reward, put \(c=a/b\) and \(Y_i=R_i-cN_i\), which are bounded independent mean-zero increments of variance \(d\). The index \(\nu(t)+1\) is a stopping time; the stopped-martingale second-moment identity gives \(\mathbb E(\sum_{i=1}^{\nu(t)+1}Y_i)^2=d\,\mathbb E(\nu(t)+1)\). Since replacing \(\nu(t)+1\) by \(\nu(t)\), and replacing \(cT_{\nu(t)}\) by \(ct\), changes the sum by bounded amounts, Cauchy--Schwarz shows that these changes affect its variance by \(o(t)\). Thus

\[
\lim_{t\to\infty}\frac1t\operatorname{Var}\left(\sum_{i\le\nu(t)}R_i\right)=\frac{d}{b}.
\]

Substituting these limits into the conditional decomposition and summing \(\sum_{k\ge1}\rho^k=\rho/(1-\rho)\) proves

\[
\sigma^2=\frac{m^2d+(1-m^2)[\mathbb ER^2+2a^2\rho/(1-\rho)]}{b},
\]

which is equivalent to the asserted formula because \(\mathbb ER^2=\operatorname{Var}(R)+a^2\).

**3. Sharp extremizer.** Let \(\pi_+=(1+m)/2\), \(\pi_-=(1-m)/2\). Stationarity requires \(\pi_+p_{+-}=\pi_-p_{-+}\); both transition probabilities are at most one. Thus

\[
\rho\ge-\frac{1-|m|}{1+|m|},\qquad
\frac{1+\rho}{1-\rho}\ge|m|.
\]

Equality occurs when a minority-sign visit is always followed by a majority-sign visit; the reverse switching probability is \((1-|m|)/(1+|m|)\). This matrix is irreducible and aperiodic for \(0<|m|<1\). Since the exact variance increases strictly with \(\rho\) whenever \(a\ne0\), this gives the unique minimizing transition matrix (up to exchanging sign labels). The formula also establishes the minimum when \(a=0\), though every transition matrix then ties.

**4. Explicit failure of a memory-blind precision constraint.** Set \(N_i=R_i=1\) and the transition matrix in the Finding. Then \(m=1/2\), \(\rho=-1/3\), and \(\sigma^2=(1-m^2)(1+\rho)/(1-\rho)=3/8\), while \(j=1/2\). The independent-orientation expression \(\frac12(e^{s_X}-1)\) uses \(s_X=m\log[(1+m)/(1-m)]=(\log3)/2\), giving \((\sqrt3-1)/2\). Strict inequality follows from \(7/3>\sqrt3\). No interpretation of \(s_X\) as full physical entropy production for the Markov process is asserted: it is the fixed *single-sign reversal information* used for the comparison.

## Verification

The included `verify.py` requires only the Python standard library. It checks exact finite-horizon first and second sign-sum moments by independent Markov-moment recursion and covariance summation; verifies the optimal transition-matrix inequality for rational parameters; and independently computes a genuine random-duration example using the principal eigenvalue of a tilted Markov renewal transfer kernel.

For \(N\in\{1,2\}\) equiprobably, \(R=1\), and the same Markov sign matrix, one obtains \(j=1/3\), \(d=1/9\), \(\sigma^2=29/108\) and precision \(12/29\). The independent tilted-kernel check derives \(29/108\) by differentiating the equation \(\lambda(s)[e^{-k(s)}+e^{-2k(s)}]/2=1\), where \(\lambda(s)\) is the top eigenvalue of \(\operatorname{diag}(e^s,e^{-s})P\). This finite example independently checks the random-time normalization; it is not substituted for the general proof.

## Relationship to prior work

Karimi and Jafarpour (2026) derive an inequality for independent orientations \(X_i\) that are independent of identically distributed cycle pairs \((N_i,R_i)\), and they allow correlations *within* each cycle's reward. The present theorem changes the distinct independence assumption between orientations at different renewals. It gives an exact Markov-memory correction, a sharp optimization over all two-state orientation transitions with fixed marginal, and a boundary example for any attempt to apply the independent-orientation inequality unchanged.

Shreshtha and Harris (2019) provide earlier renewal-reward uncertainty relations. More general Markov-renewal central limit and asymptotic-variance methods, as well as reversible-chain variance comparison theory, supply broad mathematical context; the present claim is the specific marked-cycle sharp extremizer and its direct comparison to marginal-sign reversal information, not novelty of the Green--Kubo covariance sum or of renewal-reward variance theory itself. The independent-sign bias optimization and finite-time anti-persistent binary Markov occupation-count literature address different optimizations/observables.

## Limitations

The result assumes bounded strictly positive cycle durations, bounded rewards, independence between the orientation process and all cycle marks, and an *exactly two-state, first-order stationary Markov* orientation. It does not claim a physical entropy-production inequality for general Markov protocols; the entropy cost of implementing temporal correlations is unspecified. It concerns rewards credited at completed cycles, not the physical motion within an unfinished cycle. Unbounded-duration and higher-state analogues are unproved. No claim of priority over unindexed or inaccessible specialized Markov-renewal literature is made.

## References

1. F. Karimi and F. H. Jafarpour, *Thermodynamic Uncertainty Relation For a Multi-Phase Alternating Renewal Random Walk*, arXiv:2606.16339 (first posted 2026-06-15), https://arxiv.org/abs/2606.16339.
2. M. Shreshtha and R. J. Harris, *Thermodynamic uncertainty for run-and-tumble type processes*, arXiv:1903.01972 (2019), https://arxiv.org/abs/1903.01972.
3. S. P. Clark and P. Kiessler, *A Diffusion Approximation for Markov Renewal Processes*, Journal of Applied Probability 44 (2007), DOI:10.1239/jap/1183667407.
4. G. T. Salmon and J. S. Rosenthal, *Comparing the Efficiency of General State Space Reversible MCMC Algorithms*, Advances in Applied Probability (2026), publisher article title and year; no unverified DOI asserted.
