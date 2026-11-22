# Sparse threshold-graph births and one-dependent clique clocks

## Finding
Let \(X_1,\ldots,X_n\) be independent uniform variables on \([0,1]\). For \(t\geq0\) form a graph \(G_n(t)\) on \([n]\) by joining distinct \(i,j\) when \(X_i+X_j>2-t/n\). Put \(Y_{n,i}=n(1-X_i)\). Fix \(b>0\), and let \(H_n^{(b)}(t)\), \(0\leq t\leq b\), be the marked graph process obtained by retaining exactly those vertices with \(Y_{n,i}\leq b\), ordered by their real marks, with an edge when their marks sum to less than \(t\). The remaining vertices of \(G_n(t)\) are isolated throughout the window.

Let \(\Xi\) be a homogeneous rate-one Poisson point process on \([0,\infty)\), and construct \(H^{(b)}(t)\) from its points in \([0,b]\) by the same rule. Then, for every \(n>b\),
\[
 d_{\mathrm{TV}}\bigl(\mathcal L((H_n^{(b)}(t))_{0\leq t\leq b}),\mathcal L((H^{(b)}(t))_{0\leq t\leq b})\bigr)\leq \frac{b^2}{n}.
\]
Here each graph retains its marked active vertices even before their first incident edge, so this is a statement about entire marked paths, not merely one-time edge counts.

For \(k\geq2\), let \(T_{n,k}\) denote the infimum of \(t\) at which \(G_n(t)\) has a clique of size \(k\). Write \(E_1,E_2,\ldots\) for independent standard exponential variables and \(A_j=\sum_{i=1}^jE_i\). Every finite vector of clique birth times converges jointly:
\[
 (T_{n,2},\ldots,T_{n,r})\ \xrightarrow{d}\ (T_2,\ldots,T_r),\qquad T_k=A_{k-1}+A_k.
\]
In particular, the successive limiting interbirth times \(\Delta_k=T_{k+1}-T_k=E_k+E_{k+1}\), \(k\geq2\), form a stationary **one-dependent** sequence. Each has the \(\mathrm{Gamma}(2,1)\) law, adjacent increments have covariance \(1\) and correlation \(1/2\), and increments separated by at least two indices are independent. The clique-birth times are therefore not a renewal process. Their first two survival functions are
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
and consequently
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
The weights are genuinely independent \(\mathrm{Uniform}(0,1)\); the graph has no loops and no repeated edges. All boundaries are unambiguous almost surely, so strict and weak inequalities agree in distribution. The process total-variation assertion concerns fixed bounded \(t\)-windows and the graph of points with scaled deficit at most \(b\). Original vertices with deficits exceeding \(b\) are deterministically isolated during that window. Clique-clock convergence holds for each fixed finite number of clique sizes. For exact finite moments and the finite no-edge formula assume \(n\geq2\) and \(0\leq t\leq n\).

## Proof
**Point-process reduction.** Since \(Y_{n,i}=n(1-X_i)\) is uniform on \([0,n]\), the number of marks in \([0,b]\) is \(\mathrm{Bin}(n,b/n)\). Conditional on that count, the marks are independent uniform points on \([0,b]\). This is also the conditional mark law for a Poisson process of rate one with count \(\mathrm{Pois}(b)\). Consequently the total-variation distance between the point-process laws is precisely the total-variation distance between these counts; the standard Bernoulli-to-Poisson coupling gives at most \(n(b/n)^2=b^2/n\). An edge before time \(b\) must join marks individually smaller than \(b\). The marked graph path is a deterministic measurable transformation of the point process on \([0,b]\), proving the path bound by contraction of total variation. A fixed finite collection of first order statistics converges to \((A_1,\ldots,A_r)\) by applying the same coupling on \([0,b]\) and then increasing \(b\), since the \(r\)-th point of the limiting process is finite almost surely.

**Clique clocks.** Let \(Y_{n,(1)}<\cdots<Y_{n,(n)}\) be the ordered deficits. A set of \(k\) distinct vertices forms a clique at time \(t\) exactly when the sum of its two largest deficits is less than \(t\). Every \(k\)-set has these two values at least \(Y_{n,(k-1)}\) and \(Y_{n,(k)}\) in the componentwise order, so the infimum birth threshold is precisely \(T_{n,k}=Y_{n,(k-1)}+Y_{n,(k)}\); at that equality the strict-edge graph has not yet acquired the clique. Passage to the extreme-point limit gives \(T_k=A_{k-1}+A_k\), and subtracting yields \(\Delta_k=E_k+E_{k+1}\). Disjoint pairs of exponential increments are independent; adjacent pairs share one exponential. This proves the stated Gamma margins and one-dependence, variance \(2\) and adjacent covariance \(1\). For \(T_2=2E_1+E_2\), convolution gives \(\Pr(T_2>t)=2e^{-t/2}-e^{-t}\). For \(T_3=2(E_1+E_2)+E_3\), convolution with a Gamma shape-two variable gives \(\Pr(T_3>t)=e^{-t}+te^{-t/2}\).

