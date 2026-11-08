# Exact zero-leaf-degree variance in random recursive trees

## Finding

**Theorem.** Let \(T_n\) be the uniform random recursive tree on vertices \(1,\ldots,n\), where each vertex \(j\ge2\) attaches to an independently chosen uniformly random vertex in \(\{1,\ldots,j-1\}\). Call an undirected vertex a *leaf* if its degree is one, and let \(M_{0,n}\) count vertices with no neighbors that are leaves. Then

\[
\lim_{n\to\infty}\frac{\operatorname{Var}(M_{0,n})}{n}
=\frac{3-e}{e^2}=0.03812640853839575\ldots>0.
\]

Further, with \(\mu=1-e^{-1}\) and \(\sigma^2=(3-e)e^{-2}\),

\[
\frac{M_{0,n}-\mu n}{\sqrt n}\ \xrightarrow{\ d\ }\ \mathcal N(0,\sigma^2).
\]

The explicit **variance constant** is the contribution established here. The Gaussian limit without an evaluated constant is already implied by the joint fringe-tree central limit theorems of Holmgren and Janson [2] and is not presented as an independently new central limit theorem.

## Assumptions and scope

The attachment choices at different birth times are independent; the graph is a single uniform recursive tree, not a binary search tree or a preferential-attachment tree. The root is vertex \(1\). Outdegree zero is a *rooted* leaf, whereas degree one defines an *undirected* leaf. The distinction is handled exactly below. The theorem concerns variance at scale \(n\) and a one-dimensional weak limit, not a finite-order variance formula or an entire covariance matrix for all leaf-degree counts.

For vertex \(i\), write \(Y_i\) for its number of children having **no children of their own** at time \(n\). Put \(Q_i={\bf1}\{Y_i=0\}\) and \(Z_n=\sum_{i=1}^n Q_i\). For \(n\ge3\), every undirected leaf other than the root is precisely a rooted leaf, and the only possible discrepancy is an extra leaf neighbor (the root) of vertex \(2\) when the root has only one child. Consequently

\[
0\le Z_n-M_{0,n}\le {\bf1}\{\deg_{T_n}(1)=1\},\qquad
\Pr(\deg_{T_n}(1)=1)=\frac1{n-1}.
\]

## Proof

### 1. Exact joint leaf-child avoidance probabilities

For integers \(r\ge0\), let \((N)_{\underline r}=N(N-1)\cdots(N-r+1)\), with \((N)_{\underline0}=1\); set \(\binom ar=0\) for \(r<0\) or \(r>a\). Fix \(r\) distinct arriving vertices and prescribe a parent for each, with no prescribed parent itself among those \(r\) vertices. The probability that all prescriptions hold and that all \(r\) vertices ultimately have no children is exactly

\[
\frac1{(n-1)_{\underline r}}.
\tag{1}
\]

Indeed, expose the independent parent choices in increasing birth order. Each selected vertex is required to attach to its prescribed parent at birth, and every later arrival must avoid all earlier selected vertices. At each time there is a factor of \(1/(t-1)\) for an appointed arrival and of \((t-1-k)/(t-1)\) when \(k\) selected vertices are already present. Multiplying, and cancelling the consecutive factors for the \(r\) selected vertices, gives (1). Equivalently, one can induct over the last appointed arrival to obtain the same reciprocal falling factorial. The condition on prescribed parents is essential.

Set \(N=n-1\), \(A=n-i\), and for \(i<h\) put \(B=n-h\). Inclusion–exclusion applied to (1) yields

\[
 p_i:=\Pr(Q_i=1)=\sum_{r=0}^{A}(-1)^r
 \frac{\binom Ar}{(N)_{\underline r}}.
\tag{2}
\]

For two distinct vertices, the exact joint expression is

\[
 p_{ih}:=\Pr(Q_i=Q_h=1)
 =\sum_{r\ge0}\sum_{s\ge0}(-1)^{r+s}
 \frac{F_{r,s}}{(N)_{\underline{r+s}}},
\tag{3}
\]

where terms with invalid falling factorials are omitted, and

\[
F_{r,0}=\binom Ar,\qquad
F_{r,s}=\binom Bs\binom{A-1-s}{r}\quad(s\ge1).
\tag{4}
\]

To see (4), choose the \(s\) terminal children of \(h\) among the \(B\) younger labels. Any \(r\) terminal children of \(i\) must then avoid these \(s\) labels **and \(h\) itself**, since \(h\) must have a child; the eligible remaining labels number \(A-1-s\). For \(s=0\) the label \(h\) is eligible for \(i\), as indicated. Formula (1) applies to each valid choice. These expressions contain all label-overlap constraints, including the ancestor–child issue.

Subtracting \(p_ip_h\) from (3), and using \((N)_{\underline{r+s}}=(N)_{\underline s}(N-s)_{\underline r}\), gives an exact covariance representation:

\[
\operatorname{Cov}(Q_i,Q_h)=\sum_{s\ge1}\sum_{r\ge1}
 (-1)^{r+s}\frac{\binom Bs}{(N)_{\underline s}}
 \left\{\frac{\binom{A-1-s}r}{(N-s)_{\underline r}}
 -\frac{\binom Ar}{(N)_{\underline r}}\right\}.
\tag{5}
\]

In (5), the first quotient is defined as zero when \(r>A-1-s\), including when its denominator would otherwise be undefined; the second quotient remains included through \(r=A\). This convention is necessary: terms excluded from the joint event must still be subtracted from the product of marginals. The first-order estimates below use only the region \(r+s\le K_n\) where the product denominators are positive.

### 2. Uniform first-order covariance kernel

Let \(a=(n-i)/n\), \(b=(n-h)/n\); then \(0\le b<a\le1\). Uniformly over all such pairs, we claim

\[
 \Pr(Q_i=1)=e^{-a}+O(n^{-1}),\qquad
 \operatorname{Cov}(Q_i,Q_h)=\frac{c(a,b)}n+o(n^{-1}),
\tag{6}
\]

where the uniform covariance kernel is

\[
 c(a,b)=e^{-a}\Bigl[(1+(a-1)b)e^{-b}-1\Bigr].
\tag{7}
\]

Here is a justification that also controls the small-\(a\), small-\(b\) boundary. For \(r+s\le K_n\), with \(K_n=\lceil4\log n\rceil\), expand the ratios in (5) as products. In particular,

\[
 \frac{\binom{A-1-s}r}{(N-s)_{\underline r}}
 =\frac1{r!}\prod_{u=0}^{r-1}
 \frac{na-(1+s+u)}{n-(1+s+u)},
 \quad
 \frac{\binom Ar}{(N)_{\underline r}}
 =\frac1{r!}\prod_{u=0}^{r-1}\frac{na-u}{n-(1+u)}.
\tag{8}
\]

The difference between the corresponding first-order factors is \(((a-1)s-1)/n\), independent of \(u\). Applying the elementary product-difference expansion therefore yields, uniformly for \(a\in[0,1]\) and \(r+s\le K_n\),

\[
 \frac{\binom{A-1-s}r}{(N-s)_{\underline r}}
 -\frac{\binom Ar}{(N)_{\underline r}}
 =\frac{a^{r-1}((a-1)s-1)}{(r-1)!n}
 + O\!\left(\frac{C(1+r+s)^6}{r!n^2}\right),
\tag{9}
\]

and \(\binom Bs/(N)_{\underline s}=b^s/s!+O(Cs^2/(s!n))\). The important feature is that no division by \(a\) or \(b\) is used. The constants are absolute for sufficiently large \(n\). Summation of the displayed polynomial-weighted factorial errors is \(O(n^{-2})\).

For completeness, truncation is uniformly justified without assuming the inclusion–exclusion sums converge only conditionally. The absolute value of any term of (2) is at most \(1/r!\). For a term of (3), \(F_{r,s}\le\binom Ns\binom{N-s}r\), so its absolute value is at most \(1/(r!s!)\); the same bound holds for terms of the product \(p_ip_h\). Consequently, the total absolute contribution of all terms of degree \(r+s>K_n\) in the joint probability or product of marginals is bounded by

\[
 \sum_{m>K_n}\frac{2^m}{m!}=o(n^{-2}).
\]

This also justifies extending the leading factorial series to infinity. For the truncated terms \(r+s\le K_n\), the product expansions in (8) are uniform and their polynomial-weighted factorial errors have total size \(O(n^{-2})\). The difference of joint and product probabilities is thus uniformly controlled even when either age coordinate is close to a boundary.

Inserting (9) in (5) and summing the limiting absolutely convergent exponential series, we obtain

\[
\begin{split}
 n\operatorname{Cov}(Q_i,Q_h)
 &=\sum_{r,s\ge1}(-1)^{r+s}
 \frac{a^{r-1}b^s}{(r-1)!s!}((a-1)s-1)\\
 &=e^{-a}\bigl[(1+(a-1)b)e^{-b}-1\bigr]+o(1),
\end{split}
\tag{10}
\]

with a uniform \(o(1)\) difference on the discrete triangular domain. Equation (2) is treated by the same factorial expansion, proving its part of (6).

### 3. Sum of diagonal and pair covariances

Since \(\operatorname{Var}(Z_n)=\sum_i\operatorname{Var}(Q_i)+2\sum_{i<h}\operatorname{Cov}(Q_i,Q_h)\), uniformity in (6) and Riemann summation give

\[
\lim_{n\to\infty}\frac{\operatorname{Var}(Z_n)}n
 =D+2I,
\tag{11}
\]

where

\[
 D=\int_0^1 e^{-a}(1-e^{-a})\,da
 =\frac12-e^{-1}+\frac12 e^{-2},
\tag{12}
\]

and, because \(i<h\) means \(a>b\),

