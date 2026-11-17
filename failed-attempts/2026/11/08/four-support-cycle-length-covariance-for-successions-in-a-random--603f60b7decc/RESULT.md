# Four-support cycle-length covariance for successions in a random permutation

## Finding

Let \(n\ge4\) and let \(\Pi\) be a uniform permutation of \(\{1,\dots,n\}\). Define its **increasing-succession indicators** and count by
\[
B_i=\mathbf1\{\Pi(i+1)=\Pi(i)+1\}\quad(1\le i<n),
\qquad S=\sum_{i=1}^{n-1}B_i.
\]
For \(1\le j\le n\), let \(C_j\) count the cycles of length \(j\) in the **same permutation** \(\Pi\), and set \(H(t)=\sum_{j=1}^n C_jt^j\). Write \(c_i=1\) if \(i=1\) or \(i=n-1\), and \(c_i=2\) otherwise.

The complete position-by-cycle-length cross-covariance is
\[
\boxed{
\operatorname{Cov}(B_i,H(t))=
\frac{c_it}{n(n-1)(n-2)}
+\frac{(1-c_i)t^2}{n(n-1)(n-3)}
-\frac{(n-2-c_i)t^{n-1}}{n(n-1)(n-2)(n-3)}
+\frac{t^n}{n^2(n-1)}.}
\]
Summing over positions gives the **four-support law**
\[
\boxed{
\operatorname{Cov}(S,H(t))
=\frac{2t-t^2-t^{n-1}}{n(n-1)}+\frac{t^n}{n^2}.}
\]
Thus the nonzero covariances are \(2/[n(n-1)]\) at cycle length \(1\), \(-1/[n(n-1)]\) at lengths \(2\) and \(n-1\), and \(1/n^2\) at length \(n\). All interior lengths \(3\le j\le n-2\) have exactly zero covariance with \(S\). In particular, the covariance of \(S\) with the total cycle count is \(1/n^2\). Zero covariance does not assert stochastic independence.

## Assumptions and scope

The permutation is uniformly distributed on the full symmetric group on \(n\ge4\) labels. Succession means consecutive **positions** holding consecutive increasing **values**, without cyclic wrap-around. The cycle counts refer to the usual functional digraph of this very same one-line permutation; they are not cycle counts of a Foata-transformed permutation. All covariance identities are exact for every allowed \(n,i,j\); no asymptotic hypothesis is required. When \(n=4\), the interval \(3\le j\le n-2\) is empty.

## Proof

Fix \(i\), write \(m=n-2\), and consider the event
\(E_{i,a}=\{\Pi(i)=a,\Pi(i+1)=a+1\}\) for \(1\le a<n\). Each such event has probability \(1/[n(n-1)]\), and the events partition \(\{B_i=1\}\). The two forced arrows in the permutation functional digraph fall into exactly three cases:

- If \(a=i\), the forced arrows are two fixed-point cycles. Removing them leaves an independent uniform permutation on \(m\) vertices.
- If \(a=i-1\) or \(a=i+1\), when available, the arrows form one directed path of two edges. Contracting that path produces one marked vertex in a uniform permutation on \(m\) vertices. A cycle through this mark gains two vertices on expansion.
- For all other \(a\), the arrows are two vertex-disjoint directed paths of one edge each. Contracting both paths produces two distinct marks in a uniform permutation on \(m\) vertices. Each mark contributes one extra vertex to its cycle on expansion.

Each contraction is a bijection between admissible completions of the forced arrows and permutations of the \(m\) contracted vertices: the free outgoing half-edges and free incoming half-edges match exactly once. Uniformity is therefore preserved. The three cases occur for, respectively, \(1\), \(c_i\), and \(m-c_i\) values of \(a\).

Define the deterministic polynomials
\[
L_m(t)=\sum_{h=1}^m\frac{t^h}{h},\qquad
T_m(t)=\sum_{h=1}^m t^h,\qquad
U_m(t)=\sum_{h=2}^m(h-1)t^h.
\]
For a uniform permutation on \(m\) vertices, the expected number of cycles of length \(h\) equals \(1/h\); the expected number of such cycles containing one specified mark equals \(1/m\); and the expected number containing two specified distinct marks equals \((h-1)/[m(m-1)]\). These follow by counting ordered cycle supports, or by observing that a marked vertex lies in an \(h\)-cycle with probability \(1/m\), and a second mark lies in that cycle conditionally with probability \((h-1)/(m-1)\).

