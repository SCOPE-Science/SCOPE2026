# An exact boundaryward posterior shift in finite-path epidemic source inference

## Finding

Fix integers \(n\ge4\) and \(3\le k<n\). On the path with vertices \(1,\ldots,n\), a single source starts a continuous-time susceptible–infected (SI) process at time zero. Each infected–susceptible edge transmits after an independent exponential time of rate \(\lambda>0\). At a *known* positive age \(t\), the entire infected set is observed to be precisely the prefix \(B=\{1,\ldots,k\}\). Write \(u=\lambda t\) and \(Q_r(u)=\Pr\{\operatorname{Pois}(u)\ge r\}\), with \(Q_0(u)=1\).

For each candidate source \(s\in B\), its exact snapshot likelihood is
\[
L_s(u)=e^{-u}\frac{u^{k-s}}{(k-s)!}\,Q_{s-1}(u).
\]
For *every* strictly positive prior on the candidate sources, the posterior family is strictly decreasing in the monotone-likelihood-ratio order as age increases: for all \(0<u<v\) and \(1\le s<k\),
\[
\frac{\Pr(S=s+1\mid B,v)}{\Pr(S=s\mid B,v)}
<\frac{\Pr(S=s+1\mid B,u)}{\Pr(S=s\mid B,u)}.
\]
Consequently, for each cutoff \(1\le j<k\), the posterior probability \(\Pr(S\le j\mid B,u)\) strictly increases with \(u\). This compares the posterior for the **same fixed observed prefix** at different hypothetical known ages, not the time evolution of an individual outbreak's observations.

Under the uniform source prior, let \(m=\lfloor (k-1)/2\rfloor\). There are exactly \(m\) positive thresholds \(u_1,\ldots,u_m\), defined uniquely by
\[
(k-s)Q_s(u_s)=u_s Q_{s-1}(u_s),\qquad 1\le s\le m,
\]
with strict ordering \(0<u_m<\cdots<u_2<u_1\) (when \(m\ge2\)). The unique maximum-a-posteriori (MAP) source starts at \(\lceil k/2\rceil\) at sufficiently small positive ages, then shifts left by **exactly one vertex at each threshold**, finally becoming vertex \(1\). Precisely at \(u_s\), vertices \(s\) and \(s+1\) are the only tied MAP sources; no other ties occur at positive ages. The entire result is independent of \(n\), subject to \(n>k\), and of \(\lambda\) after time rescaling.

For instance, when \(k=5\), the successive MAP locations are \(3\), \(2\), and \(1\), with transitions at \(u_2\approx2.1491257999\) and \(u_1\approx3.9206903949\).

## Assumptions and scope

- The underlying contact network is the *full known finite path*, not just its observed infected subgraph, and the observed prefix includes its left endpoint but not its right endpoint.
- The source location is drawn at time zero from a prior independent of transmission clocks; any prior strictly positive on vertices \(1,\ldots,k\) suffices for the posterior-order theorem. A uniform prior over all \(n\) vertices gives the MAP-staircase theorem. Conditional on observing \(B\), sources outside \(B\) have probability zero.
- Infection is irreversible; there is one source, no spontaneous importations, no recovery, no unobserved edges, and a common known exponential rate \(\lambda\). The observation time is measured from source initiation and is known, not estimated.
- Statements concerning the full sequence of MAP transitions require \(k\ge3\); for \(k=1\) there is no localization ambiguity and for \(k=2\) the unique MAP under a uniform prior is the boundary vertex \(1\) at every positive age.

## Proof

**1. Exact likelihood.** Conditional on source \(s\), infectious fronts advance independently along the two disjoint subpaths. Before either front reaches the physical endpoint, its succession of rate-\(\lambda\) waiting times has the same distribution as the arrival times of a rate-\(\lambda\) Poisson process. To observe \(B\), the leftward front must traverse at least \(s-1\) edges and then saturate at vertex \(1\); the rightward front must make *exactly* \(k-s\) advances, because vertex \(k+1\) is present and must remain susceptible. Independence of the two fronts yields the displayed formula for \(L_s\). No approximation is involved.

