# The fixed-point–inversion sign geometry of Ewens permutations

## Finding
Let \(\pi\) have the Ewens distribution on \(S_n\) with parameter \(\theta>0\), let \(F_k=\mathbf1\{\pi(k)=k\}\), let \(Y_{ab}=\mathbf1\{\pi(a)>\pi(b)\}\), and let \(I_n=\sum_{a<b}Y_{ab}\). All assertions below hold for every integer \(n\ge3\) unless a limit is explicitly taken.

For \(1\le a<b\le n\), write \(d=b-a\). For every \(k\notin\{a,b\}\),
\[
\operatorname{Cov}(F_k,Y_{ab})=\frac{\theta(1-\theta)}{(n+\theta-1)^2(n+\theta-2)(n+\theta-3)}
\begin{cases}
2d+\theta-2,&k<a\ \text{or}\ k>b,\\
2d-n-1,&a<k<b.
\end{cases}
\]
The outside coefficient is strictly positive, so its covariance has the sign of \(1-\theta\); an inside position changes sign at \(2d=n+1\), and its covariance is exactly zero on that line. For incident positions the conditional probabilities given \(F_k=1\) are \((a-1)/(n+\theta-2)\) for \(k=a\), and \((n-b)/(n+\theta-2)\) for \(k=b\), giving the remaining entries of the complete mixed covariance tensor.

Set \(c_n=(n+1)/2\) and
\[
H_n(\theta)=\frac{(n-1)(1-\theta)[(n-3)(2n-1)+3(n-1)\theta]}{12(n+\theta-3)(n+\theta-1)}.
\]
Then the exact fixed-position covariance profile is
\[
\boxed{\operatorname{Cov}(F_k,I_n)=\frac{2\theta}{(n+\theta-1)(n+\theta-2)}\bigl(H_n(\theta)-(k-c_n)^2\bigr).}
\]
For \(\theta>1\) every entry is strictly negative. At \(\theta=1\) every entry is nonpositive, with one zero precisely when \(n\) is odd and \(k=c_n\). For \(0<\theta<1\), the positive entries are *exactly* the positions satisfying \(|k-c_n|<\sqrt{H_n(\theta)}\); the equality case gives zero and all remaining positions give negative covariance.

For fixed \(0<\theta<1\), the positive central window has \(2\sqrt{(1-\theta)n/6}+O_\theta(1)\) positions. More precisely, if \((k_n-c_n)/\sqrt n\to u\),
\[
 n\operatorname{Cov}(F_{k_n},I_n)\longrightarrow 2\theta\bigl((1-\theta)/6-u^2\bigr).
\]
At the sharper uniform-bias crossover \(\theta_n=1-\lambda/n\) with fixed \(\lambda\ge0\) and fixed admissible integer or half-integer displacement \(k_n-c_n=r\),
\[
 n^2\operatorname{Cov}_{\theta_n}(F_{k_n},I_n)\longrightarrow 2(\lambda/6-r^2).
\]
The limit describes strict signs when its value is nonzero; it does not decide the exact-boundary case \(\lambda=6r^2\).

Despite the positive *local* window for every \(0<\theta<1\), the *total* fixed-point count \(F=\sum_kF_k\) always has strictly negative covariance with inversions:
\[
\boxed{\operatorname{Cov}(F,I_n)=-\frac{n\theta(n-1)\{n(n-2)(n-3)+[4n(n-3)+2]\theta+(4n-2)\theta^2\}}{6(n+\theta-3)(n+\theta-2)(n+\theta-1)^2}<0.}
\]
For every fixed \(\theta>0\), this is \(-\theta n/6+O_\theta(1)\).

