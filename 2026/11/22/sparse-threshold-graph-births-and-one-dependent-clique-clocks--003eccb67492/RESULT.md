# Sparse threshold-graph births and one-dependent clique clocks

## Finding
Let \(X_1,\ldots,X_n\) be independent uniform variables on \([0,1]\). For \(t\geq0\) form a graph \(G_n(t)\) on \([n]\) by joining distinct \(i,j\) when \(X_i+X_j>2-t/n\). Put \(Y_{n,i}=n(1-X_i)\). Fix \(b>0\), and let \(H_n^{(b)}(t)\), \(0\leq t\leq b\), be the marked graph process obtained by retaining exactly those vertices with \(Y_{n,i}\leq b\), ordered by their real marks, with an edge when their marks sum to less than \(t\). The remaining vertices of \(G_n(t)\) are isolated throughout the window.

Let \(\Xi\) be a homogeneous rate-one Poisson point process on \([0,\infty)\), and construct \(H^{(b)}(t)\) from its points in \([0,b]\) by the same rule. Then, for every \(n>b\),
\[
 d_{\mathrm{TV}}\bigl(\mathcal L((H_n^{(b)}(t))_{0\leq t\leq b}),\mathcal L((H^{(b)}(t))_{0\leq t\leq b})\bigr)\leq \frac{b^2}{n}.
\]
Here each graph retains its marked active vertices even before their first incident edge, so this is a statement about entire marked paths, not merely one-time edge counts.

For \(k\geq2\) and \(n\ge k\), let \(T_{n,k}\) denote the infimum of \(t\) at which \(G_n(t)\) has a clique of size \(k\). Write \(E_1,E_2,\ldots\) for independent standard exponential variables and \(A_j=\sum_{i=1}^jE_i\). Every fixed finite vector of clique birth times converges jointly:
\[
 (T_{n,2},\ldots,T_{n,r})\ \xrightarrow{d}\ (T_2,\ldots,T_r),\qquad T_k=A_{k-1}+A_k.
\]
In particular, the successive limiting interbirth times \(\Delta_k=T_{k+1}-T_k=E_k+E_{k+1}\), \(k\geq2\), form a stationary **one-dependent** sequence. Each has the \(\mathrm{Gamma}(2,1)\) law, adjacent increments have covariance \(1\) and correlation \(1/2\), and increments separated by at least two indices are independent. The clique-birth times are therefore not a renewal process. Their first two survival functions for \(t\ge0\) are
\[
 \Pr(T_2>t)=2e^{-t/2}-e^{-t},\qquad \Pr(T_3>t)=e^{-t}+te^{-t/2}.
\]

Let \(M_n(t)\) be the total number of edges of \(G_n(t)\) and \(M(t)\) the edge count of the Poisson graph. For \(0\leq t\leq n\),
\[
 \begin{aligned}
 \mathbb E M_n(t)&=\binom n2\frac{t^2}{2n^2},\\
 \operatorname{Var}M_n(t)&=\binom n2\frac{t^2}{2n^2}\left(1-\frac{t^2}{2n^2}\right)
 +n(n-1)(n-2)\left(\frac{t^3}{3n^3}-\frac{t^4}{4n^4}\right),
 \end{aligned}
\]
and the limiting graph has
\[
 \mathbb E M(t)=\frac{t^2}{4},\qquad
 \operatorname{Var}M(t)=\frac{t^2}{4}+\frac{t^3}{3}.
\]
The limiting edge-count law is not Poisson at any \(t>0\), despite its finite mean. The exact finite-sample first-edge survival probability is
\[
 \Pr(M_n(t)=0)=2\left(1-\frac{t}{2n}\right)^n-\left(1-\frac{t}{n}\right)^n,\qquad 0\leq t\leq n.
\]

