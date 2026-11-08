# Sharp directed Condorcet-cycle asymptotics in the three-alternative Mallows model

## Finding

Let \(n\) tend to infinity through odd positive integers. Suppose \(n\) voters independently draw strict rankings of three alternatives \(A,B,C\) from the Kendall-distance Mallows model centered at \(A\succ B\succ C\), with a fixed dispersion parameter \(0<\phi<1\). Put
\[
Z=(1+\phi)(1+\phi+\phi^2),\qquad
p=\frac{\phi^2(2+\phi)}{Z},\qquad
\beta=2\sqrt{p(1-p)}.
\]
The probability that the strict pairwise-majority relation forms a three-cycle satisfies the sharp equivalent
\[
\boxed{\Pr(\mathrm{cycle})
=\left(1+O_{\phi}(n^{-1})\right)
\sqrt{\frac{2}{\pi n}}\,
\frac{\sqrt{p(1-p)}}{1-2p}\,\beta^n.}
\]
More precisely, the orientation \(A\succ_M B\succ_M C\succ_M A\) alone has this equivalent. The opposite orientation \(B\succ_M A\succ_M C\succ_M B\) has strictly smaller exponential base, at most
\[
\Pr(\mathrm{opposite\ orientation})\le
\phi^{3/2}\left[\frac{2\phi(1+\sqrt\phi+\phi)}{Z}\right]^n.
\]
The ratio of that base to \(\beta\) is strictly below one at every fixed \(0<\phi<1\). Thus rare cycles concentrate on the orientation that requires a majority reversal of the most distant pair \(A,C\), while preserving both neighboring pairwise comparisons.

## Assumptions and scope

A strict ranking \(\pi\) has probability \(\phi^{\operatorname{inv}(\pi)}/Z\), where \(\operatorname{inv}(\pi)\) counts pairwise disagreements with \(A\succ B\succ C\). Ballots are identically distributed and independent; the center ranking and \(\phi\) are fixed as the odd electorate size increases. For odd \(n\) all three pairwise majority comparisons are strict, and nontransitivity is equivalent to one of two directed triangles. \(O_{\phi}\) permits a constant depending on the fixed dispersion. The result does not cover even electorates, ties, correlated voters, mixtures of centers, or the moving-parameter limit \(\phi\to1\).

The six rankings \(ABC,ACB,BAC,BCA,CAB,CBA\) have respective unnormalized weights \(1,\phi,\phi,\phi^2,\phi^2,\phi^3\). Their normalization is \(Z\). In particular,
\[
\Pr(C\succ A)=p=\frac{\phi^2(2+\phi)}{Z},\quad
1-p=\frac{1+2\phi}{Z},\quad
1-2p=\frac{(1-\phi)(1+3\phi+\phi^2)}{Z}>0.
\]

## Proof

**1. A necessary rare reversal.** Write \(I_i=\mathbf1\{C\succ A\text{ on ballot }i\}\) and \(K=\sum_{i=1}^n I_i\). Then \(K\sim\operatorname{Bin}(n,p)\). The event of the forward majority cycle, \(F_n=\{A\succ_M B,\ B\succ_M C,\ C\succ_M A\}\), is contained in \(E_n=\{K\ge(n+1)/2\}\). We prove that, conditional on \(E_n\), the other two comparisons are correct with exponentially high probability.

**2. A tilted adjacent-margin gap.** Let \(\theta=\log((1-p)/p)>0\) and change each ballot's law to
\[
Q(\pi)=\frac{P(\pi)e^{\theta\mathbf1\{C\succ A\text{ on }\pi\}}}{2(1-p)}.
\]
The denominator is \(1-p+pe^\theta=2(1-p)\). Under independent \(Q\)-ballots, \(Q(C\succ A)=1/2\), but both adjacent comparisons retain the strictly positive margin
\[
Q(A\succ B)=Q(B\succ C)
=\frac12+\delta,\qquad
\delta=\frac{1-\phi^2}{2(1+2\phi)(2+\phi)}>0.
\]
This follows by summing the six ranking weights explicitly; for example the two tilted groups for \(A\succ B\) contribute \((1+\phi)/[2(1+2\phi)]\) and \(1/[2(2+\phi)]\). Under \(Q\), each of the two adjacent pairwise-majority failures has probability at most \(e^{-2\delta^2n}\) by Hoeffding's inequality. Although the two margins can be dependent, their union is bounded by \(2e^{-2\delta^2n}\).

On \(E_n\), the Radon–Nikodym derivative satisfies
\[
\frac{dP}{dQ}=[2(1-p)]^ne^{-\theta K}
\le e^{-\theta/2}[2\sqrt{p(1-p)}]^n
=e^{-\theta/2}\beta^n.
\]
Consequently
\[
0\le\Pr(E_n)-\Pr(F_n)
\le 2e^{-\theta/2}\beta^ne^{-2\delta^2n}.
\]
The bound is exponentially smaller than the binomial tail determined in step 4.

