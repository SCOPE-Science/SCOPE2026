# Extremal pairing for ex-post envy-freeness of stochastically ordered lottery goods

## Finding

**Extremal-pairing theorem.** Consider two agents dividing four distinguished, independently valued nonnegative lottery goods, whose continuous per-good laws are identical across agents and ordered by first-order stochastic dominance from strongest to weakest. Require each agent to receive exactly two distinguished goods. Other goods are allowed, provided the already-assigned background bundles have the same value law, are independent of the distinguished goods and of one another, and are identically distributed across agents. Then, among all three ways to partition the distinguished goods into two pairs, **pairing the strongest with the weakest maximizes the probability of ex-post envy-freeness**; pairing the strongest with the second strongest minimizes it. This holds without a common convolution-power representation, symmetric utility laws, equal expectations, or ex-ante envy-freeness.

More precisely, let \(X_1,X_2,X_3,X_4\) be independent, atomless, nonnegative random variables with finite means and
\[
X_1\succeq_{\mathrm{st}}X_2\succeq_{\mathrm{st}}X_3\succeq_{\mathrm{st}}X_4.
\]
Let \(U,V\) be independent, identically distributed nonnegative background bundle values, independent of the four distinguished values. Write
\[
p_{ij}=\Pr(U+X_i+X_j>V+X_k+X_\ell),\qquad
\{k,\ell\}=\{1,2,3,4\}\setminus\{i,j\}.
\]
Then
\[
p_{12}\ge p_{13}\ge\frac12,\qquad
1-p_{13}\le p_{14}\le p_{13}.
\]
If all agent-item values are mutually independent and each good has the same law for both agents, the three ex-post envy-free probabilities are \(E_{ij}=p_{ij}(1-p_{ij})\). Consequently,
\[
\boxed{E_{14}\ge E_{13}\ge E_{12}}.
\]
The statement allows arbitrarily many background items when their two bundle sums have the same law, including an equal number of independent identically distributed background items in each bundle. Equality is possible; the theorem asserts weak optimality.

The distinction from ordering goods only by mean is essential. There are four atomless, independent nonnegative item laws whose means are strictly ordered from largest to smallest but for which the middle pairing yields ex-post fairness probability \(1/4\), whereas the extreme pairing yields only \(9/100\).

## Assumptions and scope

A deterministic allocation is chosen before utility realization. The agents have additive nonnegative utility for bundles. For each distinguished good \(j\), both agents independently observe a value distributed as \(X_j\); valuations are independent across goods and agents. Likewise, their background bundle values are independent and identically distributed, with the same background value law on both sides of the division. The allocation must put exactly two of the four distinguished goods in each agent's bundle; the background division is fixed. First-order stochastic dominance \(A\succeq_{\mathrm{st}} B\) means \(\Pr(A>t)\ge\Pr(B>t)\) for every real \(t\). Atomless distinguished values ensure no ties in comparing bundle sums. No independence between the allocations themselves is asserted; the independence is between the agents' random valuations.

## Proof

**Stochastic difference lemma.** For independent \(A,B\) with \(A\succeq_{\mathrm{st}}B\), one has \(A-B\succeq_{\mathrm{st}}B-A\). Indeed, take independent copies \(B',B''\) of \(B\) and an independent copy \(A'\) of \(A\). First-order dominance is preserved under independent addition, so
\[
A-B\succeq_{\mathrm{st}}B'-B
\succeq_{\mathrm{st}}B'-A',
\]
and the last law equals the law of \(B-A\). Both inequalities use independent stochastic replacements, not a comparison of dependent observations.

Set \(T=U-V\). Since \(U,V\) are iid, \(T\) is symmetric about zero and independent of the distinguished values. With strict comparisons justified by atomlessness, the preceding lemma applied to \(X_2,X_3\) gives
\[
\begin{aligned}
p_{12}&=\Pr(T+(X_1-X_4)+(X_2-X_3)>0)\\
&\ge\Pr(T+(X_1-X_4)+(X_3-X_2)>0)=p_{13}.
\end{aligned}
\]
To show \(p_{13}\ge1/2\), set \(Z=T+(X_1-X_2)+(X_3-X_4)\). The lemma and symmetry of \(T\) imply \(Z\succeq_{\mathrm{st}}-Z\). As \(Z\) is atomless,
\[
p_{13}=\Pr(Z>0)\ge\Pr(-Z>0)=1-p_{13}.
\]
Again applying the difference lemma to \(X_3,X_4\), we get
\[
\begin{aligned}
p_{13}&=\Pr(T+(X_1-X_2)+(X_3-X_4)>0)\\
&\ge\Pr(T+(X_1-X_2)+(X_4-X_3)>0)=p_{14}.
\end{aligned}
\]
Finally, apply the lemma to \(X_1,X_2\), using \(T\stackrel{d}= -T\):
\[
\begin{aligned}
p_{14}&=\Pr(T+(X_1-X_2)+(X_4-X_3)>0)\\
&\ge\Pr(T+(X_2-X_1)+(X_4-X_3)>0)\\
&=\Pr(-Z>0)=1-p_{13}.
\end{aligned}
\]
Thus \(p_{14}\in[1-p_{13},p_{13}]\) and \(p_{12}\ge p_{13}\ge1/2\). These imply
\[
\left|p_{14}-\frac12\right|\le p_{13}-\frac12\le p_{12}-\frac12.
\]
Because the two agents' valuations are independent copies with the same per-item laws, their non-envy probabilities for allocation \((ij\mid k\ell)\) are \(p_{ij}\) and \(1-p_{ij}\). Multiplication and \(p(1-p)=1/4-(p-1/2)^2\) prove the asserted extremal order. In particular, the exact gains factor as
\[
E_{14}-E_{13}=(p_{13}-p_{14})(p_{13}+p_{14}-1),
\]
\[
E_{13}-E_{12}=(p_{12}-p_{13})(p_{12}+p_{13}-1),
\]
with nonnegative factors.

