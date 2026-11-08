# Root-split balance and cherry-count dependence in Catalan and search-tree models

## Finding
For every integer \(n\ge2\), let \(H\) count cherries (internal vertices with two external-leaf children), let \(K\) count internal vertices in the root's left subtree, and let \(B=(2K-(n-1))^2\). For a uniformly chosen ordered full binary tree with \(n\) internal vertices (Catalan model),
\[
\operatorname{Cov}(H,B)=-\frac{n-2}{2n-1}\frac{4^{n-1}}{C_n},\qquad C_n=\frac{1}{n+1}\binom{2n}{n}.
\]
For the tree obtained by inserting a uniformly random permutation of \(n\) distinct keys into an initially empty binary search tree, filling missing children with external leaves,
\[
\operatorname{Cov}(H,B)=-\frac{8(n-2)}{3n}.
\]
Both covariances vanish at \(n=2\) and are strictly negative for every \(n\ge3\). The scales differ:
\[
\operatorname{Cov}_{\rm Catalan}(H,B)\sim-\frac{\sqrt\pi}{8}n^{3/2},\qquad
\operatorname{Cov}_{\rm BST}(H,B)\longrightarrow-\frac83.
\]
In both models the conditional expected number of cherries, given \(K=k\), is **not monotone** with root imbalance: for \(n\ge5\) it is uniquely smallest at the two extreme splits \(k=0,n-1\), uniquely largest at \(k=1,n-2\), and is smaller at balanced splits (strictly decreasing inward in the Catalan model; constant on \(2\le k\le n-3\) in the search-tree model).

## Assumptions and scope
All trees are rooted and ordered, with internal nodes having exactly two child slots. The Catalan distribution assigns equal probability \(1/C_n\) to each of the \(C_n\) shapes. In the binary-search-tree (BST) distribution, the root key has uniformly distributed rank; its two subtrees are independent BSTs given their sizes. A cherry has two external (empty) children; thus a one-internal-node tree has one cherry and the empty tree has zero. The statistic \(B\) is the *square* of the difference in internal-node subtree sizes, not total Colless imbalance. No orientation-invariant quotient or labeled-phylogeny distribution is silently substituted for these two specified laws.

## Proof
Write \(c_t=C_t\), \(a_0=0\), and \(a_t\) for the total number of cherries over all Catalan trees with \(t\) internal nodes. Let
\[
C(z)=\sum_{t\ge0}c_tz^t=1+zC(z)^2=\frac{1-\sqrt{1-4z}}{2z}.
\]
Cherry-marking at the root gives \(A(z)=\sum_{t\ge0}a_tz^t=z+2zC(z)A(z)=z/\sqrt{1-4z}\), so \(a_t=\binom{2t-2}{t-1}\) for \(t\ge1\). Consequently
\[
f(0)=0,\qquad f(t):=\mathbb E_{\rm Catalan}[H_t]=\frac{a_t}{c_t}=\frac{t(t+1)}{2(2t-1)}\quad(t\ge1).
\]
Put \(D=z\,d/dz\). For a root split with \(k+\ell=n-1\), the Catalan weight is \(c_kc_\ell\), the expected cherry count is \(f(k)+f(\ell)\), and \(B=(k-\ell)^2\). Thus, with \(U(z)\) and \(V(z)\) representing the unnormalized root-squared-imbalance and mixed cherry/imbalance moments respectively,
\[
U(z)=2\bigl((D^2C)C-(DC)^2\bigr),\quad
V(z)=2\bigl((D^2A)C+A(D^2C)-2(DA)(DC)\bigr).
\]
Direct differentiation of the displayed algebraic \(C(z),A(z)\), followed by the binomial-series identity \([z^r](1-4z)^{-\beta}=4^r(\beta)_r/r!\), yields for each integer \(n\ge2\), writing \(b_n=\binom{2n-2}{n-1}\),
\[
[z^{n-1}]U(z)=\left(4n+2-\frac2n\right)b_n-4^n,\qquad
[z^{n-1}]V(z)=(n+1)^2b_n-(n+2)4^{n-1}.
\]
The mean \(\mathbb E H=a_n/c_n=b_n/c_n\). Therefore
\[
\operatorname{Cov}(H,B)=\frac{[z^{n-1}]V}{c_n}-\frac{b_n[z^{n-1}]U}{c_n^2}.
\]
Using \(c_n=2(2n-1)b_n/[n(n+1)]\) and simplifying proves the Catalan formula. Stirling's approximation \(c_n\sim4^n/(\sqrt\pi\,n^{3/2})\) proves its stated asymptotic.

