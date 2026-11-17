# Sharp complete-pair Gini amplification of the Ehrenfest urn step

## Finding
For every integer \(n\ge1\), let \(E_n\) be the one-step observable Markov operator of the classical two-urn Ehrenfest process with \(n\) labeled balls, on the states \(\{0,1,\ldots,n\}\). For any real signal \(f\), put
\[
G_n(f)=\sum_{0\le i<j\le n}|f_i-f_j|.
\]
Then the exact induced seminorm on real signals modulo constants is
\[
\boxed{\sup_{G_n(f)>0}\frac{G_n(E_nf)}{G_n(f)}=
\begin{cases}1,&n=1,2,\\[2pt]
1+\frac{2(n-2)}{n^2},&n\ge3.
\end{cases}}
\]
For \(n\ge3\), indicators of the states \(1\) and \(n-1\) attain equality. Thus nonexpansivity holds exactly with one or two balls, and every larger urn admits complete-pair Gini amplification. Across all ball counts the largest coefficient is exactly \(5/4\), attained at \(n=4\); the coefficient decreases to \(1\) as \(n\to\infty\).

## Assumptions and scope
The state \(i\) represents the number of balls in a designated urn. One ball is chosen uniformly and moved to the other urn at each step. The corresponding row-stochastic operator is
\[
(E_nf)_i=\frac{i}{n}f_{i-1}+\frac{n-i}{n}f_{i+1},\qquad 0\le i\le n,
\]
where zero-coefficient boundary terms are omitted. The signal coordinates are real and equally weighted in \(G_n\). This is a one-step result, not an assertion about every power or the continuous-time semigroup. In particular, \(G_n\) is not the weighted total-variation distance between probability distributions.

## Proof
**1. Exact reduction to cuts.** Write \(N=n+1\). For a row-stochastic operator \(T\), one has \(T\mathbf1=\mathbf1\). Every nonconstant real vector admits the layer decomposition
\[
f=(\min_i f_i)\mathbf1+\int_{\min f}^{\max f}\mathbf1_{\{i:f_i>t\}}\,dt.
\]
The triangle inequality for the seminorm and the coarea identity give
\[
G_n(Tf)\le\int G_n(T\mathbf1_{S_t})\,dt,\qquad
G_n(f)=\int |S_t|(N-|S_t|)\,dt.
\]
Since indicators are admissible signals, the induced seminorm equals
\[
\max_{\varnothing\ne S\subsetneq\{0,\ldots,n\}}
\frac{G_n(T\mathbf1_S)}{|S|(N-|S|)}.
\]

**2. Non-singleton bound, valid for every \(n\ge3\).** Because \(E_n\mathbf1=\mathbf1\), complements yield the same ratio. It suffices to examine cuts of size \(s\le N/2\). Let \(b\in\{0,1,2\}\) count which endpoints \(0,n\) belong to \(S\). The column sums of \(E_n\) are \((n+2)/n\) on interior states and \(1/n\) at the endpoints. For \(y=E_n\mathbf1_S\), therefore,
\[
0\le y_i\le1,\qquad M:=\sum_i y_i=s+\delta,
\qquad \delta=\frac{2s-Nb}{n}\le\frac{2s}{n}.
\]
For any \(N\) numbers \(y_i\in[0,1]\), the pairwise elementary inequality
\[
|y_i-y_j|\le y_i(1-y_j)+y_j(1-y_i)
\]
implies \(G_n(y)\le M(N-M)\). If \(s\ge2\), then \(N-2s\ge0\) and
\[
\begin{aligned}
G_n(y)-s(N-s)
&\le\delta(N-2s)-\delta^2\\
&\le\frac{2s}{n}(N-2s)\\
&\le\frac{2(n-2)}{n^2}s(N-s).
\end{aligned}
\]
For the last step, after multiplying by the positive factor \(n^2/(2s)\), the inequality is precisely \((n+2)s\ge 2(n+1)\), valid because \(s\ge2\). If \(\delta<0\), the middle bound remains valid since \(\delta(N-2s)-\delta^2\le0\). Thus every cut of size at least two, after complementing if necessary, obeys the proposed operator bound. The argument is valid for all integer \(n\ge3\), without a finite-size extrapolation.

