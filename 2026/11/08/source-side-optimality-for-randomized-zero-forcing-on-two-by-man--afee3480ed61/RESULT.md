# Source-side optimality for randomized zero forcing on two-by-many bicliques

## Finding
Let \(a\ge3\) be an integer, and let \(G\) be the bidirected, unweighted complete bipartite graph \(K_{a,2}\). Under randomized zero forcing, every white vertex independently becomes blue in each simultaneous round with probability equal to the fraction of its incoming neighbors that are blue; blue vertices never revert.

Write \(T_A(a)\) for the expected time to make every vertex blue from a single blue vertex in the part of size \(a\), and \(T_B(a)\) for the analogous expectation from the part of size two. Then
\[
 T_B(a)<T_A(a)\quad\text{for every integer }a\ge3,
 \qquad T_A(a)-T_B(a)=\frac a2+O(\log a).
\]
For \(a=2\) the expectations are equal (both are \(3\)). This resolves the two-vertex-side case of the source-location conjecture in Geneson--Hicks--Lichtenberg--Moon--Robles (2026).

A finite rational recurrence is also provided, so both expectations are exactly computable for every \(a\ge2\).

## Assumptions and scope
All graphs are finite, simple, and bidirected: each undirected edge is replaced by its two directed orientations, both of weight one. Updates occur simultaneously, and conditional on the present blue set the white-vertex updates are independent. A source is a single initially blue vertex. No claim is made for the analogous probabilistic zero-forcing rule, where *blue senders* attempt to infect neighbors with a different probability.

Use \((i,j)\), with \(0\le i\le a\), \(0\le j\le2\), for the state having \(i\) blue vertices in the larger part and \(j\) in the smaller part. In one round the numbers of newly blue vertices in those parts are independent random variables distributed as \(\operatorname{Bin}(a-i,j/2)\) and \(\operatorname{Bin}(2-j,i/a)\), respectively.

## Proof
**Exact rational recurrence.** Put \(H_i=\mathbb E[\tau\mid(i,1)]\). Because all remaining large-part vertices turn blue with certainty one round after both small-part vertices are blue, \(H_a=1\) and \(\mathbb E[\tau\mid(k,2)]=\mathbf1_{k<a}\). Fix \(i<a\), set \(b=a-i\) and \(p=i/a\). First-step analysis, moving the unique self-loop to the left, gives
\[
 H_i=\frac{1+\sum_{u=0}^{b}\binom bu2^{-b}
 \left[p\mathbf1_{i+u<a}+(1-p)\mathbf1_{u>0}H_{i+u}\right]}
 {1-(1-p)2^{-b}}.
\]
The denominator is strictly positive. Computing from \(i=a\) down to \(i=0\) therefore gives exact rational numbers. If the initial blue vertex lies in the size-two part, the expected time is \(T_B(a)=H_0\).

If instead the initial blue vertex lies in the size-\(a\) part, both smaller-part vertices independently turn blue with probability \(1/a\) in each round until at least one does. The waiting time \(W\) to the first such round has success probability
\[
 q=1-(1-1/a)^2=(2a-1)/a^2.
\]
Conditional on a successful round, one smaller-part vertex turns blue with probability \(2(a-1)/(2a-1)\) and both turn blue with probability \(1/(2a-1)\). No other large-part vertices can be infected during that waiting phase. Therefore
\[
 T_A(a)=\frac{1+2(a-1)H_1/a^2+1/a^2}{(2a-1)/a^2}.
\]
The last term in the numerator is the contribution of the one subsequent deterministic round when both smaller-part vertices are newly blue.

**Bounds separating the two starting sides.** At the first successful round of the initial waiting phase in the size-\(a\) start, some large-part vertices are still white. Thus
\[
 T_A(a)\ge\frac{a^2}{2a-1}+1.
\]
Starting in the size-two part, couple each large-part vertex to an independent geometric clock of success probability \(1/2\), using the same independent uniforms as the actual process. Since at least one smaller-part vertex always stays blue, each large-part vertex is infected no later than its corresponding clock. Once all \(a\) large-part vertices are blue, any remaining smaller-part vertex becomes blue at the next round with probability one. If \(M\) is the maximum of these \(a\) independent geometric clocks and \(r=\lceil\log_2 a\rceil\), then
\[
 T_B(a)\le\mathbb E M+1
 \le 1+\sum_{t=0}^{\infty}\min\{1,a2^{-t}\}
 \le r+3.
\]
(The sum is an upper bound for \(\mathbb E M=\sum_{t\ge0}\Pr(M>t)\).)

