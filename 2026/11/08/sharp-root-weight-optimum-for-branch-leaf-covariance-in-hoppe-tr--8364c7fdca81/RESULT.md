# Sharp root-weight optimum for branch–leaf covariance in Hoppe trees

## Finding
Let \(T_{n,\theta}\) be the Hoppe recursive tree on vertices \(1,\ldots,n\): vertex \(1\) is the root and has fixed attachment weight \(\theta>0\), every other vertex has weight one, and each vertex attaches independently to an earlier vertex with probability proportional to the earlier vertex's weight. Let \(B_{n,\theta}\) be the number of root children (equivalently, root branches), and let \(L_{n,\theta}\) be the number of vertices with no children. For all integers \(n\ge 2\) and reals \(\theta>0\),

\[
\operatorname{Cov}(B_{n,\theta},L_{n,\theta})
=\frac{\theta(n-1)(n-2)}{2(\theta+n-2)^2}.
\]

For every \(n\ge3\), this covariance has a **unique** maximizer over positive root weights, namely \(\theta=n-2\), and its exact maximum is \((n-1)/8\). Thus the dependence is nonmonotone in the root weight: it tends to zero as \(\theta\downarrow0\) and as \(\theta\to\infty\). If \(\theta_n/n\to\alpha\in(0,\infty)\), then

\[
\frac{1}{n}\operatorname{Cov}(B_{n,\theta_n},L_{n,\theta_n})
\longrightarrow\frac{\alpha}{2(1+\alpha)^2},
\]

with unique macroscopic maximum \(1/8\) at \(\alpha=1\). If \(\theta_n=o(n)\), the covariance is asymptotic to \(\theta_n/2\); if \(\theta_n/n\to\infty\), it is asymptotic to \(n^2/(2\theta_n)\).

## Assumptions and scope
For each \(n\ge2\), the tree is constructed from vertex \(1\) by independently choosing, at insertion \(i\in\{2,\ldots,n\}\), its parent \(P_i\) from \(\{1,\ldots,i-1\}\), with

\[
\Pr(P_i=1)=\frac{\theta}{\theta+i-2},\qquad
\Pr(P_i=j)=\frac{1}{\theta+i-2}\quad(2\le j<i).
\]

The weight \(\theta\) remains fixed during each tree's construction. It may vary with \(n\) when an asymptotic family is considered. The root is not a leaf for \(n\ge2\), since vertex \(2\) attaches to it with probability one. Root branches are root children, not arbitrary edge branches. For \(n=2\), both statistics equal one deterministically and the covariance is zero for every \(\theta\); the uniqueness statement expressly excludes this case.

## Proof
For \(2\le i\le n\), put \(A_i=\mathbf1_{\{P_i=1\}}\); for \(2\le j\le n\), let \(F_j=\mathbf1_{\{j\text{ has no children by time }n\}}\). Then \(B_{n,\theta}=\sum_{i=2}^{n}A_i\) and \(L_{n,\theta}=\sum_{j=2}^{n}F_j\). Independence of parent choices shows that \(A_i\) and \(F_j\) are independent for \(j\ge i\). If \(j<i\), direct telescoping yields

\[
\Pr(F_j=1)=\prod_{k=j+1}^{n}\frac{\theta+k-3}{\theta+k-2}
=\frac{\theta+j-2}{\theta+n-2}.
\]

Conditioning on \(A_i=1\) guarantees that insertion \(i\) does not attach to \(j\). The factor at step \(i\) in the preceding product, \((\theta+i-3)/(\theta+i-2)\), is therefore replaced by one. Consequently, for \(2\le j<i\le n\),

\[
\operatorname{Cov}(A_i,F_j)
=\frac{\theta(\theta+j-2)}{(\theta+n-2)(\theta+i-2)(\theta+i-3)}.
\]

All remaining cross-covariances vanish. Summing over \(j<i\) gives

\[
\operatorname{Cov}(B_{n,\theta},L_{n,\theta})
=\frac{\theta}{2(\theta+n-2)}
\sum_{i=3}^{n}\frac{(i-2)(2\theta+i-3)}{(\theta+i-2)(\theta+i-3)}.
\]