**2. Strict age monotonicity of adjacent likelihood ratios.** For \(1\le s<k\), set
\[
R_s(u):=\frac{L_{s+1}(u)}{L_s(u)}
=\frac{k-s}{u}\frac{Q_s(u)}{Q_{s-1}(u)}.
\]
For \(s=1\), \(Q_1(u)/(uQ_0(u))=\int_0^1e^{-ux}\,dx\), which strictly decreases with \(u\). For each integer \(s\ge2\), the Erlang distribution identity gives
\[
Q_s(u)=\frac{u^s}{(s-1)!}\int_0^1 x^{s-1}e^{-ux}\,dx,
\]
and hence
\[
\frac{Q_s(u)}{uQ_{s-1}(u)}
=\frac{1}{s-1}\frac{\int_0^1 x^{s-1}e^{-ux}\,dx}{\int_0^1 x^{s-2}e^{-ux}\,dx}.
\]
The latter is the expectation of \(X/(s-1)\) under a nondegenerate probability density proportional to \(x^{s-2}e^{-ux}\) on \((0,1)\). Its derivative with respect to \(u\) is \(-\operatorname{Var}(X)/(s-1)<0\). Thus every \(R_s(u)\) is strictly decreasing on \((0,\infty)\).

**3. Posterior stochastic order for arbitrary priors.** Let \(\pi_s>0\) be any fixed prior on \(B\). Bayes' rule gives posterior weights proportional to \(\pi_s L_s(u)\). The adjacent ratio of posterior masses is \((\pi_{s+1}/\pi_s)R_s(u)\), and therefore strictly decreases with \(u\). For \(0<u<v\), the quotient of posterior masses at age \(v\) versus age \(u\) is strictly decreasing in source index. For every nontrivial prefix cutoff, the usual cross-product comparison (pairing each index at or below the cutoff with each index above it) gives strict increase of cumulative posterior mass on that prefix. This proves the asserted monotone-likelihood-ratio and stochastic order, with no log-concavity restriction on the prior.

**4. Strict spatial log-concavity under the uniform prior.** Let \(p_r(u)=e^{-u}u^r/r!\) be the Poisson mass. For each \(r\ge0\),
\[
\frac{Q_r(u)}{p_r(u)}=\sum_{j=0}^{\infty}\frac{u^j r!}{(r+j)!}.
\]
At fixed \(u>0\) the right-hand side strictly decreases as \(r\) increases, because every summand with \(j\ge1\) strictly decreases. Consequently the Poisson upper-tail hazard \(p_r/Q_r\) strictly increases in \(r\), and \(Q_{r+1}/Q_r=1-p_r/Q_r\) strictly decreases. Since \(k-s\) also decreases strictly with \(s\), the likelihood ratios \(R_s(u)\) strictly decrease with \(s\). Hence the sequence \((L_1(u),\ldots,L_k(u))\) is strictly log-concave in the sense of strictly decreasing adjacent ratios. Its maximizing set consists of either a unique index or two adjacent tied indices.

**5. Exactly ordered crossings.** As \(u\downarrow0\), \(Q_s(u)\sim u^s/s!\), so \(R_s(u)\to(k-s)/s\). As \(u\to\infty\), \(Q_s(u)\to1\), so \(R_s(u)\to0\). Since \(R_s\) is strictly decreasing, \(R_s(u)=1\) has exactly one positive solution if \(s<k/2\), and none if \(s\ge k/2\). When \(s<r<k/2\), the strict spatial inequality \(R_s(u)>R_r(u)\) forces \(u_s>u_r\). At \(u_s\), the spatial inequalities show that \(L_1<\cdots<L_s=L_{s+1}>\cdots>L_k\), so the two tied sources are exactly the global maximizers. Between consecutive thresholds all maximizers are unique; their indices move one step left as age increases, beginning at \(\lceil k/2\rceil\) and ending at \(1\).

