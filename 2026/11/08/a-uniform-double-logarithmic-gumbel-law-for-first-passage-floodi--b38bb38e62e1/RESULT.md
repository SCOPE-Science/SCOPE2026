# A uniform double-logarithmic Gumbel law for first-passage flooding on clique bouquets

## Finding
Let \(B_{m,k}=K_1\vee(mK_k)\) be the graph of \(m\) disjoint \(k\)-vertex cliques joined to a common hub \(o\), with independent mean-one exponential edge lengths. Let \(T_{m,k}\) be the maximum weighted shortest-path distance from \(o\) to any vertex. For **every** integer sequence \(k=k_m\ge2\), with no restriction on its growth relative to \(m\to\infty\), put
\[
 b_{m,k}=2\log(k-1)+\log m+\log\log m.
\]
Then, uniformly over \(k\ge2\), for each fixed real \(x\),
\[
 \Pr\{kT_{m,k}\le b_{m,k}+x\}\longrightarrow \exp(-e^{-x}).
\]
More precisely, if \(R_k\) is the flood time from the hub in one clique of order \(k+1\), then
\[
 m\Pr\{kR_k>b_{m,k}+x\}=e^{-x}\left[1+\frac{\log\log m+x+1+\delta_k}{\log m}\right]+O_x\!\left(\frac{m^{-1/12}}{\log m}\right),
\qquad \delta_k=2\log(k-1)-\frac{2k}{k-1}H_{k-2},
\]
where \(H_0=0\), \(H_j=\sum_{r=1}^{j}r^{-1}\), and the implied constant does not depend on \(k\ge2\). In particular, the marked point process of centered individual-petal completion times, with the uniformly distributed mark defined below, converges on regions bounded below in the time coordinate to a Poisson point process on \(\mathbb R\times[0,1]\) of intensity \(e^{-x}\,dx\,du\). The first and last exploration holding times within each petal, multiplied by \(k\), are independent rate-one exponentials, and their ratio \(U\) is exactly uniform on \([0,1]\) and independent of the petal completion time. For the boundary case \(k=1\), \(T_{m,1}-\log m\) converges to standard Gumbel, **without** the \(\log\log m\) correction.

## Assumptions and scope
All graphs are finite, simple and unweighted before edge lengths are assigned. Every edge has an independent \(\operatorname{Exp}(1)\) passage length; the root is the shared hub. The random metric is the sum of edge lengths along a minimum-weight path. The asymptotic limit takes \(m\to\infty\) over positive integers, while \(k=k_m\ge2\) may grow arbitrarily, remain fixed or oscillate. The process uses no recoveries and is not a contact process with healing. The point process convergence is vague on sets bounded below in their first coordinate, and is described equivalently by joint Poisson convergence of counts on finitely many disjoint bounded time windows with arbitrary mark intervals whose boundaries have zero Lebesgue measure.

## Proof
**1. Clique-petal factorization.** All paths from the hub to a vertex in one petal can be confined to that petal: a detour through another petal must revisit the hub and has strictly positive excess length. Distinct petals have disjoint edge sets and hence independent completion times. Consequently \(T_{m,k}=\max_{1\le j\le m}R_{k,j}\) with i.i.d. copies \(R_{k,j}\) of the single-clique completion time.

**2. Exact exponential increments.** In the usual exponential first-passage exploration of \(K_{k+1}\), when \(i\) vertices have been reached, exactly \(i(k+1-i)\) edges cross the infected--uninfected cut. Memorylessness makes the next waiting time exponential with that rate; fresh residual clocks and the strong Markov property make the successive waiting times independent. Thus
\[
 kR_k\ \overset{d}=\ \sum_{i=1}^{k}E_i,\qquad E_i\sim\operatorname{Exp}(\lambda_i)\ \text{independent},\qquad \lambda_i=\frac{i(k+1-i)}k.
\]
Both endpoint rates are \(\lambda_1=\lambda_k=1\). The other rates satisfy \(\lambda_i-1=(i-1)(k-i)/k>0\). For \(k=2\), the intermediate sum is empty. Setting \(S_k=\sum_{i=2}^{k-1}E_i\), the first and last terms are independent \(\operatorname{Exp}(1)\) variables. Their ratio \(U=E_1/(E_1+E_k)\) is \(\operatorname{Uniform}[0,1]\) and independent of \(E_1+E_k\), hence also of \(kR_k\).

