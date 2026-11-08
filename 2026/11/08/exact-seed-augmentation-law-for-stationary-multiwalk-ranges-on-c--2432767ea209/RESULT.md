# Exact seed-augmentation law for stationary multiwalk ranges on complete graphs

## Finding

**Theorem (distributional augmentation and allocation invariance).** Let \(n\ge2\) and \(k\ge1\) be integers, \(q\in[0,1]\), and \(t_1,\ldots,t_k\) be arbitrary nonnegative integers with \(T=\sum_{i=1}^k t_i\). On the labeled complete graph \(K_n\), run \(k\) independent discrete-time walks, each started uniformly on its vertices, with transition rule: stay at the current vertex with probability \(q\), otherwise move to a uniformly chosen *different* vertex. Denote the set of all vertices visited by walk \(i\) at times \(0,\ldots,t_i\) by \(\mathcal R_i(t_i)\). Let \(\mathcal R(T)\) be the range of one independent uniform-start walk of length \(T\), and let \(U_1,\ldots,U_{k-1}\) be independent uniform vertices, independent of that walk. Then **the random subsets themselves**, not just their cardinalities, obey
\[
\boxed{\quad\bigcup_{i=1}^k\mathcal R_i(t_i)
\ \overset{d}{=}\ \mathcal R(T)\cup\{U_1,\ldots,U_{k-1}\}.\quad}
\]
In particular, the entire law of the left-hand random set depends on the lifespans only through their sum \(T\). It admits a coupling containing the one-walk range almost surely, thereby giving stochastic domination for every increasing statistic of the visited set, including all thresholds on the number of distinct vertices. The conclusions include non-lazy walks \(q=0\) and *odd* \(T\).

For any fixed set of \(b\) distinct vertices, \(0\le b<n\), put
\[
\alpha_b=1-\frac{(1-q)b}{n-1},\qquad U=n-\left|\bigcup_i\mathcal R_i(t_i)\right|.
\]
Then
\[
\boxed{\quad\mathbb E[(U)_{\underline b}]
=(n)_{\underline b}\left(\frac{n-b}{n}\right)^k\alpha_b^T,\quad}
\]
with the value zero at \(b=n\) when \(k\ge1\). Here \((a)_{\underline b}=a(a-1)\cdots(a-b+1)\), and \((a)_{\underline0}=1\). Thus all factorial moments and the full finite-size distribution are explicit. For each labeled subset \(S\) of size \(r\),
\[
\boxed{\quad\Pr\left\{\bigcup_i\mathcal R_i(t_i)=S\right\}
=\sum_{j=0}^{r-1}(-1)^j\binom rj
\left(\frac{r-j}{n}\right)^k
\left(q+(1-q)\frac{r-j-1}{n-1}\right)^T.\quad}
\]
For \(r=0\), the sum is empty and the probability is zero. Multiplication by \(\binom nr\) yields the probability that the range has size \(r\).

Writing \(a=1-(1-q)/(n-1)\), the expectation difference is exactly
\[
\boxed{\quad
\mathbb E\left|\bigcup_{i=1}^k\mathcal R_i(t_i)\right|
-\mathbb E|\mathcal R(T)|
=(n-1)a^T\left[1-\left(1-\frac1n\right)^{k-1}\right].\quad}
\]
The difference is strictly positive for \(n\ge3\), \(k\ge2\), and every finite \(T\). For \(n=2\), \(q=0\), and \(T\ge1\), both strategies already cover every vertex and equality holds.

## Assumptions and scope

All \(k\) walks have the **same** holding probability \(q\), start independently from the uniform stationary law, and perform exactly the specified numbers of transitions. Each starting vertex counts as visited, even if its lifespan is zero. Walks are independent of each other, and the comparison walk and additional uniform vertices are mutually independent. Equality in distribution is on the finite space of labeled subsets of \(\{1,\ldots,n\}\), not equality of trajectories or joint temporal range processes. The theorem applies to every \(n\ge2\), \(k\ge1\), \(q\in[0,1]\), and all nonnegative integer lifespans, without asymptotic assumptions.

## Proof

Fix a forbidden labeled subset \(B\) with \(|B|=b<n\). One uniform-start walk avoids \(B\) at time zero with probability \((n-b)/n\). When its current position lies outside \(B\), its next position also lies outside \(B\) with the state-independent probability
\[
q+(1-q)\frac{n-b-1}{n-1}
=1-\frac{(1-q)b}{n-1}=\alpha_b.
\]
Consequently its entire range avoids \(B\) through time \(t\) with probability \(((n-b)/n)\alpha_b^t\). The independence of the \(k\) walks implies
\[
\Pr\left\{B\cap\bigcup_i\mathcal R_i(t_i)=\varnothing\right\}
=\left(\frac{n-b}{n}\right)^k\alpha_b^T.\tag{1}
\]
For the proposed comparison set \(\mathcal R(T)\cup\{U_1,\ldots,U_{k-1}\}\), the one-walk avoidance probability is \(((n-b)/n)\alpha_b^T\), while the independent uniform extra points avoid \(B\) with joint probability \(((n-b)/n)^{k-1}\). Hence its avoidance probability is exactly the right side of (1). When \(B\) is the entire vertex set both avoidance probabilities are zero. Thus the two random subsets have identical avoidance probabilities for *every* labeled subset \(B\).

