# Logarithmically separated Poisson birth frontiers for fixed offspring degrees

## Finding

Let \(T_n\) be the **uniform random recursive tree** with vertex labels \(1,\ldots,n\): independently for every \(j=2,\ldots,n\), vertex \(j\) selects its parent uniformly from \(1,\ldots,j-1\). Let \(D_{n,i}\) be the number of **direct children**, not all descendants, of vertex \(i\). For each fixed nonnegative integer \(r\), put
\[
 a_{n,r}=\sqrt{\frac{n}{(\log n)^r}},\qquad
 \Xi_{n,r}=\sum_{i=1}^{n}\mathbf 1\{D_{n,i}=r\}\,\delta_{i/a_{n,r}}.
\]
For every fixed integer \(K\geq1\), the random point measures \((\Xi_{n,0},\ldots,\Xi_{n,K})\) converge **jointly** in the product vague topology on locally finite measures on \([0,\infty)\) to *independent* inhomogeneous Poisson point processes \((\Xi_0,\ldots,\Xi_K)\) with respective intensities
\[
 \nu_r(dx)=\frac{x}{2^r r!}\,dx,\qquad r=0,\ldots,K.
\]
In particular, writing \(M_{n,r}=\min\{i:D_{n,i}=r\}\), with the minimum of an empty set defined as \(+\infty\), for every \(t\geq0\),
\[
 \lim_{n\to\infty}\Pr\!\left\{\frac{M_{n,r}}{a_{n,r}}>t\right\}
 =\exp\!\left(-\frac{t^2}{2^{r+1}r!}\right).
\]
Thus the earliest vertex with exactly \(r\) children has birth rank of order \(\sqrt n/(\log n)^{r/2}\). Different fixed offspring degrees have **asymptotically independent first-arrival positions on their own, logarithmically separated scales**. As a further consequence, for any fixed \(K\geq1\), the earliest vertex with **at most** \(K\) children has exactly \(K\) children with probability tending to one, and its scaled label has the same displayed limiting survival law with \(r=K\).

## Assumptions and scope

The tree is grown with one independent, uniformly chosen earlier parent for each vertex; no preferential attachment, multiple parents, conditioning on degree totals, or deterministic prescribed degree sequence is allowed. All limits hold for fixed \(K\) and fixed offspring degrees as \(n\to\infty\). Natural logarithms are used. Processes with different \(r\) are rescaled by different deterministic factors \(a_{n,r}\). In particular, the statement does **not** claim independent offspring counts at finite \(n\), uniformity when \(r\) grows with \(n\), or convergence of unscaled global degree counts to Poisson laws.

## Proof

**1. Exact finite-dimensional marked generating function.** Fix \(m\) distinct birth labels \(i_1,\ldots,i_m\), and let \(A_j=\{k:i_k<j\}\), \(d_j=|A_j|\). Independence of parent selections gives the exact multivariate probability generating function
\[
 F_n(z_1,\ldots,z_m)
 =\mathbb E\prod_{k=1}^m z_k^{D_{n,i_k}}
 =\prod_{j=2}^n\left(1-\frac{d_j}{j-1}+
 \frac{\sum_{k\in A_j}z_k}{j-1}\right).
 \tag{1}
\]
This identity also covers finite \(n\) without asymptotic approximations.

**2. A uniform rare-degree estimate.** Fix \(m\) and fixed requested degrees \(r_1,\ldots,r_m\). Suppose every selected label satisfies
\[
 \delta a_{n,s_k}\leq i_k\leq T a_{n,s_k},
 \quad s_k\in\{0,\ldots,K\},\quad 0<\delta<T<\infty.
 \tag{2}
\]
The \(s_k\) designate the scales, and may differ from the requested degrees during this intermediate calculation. In the application they equal \(r_k\). Under (2), the minimum selected label tends to infinity, and
\(\log(n/i_k)=(1/2+o(1))\log n\) uniformly.