For \(12\le a\le16\), the increasing function \(a^2/(2a-1)\) shows that the lower bound on \(T_A\) is at least \(144/23+1>7\), whereas \(T_B\le7\). For \(a\ge17\), writing \(r=\lceil\log_2 a\rceil\ge5\), we have \(a\ge2^{r-1}+1>2r+4\), where the last inequality follows by induction from \(r=5\). Hence
\[
 T_A(a)>a/2+1>r+3\ge T_B(a).
\]

For the remaining nine values \(3\le a\le11\), the rational recurrence above gives \(H_0<7/2<T_A(a)\) in every case. This is **exact rational arithmetic**, not a numerical extrapolation; `verify.py` computes all nine inequalities using integer numerators and denominators, and verifies every entry in `rational_certificates.tsv` and independently reconstructs the full labelled-subset Markov chain for \(2\le a\le6\). The case \(a=2\) gives equality \(T_A(2)=T_B(2)=3\) by symmetry or the same recurrence.

**Gap asymptotics.** When the first smaller-part infection occurs from the larger-part start, the blue set contains a smaller-part blue vertex. Using a common-uniform attractive coupling, the expected *additional* time is at most \(T_B(a)\). Thus
\[
 \frac{a^2}{2a-1}+1-T_B(a)\le T_A(a)-T_B(a)
 \le\frac{a^2}{2a-1}.
\]
Together with \(T_B(a)\le\lceil\log_2a\rceil+3\), and \(a^2/(2a-1)=a/2+O(1)\), this yields the claimed \(a/2+O(\log a)\) gap.

## Verification
Run `python3 verify.py` next to `rational_certificates.tsv` with Python 3.9 or later; only the standard library is required. It performs rational first-step recurrences for every \(a=3,\ldots,11\), proves the two strict comparisons against \(7/2\) without rounding, checks the equal-size boundary, and independently enumerates **every labelled blue subset** and every possible simultaneous infection outcome for \(a=2,3,4,5,6\). The infinite inequality is established algebraically above; finite checks alone do not establish it.

## Relationship to prior work
Geneson, Hicks, Lichtenberg, Moon and Robles (2026), Section 3.6, study this exact randomized zero-forcing rule on bidirected complete bipartite graphs. They prove a broad big-O upper bound, tabulate expectations for small part sizes, and formulate a conjecture favoring a source in the smaller part. The strict comparison above proves the complete width-two slice; its finite data are compatible with their table, but the all-parameter inequality is not a corollary of their displayed big-O bound or finite table. The 2019 Markov-chain paper by Chan and collaborators studies *probabilistic* zero forcing, a distinct update rule. Its Conjecture 2.6 favors a start in the **larger** part (when the other part has size at least two and the larger part exceeds three), the opposite direction to the present result for the recipient-side randomized rule; neither conjecture is an implication of the other. The general Markov-chain method alone does not imply the current uniform inequality.

## Limitations
This establishes the source-location conjecture only when the smaller part has exactly two vertices and the larger part has at least three. It assumes equal incoming edge weights and simultaneous independent updates. The exact finite state recurrence uses rational arithmetic whose size increases with \(a\), and no closed elementary expression for each expectation is claimed. Historical priority is assessed only against checked accessible sources; an unindexed covering result remains possible. Independent mathematical validation has not been performed.

## References
1. J. Geneson, I. Hicks, N. Lichtenberg, A. Moon and N. Robles, *Randomized Zero Forcing*, arXiv:2602.16300v1 (first public submission February 18, 2026), Sections 1, 3.6 (Theorem 3.7 and Conjecture 3.12). https://arxiv.org/abs/2602.16300
2. Y. Chan, E. Curl, J. Geneson, L. Hogben, K. Liu, I. Odegard and M. S. Ross, *Using Markov chains to determine expected propagation time for probabilistic zero forcing*, arXiv:1906.11083v1 (June 25, 2019), Sections 1--2. https://arxiv.org/abs/1906.11083