For the BST model, put \(g(t)=\mathbb E H_t\), where \(g(0)=0\), \(g(1)=1\). Uniform root rank gives \(g(t)=\frac2t\sum_{j=0}^{t-1}g(j)\) for \(t\ge2\), whence induction yields \(g(t)=(t+1)/3\) for \(t\ge2\). Since \(K\) is uniform on \(\{0,\ldots,n-1\}\), conditionally independent subtrees give the exact regression
\[
\mathbb E[H\mid K=k]-\mathbb EH=\frac13\left(-\mathbf1_{k=0}-\mathbf1_{k=n-1}+\mathbf1_{k=1}+\mathbf1_{k=n-2}\right).
\]
This identity includes coincident indicators when \(n=2\). Multiplying by \(B=(2k-n+1)^2\) and averaging, the two extreme terms have squared value \((n-1)^2\), and the two next-extreme terms have squared value \((n-3)^2\). Since the centered regression sums to zero,
\[
\operatorname{Cov}(H,B)=\frac{2}{3n}\bigl((n-3)^2-(n-1)^2\bigr)=-\frac{8(n-2)}{3n}.
\]
Finally, the Catalan regression is exactly \(f(k)+f(n-1-k)\). For \(t\ge1\),
\[
f(t)=\frac t4+\frac38+\frac{3}{8(2t-1)}.
\]
The reciprocals make this sum strictly decrease as the smaller branch grows from \(1\) toward \((n-1)/2\); direct comparison with \(f(0)=0\) shows the extreme splits give a smaller expectation than all nonempty splits. For the BST model the regression is \(g(k)+g(n-1-k)\), equal to \(n/3\) at the extremes, \((n+2)/3\) one step inward and \((n+1)/3\) elsewhere for \(n\ge5\). This proves the claimed nonmonotone shape and all finite-size sign assertions.

## Verification
The standalone standard-library script `verify.py` reproduces each covariance from exact rational conditional moments for \(2\le n\le200\), verifies both Catalan generating-function coefficient identities, independently enumerates the complete cherry-count distributions of both models through \(n=12\), tests conditional-regression profiles, and checks asymptotic convergence numerically. Running `python verify.py` returned `PASS: 1820 exact and numerical assertions`. The infinite theorems follow from the algebraic and recursive arguments above, not extrapolation from finite checks.

## Relationship to prior work
Blum, François and Janson analyze the Yule/uniform tree-shape laws and the joint behavior of **Sackin and Colless global balance indices**, using the correspondence with permutation and Catalan binary-search-tree models. Wu and Choi analyze the joint distribution of **cherries and pitchforks** under Yule-Harding-Kingman and PDA models, establishing substantial cherry-count marginal information. Neither inspected primary treatment states the root-only *squared-imbalance versus cherry-count* covariance or its contrasting orders across the two precisely defined binary-tree laws. These two works provide background rather than proof of historical uniqueness; established marginal cherry means are not claimed as new.

## Limitations
The statement is about the two specified ordered-tree probability distributions, not every phylogenetic tree distribution. The method does not derive a full joint limiting law for \((H,B)\), nor does it assert that all previous general tree-functional frameworks fail to imply the formulas. Earlier or less accessible treatments could implicitly cover the identities; the present novelty assessment is conditional on the literature examined. Independent external validation has not been performed.

## References
1. M. G. B. Blum, O. François and S. Janson, *The mean, variance and limiting distribution of two statistics sensitive to phylogenetic tree balance*, Annals of Applied Probability **16** (2006), 2195–2214. DOI: `10.1214/105051606000000547`. Public arXiv version: https://arxiv.org/abs/math/0702415 (first posted 2007-02-14).
2. T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models*, https://arxiv.org/abs/1508.03139 (first posted 2015-08-13).
