# A three-regime nearest-swap law for complete-bipartite single-peaked domains

## Finding

Let \(K_{a,b}\) be the complete bipartite candidate graph with shores of sizes \(a,b\geq1\), and \(m=a+b\geq3\). Let \(\Pi\) be a uniformly random ranking of the \(m\) labeled candidates. Write \(X_{a,b}\) for the minimum Kendall (adjacent-swap) distance from \(\Pi\) to any ranking single-peaked on \(K_{a,b}\), in the connected-top-prefix sense. If \(L(\Pi)\) denotes the length of the initial monochromatic shore run, then

\[
X_{a,b}=L(\Pi)-1.
\]

For every integer \(0\leq d\leq\max(a,b)-1\), with a falling factorial interpreted as zero beyond its upper argument,

\[
\Pr(X_{a,b}=d)=
\frac{b(a)_{\underline{d+1}}+a(b)_{\underline{d+1}}}{(m)_{\underline{d+2}}},\qquad
\Pr(X_{a,b}\geq d)=
\frac{(a)_{\underline{d+1}}+(b)_{\underline{d+1}}}{(m)_{\underline{d+1}}}\quad(1\leq d\leq\max(a,b)-1).
\]

The maximum possible distance is \(\max(a,b)-1\); outside this support all point probabilities and corresponding upper tails are zero. The single-peaked graph domain contains exactly \(2ab(m-2)!\) rankings. The expected distance is

\[
\mathbb E X_{a,b}=\frac{a}{m}\frac{a-1}{b+1}+\frac{b}{m}\frac{b-1}{a+1}
=\frac{m^2-3ab-1}{ab+m+1}.
\]

With the standard outer-diversity normalization, its exact outer diversity is

\[
\operatorname{outdiv}(\operatorname{SP}(K_{a,b}))=
1-\frac{4(m^2-3ab-1)}{m(m-1)(ab+m+1)}.
\]

For fixed \(m\), outer diversity increases strictly with the product \(ab\). Thus among complete bipartite graphs of order \(m\), the star \(K_{1,m-1}\) minimizes outer diversity, while the most balanced shore sizes maximize it, uniquely up to exchanging shores. In particular the star specializes to the previously established formula \(1-2/m+4/m^2\).

There are three asymptotic scales. Writing \(s=\min(a,b)\), and sending \(m\to\infty\):

1. For fixed \(s\geq1\), \(X_{a,b}/m\) converges in distribution to a \(\operatorname{Beta}(1,s)\) random variable, with survival function \((1-t)^s\) for \(0\leq t\leq1\), and \(\mathbb E X_{a,b}/m\to 1/(s+1)\).
2. If \(s\to\infty\) while \(s/m\to0\), then \((s/m)X_{a,b}\) converges in distribution to \(\operatorname{Exp}(1)\), and \(\mathbb E X_{a,b}\sim m/s\).
3. If \(a/m\to\rho\in(0,1)\), then \(X_{a,b}\) converges to the discrete law \(\Pr(X=d)=\rho(1-\rho)[\rho^d+(1-\rho)^d]\), for \(d\in\{0,1,\ldots\}\); its mean is \(1/[\rho(1-\rho)]-3\).

The corresponding normalized outer-diversity deficits \(1-\operatorname{outdiv}\) have orders \(m^{-1}\), \((sm)^{-1}\), and \(m^{-2}\), respectively, with leading constants obtained from the displayed exact mean.

## Assumptions and scope

The candidates are labeled, both shores are nonempty, and \(m\geq3\). The graph is unweighted, simple, undirected and complete across its two shores. A ranking \(\pi\) is in \(\operatorname{SP}(G)\) exactly when the subgraph induced by its top \(t\) candidates is connected for every \(1\leq t\leq m\). Kendall distance counts discordant unordered candidate pairs, equivalently adjacent transpositions. All probability statements concern the uniform measure on all \(m!\) rankings, not a random election or a voter-profile distribution.

The falling factorial \((q)_{\underline j}\) denotes \(q(q-1)\cdots(q-j+1)\) when \(0\leq j\leq q\), equals \(1\) at \(j=0\), and equals \(0\) for \(j>q\). Point probabilities at distances outside \(\{0,\ldots,\max(a,b)-1\}\) are zero.

## Proof

**Step 1: Characterize the domain.** On a complete bipartite graph every nonempty induced subgraph containing candidates from both shores is connected. Conversely a two-vertex induced subgraph within one shore is disconnected. Therefore a ranking has all top prefixes connected exactly when its first two candidates lie in opposite shores. There are \(2ab\) ways to choose and order such a first pair, and \((m-2)!\) orders of the rest.

**Step 2: Determine the exact nearest distance.** If the first two candidates lie in opposite shores, the distance is zero. Otherwise, let \(L\) be the number of initial consecutive candidates from the first candidate's shore; because both shores are nonempty, the next candidate is in the other shore. Moving this first opposite-shore candidate to position two by \(L-1\) adjacent swaps gives an admissible ranking. Any admissible ranking must have an opposite-shore candidate in one of its first two positions. The first such candidate in the original ranking is at position \(L+1\); to reach position two requires at least \(L-1\) adjacent swaps, and to reach position one requires still more. This lower bound proves \(X=L-1\). It is an equality for every ranking, not merely an average.