For large enough \(n\), \(j-1>d_j\) whenever \(d_j>0\). Put
\[
 B_n=\prod_{j=2}^n\left(1-\frac{d_j}{j-1}\right),\qquad
 b_j=\frac1{j-1-d_j},\qquad
 L_k=\sum_{j>i_k}b_j.
\]
Then (1) becomes
\[
 F_n(z)=B_n\prod_{j=2}^n\left(1+b_j\sum_{k\in A_j}z_k\right).
 \tag{3}
\]
Since \(d_j\leq m\), elementary logarithmic expansion, the harmonic-sum estimate, and \(\sum_{j>i_{\min}}j^{-2}=O(i_{\min}^{-1})\) yield, uniformly under (2),
\[
 B_n=\prod_{k=1}^m\frac{i_k}{n}\,(1+o(1)),\qquad
 L_k=\log(n/i_k)+O_m(i_{\min}^{-1}).
 \tag{4}
\]
To extract the coefficient of \(\prod_k z_k^{r_k}\) from the remaining product in (3), independently draw \(r_k\) indices \(j>i_k\), each with probability \(b_j/L_k\), for each color \(k\). The coefficient is **exactly**
\[
 \left(\prod_{k=1}^m\frac{L_k^{r_k}}{r_k!}\right)
 \Pr\{\text{all these }\sum_k r_k\text{ drawn indices are distinct}\}.
 \tag{5}
\]
Indeed, assigning two draws to the same parent-choice step would be forbidden by the linear-in-\(z\) factor in (3); distinct assignments have the required coefficient, with the factorials removing within-color ordering. For two draws, the collision probability is bounded by
\[
 \frac{\sum_{j>i_{\min}} b_j^2}{L_kL_\ell}
 =O_{m,K,\delta,T}\!\left(\frac1{i_{\min}(\log n)^2}\right).
\]
A finite union bound in (5) shows that the distinctness probability is \(1-o(1)\). Consequently, uniformly over all distinct marks satisfying (2),
\[
 \Pr\{D_{n,i_k}=r_k\text{ for all }k\}
 =(1+o(1))\prod_{k=1}^m
 \frac{i_k}{n}\frac{(\log(n/i_k))^{r_k}}{r_k!}.
 \tag{6}
\]
This multiplicative estimate is stronger than separate marginal convergence and controls the cross-degree dependence.

**3. Joint Poisson convergence away from the origin.** Let \(r\in\{0,\ldots,K\}\) and let \(I\) be a bounded interval with closure contained in \((0,\infty)\). For labels \(i/a_{n,r}\in I\), (6) gives
\[
 \Pr\{D_{n,i}=r\}
 =(1+o(1))\frac{i}{2^r r!\,a_{n,r}^2}.
 \tag{7}
\]
Therefore
\[
 \sum_{i:\,i/a_{n,r}\in I}\Pr\{D_{n,i}=r\}
 \longrightarrow\int_I\frac{x}{2^r r!}\,dx.
 \tag{8}
\]
To calculate arbitrary joint factorial moments of the counts on a finite collection of disjoint intervals, expand into sums over distinct physical birth labels. For equal degree classes, disjoint intervals already force distinct labels. For distinct classes \(r<s\), their compactly rescaled label ranges are eventually disjoint because
\[
 \frac{a_{n,r}}{a_{n,s}}=(\log n)^{(s-r)/2}\longrightarrow\infty.
\]
Thus (6) applies uniformly to every term of the factorial-moment expansion. The moments factorize into products of the limiting intensities in (8), exactly the mixed factorial moments of independent Poisson counts. These moments determine the joint distribution (the associated factorial-moment generating function is entire near the origin), yielding independent Poisson processes on compact subintervals of \((0,\infty)\).

