# Birth-indexed leaf status and total path length in uniform recursive trees

## Finding

Let \(n\ge2\). For a uniform random recursive tree on labels \(1,\ldots,n\), let \(T_n\) denote the sum of distances from the root to all vertices and let \(X_{n,j}\) indicate that vertex \(j\) is a leaf (has no children). Write \(H_0=0\) and \(H_k=\sum_{r=1}^k 1/r\). For all \(2\le j\le n\),

\[
\mathbb E[T_n\mid X_{n,j}=1]
=n(H_n-1)-(H_{n-1}-H_{j-1}),
\]

and hence

\[
\operatorname{Cov}(T_n,X_{n,j})
=-\frac{j-1}{n-1}(H_{n-1}-H_{j-1}).
\]

For \(j=1\), \(X_{n,1}=0\) almost surely, and the covariance is zero. The covariance is strictly negative for every \(2\le j<n\), and zero for \(j=n\). Summing the positionwise identity gives the exact global law

\[
\operatorname{Cov}(T_n,L_n)=-\frac{n-2}{4},
\qquad L_n=\sum_{j=1}^{n}X_{n,j}.
\]

The magnitude of the indexed covariance has a strictly concave, unimodal finite profile on \(j=2,\ldots,n\): the adjacent difference of its magnitude equals

\[
\frac{H_{n-1}-H_{j-1}-1}{n-1}
\quad(2\le j<n).
\]

It therefore has at most two adjacent maximizing indices. In the bulk regime \(j/n\to\alpha\in(0,1)\),

\[
\operatorname{Cov}(T_n,X_{n,j})\longrightarrow \alpha\log\alpha,
\]

and every maximizing index satisfies \(j/n\to e^{-1}\), with maximal covariance magnitude tending to \(e^{-1}\).

## Assumptions and scope

The tree grows from vertex \(1\). Independently for each \(k=2,\ldots,n\), vertex \(k\) chooses its parent uniformly from \(1,\ldots,k-1\). Depth is the graph distance to vertex \(1\). A leaf is a vertex with zero children; this definition makes vertex \(n\) a leaf with probability one. No conditioning on tree shape, degree sequence, or total number of leaves is imposed. All finite formulas are exact for the stated integer ranges. In particular, the conditional expectation exists because \(\Pr(X_{n,j}=1)>0\) for \(j\ge2\).

## Proof

Write \(P_k\) for the parent of vertex \(k\), and \(D_k\) for its depth. Since \(D_k=1+D_{P_k}\) and the parents are independent and uniform,

\[
\mathbb E[D_k]=H_{k-1},\qquad
\mu_k:=\mathbb E[T_k]=k(H_k-1).
\]

Fix \(2\le j\le n\), and set \(E_j=\{X_{n,j}=1\}\). This event is exactly \(P_k\ne j\) for every \(k=j+1,\ldots,n\). Independence of the parent choices implies that, conditioned on \(E_j\), each subsequent parent \(P_k\) is still independent and uniform among the \(k-2\) labels different from \(j\). Thus

\[
\Pr(E_j)=\prod_{k=j+1}^{n}\frac{k-2}{k-1}
=\frac{j-1}{n-1}.
\]

The parent choices through time \(j\) remain unconditioned; therefore \(\mathbb E[D_j\mid E_j]=H_{j-1}\). Set \(a_k=\mathbb E[T_k\mid E_j]\) for \(k\ge j\). At \(k=j\), \(a_j=\mu_j\). When vertex \(k+1\) arrives, the conditional average depth of an eligible parent is
\((a_k-H_{j-1})/(k-1)\), since vertex \(j\) is excluded. Consequently,

\[
 a_{k+1}=\frac{k}{k-1}a_k+1-\frac{H_{j-1}}{k-1}
\quad(j\le k<n).
\]

Subtracting \(\mu_{k+1}=(k+1)(H_{k+1}-1)\), or simply substituting into this recurrence, proves inductively that

\[
 a_k-\mu_k=-(H_{k-1}-H_{j-1})
\quad(j\le k\le n).
\]

The asserted conditional mean follows at \(k=n\). For a Bernoulli indicator \(X_{n,j}\),

