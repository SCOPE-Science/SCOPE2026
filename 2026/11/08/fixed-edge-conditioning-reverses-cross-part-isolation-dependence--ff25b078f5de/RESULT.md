# Fixed-edge conditioning reverses cross-part isolation dependence in random bipartite graphs

## Finding

Let \(X\) and \(Y\) count isolated vertices in the two parts of a uniformly selected \(k\)-edge subgraph of \(K_{a,b}\). The exact finite-size result is
\[
\operatorname{Cov}_{k}(X,Y)=ab\left[
\frac{\binom{(a-1)(b-1)}{k}}{\binom{ab}{k}}-
\frac{\binom{ab-b}{k}\binom{ab-a}{k}}{\binom{ab}{k}^{2}}
\right].
\]
It has the sharp sign classification
\[
\operatorname{Cov}_{k}(X,Y)<0\quad\Longleftrightarrow\quad
2\le k\le ab-\max\{a,b\},
\]
and is zero for all remaining allowed integer edge counts. By contrast, in the independent-edge model,
\[
\operatorname{Cov}_{p}(X,Y)=ab\,p(1-p)^{a+b-1}>0\quad(0<p<1).
\]

For positive real constants \(\alpha,\beta,c\) and any integer sequences \(a_n,b_n,k_n\) with \(a_n/n\to\alpha\), \(b_n/n\to\beta\), \(k_n/n\to c\), the sparse fixed-edge and matched independent-edge laws are
\[
\begin{aligned}
\operatorname{Cov}_{k_n}(X,Y)&\longrightarrow
-\frac{c^2}{2\alpha\beta}
\exp\!\left[-c\left(\frac1\alpha+\frac1\beta\right)\right],\\
\frac1n\operatorname{Cov}_{p_n}(X,Y)&\longrightarrow
c\exp\!\left[-c\left(\frac1\alpha+\frac1\beta\right)\right],\quad
p_n=\frac{k_n}{a_nb_n}.
\end{aligned}
\]
In particular, the two ensembles do not merely reverse the covariance sign: their cross-part covariance scales differ by a full factor of the system size. The fixed-edge limiting absolute covariance is maximized over \(c>0\) uniquely at \(c=2\alpha\beta/(\alpha+\beta)\), by differentiating \(c^2e^{-c(1/\alpha+1/\beta)}\).

In the balanced case \(a=b=n\) and \(k=n\), for the matched independent-edge probability \(p=1/n\), the corresponding correlation limits are
\[
\lim_{n\to\infty} n\operatorname{Corr}_{k=n}(X,Y)
=-\frac1{2(e-2)},\qquad
\lim_{n\to\infty}\operatorname{Corr}_{p=1/n}(X,Y)
=\frac1{e-1}.
\]

## Assumptions and scope

The vertex sets are disjoint and labeled, of respective sizes \(a,b\ge2\). Every one of the \(\binom{ab}{k}\) simple bipartite graphs with \(k\) edges is equally likely. An isolated vertex has no selected incident edge; \(X\) counts isolated vertices on the \(a\)-side and \(Y\) those on the \(b\)-side. The comparison model chooses the \(ab\) edges independently, each with common probability \(p\). For every integer \(M\ge0\), set \(\binom Mk=0\) if \(k<0\) or \(k>M\). Thus all displayed finite formulas include degenerate boundaries without division by zero, as \(0\le k\le ab\).

The limits use a deterministic index \(n\to\infty\); no central-limit theorem, convergence in distribution, or independence of the statistics is asserted. The correlation claims concern only the balanced sequences specified above, where the variances are positive for all sufficiently large \(n\).

## Proof

Put \(N=ab\), \(A=N-b\), \(B=N-a\), \(C=N-a-b+1=(a-1)(b-1)\). A specified row is empty precisely when all \(k\) selected cells are in the other \(N-b\) positions, with probability \(u=\binom Ak/\binom Nk\). A specified column has probability \(v=\binom Bk/\binom Nk\). Requiring both excludes their union of \(a+b-1\) cells; hence its probability is \(w=\binom Ck/\binom Nk\). By exchangeability across all \(ab\) row-column pairs, \(\operatorname{Cov}(X,Y)=ab(w-uv)\), proving the exact formula.

If \(k\le\min\{A,B\}\), then \(u,v>0\). In the range \(0\le k\le C+1\), cancellation of falling factorials gives the exact product identity
\[
\frac{w}{uv}=
\prod_{t=0}^{k-1}
\frac{(C-t)(N-t)}{(A-t)(B-t)}=
\prod_{t=0}^{k-1}
\left(1-\frac{t}{(A-t)(B-t)}\right).
\]
Here we used \((C-t)(N-t)-(A-t)(B-t)=-t\). For \(k=0,1\) the product is one. When \(2\le k\le C+1\), all its factors lie in \([0,1]\), and the factor for \(t=1\) is strictly below one, so \(w<uv\). If \(C+1<k\le\min\{A,B\}\), then \(w=0<uv\). Finally, when \(k>\min\{A,B\}\), at least one of \(u,v\) is zero and also \(w=0\). Since \(\min\{A,B\}=N-\max\{a,b\}\), the asserted strict/zero classification follows for every allowed \(k\).

For independent edges, the absence of edges in a row and a column has respective probabilities \((1-p)^b\) and \((1-p)^a\). They share precisely one cell, hence their joint probability is \((1-p)^{a+b-1}\). The difference of joint and product probabilities is \(p(1-p)^{a+b-1}\), giving the opposite sign and exact formula.

