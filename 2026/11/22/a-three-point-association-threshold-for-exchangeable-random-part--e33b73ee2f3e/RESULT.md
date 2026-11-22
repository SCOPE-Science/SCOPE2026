# A three-point association threshold for exchangeable random partitions

## Finding

Let \(\Pi\) be any exchangeable random partition of a finite set containing three distinct labels \(1,2,3\), and write \(X_{ij}=\mathbf 1\{i,j\text{ are in the same block of }\Pi\}\). Set
\[
p=\Pr(X_{12}=1),\qquad q=\Pr(X_{12}=X_{13}=X_{23}=1).
\]
The three-coordinate vector \((X_{12},X_{13},X_{23})\) is **positively associated** (every pair of coordinatewise increasing real-valued functions has nonnegative covariance) if and only if
\[
\boxed{q(1+p)\ge 2p^2.}
\]
If the condition fails, a negative-covariance witness is the event that the first two labels coalesce versus the event that at least one of the other two pairs coalesces. Their covariance is precisely \(q(1+p)-2p^2\).

For a uniformly random set partition of \([n]\), for every integer \(n\ge3\),
\[
p=\frac{B_{n-1}}{B_n},\qquad q=\frac{B_{n-2}}{B_n},\qquad q>p^2,\qquad q(1+p)<2p^2,
\]
where \(B_n\) is the Bell number. Thus **all distinct pair-coalescence indicators have positive covariance, but their three-coordinate vector is not positively associated**. Among the 36 unordered pairs (including identical pairs) of the eight nontrivial increasing event types on these three indicators, exactly three pairs have negative covariance; every other pair has strictly positive covariance.

Nevertheless, for any finite graph \(G\) on the labels and any two **nonempty** sets \(F,H\) of required edges, the corresponding *principal coalescence events* \(C_F=\{X_e=1\text{ for all }e\in F\}\) and \(C_H\) in the uniform-partition law are strictly positively correlated.

The general criterion also resolves a natural model trichotomy. For an exchangeable Pitman–Yor partition with \(0\le\alpha<1\) and \(\theta>-\alpha\) (and \(\theta>0\) when \(\alpha=0\)),
\[
q(1+p)-2p^2
=\frac{\alpha(1-\alpha)(\theta+\alpha)}{(1+\theta)^2(2+\theta)}.
\]
It is zero for the Ewens boundary \(\alpha=0\) and positive for \(0<\alpha<1\). In contrast, the equivalence relation induced by independent uniform colors from \(m\ge2\) colors has \(q(1+p)-2p^2=-(m-1)/m^3<0\).

## Assumptions and scope

Exchangeability means that the distribution of \(\Pi\) is invariant under permutations of the labeled ground set. The three indicated pairs are unordered edges of the triangle on labels \(1,2,3\). Positive association concerns all bounded increasing functions of the **three observed indicator coordinates**, not every indicator on the complete ground set. Since there are finitely many states, the boundedness requirement is immaterial. No infinite-volume limit is assumed. For the principal-event statement, graph edges are distinct unordered pairs, and the required sets are nonempty. The uniform Bell law is uniform over the \(B_n\) partitions of \([n]\). All assertions hold exactly at finite \(n\), except that the Pitman–Yor construction is a consistent family whose restriction to any \(n\ge3\) has the given three-label law.

## Proof

**1. Complete three-label support.** Transitivity permits only the five indicator configurations \(000\), \(100\), \(010\), \(001\), \(111\). Exchangeability assigns them probabilities \(1-3p+2q\), \(p-q\), \(p-q\), \(p-q\), and \(q\), respectively. Each nontrivial increasing event, up to equivalence on this support, contains \(111\), excludes \(000\), and includes precisely some subset \(S\subseteq\{12,13,23\}\) of the three single-edge configurations. Calling this event \(A_S\),
\[
\Pr(A_S)=q+|S|(p-q),\quad
\Pr(A_S\cap A_T)=q+|S\cap T|(p-q).
\]
When \(S\subseteq T\), the covariance is \(\Pr(A_S)(1-\Pr(A_T))\ge0\). All remaining unordered incomparable pairs fall into three symmetry types:
\[
\begin{array}{c|c}
(|S|,|T|,|S\cap T|)&\operatorname{Cov}(\mathbf1_{A_S},\mathbf1_{A_T})\\\hline
(1,1,0)&q-p^2\\
(1,2,0)&q(1+p)-2p^2\\
(2,2,1)&p-(2p-q)^2.
\end{array}
\]
The middle expression must be nonnegative if association holds. Conversely, suppose it is nonnegative. Since \(0\le p\le1\),
\[
q\ge\frac{2p^2}{1+p}\ge p^2,\qquad
p-(2p-q)^2\ge p-\frac{4p^2}{(1+p)^2}
=\frac{p(1-p)^2}{(1+p)^2}\ge0.
\]
Thus every increasing-event pair is positively correlated; expansion of finite increasing functions as nonnegative linear combinations of increasing-event indicators plus a constant proves association. This establishes the necessary-and-sufficient criterion, including degenerate boundary cases.

**2. Uniform Bell partitions.** Coalescing a specified set of \(r\) labels into one prescribed class reduces the count to \(B_{n-r+1}\). Thus \(p=B_{n-1}/B_n\), \(q=B_{n-2}/B_n\). The Bell-number theorem of Asai–Kubo–Kuo implies
\[
1<\frac{q}{p^2}=\frac{B_nB_{n-2}}{B_{n-1}^2}\le\frac n{n-1}\quad (n\ge3),
\]
where strictness on the left also follows from the nondegenerate Stam mixture described below. Also the same theorem gives \(p\le1/3\) for \(n\ge4\). Consequently
\[
\frac{q(1+p)-2p^2}{p^2}\le\frac43\cdot\frac43-2=-\frac29<0\quad (n\ge4).
\]
For \(n=3\), \((B_1,B_2,B_3)=(1,2,5)\), so the expression equals \(-1/25\).