**3. Tilted law and exact leading pole.** Define a law \(Q_k\) on \(S_k\) by \(dQ_k/dP=e^{S_k}/A_k\), where
\[
 A_k=\mathbb E e^{S_k}=\prod_{i=2}^{k-1}\frac{\lambda_i}{\lambda_i-1}
 =\prod_{i=2}^{k-1}\frac{i(k+1-i)}{(i-1)(k-i)}=(k-1)^2.
\]
Under \(Q_k\), the summands of \(S_k\) remain independent exponentials of rates \(\lambda_i-1\). Their sum has mean
\[
 \mu_k=\mathbb E_{Q_k}S_k
 =\sum_{i=2}^{k-1}\frac{k}{(i-1)(k-i)}
 =\frac{2k}{k-1}H_{k-2}.
\]
The difference \(2\log(k-1)-\mu_k=\delta_k\) is uniformly bounded in \(k\ge2\): this follows directly from \(\log(n+1)\le H_n\le1+\log n\) and the fact that \(\log(k-1)/(k-1)\) is bounded.

**4. Uniform tilted concentration.** The smallest tilted rate is at least \(1/3\) for all \(k\ge3\). With \(j=i-1\) and its reflected partner, \(1/(\lambda_i-1)\le3/\min(j,k-1-j)\). Thus
\[
 \sup_{k\ge2}\operatorname{Var}_{Q_k}(S_k)
 =\sup_k\sum_{i=2}^{k-1}(\lambda_i-1)^{-2}
 \le18\sum_{j\ge1}j^{-2}<\infty.
\]
At \(t=1/6\), each \(t/(\lambda_i-1)\le1/2\). Since \(-\log(1-z)-z\le z^2\) for \(0\le z\le1/2\), the centered exponential moment obeys
\[
 \sup_{k\ge2}\mathbb E_{Q_k}\exp\{t(S_k-\mu_k)\}<\infty.
\]
The exponential Markov inequality and integrated upper-tail inequality therefore give, uniformly in \(k\),
\[
 Q_k(S_k>\mu_k+z)+\mathbb E_{Q_k}(S_k-\mu_k-z)_+\le C e^{-z/6}\quad(z\ge0).
\]

**5. Sharp uniform survival estimate.** The sum of two independent rate-one exponentials has survival \(e^{-u}(1+u)\) for \(u\ge0\). Conditioning on \(S_k\), then changing to \(Q_k\), gives the exact identity, for any \(y\ge0\),
\[
 \Pr(kR_k>y)= A_ke^{-y}\mathbb E_{Q_k}\big[(1+y-S_k)\mathbf1_{\{S_k\le y\}}\big]
 +A_k\mathbb E_{Q_k}\big[e^{-S_k}\mathbf1_{\{S_k>y\}}\big].
\]
The right-hand side differs from \(A_ke^{-y}(1+y-\mu_k)\) in absolute value by at most
\[
 A_ke^{-y}\big[2Q_k(S_k>y)+\mathbb E_{Q_k}(S_k-y)_+\big].
\]
Take \(y=b_{m,k}+x\). We have \(A_ke^{-y}=e^{-x}/(m\log m)\) exactly, and
\[
 y-\mu_k=\log m+\log\log m+x+\delta_k\ge\tfrac12\log m
\]
for all sufficiently large \(m\), uniformly in \(k\ge2\). Step 4 bounds the residual by \(C_xm^{-1/12}\), so
\[
 m\Pr(kR_k>b_{m,k}+x)=\frac{e^{-x}}{\log m}\Big(1+\log m+\log\log m+x+\delta_k+O_x(m^{-1/12})\Big),
\]
which is the advertised second-order estimate.

