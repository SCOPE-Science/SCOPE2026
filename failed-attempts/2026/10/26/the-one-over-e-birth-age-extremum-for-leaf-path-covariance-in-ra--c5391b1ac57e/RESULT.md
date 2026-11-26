# The one-over-e birth-age extremum for leaf–path covariance in random recursive trees

## Finding

Let \(T_n\) be the uniform random recursive tree on the birth-labelled vertices \(1,\ldots,n\), with root \(1\). Write \(P_n\) for the sum of the distances from the root to all vertices, and \(X_{n,i}\) for the indicator that the vertex born at time \(i\) is a leaf (has no children). For every \(n\ge2\) and \(2\le i\le n\),

\[
\operatorname{Cov}(X_{n,i},P_n)=\frac{i-1}{n-1}\bigl(H_{i-1}-H_{n-1}\bigr),\qquad H_m=\sum_{j=1}^{m}\frac1j.
\]

The covariance is negative for \(2\le i<n\), and zero for \(i=n\). For each \(n\ge3\), a **unique** birth label \(i_n\) minimizes this covariance. It is exactly determined by

\[
i_n=1+\min\bigl\{1\le k\le n-1:\ H_{n-1}-H_k<1\bigr\}.
\]

In particular,

\[
\frac{i_n}{n}\longrightarrow e^{-1},\qquad
\min_{2\le i\le n}\operatorname{Cov}(X_{n,i},P_n)\longrightarrow-e^{-1}
\quad(n\to\infty).
\]

A distributional deletion-and-reinsertion identity gives the profile: conditional on \(X_{n,i}=1\), remove birth-label \(i\), compress larger labels by one, and retain the resulting tree. The result is a **uniform random recursive tree on \(n-1\) vertices** independent of the removed leaf's parent, which is uniform among the first \(i-1\) vertices. Consequently, if \(T^*_{n-1}\) is a fresh uniform recursive tree, \(U\) is uniform on \(\{1,\ldots,i-1\}\) independently of it, and \(D^*(u)\) denotes its depth at vertex \(u\), then

\[
\mathcal L(P_n\mid X_{n,i}=1)
=\mathcal L\bigl(P(T^*_{n-1})+1+D^*(U)\bigr).
\]

## Assumptions and scope

Every new vertex \(j\in\{2,\ldots,n\}\) chooses its parent \(U_j\) independently and uniformly from \(\{1,\ldots,j-1\}\). The tree is rooted at \(1\); leaves mean vertices with *zero children*, not undirected degree-one vertices. For \(n\ge2\) the root is never a leaf, and the last-born vertex is always a leaf. All statements are exact at finite order. The unique minimizer is asserted only when \(n\ge3\). No limiting distribution or independent statistical validation is asserted.

## Proof

**Step 1: conditional sampling and exact distribution.** For \(j>i\), the event \(X_{n,i}=1\) is exactly \(U_j\ne i\). Independence gives

\[
\Pr(X_{n,i}=1)=\prod_{j=i+1}^n\frac{j-2}{j-1}=\frac{i-1}{n-1}.
\]

Given this event, the variables \(U_j\) for \(j>i\) remain independent, each uniform on \(\{1,\ldots,j-1\}\setminus\{i\}\); variables \(U_j\) for \(j\le i\) keep their original independent uniform laws. Delete leaf \(i\), and map each surviving label \(j>i\) to \(j-1\). Each surviving vertex then chooses an independent uniform parent among all smaller surviving labels. Thus the reduced tree has the uniform recursive-tree law on \(n-1\) vertices. The original parent \(U_i\), uniform on \(\{1,\ldots,i-1\}\), is independent of that reduced tree. Reinserting \(i\) as a leaf at parent \(U_i\) increases total path length by exactly \(1+D^*(U_i)\), proving the distributional identity above.

**Step 2: the marked covariance.** Let \(H_0=0\). The growth recurrence for expected path length is

\[
\mathbb E P_m=\mathbb E P_{m-1}+1+\frac{\mathbb E P_{m-1}}{m-1},
\]

with \(\mathbb E P_1=0\), hence \(\mathbb E P_m=m(H_m-1)\). The first \(i-1\) vertices of \(T^*_{n-1}\) form a uniform recursive tree of order \(i-1\), so

\[
\mathbb E D^*(U_i)=\frac{1}{i-1}\sum_{u=1}^{i-1}\mathbb E D^*(u)=H_{i-1}-1.
\]

The distributional identity therefore yields

\[
\mathbb E[P_n\mid X_{n,i}=1]
=(n-1)(H_{n-1}-1)+H_{i-1}.
\]

Subtract \(\mathbb E P_n=n(H_n-1)\) and multiply by \(\Pr(X_{n,i}=1)\). This proves the displayed covariance formula. Its sign follows strictly from harmonic-number monotonicity, except when \(i=n\).