Finally, let \(K(t)\) be the size of the unique nontrivial connected component of the Poisson graph, setting \(K(t)=0\) when there are no edges. For every integer \(k\geq2\),
\[
 \Pr(K(t)=k)=2^{k-1}e^{-t/2}\left(1-e^{-t/2}\sum_{j=0}^{k-1}\frac{(t/2)^j}{j!}\right),
\]
with \(\Pr(K(t)=0)=2e^{-t/2}-e^{-t}\). All other components are isolated vertices. This joint picture describes the emergence of cliques and a single active component at the sparse, upper-endpoint scale.

## Assumptions and scope
The weights are independent \(\mathrm{Uniform}(0,1)\); the graph has no loops or repeated edges. For any fixed deterministic \(t\), edge equality has probability zero, so strict and weak edge inequalities give the same snapshot distribution. They need not give identical paths at the random birth thresholds: the stated marked paths use the strict rule on both sides. They can be encoded by the ordered mark list and the strict rule, which determines the path at every time, including at a birth threshold. The total-variation assertion concerns fixed bounded windows and retains only vertices of scaled deficit at most \(b\); all larger-deficit vertices are isolated in this window. Clique-clock convergence is for each fixed finite vector. For the finite edge moments and first-edge formula assume \(n\ge2\) and \(0\leq t\leq n\).

## Proof
**Point-process reduction.** The number of uniform deficits in \([0,b]\) is \(\mathrm{Bin}(n,p)\), \(p=b/n\). Conditional on the count, the ordered marks are uniform order statistics in \([0,b]\), the same conditional mark law as for a rate-one Poisson process with count \(\mathrm{Pois}(b)\). Couple each of \(n\) independent Bernoulli variables with a Poisson variable of mean \(p\) by maximal coupling; their disagreement probability is \(p(1-e^{-p})\le p^2\). The sums thus disagree with probability at most \(np^2=b^2/n\). On equality of counts use the same ordered marks. The paths then coincide at every time by the common strict rule. This proves the TV bound. The joint convergence of any fixed number of first order statistics follows by coupling on \([0,b]\) and letting \(b\) increase after \(n\to\infty\), since the corresponding last Poisson arrival is finite almost surely.

**Clique clocks.** A set of \(k\) distinct vertices forms a clique at time \(t\) exactly when the sum of its two largest deficits is less than \(t\). Every \(k\)-set has these two values at least \(Y_{n,(k-1)}\) and \(Y_{n,(k)}\) in the componentwise order; the first \(k\) marks attain the bound. The infimum birth threshold is \(T_{n,k}=Y_{n,(k-1)}+Y_{n,(k)}\); at that equality the strict-edge graph has not yet acquired the clique. The extreme-point limit gives \(T_k=A_{k-1}+A_k\), hence \(\Delta_k=E_k+E_{k+1}\). Disjoint pairs of exponentials are independent; adjacent pairs share one term of variance one. This gives the Gamma margins, stationarity, one-dependence, variance two and adjacent covariance one. Convolving \(2E_1\) with \(E_2\) gives the survival of \(T_2\), and convolving \(2(E_1+E_2)\) with \(E_3\) gives the survival of \(T_3\).

**Exact finite first edge.** Let \(Z\) be the minimum deficit. Either \(Z\ge t/2\), or \(0\le Z<t/2\) and all other marks must be at least \(t-Z\) for there to be no edge. Selecting which of the \(n\) vertices attains the minimum contributes a factor \(n\), canceled by its density \(1/n\). Thus
\[
 \Pr(M_n(t)=0)=\left(1-\frac{t}{2n}\right)^n +\int_0^{t/2}\left(1-\frac{t-z}{n}\right)^{n-1}dz
 =2\left(1-\frac{t}{2n}\right)^n-\left(1-\frac{t}{n}\right)^n.
\]

