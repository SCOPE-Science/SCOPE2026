# Two distinct direct-voter thresholds in uniform random delegation

## Finding

A random one-choice delegation network has **two inequivalent participation thresholds**. Around \(\sqrt N\) casting voters, the expected represented-vote fraction makes a nontrivial error-function transition. Yet the probability that *every* vote is represented tends to zero whenever the number of casting voters is sublinear in \(N\). If a fixed fraction \(\alpha\) vote directly, the full-representation probability tends to \(\alpha e^{1-\alpha}\), with a residual Poisson number of delegation cycles.

In exact terms, for \(1\le m<N\), the probability a specified delegating voter is represented is
\[
p_{N,m}=\frac{m}{N-1}\sum_{k=0}^{N-m-1}\prod_{j=0}^{k-1}\frac{N-m-1-j}{N-1},
\]
where an empty product equals one. The expected represented fraction is \(m/N+(1-m/N)p_{N,m}\). For every \(1\le m\le N\), the probability of complete representation is
\[
Q_{N,m}=\frac{m}{N}\left(\frac{N}{N-1}\right)^{N-m}.
\]
For integer sequences \(m=m(N)\), the represented fraction tends to zero in probability when \(m=o(\sqrt N)\), and to one in probability when \(m/\sqrt N\to\infty\). When \(m/\sqrt N\to c\in(0,\infty)\), **its expectation**, not necessarily the fraction itself, tends to
\[
\Psi(c)=c\int_0^\infty e^{-ct-t^2/2}\,dt
=c\sqrt{\frac\pi2}\,e^{c^2/2}\operatorname{erfc}(c/\sqrt2).
\]
By contrast, \(Q_{N,m}\to0\) if \(m=o(N)\); if \(m/N\to\alpha\in(0,1]\), then \(Q_{N,m}\to\alpha e^{1-\alpha}\). For \(\alpha\in(0,1)\), the number of unrepresented directed cycles converges to a Poisson variable of mean \(-\log\alpha-(1-\alpha)\). For each fixed length \(\ell\ge2\), the corresponding cycle count converges to an independent Poisson variable of mean \((1-\alpha)^\ell/\ell\), jointly for any finite collection of lengths.

## Assumptions and scope

Fix \(N\ge2\) labeled voters. A specified set of \(m\in\{1,\dots,N\}\) people cast their vote. Each of the remaining \(N-m\) voters independently selects one of the other \(N-1\) voters uniformly as a delegate. Directed delegation is transitive and has no fallback options. Any vertex whose directed path reaches a casting voter has its vote counted exactly once; any path eventually repeating a delegator belongs to a non-casting cycle component and loses its vote. Let \(H_{N,m}\) denote the resulting random fraction of represented voters. There are no assumptions about substantive voter preferences or the correctness of their chosen options.

## Proof

**Exact first moment.** Fix a non-casting voter. Expose its unique path sequentially, stopping upon meeting the casting set or repeating a vertex. After discovering \(k\) distinct *other* non-casting vertices, the next step finds a casting voter with probability \(m/(N-1)\), irrespective of the previous path. The chance of reaching that point without a repeat or casting voter is \(\prod_{j=0}^{k-1}(N-m-1-j)/(N-1)\). Sum these disjoint successful stopping events to obtain \(p_{N,m}\). Exchangeability and linearity of expectation give \(\mathbb E H_{N,m}=m/N+(1-m/N)p_{N,m}\).

**Sharp square-root transition.** Put \(D=N-1\). For \(k=t\sqrt N+o(\sqrt N)\), whenever \(m/\sqrt N\to c\in(0,\infty)\), logarithmic expansion of the product gives
\[
\sum_{j=0}^{k-1}\log\left(1-\frac{m+j}{D}\right)=-ct-\frac{t^2}{2}+o(1).
\]
For every \(m\ge1\), this product is bounded by \(\exp[-k(k-1)/(2D)]\), supplying an integrable Gaussian tail on the scaled mesh. Riemann sums therefore converge to the displayed integral. If \(m=o(\sqrt N)\), the bound \(p_{N,m}=O(m/\sqrt N)\) implies \(\mathbb EH_{N,m}\to0\). Conversely, the event that the path repeats a delegator before encountering a caster is bounded by
\[
1-p_{N,m}\le\sum_{k\ge0}\left(1-\frac mD\right)^k\frac{k}{D}
=\frac{D-m}{m^2}\le\frac N{m^2}.
\]
The estimate follows because survival through \(k\) steps implies avoidance of a caster at each step, while at step \(k\) there are at most \(k\) already visited alternative vertices. Thus \(p_{N,m}\to1\) when \(m/\sqrt N\to\infty\). In both extreme regimes, Markov's inequality applied to \(H_{N,m}\) or \(1-H_{N,m}\) upgrades expectation convergence to convergence in probability. No concentration assertion is made in the critical regime.

