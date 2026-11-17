# Sharp edge-variation heat amplification on complete bipartite graphs

## Finding
Let \(K_{a,b}\) be the unweighted complete bipartite graph with integers \(1\le a\le b\). Let \(L=D-A\) be its unnormalized combinatorial Laplacian and \(H_t=e^{-tL}\). For real vertex functions set
\[
\operatorname{TV}(f)=\sum_{i=1}^{a}\sum_{j=1}^{b}|f(A_i)-f(B_j)|.
\]
On the quotient by constant functions, for every real \(t\ge0\),
\[
\boxed{\|H_t\|_{\operatorname{TV}\to\operatorname{TV}}=
 \frac{2(b-1)}b e^{-at}-\frac{b-2}b e^{-(a+b)t}.}
\]
The bound is attained by a signal supported on a single vertex of the larger part, for every \(t\ge0\). This edge-variation norm happens to equal the sharp graph-distance Lipschitz norm on this graph, although the two seminorms are different.

The heat flow is variation-nonexpansive at all times if and only if \(b-a\le2\). If \(b-a\ge3\), the norm initially increases, has a unique positive maximizing time
\[
t_* = \frac1b\log\left(\frac{(a+b)(b-2)}{2a(b-1)}\right),
\]
and has sharp peak
\[
\frac{2(b-1)}{a+b}\left(\frac{2a(b-1)}{(a+b)(b-2)}\right)^{a/b}.
\]
For fixed \(a\) and \(b\to\infty\), the maximum tends to \(2\).

A separate sharp centering principle is part of the result: for arbitrary real vectors \(x\in\mathbb R^a\), \(y\in\mathbb R^b\), and their arithmetic means \(\bar x,\bar y\),
\[
\sum_{i,j}|(x_i-\bar x)-(y_j-\bar y)|
\le \frac{2(b-1)}b\sum_{i,j}|x_i-y_j|.
\]
The constant is sharp for every \(1\le a\le b\) (including the trivial zero constant when \(a=b=1\)).

## Assumptions and scope
All vertices have counting measure, all cross edges have unit weight, and there are no edges within parts. Time is continuous. The functions are real-valued and the graph-variation seminorm is the sum of absolute first differences over undirected edges, each edge counted once. No probability or stochastic normalization of the Laplacian is used. Every norm is on functions modulo constants. A vertex supported indicator is assigned value one at the indicated vertex and zero elsewhere.

## Proof
**1. Cut reduction.** For a linear operator \(T\) killing constants, the inequality \(\operatorname{TV}(Tf)\le C\operatorname{TV}(f)\) follows if it holds for every indicator \(\mathbf1_S\): write a finite-level decomposition of \(f\) as a constant plus a positive linear combination of nested superlevel-set indicators. The graph coarea identity expresses \(\operatorname{TV}(f)\) as the same positive linear combination of their cut sizes; apply linearity and the triangle inequality. We use this with the centering operators below.

**2. Sharp two-sided centering inequality.** Define \(T_{AB}f\) by subtracting the mean in each part separately. Fix a cut indicator with \(k\) selected vertices in the first part and \(\ell\) in the second. Put \(\alpha=k/a\), \(\beta=\ell/b\), and let independent \(P,Q\) be Bernoulli variables with probabilities \(\alpha,\beta\). Dividing the cross-edge sum by \(ab\), the original variation is \(\mathbb E|P-Q|\); the centered variation is \(\mathbb E|P-Q-\delta|\), where \(\delta=\alpha-\beta\).

When \(\delta>0\), put \(p_+=\alpha(1-\beta)\). Directly summing the three values of \(P-Q\) gives
\[
\mathbb E|P-Q-\delta|=\mathbb E|P-Q|+\delta(1-2p_+).
\]
The strict inequality \(kb>a\ell\), together with \(b\ge a\), implies \(b-\ell>a-k\); integrality gives \(b-\ell\ge a-k+1\). Thus \(k(b-\ell)\ge k(a-k+1)\ge a\), or \(p_+\ge1/b\). Since \(0<\delta\le\mathbb E|P-Q|\) and \(b\ge2\), the last displayed expression is at most \((2-2/b)\mathbb E|P-Q|\).

When \(\delta<0\), instead \(a\ell>bk\) implies \(\ell>k\), so \((a-k)\ell\ge(a-k)(k+1)\ge a\). Consequently \(p_-=(1-\alpha)\beta\ge1/b\). The analogous identity
\[
\mathbb E|P-Q-\delta|=\mathbb E|P-Q|+|\delta|(1-2p_-)
\]
gives the same bound. When \(\delta=0\), centering changes no cross difference. If \(a=b=1\), this centering is identically zero. Cut reduction proves the asserted inequality for all real signals. For a singleton selected in the second part, its original variation is \(a\), and the centered variation is \(2a(b-1)/b\), proving optimality.