\[
\begin{split}
 I&=\int_0^1\int_0^a
 e^{-a}\bigl[(1+(a-1)b)e^{-b}-1\bigr]\,db\,da\\
 &=\frac{5-e^2}{4e^2}.
\end{split}
\tag{13}
\]

Thus \(D+2I=(3-e)e^{-2}\). The Riemann-sum argument uses only bounded continuous functions and the uniform estimates already established.

Finally write \(\delta_n=Z_n-M_{0,n}\). The root estimate in the scope section gives \(\operatorname{Var}(\delta_n)\le\mathbb E\delta_n^2\le1/(n-1)\). Since (11) implies \(\operatorname{Var}(Z_n)=O(n)\), Cauchy–Schwarz gives

\[
 \bigl|\operatorname{Var}(M_{0,n})-\operatorname{Var}(Z_n)\bigr|
 \le2\sqrt{\operatorname{Var}(Z_n)\operatorname{Var}(\delta_n)}+\operatorname{Var}(\delta_n)=O(1).
\tag{14}
\]

This proves the exact limiting variance for undirected leaf degree zero.

### 4. Identification of the normal limit

The same expansion in (6) shows \(\mathbb E M_{0,n}=(1-e^{-1})n+O(1)\). In a rooted recursive tree, let \(L_n\) be the number of childless vertices and \(P_n\) the number of nonchildless vertices with no childless child. Then \(Z_n=L_n+P_n\). The 1-protected count is \(n-L_n\), and the 2-protected count is \(P_n\). Holmgren and Janson [2], Theorem 8.6 and Remark 1.26, prove joint asymptotic Gaussianity of these counts with \(\sqrt n\) normalization. Thus \(Z_n\), being a linear combination, has a Gaussian limit with an unspecified variance parameter, which our calculation (11) evaluates as \((3-e)e^{-2}\). The bounded \(\delta_n\) correction vanishes after division by \(\sqrt n\), and centering by \((1-e^{-1})n\) is valid because the mean discrepancy is \(O(1)\). This establishes the stated limit. The use of the existing joint normality theorem is explicit: the **new** step is identification of its variance for this particular observable.

## Verification

Run `python3 check.py` from the directory containing the embedded files. It uses only the Python standard library. It enumerates every recursive tree of orders \(3\) through \(8\), reconstructs the rooted childless-child indicators directly from parent arrays, and compares every one- and two-vertex probability against the independent alternating-sum formulas (2)–(4) using exact rational arithmetic. It also checks the first and second moments of \(Z_n\) and computes the displayed constant. These are finite consistency checks, not an infinite proof. The infinite assertion follows from the combinatorial and uniform asymptotic argument above together with the cited existing joint CLT.

## Relationship to prior work

Hartle and Krapivsky [1] formulate the leaf-degree statistic \(M_0\), obtain the limiting first-order frequency \(1-e^{-1}\), and discuss approximately Gaussian extensive fluctuations through simulation; their work does not display a proved exact variance coefficient for \(M_0\). Holmgren and Janson [2] already establish the joint normal limit needed for the 1-protected and 2-protected counts, but explicitly note the difficulty of evaluating variances for protected nodes in recursive trees. Mahmoud and Ward [3] derive mean and order-of-magnitude variance statements for protected nodes, not the closed constant for their sum with leaves. Hartle and Krapivsky [4] subsequently study joint degree and leaf-degree **one-vertex limiting frequencies** and selected fluctuations in preferential-attachment trees; their Appendix A on the recursive tree does not derive this second-order global count constant.

Prior general asymptotic normality and first-order counts are acknowledged, not relabeled as discoveries. The distinguishing claim is the closed form \((3-e)/e^2\) for the global count variance in the uniform recursive tree. It requires the nontrivial two-vertex leaf-child exclusion comparison above; it is not obtained by summing one-vertex limiting frequencies.

## Limitations

The result is for the uniform recursive tree and leaf-degree zero alone. It gives neither an exact finite-size variance of \(M_{0,n}\) nor joint asymptotic covariances for all leaf-degree classes. A numerical value of the variance is not a proof of the stated exact constant. General implicit fringe-tree covariance representations may yield the same coefficient after additional computation, so historical-priority comparisons beyond the inspected literature may remain. Independent expert validation of the new covariance-kernel calculation has not been performed.

## References

[1] H. Hartle and P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085 (first publicly posted 2025-11-06), https://arxiv.org/abs/2511.04085 .

[2] C. Holmgren and S. Janson, *Limit laws for functions of fringe trees for binary search trees and random recursive trees*, arXiv:1406.6883 (2014), subsequently Electronic Journal of Probability 20 (2015); Theorem 8.6 and Remark 1.26, https://arxiv.org/abs/1406.6883 .

[3] H. M. Mahmoud and M. D. Ward, *Asymptotic properties of protected nodes in random recursive trees*, Journal of Applied Probability 52 (2015), 290–297, https://doi.org/10.1239/jap/1429282623 .

[4] H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021 (first publicly posted 2026-02-01), Appendix A, https://arxiv.org/abs/2602.01021 .
