# Exact absorption-time law for source-anchored voter consensus on complete graphs

## Finding

For arbitrary integers \(n\ge 2\) and \(1\le z<n\), let \(m=n-z\). There are \(z\) permanently correct source agents and \(m\) initially incorrect non-source agents. At every integer tick a uniform random agent is selected; a source does nothing, while a non-source copies a new uniform random agent from the full population, including itself. Independent choices are made at successive ticks. Let \(T\) be the first time all agents are correct.

Define
\[
p_j=\frac{j(j+z-1)}{n^2},\qquad 1\le j\le m.
\]
Then \(0<p_j<1\) and the **entire distribution** of \(T\) is
\[
T\overset{d}=\sum_{j=1}^{m}G_j,\qquad
\Pr(G_j=k)=p_j(1-p_j)^{k-1}\quad(k=1,2,\ldots),
\]
where all \(G_j\) are independent. In particular, for \(0\le s\le1\),
\[
\mathbb E[s^T]=\prod_{j=1}^{m}\frac{p_j s}{1-(1-p_j)s},
\qquad
\mathbb E[T]=n^2\sum_{j=1}^{m}\frac1{j(j+z-1)},
\]
\[
\operatorname{Var}(T)=\sum_{j=1}^{m}\frac{1-p_j}{p_j^2}.
\]
As the \(p_j\) are pairwise distinct, every integer \(t\ge0\) satisfies the exact survival identity
\[
\Pr(T>t)=\sum_{j=1}^{m}(1-p_j)^t
\prod_{\substack{1\le k\le m\\k\ne j}}
\frac{p_k}{p_k-p_j}.
\]
Consequently, with \(n,z\) fixed and \(t\to\infty\),
\[
\Pr(T>t)\sim\frac{m(z+1)}n\left(1-\frac z{n^2}\right)^t.
\]
The all-incorrect non-source starting state also maximizes the law of \(T\) in stochastic order among all binary starting states with the same sources.

For each **fixed** positive integer \(z\) and \(n\to\infty\),
\[
\frac{T}{n^2}\ \xrightarrow{d}\ Y_z=\sum_{j=1}^{\infty}E_j,
\qquad E_j\text{ independent},\quad E_j\sim\operatorname{Exp}(j(j+z-1)).
\]
This infinite sum is almost surely finite, and its limit law is nondegenerate, with
\[
\Pr(Y_z>t)\sim(z+1)e^{-zt}\quad(t\to\infty).
\]
For one source, Euler's product gives the explicit transform
\[
\mathbb E[e^{-sY_1}]=\prod_{j=1}^{\infty}\frac{j^2}{j^2+s}
=\frac{\pi\sqrt{s}}{\sinh(\pi\sqrt{s})}\quad(s\ge0),
\]
where the expression at \(s=0\) is defined by continuity. In particular, \(\mathbb E[T]/n^2\to\pi^2/6\) for one source.

## Assumptions and scope

All assertions use discrete random-sequential updates, full-population sampling **with replacement**, and self-inclusion. Selecting a source consumes one tick without changing it. Sources all hold the same correct binary opinion forever. The geometric convention has support \(\{1,2,\ldots\}\). The sharp fixed-population tail is a limit in \(t\) for each fixed \(n,z\); the subsequent exponential-sum limit takes \(n\) to infinity while \(z\) is held fixed. No assertion covers arbitrary interaction graphs, heterogeneous influence rates, parallel updating or competing fixed sources.

## Proof

**1. Graphical duality with anchored sources.** Fix a deterministic horizon \(t\). Expose the random copying arrows in reverse chronological order, beginning with one ancestry tracer at each of the \(n\) present-day agent sites. Whenever an arrow selects a non-source site occupied by an active tracer, move that tracer to the sampled predecessor site; when two tracers meet, merge them. Tracers reaching any permanent source can be discarded as *anchored*: their time-zero opinion is necessarily correct. Source updates are identity arrows. Because all non-source agents were initially incorrect, the forward population is all correct at time \(t\) if and only if every backward tracer has been anchored after processing these \(t\) arrows. This is exact equality of events for the same arrow array, not an approximation.

**2. A closed pure-death count.** Suppose \(j\ge1\) unanchored tracers remain, occupying distinct non-source sites. A single backward arrow can reduce their number only if its selected target is one of those \(j\) sites and its independently selected predecessor lies in either one of the \(z\) permanent-source sites or one of the \(j-1\) other currently occupied tracer sites. Thus the exact one-tick decrease probability, irrespective of their actual locations, is
\[
\frac jn\cdot\frac{z+j-1}n=p_j.
\]
Otherwise the number stays at \(j\), although tracer positions can change. Since arrows are independent across times, the decreasing count is a homogeneous pure-death Markov chain with holding probabilities \(p_j\). Starting at \(m=n-z\), the holding times at successive levels \(m,m-1,\ldots,1\) are mutually independent geometric variables. Reversal of a finite i.i.d. arrow array does not change its law, so this backward absorption time has exactly the same law as forward \(T\). This proves the sum representation.