Consequently the conditional expectations of \(H(t)\) in the fixed-cycle, single-path, and two-path cases are, respectively,
\[
F(t)=L_m(t)+2t,
\]
\[
P(t)=L_m(t)+\frac{t^2-1}{m}T_m(t),
\]
\[
Q(t)=L_m(t)+\frac{2(t-1)}mT_m(t)
+\frac{(t-1)^2}{m(m-1)}U_m(t).
\]
For \(m\ge2\), elementary cancellation gives the sparse expressions
\[
P(t)=L_m(t)-\frac{t+t^2}{m}+\frac{t^{m+1}+t^{m+2}}m,
\]
\[
Q(t)=L_m(t)-\frac{2t}m+\frac{t^2}{m(m-1)}
+\frac{(m-2)t^{m+1}}{m(m-1)}+\frac{t^{m+2}}m.
\]
It follows exactly that
\[
\mathbb E[B_iH(t)]
=\frac{F(t)+c_iP(t)+(m-c_i)Q(t)}{n(n-1)}.
\]
Since \(\mathbb E B_i=1/n\) and \(\mathbb E H(t)=L_n(t)\), subtracting \(L_n(t)/n\) and collecting the coefficients of \(t,t^2,t^{m+1},t^{m+2}\) yields the displayed positionwise identity. All other coefficients cancel identically. Finally \(\sum_{i=1}^{n-1}c_i=2(n-2)\) and \(\sum_{i=1}^{n-1}(n-2-c_i)=(n-2)(n-3)\); summing the positionwise identity yields the four-support law. Setting \(t=1\) gives the total-cycle covariance \(1/n^2\). This proves every assertion.

## Verification

The included independent arithmetic implementation, `verify.py`, enumerates every permutation of orders \(4\) through \(9\), computes all \((n-1)n\) local covariances with exact rational arithmetic, and compares them with the theorem. Separately it computes conditioned cycle moments from the three contraction cases and checks the simplified coefficients for orders \(4\) through \(19\). A run of `python3 verify.py` completed with `PASS: 2688 exact rational comparisons; all permutations of sizes 4 through 9 enumerated`. The all-\(n\) proof is the contraction and coefficient calculation above, not finite enumeration.

## Relationship to prior work

The random set of succession positions was proved equidistributed with fixed points outside the last position by Diaconis, Evans, and Graham. That marginal equidistribution does **not** preserve the original permutation's cycle structure, which is the essential joint statistic here. An earlier complete covariance calculation between individual fixed-point and succession indicators already implies the entire \(j=1\) positionwise coefficient and its aggregate \(2/[n(n-1)]\). These are acknowledged as prior, not new results. The new content is the complete cycle-length cross-covariance, including the zero interior, the opposite \(j=2,n-1\) coefficients, and the positive \(j=n\) coefficient, together with their positionwise boundary law.

Mansour and Shattuck count cycle successions jointly with the total number of cycles, using cycle-notation successions. Their paper explicitly distinguishes the joint laws of these transformed statistics from those of ordinary one-line successions with other permutation statistics. A total-cycle count also does not determine the cycle-length-resolved covariance. Reilly and Tanny's earlier succession-enumeration work concerns counts of successions and rises/runs; the accessible accounts do not report the present cross-covariance. Related work on refinements of the Diaconis–Evans–Graham bijection tracks other local statistics but has not been shown to imply this law.

## Limitations

These formulas are covariances, not joint-distribution or independence theorems; a vanishing coefficient for an intermediate cycle length does not imply independence. No nonuniform permutation law is considered. The positionwise identity is stated only for \(n\ge4\) to keep its four degree positions distinct and denominators nonzero. Historical priority remains contingent on additional older enumerative literature, especially general cycle-index refinements that might imply the identity without stating it. The proof and exact checker do not constitute independent validation.

## References

1. P. Diaconis, S. N. Evans, R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Technical Report 822 (August 1, 2013); subsequently *Advances in Applied Mathematics* 61 (2014), 102–124. https://statistics.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf ; https://statistics.berkeley.edu/tech-reports/822
2. T. Mansour, M. Shattuck, *Counting permutations by the number of successions within cycles*, *Discrete Mathematics* 339 (2016), 1368–1376. https://doi.org/10.1016/j.disc.2015.12.004 ; author-uploaded text https://www.researchgate.net/publication/301752905_Counting_permutations_by_the_number_of_successions_within_cycles
3. J. W. Reilly, S. M. Tanny, *Counting permutations by successions and other figures*, *Discrete Mathematics* 32 (1980), 69–76. https://doi.org/10.1016/0012-365X(80)90101-6
4. L. R. Du, K. Q. Ji, *A refinement of the Diaconis-Evans-Graham theorem*, first preprint March 2024, published in *Frontiers in Combinatorics and Number Theory* 2 (2026), 75–79. https://arxiv.org/abs/2404.00607