**3. The opposite cycle is exponentially negligible.** For each ballot define \(X_i=\mathbf1\{B\succ A\}+\mathbf1\{C\succ B\}\). Its generating function is
\[
\mathbb E[z^{X_i}]
=\frac{1+2(\phi+\phi^2)z+\phi^3z^2}{Z}.
\]
An opposite cycle requires both majority inequalities \(B\succ_M A\) and \(C\succ_M B\), so \(\sum X_i\ge n+1\). Markov's inequality with \(z=\phi^{-3/2}>1\) gives
\[
\Pr(\mathrm{opposite\ cycle})
\le z^{-(n+1)}\big(\mathbb E z^{X_i}\big)^n
=\phi^{3/2}\beta_2^n,
\quad \beta_2=\frac{2\phi(1+\sqrt\phi+\phi)}Z.
\]
The first reversal's base is
\[
\beta=\frac{2\phi\sqrt{(1+2\phi)(2+\phi)}}Z.
\]
Writing \(t=\sqrt\phi\in(0,1)\) yields the strict polynomial identity
\[
(1+2t^2)(2+t^2)-(1+t+t^2)^2=(1-t)^2(1+t^2)>0.
\]
Hence \(\beta_2<\beta<1\), proving exponential separation.

**4. The sharp one-dimensional tail.** Set \(n=2m+1\). Stirling's formula gives
\[
\Pr(K=m+1)=\sqrt{\frac{2}{\pi n}}\sqrt{\frac p{1-p}}\,\beta^n
\left(1+O_p(n^{-1})\right).
\]
For each nonnegative integer \(j\), the ratio of the probability at \(m+1+j\) to that at \(m+1\) converges to \((p/(1-p))^j\); more precisely, the ratio is this power times \(1+O_p(j^2/n)\) for \(j\le n^{1/3}\). All larger terms are dominated by a geometric tail because the consecutive-mass ratio does not exceed \(p/(1-p)<1\). Summing and using \(\sum_{j\ge0}(p/(1-p))^j=(1-p)/(1-2p)\) yields
\[
\Pr(E_n)=\sqrt{\frac{2}{\pi n}}\frac{\sqrt{p(1-p)}}{1-2p}\,\beta^n\big(1+O_p(n^{-1})\big).
\]
Steps 2 and 3 remove only exponentially smaller contributions. Since the two directed cycles are disjoint and exhaust nontransitivity for odd \(n\), the claimed equivalent and its orientation statement follow. \(\square\)

## Verification

The standalone Python 3 script `verify_mallows.py` uses only the standard library. It checks the six-ballot normalizer, the remote-pair marginal, the tilted adjacent margins, both polynomial factorizations, exact weighted profile probabilities by an independent finite-state convolution, and brute-force labeled profiles for the smallest odd electorates. Its reproducible execution yields `PASS: 171 exact coefficient / rational / exhaustive checks`. The finite enumeration is evidence for implementation consistency only; the asymptotic theorem is proved in the preceding four steps, using an explicit exponential error bound, Stirling's formula, and the binomial ratio argument.

For \(\phi=1/2\) and \(n=3\), the exact cycle probability calculated by the checker is \(32/1029\). At fixed \(\phi\) the ratio of cycle probability to the corresponding remote-pair binomial majority tail tends to one, although convergence can be slow at moderate electorate sizes.

## Relationship to prior work

Mallows' ranking law is a classical model; Vitelli et al. (2014) develop probabilistic inference for it. Lackner and Lackner (2015, arXiv preprint; 2017 journal) study Mallows probabilities of single-peaked preferences and give lower bounds for that structurally different property. Xia (2020) studies general smoothed social-choice probabilities; the accessible abstract provides broad probabilistic background, not the constant below. Caizergues et al. (2025) analyze Condorcet-*winner* probabilities, including Mallows models, using multivariate analytic combinatorics. Their Section 1 explicitly places majority-relation transitivity outside their scope; in particular, their last-candidate winner asymptotic has a different rare-event geometry from the single remote-pair majority reversal controlled here. Their general coefficient framework may be adaptable, but no sharp three-alternative directed-cycle equivalent or orientation comparison was found in the examined text.

The statement is a sharp fixed-dispersion calculation for the majority-*cycle* event, not a general claim to originate the Mallows model, Condorcet paradox, exponential concentration, or large-deviation methods.

## Limitations

The equivalent is not uniform as \(\phi\uparrow1\): the strict positive margin \(\delta\) vanishes, and impartial culture has a positive limiting cycle probability. The theorem also excludes \(\phi=0\), weak majority ties, even electorate sizes, and any common latent heterogeneity or cross-voter dependence. The finite verifier cannot establish asymptotics by itself. A comprehensive search of older print-only Condorcet-paradox literature remains a residual historical-priority risk.

## References

- Vitelli, V., Sørensen, Ø., Crispino, M., Frigessi, A., and Arjas, E. (2014 preprint). *Probabilistic preference learning with the Mallows rank model*. https://arxiv.org/abs/1405.7945
- Lackner, M.-L. and Lackner, M. (2015 preprint; 2017 journal). *On the likelihood of single-peaked preferences*. https://arxiv.org/abs/1505.05852 ; https://doi.org/10.1007/s00355-017-1033-0
- Xia, L. (2020 preprint). *The Smoothed Possibility of Social Choice*. https://arxiv.org/abs/2006.06875
- Caizergues, E., Durand, F., Noy, M., de Panafieu, É., and Ravelomanana, V. (2025 preprint). *Probability of a Condorcet Winner for Large Electorates: An Analytic Combinatorics Approach*. https://arxiv.org/abs/2505.06028
