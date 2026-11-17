# Exact cherry-size-biased leaf law in uniform labelled trees

## Finding

Let \(T_n\) be uniform among all \(n^{n-2}\) unrooted trees on the labelled vertex set \([n]\), with \(n\ge4\). Let \(L_n\) denote its number of degree-one vertices. Let \(C_n\) count **all unordered pairs of leaves with a common neighbor**, even when that neighbor has degree greater than three. Equivalently, if \(s_v\) is the number of leaf neighbors of vertex \(v\), then \(C_n=\sum_v\binom{s_v}{2}\). This definition deliberately differs from the degree-three-only cherry statistic.

Put \(M_n=n\binom{n-1}{2}\) and
\[
 c_n=\mathbb E C_n=\frac{n(n-1)(n-2)^{n-3}}{2n^{n-2}}.
\]
For every integer \(0\le r\le n-3\), the following **exact cherry-size-biased leaf law** holds:
\[
 \boxed{\frac{\mathbb E\!\left[C_n\binom{L_n-2}{r}\right]}{\mathbb E C_n}
 =\binom{n-3}{r}\left(1-\frac{r}{n-2}\right)^{n-4}.}
\]
Equivalently, under the probability measure with density \(C_n/\mathbb EC_n\) relative to the law of \(T_n\), the variable \(L_n-2\) has the distribution of the number of empty boxes among \(n-3\) designated boxes after \(n-4\) independent uniform throws into \(n-2\) boxes. Thus the formula specifies the entire size-biased leaf distribution, not only its first moment.

For **every** \(n\ge4\),
\[
 \boxed{\operatorname{Cov}(L_n,C_n)
 =c_n\left[2+(n-3)\left(\frac{n-3}{n-2}\right)^{n-4}-n\left(\frac{n-1}{n}\right)^{n-2}\right]>0.}
\]
The square-bracketed difference is at least \(5/16\). Its sharp asymptotic leading behavior, together with both marginal variances, is
\[
 \begin{aligned}
 \operatorname{Cov}(L_n,C_n)&\sim n\frac{e-3/2}{e^3},\\
 \operatorname{Var}(L_n)&\sim n\frac{e-2}{e^2},\\
 \operatorname{Var}(C_n)&\sim n\frac{e^2/2+e-1}{e^4}.
 \end{aligned}
\]
In particular the **Pearson correlation**, without any assertion here about a joint distributional central limit theorem, has the nonzero limit
\[
 \boxed{\lim_{n\to\infty}\operatorname{Corr}(L_n,C_n)
 =\frac{e-3/2}{\sqrt{(e-2)(e^2/2+e-1)}}
 =0.617858378306\ldots.}
\]

## Assumptions and scope

The sample is a uniformly chosen *labelled, unrooted, simple tree*; it is not a uniform unlabelled tree, a binary phylogenetic tree, or a conditioned binary Galton--Watson tree. Leaves have degree exactly one, not degree zero. A center with \(s\ge3\) leaf neighbors contributes \(\binom{s}{2}\) to \(C_n\). All statements on the size-biased distribution and covariance hold for every integer \(n\ge4\); the second factorial moment formula below is displayed for \(n\ge5\), with the \(n=4\) boundary treated separately. The limits refer to \(n\to\infty\) through the positive integers.

## Proof

**1. Marking and deletion.** Fix distinct labels \(a,b,v\), with \(a,b\) unordered. Let \(Q_{a,b;v}\) be the event that \(a\) and \(b\) are leaves both adjacent to \(v\). Delete \(a,b\). For \(n\ge4\), this is a bijection between trees satisfying \(Q_{a,b;v}\) and all Cayley trees on the remaining \(m=n-2\) labels, including \(v\): adding the two prescribed pendant edges is the inverse. Hence
\[
 \Pr(Q_{a,b;v})=\frac{(n-2)^{n-4}}{n^{n-2}}
 \quad\text{and}\quad
 \mathbb EC_n=M_n\Pr(Q_{a,b;v})=c_n.
\]
Conditional on \(Q_{a,b;v}\), the reduced tree is exactly uniform. For the reduced tree \(U_m\),
\[
 L_n=2+L(U_m)-\mathbf 1\{\deg_{U_m}(v)=1\}.
\]
The subtraction is essential: the center \(v\), if previously a leaf, ceases being a leaf when its two new neighbors are attached.

