# A sharp three-quarter rare-failure law for greedy matching on cocktail-party graphs

## Finding

Let \(G_n=K_{2n}\setminus M_n\), where \(M_n\) is any fixed perfect matching, and let \(n\ge2\). Run the **uniform-feasible-edge greedy matching algorithm**: while an edge remains on the vertices not yet matched, choose one of these edges uniformly, add it to the matching, and remove its endpoints. Let \(p_n\) be the probability that the resulting matching is *not* perfect. Then

\[
0\le \frac{3n}{4n^2-1}-p_n\le\frac{12 H_{n-1}}{n^2},
\qquad H_k=\sum_{j=1}^{k}\frac1j.
\]

In particular,

\[
\lim_{n\to\infty}n p_n=\frac34,
\qquad p_n=\frac{3}{4n}+O\!\left(\frac{\log n}{n^2}\right).
\]

A natural unconditioned uniform pair of vertices belongs to the deleted matching with probability \(1/(2n-1)\). Thus the greedy algorithm's terminal forbidden-pair event is asymptotically \(3/2\) times that reference probability. The result characterizes a rare failure event rather than only the asymptotically trivial matching-size ratio.

There is also an exact rational recurrence for every finite \(n\). For \(1\le m\le n\) and \(0\le f\le m\), put \(s=2(m-f)\) and \(D=m(2m-1)-f\). Define \(F(1,0)=0\), \(F(1,1)=1\); for \(m\ge2\),

\[
F(m,f)=\frac{\binom{s}{2}F(m-1,f)
  +2fs F(m-1,f-1)
  +2f(f-1)F(m-1,f-2)}{D},
\]

where a term with zero coefficient is omitted, including references to inadmissible states. Then \(p_n=F(n,n)\). For example, \(p_2=0\), \(p_3=1/5\), \(p_4=8/65\), and \(p_5=1231/11375\).

## Assumptions and scope

The graph is finite, simple, and labeled. It is the complete graph on \(2n\) vertices after deleting precisely \(n\) pairwise disjoint edges. The random choice is **uniform among presently feasible edges**, not uniform among vertices and not a random-edge-arrival online matching algorithm with a different rule. Probabilities concern the law of this particular algorithm. All limits are as \(n\to\infty\) through integers; bounds are valid for every integer \(n\ge2\). The result makes no assertion for general regular graphs or for other matching algorithms.

## Proof

**1. Exact reduced state.** Before a choice there are \(2m\) unmatched vertices. Let \(f\) be the number of forbidden pairs whose two endpoints both remain. The other \(s=2m-2f\) vertices are singletons from distinct forbidden pairs. There are exactly \(D=\binom{2m}{2}-f=m(2m-1)-f\) feasible edges. The selected endpoints can be: two singletons, in \(\binom{s}{2}\) ways; one singleton and one endpoint of an intact forbidden pair, in \(2fs\) ways; or endpoints belonging to two distinct intact forbidden pairs, in \(2f(f-1)\) ways. The next state is, respectively, \((m-1,f)\), \((m-1,f-1)\), or \((m-1,f-2)\). The coefficients sum to \(D\), proving the recurrence. When two vertices remain, the matching fails exactly if they form a forbidden pair, so \(p_n=\mathbb P(f_1=1)=\mathbb E f_1\), where \(f_m\) denotes the intact-pair count after \(n-m\) edge selections.

**2. One-pair survival and a telescoping moment.** Conditional on \(f_m=f\), an identified intact forbidden pair survives the next step with probability

\[
q_1(m,f)=1-\frac{4(m-1)}{D},
\]

where \(D=m(2m-1)-f\). At \(f=1\) it equals \((2m-3)/(2m+1)\). Writing \(e_m=\mathbb E f_m\), one consequently obtains for every \(m\ge2\)

\[
e_{m-1}=\frac{2m-3}{2m+1}e_m-c_m,
\qquad
c_m=4(m-1)\,\mathbb E\left[
\frac{f_m(f_m-1)}{[m(2m-1)-1][m(2m-1)-f_m]}
\right]\ge0.
\]

Set \(h_m=3e_m/[(2m-1)(2m+1)]\). The factors cancel exactly, giving

\[
p_n=h_1=h_n-\sum_{m=2}^n\frac{3c_m}{(2m-3)(2m-1)},
\qquad h_n=\frac{3n}{4n^2-1}.
\]