\[
 \operatorname{Cov}(T_n,X_{n,j})
 =\Pr(E_j)\bigl(\mathbb E[T_n\mid E_j]-\mathbb E[T_n]\bigr),
\]

which proves the local covariance law, including its strict sign. For the root, \(P_2=1\) deterministically, so \(X_{n,1}=0\).

Linearity of covariance and a change in summation order yield

\[
\begin{aligned}
\operatorname{Cov}(T_n,L_n)
&=-\frac1{n-1}\sum_{j=2}^{n-1}(j-1)\sum_{k=j}^{n-1}\frac1k\\
&=-\frac1{2(n-1)}\sum_{k=2}^{n-1}(k-1)
=-\frac{n-2}{4}.
\end{aligned}
\]

Finally, set \(f_n(j)=-\operatorname{Cov}(T_n,X_{n,j})\) for \(j\ge2\). The displayed adjacent-difference formula follows by subtracting \((j-1)(H_{n-1}-H_{j-1})/(n-1)\) at consecutive indices. Since its numerator decreases strictly with \(j\), the profile is strictly discretely concave; any maximum occurs at one index or two adjacent indices. For \(j/n\to\alpha\in(0,1)\), harmonic asymptotics give \(f_n(j)\to-\alpha\log\alpha\). This limiting profile has its unique maximizer \(\alpha=e^{-1}\). The endpoints cannot carry an asymptotically maximal value: uniformly for \(j/n\le\varepsilon\), \(f_n(j)\le (j/n)(1+\log(n/j))\), which approaches zero with \(\varepsilon\), while for \(j/n\ge1-\varepsilon\), \(f_n(j)\le \varepsilon+o(1)\). Therefore every sequence of maximizing indices has the stated limit, and the maximal value tends to \(e^{-1}\).

## Verification

The standalone Python 3 standard-library program `verify.py` exhaustively enumerates all \((n-1)!\) parent sequences for each \(2\le n\le9\), calculating every local mixed moment, conditional expectation, global covariance, and boundary case with exact rational arithmetic. It also checks the conditional-mean recurrence for \(2\le n\le159\). Running `python3 verify.py` produced `PASS: 669769 mathematical exact assertions, 46233 enumerated trees, n<=9 exhaustive, recurrences through n=159`. These finite checks are evidence for implementation correctness, not substitutes for the induction and summation proof for all \(n\).

## Relationship to prior work

Dobrow and Fill (1999) analyze moments and distributional limits of total path length in uniform recursive trees, without marking a specified birth-index leaf event in their investigated theorems. Janson (2004) studies aggregate degree distributions in random recursive trees rather than their birth-indexed cross-covariance with total path length. Gopaladesikan (2014) studies fringe motifs and separately a recursive block-growth model; its accessible abstract does not settle this indexed covariance. Lundblad and Wagner (2026) analyze global leaf counts, path length and external path length via multivariate generating functions; their global markers could yield aggregate covariance information but do not isolate the birth index in the displayed model. The present result is the finite indexed conditional-mean and covariance profile; the global covariance formula is a corollary rather than a separately claimed innovation.

## Limitations

The result applies only to uniform recursive trees and to first mixed moments. It does not establish a joint limit law, independence, or stochastic ordering. Literature priority is not independently certified: an implicit older specialization may exist in the literature on random increasing-tree profiles and mixed moments. Relevant full texts and accessible source summaries were compared, but not every historical result can be excluded.

## References

1. R. P. Dobrow and J. A. Fill, *Total Path Length for Random Recursive Trees*, Combinatorics, Probability and Computing **8** (1999), 317–333. DOI: https://doi.org/10.1017/S0963548399003855 (first public online date: 1999-07-01).
2. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms (2004). DOI: https://doi.org/10.1002/rsa.20046.
3. M. Gopaladesikan, *On the occurrences of motifs in recursive trees, with applications to random structures*, doctoral dissertation, Purdue University (2014). https://docs.lib.purdue.edu/open_access_dissertations/274/.
4. J. Lundblad and S. Wagner, *Path Length and External Path Length in Random Trees*, AofA 2026, LIPIcs **381**, article 2 (2026). DOI: https://doi.org/10.4230/LIPIcs.AofA.2026.2.