## Assumptions and scope
The sample space is the set of all permutations \(\pi:[n]\to[n]\), with probability \(\theta^{\#\mathrm{cycles}(\pi)}/\prod_{j=0}^{n-1}(\theta+j)\). Inversions are defined through the **images** \(\pi(a)>\pi(b)\). The law is invariant under inversion of the permutation, so the corresponding total-count formulas also apply under the preimage convention; the indexed mixed tensor is stated for the image convention. The theorem excludes \(\theta=0\), where a single fixed point has probability zero for \(n\ge2\). Every denominator above is positive for \(n\ge3\) and \(\theta>0\). Strict inequalities refer to nonzero covariance, not independence.

## Proof
**Partial-arrow Ewens weights.** Fix \(r\) mutually consistent specified directed arrows in the permutation diagram. Contracting the resulting directed paths into vertices gives the Ewens normalization on \(n-r\) remaining supervertices; every completely closed cycle contributes one additional factor \(\theta\). Hence the probability of two specified arrows is \(\theta^q/[(n+\theta-1)(n+\theta-2)]\), with \(q\) the number of already closed directed cycles. For the inversion event \(\pi(a)>\pi(b)\) there are \(\binom n2\) distinct ordered image choices, of which the choices creating one closed cycle are \(a-1\) loops at \(a\), \(n-b\) loops at \(b\), and one two-cycle \(a\leftrightarrow b\). No inversion choice closes two cycles. Thus
\[
 p_n(d):=\Pr(Y_{ab}=1)=\frac{\binom n2+(\theta-1)(n-d)}{(n+\theta-1)(n+\theta-2)}.
\]
Summing over gaps yields the known mean
\[
 Q_n:=\mathbb E I_n=\frac{n^2(n-1)^2/4+(\theta-1)n(n-1)(2n-1)/6}{(n+\theta-1)(n+\theta-2)}.
\]
The mean and marginal pair formula are not claimed as new; they agree with Pinsky–Schickentanz, Theorem 1.

**Deletion at a designated fixed point.** The probability of \(F_k=1\) is \(\theta/(n+\theta-1)\). Conditioned on this event, deleting \(k\) and order-preservingly relabelling the other \(n-1\) positions leaves an Ewens permutation with the same parameter. If \(k\notin\{a,b\}\), the pair's new gap is \(d-\mathbf1_{a<k<b}\), giving the conditional probability \(p_{n-1}(d-\mathbf1_{a<k<b})\). For \(k=a\) or \(k=b\), a direct one-arrow calculation gives the respective incident conditional probabilities recorded above. Subtract \(p_n(d)\), multiply by \(\theta/(n+\theta-1)\), and factor the resulting rational functions to obtain the displayed complete tensor. In the nonincident case these simplify, respectively, to the numerator factors \(\theta(1-\theta)(2d+\theta-2)\) and \(\theta(1-\theta)(2d-n-1)\).

**Total inversions incident to a fixed position.** When \(F_k=1\), the expected inversion count among the other \(n-1\) labels is \(Q_{n-1}\). Each of the \(k-1\) earlier positions has conditional probability \((n-k)/(n+\theta-2)\) of mapping above \(k\), and each of the \(n-k\) later positions has probability \((k-1)/(n+\theta-2)\) of mapping below \(k\). Consequently
\[
 \mathbb E[I_n\mid F_k=1]=Q_{n-1}+\frac{2(k-1)(n-k)}{n+\theta-2}.
\]
Using \((k-1)(n-k)=(n-1)^2/4-(k-c_n)^2\) and substituting the explicit rational functions \(Q_n,Q_{n-1}\) gives precisely \(H_n(\theta)\) and the boxed profile. The factor \([(n-3)(2n-1)+3(n-1)\theta]\) is strictly positive, including at \(n=3\), so \(H_n\) has exactly the sign of \(1-\theta\). The complete position and equality classification follows.

**Global sign and scaling.** Summing the position profile and using \(\sum_{k=1}^{n}(k-c_n)^2=n(n^2-1)/12\) gives the boxed formula for \(\operatorname{Cov}(F,I_n)\). All coefficients of its numerator's bracket are nonnegative for \(n\ge3\) and the coefficients of positive powers of \(\theta\) are strictly positive. This proves strict negativity. Finally, rational expansion gives \(H_n(\theta)=(1-\theta)n/6+O_\theta(1)\) at fixed \(\theta\), and \(H_n(1-\lambda/n)\to\lambda/6\); insert these into the exact profile to obtain both limiting laws and the positive-window count. The aggregate expansion follows from the boxed rational formula. All limits use ordinary real-valued parameters and integer indices satisfying the specified range.

## Verification
Run `python3 verify.py` using Python's standard library. The checker independently enumerates Ewens-weighted permutations for \(3\le n\le7\) over six positive rational biases, checks means, every position covariance, aggregate covariance, exact symmetry and sign boundaries; it additionally enumerates the complete three-index mixed tensor for \(3\le n\le6\) over four rational biases. The recorded result is `VERIFY_OK 1672 exact assertions`. Exact finite checks corroborate, but do not replace, the symbolic proof for all sizes and parameters. No stochastic simulation, external dataset or external code is required.

## Relationship to prior work
Kammoun's work (arXiv:1805.05253, first public 2018-05-14) treats the Ewens/conjugation-invariant permutation setting and limiting descent processes, but not this fixed-point/inversion covariance profile. Hamaker and Rhoades (arXiv:2206.06567) give far-reaching local-pattern and cycle-type moment machinery; their Section 9.6 explicitly discusses joint-distribution extensions, but does not state the exact designated-location sign classification here. Campion Loth et al. (arXiv:2301.00898) address weighted inversions and cycle-class moments, without resolving this specific fixed-index problem. Most importantly, Pinsky and Schickentanz (arXiv:2510.20654, 2025) explicitly derive the unconditional inversion mean and pair probabilities and conditioned-on-**number**-of-fixed-points inversions. Those published marginal formulas are used and fully credited: the present additional result is the designated-fixed-position mixed tensor, complete finite-size sign geometry, positive central-window/negative-aggregate contrast, and near-uniform critical scaling. They are not stated as such in the inspected paper. These consequences are algebraically accessible from the published mean combined with the standard fixed-point deletion property; novelty is therefore claimed only for the complete dependence classification, not for the unconditional marginal formulas or for a new proof of them.

## Limitations
This result gives first mixed moments, not the joint distribution or independence of the statistics. The equal-threshold near-uniform scaling case is left undecided by the leading limit, although the exact finite covariance formula still applies. The calculations are exact and reproducible, but historical priority may be affected by earlier implicit class-function, generating-function or size-biased enumerators. Independent mathematical evaluation has not been performed.

## References
- M. S. Kammoun, *Monotonous subsequences and the descent process of invariant random permutations*, arXiv:1805.05253v1, 2018. https://arxiv.org/abs/1805.05253
- Z. Hamaker and B. Rhoades, *Characters of local and regular permutation statistics*, arXiv:2206.06567, first public 2022. https://arxiv.org/abs/2206.06567
- J. Campion Loth, M. Levet, K. Liu, E. N. Stucky, S. Sundaram and M. Yin, *Permutation Statistics in Conjugacy Classes of the Symmetric Group*, arXiv:2301.00898, first public 2023. https://arxiv.org/abs/2301.00898
- R. G. Pinsky and D. T. Schickentanz, *Inversions in Random Permutations Under the Ewens Sampling Distribution With and Without a Prescribed Number of Fixed Points*, arXiv:2510.20654v2, 2025. https://arxiv.org/abs/2510.20654
- R. G. Pinsky, *The inversion statistic in derangements and in other permutations with a prescribed number of fixed points*, arXiv:2505.02058, 2025. https://arxiv.org/abs/2505.02058