**Step 3: uniqueness at every order.** Put \(N=n-1\), \(k=i-1\), and \(f_N(k)=k(H_k-H_N)\) for \(1\le k\le N\). Since the factor \(1/N\) is positive, minimizing covariance means minimizing \(f_N\). For \(1\le k<N\),

\[
f_N(k+1)-f_N(k)=1-(H_N-H_k).
\]

This difference strictly increases with \(k\). It is also never zero: a sum of reciprocals of consecutive integers \(a,a+1,\ldots,b\) with \(a\ge2\) cannot equal \(1\). To see this, if there is only one term then it is less than \(1\); otherwise the interval contains an even number, and there is a unique denominator divisible by the highest power of \(2\) among the denominators (two such denominators would enclose a multiple of the next higher power). Multiplying the sum by the least common multiple gives an odd contribution from this unique denominator and even contributions from all others, so the sum cannot be an integer. Therefore the differences cross strictly from negative to positive, or are positive from the outset, and there is one minimizer, exactly at the stated first index \(k\) with \(H_N-H_k<1\).

**Step 4: asymptotic position and strength.** Uniformly for \(k/N\) bounded away from \(0\), the integral comparison for harmonic numbers yields \(H_N-H_k=\log(N/k)+o(1)\). The exact threshold in Step 3 therefore implies \(k/N\to e^{-1}\). The extremal covariance equals \((k/N)(H_k-H_N)\to-e^{-1}\), as claimed.

**Consistency with the unmarked statistic.** Writing \(L_n=\sum_{i=2}^{n}X_{n,i}\), the identity \(\sum_{k=1}^N kH_k=\frac{N(N+1)}2H_N-\frac{N(N-1)}4\) gives \(\operatorname{Cov}(L_n,P_n)=-(n-2)/4\). This *unmarked aggregate identity is not asserted to be new*; it is accessible from previously published joint generating-function methods.

## Verification

A standalone checker, `verify.py`, enumerates all \((n-1)!\) recursive trees for each \(2\le n\le9\) with integer parent arrays. For each permissible leaf mark it checks the deletion-and-parent bijection directly and evaluates conditional means, marked covariances, and the aggregate covariance with exact rational arithmetic. It separately verifies the unique harmonic-threshold minimizer for every \(3\le n\le300\). Its latest observed output ends with `VERIFY_OK`. These finite checks corroborate but do not replace the unrestricted arguments above.

## Relationship to prior work

Eslava's first-public November 2016 paper (arXiv:1611.07466) studies the joint asymptotic behavior of the depths and *large* degrees of vertices in random recursive trees (primary MSC 60C05). It neither marks an ordinary vertex of **specified birth label** conditioned to have zero children nor analyzes its covariance with the *total* path length. Grübel and Michailow study recursive-tree boundary limits and global path-length functionals, but no analogous birth-marked leaf conditioning appears in the inspected work.

Lundblad and Wagner (2026) consider joint path length, external path length, and the unmarked number of leaves. Their recursive-tree generating function \(F_r(x,y,z,u)\) has variables for these aggregate statistics (Equation (13)). It can cover the unmarked covariance \(\operatorname{Cov}(L_n,P_n)\); the present new claim is instead the **birth-indexed conditional law and its unique finite-order extremizer**. Their displayed generating function neither retains the individual birth index nor directly supplies the claimed conditional distribution or index threshold. Two related published records investigate root-attachment versus path length and root degree versus total leaves, neither of which has the marked-leaf conditioning event. These differences are comparisons of statistical objects and implications, not merely terminology.

## Limitations

The theorem concerns uniform recursive trees, parent labels rather than degree-ranked vertices, and the covariance (not the Pearson correlation). It gives an exact conditional path-length law via another random tree, rather than a closed-form univariate probability distribution or higher conditional moments. An earlier marked-tree insertion statement might exist in the broad recursive-tree literature; historical priority is therefore not guaranteed. The aggregate covariance alone is not offered as an original result. Finite checks do not establish uniqueness outside their tested ranges; Step 3 does.

## References

1. Laura Eslava, *Depth of vertices with high degree in random recursive trees*, first arXiv version November 22, 2016, arXiv:1611.07466, https://arxiv.org/abs/1611.07466 (primary MSC 60C05).
2. Rudolf Grübel and Igor Michailow, *Random recursive trees: A boundary theory approach*, arXiv:1406.7614, https://arxiv.org/abs/1406.7614.
3. Robert P. Dobrow and James Allen Fill, *Total Path Length for Random Recursive Trees*, Combinatorics, Probability and Computing 8 (1999), 317–333, https://doi.org/10.1017/S0963548399003855.
4. Jacob Lundblad and Stephan Wagner, *Path Length and External Path Length in Random Trees*, LIPIcs AofA 2026, https://doi.org/10.4230/LIPIcs.AofA.2026.2, specifically the joint aggregate generating function in Equation (13).
