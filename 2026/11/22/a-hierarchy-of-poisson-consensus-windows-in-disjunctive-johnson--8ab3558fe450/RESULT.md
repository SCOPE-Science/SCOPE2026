# A hierarchy of Poisson consensus windows in disjunctive Johnson dynamics

## Finding
Let \(k\ge4\) be fixed and let \(n\to\infty\) through integers \(n\ge2k\). On the Johnson graph \(J(n,k)\), put independent Bernoulli-\(p\) values at its \(\binom nk\) vertices, and update synchronously by the OR of the values at adjacent vertices (without self-input). Let \(T\) be the first update at which every vertex has value one, with \(T=\infty\) if this never occurs.

For each fixed integer \(2\le r\le k-2\), put
\[
 b=\binom kr,\quad m_n=\binom{n-r}{k-r},\quad p=p_{n,r}(c)=\frac{(k/b)\log n+c}{m_n},\qquad c\in\mathbb R.
\]
Let \(Y_{n,r}\) count the \(k\)-subsets \(A\subseteq[n]\) having **no initially occupied \(k\)-subset meeting \(A\) in at least \(r\) elements**. Then
\[
 Y_{n,r}\ \xrightarrow{d}\ \operatorname{Poisson}\!\left(\frac{e^{-bc}}{k!}\right).
\]
In the same regime, the only asymptotically possible hitting times are \(k-r\) and \(k-r+1\), with
\[
 \lim_{n\to\infty}\Pr(T=k-r)=\exp\!\left(-\frac{e^{-bc}}{k!}\right),\qquad
 \lim_{n\to\infty}\Pr(T=k-r+1)=1-\exp\!\left(-\frac{e^{-bc}}{k!}\right).
\]
Thus each temporal layer from update \(2\) through update \(k-2\) has a distinct Poisson window, at scale \((\log n)/n^{k-r}\). These are windows for eliminating **all-uncovered \(k\)-subsets of the \(r\)-shadow**, not for covering every \(r\)-subset. In fact the latter event is overwhelmingly absent at these densities.

The endpoint \(r=1\) has a different limiting law: for \(p=(\log n+c)/\binom{n-1}{k-1}\),
\[
 \lim_{n\to\infty}\Pr(T=k-1)
 =e^{-e^{-c}}\sum_{j=0}^{k-1}\frac{e^{-cj}}{j!},\qquad
 \lim_{n\to\infty}\Pr(T=k)=1-e^{-e^{-c}}\sum_{j=0}^{k-1}\frac{e^{-cj}}{j!}.
\]
The first expression is a Poisson lower tail rather than the probability of zero points in a Poisson process. For each finite \(n\ge2k\), the worst-case time over all nonzero initial states is exactly \(k\).

## Assumptions and scope
The graph is the simple, undirected Johnson graph on the \(k\)-subsets of \([n]=\{1,\ldots,n\}\), with adjacency exactly when two distinct subsets share \(k-1\) points. The local OR update has **no self-loop**. The two-value initial states are independent and identically distributed; \(k,r,c\) remain fixed as \(n\) grows. The displayed probabilities are within \([0,1]\) for all sufficiently large \(n\). Only the asymptotic laws, not finite-\(n\) Poisson equality or arbitrary growing \(k\), are asserted.

Write \(\mathcal S\) for the set of initially occupied \(k\)-subsets, and \(\partial_r\mathcal S\) for the \(r\)-subsets contained in some member of \(\mathcal S\). At time \(t=k-r\ge2\), a vertex \(A\) remains zero exactly when every \(r\)-subset of \(A\) is absent from \(\partial_r\mathcal S\). This equivalence is exact at every finite \(n\ge2k\).

