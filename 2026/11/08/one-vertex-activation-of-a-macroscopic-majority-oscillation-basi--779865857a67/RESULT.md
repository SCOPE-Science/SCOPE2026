# One-vertex activation of a macroscopic majority-oscillation basin

## Finding

Let \(G_n=K_{n,n,n+1}\) be the labelled complete tripartite graph with independent parts of sizes \(n,n,n+1\), for any integer \(n\ge1\). Update all binary vertex opinions synchronously by strict majority among open neighbors, retaining the previous opinion on an exact tie. Every initial configuration reaches either one of the two unanimous fixed points or a primitive two-cycle in at most **two updates**. There are no other fixed points or eventual cycle types. The two-update bound is sharp for every \(n\ge2\).

For integers \(0\le a,b\le n\), put
\[
S_n(a,b)=
\begin{cases}
2\displaystyle\sum_{c=n+1-\min(a,b)}^{n+1}\binom{n+1}{c},&a+b<n,\\
\displaystyle\sum_{c=\min(a,b)+1}^{\max(a,b)}\binom{n+1}{c},&a+b=n,\\
0,&a+b>n.
\end{cases}
\]
Empty sums are zero. The exact number of labelled configurations attracted to primitive two-cycles is
\[
\boxed{B_n=\sum_{a=0}^{n}\sum_{b=0}^{n}\binom na\binom nb\,S_n(a,b).}
\]
The remaining \(2^{3n+1}-B_n\) configurations enter the two unanimous fixed points, in equal populations. Among all initial configurations, precisely \(2^{n+2}-2\) are **already** on primitive two-cycles (a periodic-state count independently obtainable from the known unequal-tripartite orbit classification). In particular, an exponentially small periodic set attracts a positive proportion of all initial states:
\[
\boxed{\lim_{n\to\infty}\frac{B_n}{2^{3n+1}}=\frac16,\qquad
\frac{2^{n+2}-2}{2^{3n+1}}\longrightarrow0.}
\]

The contrast is discontinuous at one added vertex: on the balanced graph \(K_{n,n,n}\), the probability of eventual primitive period two under the same independent unbiased initial opinions tends to zero, and indeed is at most \(3\binom{2n}{n}/4^n\). Thus adding one vertex to one of three equal independent parts changes the limiting oscillation-basin probability from zero to \(1/6\).

More generally, for any integer sequence \(m_n>n\) with \(m_n/n\to\lambda\in[1,\infty)\), let \(P_{n,m_n}\) be the probability of eventual primitive period two for unbiased initial opinions on \(K_{n,n,m_n}\). Then
\[
\boxed{\lim_{n\to\infty}P_{n,m_n}=\Phi(\lambda)
=\frac14+\frac{1}{2\pi}\left[
\arcsin\!\left(\frac{\lambda}{1+\lambda}\right)
-2\arcsin\!\left(\frac{1}{\sqrt{2(1+\lambda)}}\right)
\right].}
\]
The function is strictly increasing, \(\Phi(1)=1/6\), and \(\Phi(2)\approx0.232279527199\). If instead \(m_n/n\to\infty\), the corresponding limit is \(1/2\). The condition \(m_n>n\) is essential: at exact equality \(m_n=n\), the limit is zero rather than \(\Phi(1)\).

## Assumptions and scope

The graph is finite, simple, undirected, loop-free, and completely joined between its three labelled independent parts. The first two parts each have size \(n\); the third has size \(m\). Opinions are bits \(0\) and \(1\). Every vertex updates simultaneously, using its **open** neighbor set, with its current bit retained at a tie. For the probability statements, all initial vertex bits are independent and fair; dynamics itself is deterministic. A configuration belongs to the primitive-two basin when the eventual orbit has least period exactly two, even when the configuration is not itself periodic. An update time of zero denotes the initial configuration.

Let \(a,b,c\) denote the initial numbers of ones in the three parts. For \(G_n\) we write \(m=n+1\). The first two parts are always uniform after one update because their degrees are the odd number \(2n+1\). The third part has degree \(2n\), and retains its initial bit pattern exactly when \(a+b=n\).

## Proof

