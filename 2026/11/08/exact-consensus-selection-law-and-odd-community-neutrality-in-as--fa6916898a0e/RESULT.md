# Exact consensus-selection law and odd-community neutrality in asynchronous bipartite majority dynamics

## Finding

For every pair of positive integers \(m,n\), run asynchronous binary strict-neighbor-majority dynamics with **retention on ties** on the complete bipartite graph \(K_{m,n}\). Each discrete step uniformly chooses one vertex, independently of previous steps, and replaces its bit by the strict majority among neighbors, if one exists. Let \(a\) and \(b\) be the initial numbers of one-bits in the two labelled parts of sizes \(m\) and \(n\), respectively.

Every trajectory almost surely reaches one of the two monochromatic consensus states, except when both part sizes are even and both parts initially contain exactly half ones. These doubly tied configurations are fixed; there are \(\binom{m}{m/2}\binom{n}{n/2}\) of them. No other recurrent configurations occur.

Let \(p_{m,n}(a,b)\) denote the probability of eventual all-one consensus. If both parts have a strict one-majority, \(p=1\); if both have a strict zero-majority, \(p=0\). If one part is tied and the other has a strict majority, the strict majority determines the consensus with probability one. A doubly tied configuration is nonconsensual and its all-one probability is zero.

The nontrivial case is \(2a>m\) and \(2b<n\). Put
\[
  c=n-b,\qquad r=a-\lfloor m/2\rfloor,\qquad s=\lceil n/2\rceil-b,
\]
and write \((z)_{\underline{k}}=z(z-1)\cdots(z-k+1)\) with \((z)_{\underline0}=1\). Then
\[
\boxed{
 p_{m,n}(a,b)=\sum_{j=0}^{r-1}\binom{s+j-1}{j}
 \frac{(c)_{\underline{s}}(a)_{\underline{j}}}{(a+c)_{\underline{s+j}}}.}
\]
For opposite strict majorities with \(2a<m\), \(2b>n\), the all-one probability is \(1-p_{m,n}(m-a,n-b)\), using the displayed formula on the complemented initial configuration.

For the important polarization experiment in which the first part starts entirely at one and the second entirely at zero, define \(W_{m,n}=p_{m,n}(m,0)\). Then **\(W_{m,n}=1/2\) for every two odd positive part sizes, even if they are unequal**. If \(m\) is odd and \(n\) even, then \(W_{m,n}>1/2\), whereas if \(m\) is even and \(n\) odd, then \(W_{m,n}<1/2\). With \(n\) fixed,
\[
\boxed{\lim_{m\to\infty} W_{m,n}=
\begin{cases}
1/2,&n\text{ odd},\\
1/2+\binom{n}{n/2}2^{-(n+1)},&n\text{ even}.
\end{cases}}
\]
Thus an even-sized smaller community has an enduring tie-rule advantage in the large-opposing-community limit, while an odd-sized community is exactly neutral there.

## Assumptions and scope

The graph is simple, undirected, loopless and complete bipartite. Bits are initially announced at every vertex, unlike first-announcement learning models. Ties retain the *current* bit, not an initial private signal and not a random tie coin. Updates use one uniformly random vertex at each discrete time, with no simultaneous updates. Probabilities refer solely to update-order randomness with the labelled initial colouring fixed. All conclusions hold for \(m,n\ge1\), including the two-vertex graph.

## Proof

**1. Termination and absorbing set.** Let \(D\) be the number of bichromatic edges. Flipping at a vertex with a strict opposing neighbor majority strictly reduces \(D\). Ties do not flip. Consequently at most \(mn\) genuine flips occur. Each nonabsorbing configuration has a vertex with a possible flip, chosen eventually almost surely under iid uniform sampling; thus the process a.s. reaches an absorbing configuration. At a fixed state, if one part contains both bits, the other part must be tied, since a strict other-part majority would compel one of those bits to flip. If both parts are mixed, both must be tied. If one part is monochromatic and the other mixed, the latter has vertices compelled to match the former. Two opposite monochromatic parts also have compelled flips. Hence only both monochromatic with the same bit, or both mixed and tied, are fixed. Both mixed-and-tied states exist precisely for even \(m,n\), giving the stated count.

**2. Sign regimes.** Write \(a_t,b_t\) for the one-counts in the parts. If both non-tied signs agree, each permitted flip moves toward their common sign, so consensus with that sign follows almost surely. If one part is tied while the other has a strict sign, the tied part's opposite bits are forced to flip toward that sign; the other part cannot flip until the tie is broken, after which the signs agree. If both parts are tied, no flip is possible. Therefore only initially opposing strict majorities require a stochastic winner calculation.

**3. A race of order statistics.** Suppose \(2a>m\) and \(2b<n\). As long as these opposing strict signs persist, the eligible vertices are precisely the \(a\) one-vertices in the first part, changing to zero, and the \(c=n-b\) zero-vertices in the second, changing to one. No vertex flips twice before the first sign ceases to be strict. The first majority loses strictness when \(r=a-\lfloor m/2\rfloor\) of the first group have flipped; the second when \(s=\lceil n/2\rceil-b\) of the second group have flipped. If the first part reaches its threshold first, the second still has a strict zero-majority, the first part continues to convert to zero (possibly passing through a tie), and the all-zero consensus follows. If the second part reaches its threshold first, the symmetric argument gives all-one consensus.