**3. Finite law and sharp survival.** Multiplying geometric generating functions gives the first identity, and summing independent means and variances gives the moments. Set \(a_j=1-p_j\). Partial fractions of \(\prod_j p_js/(1-a_js)\), or the generating function for \(\Pr(T>t)\), gives the displayed survival formula. The bases \(a_1>a_2>\cdots>a_m\ge0\) are strictly ordered, so only the term with \(j=1\) remains at exponential scale. Its exact coefficient telescopes:
\[
\prod_{k=2}^{m}\frac{p_k}{p_k-p_1}
=\prod_{k=2}^{m}\frac{k(k+z-1)}{(k-1)(k+z)}
=\frac{m(z+1)}{m+z}=\frac{m(z+1)}n.
\]
For \(m=1\) the empty product equals one. The result follows for every admissible fixed \(n,z\).

**4. Limiting law and its tail.** With \(z\) fixed, for each fixed \(j\), \(G_j/n^2\) converges to an exponential variable of rate \(j(j+z-1)\) as \(n\to\infty\). The expected normalized contribution from all indices \(j>J\) is at most \(\sum_{j>J}1/[j(j+z-1)]\), tending to zero as \(J\to\infty\). This uniform truncation bound and finite-dimensional independence establish convergence to \(Y_z\); summability of its mean proves almost-sure finiteness. Writing \(Y_z=E_1+R\), the variable \(R=\sum_{j\ge2}E_j\) has a finite exponential moment at some rate strictly greater than \(z\), because its smallest exponential rate is \(2(z+1)>z\) and the reciprocal rates are summable. Conditioning on \(R\), then using dominated convergence, yields
\[
\lim_{t\to\infty}e^{zt}\Pr(Y_z>t)
=\mathbb E[e^{zR}]
=\prod_{j=2}^{\infty}\frac{j(j+z-1)}{(j-1)(j+z)}
=z+1.
\]
For \(z=1\), the Euler hyperbolic-sine product evaluates the displayed Laplace transform. Stochastic worst-case dominance follows by coupling every binary starting assignment with the all-incorrect assignment using the same directed copying arrows: every correct site in the latter remains correct in the former at each time.

## Verification

The accompanying standalone `verify.py` checks, using exact rational arithmetic and separate forward-state and backward-holding calculations, all \(55\) pairs \(2\le n\le11\), \(1\le z<n\), at each of \(14\) time points \(0\le t\le13\), totaling \(770\) full-CDF and finite spectral-survival comparisons. It also checks the leading-tail coefficient by an independent rational product for each pair. Running `python verify.py` gives a `PASS` result. These finite checks do not establish the infinite statements; Steps 1–4 above are the proofs.

## Relationship to prior work

Becchetti, Clementi, Korman, Pasquale, Trevisan and Vacus (2023), Section 4, analyze the **same sequential copying model** through a reversible birth-death chain and give asymptotic upper bounds on mean and high-probability consensus time; their source also treats several permanent sources. The present distribution-level claim uses anchored ancestry to obtain a factorized exact transform, finite-time law, the sharp slowest-mode coefficient, and a fixed-source scaling distribution. Those statements are not established by the bounds in that source.

Fudolig and Esguerra (2014) analyze **exact mean** consensus time for single-type zealots on complete graphs. The mean displayed here is not asserted to be new. Their full text could not be inspected, so priority for the additional distributional formulas remains uncertain. Pickering and Lim (2014/2015) obtain full spectral distributions for the **unanchored** complete-graph voter chain, while Aldous and Fill describe pure-death coalescence on complete graphs without absorbing fixed sources. Hathcock and Strogatz (2018) derive neutral Moran fixation-time laws without committed sources. D'Archivio and Vacus (2024) use backward ancestries for a voter upper bound in a **parallel-round** protocol. These existing tools motivate the construction but do not explicitly supply the fixed-source sequential full law as presented.

## Limitations

The model is a homogeneous complete graph with a common correct opinion and random-sequential updates. Exact distribution formulas do not imply universality for structured networks, opinion-dependent sampling, noisy copying or parallel rounds. The continuous scaling limit holds for **fixed** \(z\), not for sources growing proportionally with population. The precise full-distribution priority comparison with the inaccessible 2014 paper remains unresolved, and independent validation has not been carried out. A geometric-convolution representation is a classical type of Markov-chain consequence; the proposed contribution is its exact source-anchored specialization and accompanying sharp distributional and scaling information, not invention of coalescing duality or the basic mean analysis.

## References

1. L. Becchetti et al., *On the Role of Memory in Robust Opinion Dynamics*, first public 2023-02-16, https://arxiv.org/abs/2302.08600 .
2. M. I. D. Fudolig and J. P. H. Esguerra, *Analytic treatment of consensus achievement in the single-type zealotry voter model*, Physica A 413 (2014), 626–634, https://doi.org/10.1016/j.physa.2014.07.033 .
3. N. D'Archivio and R. Vacus, *On the Limits of Information Spread by Memory-Less Agents*, DISC 2024, https://doi.org/10.4230/LIPIcs.DISC.2024.18 .
4. W. Pickering and C. Lim, *Solution of the Voter Model by Spectral Analysis*, https://arxiv.org/abs/1408.2130 .
5. D. Hathcock and S. H. Strogatz, *Fitness dependence of the fixation-time distribution for evolutionary dynamics on graphs*, https://arxiv.org/abs/1812.05652 .
6. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, §14.3, https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch14.S3.html .
