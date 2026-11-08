# Second-order rare-obstruction law for kings in random tournaments

## Finding

In a uniformly random tournament with \(n\) labeled vertices, let \(W_n\) count ordered pairs \((a,b)\), \(a\ne b\), for which there is no path from \(b\) to \(a\) using at most two directed edges. A vertex is a *king* if it reaches every other vertex within two edges; hence every vertex is a king exactly when \(W_n=0\). Define
\[
A_n=\frac{n(n-1)}2\left(\frac34\right)^{n-2},\qquad
B_n=\frac{n(n-1)(n-2)}4\left(\frac58\right)^{n-3}.
\]
Then, for \(n\to\infty\),
\[
\Pr(W_n\ge1)=A_n-B_n+O\!\left(n^6(9/16)^{n-6}\right),
\qquad \Pr(W_n\ge2)\sim B_n.
\]
In particular \((A_n-\Pr(W_n\ge1))/B_n\to1\). Conditional on at least two failed ordered reachabilities, with probability tending to one there are exactly two, and they share their first coordinate or share their second coordinate, with asymptotic probability \(1/2\) each.

The leading term \(A_n\), obtained by summing individual ordered-pair failure probabilities, is classical; the contribution claimed here is the second exponential correction and its obstruction-cluster interpretation.

## Assumptions and scope

The underlying labeled tournament is a complete graph on \(\{1,\ldots,n\}\), independently orienting each edge with probability \(1/2\) in either direction. The probability is *annealed* over the orientations. For distinct \(a,b\), let \(E_{a,b}\) be the event that \(b\) cannot reach \(a\) by a directed path of length one or two. The indices are ordered: the first is the unreachable target, and the second the failing source. There are \(N=n(n-1)\) possible events. Throughout the asymptotic statements \(n\) is an integer tending to infinity; the explicit remainder bound below holds for \(n\ge6\).

## Proof

**One obstruction.** The event \(E_{a,b}\) forces \(a\to b\). For each other vertex \(z\), it forbids the path \(b\to z\to a\). The required orientation constraint has probability \(3/4\), independently over such \(z\); therefore
\[
\Pr(E_{a,b})=\frac12(3/4)^{n-2},\qquad
S_1:=\sum_{a\ne b}\Pr(E_{a,b})=A_n.
\]

**Two obstructions.** If \(E_{a,b}\) and \(E_{a,c}\) share their first coordinate, the two forced edges \(a\to b,a\to c\) cost \(1/4\). For an external vertex \(z\), write \(X_v=\mathbf1\{v\to z\}\). The two restrictions are \(X_b\le X_a\) and \(X_c\le X_a\), satisfied by five of the eight assignments; the internal edge between \(b\) and \(c\) is unrestricted. Thus
\[
\Pr(E_{a,b}\cap E_{a,c})=\tfrac14(5/8)^{n-3}.
\]
Reversing all edges gives the same probability when the two obstructions share their second coordinate, as in \(E_{a,b}\cap E_{c,b}\). These are \(2n\binom{n-1}{2}\) *unordered* pairs of events, contributing exactly \(B_n\) to the second Bonferroni sum \(S_2\).

Events \(E_{a,b}\) and \(E_{b,a}\) cannot coexist. If two events form a chain \(E_{a,b},E_{b,c}\) on three distinct vertices, the three internal edges are forced into a transitive orientation and each external vertex must satisfy two nested implications (probability \(1/2\)). Their intersection probability is \(\frac18(1/2)^{n-3}\). There are \(n(n-1)(n-2)\) such unordered event pairs. Finally, for disjoint endpoints, the two constraints on any external vertex are independent and each has probability \(3/4\), so their intersection probability is at most \((9/16)^{n-4}\). It follows that
\[
0\le S_2-B_n\le \frac{n(n-1)(n-2)}8(1/2)^{n-3}
 +\binom N2(9/16)^{n-4}. \tag{1}
\]