**1. The part-count update.** For arbitrary \(m\), the number of neighboring ones seen by a vertex in the first, second, and third parts is respectively \(b+c\), \(a+c\), and \(a+b\); its degree is respectively \(n+m\), \(n+m\), and \(2n\). Thus the next part count equals its part size when twice the neighboring-one count exceeds the degree, equals zero when it is smaller, and retains the old count on a tie. In particular, for \(m=n+1\) the first two part counts after one update are in \(\{0,n\}\), without exception.

**2. The case \(a+b\ne n\).** Then the third part also becomes uniform after the first update. Label the uniform states of the three parts by bits \((u,v,w)\). Since \(m>n\), the eight uniform triples obey
\[
000\mapsto000,\quad111\mapsto111,\quad001\leftrightarrow110,
\]
\[
100\mapsto000,\quad010\mapsto000,\quad011\mapsto111,\quad101\mapsto111.
\]
Consequently the first-updated state enters a primitive two-cycle precisely when it is \(001\) or \(110\); every other state is unanimous after one further update. Because the first two update bits are one precisely when \(b+c\ge n+1\) and \(a+c\ge n+1\), this primitive-two event is exactly
\[
(a+b<n\ \text{and}\ c>n-\min(a,b))
\quad\text{or}\quad
(a+b>n\ \text{and}\ c\le n-\max(a,b)).
\]

**3. The case \(a+b=n\).** The third part keeps its individual initial colors after one update, while the first and second parts become uniform with respective bits
\[
u={\bf1}_{\{c>a\}},\qquad v={\bf1}_{\{c>b\}}.
\]
If \(u=v=0\), the second update makes the entire graph zero. If \(u=v=1\), the second update makes it entirely one. If \(u\ne v\), then \(\min(a,b)<c\le\max(a,b)\); necessarily \(1\le c\le n\). In that case the third part sees a tie forever and preserves its exact initial pattern, while the other two uniform parts swap opposite opinions on every update. Hence the state after the first update is already on a primitive two-cycle. These cases exhaust all initial configurations, prove the two-update bound, and show that only unanimous states are fixed. For \(n\ge2\), the counts \((a,b,c)=(1,n-1,1)\) witness an entry first at update two.

**4. Exact basin count and periodic core.** For given initial part counts \((a,b,c)\), there are exactly \(\binom na\binom nb\binom{n+1}{c}\) labelled colorings. The three disjoint primitive-two conditions from steps 2–3 yield a triple binomial sum. Complementing all opinions maps the \(a+b>n\) contribution bijectively to the \(a+b<n\) contribution, producing the stated double sum \(B_n\). Opinion complementation also gives equal populations for the two consensus basins.

To count **initially periodic** states, observe that the first two parts must be uniform on any periodic orbit. Besides the pair \(001\leftrightarrow110\), the only primitive-two states have opposite uniform first and second parts and a stationary third-part coloring containing between one and \(n\) ones. Thus their total number is
\[
2+2\sum_{c=1}^{n}\binom{n+1}{c}=2^{n+2}-2.
\]
This periodic-core count agrees with the previously derived general unequal-tripartite primitive-orbit classification; the new result concerns its full attraction basin and the singular large-size law.

**5. Singular asymptotic limit.** Let the initial part counts on \(K_{n,n,m_n}\) be independent \(a,b\sim\operatorname{Bin}(n,1/2)\), \(c\sim\operatorname{Bin}(m_n,1/2)\). Outside the union of the three neighbor-tie events, the first update makes every part uniform. For \(m_n>n\), the uniform transition table from step 2 applies, so the eventual orbit has primitive period two exactly when the signs of
\[
U=b+c-(n+m_n)/2,\quad V=a+c-(n+m_n)/2,\quad W=a+b-n
\]
are \((+,+,-)\) or \((-,-,+)\). Each tie event has probability at most the central binomial mass of a fair sum of at least \(2n\) bits. Their union therefore has probability \(O(n^{-1/2})\); no assumption about the behavior on that exceptional set is needed for the limit.