**3. One-sided centering.** Let \(T_Bf\) vanish on the first part and equal \(y_j-\bar y\) on the second. The elementary \(\ell_1^b\)-norm identity for \(I-\mathbf1\mathbf1^\mathsf T/b\) yields \(\sum_j|y_j-\bar y|\le(2-2/b)\sum_j|y_j-c|\) for every real \(c\). Take \(c=\bar x\); Jensen's inequality implies
\[
\operatorname{TV}(T_Bf)=a\sum_j|y_j-\bar y|
\le(2-2/b)\sum_{i,j}|x_i-y_j|.
\]
Singleton second-part indicators attain equality.

**4. Exact heat decomposition.** Write \(\bar x\) and \(\bar y\) for the initial part means, and let \(n=a+b\). The three Laplacian eigenspaces are: fluctuations within the first part, eigenvalue \(b\); fluctuations within the second part, eigenvalue \(a\); and functions constant on each part with zero global mean, eigenvalue \(n\). Constants have eigenvalue zero. Put \(s=e^{-bt}\), \(r=e^{-at}\), and \(z=e^{-nt}\); then \(0<z\le s\le r\le1\). Each cross-edge difference after heat flow equals
\[
s(x_i-\bar x)-r(y_j-\bar y)+z(\bar x-\bar y).
\]
Since the original difference is \(x_i-y_j\), this equals the edge difference of
\[
(r-s)T_Bf+(s-z)T_{AB}f+zf.
\]
The two bounds above therefore give
\[
\operatorname{TV}(H_tf)
\le\left[(r-s)\frac{2(b-1)}b+(s-z)\frac{2(b-1)}b+z\right]\operatorname{TV}(f)
=\left[\frac{2(b-1)}b r-\frac{b-2}b z\right]\operatorname{TV}(f).
\]
For the second-part singleton indicator, direct evaluation produces cross-edge absolute values \((r(b-1)+z)/b\) at its \(a\) incident edges and \((r-z)/b\) at each of the other \(a(b-1)\) edges. Their sum divided by its initial variation \(a\) is exactly the proposed bound. This proves the all-time formula, including the two-vertex case.

**5. Contractivity, peak, and asymptotics.** Differentiate the proved norm formula. Its derivative at zero is \(b-a-2\). Its derivative at time \(t\) has the same sign as \(-2a(b-1)+(a+b)(b-2)e^{-bt}\). This expression is strictly decreasing in positive time if \(b>2\), proving nonexpansivity for \(b-a\le2\), or a unique positive peak for \(b-a\ge3\), with the stated formulas. For fixed \(a\), the peak time tends to zero as \(b\to\infty\) and its value tends to two.

## Verification
Run `python3 verify.py` using only the Python standard library. The checker verifies exact spectral semigroup composition, all cut and centering inequalities on a systematic set of part sizes, equality witnesses, rational-input inequalities, and the claimed initial derivative. It uses rational times \(t=-\log u\) with rational \(0<u\le1\), so all tested heat factors are exact rational numbers. Finite checks corroborate but do not establish the universal theorem, which is proved above.

## Relationship to prior work
Bauer et al. (2013) develop general graph heat gradient estimates and curvature-dimension methods, not sharp graph-edge-variation operator norms. Münch and Wojciechowski (2017), Theorem 3.8, characterize curvature by the **supremum** of edge gradients (Lipschitz norm), not by their sum. Chen, Coulhon and Hua (2017) study graph edge-gradient \(\ell_p\) estimates for \(1<p\le2\), not this sharp endpoint \(\ell_1\) operator norm on bicliques.

The graph-distance Lipschitz heat-semigroup norm on complete multipartite graphs has already been evaluated; its complete-bipartite specialization coincides numerically with the formula here. That earlier different-seminorm theorem is not claimed as new, nor does it by itself give the present total-variation estimate or the cross-difference centering inequality. The equality of the two sharp profiles on bicliques is a structural comparison, not a claim that their Banach norms coincide. An equivalent or stronger edge-variation result implicit in older matrix semigroup literature remains a residual priority risk.

## Limitations
This concerns finite complete bipartite graphs, counting measure, unnormalized unit-weight Laplacians, and ordinary anisotropic graph total variation on real functions. It does not cover arbitrary multipartite graphs, weighted bicliques, normalized/random-walk Laplacians, or all maximizing functions. Sharpness is established by one explicit family, not a classification of every equality case. The full bibliographic priority question is unresolved independently.

## References
- F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi, S.-T. Yau, *Li-Yau inequality on graphs*, arXiv:1306.2561, first posted 2013-06-11, https://arxiv.org/abs/1306.2561.
- F. Münch, R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first posted 2017-12-04, https://arxiv.org/abs/1712.00875.
- L. Chen, T. Coulhon, B. Hua, *Riesz transforms for bounded Laplacians on graphs*, arXiv:1708.05476, first posted 2017-08-18, https://arxiv.org/abs/1708.05476.
