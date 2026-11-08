# Age-resolved covariance kernel for intact blocks in random Stirling permutations

## Finding

For every fixed integer \(r\ge2\), a uniform \(r\)-Stirling permutation of order \(n\) has a birth-label-indexed intact-block process with an explicit limiting covariance kernel. Write \(X_{n,i}\) for the indicator that *all* \(r\) copies of symbol \(i\) occur consecutively, and put
\[
W_n(t)=\sum_{i=1}^{\lfloor nt\rfloor}X_{n,i},\qquad 0\le t\le1,
\quad \beta=\frac{r-1}{r}.
\]
Then, for every fixed \(s,t\in[0,1]\),
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(W_n(s),W_n(t))}{n}
=K_r(s,t),
\]
where, with \(\kappa(x,y)=x^\beta y^\beta(1/\max\{x,y\}-1)\) for positive \(x,y\), and zero if either argument is zero,
\[
K_r(s,t)=\int_0^{\min(s,t)}(x^\beta-x^{2\beta})\,dx
-\beta^2\int_0^s\int_0^t\kappa(x,y)\,dy\,dx.
\]
In particular the birth-prefix variance coefficient is explicitly
\[
\boxed{\ K_r(t,t)=\frac{t^{\beta+1}}{\beta+1}
-\frac{2\beta^2+\beta+1}{(\beta+1)(2\beta+1)}t^{2\beta+1}
+\frac{\beta^2}{(\beta+1)^2}t^{2\beta+2}.\ }
\]
For example, at \(r=2\), the full count has \(K_2(1,1)=1/9\), while the formula specifies the nontrivial covariance of *every two age prefixes*, not just the full count.

The finite-size mechanism is an exact joint inclusion formula. For every subset \(S\subseteq\{1,\ldots,n\}\), define \(c_k(S)=|S\cap\{1,\ldots,k-1\}|\). Then
\[
\boxed{\ \Pr\{X_{n,i}=1\text{ for every }i\in S\}
=\prod_{k=2}^{n}\left(1-\frac{(r-1)c_k(S)}{r(k-1)+1}\right).\ }
\]
The formula determines the entire joint law by inclusion-exclusion. It also gives the following local limit: whenever \(i_n/n\to a\), \(j_n/n\to b\), with \(0<a<b<1\),
\[
\lim_{n\to\infty}n\operatorname{Cov}(X_{n,i_n},X_{n,j_n})
=-\beta^2a^\beta b^\beta\left(\frac1b-1\right).
\]

## Assumptions and scope

An \(r\)-Stirling permutation is a word containing exactly \(r\) copies of each value in \(\{1,\ldots,n\}\), such that every letter strictly between two successive copies of \(i\) is greater than \(i\). All such words are equally likely. The parameters \(r,n\) are integers with \(r\ge2\), \(n\ge1\). The limiting statements keep \(r\) fixed as \(n\to\infty\). By *intact block* we mean a run of length exactly \(r\) containing every occurrence of its value, not a plateau-position or a count by occurrence number. The birth-prefix variable \(W_n(t)\) is defined for every real \(t\in[0,1]\). No distributional central limit theorem is claimed.

## Proof

**Uniform insertion representation.** To form the word of order \(k\), insert a contiguous run of \(r\) copies of the new largest letter \(k\) into one of the \(d_k=r(k-1)+1\) gaps of the order-\(k-1\) word. Removal of this run recovers the precursor uniquely. Every choice history therefore gives one distinct valid word and all histories have the same probability. At its birth, label \(i\) forms an intact run. A later insertion can destroy its intactness only by selecting one of its \(r-1\) internal gaps, and once destroyed it can never be restored. If every value in \(S\) born before stage \(k\) is still intact, these vulnerable gaps are distinct (runs of distinct labels are disjoint), and their number is \((r-1)c_k(S)\). Hence the one-step conditional survival probability equals \(1-(r-1)c_k(S)/d_k\). Multiplication over the steps proves the stated inclusion formula, including empty and singleton sets.

**Exact pair structure.** Put \(h_k=(r-1)/(r(k-1)+1)\), and \(p_{n,i}=\Pr(X_{n,i}=1)=\prod_{k=i+1}^{n}(1-h_k)\). For \(1\le i<j\le n\), the joint inclusion formula gives
\[
\operatorname{Cov}(X_{n,i},X_{n,j})
=p_{n,i}p_{n,j}\left(R_{n,j}-1\right),
\quad R_{n,j}=\prod_{k=j+1}^{n}\frac{1-2h_k}{(1-h_k)^2}.
\]
Every factor is in \((0,1)\) when \(k\ge3\). Thus distinct indices have negative covariance for \(j<n\); the last indicator \(X_{n,n}=1\) is deterministic and its covariance is zero. The pair formula also shows that the normalized covariance depends only on the younger label \(j\), a property not visible from unindexed plateau counts.

**Pointwise bulk limits.** Since \(h_k=\beta/k+O_r(k^{-2})\), uniform harmonic-sum estimates on compact subsets of \((0,1]\) show
\[
p_{n,\lfloor nx\rfloor}\longrightarrow x^\beta\qquad(x>0).
\]
For \(j_n/n\to b\in(0,1)\), expanding the logarithm gives
\[
\log R_{n,j_n}
=-\sum_{k=j_n+1}^{n}h_k^2+O_r\left(\sum_{k=j_n+1}^{n}h_k^3\right),
\qquad n(R_{n,j_n}-1)\longrightarrow-\beta^2(1/b-1).
\]
Combining the two asymptotics yields the displayed local covariance limit.

