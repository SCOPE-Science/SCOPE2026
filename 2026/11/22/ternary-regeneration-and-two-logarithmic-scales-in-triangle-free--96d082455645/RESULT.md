# Ternary regeneration and two logarithmic scales in triangle-free random interval graphs

## Finding

Let \(I_1,\ldots,I_n\) be independent random intervals, each made from two independent samples from the same nonatomic distribution on the real line, and let \(G_n\) join intersecting intervals. Write \(E_n\) for the event that \(G_n\) contains no triangle, \(C_n\) for its number of components, \(N_{n,k}\) for its number of components of size \(k\), \(D_{n,d}\) for its number of vertices of degree \(d\), \(M_n\) for its largest component size, and \(\Delta_n\) for its maximum degree.

**Conditional regeneration theorem.** For every integer \(n\ge1\), conditional on \(E_n\), the interval matching in increasing left-endpoint order is in bijection with a uniformly random word of length \(n-1\) on three letters \(\{B,O,N\}\). The letters are independent and equiprobable. The letter \(B\) starts a new component; \(O\) attaches a new pendant vertex to the currently active interval and retains the old interval; \(N\) attaches the new vertex and makes it the next active interval. Every component is a caterpillar tree. In particular,

\[
\Pr(E_n)=\frac{3^{n-1}}{(2n-1)!!},\qquad C_n\mid E_n\ \overset{d}=1+\operatorname{Bin}(n-1,1/3).
\]

For \(1\le k<n\), the exact conditional mean component spectrum is

\[
\mathbb E[N_{n,k}\mid E_n]=\left(\frac23+\frac{n-k-1}{9}\right)\left(\frac23\right)^{k-1},\qquad
\mathbb E[N_{n,n}\mid E_n]=\left(\frac23\right)^{n-1}.
\]

For every fixed integer \(k\ge1\) and \(d\ge0\), as \(n\to\infty\), the conditional empirical fractions converge in probability:

\[
\frac{N_{n,k}}n\xrightarrow{\Pr}\frac19\left(\frac23\right)^{k-1},\qquad
\frac{D_{n,d}}n\xrightarrow{\Pr}\pi_d,
\]

where the **complete degree spectrum** is

\[
\pi_0=\frac19,\qquad \pi_1=\frac{16}{27},\qquad
\pi_d=\frac{16}{3^{d+2}}\quad(d\ge2).
\]

The two natural extremes diverge on *different logarithmic scales*:

\[
\frac{M_n}{\log n}\xrightarrow{\Pr}\frac{1}{\log(3/2)},\qquad
\frac{\Delta_n}{\log n}\xrightarrow{\Pr}\frac{1}{\log3},
\]

all probabilities and convergence statements here referring to the conditional laws given \(E_n\). Thus the limiting ratio \(\Delta_n/M_n\) is \(\log(3/2)/\log3\) in probability. The exact count of components is a consequence of the ternary coding; the degree spectrum and distinct extreme scales require additional tracking of which live interval survives each closing event.

## Assumptions and scope

All \(2n\) endpoints are independent with a common nonatomic law; their ranks are distinct almost surely. The model is the *endpoint-pairing* random interval graph, not the uniformly sampled unlabeled interval graph or the Poisson-arrival/service-time model. The event \(E_n\) is equivalently bipartiteness (interval graphs are chordal) or clique number at most two (the interval Helly property). Statements about component sizes use the birth order of increasing left endpoints only for coding; graph statistics themselves do not depend on a vertex labeling. The exact formula for \(N_{n,k}\) treats \(k=n\) separately. Logarithms are natural.

## Proof

**1. Uniform endpoint matchings.** Rank the \(2n\) endpoints. Exchangeability makes every perfect pairing of the ordered rank positions equiprobable; there are \((2n-1)!!\) such pairings. Scan left to right, keeping the number of currently open intervals. Three pairwise intersecting intervals share a point, hence create an instant with at least three open intervals, and conversely. Consequently \(E_n\) is exactly the condition that the open-interval count never exceeds two.