These probabilities uniquely determine a probability distribution on subsets: for any candidate range \(S\), use the event that the range is contained in a given \(A\subseteq S\), then Möbius inversion on the Boolean lattice gives
\[
\Pr\{\text{range}=S\}
=\sum_{A\subseteq S}(-1)^{|S\setminus A|}\Pr\{\text{range}\subseteq A\}.
\]
The probability of containment in \(A\) is the avoidance probability for \(B=V\setminus A\), which equals
\[
\left(\frac{|A|}{n}\right)^k
\left(q+(1-q)\frac{|A|-1}{n-1}\right)^T
\]
for nonempty \(A\), and equals zero for \(A=\varnothing\). Grouping by \(|A|\) proves the displayed exact subset formula and the asserted equality in law. This also proves allocation invariance, since (1) uses the lifespans solely through \(T\).

To obtain the factorial moments, expand \((U)_{\underline b}\) as the sum over all ordered \(b\)-tuples of distinct vertices of the indicator that all \(b\) remain unvisited. There are \((n)_{\underline b}\) such tuples, and (1) supplies each expectation, proving the moment formula (with \(b=n\) treated separately). Taking \(b=1\) gives
\[
\mathbb E\left|\bigcup_i\mathcal R_i(t_i)\right|
=n\left[1-\left(\frac{n-1}{n}\right)^k a^T\right].
\]
Subtract the same expression with \(k=1\) to obtain the exact expectation gap and its stated strictness.

Finally, construct \(\mathcal R(T)\) and independent \(U_1,\ldots,U_{k-1}\) on one probability space. The union contains \(\mathcal R(T)\) almost surely, and the union's law is that of the multiwalk set. This gives a genuine set-inclusion coupling and hence the stochastic inequalities; no trajectory-level assertion is needed. All conclusions follow.

## Verification

The standalone file `check.py` performs exact-rational finite-state checks, using independent dynamic programming over pairs of visited-subset masks and current vertices for each individual walk. It convolves the exact distributions of all weak lifespan compositions, compares each labeled-subset probability with the augmentation construction and with the inclusion-exclusion formula, and tests all uncovered factorial moments. It passes 5,560 exact comparisons over \(n\in\{2,3,4,5\}\), \(q\in\{0,1/3,1/2,1\}\), \(k\in\{1,2,3\}\), and \(T\in\{0,1,2,3,4\}\). These finite checks are supplementary; the proof above works for the full stated domain.

The complete-graph hypothesis matters. For a stationary simple random walk on the three-vertex path, two independent walkers with lifespans \((1,3)\) cover all three vertices with probability \(3/4\), while lifespans \((2,2)\) cover all three with probability \(23/32\). Thus allocation invariance already fails on this natural noncomplete graph, even with the same number of walkers and total number of steps. This boundary example is an exact finite-state computation, not a claimed characterization of all graphs.

## Relationship to prior work

Dey, Kim and Terlov (first preprint, February 28, 2023, arXiv:2302.14241) prove an inequality **only for the expected size** of collaborative ranges (Theorem 1.1). Their Question 3.2 asks for quantitative collaboration gaps and Question 3.6 asks for full stochastic domination. The result here supplies a complete-graph answer that is stronger than both: an equality of random *sets*, with exact distributions and gap. It does **not** resolve either question on general reversible chains. Their additional odd-total-time Conjecture 3.1 is likewise verified here only in this complete-graph family.

Rivera, Sauerwald and Sylvester (arXiv:2011.07893, initially posted November 16, 2020) establish bounds for parallel-walk cover times and stationary starts on broad graph classes, but do not state this finite-time random-set identity. Upadhyay, Sandev, Kumar and Singh (arXiv:2604.20829, April 22, 2026) give the single-walk complete-network distinct-range distribution and continuous-time variants; this is prior baseline work, not the multiple-walk set-law equivalence or allocation invariance proved here. Classical coupon-collector and finite-set inclusion-exclusion techniques underpin the derivation and are not themselves claimed new.

## Limitations

The identity depends critically on uniform stationary starts, identical complete-graph transition rules, independent walkers, and fixed discrete transition counts. It need not hold on noncomplete graphs (as the path example demonstrates), for heterogeneous start laws, or when the holding probabilities differ across walks. It compares final random visited sets, not their entire temporal evolution; it is not a general-graph stochastic domination theorem. The relative novelty of the specific exact augmentation identity remains subject to independent literature and mathematical review.

## References

1. P. S. Dey, D. Kim, and G. Terlov, *Collaboration of Random Walks on Graphs*, arXiv:2302.14241 (first public version February 28, 2023), Theorem 1.1 and Questions 3.2, 3.6, Conjecture 3.1. https://arxiv.org/html/2302.14241v1
2. N. Rivera, T. Sauerwald, and J. Sylvester, *Multiple Random Walks on Graphs: Mixing Few to Cover Many*, arXiv:2011.07893 (first public version November 16, 2020), especially Sections 1, 3. https://arxiv.org/html/2011.07893v3
3. S. K. Upadhyay, T. Sandev, S. Kumar, and R. K. Singh, *Network exploration by random walks: A large deviation perspective*, arXiv:2604.20829 (first public version April 22, 2026), Section 2. https://arxiv.org/html/2604.20829v2