**Covariance-kernel limit and boundary control.** Expand
\[
\operatorname{Cov}(W_n(s),W_n(t))=
\sum_{i\le\lfloor ns\rfloor}\sum_{j\le\lfloor nt\rfloor}
\operatorname{Cov}(X_{n,i},X_{n,j}).
\]
On the diagonal, \(\operatorname{Var}(X_{n,i})=p_{n,i}(1-p_{n,i})\); after division by \(n\), its Riemann sum converges to the first integral of \(K_r\). For distinct indices whose scaled labels stay bounded away from zero, the bulk limit above, applied symmetrically with \(\max\{i,j\}\), gives the double-integral term.

For completeness, the origin poses no hidden mass. For each fixed \(r\), the finite product identity and \(1-\prod a_k\le\sum(1-a_k)\) for \(a_k\in[0,1]\) give
\[
0\le-\operatorname{Cov}(X_{n,i},X_{n,j})
\le p_{n,i}p_{n,j}\sum_{k=\max\{i,j\}+1}^{n}
\frac{h_k^2}{(1-h_k)^2}
\le\frac{C_r}{\max\{i,j\}},\qquad i\ne j.
\]
Here \(C_r\) is a finite constant independent of \(n,i,j\); for \(\max\{i,j\}\ge2\) this follows from a convergent tail of squared reciprocals, and the smallest indices can be absorbed in the constant. In the double sum, the contribution from pairs with \(\min\{i,j\}<\delta n\), after division by \(n\), is \(O_r(\delta)\), since \(\sum_{j\le n} \min\{j,\delta n\}/j=O(\delta n+\delta n\log(1/\delta))\); the latter bound tends to zero with \(\delta\). Diagonal terms in that region contribute at most \(\delta\). Consequently the compact Riemann-sum limit extends to both coordinate axes. The integral defining \(K_r\) is finite, since its only potential singularity near the origin is integrable. This proves the kernel for all \(s,t\in[0,1]\).

**Variance evaluation.** At \(s=t=u\), symmetry and the identity \(\int_0^y x^\beta\,dx=y^{\beta+1}/(\beta+1)\) give
\[
\int_0^u\int_0^u\kappa(x,y)\,dx\,dy
=\frac{2}{\beta+1}\left(
\frac{u^{2\beta+1}}{2\beta+1}
-\frac{u^{2\beta+2}}{2\beta+2}\right).
\]
Substitution and algebra yield the displayed closed form. This completes the proof.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. It constructs the entire set of words by all insertion histories for multiple \((r,n)\) cases, computes the exact indicator subsets, compares all subset probabilities with the product formula using rational arithmetic, inverts the joint law by inclusion-exclusion, checks the exact pair covariance, and checks a log-submodular inclusion inequality and exponential-moment upper bounds. All 6,375 exact rational assertions passed. Additional direct finite evaluation of the pair covariance recurrence at \(n=4000\) gave agreement with the proposed variance coefficient (e.g. \(r=2\), \(t=1\): normalized variance approximately \(0.111125\) versus limit \(1/9\)); these numerical comparisons are diagnostic, not proof. The asymptotic justification is the preceding analytic argument.

## Relationship to prior work

Janson's *Plane recursive trees, Stirling permutations and an urn model* (proceedings publication 2007, arXiv 2008) identifies the corresponding random growing tree and develops aggregate plateau counts. Janson, Kuba and Panholzer (2008 preprint) treat generalized \(r\)-Stirling permutations and aggregate refinements by the *occurrence number* of a plateau. Haglund and Visontai (2012), in their Theorems 3.3–3.5, prove real stability for multivariate Eulerian polynomials **indexed by the value of a plateau**; their polynomial already encodes the full finite joint distribution implicitly and supplies stronger qualitative negative-dependence machinery. This is substantial prior coverage and is not claimed anew. The present quantitative assertion is the explicit age-resolved covariance kernel, including the birth-prefix variance curve and local \(1/n\) covariance scale, obtained from a direct exact subset-product formula. Kuba and Panholzer's earlier specified-node degree work concerns fixed-node marginals. Acan and Hitczenko (2014) simplify the covariance matrix of counts by outdegree class in plane recursive trees, a different indexing from birth-label prefixes. The novelty comparison is therefore quantitative and parameter-specific, not a claim that label-indexed plateau statistics or their negative association were first discovered here.

## Limitations

The result proves covariance convergence only; it does not prove a Gaussian process limit, a functional central limit theorem, or uniform error rates. For the fixed index \(n\), \(X_{n,n}\) is deterministic. Prior multivariate stable-polynomial generating functions in principle permit exact coefficient extraction, so historical or implicit formulas for the same age-resolved covariance remain a priority risk. No independent audit or external validation has been conducted.

## References

1. S. Janson, *Plane recursive trees, Stirling permutations and an urn model*, DMTCS Proceedings (published 2007-12-31), https://dmtcs.episciences.org/en/articles/3590 ; arXiv:0803.1129, https://arxiv.org/abs/0803.1129 .
2. S. Janson, M. Kuba, and A. Panholzer, *Generalized Stirling permutations, families of increasing trees and urn models*, first arXiv submission 2008-05-27, https://arxiv.org/abs/0805.4084 .
3. J. Haglund and M. Visontai, *Stable multivariate Eulerian polynomials and generalized Stirling permutations*, European Journal of Combinatorics 33 (2012), 477–487, DOI: https://doi.org/10.1016/j.ejc.2011.10.007 . An accessible author-copy PDF is https://sites.math.washington.edu/~billey/classes/561.fall.2021/past.articles/haglund.vis.2012.pdf .
4. M. Kuba and A. Panholzer, *On the degree distribution of the nodes in increasing trees*, https://www.dmg.tuwien.ac.at/kuba/nodedegree3.pdf .
5. H. Acan and P. Hitczenko, *On the covariances of outdegrees in random plane recursive trees*, arXiv:1411.5756, https://arxiv.org/abs/1411.5756 .
