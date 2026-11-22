# Opposite finite covariances and joint limit decoupling in random threshold digraphs

## Finding

Let \(n\ge2\). Independently sample \((U_i,V_i)\), \(1\le i\le n\), with both coordinates uniform on \([0,1]\), and put the directed arc \(i\to j\), for distinct labels, exactly when \(U_i+V_j>1\). Write \(S_n\) for the number of vertices of out-degree zero, \(T_n\) for the number of vertices of in-degree zero, and \(R_n\) for the number of unordered vertex pairs carrying both directed arcs. Then

\[
\begin{aligned}
\mathbb E S_n&=\mathbb E T_n=1,\\
\mathbb E R_n&=\tfrac14\binom n2,\\
\operatorname{Var}(R_n)&=\tfrac3{16}\binom n2+\tfrac7{24}\binom n3,\\
\operatorname{Cov}(S_n,R_n)&=\operatorname{Cov}(T_n,R_n)=-\frac{n(n-1)}{2(n+2)},\\
\operatorname{Cov}(S_n,T_n)&=\frac{2n-1}{n(n-1)}-n\frac{(n-1)!(n-2)!}{(2n-2)!}>0.
\end{aligned}
\]

Moreover, jointly as \(n\to\infty\),

\[
\left(S_n,T_n,\frac{R_n-\binom n2/4}{n^{3/2}}\right)
\ \xrightarrow{d}\ (G_1,G_2,Z),
\]

where all three limit variables are independent, \(\Pr(G_a=k)=2^{-k-1}\) for \(k=0,1,2,\ldots\), and \(Z\sim N(0,7/144)\). The finite-sample sink/source covariances with reciprocal pairs are therefore strictly negative, while the sink/source covariance is strictly positive, even though the limiting variables decouple on their natural scales.

## Assumptions and scope

The directed graph is loopless. Each \(U_i\) and \(V_i\) is independent uniform on \([0,1]\), with no additional conditional graph sampling. A reciprocal pair requires both arcs and is counted once. The results hold for every integer \(n\ge2\); the limit uses \(n\to\infty\), with no sparsification or tuning of the threshold. A source here means zero in-degree and a sink means zero out-degree; \(S_n\) is the sink count and \(T_n\) the source count.

## Proof

**1. Reciprocity moments.** Set \(W_i=1-V_i\). Arc \(i\to j\) occurs exactly when \(U_i>W_j\). Define \(h_{ij}=\mathbf1\{U_i>W_j,\ U_j>W_i\}\). Each directed arc indicator inside \(h_{ij}\) uses disjoint independent coordinates, so \(\mathbb Eh_{ij}=1/4\) and \(\operatorname{Var}(h_{ij})=3/16\). For distinct \(i,j,k\), conditioning on \((U_i,W_i)\) yields

\[
\mathbb E[h_{ij}\mid U_i,W_i]=U_i(1-W_i),\qquad
\operatorname{Cov}(h_{ij},h_{ik})=\operatorname{Var}(U_i(1-W_i))=\frac7{144}.
\]

Disjoint unordered pairs are independent. Counting \(3\binom n3\) pairs of reciprocal-pair indicators that share one vertex, and remembering the factor \(2\) in a variance expansion, gives the stated variance and mean.

**2. Sink–reciprocity covariance.** Let \(A_i\) indicate that vertex \(i\) has out-degree zero. Conditioning on \(U_i=t\), the event \(A_i\) requires \(V_j<1-t\) for all \(j\ne i\). Thus \(\Pr(A_i)=\int_0^1(1-t)^{n-1}\,dt=1/n\). For \(j\ne i\), \(A_ih_{ij}=0\). If \(i,j,k\) are distinct, integrating first over the two receiver weights yields

\[
\Pr(A_i=1,h_{jk}=1)
=\int_0^1(1-t)^{n-3}
\left(\int_0^{1-t}v\,dv\right)^2dt
=\frac1{4(n+2)}.
\]

The integrand arises because, at fixed receiver weights \(V_j,V_k\), the two arcs \(j\leftrightarrow k\) appear with probability \(V_jV_k\). Therefore

\[
\begin{aligned}
\operatorname{Cov}(S_n,R_n)&=n\left[
(n-1)\left(-\frac1{4n}\right)
+\binom{n-1}{2}\left(\frac1{4(n+2)}-\frac1{4n}\right)
\right]\\
&=-\frac{n(n-1)}{2(n+2)}.
\end{aligned}
\]

Reversing all arcs exchanges \(U_i\) and \(V_i\) in distribution, so the same formula holds for \(T_n\).

**3. Sink–source covariance.** Write \(B_i\) for zero in-degree. The events \(A_i,B_i\) depend on disjoint groups of random coordinates and are independent, so \(\Pr(A_iB_i)=n^{-2}\). For \(i\ne j\), setting \(x=U_i\), \(y=1-V_j\), we need \(x<y\), all other receiver thresholds greater than \(x\), and all other sender weights below \(y\). Hence

\[
\Pr(A_iB_j)=\int_0^1\int_x^1(1-x)^{n-2}y^{n-2}\,dy\,dx
=\frac1{(n-1)^2}-\frac{\mathrm B(n,n-1)}{n-1},
\]

with \(\mathrm B(n,n-1)=(n-1)!(n-2)!/(2n-2)!\). Summing the \(n(n-1)\) off-diagonal pairs and subtracting \(\mathbb ES_n\mathbb ET_n=1\) gives the formula. It is strictly positive: \(\mathrm B(n,n-1)=1/[(n-1)\binom{2n-2}{n-1}]\le1/[n(n-1)]\) for \(n\ge2\), so \(\operatorname{Cov}(S_n,T_n)\ge1/n>0\). In particular, this covariance is \(2/n+O(n^{-2})\).