**3. Sharp singleton bound.** For \(j=0\) or \(j=n\), the output of \(\mathbf1_{\{j\}}\) has exactly one nonzero entry of size \(1/n\), giving ratio \(1/n\). For any interior \(1\le j\le n-1\), the output has exactly two nonzero entries, at positions \(j-1,j+1\), with values \((n-j+1)/n\) and \((j+1)/n\). Hence, using \(G_n(\mathbf1_{\{j\}})=n\),
\[
\frac{G_n(E_n\mathbf1_{\{j\}})}{G_n(\mathbf1_{\{j\}})}
=\frac{(n-1)(n+2)+|n-2j|}{n^2}
\le1+\frac{2(n-2)}{n^2}.
\]
For \(n\ge3\), equality holds when \(j=1\) or \(j=n-1\), establishing sharpness. For \(n=2\), direct inspection of singleton cuts gives coefficient \(1\); for \(n=1\), the operator swaps two entries and preserves \(G_1\). The function \(1+2(n-2)/n^2\) increases up to real \(n=4\), then decreases, completing the asserted finite and asymptotic conclusions.

**4. Why this does not contradict reversibility.** The stationary measure of the count chain is the binomial law \(\pi_i=2^{-n}\binom ni\). Under the weighted pair seminorm
\[
G_\pi(f)=\sum_{i<j}\pi_i\pi_j|f_i-f_j|,
\]
ordinary Markov-Jensen conditioning and stationarity give \(G_\pi(E_nf)\le G_\pi(f)\). This last inequality is a standard consequence of stationarity, not a separate novelty assertion. The amplification found above concerns **equal** weights on the count states, rather than their binomial equilibrium weights.

## Verification
The accompanying standard-library Python checker performs exact-integer enumeration of all nontrivial binary cuts up to fourteen balls (32,752 representative cuts), verifies the non-singleton mass envelope through one hundred balls, checks the closed-form singleton witnesses through one hundred balls, tests 300 additional rational signals, and confirms binomial stationarity through nineteen balls. It reports `ALL_EHRENFEST_GINI_CHECKS_PASSED` when all checks pass. Execute `python3 check_ehrenfest_gini.py` in a directory containing that file. The proof above, not the finite enumeration, establishes the claim for all ball counts.

## Relationship to prior work
Mizukawa's 2010 Gelfand-pair treatment identifies the Ehrenfest walk and derives spectral/mixing statements in group-theoretic form. Fill and Kahn's 2011 comparison theory controls Markov-chain mixing and distributional distances for birth-and-death chains. Diaconis and Griffiths (2012) investigate Bernoulli exchangeability and Krawtchouk eigenfunctions of Ehrenfest urns. Those inspected results do not supply the exact induced complete-pair Gini seminorm of a one-step observable operator. A published analysis of the continuous-time Ehrenfest semigroup in counting \(\ell^1\) concerns a different norm and time evolution. General comparisons between Gini and oscillation coefficients give broader nonsharp bounds, not the particular coefficient derived above. The available evidence is not a proof of historical priority.

## Limitations
The result concerns the standard two-urn, one-ball-per-step count chain and unweighted Gini variation of real observables. It does not determine all higher-step Gini norms, continuous-time Gini decay, or analogous constants for more than two urns. The full text of Diaconis and Griffiths (2012) was unavailable at review; its abstract and bibliographic material were examined, leaving a specific historical-coverage uncertainty. The earliest precisely dated cited public source is the 2010 arXiv preprint, not the historical invention date of the Ehrenfest model.

## References
1. Hiroshi Mizukawa, *Finite Gelfand Pair Approaches for Ehrenfest Diffusion Model*, arXiv:1009.1205v1, publicly posted 7 September 2010. https://arxiv.org/abs/1009.1205
2. James Allen Fill and Jonas Kahn, *Comparison Inequalities and Fastest-Mixing Markov Chains*, arXiv:1109.6075v1, publicly posted 28 September 2011. https://arxiv.org/abs/1109.6075
3. Persi Diaconis and Robert Griffiths, *Exchangeable Pairs of Bernoulli Random Variables, Krawtchouck Polynomials, and Ehrenfest Urns*, Australian & New Zealand Journal of Statistics 54 (2012), 81–101, first online 4 May 2012. DOI:10.1111/j.1467-842X.2012.00654.x
