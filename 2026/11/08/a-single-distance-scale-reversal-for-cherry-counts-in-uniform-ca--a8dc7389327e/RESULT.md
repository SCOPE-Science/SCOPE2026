# A single distance-scale reversal for cherry counts in uniform Cayley trees

## Finding
Let \(T_n\) be uniform among the \(n^{n-2}\) labeled trees on \([n]\). Write \(C_n\) for the number of unordered pairs of leaves having a common neighbor (a center can contribute more than one such pair), and \(M_{n,k}\) for the number of unordered vertex pairs at graph distance \(k\).

For \(n\ge4\), set
\[p_{m,k}=\frac{(k+1)(m-2)_{\underline{k-1}}}{m^k}\quad(1\le k<m),\qquad p_{m,k}=0\quad\text{otherwise},\]
where the falling factorial of length zero is one. Put
\[c_n=\frac{\binom n2(n-2)^{n-3}}{n^{n-2}}.\]
Then \(\mathbb E C_n=c_n\), \(\mathbb E M_{n,k}=\binom n2p_{n,k}\), \(\operatorname{Cov}(C_n,M_{n,1})=0\), and for \(2\le k\le n-1\),
\[\boxed{\operatorname{Cov}(C_n,M_{n,k})=c_n\left(\binom{n-2}{2}p_{n-2,k}+2(n-3)p_{n-2,k-1}+\mathbf1_{\{k=2\}}-\binom n2p_{n,k}\right).}\]
The sign is positive at shell \(k=2\), negative at \(k=n-1\), and switches **exactly once** from positive to negative as the shell index increases, allowing at most one intervening zero integer shell. If \(k_n^-\) denotes the first negative shell, then
\[\frac{k_n^-}{\sqrt n}\longrightarrow\sqrt2.\]
For each nondecreasing \(f:\{1,\dots,n-1\}\to\mathbb R\),
\[\operatorname{Cov}\!\left(C_n,\sum_{u<v}f(d_T(u,v))\right)\le0,\]
with strict inequality when \(f\) is strictly increasing; in particular \(\operatorname{Cov}(C_n,\operatorname{Wie}(T_n))<0\), where \(\operatorname{Wie}(T)=\sum_{u<v}d_T(u,v)\).

## Assumptions and scope
The tree is unrooted and uniformly labeled, not a uniformly chosen binary phylogenetic tree, recursive tree, or preferential-attachment tree. There are no random edge lengths. A cherry is an unordered *pair* of degree-one neighbors of a common center; a center with \(r\) leaf neighbors contributes \(\binom r2\). All formulas hold for every integer \(n\ge4\). The asymptotic statement concerns \(n\to\infty\) with distance on the square-root scale; no central limit theorem or concentration statement is asserted.

## Proof
**1. Fixed path and marked-cherry counts.** For distinct fixed vertices \(u,v\), the path \(u\to v\) has length \(k\) with probability \(p_{n,k}\). Indeed, choose its \(k-1\) internal vertices in order in \((n-2)_{\underline{k-1}}\) ways. The forest-extension form of Cayley's formula counts \((k+1)n^{n-k-2}\) trees containing that fixed path. Division by \(n^{n-2}\) proves the formula, including the terminal case \(k=n-1\).

Mark an unordered cherry pair \(\{a,b\}\) and its unique common center \(c\). Deleting \(a,b\) leaves an arbitrary tree on the other \(n-2\) vertices, and \(c\) may be any of these vertices. Conversely any such tree and marked center determines exactly one marked-cherry tree. Hence the number of marked-cherry trees is \(\binom n2(n-2)^{n-3}\). Under cherry size bias, the residual tree is a uniform Cayley tree of order \(n-2\), and the center is uniform over its vertices.

**2. Conditional distance-shell expectation.** Each old-old vertex pair contributes the ordinary \(\binom{n-2}2p_{n-2,k}\). Each new leaf has distance one from the uniformly marked center, and distance \(k\ge2\) from a different old vertex with expected multiplicity \((n-3)p_{n-2,k-1}\). The two new leaves form one additional distance-two pair. Therefore, writing \(\mu_{n,k}\) for the expectation in the cherry-size-biased tree,
\[\mu_{n,k}=\binom{n-2}2p_{n-2,k}+2(n-3)p_{n-2,k-1}+\mathbf1_{\{k=2\}}\quad(k\ge2),\]
whereas \(\mu_{n,1}=n-1\). By the definition of size bias,
\[\operatorname{Cov}(C_n,M_{n,k})=\mathbb E C_n\left(\mu_{n,k}-\mathbb E M_{n,k}\right).\]
This gives the exact formula and the zero first shell, since every tree has exactly \(n-1\) edges.