**2. Full size-biased law.** Under the uniformly random Prüfer word for \(U_m\), each of its \(m-2\) entries is independent uniform in the \(m\)-label set. A vertex is a leaf exactly when its label does not occur in this word. Therefore \(L(U_m)-\mathbf1\{\deg_{U_m}(v)=1\}\) is the number of missing labels among the \(m-1=n-3\) labels other than \(v\). Its \(r\)-th binomial moment is
\[
 \binom{m-1}{r}\left(\frac{m-r}{m}\right)^{m-2}.
\]
By label exchangeability, \(\mathbb E[C_n f(L_n)]/c_n\) equals \(\mathbb E[f(L_n)\mid Q_{a,b;v}]\) for every bounded function \(f\): expand \(C_n=\sum_{v,\{a,b\}}\mathbf1_{Q_{a,b;v}}\). Taking \(f(\ell)=\binom{\ell-2}{r}\) gives the boxed formula. Binomial moments of orders \(0,\dots,n-3\) determine the finite distribution by inversion.

**3. Exact covariance and strict sign.** The usual Prüfer absence identity gives
\[
 \mathbb E L_n=n a_n,\qquad a_n=\left(1-\frac1n\right)^{n-2}.
\]
Taking \(r=1\) in step 2 yields \(\mathbb E[L_n C_n]/c_n=2+(n-3)a_{n-2}\). The covariance identity follows. For real \(x\ge2\), the function \(a_x=(1-1/x)^{x-2}\) is strictly decreasing, since
\[
 \frac{d}{dx}\log a_x
 =\log\left(1-\frac1x\right)+\frac{x-2}{x(x-1)}<0,
\]
using \(\log(1-1/x)<-1/x\) and \((x-2)/(x(x-1))<1/x\). Thus, for \(n\ge4\),
\[
 2+(n-3)a_{n-2}-na_n\ge 2-3a_n\ge2-3a_4=\frac5{16}>0.
\]
This argument establishes the sign for all sizes, without extrapolating finite enumeration.

**4. Exact second moments.** For \(n\ge5\), the ordered pairs of distinct marked cherry events are separated into the following exhaustive compatible cases: same center with exactly one shared leaf; same center with four distinct leaves; and different centers with four distinct leaves. Events with a leaf serving as another center or with different centers sharing a leaf are impossible. Deleting three distinct prescribed leaves in the first case gives \((n-3)^{n-5}\) reduced trees. Deleting four in the other cases gives \((n-4)^{n-6}\) reduced trees; at \(n=5\) the reduced singleton is counted by the convention \(1^{-1}=1\). Counting event pairs then simplifies to
\[
 \mathbb E[C_n(C_n-1)]=
 \frac{n(n-1)(n-2)(n-3)^{n-4}}{n^{n-2}}
 +\frac{n(n-1)(n-2)(n-3)(n-4)^{n-4}}{4n^{n-2}}.
\]
For \(n=4\), directly \(\mathbb E[C_4(C_4-1)]=3/2\), whereas \(\mathbb EC_4=3/4\). Additionally, for all \(n\ge4\),
\[
 \mathbb E[L_n(L_n-1)]
 =n(n-1)\left(1-\frac2n\right)^{n-2}.
\]
Subtracting squares of the means now determines \(\operatorname{Var}(C_n)\) and \(\operatorname{Var}(L_n)\) exactly. Note that the covariance and size-bias statements did not require the second-cherry pair enumeration.

