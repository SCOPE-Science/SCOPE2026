# Exact degree law and Gaussian fluctuations in the two-read deletion reconstruction graph

## Finding
Fix an integer alphabet size \(q\ge 2\). The two-read single-deletion graph \(G_{n,q}\) has the \(q^n\) words of length \(n\) as vertices; two distinct words are adjacent precisely when their sets of distinct length-\(n-1\) one-deletion outputs have intersection size two. Write \(\Delta(x)\) for a vertex degree and \(F_{n,q}(z)=\sum_{x\in\Sigma_q^n}z^{\Delta(x)}\). For every \(n\ge1\), the complete degree enumerator is given by the explicit coefficient-positive recursion below:

\[
\begin{aligned}
f_{1,1}(z)&=q,\\
f_{n+1,1}(z)&=\sum_{t=1}^{n}f_{n,t}(z),\\
f_{n+1,2}(z)&=z\left((q-1)f_{n,1}(z)+(q-2)\sum_{t=2}^{n}f_{n,t}(z)\right),\\
f_{n+1,t+1}(z)&=z^t f_{n,t}(z)\quad(2\le t\le n),\\
F_{n,q}(z)&=\sum_{t=1}^{n}f_{n,t}(z).
\end{aligned}
\]

All unlisted initial states are zero. If \(X\) is a uniform random vertex and \(r=1/q\), define
\[
V_{i,q}=\frac{2}{q-1}+r^{i-1}\left(\frac{q-3}{q-1}-2(i-1)\right)-r^{2(i-1)}.
\]
Then, for every \(n\ge1\),
\[
\mathbb E\Delta(X)=n-\frac{q(1-q^{-n})}{q-1},\qquad
\operatorname{Var}(\Delta(X))=\sum_{i=1}^{n}V_{i,q}\left(1+\frac{2(1-q^{-(n-i)})}{q-1}\right).
\]
For fixed \(q\) and \(n\to\infty\),
\[
\operatorname{Var}(\Delta(X))=\frac{2(q+1)}{(q-1)^2}n+O_q(1),\qquad
\frac{\Delta(X)-\mathbb E\Delta(X)}{\sqrt n}\xrightarrow{d}\mathcal N\left(0,\frac{2(q+1)}{(q-1)^2}\right).
\]
The mean is included for normalization and agrees with an earlier exact edge-count result; the claimed contribution is the full distribution recursion, finite variance and explicit asymptotic fluctuations.

## Assumptions and scope
The channel deletes exactly one coordinate, leaving a *set* of distinct outputs. There are no cyclic endpoints, no substitutions, and no repeated-read multiplicities. An edge means exactly two common deletion outputs, not at least one. All formulas hold for every integer \(q\ge2\) and \(n\ge1\), including the edgeless case \(n=1\). The central limit theorem holds with fixed \(q\) as \(n\to\infty\); it makes no assertion for \(q\) growing with \(n\).

For a word \(x=x_1\cdots x_n\), call an interval \([a,b]\), \(1\le a<b\le n\), alternating if it uses two different symbols in alternating order: \(x_a\ne x_{a+1}\) and \(x_{k}=x_{k-2}\) for \(a+2\le k\le b\). Define \(R_1=0\), and for \(j\ge2\) define \(R_j\) as the number of alternating intervals ending at \(j\), equivalently the maximal alternating suffix length minus one (zero if its last two symbols agree).

## Proof
**Step 1 — degrees are alternating-interval counts.** Proposition 9 in Cai–Kiah–Nguyen–Yaakobi (2020) characterizes pairs of length-\(n\) distinct words with exactly two common deletion outputs: they agree outside an interval and on that interval they are the two opposite phases of an alternating two-symbol pattern. Every alternating interval in \(x\) therefore defines a neighboring word by exchanging the two local symbols over the entire interval. Different intervals give different neighbors: the interval is recovered uniquely as the first through last coordinates on which the two words differ. Conversely the cited characterization supplies such an interval for every neighbor. Consequently
\[\Delta(x)=\sum_{j=1}^{n}R_j.\]
The Type-A characterization is prior work; this argument uses it without claiming the characterization itself.

**Step 2 — exact enumerator.** Let \(f_{n,t}(z)\) count length-\(n\) words with maximal alternating suffix length exactly \(t\), weighted by \(z^{\Delta(x)}\). Appending the preceding symbol sets the suffix length to one and creates no new alternating interval (one choice). If the previous suffix has length one, appending any of the other \(q-1\) symbols gives suffix length two and creates one interval. If the suffix has length \(t\ge2\), appending the penultimate symbol (one choice) extends the suffix to \(t+1\) and creates \(t\) intervals, while appending a symbol different from both of its two last symbols (\(q-2\) choices) resets the alternating suffix length to two and creates one interval. These exhaustive disjoint cases give the displayed recurrence by induction for every \(n\), including \(q=2\), where the third case is absent.