**3. One sign reversal.** Let \(\Delta_{n,k}=\mu_{n,k}-\binom n2p_{n,k}\). At distance two, direct simplification yields
\[\Delta_{n,2}=\frac{2(n-3)(n-1)}{n(n-2)}>0.\]
At distance \(n-1\), the cherry-conditioned tree cannot be a path, so \(\Delta_{n,n-1}=-\binom n2p_{n,n-1}<0\). For \(3\le k\le n-2\), cancellation of falling factorials shows that the sign is that of \(H_n(k)-1\), where
\[H_n(x)=\frac{(n-x-1)(n-x+2-4/(x+1))}{n(n-1)((n-2)/n)^x}\quad(3\le x\le n-2).\]
Both factors in its numerator are positive on this interval. Since \(\log(n-x-1)\) is strictly concave and \(n-x+2-4/(x+1)\) is positive and strictly concave, \(\log H_n(x)\) is strictly concave; the denominator contributes only a linear term to its logarithm. Moreover
\[H_n(3)-1=\frac{n^2-8n+4}{(n-2)^2(n-1)}>0\quad(n\ge8).\]
At the right endpoint, the numerator is less than four while the denominator exceeds four: indeed \(((n-2)/n)^{n-2}\ge e^{-2}\), so \(n(n-1)((n-2)/n)^{n-2}\ge n(n-1)e^{-2}>4\) for \(n\ge8\). Thus \(H_n(n-2)<1\). Strict log concavity means the superlevel set \(\{x:H_n(x)\ge1\}\) is an interval: beginning strictly above one and ending strictly below one, it has a single crossing, with at most one integer zero. For \(4\le n\le7\), the formula directly gives \(\Delta_{n,2}>0\) and \(\Delta_{n,k}<0\) for every \(3\le k<n\), which is also independently checked in the attached exact enumerator.

For fixed \(t>0\) and \(x=t\sqrt n\), direct expansions of the two factors and the exponential give
\[H_n(t\sqrt n)=1+\frac{2-t^2}{n}+o(n^{-1}).\]
Therefore the first negative shell tends to \(\sqrt{2n}\) in ratio, by the established unique crossing.

**4. Monotone-distance functionals.** The exact identity \(\sum_{k=1}^{n-1}M_{n,k}=\binom n2\) implies \(\sum_k\operatorname{Cov}(C_n,M_{n,k})=0\). Since the shell covariances have one positive-to-negative transition, a nondecreasing sequence \(f(k)\) has nonpositive covariance-weighted sum. It is strictly negative for strictly increasing \(f\), because shell two is strictly positive and the terminal shell strictly negative. This yields the Wiener-index assertion.

## Verification
The standalone pure-Python script `check_cherry_distance.py` independently constructs every labeled tree using Prüfer codes for \(n=4,5,6,7\) (18,244 trees in total), measures cherries and all-pairs distances directly, and compares exact rational covariances to the formula for every shell. It also checks the exact shell identities, sign sequence, and Wiener-index negativity for each integer size \(4\le n\le200\). Its output reports PASS. Enumeration confirms finite instances but does not replace the all-order forest-extension, log-concavity, and asymptotic proofs above.

## Relationship to prior work
Aldous and Pitman's 1998 report establishes a family of random labeled trees and tree-structure enumeration. The broad random-tree distance-profile work of Berzunza Ojeda and Janson studies scaling limits and leaf-size bias, not the exact cherry-count shell covariance here. A separate literature on leaf-to-leaf distances and tree extremal indices considers different objects and optimizations. Relevant published results on marked endpoints concern their degrees conditioned on their distance, whereas the current statistic counts *sibling leaf pairs anywhere* against *all vertex-pair distances*; one endpoint's degree is not the cherry statistic. Existing elementary fixed-path and marked-leaf identities are inputs, not claimed as new findings. This is a best-knowledge priority comparison, not proof of absolute historical novelty.

## Limitations
The theorem makes no claim for different tree distributions or edge-weight laws. The cutoff is asymptotic rather than an elementary closed-form integer expression at every order, and an integer shell may have zero covariance. Stronger distributional dependence or independence of statistics is not asserted. Historical coverage inside older specialized enumerative sources cannot be excluded without independent review.

## References
- D. Aldous and J. Pitman, *A family of random trees with random edge lengths*, Berkeley Technical Report 526 (June 1, 1998), https://live-statistics.pantheon.berkeley.edu/tech-reports/526.
- G. Berzunza Ojeda and S. Janson, *The distance profile of rooted and unrooted simply generated trees*, arXiv:2009.00572 (2020), https://arxiv.org/abs/2009.00572.
- L. A. Székely, H. Wang, and T. Wu, *The sum of the distances between the leaves of a tree and the semi-regular property*, Discrete Mathematics 311 (2011), 1197–1203, https://doi.org/10.1016/j.disc.2010.06.005.
- Cayley's labeled-tree formula and the standard rooted-forest extension (classical enumerative identities).
