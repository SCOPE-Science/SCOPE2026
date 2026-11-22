# A Weibull first-singleton age and a Poisson birth frontier in site-percolated recursive trees

## Finding

Fix a site-retention probability \(p\in(0,1)\). In a uniform random recursive tree on birth labels \(1,\ldots,n\), retain every vertex independently with probability \(p\), delete the other vertices and their incident edges, and write \(J_{n,j}=1\) if the retained vertex \(j\) is an isolated (one-vertex) component. Put \(b_n=n^{p/(1+p)}\). Then the birth-label point process of isolated retained vertices converges vaguely on \([0,\infty)\):

\[
\Xi_n:=\sum_{j=1}^{n}J_{n,j}\,\delta_{j/b_n}\ \xRightarrow[n\to\infty]{\mathrm{vague}}\ \operatorname{PPP}\bigl(p(1-p)x^p\,dx\bigr).
\tag{1}
\]

Let \(M_{n,k}\) be the \(k\)-th smallest birth label of a retained singleton, assigning \(+\infty\) if fewer than \(k\) exist. For every fixed \(k\ge1\),

\[
\frac{p(1-p)}{1+p}\left(\frac{M_{n,k}}{b_n}\right)^{1+p}\ \xRightarrow[n\to\infty]{}\ \operatorname{Gamma}(k,1),
\tag{2}
\]

jointly at any fixed finite collection of ranks as arrival times of a unit-rate Poisson process. In particular, for every \(x\ge0\),

\[
\lim_{n\to\infty}\Pr\{M_{n,1}>xb_n\}
=\exp\left[-\frac{p(1-p)}{1+p}x^{1+p}\right].
\tag{3}
\]

An exact finite input, valid for \(2\le j\le n\), is
\[
\Pr\{J_{n,j}=1\}=p(1-p)\prod_{t=j}^{n-1}\left(1-\frac{p}{t}\right)
=p(1-p)\frac{\Gamma(n-p)\Gamma(j)}{\Gamma(n)\Gamma(j-p)}.
\tag{4}
\]
The root has probability \(p\prod_{t=1}^{n-1}(1-p/t)\) of being an isolated retained vertex. Empty products are one.

## Assumptions and scope

For each \(t=2,\ldots,n\), vertex \(t\) independently selects one parent uniformly from \(1,\ldots,t-1\). Independently of all parent choices, each vertex is retained with independent probability \(p\). An isolated *retained* vertex is allowed to have children in the original tree, but all of its original neighbors must be deleted. The root is included. The parameter \(p\) is held fixed strictly between zero and one, and all order-statistic ranks are fixed as \(n\) tends to infinity. Vague point-process convergence concerns bounded birth-label windows after the specified rescaling. There is no claim uniform in the retention parameter or valid at \(p=0,1\).

## Proof

**1. One-vertex probabilities and scale.** For a nonroot vertex \(j\), the vertex itself must be retained, its parent must be deleted, and each later vertex \(t>j\) must not be simultaneously retained and attached to \(j\). The first two factors have probability \(p(1-p)\), and the independent later restrictions each have probability \(1-p/(t-1)\). This proves (4). The root has no parent and obeys the displayed root formula. For fixed \(0<\epsilon<T<\infty\), standard uniform Gamma-ratio asymptotics give
\[
\sup_{\epsilon b_n\le j\le Tb_n}\left|\frac{\prod_{t=j}^{n-1}(1-p/t)}{(j/n)^p}-1\right|\longrightarrow0.
\tag{5}
\]
Since \(b_n^{1+p}=n^p\), summing (4) over a window \((u b_n,v b_n]\) yields
\[
\sum_{ub_n<j\le vb_n}\Pr(J_{n,j}=1)
\longrightarrow p(1-p)\int_u^v x^p\,dx
\quad(0<u<v<\infty).
\tag{6}
\]

