# Age-resolved sign reversal in recursive-tree degree–leaf dependence

## Finding
Let a uniformly random recursive tree have vertices \(1,\ldots,n\), with vertex \(j\ge2\) choosing its parent independently and uniformly from \(1,\ldots,j-1\). Write \(D_i\) for the number of children of vertex \(i\) and \(L_n\) for the total number of vertices with no children. Set \(H_m=\sum_{k=1}^{m}1/k\), with \(H_0=0\).

For each integer \(n\ge2\),
\[
\operatorname{Cov}(D_1,L_n)=\frac{n-2}{2(n-1)},\qquad
\operatorname{Cov}(D_n,L_n)=0.
\]
For every \(2\le i\le n-1\),
\[
\boxed{\operatorname{Cov}(D_i,L_n)=\frac{n-i}{2(n-1)}-\frac{i-1}{n-1}(H_{n-2}-H_{i-2}).}
\]
For every \(n\ge7\) this profile starts positive at \(i=2\), ends negative at \(i=n-1\), and switches sign at most once, with at most one zero. For \(3\le n\le6\), all nonroot, nonterminal entries are strictly negative; for \(n=2\) both entries vanish. If \(i/n\to\alpha\in(0,1)\), then
\[
\operatorname{Cov}(D_i,L_n)\longrightarrow g(\alpha)=\frac{1-\alpha}{2}+\alpha\log\alpha.
\]
This function has exactly one zero in \((0,1)\), namely \(\alpha_*=0.284668137040838\ldots\); it is positive below and negative above that number. The deterministic parent edge of a nonroot vertex does not change its covariance, so the same result holds for ordinary undirected degree.

## Assumptions and scope
The tree is the ordinary *uniform* (unordered) recursive tree, not a uniformly random Cayley tree or plane recursive tree. Parent choices at different arrival times are mutually independent. All statements hold for the indicated finite integer ranges; the limit uses \(n\to\infty\) and a sequence of nonroot indices with \(i/n\to\alpha\). In the root formula, \(D_1\) is its outdegree, not total degree; those coincide.

## Proof
For \(j\ge2\) write \(X_{ij}=\mathbf1_{\{P_j=i\}}\) when \(i<j\), so \(D_i=\sum_{j=i+1}^n X_{ij}\). For \(v\ge2\), let \(Y_v\) indicate that \(v\) receives no children. Vertex 1 is never a leaf once \(n\ge2\), and \(L_n=\sum_{v=2}^nY_v\). Independence across parent choices gives
\[
\mathbb E Y_v=\prod_{k=v+1}^n\left(1-\frac1{k-1}\right)=\frac{v-1}{n-1}.
\]
For \(j\le v\), \(X_{ij}\) and \(Y_v\) are independent. When \(j>v\), \(i\ne v\) and \(j\ge3\), conditioning on \(P_j=i\) forces \(P_j\ne v\); hence
\[
\operatorname{Cov}(X_{ij},Y_v)=\frac{v-1}{(n-1)(j-1)(j-2)}.
\]
For \(j>i\ge2\), the exceptional term \(v=i\) has
\[
\operatorname{Cov}(X_{ij},Y_i)=-\frac{i-1}{(n-1)(j-1)}.
\]
Summing over \(v=2,\ldots,j-1\), using \(\sum_{v=2}^{j-1}(v-1)=(j-2)(j-1)/2\), gives
\[
\operatorname{Cov}(X_{ij},L_n)=\frac1{2(n-1)}-\frac{i-1}{(n-1)(j-2)},\quad j>i\ge2.
\]
For \(i=1\) and \(j\ge3\), the same sum without the exceptional term is \(1/(2(n-1))\); \(j=2\) contributes zero because that attachment is deterministic. Summing over \(j\) proves the three formulas.

For finite \(n\), let \(G_i=(n-1)\operatorname{Cov}(D_i,L_n)\) for \(2\le i\le n-1\). Direct subtraction yields \(G_{i+1}-G_i=1/2-(H_{n-2}-H_{i-1})\) for \(2\le i\le n-2\), which increases strictly with \(i\). Thus the \(G_i\) are strictly convex. Moreover \(G_{n-1}=-1/2\), and \(G_2=(n-2)/2-H_{n-2}\), which is positive exactly for \(n\ge7\) (the increment is \(1/2-1/(n-1)>0\) for \(n>3\)). Strict convexity and the negative right endpoint exclude a return from negative to positive; hence the stated single transition. For \(3\le n\le6\), \(G_2<0\) and \(G_{n-1}<0\), and convexity makes all intermediate values negative.

Finally, if \(i/n\to\alpha\in(0,1)\), the harmonic difference converges to \(\log(1/\alpha)\), yielding \(g(\alpha)\). The function is strictly convex because \(g''(\alpha)=1/\alpha>0\); it has \(g(0+)=1/2\), \(g(1)=0\), and is negative just below 1 since \(g'(1)=1/2\). These facts prove uniqueness of its interior zero and the sign classification.

## Verification
Run `python3 verify.py` to reproduce exact rational checks; the script exhaustively enumerates all \((n-1)!\) recursive trees for \(2\le n\le8\), checks the original covariance against the formula, independently checks local-summation identities for \(2\le n\le120\), and tests the strict finite sign transition for \(7\le n\le120\). The verifier returned 7408 successful comparisons. Finite enumeration confirms but does not replace the all-\(n\) argument above.

## Relationship to prior work
Janson's degree-distribution work gives multivariate laws and covariance information for *unlabeled outdegree frequency counts*, not this birth-indexed covariance of one marked vertex's degree with total leaves. A published exact root-degree/leaf-count identity gives the \(i=1\) case; the new content is the all-index harmonic profile and its unique age-dependent sign transition. The proof uses the standard independent-parent description, whose simplicity permits exact rather than asymptotic formulas.

## Limitations
The result concerns first-order covariance, not stochastic ordering, conditional regression, or a full joint distribution. The root case is prior known. A historical marked-vertex mixed-moment identity in older recursive-tree literature may imply the result; priority remains subject to further checking, especially inaccessible publications. No independent audit has been performed.

## References
1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83. Published online November 16, 2004. https://doi.org/10.1002/rsa.20046 . Author preprint: https://www2.math.uu.se/~svantejs/papers/sj155.pdf .
2. H. M. Mahmoud and R. T. Smythe, *Asymptotic joint normality of outdegrees of nodes in random recursive trees*, Random Structures & Algorithms 3 (1992), 255–266; first-publication date October 18, 1992; https://doi.org/10.1002/rsa.3240030305 .
3. *Equal-share covariance of root degree and leaves in a random recursive tree*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f .