## Proof
**1. Exact-length propagation.** The graph distance from \(A\) to \(B\) in \(J(n,k)\) is \(d(A,B)=k-|A\cap B|\). For any \(t\ge2\), a walk of length exactly \(t\) from \(B\) to \(A\) exists if and only if \(d(A,B)\le t\). To see sufficiency, use a shortest path of length \(d\ge1\); every edge lies in a triangle, allowing a one-step detour, and backtracks add two steps. For \(d=0\), closed walks of lengths two and three exist, and their sums give every length at least two. This uses \(n\ge2k\) and \(k\ge4\). Consequently, for \(2\le t\le k\),
\[
 F^t(x)_A=\bigvee_{B:\,|A\cap B|\ge k-t}x_B.
\]
In particular a nonempty initial support fills the graph by update \(k\); a singleton support and a disjoint target attain update \(k\).

**2. Vacant shadow cliques.** At \(t=k-r\), the preceding formula says that \(F^t(x)_A=0\) precisely when all \(\binom kr=b\) members of \(\binom Ar\) are uncovered by initially occupied blocks. Hence \(F^t(x)\) is all ones if and only if \(Y_{n,r}=0\). For one fixed \(A\), the number of potential initially occupied \(k\)-blocks meeting \(A\) in at least \(r\) labels is
\[
 D_n=\sum_{j=r}^k\binom kj\binom{n-k}{k-j}
    =b m_n+O(n^{k-r-1}).
\]
Thus \(\Pr(A\text{ is vacant})=(1-p)^{D_n}=n^{-k}e^{-bc}(1+o(1))\), and \(\mathbb E Y_{n,r}\to\mu=e^{-bc}/k!\).

**3. Dependence-controlled factorial moments.** Fix any positive integer \(h\) and distinct candidate sets \(A_1,\ldots,A_h\). Let \(v=|\bigcup_i A_i|\) and let \(e\) count the distinct \(r\)-subsets contained in at least one \(A_i\). Each such \(r\)-subset is contained in \(m_n\) possible initially occupied blocks, and the overlap of two distinct containment families is \(O(n^{k-r-1})\). As \(h,k\) are fixed,
\[
 \Pr(A_1,\ldots,A_h\text{ all vacant})
 =(1-p)^{e m_n+O(n^{k-r-1})}
 =n^{-ke/b}e^{-ce}(1+o(1)).
\]
The error is uniform over the finitely many overlap patterns for each fixed \(h\), because \(p=O(\log n/n^{k-r})\) and \(p^2m_n=o(1)\).

For vertex-disjoint \(A_i\), \(v=hk\) and \(e=hb\), so these tuples contribute \(\mu^h+o(1)\) to \(\mathbb E(Y_{n,r})_h\). Any tuple containing overlapping sets has \(v-ke/b<0\): start each connected component of the intersection pattern with one \(k\)-set. When another \(k\)-set shares \(s\) vertices with those already present, it adds \(k-s\) vertices and at least \(b-\binom sr\) new \(r\)-subsets. For \(1\le s<k\), the change in \(v-ke/b\) is at most
\[
 -s+\frac{k}{b}\binom sr<0,
\]
using \(r\ge2\) and \(\binom{s-1}{r-1}<\binom{k-1}{r-1}\). If \(s=k\), the change is nonpositive. An overlapping component of distinct sets has at least one strict change. Therefore its total contribution is \(O(n^{v-ke/b})=o(1)\). The falling factorial moments all tend to \(\mu^h\), which proves \(Y_{n,r}\Rightarrow\operatorname{Poisson}(\mu)\).

**4. Only two adjacent times survive.** For a fixed target \(A\), the number of blocks meeting it in at least \(r+1\) elements is \(O(n^{k-r-1})\). Its probability of receiving any such initially active block is \(O(pn^{k-r-1})=O(\log n/n)=o(1)\). Even when \(k-r-1=1\), this bounds the one-step activation event. Hence \(\Pr(T\le k-r-1)=o(1)\). On the other side, the probability that a fixed \((r-1)\)-set is uncovered is \((1-p)^{\binom{n-r+1}{k-r+1}}=\exp(-\Theta(n\log n))\); a union bound shows that all such sets are covered with probability tending to one, forcing \(F^{k-r+1}(x)\) to be all ones. The Poisson zero-count probability now gives the two displayed limits. More sharply, the number \(Z_n\) of entirely uncovered \(r\)-subsets satisfies \(\mathbb E Z_n\asymp n^{r-k/b}\to\infty\) in this window, because \(k/b<r\). Two distinct \(r\)-subsets have containment families overlapping in only \(O(n^{k-r-1})\) potential blocks, so their uncovered-event joint probability is the product of the marginal probabilities times \(1+o(1)\), uniformly in the pair. Hence \(\operatorname{Var}(Z_n)=o((\mathbb E Z_n)^2)\), and with high probability some \(r\)-subsets remain uncovered even though every \(k\)-set contains a covered one when \(Y_{n,r}=0\).