To classify *all* increasing-event covariances, the first nonnested type \(q-p^2\) is strictly positive by strict Bell log-convexity. The third \(p-(2p-q)^2\) is positive for \(n\ge7\) since \(p\le B_6/B_7=203/877<1/4\) and \(0\le q\le p\) imply it is at least \(p-4p^2>0\). For \(n=3,4,5,6\), direct Bell substitution gives, respectively, \(1/25\), \(11/225\), \(155/2704\), and \(2635/41209\). All nested covariances are strictly positive because every nontrivial event has probability strictly between zero and one. Of the 36 unordered pairs of the eight events \(A_S\), exactly the three disjoint \((1,2)\) pairs are therefore negative.

**3. Principal coalescence.** For \(F\) a graph-edge set, put \(r(F)=n-c(F)\), where \(c(F)\) is the number of connected components of the spanning graph \(([n],F)\). Contracting those components shows \(\Pr(C_F)=B_{n-r(F)}/B_n\). Stam's urn representation chooses \(M\ge1\) with \(\Pr(M=m)=m^n/(e\,m!B_n)\), then colors every vertex independently and uniformly from \(M\) boxes; its induced equivalence relation is uniform over set partitions. Conditional on \(M\), \(\Pr(C_F\mid M)=M^{-r(F)}\), and
\[
\Pr(C_F\cap C_H)=\mathbb E[M^{-r(F\cup H)}]
\ge\mathbb E[M^{-r(F)-r(H)}]
>\mathbb E[M^{-r(F)}]\mathbb E[M^{-r(H)}]
\]
whenever \(F,H\ne\varnothing\). The first inequality uses \(r(F\cup H)\le r(F)+r(H)\); the second is strict Chebyshev covariance for two strictly decreasing functions of the nondegenerate \(M\). This proves the claimed strict positive correlation, irrespective of overlap.

**4. Partition-model trichotomy.** In Pitman's Chinese-restaurant rule, the second tagged individual joins the first with probability \(p=(1-\alpha)/(1+\theta)\). For all three to share a block, the third additionally joins with probability \((2-\alpha)/(2+\theta)\), hence \(q=(1-\alpha)(2-\alpha)/[(1+\theta)(2+\theta)]\). Direct cancellation yields the displayed formula and its sharp signs. Independent coloring from \(m\) equally likely boxes yields \(p=1/m\), \(q=1/m^2\) and the negative formula. The criterion completes the classification.

## Verification

Execute `python3 verify.py` from the package directory (Python standard library only). It computes the Bell numbers by their exact integer recurrence and checks the inequality and all 36 covariance types for every \(3\le n\le128\). It separately enumerates all set partitions for \(3\le n\le6\), performs all edge-requirement comparisons for \(n=3,4\) against exact contraction ranks and complete partition enumeration, and tests the association criterion on an admissible grid of rational three-point exchangeable laws. It also independently verifies the Pitman–Yor algebraic expression at rational parameter values and the fixed-color formula. The run passed **18,650 exact assertions/checks**. The all-size conclusions do not rely on finite enumeration; their proof is above.

## Relationship to prior work

The Bell-number log-convexity and factorial-log-concavity inequalities used in the strict sign proof are from Asai, Kubo and Kuo (2001); the construction of uniform set partitions from a random box count is from Stam (1983). Pitman (2006, §3.2) provides the Pitman–Yor seating rule and exchangeable partition probability formula. These sources supply the ingredients but the three-coordinate association criterion, its universal three-model sign classification and the simultaneous contrast with strict principal-event correlation are separate consequences established here. The literature on higher moments of set-partition statistics, including Chern et al. (2016), concerns additive statistics rather than the full family of three-label increasing events. Classical correlation-inequality theory distinguishes pairwise positive correlation from positive association.

## Limitations

The association criterion is complete for three tagged labels only; it does not assert association or nonassociation of all pair indicators on larger labeled sets. Strict positive correlation of principal coalescence events is weaker than full association and must not be mistaken for an FKG lattice inequality. A prior publication establishing the identical three-label criterion under a different equivalence-relation terminology remains possible; the cited studies were checked for direct implication, not a proof of absolute historical novelty. Exact-rational finite checks corroborate but do not establish the infinite family; the analytic Bell-number bounds and Stam coupling are essential. No independent external mathematical audit has been performed.

## References

1. N. Asai, I. Kubo, H.-H. Kuo, *Bell Numbers, Log-Concavity, and Log-Convexity*, arXiv:math/0104137v1 (first posted 2001-04-12), Theorem 1. https://arxiv.org/abs/math/0104137
2. A. J. Stam, *Generation of a Random Partition of a Finite Set by an Urn Model*, Journal of Combinatorial Theory, Series A **35** (1983), 231–240. https://doi.org/10.1016/0097-3165(83)90009-2
3. J. Pitman, *Combinatorial Stochastic Processes*, Lecture Notes in Mathematics **1875**, Springer (2006), §3.2. https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/pitman_CSP.pdf
4. A. Chern et al., *Central limit theorems for some set partition statistics*, Advances in Applied Mathematics **70** (2015), 92–105. https://doi.org/10.1016/j.aam.2015.06.008
5. N. Gladkov, *A strong FKG inequality for multiple events*, Bulletin of the London Mathematical Society (2024). https://doi.org/10.1112/blms.13101
