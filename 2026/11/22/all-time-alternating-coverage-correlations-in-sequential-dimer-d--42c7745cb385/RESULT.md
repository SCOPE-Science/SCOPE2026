# All-time alternating coverage correlations in sequential dimer deposition

## Finding

In random sequential covering of the initially empty integer lattice by dimers, every oriented nearest-neighbor edge receives independent unit-rate Poisson deposition attempts. A dimer is accepted exactly when it covers at least one previously uncovered site; later overlapping successful dimers count as additional coverage. Let \(K_i(t)\in\{0,1,2\}\) be the number of accepted dimers covering site \(i\) by time \(t\in(0,\infty]\). Set \(p=1-e^{-t}\), with \(p=1\) at \(t=\infty\). For \(d\ge0\) write \(\kappa_d(p)=\operatorname{Cov}(K_0(t),K_d(t))\).

**Exact all-time spatial correlation theorem.** For every \(0<p\le1\),
\[
\begin{aligned}
\kappa_1(p)&=\frac{p}{45}\left(45-45p-75p^2+90p^3+6p^4-20p^5\right)>0,\\
\kappa_2(p)&=-\frac{p^3}{15}\left(10-10p-4p^2+5p^3\right)<0,\\
\kappa_3(p)&=\frac{p^5(6-5p)}{45}>0,\\
\kappa_d(p)&=0\qquad(d\ge4).
\end{aligned}
\]
Moreover the field is **three-dependent**, not just pairwise uncorrelated beyond distance three: subfamilies separated by at least four sites are independent. The correlation range is sharp at every positive time since \(\kappa_3(p)>0\). At saturation, \((\kappa_1,\kappa_2,\kappa_3)=(1/45,-1/15,1/45)\).

The mean site multiplicity is \(m(p)=2p-2p^3/3\), and the single-site variance is
\[
\kappa_0(p)=\frac{-2p}{9}(2p^5-12p^3+9p^2+9p-9).
\]
For the total multiplicity on \(n\) consecutive sites of the *infinite-lattice* process, \(S_n(t)=\sum_{i=1}^{n}K_i(t)\), the exact long-window variance coefficient is
\[
V(p)=\kappa_0(p)+2\kappa_1(p)+2\kappa_2(p)+2\kappa_3(p)
=\frac{4p}{45}\left(45-45p-75p^2+90p^3+12p^4-25p^5\right)>0.
\]
Consequently, for each fixed \(t\in(0,\infty]\),
\[
\frac{S_n(t)-nm(p)}{\sqrt n}\ \Longrightarrow\ \mathcal N(0,V(p)),\qquad n\to\infty,
\]
and for all integers \(n\ge4\),
\[
\operatorname{Var}(S_n(t))=nV(p)-2\kappa_1(p)-4\kappa_2(p)-6\kappa_3(p).
\]
In particular \(V(1)=8/45\). The theorem concerns **coverage with multiplicity**, not the binary indicator of whether a site has been covered.

## Assumptions and scope

Let \((N_j(t))_{j\in\mathbb Z}\) be mutually independent unit-rate Poisson counting processes, one at each edge \(\{j,j+1\}\). At an attempt at edge \(j\), the interval is retained if either endpoint was not previously covered. The system starts with no covered sites. Every edge is retained at most once, and the definition is consistent on the entire infinite lattice because retaining the first attempted dimer covering a site permanently covers that site. The observation \(K_i(t)\) is the number of retained edges incident to \(i\). No external boundary is imposed when recording the sites \(1,\ldots,n\).

All conclusions hold at finite \(t>0\) and at saturation \(t=\infty\). Physical attempt intensity \(\lambda>0\) is recovered by replacing \(t\) with \(\lambda t\). At \(t=0\) all counts and covariances vanish, so strict signs are not asserted there.

## Proof

**1. Local first-arrival reduction.** Let \(T_j\) be the first arrival time at edge \(j\); the variables are independent unit-mean exponentials. An edge can be successfully deposited only at its first attempt: after a rejected first attempt both endpoints are already covered permanently. Its first attempt succeeds exactly when it precedes the first attempt of **at least one** of its two adjacent edges. Hence, with ties having probability zero,
\[
A_j(t)=\mathbf1\{T_j\le t\}\,\mathbf1\{T_j<T_{j-1}\text{ or }T_j<T_{j+1}\},\qquad K_i(t)=A_{i-1}(t)+A_i(t).
\]
The variable \(A_j\) uses only \(T_{j-1},T_j,T_{j+1}\); \(K_i\) uses only \(T_{i-2},\ldots,T_{i+1}\). Thus subfamilies separated by at least four sites use disjoint independent clocks, proving three-dependence.

**2. Covariances of the accepted edges.** Write \(R_j=\mathbf1\{T_j\le t\}\) and \(M_j=\mathbf1\{T_j\le t,T_{j-1}<T_j,T_{j+1}<T_j\}\). Then \(A_j=R_j-M_j\) and, by the substitution \(u=1-e^{-s}\),
\[
\mathbb E M_j=\int_0^t e^{-s}(1-e^{-s})^2\,ds=\frac{p^3}{3},\qquad
 a:=\mathbb E A_j=p-\frac{p^3}{3}.
\]
Put \(c_k=\operatorname{Cov}(A_0,A_k)\). Since \(A_0\) is Bernoulli, \(c_0=a(1-a)\). Adjacent local maxima cannot occur simultaneously, and \(M_0R_1=M_0\), \(R_0M_1=M_1\). Consequently
\[
\mathbb E(A_0A_1)=p^2-\frac{2p^3}{3},\qquad
c_1=-\frac{p^3(p^3-6p+6)}{9}.
\]
At edge distance two, \(M_0\) is independent of \(R_2\), and \(R_0\) is independent of \(M_2\). To evaluate the shared-clock event, integrate the independent first-arrival densities with \(T_1<\min(T_0,T_2)\), \(T_{-1}<T_0\), \(T_3<T_2\):
\[
\mathbb E(M_0M_2)
=\int_0^p\!\int_0^p xy\min(x,y)\,dx\,dy
=\frac{2p^5}{15}.
\]
Thus
\[
\mathbb E(A_0A_2)=p^2-\frac{2p^4}{3}+\frac{2p^5}{15},\qquad
c_2=\frac{p^5(6-5p)}{45}.
\]
For edge distance at least three, all relevant clocks are disjoint, giving \(c_k=0\). These equations also prove the normalization and exact range of all edge covariances.