**4. Boundary-count coupling.** With \(W_i=1-V_i\), define proxy counts

\[
\widetilde S_n=\#\{i:U_i<\min_jW_j\},\qquad
\widetilde T_n=\#\{i:W_i>\max_jU_j\}.
\]

For a row other than the label attaining the smallest \(W\), the out-degree-zero condition is exactly \(U_i<\min W\). The exceptional row instead compares its \(U_i\) with the second-smallest \(W\). Since \(U_i\) is independent of the \(W\)'s, \(\Pr(S_n\ne\widetilde S_n)\le\mathbb E(W_{(2)}-W_{(1)})=1/(n+1)\). The analogous argument for the column containing the largest \(U\) gives \(\Pr(T_n\ne\widetilde T_n)\le1/(n+1)\).

The four lower and upper endpoint processes of the independent uniform arrays converge jointly to four independent unit-intensity Poisson point processes on \([0,\infty)\). For example, the lower processes are \(\sum_i\delta_{nU_i}\) and \(\sum_i\delta_{nW_i}\); the upper processes use \(n(1-U_i)\) and \(n(1-W_i)\). A bounded endpoint window has probability \(O(1/n)\) per array index, and overlapping windows on the same coordinate are disjoint for large \(n\), while simultaneous rare extremes in its two independent coordinates have probability \(O(1/n^2)\). The joint Laplace functional therefore factors in the limit. Consequently \(\widetilde S_n\) counts lower-\(U\) Poisson points preceding the first lower-\(W\) point, while \(\widetilde T_n\) counts upper-\(W\) points preceding the first upper-\(U\) point. Each is geometric with parameter \(1/2\), and they are independent. The mapping from point measures to these counts is almost surely continuous at the four Poisson limits (no tied points or missing first points). The coupling errors vanish, proving the joint geometric convergence.

**5. Joint Gaussian component and independence.** The symmetric reciprocal kernel \(h((U,W),(U',W'))\) has first projection \(g(U,W)=U(1-W)\), with \(\mathbb Eg=1/4\) and \(\operatorname{Var}(g)=7/144\). Hoeffding's decomposition gives

\[
R_n-\mathbb ER_n=(n-1)\sum_{i=1}^n(g(U_i,W_i)-1/4)+D_n,
\qquad \mathbb ED_n^2=O(n^2).
\]

Hence \(D_n/n^{3/2}\to0\) in \(L^2\), and the ordinary iid central limit theorem yields the stated normal marginal. To see that it is independent of all four limiting endpoint processes, fix compactly supported nonnegative continuous test functions for these processes and a real \(t\). The joint Laplace–Fourier transform is the \(n\)-th power of one-index expectations. A one-index endpoint event has probability \(O(n^{-1})\), its mixed contribution with \(e^{it(g-1/4)/\sqrt n}-1\) is \(O(n^{-3/2})\), and the ordinary centered characteristic-function contribution is \(-t^2(7/144)/(2n)+o(n^{-1})\). Thus the exponent has no mixed term in the limit. The Gaussian is independent of the four Poisson processes, and hence of the two geometric counts obtained from them. Slutsky's theorem completes the joint limit.

## Verification

Running `python check.py` produces 1,221 exact assertions. For \(n=2,3,4\) it enumerates all orders of the \(2n\) independent sender and receiver ranks and compares seven exact moment and covariance identities; it also tests sign conditions for \(2\le n<400\). Using ranks is exact because all \(2n\) transformed coordinates are independent continuous uniforms. These finite computations are consistency checks, not proofs of the distributional limit or the universal finite formulas.

## Relationship to prior work

Reilly, Scheinerman and Zhang (2014) introduced this uniform-weight random threshold digraph and proved exact sink-count distributions, the one-dimensional geometric sink limit (Proposition 22 and Corollary 23), the probability of no sinks and no sources (Proposition 24), and a Gaussian limit for the total **directed-arc** count (Theorem 19). The present claim does **not** present any of those results as new. The objects newly combined here are the full joint sink–source limit, reciprocal rather than directed-arc counts, their joint Gaussian decoupling, and the three exact cross-covariances. In particular, knowing the two marginals and the probability of simultaneous zero counts does not determine the full joint law. General U-statistic and independent-extreme-value principles underpin the proof, but do not themselves state these model-specific finite covariance identities. Cloteaux et al. (2014) describe structural characterizations of threshold digraphs, not this sampling-law comparison.

## Limitations

This theorem concerns the uniform independent two-weight model, not fixed-outdegree digraphs, independently sampled arcs, arbitrary weight distributions, or weighted thresholds. The Gaussian scaling is \(n^{3/2}\); the sink/source counts remain order one. Exact finite-sample *joint distributions* of all three counts and quantitative rates of joint convergence are not claimed. Broad historical priority for this exact covariance/joint-limit package is not independently certified; general extremal-process theorems may contain parts of the limiting argument.

## References

1. E. Reilly, E. Scheinerman and Y. Zhang, *Random Threshold Digraphs*, Electronic Journal of Combinatorics **21** (2014), P2.48. First publicly verified date: 2014-06-09. https://doi.org/10.37236/4050 ; full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p48/pdf/
2. B. Cloteaux, M. D. LaMar, E. Moseman and J. Shook, *Threshold Digraphs*, Journal of Research of the National Institute of Standards and Technology **119** (2014), 227–234. https://doi.org/10.6028/jres.119.007 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4597423/
3. W. Hoeffding, *A Class of Statistics with Asymptotically Normal Distribution*, Annals of Mathematical Statistics **19** (1948), 293–325. https://doi.org/10.1214/aoms/1177730196