**3. Uniform two-pair survival control.** If two specified intact forbidden pairs are still present at state \((m,f)\), then both survive the next edge selection with probability

\[
q_2(m,f)=\frac{\binom{2m-4}{2}-(f-2)}{m(2m-1)-f}.
\]

For fixed \(m\) this decreases with \(f\), hence it is at most \(q_2(m,2)\). A direct subtraction gives, for every integer \(m\ge2\),

\[
\left(\frac{m-1}{m}\right)^4-q_2(m,2)
=\frac{4m^4-6m^3-6m^2+7m-2}{m^4(2m^2-m-2)}\ge0.
\]

Indeed, with \(t=m-2\ge0\), the numerator becomes \(4t^4+26t^3+54t^2+39t+4>0\), and the denominator is positive. Pairwise survival over successive stages therefore implies the *factorial-moment* estimate

\[
\mathbb E[f_m(f_m-1)]\le n(n-1)\prod_{k=m+1}^n\left(\frac{k-1}{k}\right)^4
=n(n-1)\left(\frac{m}{n}\right)^4\le\frac{m^4}{n^2}.
\]

This is an expectation over the actual process, not an independence assumption. The two denominator factors in the definition of \(c_m\) are at least \(2m(m-1)\), since \(0\le f_m\le m\). Thus

\[
0\le c_m\le\frac{\mathbb E[f_m(f_m-1)]}{m^2(m-1)}\le\frac{m^2}{n^2(m-1)}.
\]

The telescoping formula now yields

\[
0\le \frac{3n}{4n^2-1}-p_n
\le\frac{3}{n^2}\sum_{m=2}^n
\frac{m^2}{(m-1)(2m-3)(2m-1)}
\le \frac{12}{n^2}\sum_{m=2}^n\frac1{m-1},
\]

since \(m^2\le4(m-1)^2\) and \((2m-3)(2m-1)\ge(m-1)^2\). This proves both the finite bound and the limit. No finite enumeration is used to infer the limit.

## Verification

The standalone \(\texttt{VERIFY.py}\) uses standard-library exact rational arithmetic to calculate the recurrence, independently enumerates the labeled greedy process for \(2n\le10\) vertices, checks all admissible reduced transition counts and pair-survival inequalities up to 39 intact-pair stages, propagates exact state distributions through \(n=28\), checks the finite bound, and performs separate numerical asymptotic smoke checks. A complete run returns `VERIFY_OK 4287 checks`. Run `python VERIFY.py` from this directory. The infinite theorem depends on the explicit displayed analytic argument, not a finite computer census.

## Relationship to prior work

Dyer and Frieze (1991) introduced and analyzed this uniform-feasible-edge randomized greedy matching algorithm on arbitrary fixed graphs, with emphasis on approximation performance and forest results. Its abstract and bibliographic material were available, but its full text was not accessible for an exhaustive comparison. Arnosti (2021) precisely distinguishes random-edge greedy matching from other greedy rules, and studies random bipartite inputs and algorithm comparisons rather than the explicit fixed dense cocktail-party graph. Glebov, Luria and Simkin (2018) study the different process of randomly *adding edges* to regular bipartite graphs until a perfect matching appears. Bennett and Bohman (2012) treat a broad random greedy hypergraph matching process and unmatched-vertex bounds, not this sharp rare-event probability. The theorem here is the explicit \(3/4\) constant and quantitative error for the fixed \(K_{2n}\setminus M_n\) instance, not a claim to have invented random greedy matching or the reduced-state method.

## Limitations

No independent audit or historical-priority certification has been performed. The full text of the especially relevant Dyer–Frieze 1991 paper could not be inspected; available abstracts and related full texts do not establish the identical claim, but priority uncertainty remains. The displayed upper/lower bounds are not claimed to be sharp in their second-order correction, and no limit theorem for non-complete or differently weighted graphs is asserted. Finite tests are corroborative only.

## References

1. M. E. Dyer and A. M. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45, https://doi.org/10.1002/rsa.3240020104.
2. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, Stochastic Systems 12 (2022), 133–150. First published online 2021-11-02. https://doi.org/10.1287/stsy.2021.0082.
3. R. Glebov, Z. Luria and M. Simkin, *Perfect matchings in random subgraphs of regular bipartite graphs*, arXiv:1805.06944, initial public version 2018-05-17, https://arxiv.org/abs/1805.06944.
4. P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581 (2012), https://arxiv.org/abs/1210.3581.
