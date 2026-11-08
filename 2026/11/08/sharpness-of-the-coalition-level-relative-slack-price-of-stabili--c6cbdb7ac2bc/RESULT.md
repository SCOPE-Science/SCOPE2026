# Sharpness of the coalition-level relative-slack price-of-stability guarantee

## Finding

**Theorem.** Fix a real number \(0<\delta<1\). In every finite symmetric pairwise hedonic coalition game in which every nonempty coalition has coordinator-retained slack satisfying
\[
0\le r(S)\le\delta W(S),
\]
the grand coalition is Nash stable and attains at least \(1-\delta\) of the largest possible partition welfare. This guarantee cannot be improved uniformly: for every fixed \(\delta\), three-agent examples with all positive pairwise utilities have a unique Nash-stable partition of welfare \(1-\delta+2\varepsilon\) and a unique social optimum of welfare \(1\), where \(\varepsilon\) may be arbitrarily small and positive. Two agents never exhibit this efficiency gap under the same condition.

Equivalently, for positive optimal welfare, the universal **supremum** of the price of stability over all such games is
\[
\sup\operatorname{PoS}=\frac{1}{1-\delta}.
\]

## Assumptions and scope

Let \(N\) be a finite set of \(n\ge2\) participants. For each nonempty \(S\subseteq N\), the primitive transferable surplus \(W(S)\) is an arbitrary real number, not assumed monotone or superadditive. A symmetric matrix \(v\), with \(v_{ij}=v_{ji}\) and \(v_{ii}=0\), induces the hedonic participant utility
\[
U_i(S)=\sum_{j\in S\setminus\{i\}}v_{ij},\qquad U_i(\{i\})=0.
\]
For a coalition \(S\) put \(P(S)=\sum_{\{i,j\}\subseteq S}v_{ij}\) and define retained coordinator surplus \(r(S)=W(S)-2P(S)\). The hypothesis is \(0\le r(S)\le\delta W(S)\) for **every** nonempty coalition, not merely for the optimum partition. A partition \(\Pi\) is Nash stable if no participant can strictly improve by moving to another existing coalition or to an empty destination. Its welfare is \(\operatorname{SW}(\Pi)=\sum_{S\in\Pi}W(S)\). The price of stability is the ratio of optimal welfare to the greatest Nash-stable welfare, when optimal welfare is positive.

## Proof

**Structural implication.** Since \(\delta>0\), the inequalities \(0\le r(S)\le\delta W(S)\) force \(W(S)\ge0\). Moreover,
\[
2P(S)=W(S)-r(S)\ge(1-\delta)W(S)\ge0.
\]
For \(S=\{i,j\}\), we have \(P(S)=v_{ij}\), hence \(v_{ij}\ge0\) for every pair. In the grand coalition every participant obtains the nonnegative utility \(\sum_{j\ne i}v_{ij}\), so no one strictly prefers leaving to be alone. There is no other destination coalition. Thus the grand coalition is Nash stable.

For an arbitrary partition \(\Pi\), nonnegative pair values give
\[
\operatorname{SW}(\Pi)
\le\frac{2}{1-\delta}\sum_{S\in\Pi}P(S)
\le\frac{2P(N)}{1-\delta}
\le\frac{W(N)}{1-\delta}.
\]
The middle step holds because the within-coalition unordered pairs form a subset of all unordered pairs. The last step is \(2P(N)=W(N)-r(N)\le W(N)\). Thus \(W(N)\ge(1-\delta)\max_\Pi\operatorname{SW}(\Pi)\), proving the universal estimate.

**Three-person sharpness.** Choose any \(0<\varepsilon<\delta/2\) and write \(N=\{1,2,3\}\). Assign strictly positive pair values
\[
v_{12}=\frac{1-\delta}{2},\qquad v_{13}=v_{23}=\frac{\varepsilon}{2}.
\]
Set the primitive surpluses as follows:
\[
\begin{aligned}
W(\{i\})&=0\quad(i=1,2,3),\\
W(\{1,2\})&=1,\\
W(\{1,3\})=W(\{2,3\})&=\varepsilon,\\
W(N)&=1-\delta+2\varepsilon.
\end{aligned}
\]
Direct substitution gives \(r(\{1,2\})=\delta=\delta W(\{1,2\})\), while \(r(S)=0\) for every other nonempty \(S\). Thus **every** coalition meets the stronger relative-slack condition.