**Step 3 — exact first and second moments.** For uniform independent symbols let \(r=1/q\), \(p=(q-1)/q\). For \(1\le k\le j-1\), the alternating interval of length \(k+1\) ending at \(j\) occurs with probability \(p r^{k-1}\). Thus
\[\Pr(R_j\ge k)=p r^{k-1},\quad \mathbb ER_j=1-r^{j-1},\quad
\operatorname{Var}(R_j)=V_{j,q},\]
where the last identity follows by evaluating \(\mathbb E R_j^2=\sum_{k=1}^{j-1}(2k-1)\Pr(R_j\ge k)\). Given all symbols through position \(j\), the conditional mean of \(R_{j+1}\) is
\[\mathbb E(R_{j+1}\mid X_1,\ldots,X_j)=p+rR_j.\]
Indeed a repeated last symbol resets to zero, an appropriate penultimate-symbol append extends a nontrivial suffix, and each of the remaining choices creates one interval. Repeated conditional expectation gives
\[\operatorname{Cov}(R_i,R_j)=r^{j-i}V_{i,q}\quad(1\le i\le j\le n).\]
Summation over all pairs of indices yields the exact variance formula. Since \(V_{i,q}=2/(q-1)+O_q(iq^{-i})\), its leading term is \(2n/(q-1)\) times \(1+2/(q-1)\), with a uniformly bounded remainder, yielding the displayed coefficient \(2(q+1)/(q-1)^2\).

**Step 4 — Gaussian limit.** The nonnegative integer process \((R_j)\) is a Markov chain: from \(R_j=0\) it moves to zero with probability \(1/q\) and to one otherwise; from \(R_j=t\ge1\), it moves to zero with probability \(1/q\), to \(t+1\) with probability \(1/q\), and to one with probability \((q-2)/q\). Every state has a common atom at zero with probability \(1/q\), hence the chain is uniformly mixing and has a unique stationary distribution with \(\Pr(R\ge k)=p r^{k-1}\). Its stationary variance is \(2/(q-1)\). Define the martingale differences
\[\varepsilon_j=R_j-p-rR_{j-1}\quad(j\ge2).\]
They have mean zero conditional on the past and stationary mean-square
\[v_q=\mathbb E\varepsilon_j^2=(1-r^2)\operatorname{Var}(R)=\frac{2(q+1)}{q^2}.\]
The common reset atom gives convergence of Markov time averages from the initial state \(R_1=0\); hence the average conditional quadratic variation of these differences converges in probability to \(v_q\). Their fourth moments are uniformly bounded by the geometric suffix tail, so the martingale Lindeberg condition holds. The martingale central limit theorem gives \(n^{-1/2}\sum_{j=2}^n\varepsilon_j\Rightarrow\mathcal N(0,v_q)\). Iterating the linear recursion and summing gives the exact identity
\[
\Delta(X)-\mathbb E\Delta(X)
=\frac{1}{1-r}\sum_{j=2}^n\left(1-r^{n-j+1}\right)\varepsilon_j.
\]
The weighted correction relative to \((1-r)^{-1}\sum_{j=2}^n\varepsilon_j\) has bounded second moment by orthogonality of martingale differences and the geometric weights. After division by \(\sqrt n\) it vanishes in probability; the claimed normal variance \(v_q/(1-r)^2=2(q+1)/(q-1)^2\) follows.

## Verification
Run `python3 checker.py` using Python 3 and only its standard library. It independently builds the full graph by deletion-set intersections, checks every resulting degree against alternating-interval counting, and compares complete degree histograms to the recurrence for all \(q=2, n\le9\), \(q=3,n\le6\), and \(q=4,n\le5\), totaling \(3478\) vertex instances over those settings. It separately checks exact rational means and variances against recurrence coefficients for \(2\le q\le7\) and \(1\le n\le23\). All tests passed in the packaged source before acceptance. These finite computations test, but do not replace, the all-length proof and Markov/martingale limit argument.

## Relationship to prior work
The 2026 study by Wang–Li–Fu motivates deletion-ball intersection reconstruction problems but addresses extremal multi-deletion overlap rather than random vertices of the one-deletion two-read graph. Cai–Kiah–Nguyen–Yaakobi (2020), Proposition 9, already supplies the Type-A intersection characterization, used in Step 1. A public 2026 result determines the exact total number of graph edges, and therefore the mean degree appearing above; that scalar does not determine the degree polynomial or its variance and limit law. The principal additional mathematical work is the suffix-state weighted counting and the explicit covariance and martingale calculations. General results about finite-state additive functionals may imply a qualitative central limit theorem but do not by themselves identify this graph's all-length degree distribution and its exact dispersion coefficient.

## Limitations
This is a self-reviewed theorem, not independent mathematical validation. Possible unindexed previous formulas for alternating interval counts or stochastic pattern functionals remain a historical-priority risk. No claim is made about code optimality, degree-sensitive bounds beyond those automatically available from a known degree distribution, larger deletion radii, or growing alphabet sizes. One closely related public research result was compared through its descriptive record but not its entire underlying technical manuscript.

## References
1. X. Wang, H. Li and F.-W. Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels*, arXiv:2609.16837, first public September 15, 2026. https://arxiv.org/abs/2609.16837
2. K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376, first public January 6, 2020, especially Definition 8 and Proposition 9. https://arxiv.org/abs/2001.01376
3. N. Chrisnata, H. M. Kiah and E. Yaakobi, *Optimal Reconstruction Codes for Deletion Channels*, arXiv:2004.06032, first public April 13, 2020. https://arxiv.org/abs/2004.06032
4. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, public research record, October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91