**Edge moments.** A specified edge has probability \(p_e=t^2/(2n^2)\) by the area of the threshold triangle in \([0,n]^2\). Two edges sharing a vertex have joint probability \(q_e=\int_0^t(t-z)^2dz/n^3=t^3/(3n^3)\); disjoint edges are independent. There are \(\binom n2\) individual edges and \(n(n-1)(n-2)\) ordered pairs sharing an endpoint, giving the finite variance. For the Poisson graph use its factorial moment measures, which are Lebesgue measure in each coordinate. The mean is half the same threshold-triangle area. In the variance, the disjoint pairs cancel the squared mean, the identical pairs contribute the mean, and the ordered pairs sharing an endpoint contribute exactly \(\int_0^t(t-z)^2dz=t^3/3\). This proves the limiting moments directly; total-variation convergence need not on its own control unbounded moments.

**Unique nontrivial component.** For the Poisson graph let \(Z\) be the smallest mark. If \(Z\ge t/2\), there are no edges. Otherwise every mark other than \(Z\) below \(t-Z\) is connected to \(Z\), and marks at or above that threshold are isolated. Conditional on \(Z=z<t/2\), the number of additional vertices below \(t-Z\) is \(\mathrm{Pois}(t-2z)\), by the independent Poisson process after the first arrival. For \(k\ge2\),
\[
 \begin{aligned}
 \Pr(K(t)=k)
 &=\int_0^{t/2} e^{-z}e^{-(t-2z)}\frac{(t-2z)^{k-1}}{(k-1)!}\,dz\\
 &=2^{k-1}e^{-t/2}\left(1-e^{-t/2}\sum_{j=0}^{k-1}\frac{(t/2)^j}{j!}\right),
 \end{aligned}
\]
by the substitution \(w=(t-2z)/2\). The zero case is exactly first-edge survival.

**Critical scale.** At threshold \(2-cn^{-\alpha}\) with \(c>0\), \(\alpha>1\) forces the expected edge count to zero at order \(n^{2-2\alpha}\). For \(0<\alpha<1\), the number of weights within \(cn^{-\alpha}/2\) of one diverges in probability by the binomial mean and variance bounds. These vertices form a clique almost surely at that deterministic threshold, so every fixed clique appears with probability tending to one. Hence \(\alpha=1\) is the nondegenerate birth scale for every fixed clique size at least two.

## Verification
The companion `CHECKER.py` compares exact binomial-integral expansions and finite variance calculations and exhausts its stated small ordered grid configurations for the clique criterion. These tests are supplementary; the bounds and infinite-process laws follow from the analytic proof.

## Relationship to prior work
Diaconis, Holmes and Janson, §6.2 and Theorem 6.3, give the general random threshold-graph representation and graph limits for a fixed iid weight law and fixed threshold. Reilly and Scheinerman study independent uniform weights at the fixed threshold one; their published abstract describes graph statistics including chromatic number and Hamiltonicity. That observation threshold corresponds to \(t=n\) here, not the bounded sparse window. The Poisson approximation of rare Bernoulli points is classical; the path bound here is its direct marked-process application. The additions assessed here are the collection of graph-process and joint-statistic consequences for the moving sparse threshold, especially the one-dependent clique clocks and the explicit active-component law. The comparison is not a claim of historical priority; the full Reilly–Scheinerman proof was not used to exclude related results there.

## Limitations
The bound \(b^2/n\) is an upper bound, not a claimed optimal asymptotic. It does not compare full original graphs with differing numbers of isolated vertices in total variation. Clique-clock convergence is in fixed finite dimensions. Nonuniform weight tails, growing windows, and uniform-in-clique-size error bounds are not proved.

## References
1. P. Diaconis, S. Holmes, and S. Janson, *Threshold graph limits and random threshold graphs*, *Internet Mathematics* 5 (2008), 267–320; arXiv:0908.2448, https://arxiv.org/abs/0908.2448.
2. E. Perez Reilly and E. R. Scheinerman, *Random Threshold Graphs*, *Electronic Journal of Combinatorics* 16 (2009), R130, https://doi.org/10.37236/219.
3. L. Le Cam, *An approximation theorem for the Poisson binomial distribution*, *Pacific Journal of Mathematics* 10 (1960), 1181–1197.