**6. Extreme values and marks.** Petal completion times are independent, so the centered maximum has CDF \((1-p_{m,k}(x))^m\), with \(mp_{m,k}(x)\to e^{-x}\) and \(p_{m,k}(x)\to0\), uniformly in \(k\ge2\). Its limit is \(\exp(-e^{-x})\). More generally, subtracting the two tail limits gives rare-event probabilities for any bounded interval. Counts in disjoint intervals are multinomial with probabilities asymptotic to their Poisson intensities divided by \(m\), establishing joint independent Poisson limits. The marks \(U_j\) are independent uniform variables independent of all completion times by step 2, giving the product intensity. For \(k=1\), each petal has a single edge of rate one and the CDF is exactly \((1-e^{-t})^m\), which yields the stated one-bottleneck Gumbel limit.

## Verification
The companion `verify.py` uses exact fractions to check the key product \(A_k=(k-1)^2\), the tilted mean, rate inequalities, and finite cut sizes; separately it computes the completion-time survival from the independent upper-bidiagonal phase-type matrix for small clique sizes. The check was replayed successfully with `VERIFY_OK 33396 assertions`. These finite checks support the formulas, while the proof of uniformity over unbounded \(k\) is analytic in steps 3--6.

## Relationship to prior work
Janson (1999) gives the single-complete-graph exploration law and asymptotic distances. **For each fixed clique size** \(k\), the Gumbel limit and its \(\log\log m\) centering are an instance of Proposition 1 of Asimit and Jones (2007), which treats maxima of independent, identically distributed phase-type variables with a repeated dominant pole. Those fixed-parameter facts are not claimed as new. The assertion here is stronger: one uniform second-order survival expansion for *every* sequence \(k=k_m\ge2\), even arbitrarily rapidly growing or oscillating, together with the explicit independent endpoint-stage mark and its Poisson point-process limit. The fixed-phase-type theorem takes its matrix and pole residue as constant and gives no uniform remainder as its dimension and residue grow. Leskelä and Ngo (2018) and Mountford and Saliba (2019) study sparse random graph flooding under incompatible degree assumptions and derive first-order asymptotic bounds. The crucial calculation for the present two-parameter result is a telescoping, size-dependent residue \(A_k=(k-1)^2\) plus concentration uniform under the exponential tilt.

## Limitations
All edge passage lengths must be independent exponential variables of common rate one; varying rates, persistent dependencies, finite recovery, and general petal graphs are not covered. Only hub-rooted flooding is studied; unrestricted graph diameter and flooding from a non-hub root need not obey the stated law. The Poisson point-process conclusion describes extreme times and the particular endpoint-stage mark, not the entire path-tree geometry. A similar general-purpose extreme-value theorem for an equivalent triangular-array family might imply the result even without explicitly mentioning clique bouquets; historical priority is not independently certified. No external audit was performed.

## References
1. L. Leskelä and H. Ngo, *First passage percolation on sparse random graphs with boundary weights*, arXiv:1806.09568 (first version 25 June 2018); Journal of Applied Probability 56 (2019), 458–471. https://arxiv.org/abs/1806.09568
2. T. Mountford and J. Saliba, *Flooding and Diameter in General Weighted Random Graphs*, arXiv:1909.04563 (first version 10 September 2019); Journal of Applied Probability 57 (2020), 956–980. https://arxiv.org/abs/1909.04563
3. S. Janson, *One, Two and Three Times \(\log n/n\) for Paths in a Complete Graph with Random Weights*, Combinatorics, Probability and Computing 8 (1999), 347–361. https://doi.org/10.1017/S0963548399003892
4. A. V. Asimit and B. L. Jones, *Extreme behavior of multivariate phase-type distributions*, Insurance: Mathematics and Economics 41 (2007), 223–233, Proposition 1. https://openaccess.city.ac.uk/13144/1/Asimit_Jones_2006_revised.pdf
