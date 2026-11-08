# First leaf-optimal proper double star for probabilistic zero forcing

## Finding

Let \(D_{a,b}\), with integers \(2\le a\le b\), be the tree formed by joining two hubs with \(a\) and \(b\) pendant leaves, respectively. Run standard synchronous probabilistic zero forcing from exactly one initial blue vertex. Denote by \(h_a,h_b,\ell_a,\ell_b\) the mean numbers of rounds to complete infection when started at a hub on the \(a\)- or \(b\)-leaf side, or a leaf on the corresponding side.

**Theorem (sharp first peripheral seed among proper double stars).** Every proper double star with at most eight vertices has an optimal one-vertex seed at a hub. At nine vertices, there are exactly two proper double-star isomorphism types: \(D_{2,5}\) and \(D_{3,4}\). The **unique optimal seed orbit** of \(D_{2,5}\) is the set of its five leaves adjacent to the degree-six hub; the unique optimal seed orbit of \(D_{3,4}\) is its degree-five hub. Thus \(D_{2,5}\), on nine vertices, is the smallest proper double star for which any leaf achieves a lower expected propagation time than every hub.

The key new strict comparison is exact:
\[
 h_5-\ell_5=\frac{10821394247161847}{236576000775098985}>0\quad\text{in }D_{2,5},
\]
whereas the corresponding larger-side hub is better than its adjacent leaf for \(D_{2,3}\), \(D_{2,4}\), and \(D_{3,4}\). In all unequal types in this classification, the degree-larger hub outperforms the smaller hub, and its corresponding leaf outperforms the smaller-side leaf. For the equal types \(D_{2,2}\) and \(D_{3,3}\), both hubs tie and strictly outperform every leaf. Consequently, all optimal source orbits through order nine are classified.

## Assumptions and scope

Graphs are finite, simple, undirected, unweighted and connected. A blue vertex \(u\) attempts to turn each white neighbor \(w\) blue independently with probability \(\lvert N[u]\cap B\rvert/\deg(u)\) determined by the blue set at the **start** of each simultaneous round. Infected vertices remain blue. The completion time is the first whole-number round at which all vertices are blue, with the initial seed at time zero. The adjective *proper* is essential: both hubs have at least two pendant leaves. The statement does **not** assert a first reversal among all trees or among double stars with one leaf on a side. The classification is limited to \(a+b+2\le9\). Primary classification is MSC2020 60J10 (finite Markov absorption times).

## Proof

We give exact finite recurrences for every seed type in an arbitrary proper double star, and use them to check exhaustively the six types of order at most nine. These recurrences follow directly from first-step conditioning; there is no extrapolation from a numerical experiment.

When both hubs are blue and exactly \(i\) and \(j\) leaves on their sides are blue, let \(F(i,j)\) be the expected remaining number of rounds. Set \(F(a,b)=0\). When \(i<a\), each of the \(a-i\) white leaves on that side is independently infected next round with probability \(p_i=(i+2)/(a+1)\). When \(j<b\), each of the \(b-j\) white leaves on that side has infection probability \(q_j=(j+2)/(b+1)\). For \(i=a\) or \(j=b\), interpret the corresponding new-leaf count as identically zero. Put
\[
 P_i(r)=\binom{a-i}{r}p_i^r(1-p_i)^{a-i-r},\qquad
 Q_j(s)=\binom{b-j}{s}q_j^s(1-q_j)^{b-j-s},
\]
with point masses at zero when a side is complete. The two sides' infections are independent; hence for \((i,j)\ne(a,b)\),
\[
 F(i,j)=\frac{1+\displaystyle\sum_{\substack{0\le r\le a-i,\ 0\le s\le b-j\\r+s>0}}
 P_i(r)Q_j(s)F(i+r,j+s)}{1-P_i(0)Q_j(0)}.
\]
Every denominator is positive because at least one white leaf has positive infection probability; the recurrence terminates by backward induction on \(i+j\).