**3. Site covariance and sharp signs.** Expanding \(K_0=A_{-1}+A_0\) and \(K_d=A_{d-1}+A_d\) gives
\[
\kappa_0=2(c_0+c_1),\quad
\kappa_1=c_0+2c_1+c_2,\quad
\kappa_2=c_1+2c_2,\quad
\kappa_3=c_2,
\]
with \(\kappa_d=0\) for \(d\ge4\). Substitution yields every displayed polynomial. To certify signs globally rather than rely on sampling, use the degree-\(n\) Bernstein basis \(\binom nk p^k(1-p)^{n-k}\). The Bernstein coefficient lists of the polynomials \(45\kappa_1/p\), \(-15\kappa_2/p^3\), and \(45V/(4p)\), respectively, are
\[
(45,36,39/2,9/2,6/5,1),\quad
(10,20/3,2,1),\quad
(45,36,39/2,9/2,12/5,2).
\]
Every coefficient is strictly positive. The remaining sign, \(\kappa_3=p^5(6-5p)/45>0\), follows directly. This proves the exact positive–negative–positive sign profile for all \(0<p\le1\), with a sharp positive covariance at distance three.

**4. Fluctuations.** The covariance sum for a stationary three-dependent field is
\[
\operatorname{Var}(S_n)=n\kappa_0+2\sum_{d=1}^3(n-d)_+\kappa_d.
\]
For \(n\ge4\) it gives the stated finite-size identity and \(V=4(c_0+2c_1+2c_2)\); the last Bernstein coefficient list proves \(V>0\). Bounded stationarity and three-dependence imply the central limit theorem by the standard separated-block argument: use blocks of length \(\lfloor n^{1/3}\rfloor\), separated by three discarded sites, giving independent centered main-block sums. Their total variance is asymptotic to \(nV\), each block is \(o(\sqrt n)\), and the discarded terms have \(o(n)\) variance. Lindeberg's theorem and Slutsky's lemma complete the proof.

## Verification

The accompanying \(\texttt{verify.py}\), using only the Python 3 standard library, exhaustively enumerates possible first-arrival subsets and their orders for each pair of sites at separation \(0,1,2,3\). Conditional on which of the finitely many clocks have arrived before \(t\), their relative order is uniform. Each exact finite expectation is therefore a polynomial in \(p\) whose coefficients are calculated by rational arithmetic. The independent coefficient-by-coefficient identities agree with all four displayed covariances, the mean, the long-window variance, and the Bernstein positivity certificates. Run \(\texttt{python3 verify.py}\) from the extracted files. The checker is not being used in place of the analytic proof above.

## Relationship to prior work

Krapivsky, *Random Sequential Covering* (first publicly posted 2022-09-08, arXiv:2209.03992), introduced the accepted-if-new rule, studied finite-interval deposited-dimer count cumulants, and derived the **single-site** dimer multiplicity probabilities at each time in Section VI A. These are premises and consistency checks, not claimed here as new. Viot and Krapivsky, *Random sequential covering of a one-dimensional lattice by k-mers* (first publicly posted 2024-10-16, arXiv:2410.12373), derived a finite hierarchy for selected local occupation probabilities and explicitly identified spatial pair correlations as a further problem in the Discussion. Its general finite-clock locality does not supply this evaluated all-time covariance kernel or its global signs without additional joint calculations.

A published 2026 trimer-covering result gives terminal correlations of the **indicator of triple covering** and a Gaussian limit for the number of such sites. It concerns length-three rods, a binary terminal event and six nonzero spatial lags. It does not imply the all-time **multiplicity-count** correlations here for length-two rods or their sign inequalities. The first-arrival idea and finite-dependence central limit technique are not claimed as novel by themselves. The new content is the exact temporal three-lag covariance law, strict all-time sign classification, and explicitly normalized site-multiplicity fluctuation amplitude.

## Limitations

The process is homogeneous, one-dimensional, and uses independent exponential attempt clocks. It does not cover binary occupancy covariances, longer rods, spatially heterogeneous attempt rates, open finite-interval boundary rules, or joint multi-time correlations. The normal limit is for a growing observation window at a **fixed** observation time, not for a joint long-time/large-window scaling. Existing published total-dimer count cumulants at saturation may imply aggregate variance constants; no novelty is claimed for the terminal number variance alone. Comprehensive bibliographic priority still requires independent expert review.

## References

1. P. L. Krapivsky, *Random Sequential Covering*, arXiv:2209.03992 (first posted 2022-09-08), https://arxiv.org/abs/2209.03992.
2. P. Viot and P. L. Krapivsky, *Random sequential covering of a one-dimensional lattice by k-mers*, arXiv:2410.12373 (first posted 2024-10-16), https://arxiv.org/abs/2410.12373.
3. *Oscillating spatial correlations and exact Gaussian fluctuations in trimer sequential covering* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-oscillating-spatial-correlations-and-exact-gaussian-fluctuations--27b43bfd218a/RESULT.md.