**2. Exact ternary bijection.** At the first opening there is one active interval, called the carrier. Before each later opening, either the carrier has already closed, or it is still open. In the first case assign \(B\) and start a new carrier. In the second case the new interval intersects the carrier; before another opening, one of those two intervals must close, since the open count is bounded by two. Assign \(O\) if the *new* interval closes first (old carrier survives), and \(N\) if the *old* one closes first (new carrier survives). The second endpoint in each overlap is eventually closed as prescribed. Conversely, start with one opening and perform the deterministic endpoint operations associated with the word: \(B\) closes the carrier and opens a new one, \(O\) opens and immediately closes the new interval, and \(N\) opens a new interval and closes the old carrier. Close the last carrier at the end. This gives a unique matching of the \(2n\) endpoint ranks and inverts the encoding. Every ternary word is valid; therefore there are exactly \(3^{n-1}\) admissible matchings and their conditional words are iid uniform.

**3. Caterpillar components and exact counts.** Each \(B\) ends a component; each \(O\) or \(N\) attaches the incoming vertex to exactly one earlier vertex, the carrier. Former intervals that have closed cannot intersect incoming ones. Thus the graph is a forest and \(C_n=1+\#B\). Between changes of carrier, all noncarrier new vertices are leaves; successive carriers form a path. Removing leaves therefore leaves a path (or the empty graph), so each component is a caterpillar. A component of size \(k\) is a run of \(k-1\) non-\(B\) letters between component boundaries. For \(k<n\) there are two endpoint placements (one \(B\) boundary) and \(n-k-1\) interior placements (two \(B\) boundaries). Independence gives the stated finite mean. For \(k=n\) no \(B\) occurs. Fixed-length pattern indicators form bounded finite-dependent sequences, giving the component-spectrum law of large numbers.

**4. Limiting degree probabilities.** For an interior vertex, its preceding letter is \(B,O,N\), each with probability \(1/3\). A vertex born after \(O\) closes immediately and has degree one. A vertex born after \(B\) is the new carrier with no previous incident edge; one born after \(N\) is the new carrier with one previous edge. During its subsequent carrier lifetime, it receives one incident edge at each \(O\), and possibly one at the terminating \(N\); a terminating \(B\) gives no additional edge. If \(R\) is the number of successive \(O\)'s before the first non-\(O\), then

\[
\Pr(R=r)=\frac23\left(\frac13\right)^r\quad(r\ge0).
\]

The terminating symbol is equally likely to be \(B\) or \(N\), independently of \(R\). Hence the degree of a typical interior vertex has the mixture distribution

\[
\begin{cases}
1,&\text{with probability }1/3,\\
R+J,&\text{with probability }1/3,\\
1+R+J,&\text{with probability }1/3,
\end{cases}
\]

where \(J\sim\operatorname{Bernoulli}(1/2)\) is independent of \(R\). Summing gives precisely \(\pi_0=1/9\), \(\pi_1=16/27\), and \(\pi_d=16/3^{d+2}\) for \(d\ge2\). These sum to one and have mean \(4/3\), consistent with \(2(n-C_n)/n\to4/3\). For the empirical limit, restrict the forward carrier run to \(h\) symbols; the resulting bounded indicators are \((h+2)\)-dependent and obey a weak law. The discarded long-run probability is at most \((1/3)^{h+1}\), and the \(O(h)\) boundary positions are negligible. Let \(n\to\infty\) and then \(h\to\infty\).

**5. Extremes.** Let \(L_n^{(2)}\) be the longest run of non-\(B\) letters and \(L_n^{(1)}\) the longest run of \(O\) letters. Exactly \(M_n=1+L_n^{(2)}\). Moreover, every consecutive run of \(r\) letters \(O\) creates \(r\) different neighbors of one carrier, while any carrier has at most one incident edge from its birth and at most one incident edge from the next \(N\). It follows deterministically that

\[
L_n^{(1)}\le\Delta_n\le L_n^{(1)}+2.
\]

For iid Bernoulli symbols of success probability \(s\in(0,1)\), the longest success run among \(n-1\) trials divided by \(\log n\) converges in probability to \(1/\log(1/s)\). Indeed a union bound over starting positions proves the upper bound at \((1+\epsilon)\log_{1/s}n\); partitioning into disjoint blocks of length \((1-\epsilon)\log_{1/s}n\) proves the lower bound, since the expected number of entirely successful blocks diverges. Apply this elementary fact to \(s=2/3\) and \(s=1/3\), and use the deterministic inequalities. The ratio assertion follows by division by a nonzero limit.

## Verification

The executable standalone script `checks/verify.py` exhaustively generates all perfect pairings of \(2n\) ordered positions for \(1\le n\le7\). It independently tests eligibility using active-interval counts, reconstructs the conditioned ternary words, tests the inverse reconstruction, measures connected components and degree maxima from interval intersections, and checks the exact binomial component distribution and the two deterministic run inequalities. It also enumerates every ternary word through length ten to verify the component count and exact component-size expectation formulas. Execute with Python 3 as `python checks/verify.py` from the directory containing this file. These computations check finite instances; the laws of large numbers and logarithmic extremes are established by the arguments above, not finite testing.

## Relationship to prior work

Scheinerman's random interval-graph model and the degree/clique summaries in Diaconis, Holmes and Janson (2011) concern typical, dense interval graphs, not the rare triangle-free conditional graph. Korbel and Mörters (2020) give a general exact probability formula for the *open-pair count path* in sock sorting; in particular, the height-at-most-two path enumeration underlying the probability and component count here is derivable from their path formula and is not claimed as a wholly new general matching formula. The additional object studied here is the surviving-carrier graph process, yielding the complete conditioned degree spectrum and the two different logarithmic extreme scales. Iliopoulos's available thesis studies unconditioned random interval graph degrees and cliques. The 1990 article of Justicz, Scheinerman and Winkler principally advertises independence numbers and universal intersections; its complete text could not be inspected, so exhaustive historical priority is not asserted.

## Limitations

The theorem covers endpoint-pairing interval graphs with iid nonatomic endpoints and conditioning on clique number at most two. It does not assert results for uniformly sampled *graph isomorphism classes*, other interval-length distributions, higher clique cutoffs, or full centered extreme-value limit laws. The scientific comparison establishes best-knowledge novelty for the conditional graph's degree law and its simultaneous component/degree scales, not uniqueness across inaccessible historical sources. Independent mathematical validation is not included.

## References

1. P. Diaconis, S. Holmes, and S. Janson, *Interval graph limits*, arXiv:1102.2841v1 (first submitted 2011-02-14), especially Section 2.3. https://arxiv.org/html/1102.2841v1
2. S. Korbel and P. Mörters, *A path formula for the sock sorting problem*, arXiv:2009.08113v1 (2020-09-17), Theorem and Lemma 3. https://arxiv.org/abs/2009.08113
3. V. Iliopoulos, *Random Interval Graphs*, MSc thesis (available institutional repository), Sections 3.2, 4, 5. https://repository.essex.ac.uk/14414/1/M.Sc.%20thesis.pdf
4. J. Justicz, E. R. Scheinerman, and P. M. Winkler, *Random Intervals*, American Mathematical Monthly 97 (1990), 881–889, DOI:10.1080/00029890.1990.11995679 (bibliographic record and abstract inspected; full text unavailable).
5. E. R. Scheinerman, *Random interval graphs*, Combinatorica 8 (1988), 357–371, DOI:10.1007/BF02189092 (bibliographic record inspected; full text unavailable).