Now let \(G_a(i)\) be the expected remaining rounds with the \(a\)-side hub blue, the other hub white, and exactly \(i\) leaves on the first side blue. No leaf on the other side can yet be blue. The first hub attempts to infect both its white leaves and the opposite hub independently, each with probability \(t_i=(i+1)/(a+1)\). Let \(A_i(r)=\binom{a-i}{r}t_i^r(1-t_i)^{a-i-r}\). First-step conditioning yields
\[
 G_a(i)=\frac{1+\displaystyle\sum_{r=0}^{a-i} A_i(r)t_i F(i+r,0)
 +\displaystyle\sum_{r=1}^{a-i} A_i(r)(1-t_i)G_a(i+r)}
 {1-A_i(0)(1-t_i)}.
\]
Similarly, if only the \(b\)-side hub is blue, with \(j\) adjacent leaves blue, its expected remaining rounds satisfy
\[
 G_b(j)=\frac{1+\displaystyle\sum_{s=0}^{b-j} C_j(s)u_j F(0,j+s)
 +\displaystyle\sum_{s=1}^{b-j} C_j(s)(1-u_j)G_b(j+s)}
 {1-C_j(0)(1-u_j)},
\]
where \(u_j=(j+1)/(b+1)\) and \(C_j(s)=\binom{b-j}{s}u_j^s(1-u_j)^{b-j-s}\). The denominators here also are positive, and recursion downward in \(i\) or \(j\) is well-founded. The four single-seed expectations are exactly
\[
 (h_a,h_b,\ell_a,\ell_b)
 =(G_a(0),G_b(0),1+G_a(1),1+G_b(1)).
\]
The additional first round for a leaf seed is deterministic: a degree-one blue leaf forces its sole hub neighbor with probability one, without any other infection that round.

Finally, since \(2\le a\le b\) and \(a+b+2\le9\), the **entire** set of types is
\[
 (a,b)\in\{(2,2),(2,3),(2,4),(3,3),(2,5),(3,4)\}.
\]
The supplied exact rational checker evaluates all four expressions by these recurrences for all six pairs, verifies every stated strict optimum, and checks the displayed rational difference for \(D_{2,5}\). For the two equal types it verifies equality of opposite-side expectations and strict hub dominance. Thus every orbit for every relevant graph is covered, proving both minimality and uniqueness of the optimal orbit. Independently, a second program path in the same supplied script constructs all individual vertex-labeled infection states and uses the original per-neighbor forcing rule, reproducing exactly all four rational expectations for **five** of the six graph types: \(D_{2,2}\), \(D_{2,3}\), \(D_{2,4}\), \(D_{2,5}\), and \(D_{3,4}\). The omitted symmetric \(D_{3,3}\) is still exactly proved by the quotient recurrence and its verification. The finite comparisons are exact and do not depend on rounded floating point.

## Verification

Use `python3 verify.py`. The implementation uses only standard-library arbitrary-precision `Fraction`, `comb`, and memoization, with no third-party data or stored artifacts. It prints the four expectations for each graph for orientation, but every theorem conclusion is asserted using exact rational comparisons. In particular, it asserts
\[
 \frac{45}{1000}< h_5-\ell_5<\frac{46}{1000}
\]
in \(D_{2,5}\), independently of printed decimals. The labeled-state implementation checks the same source types through size nine without reusing the quotient recurrences.

## Relationship to prior work

Geneson–Hogben (2018) introduced systematic expected PZF propagation-time investigations. Chan et al. (2019 preprint; 2020 published version) established general Markov-chain methods for exact PZF propagation times and studied seed placement on several graph families. In their published Section 2.1 they explicitly discuss **balanced** double stars \(D_{k,k}\), including the known transition from hub seeds for \(2\le k\le9\) to leaf seeds at \(k\ge10\), and use those graphs to discuss subdivision. That established balanced-family transition is **not** claimed as new here. In contrast, the theorem here exhaustively classifies the smallest **unequal** proper double stars and finds a leaf-optimal case already at nine vertices, a substantially earlier cutoff arising from asymmetry. The published general Markov-chain method is compatible with the recurrences but does not state these complete six-type exact comparisons or the nine-vertex first-leaf assertion. Deterministic zero-forcing and fractional fort-hypergraph results on double stars concern different forcing rules and do not imply this stochastic seed optimization result.

## Limitations

The classification is exact only for proper double stars with at most nine vertices. It does not claim a global smallest leaf-optimal tree, an all-parameter classification of unbalanced double stars, or any statement about larger unbalanced families. This is a finite theorem supported by exhaustive rational computation under rigorously proved recurrences, not an infinite monotonicity result. General Markov-chain techniques were known; the stated exact first threshold is the object assessed for historical originality. Independent literature-priority review has not been performed.

## References

1. J. Geneson and L. Hogben, *Propagation time for probabilistic zero forcing*, arXiv:1812.10476 (first public preprint December 24, 2018), https://arxiv.org/abs/1812.10476 .
2. Y. Chan, E. Curl, J. Geneson, L. Hogben, K. Liu, I. Odegard and M. Ross, *Using Markov Chains to Determine Expected Propagation Time for Probabilistic Zero Forcing*, arXiv:1906.11083 (first public preprint June 25, 2019); Electronic Journal of Linear Algebra 36 (2020), 318–333, especially Section 2.1, https://emis.de/ft/34759 .