**Exact complete coverage.** Every vote is represented precisely when the non-casters' outgoing choices form a directed forest rooted at the \(m\) prescribed casters. The directed matrix-tree theorem gives the number of such forests as the determinant of the non-caster minor of the complete-graph outdegree Laplacian. For \(s=N-m\ge1\), this minor is \(N I_s-J_s\), with eigenvalues \(N\) of multiplicity \(s-1\) and \(m\) of multiplicity one. Therefore exactly \(mN^{s-1}\) assignments succeed among \((N-1)^s\) equally likely assignments. The formula also gives one when \(s=0\). Its limits are immediate from \((1+1/(N-1))^{N-m}\to e^{1-\alpha}\) when \(m/N\to\alpha\), including \(\alpha=0\) as an upper-bound case.

**Residual cycles.** Let \(C_{N,\ell}\) count directed cycles of length \(\ell\ge2\) formed entirely by non-casters. Such cycles are necessarily vertex-disjoint in any functional graph. Their exact expected count is \(\mathbb EC_{N,\ell}=(N-m)_\ell/[\ell(N-1)^\ell]\), where \((x)_\ell\) is the falling factorial. For fixed \(\ell\) and \(m/N\to\alpha\in(0,1)\), this tends to \((1-\alpha)^\ell/\ell\). Joint factorial moments count disjoint prescribed cycles; different cycles use independent outgoing edges, and the number of ways to choose disjoint labeled vertices yields precisely the joint factorial moments of independent Poisson variables in the limit. Furthermore,
\[
\sum_{\ell\ge L}\mathbb EC_{N,\ell}
\le\sum_{\ell\ge L}\frac{1}{\ell}\left(\frac{N-m}{N-1}\right)^\ell,
\]
which vanishes uniformly for large \(N\) as \(L\to\infty\). Hence the total cycle count is Poisson in the limit with mean \(\sum_{\ell\ge2}(1-\alpha)^\ell/\ell=-\log\alpha-(1-\alpha)\). In particular, its zero probability matches the limit \(\alpha e^{1-\alpha}\) from the independent forest count.

## Verification

The accompanying `verify.py` exhaustively enumerates \(60{,}277\) delegation assignments over \(21\) distinct \((N,m)\) parameter pairs with \(2\le N\le7\), and verifies the exact expected fraction and complete-coverage probability by independent functional-graph tracing. It compares numerical critical-window values with the error-function formula at three scales and checks representative finite-sample regimes. Its output ends `VERIFY_OK`. Finite computations are checks, not proofs of the asymptotic assertions.

## Relationship to prior work

Berinsky et al. (arXiv:2107.11868, first public 2021-07-25) study random transitive liquid-democracy delegations, including cycles and lost vote weights, but their examined bounds work with a fixed non-delegation probability and do not provide the vanishing-caster, square-root crossover or the exact complete-representation probability. Brill et al. (arXiv:2112.07509, first public 2021-12-14) empirically investigate isolated voters and backup delegations; the analyzed text contains no equivalent complete-graph formula. Utke and Schmidt-Kraepelin (arXiv:2307.01174, first public 2023-07-03) study random-walk/fractional delegation and matrix-tree algorithms, not this one-choice random-delegation model's asymptotic participation regimes. Classical Cayley–matrix-tree and random-mapping methods, including Pitman's 1998 work, underpin the proof; those general combinatorial facts are **not** asserted to be newly discovered. The assessed contribution is their precise application to the different *fractional versus universal* representation scales in the stated voting model.

## Limitations

The model assumes homogeneous complete-network choice, independent delegations, and fixed casting-voter identities. It does not cover weighted trust, correlated delegations, strategic voter behavior, alternate cycle-resolution rules, or the probability of a substantively correct collective outcome. A limiting expected fraction in the square-root window must not be mistaken for a distributional limit of the random represented fraction. The constituent random-mapping ideas are classical; an unlocated formulation could already cover this combined application. Independent scientific and publication-priority audits remain unperformed.

## References

1. Berinsky, A. et al., *Tracking Truth with Liquid Democracy* (2021), arXiv:2107.11868, https://arxiv.org/abs/2107.11868 .
2. Brill, M. et al., *Liquid Democracy with Ranked Delegations* (2021), arXiv:2112.07509, https://arxiv.org/abs/2112.07509 .
3. Utke, M. and Schmidt-Kraepelin, U., *Anonymous and Copy-Robust Delegations for Liquid Democracy* (2023), arXiv:2307.01174, https://arxiv.org/abs/2307.01174 .
4. Pitman, J., *Abel-Cayley-Hurwitz multinomial expansions associated with random mappings, forests, and subsets* (1998), Berkeley Statistics Technical Report 498, https://statistics.berkeley.edu/tech-reports/498 .