**4. No loss of points at zero.** For \(i\geq2\), the independent parent choices give the exact zero-child probability and the coefficient estimate
\[
 \Pr\{D_{n,i}=r\}
 =\frac{i-1}{n-1}
 e_r\left(\frac1{i-1},\frac1i,\ldots,\frac1{n-2}\right)
 \leq\frac{i-1}{n-1}\frac{(H_{n-2}-H_{i-2})^r}{r!},
 \tag{9}
\]
where \(e_0=1\), \(e_r\) is the elementary symmetric polynomial, and the list is empty when \(i=n\). For the root, its compulsory child \(2\) yields
\(\Pr\{D_{n,1}=r\}\leq (n-1)^{-1}H_{n-2}^{r-1}/(r-1)!\) for \(r\geq1\), while \(\Pr\{D_{n,1}=0\}=0\) for \(n\geq2\). Summing (9) over \(2\leq i\leq\delta a_{n,r}\), and using \(H_{n-2}-H_{i-2}\leq\log n+O(1)\), gives
\[
 \limsup_{n\to\infty}\mathbb E\Xi_{n,r}([0,\delta])
 \leq C_r\delta^2.
 \tag{10}
\]
The root contribution tends to zero. Letting \(\delta\downarrow0\) extends joint point-process convergence to \([0,\infty)\).

**5. Earliest arrivals and the degree hierarchy.** The limiting Poisson process has no point exactly at \(t\), and its mass on \([0,t]\) is \(t^2/(2^{r+1}r!)\). The zero-count probability therefore yields the stated first-birth survival law and joint independence of the first-birth limits across fixed degrees. For \(r<K\), the same upper estimate as in (10), summed only to \(Ta_{n,K}\), gives
\[
 \Pr\{\exists i\leq Ta_{n,K}:D_{n,i}=r\}
 =O_{r,K,T}((\log n)^{r-K})\longrightarrow0.
\]
With arbitrarily high probability for sufficiently large \(T\), some degree-\(K\) vertex occurs by \(Ta_{n,K}\), by its nondegenerate Poisson first-arrival law. Hence the first vertex having at most \(K\) children has exactly \(K\) children with probability tending to one. This completes the proof.

## Verification

The standalone file `verify.py` contains an independent finite dynamic-programming implementation of (1), compared with exhaustive enumeration of parent-choice sequences through eight vertices. It also checks the individual Bernoulli-factor marginals and the exact leaf formula, and computes numerical first-moment diagnostics on the claimed scales. Run `python verify.py` in a Python 3 environment with only the standard library. Exact finite checks support (1) and (9), while the uniform asymptotic estimates and factorial-moment argument above supply the infinite proof.

## Relationship to prior work

The classical global fixed-degree laws and asymptotic normality in Janson (2004) and Holmgren–Janson (2014) describe counts of each outdegree over **all** labels, with linear means and square-root fluctuations; they do not establish the early-birth frontiers at \(\sqrt n/(\log n)^{r/2}\). Kuba–Panholzer (2006 online) give exact laws and limit regimes for the offspring count at a **prescribed** birth label, which supply important single-label background but not the simultaneous rare-event process. The previously established first-leaf process concerns \(r=0\) and has the \(\sqrt n\) scaling; it is recovered here. The new mathematical contribution is the multi-degree logarithmic hierarchy, independent Poisson limits on distinct scales, and the earliest-\(\leq K\) degree selection law. The result concerns direct children and is distinct from early **fringe-subtree size** processes, whose marks depend on all descendants.

## Limitations

The theorem is asymptotic for fixed finite degrees and a fixed finite number of color classes. No quantitative total variation rate, growing-degree regime, or finite-sample independence is asserted. Full-text comparison was possible for Kuba–Panholzer and the relevant sections of Holmgren–Janson; Janson's 2004 article was accessible through its abstract and references rather than complete article text. The possibility of an older equivalent birth-rank process theorem not found in the checked literature is a historical-priority uncertainty. No independent mathematical review has been performed.

## References

1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83. First published 2004-11-16. https://doi.org/10.1002/rsa.20046
2. M. Kuba and A. Panholzer, *On the degree distribution of the nodes in increasing trees*, Journal of Combinatorial Theory, Series A 114 (2007), 597–618. Online 2006-09-18. https://doi.org/10.1016/j.jcta.2006.08.003
3. C. Holmgren and S. Janson, *Limit laws for functions of fringe trees for binary search trees and recursive trees*, preprint 2014-06-26, arXiv:1406.6883. https://arxiv.org/abs/1406.6883
4. L. Addario-Berry and L. Eslava, *High degrees of random recursive trees*, arXiv:1507.05981 (2015). https://arxiv.org/abs/1507.05981
