# Strict negative dependence of the two extreme-key depths in random binary search trees

## Finding
Let \(T_n\), \(n\ge 2\), be the binary search tree obtained by inserting the keys \(1,\ldots,n\) in a uniformly random order. Let \(D_n^-\) and \(D_n^+\) be the depths, counted in edges from the root, of keys \(1\) and \(n\), respectively. With \(H_n=\sum_{j=1}^{n}1/j\) and \(H_n^{(2)}=\sum_{j=1}^{n}1/j^2\), the following hold.

1. **Strict negative quadrant dependence.** For every \(a,b\in\{0,\ldots,n-2\),
   \[\Pr(D_n^->a,D_n^+>b)<\Pr(D_n^->a)\Pr(D_n^+>b).\]
   More generally, for all nondecreasing real functions \(f,g\) on \(\{0,\ldots,n-1\}\),
   \[\operatorname{Cov}(f(D_n^-),g(D_n^+))\le 0,\]
   with strict inequality if both functions are nonconstant.
2. **Exact dependence and its limit.**
   \[\operatorname{Cov}(D_n^-,D_n^+)=1-H_n^{(2)}<0,\qquad \operatorname{Var}(D_n^-)=\operatorname{Var}(D_n^+)=H_n-H_n^{(2)}.\]
   Hence the covariance decreases strictly from \(-1/4\) at \(n=2\) to \(1-\pi^2/6\), whereas
   \[\lim_{n\to\infty}(\log n)\operatorname{Corr}(D_n^-,D_n^+)=1-\frac{\pi^2}{6}.\]
3. **Independent Gaussian scaling limit.**
   \[\left(\frac{D_n^--(H_n-1)}{\sqrt{\log n}},\frac{D_n^+-(H_n-1)}{\sqrt{\log n}}\right)\ \xrightarrow{d}\ (Z_1,Z_2),\]
   where \(Z_1,Z_2\) are independent standard normal variables. Thus finite-size strict negative dependence is compatible with asymptotically independent normalized search depths.

## Assumptions and scope
The insertion order is uniform over all \(n!\) permutations. All keys are distinct and totally ordered. The root has depth zero. The conclusions concern the two deterministic extreme ranks, not randomly selected keys, and hold exactly for all integers \(n\ge2\); the normal limit is as \(n\to\infty\). This is the usual random-permutation binary-search-tree model, equivalently a treap with independent continuous priorities.

## Proof
**Step 1: One-sided depth law.** Write \(Q_m\) for the depth of the smallest key in an independent uniform tree of size \(m\), with \(Q_1=0\). Assign the \(m\) keys independent continuous insertion priorities \(U_1,\ldots,U_m\). For each \(j=2,\ldots,m\), key \(j\) is an ancestor of key \(1\) precisely when \(U_j\) is the minimum among \(U_1,\ldots,U_j\). These are independent lower-record indicators of respective probabilities \(1/j\), so
\[Q_m\ \overset{d}=\ \sum_{j=2}^m B_j,\qquad B_j\text{ independent Bernoulli}(1/j).\]
In particular \(\mathbb E Q_m=H_m-1\) and \(\operatorname{Var}(Q_m)=H_m-H_m^{(2)}\). The record coupling also shows \(Q_m\le Q_{m+1}\) almost surely under a suitable joint construction, and both differences have positive probability.

**Step 2: Conditional splitting and negative dependence.** Let \(L\) be the left-subtree size of the root; \(L\) is uniform on \(\{0,\ldots,n-1\}\), and the two subtrees are independent uniform search trees conditional on \(L\). Set \(A_0=0\) and \(A_m=1+Q_m\) for \(m\ge1\). Conditional on \(L=l\), the pair \((D_n^-,D_n^+)\) consists of independent variables with respective laws \((A_l,A_{n-1-l})\). For any nondecreasing \(f\), the sequence \(F(l)=\mathbb E f(A_l)\) is nondecreasing, and it is nonconstant if \(f\) is nonconstant on \(\{0,\ldots,n-1\}\): indeed \(A_0=0\), while \(A_{n-1}\) assigns positive probability to every depth from one through \(n-1\). Analogously \(G(l)=\mathbb E g(A_l)\) is nondecreasing. Conditional covariance is zero, and hence
\[\operatorname{Cov}(f(D_n^-),g(D_n^+))=\operatorname{Cov}(F(L),G(n-1-L))\le0.\]
The final inequality is the reversed Chebyshev sum inequality: in the double-sum expression for covariance, every factor \((F(l)-F(k))(G(n-1-l)-G(n-1-k))\) is nonpositive. The extreme pair \(l=0,k=n-1\) makes the sum strictly negative when both functions are nonconstant. Taking the nondecreasing tail indicators \(f(x)=\mathbf1_{\{x>a\}}\) and \(g(x)=\mathbf1_{\{x>b\}}\), for \(0\le a,b\le n-2\), gives strict negative quadrant dependence.

**Step 3: Exact mixed moment.** Define \(H_0=0\). From the root split, \(\mathbb E(D_n^-\mid L=l)=H_l\) and \(\mathbb E(D_n^+\mid L=l)=H_{n-1-l}\), giving \(\mathbb E D_n^- =\mathbb E D_n^+=H_n-1\) and
\[\mathbb E[D_n^-D_n^+]=\frac1n\sum_{l=0}^{n-1}H_lH_{n-1-l}.\]
The identity \(\sum_{l\ge0}H_lz^l=-\log(1-z)/(1-z)\) and twice differentiating \([z^{n-1}](1-z)^{-a}=(a)_{n-1}/(n-1)!\) with respect to \(a\) at \(a=2\) give
\[\frac1n\sum_{l=0}^{n-1}H_lH_{n-1-l}=(H_n-1)^2+1-H_n^{(2)}.\]
Subtracting the product of the means proves the covariance formula. Its successive difference is \(-1/(n+1)^2\). The marginal variance from Step 1 and \(H_n\sim\log n\), \(H_n^{(2)}\to\pi^2/6\) give the correlation limit.

**Step 4: Joint normal limit.** Fix \(0<\varepsilon<1/2\) and condition on \(\varepsilon n\le L\le(1-\varepsilon)n\). Each depth is, independently given \(L=l\), a constant one plus a sum of independent Bernoulli variables with parameters \(1/j\), \(2\le j\le l\) or \(2\le j\le n-1-l\). Uniformly over this central range, both means differ from \(H_n-1\) by at most a constant depending on \(\varepsilon\), and both variances equal \(\log n+O_\varepsilon(1)\). The triangular-array Lindeberg central limit theorem (bounded summands and diverging variance) therefore gives two independent standardized normal limits uniformly over the central range. The probability that \(L\) is outside it is at most \(2\varepsilon+O(1/n)\). First let \(n\to\infty\) and then \(\varepsilon\downarrow0\), establishing the joint limit.

## Verification
The standalone script `verify.py` implements a rational joint-law calculation from independent left and right subtree depths, independently enumerates all \(n!\) insertion orders for \(2\le n\le8\), checks every nontrivial upper-quadrant inequality for those sizes, and checks the exact harmonic convolution through \(n=300\). It reports 796 passing exact assertions. The finite enumeration checks the proof at small sizes but is not offered as proof of the general statements, which follow from the preceding arguments. Reproduce with `python3 verify.py` using Python 3 standard library only.

## Relationship to prior work
Seidel and Aragon's *Randomized Search Trees* (1996) establishes the random-priority search-tree framework and exact one-key depth expectations. Devroye and Neininger's *Distances and Finger Search in Random Binary Search Trees* (2004; author version dated 2003) establishes record representations and marginal normal limits for specified ranks and studies path-distance distributions. Panholzer and Prodinger's *Spanning Tree Size in Random Binary Search Trees* (public arXiv version of 14 May 2004) derives moments and normal laws for spanning trees of randomly selected keys, with a harmonic-square coefficient identity related to the algebra in Step 3. These are genuinely close foundations but, in the portions inspected, do not state strict negative quadrant dependence between the two **deterministic extreme-key depths**, its covariance \(1-H_n^{(2)}\), or the joint independent-normal limit for those two depths. In particular, the distance between a randomly selected pair does not determine the bivariate law of the two fixed extreme ranks. The general ingredients are classical; the contribution is their specific exact joint-dependence synthesis, not a claim that the generating-function identity is new.

## Limitations
The result is restricted to the uniform random-permutation search-tree law; weighted, biased, and Mallows trees are not covered. It does not establish negative regression or negative association for an entire family of node depths. The exact covariance is a mixed moment and does not identify the entire bivariate distribution by itself. Historical coverage remains possible in older specialized literature on joint extreme-rank depth laws or as an unstated corollary of general multivariate treap results. No independent audit or external formal certification has been performed.

## References
- R. Seidel and C. R. Aragon, *Randomized Search Trees*, Algorithmica 16 (1996), 464–497. https://doi.org/10.1007/BF01940876 . Author-hosted text: https://faculty.washington.edu/aragon/pubs/rst96.pdf
- L. Devroye and R. Neininger, *Distances and Finger Search in Random Binary Search Trees*, SIAM Journal on Computing 33 (2004), 647–658. https://doi.org/10.1137/S0097539703424521 . Author text: https://www.math.uni-frankfurt.de/~neiningr/pathdist.pdf
- A. Panholzer and H. Prodinger, *Spanning Tree Size in Random Binary Search Trees*, Annals of Applied Probability 14 (2004), 718–733. First arXiv version dated 2004-05-14: https://arxiv.org/abs/math/0405292