**Exact finite first edge.** The minimum deficit \(Z\) has survival \(\Pr(Z\geq u)=(1-u/n)^n\) for \(0\leq u\leq n\). No pair has sum below \(t\) iff the second-smallest mark is at least \(t-Z\). Decompose according to \(Z\geq t/2\), or \(0\leq Z<t/2\) with all other marks at least \(t-Z\). Integration of the density of the minimum gives
\[
 \Pr(M_n(t)=0)=\left(1-\frac{t}{2n}\right)^n +\int_0^{t/2}\left(1-\frac{t-z}{n}\right)^{n-1}dz.
\]
The integral is \((1-t/(2n))^n-(1-t/n)^n\), producing the claimed expression.

**Edge moments.** The area of \(\{(y_1,y_2)\in[0,n]^2:y_1+y_2<t\}\) is \(t^2/2\), so the probability of a specified edge is \(p=t^2/(2n^2)\). For two edges sharing one endpoint, integrating the squared conditional neighbor probability gives \(q=\int_0^t (t-z)^2 dz/n^3=t^3/(3n^3)\). Disjoint-edge indicators are independent. In the variance expansion, there are \(\binom n2\) individual edge terms and \(n(n-1)(n-2)\) ordered pairs of edges sharing exactly one vertex. This yields the exact formula. Bounded-window path total-variation convergence transfers the edge-count distribution, and the exact moments converge to \(t^2/4\) and \(t^2/4+t^3/3\); alternatively Poisson Campbell integration gives those same limits directly. Their unequal mean and variance prove non-Poissonity for \(t>0\).

**Unique nontrivial component.** In the limiting Poisson graph at time \(t\), let \(Z\) be the smallest mark. If no mark lies below \(t/2\), there are no edges. Otherwise every vertex with mark less than \(t-Z\) is joined to \(Z\), while every larger-mark vertex is isolated, because \(Z\) is smallest. Conditional on \(Z=z<t/2\), the number of *additional* vertices joined to \(Z\) is \(\mathrm{Pois}(t-2z)\). The event of a nontrivial component of size \(k\geq2\) therefore has probability
\[
 \int_0^{t/2}e^{-z}e^{-(t-2z)}\frac{(t-2z)^{k-1}}{(k-1)!}\,dz
 =2^{k-1}e^{-t/2}\left(1-e^{-t/2}\sum_{j=0}^{k-1}\frac{(t/2)^j}{j!}\right).
\]
The zero case is the first-edge survival probability. This also proves the uniqueness of the nontrivial component.

**Critical scale.** More generally set the original threshold to \(2-cn^{-\alpha}\), with \(c>0\) and \(\alpha>0\). For \(\alpha>1\), the expected edge count is at most a constant times \(n^{2-2\alpha}\), hence the graph is empty with probability tending to one. For \(0<\alpha<1\), the number of weights within \(cn^{-\alpha}/2\) of one diverges in probability and these vertices form a clique, so every fixed clique appears with probability tending to one. Thus \(\alpha=1\) is the sharp nondegenerate first-clique birth scale.

## Verification
The companion `CHECKER.py` uses only Python's standard library. It exactly compares an independent binomial-integral expansion against the finite no-edge identity, two combinatorial variance calculations, and all small strictly ordered grid configurations for the clique-clock criterion. The test suite completed 7,387 exact assertions. Those finite tests are corroboration; the infinite-process and limiting statements are justified by the analytic arguments above.

## Relationship to prior work
Diaconis, Holmes and Janson provide the general threshold-graph representation \(X_i+X_j>t\) and dense fixed-distribution graph limits, notably Section 6.2 and Theorem 6.3. Reilly and Scheinerman investigate the uniform-weight model at the **fixed** threshold one, with clique and edge statistics. Neither inspected primary treatment establishes the moving upper-endpoint scale \(2-t/n\), the complete marked Poisson graph-path approximation, the one-dependent Gamma clique-birth sequence, or this explicit component-size law. The Poisson approximation of rare Bernoulli points is classical and is used as an ingredient rather than claimed as new. The result records the combined graph-process and joint-statistic consequences for this boundary regime. This is a best-knowledge literature comparison, not a certified historical priority statement.

## Limitations
The error \(b^2/n\) is an upper bound, not a claimed optimal asymptotic. It controls a **bounded window** of the active marked graph path; it does not compare full original graphs with differing numbers of deterministic isolated vertices in total variation. The clique-clock result concerns fixed finite dimensions as \(n\to\infty\). General non-uniform upper-tail weight laws, growing windows, and uniform-in-clique-size error bounds are not proved. Historical priority may be affected by literature not indexed or accessible in the cited sources.

## References
1. P. Diaconis, S. Holmes, and S. Janson, *Threshold graph limits and random threshold graphs*, *Internet Mathematics* 5 (2008), 267–320; manuscript August 2009, arXiv:0908.2448, https://arxiv.org/abs/0908.2448 and author's full text https://www2.math.uu.se/~svantejs/papers/sj238.pdf.
2. E. Perez Reilly and E. R. Scheinerman, *Random Threshold Graphs*, *Electronic Journal of Combinatorics* 16 (2009), R130, https://doi.org/10.37236/219; full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r130/pdf.
3. L. Le Cam, *An approximation theorem for the Poisson binomial distribution*, *Pacific Journal of Mathematics* 10 (1960), 1181–1197. The standard sum-of-squared-Bernoulli-parameters bound is used only for the marked-process coupling.