For the asymptotic formula, write \(u_n,v_n,w_n\) for the finite probabilities at \(a=a_n,b=b_n,k=k_n\). The product representation of each single-vertex isolation probability implies
\[
u_n\to U=e^{-c/\alpha},\qquad v_n\to V=e^{-c/\beta}.
\]
Since \(a,b\) are of linear order in \(n\), the product ratio above is valid for all sufficiently large \(n\), and uniformly for \(0\le t<k=O(n)\) its factor deficit is \(O(n^{-3})\). The uniform Taylor estimate for \(\log(1-z)\) gives
\[
\log\frac{w_n}{u_nv_n}
=-\sum_{t=0}^{k-1}\frac{t}{(A-t)(B-t)}+O(n^{-4})
=-\frac{c^2}{2\alpha^2\beta^2n^2}+o(n^{-2}).
\]
Consequently, \(w_n-u_nv_n=-UV\,c^2/(2\alpha^2\beta^2n^2)+o(n^{-2})\). Multiply by \(ab\sim\alpha\beta n^2\) to obtain the first limit. For \(p_n=k_n/(a_nb_n)\sim c/(\alpha\beta n)\), the exact independent-edge formula and \((1-p_n)^{a_n+b_n-1}\to UV\) prove the second.

For the correlation refinement, let \(r=\binom{N-2b}{k}/\binom Nk\), the probability that two specified distinct rows are both empty. Then
\[
\operatorname{Var}_k(X)=a\,u(1-u)+a(a-1)(r-u^2),
\qquad
\frac{r}{u^2}=\prod_{t=0}^{k-1}
\left(1-\frac{b^2}{(N-b-t)^2}\right).
\]
In the sparse regime the last logarithm is \(-c/(\alpha^2n)+o(n^{-1})\), giving
\[
\frac{\operatorname{Var}_{k_n}(X)}n\longrightarrow
\alpha U(1-U)-cU^2>0.
\]
Interchanging \(a,b\) gives \(\operatorname{Var}_{k_n}(Y)/n\to\beta V(1-V)-cV^2>0\). Positivity follows from \(1-(1+t)e^{-t}>0\) for \(t>0\). Under independent edges, different rows involve disjoint cells, so \(\operatorname{Var}_p(X)=a(1-p)^b[1-(1-p)^b]\), and likewise for columns. Specializing to \(\alpha=\beta=c=1\) yields the two displayed correlation limits.

## Verification

Run `python verify.py` with Python 3 and the standard library. The checker independently enumerates all binary matrices for \((a,b)\in\{(2,2),(2,3),(3,3),(3,4),(4,4)\}\), compares exact rational mixed moments against the formula for every edge count, checks the strict/zero sign classification for all \(2\le a,b\le12\), checks the product identity, and tests exact independent-edge signs. It also performs numerical sanity checks for the asymptotic constants and variance/correlation normalization; those finite numerical checks are not substituted for the analytic limit proofs. The program reports `PASS: 17150 exact/sign/product/ensemble checks plus sparse-scale sanity checks`.

## Relationship to prior work

McKay and Skerman (2013) explicitly define the uniformly fixed-edge \(\mathcal G_k\) and independent-edge \(\mathcal G_p\) random bipartite graph models and study full degree-sequence approximations. Their Theorem 1 imposes an acceptability condition implying \(p(1-p)=\Omega(1/\log n)\), whereas the present cross-part covariance and correlation limits concern \(p\asymp1/n\); that approximation theorem does not give the displayed sparse limits or a finite exact covariance sign classification. Its general degree-sequence setup is background, not claimed as new.

Strona and collaborators (2014) develop sampling of binary matrices with *both* row and column sums fixed. Under that different null model, the number of zero rows and columns is deterministic from the margins, hence its covariance is identically zero; it cannot imply the cross-part sign reversal in the globally fixed-edge model. Classical matrix-occupancy references of Eicker, Siddiqui and Mielke (1972) and Holst (1980) remain potential sources of implicit coverage; full texts were not available for examination, and this is a priority limitation rather than evidence of novelty.

## Limitations

No claim is made that every historical occupancy identity has been excluded, and the finding has not undergone independent scientific audit. The exact covariance identity may be derivable from general multivariate occupancy theory; priority should be revisited if the older full texts become available. The covariance sign is not a negative-association assertion for arbitrary functions or arbitrary bipartite graphs, and vanishing limiting correlation does not establish independence. The sparse asymptotics require both part sizes to be proportional to the scaling index with positive limits.

## References

1. Brendan D. McKay and Fiona Skerman, *Degree sequences of random digraphs and bipartite graphs*, first arXiv submission 2013-02-11, arXiv:1302.2446, https://arxiv.org/abs/1302.2446 .
2. Giovanni Strona, Domenico Nappo, Francesco Boccacci, Simone Fattorini and Jesus San-Miguel-Ayanz, *A fast and unbiased procedure to randomize ecological binary matrices with fixed row and column totals*, Nature Communications 5, 4114 (2014), https://doi.org/10.1038/ncomms5114 .
3. Patrick J. Eicker, M. M. Siddiqui and Paul W. Mielke Jr., *A matrix occupancy problem*, Annals of Mathematical Statistics 43 (1972), 988–996, https://doi.org/10.1214/aoms/1177692562 . Full text not inspected.
4. Lars Holst, *On matrix occupancy, committee, and capture-recapture problems*, Scandinavian Journal of Statistics 7 (1980), 139–146. Full text not inspected.