**5. The exceptional first shadow.** If \(r=1\), let \(X_n\) be the number of labels of \([n]\) belonging to no initially occupied block. At the displayed \(p\), for every fixed \(h\),
\[
 \mathbb E(X_n)_h=(n)_h(1-p)^{\binom nk-\binom{n-h}{k}}\longrightarrow e^{-ch}.
\]
Therefore \(X_n\Rightarrow\operatorname{Poisson}(e^{-c})\). Exactly \(\binom{X_n}{k}\) target \(k\)-sets are zero at time \(k-1\); this is not an independent Poisson count. At time \(k-2\), any fixed target has probability \(O(\log n/n)\) of having been activated, whereas any nonempty initial support reaches full ones by update \(k\). The probability of the empty initial support tends to zero. The endpoint limits follow.

## Verification
The standalone `check.py` constructs the Johnson adjacencies and computes synchronous OR iterations directly, independently comparing them with distance-ball propagation and vacant-shadow predicates. With deterministic seeds it passed 26,180 update comparisons on 5,974 initial states across \((n,k)=(6,3),(8,4),(10,5),(12,6)\). These are sampled finite checks, not exhaustive proofs. The standalone `moment_check.py` computes exact first and second falling factorial moments by enumerating overlaps of candidate target blocks, and reports their convergence toward the predicted Poisson moments for \((k,r)=(4,2),(5,2),(5,3)\). Both scripts require only standard Python. The infinite statements rest on the preceding factorial-moment proof, not on the numerical checks.

## Relationship to prior work
Jarrah, Laubenbacher and Veliz-Cuba (2008) analyze general conjunctive and disjunctive Boolean networks and their cycle structures and transient bounds. Johnson graph geometry and lotto-design correspondence are standard; Cornet, Dravec and Torres (2026) study minimum domination and total domination, including the one-step overlap condition. Godbole and Janson (1996) study random **complete** covering of every \(r\)-set, and Cooley, Kang and Koch (2015) give Poisson laws for isolated \(r\)-sets near the much later full-shadow-cover threshold \(p\sim r\log n/m_n\). Those statements do not yield the present earlier threshold \(p\sim(k/\binom kr)\log n/m_n\), where many uncovered \(r\)-sets remain but no \(k\)-set has all its \(r\)-faces uncovered. The new assertion is the complete hierarchy of Poisson gap counts and their precise synchronous consensus-time laws. The underlying distance and shadow equivalence is not asserted to be new.

## Limitations
The fixed-\(k\) regime does not imply uniformity for growing \(k\). No claim is made for the distinct first-update window \(t=1\), for nonuniform initial probabilities, for asynchronous updates, or for finite-\(n\) Poisson equality. The factorial-moment argument supplies weak convergence, not a quantitative total-variation rate. Priority remains subject to literature not located in the referenced searches.

## References
- A. S. Jarrah, R. Laubenbacher, A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, arXiv:0805.0275v1, first public 2008-05-02, https://arxiv.org/abs/0805.0275.
- A. P. Godbole and S. Janson, *Random Covering Designs*, Journal of Combinatorial Theory, Series A 75 (1996), 85–98, https://doi.org/10.1006/jcta.1996.0065.
- O. Cooley, M. Kang and C. Koch, *Threshold and hitting time for high-order connectivity in random hypergraphs*, arXiv:1502.07289, first public 2015-02-25, https://arxiv.org/abs/1502.07289.
- M. G. Cornet, T. Dravec and P. Torres, *Domination and Total Domination in Johnson graphs*, arXiv:2610.04675v1, first public 2026-10-03, https://arxiv.org/html/2610.04675v1.
