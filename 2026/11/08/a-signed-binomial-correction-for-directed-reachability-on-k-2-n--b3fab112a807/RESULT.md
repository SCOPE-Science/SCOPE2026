# A signed binomial correction for directed reachability on \(K_{2,n}\)

## Finding

Fix an integer \(n\ge1\) and a real bias \(0<p<1\). Independently orient each edge of the complete bipartite graph \(K_{2,n}\) from its two-vertex part toward its \(n\)-vertex part with probability \(p\), and in the reverse direction with probability \(1-p\). Write \(s,t\) for the two vertices of the small part, and start directed reachability from \(s\). Let \(X_n\) be the number of the \(n\) other-part vertices reachable from \(s\), and let \(J_n\) be the indicator that \(t\) is reachable.

Put \(a=p(1-p)\), \(q=1-a\), and \(c=p(2-p)\). The **complete joint probability generating function** is

\[
\mathbb E[z^{X_n}w^{J_n}]
=(1-p+p^2z)^n
+w\left[\big((1-p)^2+cz\big)^n-\big((1-p)^2+pz\big)^n\right]. \tag{1}
\]

In particular, for \(Y_n\sim\operatorname{Bin}(n,c)\),

\[
\Pr(X_n=k)-\Pr(Y_n=k)
=q^n\left[\Pr\{\operatorname{Bin}(n,p^2/q)=k\}
-\Pr\{\operatorname{Bin}(n,p/q)=k\}\right] \tag{2}
\]

for every \(k=0,\ldots,n\). Thus \(X_n\le_{\mathrm{st}}Y_n\), with strict inequality in distribution. The signed error in (2) is positive when \(k<n\tau(p)\), negative when \(k>n\tau(p)\), and zero when equality holds, where

\[
\tau(p)=\frac{\log(1-p)}{\log(p(1-p))}\in(0,1).
\]

The total-variation distance is **exactly**

\[
d_{\mathrm{TV}}\bigl(\mathcal L(X_n),\operatorname{Bin}(n,c)\bigr)
=q^n d_{\mathrm{TV}}\left(\operatorname{Bin}(n,p^2/q),\operatorname{Bin}(n,p/q)\right)
=q^n\left(1+O_p(e^{-\kappa_p n})\right), \tag{3}
\]

where \(\kappa_p>0\) exists for every fixed \(p\in(0,1)\). Hence the sharp exponential error rate is \(q^n\), not merely an unspecified exponential rate. The formula also supplies a finite exact sum by taking the positive terms of (2).

For each fixed \(n\ge1\),

\[
\mathbb E X_n=n\left(c-aq^{n-1}\right). \tag{4}
\]

For distinct other-part vertices \(b_i,b_j\) (so \(n\ge2\)), writing \(I_i=\mathbf1\{s\leadsto b_i\}\),

\[
\operatorname{Cov}(I_i,I_j)
=a^2q^{n-2}\left(1+2(1-p)^2-q^n\right)>0. \tag{5}
\]

At unbiased orientation \(p=1/2\), with \(b=(3/4)^n\), equations (4)--(5) imply

\[
\operatorname{Var}(X_n)=\frac{3n}{16}
+n^2\left(\frac b6-\frac{b^2}{9}\right)>\frac{3n}{16}. \tag{6}
\]

Thus a stochastically smaller reachable-vertex count has a strictly *larger* variance than its natural binomial proxy. The excess is a precisely evaluated, exponentially rare global-bottleneck effect.

## Assumptions and scope

All edge orientations are mutually independent. The orientation bias is common to every edge, measured from the two-vertex part toward the \(n\)-vertex part. Reachability allows directed paths of any finite length. The theorem covers every integer \(n\ge1\) and every real \(p\in(0,1)\); the covariance statement requires \(n\ge2\). The asymptotic in (3) holds as \(n\to\infty\) for fixed \(p\), and uniformly for \(p\) in any compact subinterval of \((0,1)\). No asymptotic claim is made when \(p\) approaches an endpoint with \(n\).

## Proof

Independently classify each vertex \(b_i\) by the directions of its two incident edges. The four types and their probabilities are: (I) \(s\to b_i\to t\), probability \(a\); (II) \(t\to b_i\to s\), probability \(a\); (III) both hubs point to \(b_i\), probability \(p^2\); (IV) \(b_i\) points to both hubs, probability \((1-p)^2\). Types for different \(i\) are independent. The other hub \(t\) is reachable from \(s\) exactly when at least one type-I vertex exists. If so, each \(b_i\) is reachable exactly when its type is I, II or III. Otherwise, \(t\) is unreachable and \(b_i\) is reachable exactly when its type is III. This follows because every directed walk alternates between the two parts, so any route through the other hub must first contain an I-type two-edge path.

On the event of no I-type vertices, the unnormalized probability generating function of \(X_n\) is \((1-p+p^2z)^n\). On the event with an I-type vertex, assign weight \(z\) to each I-, II- or III-type vertex, then subtract the orientations with no I-type vertices. This gives \(\big((1-p)^2+cz\big)^n-\big((1-p)^2+pz\big)^n\), proving (1) with a marker \(w\) for reachability of \(t\).