Give every vertex an independent rate-one Poisson clock. Ignoring clock rings that do not change a bit gives exactly the embedded nontrivial moves of the stated discrete-time uniform-vertex dynamics. Before the first threshold, the first effective ring of each initially eligible vertex has an independent exponential waiting time of rate one. Their order is a uniformly random permutation of the \(a+c\) eligible vertices. The second-part threshold occurs first precisely when its \(s\)-th chosen vertex appears before the first part's \(r\)-th chosen vertex. For a winning prefix ending with a second-part vertex and containing exactly \(j\) first-part vertices, where \(0\le j<r\), there are \(\binom{s+j-1}{j}\) interleavings, the probability of any specified interleaving of group types is \((c)_{\underline{s}}(a)_{\underline j}/(a+c)_{\underline{s+j}}\), and summation gives the asserted formula. Bit complementation gives the reverse-opposition formula.

**4. Odd-community neutrality and parity effect.** In the initially opposite monochromatic case, let \(T_m\) be the time for \(\lceil m/2\rceil\) of \(m\) independent rate-one exponential clocks to ring, and define \(U_m=e^{-T_m}\). As \(e^{-E}\) is uniform on \((0,1)\) when \(E\) is exponential of rate one, elementary uniform-order-statistic theory gives
\[
U_{2k-1}\sim\operatorname{Beta}(k,k),\qquad U_{2k}\sim\operatorname{Beta}(k+1,k).
\]
For independent parts \(W_{m,n}=\Pr(U_n>U_m)\). Two independent variables symmetric about \(1/2\) have a symmetric difference, implying exactly \(W_{m,n}=1/2\) for odd \(m,n\). For even order \(2k\), the beta density is a strictly increasing likelihood-ratio tilt \(2u\) of the symmetric \(\operatorname{Beta}(k,k)\) density. Therefore its law strictly stochastically dominates the symmetric one. Comparison with the other independent symmetric variable proves the strict stated one-even/one-odd inequalities.

For fixed \(n\), the empirical median theorem, or a binomial concentration inequality, gives \(T_m\to\log 2\) in probability. Since \(T_n\) has no atoms, \(W_{m,n}=\Pr(T_n<T_m)\to\Pr(T_n<\log2)\). Each of the \(n\) rate-one clocks rings by \(\log2\) with probability \(1/2\). Hence the limit is the binomial tail \(2^{-n}\sum_{j=\lceil n/2\rceil}^n\binom nj\). Symmetry of binomial coefficients evaluates it as claimed.

## Verification

The included independent exact-rational programs are `check_exact.py` and `check_vertex.py`. Run with standard Python 3 from a directory containing both files: `python3 check_exact.py` and `python3 check_vertex.py`. The first checks the closed formula against count-state dynamic programming on all \(1\le m,n\le8\), for 1,936 pairs of starting counts. The second computes the Markov absorption probabilities directly from all individually labelled binary vertex configurations for 33 graph sizes with \(1\le m,n\le6\) and \(m+n\le10\), covering 7,684 labelled configurations. Both report PASS. The recurrence and labelled-state checker are finite tests; they do not replace the all-size order-statistic proof.

## Relationship to prior work

Auletta, Caragiannis, Ferraioli, Galdi and Persiano (2014), arXiv:1402.4050, treat precisely the sequential strict-majority update with retention on ties, but study the existence of adversarial update sequences that subvert majorities on general graphs; they do not supply a random-order absorption kernel for \(K_{m,n}\). Feldman, Immorlica, Lucier and Weinberg (2014), arXiv:1408.5192, analyze an asynchronous learning model in which nodes initially have unannounced public opinions and tie-breaking uses private initial signals, so their consensus guarantees do not imply the present fixed-initial-profile probabilities. Mohan and Prałat (2023), arXiv:2309.04691, develop high-probability convergence results for binomial random graphs under that private-signal announcement model, not this exact bipartite process. The classical beta-order-statistic identities are standard tools, not claimed as new. The contribution is the graph-specific all-start kernel and its odd/odd fairness and parity-sensitive limiting consequence.

## Limitations

The result does not give the entire distribution of absorption times, nor extend the kernel to asynchronous models with random tie-breaking, private initial announcements, nonuniform vertex-selection rates, or arbitrary incomplete bipartite graphs. The source comparisons support a qualified originality assessment, not an exhaustive global priority claim. Independent external validation has not been performed.

## References

- V. Auletta, I. Caragiannis, D. Ferraioli, C. Galdi, G. Persiano, *Minority Becomes Majority in Social Networks*, first public arXiv version dated 2014-02-17, arXiv:1402.4050, https://arxiv.org/abs/1402.4050.
- M. Feldman, N. Immorlica, B. Lucier, S. M. Weinberg, *Reaching Consensus via non-Bayesian Asynchronous Learning in Social Networks*, first public arXiv version dated 2014-08-22, arXiv:1408.5192, https://arxiv.org/abs/1408.5192.
- D. Mohan, P. Prałat, *Asynchronous Majority Dynamics on Binomial Random Graphs*, first public arXiv version dated 2023-09-09, arXiv:2309.04691, https://arxiv.org/abs/2309.04691.