**Step 3: Count the entire distribution.** The event \(X\geq d\), for integer \(d\geq1\), says that the first \(d+1\) candidates lie in one shore. Counting ordered without-replacement initial strings from either shore gives the tail probability. The event \(X=d\) additionally requires the next candidate to lie in the other shore. Counting the two exclusive cases gives the point-mass formula. In particular the largest possible initial monochromatic run has length \(\max(a,b)\).

**Step 4: Compute the mean and diversity.** Condition on whether the first candidate belongs to the shore of size \(a\) or \(b\). If it is in the first shore, the expected number of additional candidates from that shore before the first candidate of the other shore is \((a-1)/(b+1)\). This follows by interleaving the remaining \(a-1\) first-shore candidates among the \(b+1\) gaps before, between and after the \(b\) opposing candidates, with all candidate orderings symmetric. Symmetrically the conditional expectation is \((b-1)/(a+1)\) when the first candidate is in the second shore. Weighted by \(a/m\) and \(b/m\), this yields the first expectation formula; reducing to a common denominator gives the second. The standard normalized outer diversity is \(1-2\mathbb E X/\binom{m}{2}\), yielding the displayed value.

For fixed \(m\), write \(t=ab\), and regard \(\mathbb E X=(m^2-3t-1)/(t+m+1)\) as a rational function of \(t\). Its derivative is

\[
\frac{d}{dt}\mathbb E X=-\frac{(m+1)(m+2)}{(t+m+1)^2}<0.
\]

Since \(ab=a(m-a)\) is minimized at \(a\in\{1,m-1\}\) and maximized when the shores differ by at most one, the claimed extremal ordering follows; the outer-diversity monotonicity is the reverse of the mean-distance monotonicity. Substituting \(a=1\) gives \(\mathbb E X=(m-1)(m-2)/(2m)\) and the star formula.

**Step 5: Establish all three limits.** If the smaller shore has a fixed size \(s\), its \(s\) labeled positions, scaled by \(m\), converge jointly as an unordered sample to \(s\) independent uniform points in \([0,1]\). The initial candidate is in the larger shore with probability tending to one. Consequently the first small-shore arrival, and hence \(X/m\), converges to the minimum of those uniform points, which has the stated beta law. The mean follows directly from the exact formula, avoiding an unproved interchange of moments.

If \(s\to\infty\) with \(s/m\to0\), use the exact tail, taking \(d=\lfloor xm/s\rfloor\) for fixed \(x>0\). The contribution of a prefix wholly within the small shore vanishes. The other contribution is

\[
\frac{(m-s)_{\underline{d+1}}}{(m)_{\underline{d+1}}}
=\prod_{j=0}^{d}\left(1-\frac{s}{m-j}\right),
\]

whose logarithm is \(-x+o(1)\), since \(d/m\to0\), \(s/m\to0\), and \(s(d+1)/m\to x\). Thus the rescaled tail tends to \(e^{-x}\). The mean follows from the exact rational identity.

Finally, if \(a/m\to\rho\in(0,1)\), each fixed-length initial string has asymptotically independent shore labels with probabilities \(\rho\) and \(1-\rho\). Passing to the point-probability formula gives the claimed geometric mixture. Its masses sum to one. The exact rational mean converges to \(1/[\rho(1-\rho)]-3\), and the three normalized-deficit orders follow immediately. These arguments cover the boundary \(d=0\), small shores and balanced shores without extrapolating from finite experiments.

## Verification

The accompanying standard-library Python program `verify.py` performs an independent multi-source breadth-first search on the adjacent-swap permutation graph, using all admissible rankings as sources. It checks **every ranking** for each \(3\leq m\leq8\) and every shore split up to exchanging shores. It compares actual shortest-path distances with the initial-run formula and matches the exact rational point probabilities and means. The full analytic result is independent of these finite tests.

To reproduce, save `verify.py` from this package and run `python verify.py`. No third-party packages or external services are required.

## Relationship to prior work

Faliszewski, Sornat, Szufa and Wąs (2026) introduced outer diversity for structured preference domains, including single-peaked domains on general graphs, and proved the nearest-ranking problem NP-complete for general graph inputs. Their results do not imply the present full exact complete-bipartite distribution: this family has a special two-position connected-prefix constraint.

Faliszewski, Jabrocki, Słuszniak, Sornat, Szufa and Wąs (2026) computed outer diversity for star-based single-peaked domains as \(1-2/m+4/m^2\), among other results. That is exactly the \(\min(a,b)=1\) specialization of the formula above; it does not yield the nonstar \(K_{a,b}\) law, the balanced-shore extremum, or the beta-to-exponential-to-geometric transition. Complete bipartite graphs with both shore sizes at least two contain cycles and need not define weak Condorcet domains. The finding concerns graph-based single-peakedness and outer diversity, not Condorcet stability.

## Limitations

The exact form relies on full adjacency between the shores. Deleting cross-shore edges can invalidate the first-two-position characterization and all formulas. The asymptotics concern one uniformly random ranking, not the distribution of election outcomes, and the positive novelty assessment is not a claim of exhaustive publication priority. The numerical verification covers at most eight candidates; the general assertion is established by proof.

## References

- Faliszewski, P., Sornat, K., Szufa, S., and Wąs, T. *Outer Diversity of Structured Domains*. arXiv:2602.15708v1, 17 February 2026. https://arxiv.org/html/2602.15708v1
- Faliszewski, P., Jabrocki, J., Słuszniak, M., Sornat, K., Szufa, S., and Wąs, T. *Outer Diversity of Condorcet Domains*. arXiv:2610.00720v1, 30 September 2026. https://arxiv.org/html/2610.00720v1