Now let \(Y_n\) be the number of vertices of types I, II or III. It is \(\operatorname{Bin}(n,c)\). The same orientation gives \(X_n=Y_n\) if an I-type occurs, and otherwise \(X_n\) counts only type III, so \(X_n\le Y_n\) pathwise. The event of no I-type has probability \(q^n\). Conditional on this event, \(X_n\sim\operatorname{Bin}(n,p^2/q)\) and \(Y_n\sim\operatorname{Bin}(n,p/q)\). Subtracting their conditional laws gives (2), the exact total-variation identity in (3), and strict stochastic domination.

For the sign of (2), the unnormalized difference at integer \(k\) is

\[
\binom nk\left[p^{2k}(1-p)^{n-k}-p^k(1-p)^{2(n-k)}\right].
\]

After division by the positive factor \(\binom nk p^k(1-p)^{n-k}\), its sign is that of \(p^k-(1-p)^{n-k}\). Taking logarithms and reversing the inequality upon division by \(\log(p(1-p))<0\) gives the threshold \(k=n\tau(p)\). Since \(p^2/q<p/q\), this threshold lies strictly between their respective Bernoulli parameters. Hoeffding's inequality shows that the total variation of the two corresponding binomial distributions is \(1-O_p(e^{-\kappa_p n})\), with \(\kappa_p\) chosen positive from the two gaps to \(\tau(p)\). This proves the sharp asymptotic in (3), uniformly on compact bias intervals.

Differentiating the marginal polynomial \(\mathbb E z^{X_n}=\big((1-p)^2+cz\big)^n+(1-p+p^2z)^n-\big((1-p)^2+pz\big)^n\) at \(z=1\) yields (4). Its first and second factorial moments also give

\[
\mathbb E I_i=c-aq^{n-1},\qquad
\mathbb E(I_iI_j)=c^2-(p^2-p^4)q^{n-2}.
\]

Subtracting the square of the mean and using the elementary identity \(2cq-p(1+p)=a\big(1+2(1-p)^2\big)\) gives (5). Its final factor is positive since \(0<q<1\). For \(p=1/2\), the single-vertex mean is \(3/4-b/3\) and the pair covariance is \(b/6-b^2/9\). The variance-of-sum formula yields (6), including the case \(n=1\) by its direct one-vertex calculation.

## Verification

The standalone Python 3 script `check.py` independently enumerates all \(2^{2n}=4^n\) edge orientations for every \(n=1,\ldots,6\) and five exact rational biases \(p\in\{1/4,1/3,1/2,2/3,3/4\}\). It obtains reachability by breadth-first search on each directed graph rather than by type classification, and compares the resulting exact rational joint probabilities to (1). It also checks normalization, all coefficients in (2), the sign criterion, exact mean and covariance, and the total-variation identity. The replay reports `VERIFY_OK 710 exhaustive weighted-orientation and rational identities`. The infinite claims are proved above; finite checks only corroborate them.

To reproduce, run `python3 check.py` from the directory containing this file and the checker. No third-party Python dependencies are required.

## Relationship to prior work

Bienvenu's oriented-reachability theorem proves positive association of reachability indicators on arbitrary randomly oriented graphs, extending Narayanan's two-event inequality. Equation (5) does not claim that qualitative fact as new; it quantifies its magnitude on a concrete non-tree family. Aas studies correlations of paths \(x\leadsto y\) and \(y\leadsto z\) in growing complete bipartite graphs with both sides large. Those are different events and a different size regime. Equations (1)--(3) instead determine a complete rooted cluster-count law on \(K_{2,n}\), its one-crossing signed correction, and its sharp total-variation error relative to an explicit binomial proxy. Neither inspected primary result states or logically yields these numerical identities without additional family-specific calculation.

## Limitations

This is an exact solvable-family result, not a universal law for arbitrary graph orientations or all complete bipartite part sizes. The binomial approximation rate in (3) assumes fixed interior bias. The positivity of (5) is compatible with, but no substitute for, the existing general positive-association theorem. Claims of historical priority are limited to the literature actually compared; independent validation has not been conducted.

## References

- F. Bienvenu, *Positive association of the oriented percolation cluster in randomly oriented graphs*, arXiv:1711.08815 (first public 2017-11-23), published in *Combinatorics, Probability and Computing* 28 (2019), 811--815, https://arxiv.org/abs/1711.08815 ; lawful full text: https://www.normalesup.org/~bienvenu/articles/BienvenuCPC2019.pdf .
- B. Narayanan, *Connections in randomly oriented graphs*, arXiv:1609.01003 (2016), *Combinatorics, Probability and Computing* 27 (2018), 667--671, https://arxiv.org/abs/1609.01003 .
- E. Aas, *Path correlations in a randomly oriented complete bipartite graph*, arXiv:1102.1711 (2011), https://arxiv.org/abs/1102.1711 .