There are exactly five set partitions of three participants. The welfare of the grand coalition is \(1-\delta+2\varepsilon\); the partition \(\{\{1,2\},\{3\}\}\) has welfare \(1\); the other two pair-plus-singleton partitions have welfare \(\varepsilon\); and all singletons have welfare zero. Because \(0<\varepsilon<\delta/2\) and \(\delta<1\), the pair \(\{1,2\}\) plus singleton \(\{3\}\) is uniquely welfare-optimal.

Every nongrand partition has a singleton. That singleton strictly gains by joining an existing other coalition because every pair value is positive. Consequently every nongrand partition fails Nash stability; the grand coalition is uniquely Nash stable. Therefore
\[
\operatorname{PoS}=\frac{1}{1-\delta+2\varepsilon}\nearrow\frac{1}{1-\delta}
\quad\text{as }\varepsilon\downarrow0.
\]
This establishes the asserted sharp supremum.

**Minimality.** With exactly two participants, the singleton inequalities imply \(W(\{i\})=r(\{i\})=0\), while the pair has \(W(N)\ge0\) and \(v_{12}\ge0\). Hence the grand coalition is both welfare-optimal and Nash stable. If optimal welfare is positive, its price of stability is one. For \(\delta=0\), exact budget balance separately implies price of stability one whenever the ratio is defined, although the grand coalition need not be stable when pair values are negative.

## Verification

The standalone standard-library script `checker.py` implements the five set partitions, all seven nonempty coalitions, and every unilateral Nash deviation using exact rational arithmetic. Executing `python3 checker.py` passed \(2245\) rational parameter tests, checking each coalition's slack, optimum uniqueness, Nash-stability uniqueness and the exact ratio. For the sample \(\delta=2/5\), \(\varepsilon=1/100\), it gives \(\operatorname{PoS}=50/31\). The continuous-parameter and all-population-size assertions above follow from the algebraic proof, not from these finite tests.

## Relationship to prior work

Hasan's 2026 coalition-formation framework defines these utility, potential and retained-slack quantities. Its Corollary 5.12 gives the universal \(1/(1-\delta)\) upper bound under coalition-level relative slack, and its Proposition 5.13 provides an asymptotically tight construction **only** under weaker optimum-partition slack: its positive singleton slack violates the coalition-level condition. The text explicitly leaves open whether the stronger coalition-level hypothesis permits improvement. The example above places the permitted slack on a pair coalition instead, answering that precise sharpness question. The additional deduction that this hypothesis forces all pair utilities nonnegative and makes the grand coalition Nash stable is used directly in the proof.

Donahue and Kleinberg (2021) bound stability inefficiency in a distinct federated-learning model based on agents' expected prediction errors; their price-of-anarchy bound neither states nor implies this ratio under arbitrary transferable coalition surpluses and proportional coordinator slack.

## Limitations

The result is about the specified symmetric pairwise transfer model, not learned model accuracy in any particular federated-learning system. No monotonicity, submodularity or other structure of \(W\) is asserted; adding such restrictions may change sharpness. The universal constant is a supremum approached by examples as \(\varepsilon\) tends to zero; attainment at a positive parameter is not asserted. No quantitative bound on the number of improvement steps is proved. Independently replicated scientific validation has not been performed.

## References

1. C. Hasan, *Stable and Budget-Feasible Coalition Formation for Clustered Federated Learning: A Hedonic Potential-Game Approach*, Research Square preprint, first publicly posted July 21, 2026, DOI: https://doi.org/10.21203/rs.3.rs-10405564/v1; arXiv:2607.26788 (July 29, 2026), https://arxiv.org/abs/2607.26788. See Sections 4.2 and 5.1–5.3, especially Corollary 5.12 and Proposition 5.13.
2. K. Donahue and J. Kleinberg, *Optimality and Stability in Federated Learning: A Game-theoretic Approach*, NeurIPS 2021, https://arxiv.org/abs/2106.09580. See Sections 1–3 and the price-of-anarchy model definition.
