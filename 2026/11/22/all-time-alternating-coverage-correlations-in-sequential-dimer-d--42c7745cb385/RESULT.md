# All-time alternating coverage correlations in sequential dimer deposition

## Finding

In random sequential covering of the initially empty integer lattice by dimers, each **undirected bond** \(\{j,j+1\}\) receives deposition attempts from one independent unit-rate Poisson clock. A dimer is accepted exactly when it covers at least one previously uncovered site; later overlapping successful dimers count as additional coverage. Let \(K_i(t)\in\{0,1,2\}\) be the number of accepted dimers covering site \(i\) by time \(t\in(0,\infty]\). Set \(p=1-e^{-t}\), with \(p=1\) at \(t=\infty\). For \(d\ge0\) write \(\kappa_d(p)=\operatorname{Cov}(K_0(t),K_d(t))\).

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

Let \((N_j(t))_{j\in\mathbb Z}\) be mutually independent unit-rate Poisson counting processes, one at each bond \(\{j,j+1\}\). At an attempt at bond \(j\), the interval is retained if either endpoint was not previously covered. The system starts with no covered sites. Every bond is retained at most once. The observation \(K_i(t)\) is the number of retained bonds incident to \(i\). No external boundary is imposed when recording the sites \(1,\ldots,n\).

All conclusions hold at finite \(t>0\) and at saturation \(t=\infty\). A per-bond attempt intensity \(\lambda>0\) gives \(p=1-e^{-\lambda t}\). If one instead puts independent unit-rate clocks on both directions of each bond, the proposals superpose with rate two per bond, since either direction attempts to cover the same two sites. In that convention use \(p=1-e^{-2t}\). At \(t=0\) all counts and covariances vanish, so strict signs are not asserted there.

## Proof

**1. Local first-arrival reduction.** Let \(T_j\) be the first arrival time at bond \(j\); the variables are independent unit-mean exponentials. At every site, its first incident attempt necessarily covers it: if it were uncovered, that attempt succeeds; if it had already been covered, an earlier incident attempt would have occurred. Thus whether a site is uncovered just before an attempt is determined by the first incident arrival, and no recursive construction on the infinite lattice is needed. A bond can be retained only at its first attempt: after that attempt both endpoints are permanently covered. Its first attempt succeeds exactly when it precedes the first attempt at **at least one** of its two adjacent bonds. Hence, with ties having probability zero,
\[
 A_j(t)=\mathbf1\{T_j\le t\}\,\mathbf1\{T_j<T_{j-1}\text{ or }T_j<T_{j+1}\},\qquad K_i(t)=A_{i-1}(t)+A_i(t).
\]
The variable \(A_j\) uses only \(T_{j-1},T_j,T_{j+1}\); \(K_i\) uses only \(T_{i-2},\ldots,T_{i+1}\). Thus subfamilies separated by at least four sites use disjoint independent clocks, proving three-dependence.

**2. Covariances of the retained bonds.** Write \(R_j=\mathbf1\{T_j\le t\}\) and \(M_j=\mathbf1\{T_j\le t,T_{j-1}<T_j,T_{j+1}<T_j\}\). Then \(A_j=R_j-M_j\) and, by the substitution \(u=1-e^{-s}\),
\[
 \mathbb E M_j=\int_0^t e^{-s}(1-e^{-s})^2\,ds=\frac{p^3}{3},\qquad
 a:=\mathbb E A_j=p-\frac{p^3}{3}.
\]
Put \(c_k=\operatorname{Cov}(A_0,A_k)\). Since \(A_0\) is Bernoulli, \(c_0=a(1-a)\). Adjacent local maxima cannot occur simultaneously, and \(M_0R_1=M_0\), \(R_0M_1=M_1\). Consequently
\[
 \mathbb E(A_0A_1)=p^2-\frac{2p^3}{3},\qquad
 c_1=-\frac{p^3(p^3-6p+6)}{9}.
\]
At bond distance two, \(M_0\) is independent of \(R_2\), and \(R_0\) is independent of \(M_2\). To evaluate the shared-clock event, integrate the independent first-arrival densities with \(T_1<\min(T_0,T_2)\), \(T_{-1}<T_0\), \(T_3<T_2\):
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
For bond distance at least three, all relevant clocks are disjoint, giving \(c_k=0\).

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
For \(n\ge4\) it gives the stated finite-size identity and \(V=4(c_0+2c_1+2c_2)\); the last Bernstein coefficient list proves \(V>0\). For the central limit theorem use blocks of length \(\lfloor n^{1/3}\rfloor\), separated by three discarded sites, giving independent centered main-block sums. Their total variance is asymptotic to \(nV\) by the finite-size identity. Each block sum is bounded by twice the block length in absolute value and hence is \(o(\sqrt n)\). The discarded sites and remainder have total cardinality \(o(n)\), and therefore variance \(o(n)\) since each site has bounded covariance with at most six other sites. Lindeberg's theorem and Slutsky's lemma complete the proof.