When \(m_n/n\to\lambda<\infty\), the joint central limit theorem implies that the standardized deviations \((2a-n,2b-n,2c-m_n)/\sqrt n\) converge to independent normals \((X,Y,Z)\) with variances \((1,1,\lambda)\). The limiting sign event concerns \((Y+Z,X+Z,X+Y)\), whose pairwise correlations are
\[
\rho_{12}=\frac{\lambda}{1+\lambda},\qquad
\rho_{13}=\rho_{23}=\frac{1}{\sqrt{2(1+\lambda)}}.
\]
For a centered Gaussian pair of correlation \(\rho\), the elementary angular argument gives \(\mathbb E[\operatorname{sgn}(X)\operatorname{sgn}(Y)]=(2/\pi)\arcsin\rho\). Expanding the indicator of the sign pattern \((+,+,-)\), and using symmetry to cancel odd sign moments, gives the displayed \(\Phi(\lambda)\). Substituting \(\lambda=1\) gives \(1/6\). Both arcsine contributions vary in the directions required for strict monotonic increase.

When \(m_n/n\to\infty\), the standardized third-part deviation dominates the first two with probability tending to one. The first two sign expressions therefore agree with the sign of that deviation, whereas \(a+b-n\) is asymptotically equally likely to have either sign, independently. The mixed-sign event has limiting probability \(1/2\).

For the balanced graphs \(K_{n,n,n}\), on the complement of the three tie events the first update makes all parts uniform, and every uniform triple reaches consensus within one more update; this follows by checking the eight uniform triples with equal part sizes. Hence the chance of eventual primitive period two is bounded above by the union probability of three ties,
\[
3\Pr\{\operatorname{Bin}(2n,1/2)=n\}=3\binom{2n}{n}/4^n=O(n^{-1/2}).
\]
This proves the one-vertex jump without importing any other basin classification.

## Verification

Three Python 3 programs, all using only the standard library, reproduce independent checks. Run `python verify_vertex.py`, `python verify_counts.py`, and `python verify_ratio.py` from the directory containing the package files.

`verify_vertex.py` constructs the adjacency lists explicitly and updates vertex bits, independently of part-count expressions. It enumerates all \(74,896\) labelled initial states across \(1\le n\le5\), verifies periodicity by time two, both unanimous fixed points, the primitive-two periodic-core population, and the binomial basin formula. `verify_counts.py` instead uses the three-coordinate part map and an independently implemented binomial-tail sum. It checks all \(n=1,\ldots,20\), then evaluates the exact formula at \(n=30,50,100,200\).

The exact basin counts for \(n=1,2,3,4,5,6\) are, respectively, \(6,22,252,1526,14296,98092\), out of \(2^{3n+1}\) total configurations. `verify_ratio.py` independently checks the count-state dynamics on \(K_{n,n,2n}\) at \(n=2,4,8,16,32\) and compares its finite oscillation probabilities with the proven \(\Phi(2)\) limit; finite tie effects explain the slow convergence. At \(n=200\), the exact one-vertex basin fraction is approximately \(0.170668229711\), compared with the proven limit \(1/6\). These finite computations corroborate, but are not used to prove, the all-size classification or Gaussian limit.

## Relationship to prior work

Goles and Olivos established the general finite symmetric-threshold period-at-most-two theorem in 1980. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, made public May 11, 2014) explicitly formulate synchronous majority with retention on ties, credit that periodicity theorem, and study random and infinite graph families. Tamuz and Tessler (arXiv:1307.4035) study information retention and general combinatorial bounds on majority dynamics. Those results neither enumerate the present attraction basin nor establish its one-vertex discontinuity or Gaussian interpolation curve.

An earlier exact unequal-tripartite calculation gives the number of states already on primitive two-cycles, and a separate balanced-tripartite calculation addresses \(K_{n,n,n}\). The periodic-orbit count and balanced limit are not presented here as original. Neither earlier statement gives the full basin formula for \(K_{n,n,n+1}\), its positive one-vertex limiting mass, or \(\Phi(\lambda)\). The key new distinction is the large basin of an exponentially sparse periodic core, even under a vanishing relative size imbalance.

## Limitations

The initial opinions are independent, unbiased bits; the limiting law need not hold for fixed nonzero bias or for randomized tie breaking. The general \(m_n>n\) result determines the limiting primitive-two probability, not an exact finite-size census for every \(m_n\); the exact census is claimed only when \(m_n=n+1\). The all-size statements rest on the written proof and not on exhaustive finite simulations. Historical novelty is supported by the stated comparisons, but cannot be made absolute from indexed literature alone.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486v1 (first public version May 11, 2014), https://arxiv.org/abs/1405.2486.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI:10.1016/0012-365X(80)90121-1.
3. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035, https://arxiv.org/abs/1307.4035.