**5. Asymptotic constants.** Write \(t=1/n\) and use
\[
 (1-kt)^{1/t-h}
 =e^{-k}\left[1+\left(hk-\frac{k^2}{2}\right)t+O(t^2)\right]
\]
for fixed integers \(k,h\). Substitute into the explicit first and second moment expressions. The \(n^2\) terms in \(\operatorname{Var}(C_n)\) cancel; retaining the \(n\) terms gives \((e^2/2+e-1)e^{-4}\). The two other coefficients follow from the first moments and the leaf factorial moment. Both variance coefficients are strictly positive, so division gives the stated limiting correlation.

## Verification

The standalone file `check.py` independently enumerates every Prüfer sequence through \(n=8\), decodes its tree, counts leaf-neighbor pairs from the decoded graph, and compares exact rational values of the five moments \(\mathbb EC_n\), \(\mathbb EL_n\), \(\mathbb E L_nC_n\), \(\mathbb E C_n(C_n-1)\), and \(\mathbb E L_n(L_n-1)\). It checks every permitted size-biased binomial moment at those orders, and checks exact positivity and variance signs through \(n=350\). On the included source it returns `VERIFY_OK 1076`. The infinite-domain statements above are proved algebraically and analytically; the finite checks are corroboration, not a substitute.

## Relationship to prior work

Junk, Schmidt and Weber (preprint first posted November 7, 2019; journal 2020) use a **different degree-three-restricted** cherry definition and calculate its first two moments in their Section 3. They expressly distinguish it from the unrestricted leaf-pair definition of Erdős and Rényi. Their restrictive count is not the present \(C_n\), nor does its covariance with \(L_n\) determine the unrestricted covariance. Isaev, Southwell and Zhukovskii (first posted December 20, 2019) develop general pattern-count moments and limit laws for uniform labelled trees; their counting lemma supports the basic marked-pattern probabilities, and no claim of novelty is made for the underlying Cayley/Prüfer enumeration or for general pattern-count normality. The present scoped result is the specific **entire cherry-size-biased leaf distribution, strictly positive all-size mixed covariance, and explicit positive limiting Pearson correlation**. Broader general-purpose pattern-count machinery may implicitly yield these special values after additional calculations; this is a priority limitation. Phylogenetic cherry--pitchfork papers use different sampling models and different statistics.

## Limitations

No independent mathematical audit has been performed. Historical-priority coverage by a general bivariate Cayley-tree pattern enumerator cannot be ruled out. The displayed Pearson correlation limit does **not** itself prove a bivariate central limit theorem; no new CLT or quantitative convergence rate is claimed. The theorem uses the uniform labelled model and counts every leaf pair even at high-degree centers; it should not be transferred without proof to the degree-three-only cherry count or to Yule/PDA phylogenetic trees.

## References

1. L. Junk, S. Schmidt, M. Weber, *Almost all trees have quantum symmetry*, arXiv:1911.02952v1 (2019-11-07); Archiv der Mathematik 115 (2020), Section 3. https://arxiv.org/abs/1911.02952 ; https://link.springer.com/article/10.1007/s00013-020-01476-x
2. M. Isaev, A. Southwell, M. Zhukovskii, *Distribution of tree parameters by martingale approach*, arXiv:1912.09838v1 (2019-12-20), Section 2 (especially Lemma 2.3). https://arxiv.org/abs/1912.09838
3. S. B. Ekhad, D. Zeilberger, *Automated Counting and Statistical Analysis of Labeled Trees with Degree Restrictions*, arXiv:2201.07326v1 (2022-01-18), on one-vertex degree counts. https://arxiv.org/abs/2201.07326
4. K. P. Choi, A. Thompson, T. Wu, *On cherry and pitchfork distributions of random rooted and unrooted phylogenetic trees*, arXiv:2002.12643v1 (2020-02-28). https://arxiv.org/abs/2002.12643