**Means alone do not suffice.** Let \(\eta\in(0,1/4)\), and add independent \(\mathrm{Unif}(0,\eta)\) noise to each of four base values. Take the first base value to be \(0,9,100\) with respective probabilities \(1/2,2/5,1/10\), and the other three base values to be deterministically \(9,3,1\). The means, before a common jitter mean is added, are \(68/5,9,3,1\), strictly decreasing. All pairwise comparisons have nonzero integer-part margins that cannot be reversed by the jitters. Direct conditioning on the first base value gives
\[
(p_{12},p_{13},p_{14})=(1,1/2,1/10),
\]
and hence \((E_{12},E_{13},E_{14})=(0,1/4,9/100)\). The item means are ordered but their distributions are not ordered by first-order stochastic dominance. This shows that replacing the stochastic-order hypothesis by decreasing means invalidates the conclusion.

## Verification

The proof covers all independent atomless laws satisfying the hypotheses, not merely finite experiments. The standalone `verify.py` checks \(1764\) chains of rational three-point laws ordered by stochastic dominance, with both no background and one symmetric Bernoulli background on each side (\(3528\) exact comparisons). Independent infinitesimal continuous jitter resolves equality with probability one, so the exact half-tie calculations coincide with the continuous model. It also checks the exponential example and the mean-order counterexample. Run: `python3 verify.py` (standard library only).

For independent exponential distinguished values with strictly decreasing means \((8,4,2,1)\) and no background, the win probabilities for strongest-pair, middle-pair and extreme-pair allocations are exactly
\[
(p_{12},p_{13},p_{14})=\left(\frac89,\frac{58}{81},\frac35\right),
\]
so the ex-post envy-free probabilities are, respectively,
\[
\left(\frac8{81},\frac{1334}{6561},\frac6{25}\right).
\]
For arbitrary positive exponential rates \(a,b,c,d\), a direct Laplace-transform calculation gives the comparison probability of \(\mathrm{Exp}(a)+\mathrm{Exp}(b)\) against an independent \(\mathrm{Exp}(c)+\mathrm{Exp}(d)\) as
\[
\frac{cd(a^2+ab+ac+ad+b^2+bc+bd+cd)}{(a+c)(a+d)(b+c)(b+d)}.
\]
This is independent supplementary evidence, not a replacement for the stochastic-order proof.

## Relationship to prior work

Igarashi and Oh, *Fair Division of Lotteries*, arXiv:2610.34906 (public 26 October 2026), formulate ex-post envy-freeness probabilities under independently realized random item values. Their Theorem 4.2 proves optimality of an ex-ante envy-free allocation for two agents when item distributions belong to a common convolution-power family; Theorem 4.5 extends such reasoning under log-concavity of a common generator; Proposition 5.6 treats non-atomic symmetric item distributions. None of these conditions is required by the theorem above, which instead produces an explicit exact optimum among all two-two splits of four first-order-stochastically ordered, not necessarily symmetric, heterogeneous lotteries even when no ex-ante envy-free split exists. Their generic approximation bound does not imply which split is optimal. The present four-good extremal ordering is not stated in the inspected sections.

Aloisio et al., *Approximately Fair Allocation of Indivisible Items with Random Valuations*, AAMAS 2024, study expected maximum envy and randomized allocation guarantees, not distribution-free maximization of the exact ex-post envy-free probability among fixed two-two splits. Other random-assignment literature often randomizes allocation rather than the goods' exogenous realized values. The stochastic-difference lemma is elementary and is not claimed as independently novel; the proposed contribution is its complete sharp application to the natural four-heterogeneous-good pairing problem, including the symmetric background extension and the mean-order boundary.

## Limitations

The result assumes full independence of agent-item values and common per-item distributions across the two agents, and a fixed equal two-two split of the four heterogeneous goods. It does not assert optimality over one-versus-three heterogeneous splits, over arbitrarily assigned unequal-law background bundles, or when all items are correlated. Continuous values are used to avoid a positive probability of tied bundle totals: with atoms, ex-post envy-freeness can benefit from ties and a different statement is needed. First-order stochastic dominance is sufficient, not asserted necessary; the means-only example shows only that means do not replace it. Unindexed or inaccessible equivalent rearrangement results remain a literature-priority risk. No independent scientific audit has been performed.

## References

1. A. Igarashi and Y. Oh, *Fair Division of Lotteries*, arXiv:2610.34906, first posted 2026-10-26. https://arxiv.org/abs/2610.34906 ; readable manuscript https://arxiv.org/html/2610.34906 .
2. A. Aloisio, V. Bilò, A. M. Caruso, M. Flammini, and C. Vinci, *Approximately Fair Allocation of Indivisible Items with Random Valuations*, AAMAS 2024, pp. 2120–2122. https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p2120.pdf .
3. M. Shaked and J. G. Shanthikumar, *Stochastic Orders*, Springer, 2007 (standard stochastic-order background, not used for any unproved special lemma).