The numerator in each summand is \((\theta+i-2)(\theta+i-3)-\theta(\theta-1)\), while

\[
\sum_{i=3}^{n}\frac{1}{(\theta+i-2)(\theta+i-3)}
=\frac1\theta-\frac1{\theta+n-2}.
\]

The sum therefore equals \((n-2)(n-1)/(\theta+n-2)\), proving the exact covariance.

A separate one-step check follows by conditioning on the state at insertion \(i\). With \(C_i=\operatorname{Cov}(B_{i,\theta},L_{i,\theta})\) and \(i\ge3\), the probability that the arriving vertex attaches to an existing leaf is \(L_{i-1,\theta}/(\theta+i-2)\). Using that attaching to the root and attaching to a leaf are mutually exclusive, one finds

\[
C_i=\frac{\theta+i-3}{\theta+i-2}C_{i-1}
+\frac{\theta}{(\theta+i-2)^2}\,\mathbb E[L_{i-1,\theta}],
\qquad C_2=0,
\]

where \(\mathbb E[L_{m,\theta}]=(m-1)(m-2+2\theta)/(2(\theta+m-2))\). Substitution verifies the same closed form by induction.

For \(n\ge3\), differentiation gives

\[
\frac{\partial}{\partial\theta}
\operatorname{Cov}(B_{n,\theta},L_{n,\theta})
=\frac{(n-1)(n-2)(n-2-\theta)}{2(\theta+n-2)^3}.
\]

It is positive below \(n-2\) and negative above \(n-2\). Both endpoint limits are zero, so the maximum is unique; direct substitution gives \((n-1)/8\). Finally, each asymptotic statement follows by dividing the exact formula by its dominant powers of \(n\) and \(\theta_n\). No probabilistic limit theorem is assumed.

## Verification
The standalone `verify.py` uses a separate exhaustive weighted enumeration of every possible vector of parent choices for \(n=2,\ldots,8\), at eight rational values of \(\theta\). It reconstructs branch and leaf counts independently from parent vectors and checks the normalization, both means, the full covariance and each attachment-position covariance profile against exact rational formulas. Additional rational checks compare the claimed maximizing value with seven distinct test weights for each \(3\le n<150\). The script passed 1,567 exact assertions. Run `python3 verify.py` from the extracted package directory. The finite enumeration supports but does not replace the preceding proof, which applies to all real \(\theta>0\) and every stated integer \(n\).

## Relationship to prior work
Leckey and Neininger introduced the Hoppe-tree model and derived leaf-count moments and fixed-root-weight limit laws; these do not give the joint root-branch/leaf covariance or a variable-weight optimizer. Hiesmayr and Işlak extended weighted-recursive-tree analyses to leaf and root-branch statistics, with their marginal results presented separately. A published calculation for uniform random recursive trees gives the specialization \(\theta=1\), so that specialization is **not** claimed as new. The result here is the arbitrary-positive-weight identity together with its unique finite-size optimizer and macroscopic weight-scaling law, neither of which follows from a single fixed-weight specialization.

## Limitations
The theorem concerns the standard Hoppe model with one distinguished weighted root and every nonroot weight equal to one. It makes no claim for an arbitrary sequence of nonroot weights, for joint convergence in distribution, or for the optimizer of correlation (which need not coincide with the optimizer of covariance). The publicly accessible literature comparison is not an exhaustive priority certificate: broader bivariate tree-enumerator identities might imply the same covariance without stating it explicitly. Independent audit has not been performed.

## References
- K. Leckey and R. Neininger, *Asymptotic analysis of Hoppe trees*, arXiv:1202.2439, first submitted 2012-02-11, https://arxiv.org/abs/1202.2439.
- E. Hiesmayr and Ü. Işlak, *Asymptotic results on Hoppe trees and its variations*, arXiv:1712.03572, first submitted 2017-12-10, https://arxiv.org/abs/1712.03572.
- *Equal-share covariance of root degree and leaves in a random recursive tree*, previously published uniform-weight result (\(\theta=1\) case).