**2. Exact multi-vertex conditional representation.** Fix any set \(S=\{s_1<\cdots<s_r\}\subset\{2,\ldots,n\}\) with fixed size \(r\). Force the marked vertices in \(S\) to be retained, contributing a factor \(p^r\). For each \(t\notin S\), let \(X_t\) be its independent Bernoulli-\(p\) retention indicator. Define \(m_t=\#\{s\in S:s<t\}\) and \(C_{s-1}=\sum_{t<s,\ t\notin S}(1-X_t)\). Conditional on these indicators, the marked vertex \(s\) chooses a deleted parent with probability \(C_{s-1}/(s-1)\); each unmarked retained vertex \(t\ge2\) avoids all \(m_t\) already marked vertices with probability \(1-m_t/(t-1)\). These parent choices are mutually independent, so the *exact* joint probability is
\[
\Pr\{J_{n,s}=1\text{ for all }s\in S\}
=p^r\,\mathbb E\left[
\prod_{s\in S}\frac{C_{s-1}}{s-1}\cdot
\prod_{\substack{t\notin S\\2\le t\le n}}
\left(1-\frac{m_t X_t}{t-1}\right)
\right].
\tag{7}
\]
No independence between the singleton indicators themselves is asserted.

**3. Uniform rare-event factorization.** Put \(B=\prod_{t\notin S,\ t\ge2}(1-m_tX_t/(t-1))\). Independence of the \(X_t\) gives
\[
\mathbb EB=\prod_{\substack{t\notin S\\t\ge2}}\left(1-\frac{p m_t}{t-1}\right).
\tag{8}
\]
Suppose \(\epsilon b_n\le s_1<\cdots<s_r\le Tb_n\) for fixed \(r,\epsilon,T,p\). Then \(m_t\le r\) and all nonzero factors in (8) start at \(t>s_1\). Taylor's bound for \(\log(1-z)\), with each \(z=O_{p,r}(1/s_1)\), implies
\[
\log\mathbb EB-
\sum_{s\in S}\sum_{t=s}^{n-1}\log(1-p/t)=O_{p,r}(s_1^{-1}).
\tag{9}
\]
Indeed the log discrepancy at an unmarked time is \(O_{p,r}(t^{-2})\), and omitting the at most \(r\) marked times produces \(O_{p,r}(s_1^{-1})\). Hence, if \(f_n(s)=\prod_{t=s}^{n-1}(1-p/t)\), then
\[
\mathbb EB=\prod_{s\in S}f_n(s)\,[1+O_{p,r,\epsilon,T}(b_n^{-1})].
\tag{10}
\]

For sufficiently large \(n\), \(\mathbb EB>0\). Tilting the independent Bernoulli law by density \(B/\mathbb EB\) yields a product law \(Q\) in which, for \(t\notin S\), \(t\ge2\),
\[
Q(X_t=1)=\frac{p(1-m_t/(t-1))}{1-pm_t/(t-1)}.
\tag{11}
\]
The site \(t=1\) retains its original Bernoulli law. For every marked \(s\in[\epsilon b_n,Tb_n]\), the numerator \(C_{s-1}\) is a sum of independent, bounded variables under \(Q\). Since (11) differs from \(p\) by at most \(O_{p,r}(1/t)\), we have
\[
\mathbb E_Q\left|\frac{C_{s-1}}{s-1}-(1-p)\right|
=O_{p,r,\epsilon,T}(b_n^{-1/2}).
\tag{12}
\]
The mean bias is bounded by \(O_{p,r}(\log s/s)\) and the standard deviation by \(O(s^{-1/2})\). All fractions \(C_{s-1}/(s-1)\) lie in \([0,1]\), so the elementary telescoping inequality for products and (12) show that the expectation under \(Q\) of their product equals \((1-p)^r+O_{p,r,\epsilon,T}(b_n^{-1/2})\). Combining this with (7) and (10) establishes, **uniformly in all such marked subsets**, 
\[
\Pr\{J_{n,s}=1\text{ for all }s\in S\}
= [p(1-p)]^r\prod_{s\in S}f_n(s)
\bigl[1+O_{p,r,\epsilon,T}(b_n^{-1/2})\bigr].
\tag{13}
\]
The relative form is legitimate since \(1-p>0\) is fixed.

**4. Poisson point process and the left boundary.** In any finite collection of disjoint intervals inside \((0,\infty)\), (5), (6), and uniform factorization (13) imply convergence of all mixed factorial moments of the corresponding singleton counts to those of independent Poisson variables with means \(p(1-p)\int x^p\,dx\). These moments identify the joint Poisson law; the bounded-window first moments give tightness. Equivalently the Laplace functionals of compactly supported nonnegative continuous functions away from zero converge to those of the Poisson process in (1), by their factorial expansions and a standard truncation argument using factorial moments. At the origin, the product bound \(f_n(j)\le(j/n)^p\), (4), and the root formula show for every fixed \(\epsilon>0\)
\[
\limsup_{n\to\infty}\mathbb E\Xi_n([0,\epsilon])
\le \frac{p(1-p)}{1+p}\epsilon^{1+p}.
\tag{14}
\]
Letting \(\epsilon\downarrow0\) extends the convergence to the locally compact space \([0,\infty)\), proving (1).

**5. Earliest singleton ranks.** The intensity measure of the limit on \([0,x]\) is \(\Lambda(x)=p(1-p)x^{1+p}/(1+p)\). The limiting point process is simple, has no atom at a deterministic boundary, and has \(\Lambda(x)\to\infty\) as \(x\to\infty\). The continuous mapping from point configurations to their first fixed number of birth labels therefore yields (2) and (3). The mapping \(x\mapsto\Lambda(x)\) transforms the limiting process into a unit-rate homogeneous Poisson process, whose arrival times have the asserted Gamma laws.

## Verification

The standalone standard-library script `verify.py` independently enumerates every recursive-tree parent assignment and every site-retention mask for sizes \(2\) through \(7\), checking all singleton and pair/triple singleton probabilities at retention probabilities \(1/3\), \(1/2\), and \(2/3\). It compares brute-force results to the exact conditional formula (7) and the finite marginal formula (4). Four further large-size computations check the first-moment scaling in (6). The delivered script passes 544 assertions/comparisons. These finite calculations verify only finite identities and numerical consistency; they are not proofs of the infinite-dimensional point-process convergence. Steps 1–5 give the all-size analytic derivation and asymptotic argument. Run `python3 verify.py` from the directory containing this file.

## Relationship to prior work

Kalay and Ben-Naim [1] investigate fragmentation of uniform recursive trees and fragment-size distributions under random deletions, but do not give the first birth label or point process of isolated retained vertices. The more recent independent-site model of Gu and Yuan [2] has a cluster-size law of large numbers and a global singleton density, which agrees with the sum of (4); those global statistics do not determine the earliest singleton label, the age exponent, or joint rare-age distribution. The known oldest-leaf birth-label Poisson theorem [3] concerns vertices with **no children at all** in the original tree and uses a square-root birth scale, whereas a site-isolated vertex may have deleted children and must additionally have a deleted parent. Its theorem cannot be applied by a mere thinning or substitution. Janson's degree-profile results [4] concern global recursive-tree degree counts rather than age-resolved site-isolation events. Earlier one-label increasing-tree degree laws [5] do not settle the simultaneous rare-event configuration. The Poisson frontier (1), parameter-dependent age exponent, and Weibull first-label law are the specific assertions evaluated here, rather than a generic assertion of uniqueness of all moment formulas.

## Limitations

The result assumes independent Bernoulli vertex retention with fixed \(p\in(0,1)\) and a uniformly chosen older parent for each new vertex. It is not a result for edge percolation, a fixed number of deleted vertices, or preferential attachment, and it gives no convergence rate or uniform theory at \(p\to0\) or \(p\to1\). The theorem does not describe component sizes beyond singletons. Although the specified primary papers and closely related indexed findings were checked, unidentified equivalent joint-rare-event theorems remain a historical-priority risk. No independent mathematical validation is asserted.

## References

1. Z. Kalay and E. Ben-Naim, *Fragmentation of Random Trees*, arXiv:1409.7106, first made public 24 September 2014; https://arxiv.org/abs/1409.7106; full manuscript: https://cnls.lanl.gov/~ebn/pubs/treefrag/treefrag.pdf.
2. C. Gu and L. Yuan, *Size distribution of clusters in site-percolation on random recursive tree*, arXiv:2408.12515, first made public 22 August 2024; https://arxiv.org/pdf/2408.12515, especially the cluster-size transition mechanism and main limit theorems.
3. *The oldest leaves of random recursive trees form a Poisson point process*, public mathematical note, 18 October 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-oldest-leaves-of-random-recursive-trees-form-a-poisson-point--0a1a1c4bbf35, particularly the joint leaf formula and earliest-leaf theorem.
4. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83; DOI 10.1002/rsa.20046.
5. M. Kuba and A. Panholzer, *On the degree distribution of the nodes in increasing trees*, Journal of Combinatorial Theory A 114 (2007), 597–618; https://www.dmg.tuwien.ac.at/kuba/nodedegree3.pdf.