**6. Boundary limits.** As \(u\downarrow0\), the uniform-prior posterior obeys
\[
\Pr(S=s\mid B,u)\longrightarrow 2^{-(k-1)}\binom{k-1}{s-1},
\]
which explains the initial middle-source preference. As \(u\to\infty\), \(L_s/L_1\sim [(k-1)!/(k-s)!]u^{-(s-1)}\) for \(s>1\), so the posterior tends to a point mass at vertex \(1\). These limits are conditional on the fixed prefix observation, whose unconditional likelihood tends to zero at both extreme ages for \(k\ge2\).

## Verification

`verify.py` computes the likelihood independently by direct uniformization of the *finite-state continuous-time Markov chain of infected intervals* on paths with \(4\le n\le10\), all valid source and observed-prefix locations, and seven positive ages. It compares this calculation with the Poisson-frontier formula, checks strict spatial likelihood-ratio order, checks posterior stochastic order for both uniform and nonuniform priors, and numerically brackets every threshold for \(3\le k\le17\). The verifier runs with Python 3 and only standard-library modules, producing `PASS 4137 independent CTMC, posterior, and threshold diagnostics`. These finite tests are diagnostics; they are not used to infer the universal theorem. The analytic arguments above cover every allowed integer and parameter value.

## Relationship to prior work

Shah and Zaman's rumor-centrality framework introduced SI source identification and studied path behavior using independent Poisson fronts, principally when the infection age or full path boundary is not incorporated in the proposed source score [1,2]. Antulov-Fantulin et al. provided a simulation-based source-likelihood framework that can use an assumed observation time but did not derive an age-indexed finite-path posterior order or exact MAP transition sequence [3]. Kazemitabar and Amini gave general source-likelihood recursions for a different, time-independent **event-order** likelihood, the probability that one infected set is reached before any vertex outside it, not the probability of observing exactly that set at a specified elapsed time [4]. Shi, Zhang and Chu investigated observation-time effects for discrete-time SIR with partial snapshots by numerical methods, without the present continuous-time SI prefix-source classification [5]. The novel claim here is the simultaneous exact age-monotone posterior order under any positive prior and the complete ordered MAP staircase for a uniform prior; not the use of Bayes' rule or the fact that Poisson processes describe SI fronts.

## Limitations

- This is a conditional, idealized source-inference theorem on a one-dimensional finite contact network with perfect full-state observation. It does not describe dynamic updating while an infected set itself grows with observation time, and the conditioning event may be rare for large ages.
- It does not extend automatically to SIR recovery, heterogeneous edge rates, multiple sources, noisy network observations, unknown outbreak age, general trees, or general graphs. The uniform-prior one-vertex-at-a-time MAP staircase need not persist for an arbitrary prior, although monotone-likelihood-ratio posterior ordering does.
- Related works may contain alternative derivations or less-indexed special cases. The literature comparison is an inspected evidence assessment rather than a proof of global historical priority; independent mathematical and historical review remain outstanding.

## References

[1] D. Shah and T. Zaman, *Rumors in a Network: Who's the Culprit?*, arXiv:0909.4370 (first submitted September 24, 2009); later *IEEE Trans. Inform. Theory* **57** (2011), 5163–5181. https://arxiv.org/abs/0909.4370

[2] D. Shah and T. Zaman, *Finding Rumor Sources on Random Trees*, arXiv:1110.6230 (2011), later *Operations Research* **64** (2016), 736–755. https://arxiv.org/abs/1110.6230

[3] N. Antulov-Fantulin, A. Lančić, H. Štefančić, M. Šikić, and T. Šmuc, *Statistical inference framework for source detection of contagion processes on arbitrary network structures*, arXiv:1304.0018 (March 29, 2013), conference version (2014). https://arxiv.org/abs/1304.0018

[4] S. J. Kazemitabar and A. A. Amini, *Approximate Identification of the Optimal Epidemic Source in Complex Networks*, arXiv:1906.03052 (2019). https://arxiv.org/abs/1906.03052

[5] C. Shi, Q. Zhang, and T. Chu, *Effect of observation time on source identification of diffusion in complex networks*, *Chinese Physics B* **31** (2022), 070203. https://doi.org/10.1088/1674-1056/ac5985