**Three obstructions.** Fix any three distinct ordered-pair events and let \(U\) be their at most six endpoints. For every vertex \(z\notin U\), its independent fair orientations toward \(U\) must satisfy three implications \(X_{b_i}\le X_{a_i}\). For any three distinct directed constraints on independent fair Boolean variables, the probability of meeting all three is at most \(9/16\). To verify this finite lemma, view constraints as three directed edges. If a reciprocal pair occurs, satisfying both enforces equality and the third constraint cannot increase probability; if all three edges are distinct as undirected edges, the possibilities are a directed-orientation triangle, a three-edge star, a three-edge path, a two-edge component plus a disjoint edge, or three disjoint edges. The respective upper bounds are \(1/2,9/16,1/2,15/32,27/64\). The star of three implications pointing in one direction attains \(9/16\). This exhausts the underlying simple three-edge graph types. Conditioning on edges within \(U\), the other vertices contribute independent factors, yielding
\[
S_3:=\sum_{|J|=3}\Pr\Big(\bigcap_{E\in J}E\Big)
\le \binom N3(9/16)^{n-6}\qquad(n\ge6). \tag{2}
\]

**Bonferroni and clustering.** The two Bonferroni inequalities give
\(S_1-S_2\le\Pr(W_n\ge1)\le S_1-S_2+S_3\). Using (1)–(2),
\[
\left|\Pr(W_n\ge1)-(A_n-B_n)\right|\le
\frac{n(n-1)(n-2)}8(1/2)^{n-3}
+\binom N2(9/16)^{n-4}
+\binom N3(9/16)^{n-6},
\]
which proves the stated error and \((A_n-\Pr(W_n\ge1))/B_n\to1\), since \((9/16)/(5/8)=9/10\). Also \(S_2-2S_3\le \Pr(W_n\ge2)\le S_2\), because for integers \(w\ge2\), \(\binom w2-\mathbf1\{w\ge2\}\le2\binom w3\); therefore \(\Pr(W_n\ge2)\sim B_n\). Finally, \(\Pr(W_n\ge3)\le S_3=o(B_n)\). By (1), the total pair mass from configurations not sharing a first or second coordinate is \(o(B_n)\), and the two sharing types contribute exactly \(B_n/2\) each. These facts establish the conditional two-obstruction structure and its symmetric half-half split.

## Verification

Run `python3 verify.py` from the same directory. The standalone standard-library program exactly enumerates all labeled tournaments of orders two through six, tests each ordered-pair event, checks the one-event and shared-coordinate two-event formulas, and verifies Bonferroni inequalities. It also checks the three-implication Boolean bound for all triples of distinct directed implications on at most six variables. The packaged version passed 5,740 exact rational/exhaustive assertions. These finite tests do not replace the all-order proof.

## Relationship to prior work

Maurer's *The King Chicken Theorems* (1980) established that all vertices of a large uniformly random tournament are kings with high probability; the first-moment scale for an individual failed two-step reachability follows from the elementary obstruction probability and is not asserted to be new. Manurangsi and Suksompong (2022), including their Section 5.1, examine random-tournament king prevalence and give a product formula for one ordered pair, but do not state the second exponential overlap correction or the two-obstruction clustering limit in the inspected accessible article. Linusson and Leander (2013) study correlations of unrestricted directed reachability, rather than the bounded-two-step obstruction. Published mathematical research-record comparisons did not identify this precise second-order statement. This comparison is not a proof of global novelty.

## Limitations

The expansion applies to fair independent edge orientations with \(n\to\infty\); it does not assert an approximation uniform over arbitrary biased tournament laws or accurate numerical truncations for small \(n\). The error is an explicit exponential envelope, not a complete third-order coefficient. Maurer's original full text could not be obtained from the accessible open sources or authorized institutional route; that inaccessible historical article, and any prior unindexed higher-order inclusion-exclusion analysis, remain originality risks. No independent scientific audit has been performed.

## References

1. Stephen B. Maurer, *The King Chicken Theorems*, Mathematics Magazine 53 (1980). Public bibliographic record: https://works.swarthmore.edu/fac-math-stat/146/ .
2. Svante Linusson and Madeleine Leander, *Correlation of paths between distinct vertices in a randomly oriented graph* (first posted March 16, 2013), arXiv:1303.3961, https://arxiv.org/abs/1303.3961 .
3. Pasin Manurangsi and Warut Suksompong, *Generalized kings and single-elimination winners in random tournaments*, Autonomous Agents and Multi-Agent Systems 36 (2022), https://doi.org/10.1007/s10458-022-09557-7 .
4. Arindam Biswas, Varunkumar Jayapaul, Venkatesh Raman and Srinivasa Rao Satti, *Finding kings in tournaments*, Discrete Applied Mathematics 322 (2022), https://doi.org/10.1016/j.dam.2022.08.014 .