## Verification

The accompanying \(\texttt{verify.py}\), using only the Python 3 standard library, exhaustively enumerates possible first-arrival subsets and their orders for each pair of sites at separation \(0,1,2,3\). Conditional on which of the finitely many clocks have arrived before \(t\), their relative order is uniform. Each exact finite expectation is therefore a polynomial in \(p\) whose coefficients are calculated by rational arithmetic. The coefficient-by-coefficient identities agree with all four displayed covariances, the mean, the long-window variance, and the Bernstein positivity certificates. Run \(\texttt{python3 verify.py}\) from the extracted files. The checker is not being used in place of the analytic proof above.

## Relationship to prior work

Krapivsky, *Random Sequential Covering*, introduced the accepted-if-new rule, studied finite-interval deposited-dimer count cumulants, and derived the **single-site** dimer multiplicity probabilities at each time in Section VI A. In particular, the one-site marginals already give the mean and single-site variance, and the saturated deposited-dimer bulk variance gives the coefficient \(8/45\) for multiplicity by counting both endpoints. Viot and Krapivsky derived a finite hierarchy for selected local occupation probabilities and identified spatial pair correlations as a further direction in the Discussion.

The all-length outermost-lag covering result listed below gives the same sharp cutoff and the same positive outer-lag formula upon specialization of its proof to dimers, without giving the inner-lag covariances. In that proof the outer-lag covariance is \(\operatorname{Var}(\tfrac12 U_p^2)\) at length two, where \(U_p=\min(U,p)\) for a uniform \(U\) on \([0,1]\); this is precisely \(p^5(6-5p)/45\). Its reference to a separately recorded complete dimer law does not identify the record. The separate trimer result gives terminal correlations of the **indicator of triple covering** and a Gaussian limit for the number of such sites. It concerns length-three rods and a binary terminal event, not the all-time dimer multiplicity count.

The distinct content supported here is the complete time-dependent dimer covariance profile, in particular the evaluated inner lags and their strict signs over the entire time range, and the explicit finite-time growing-window fluctuation coefficient. The first-arrival construction and finite-dependence central limit technique are not themselves new.

## Limitations

The process is homogeneous, one-dimensional, and uses independent exponential attempt clocks. It does not cover binary occupancy covariances, longer rods, spatially heterogeneous attempt rates, open finite-interval boundary rules, or joint multi-time correlations. The normal limit is for a growing observation window at a **fixed** observation time, not for a joint long-time/large-window scaling. Complete bibliographic priority is not asserted.

## References

1. P. L. Krapivsky, *Random Sequential Covering*, arXiv:2209.03992, https://arxiv.org/abs/2209.03992.
2. P. Viot and P. L. Krapivsky, *Random sequential covering of a one-dimensional lattice by k-mers*, arXiv:2410.12373, https://arxiv.org/abs/2410.12373.
3. *Oscillating spatial correlations and exact Gaussian fluctuations in trimer sequential covering*, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-oscillating-spatial-correlations-and-exact-gaussian-fluctuations--27b43bfd218a/RESULT.md.
4. *Sharp outermost coverage covariance for all sequentially deposited k-mers*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-outermost-coverage-covariance-for-all-sequentially-deposit--5023e9240d95/RESULT.md.
