# Critical resampling noise and a three-Poisson vacancy law at coupon coverage

## Finding
Let \(n\to\infty\), fix \(c\in\mathbb R\), and let \(m_n\) be nonnegative integers satisfying \(m_n=n\log n+cn+o(n)\). Throw \(m_n\) independent uniform labelled balls into \(n\) boxes. Independently refresh every ball with probability \(\varepsilon_n\in[0,1]\): a refreshed ball chooses an independent uniform box, and an unrefreshed ball retains its old box. Write \(A_n\) and \(B_n\) for the sets of empty boxes before and after refreshing. Let \(C_n=|A_n\cap B_n|\), \(L_n=|A_n\setminus B_n|\), and \(R_n=|B_n\setminus A_n|\).

For any \(\varepsilon_n\log n\to\tau\in[0,\infty]\), with \(e^{-\infty}=0\), put \(\lambda=e^{-c}\) and \(p=e^{-\tau}\). Then, jointly and in total variation,
\[
(C_n,L_n,R_n)\longrightarrow
(C,L,R),\qquad
C\sim\operatorname{Pois}(\lambda p),\quad
L,R\stackrel{\mathrm{iid}}\sim\operatorname{Pois}(\lambda(1-p)),
\]
where the three limiting variables are mutually independent. Thus both marginal missing-coupon counts converge to \(\operatorname{Pois}(\lambda)\), while their shared component transitions at refresh scale \(1/\log n\).

In particular, the probability both configurations cover all boxes converges to \(\exp[-\lambda(2-p)]\), and
\[
\Pr(B_n=\varnothing\mid A_n=\varnothing)\longrightarrow
\exp[-\lambda(1-p)].
\]
For finite \(n\ge2\) and integer \(m\ge0\), the exact covariance of the two vacancy counts \(U=|A|\), \(V=|B|\) is
\[
\operatorname{Cov}(U,V)=n b+n(n-1)d-n^2 a^2,
\]
where \(a=(1-1/n)^m\), \(b=(1-(1+\varepsilon)/n+\varepsilon/n^2)^m\), and \(d=(1-2/n+\varepsilon/n^2)^m\). Along the stated scaling this covariance tends to \(\lambda p\).

## Assumptions and scope
All box choices and refresh indicators are independent across ball labels. The refreshed draw is independent of the original draw, including the possibility of selecting the same box. No independence is asserted for finite-size vacancy indicators or for the finite-size counts \((C_n,L_n,R_n)\). The asymptotic statement permits the full range \(\tau=0\), finite positive \(\tau\), and \(\tau=\infty\). It is not a statement about unequal box probabilities or about adaptively stopping at the cover time.

## Proof
For fixed nonnegative integers \(s,t,u\), select \(s+t+u\) distinct ordered boxes: the first \(s\) must be vacant in both configurations, the next \(t\) vacant only before refreshing, and the last \(u\) vacant only afterwards. A ball with original destination \(X\) and refreshed destination \(Y\) satisfies, for any forbidden sets \(F,G\),
\[
\Pr(X\notin F,Y\notin G)=1-\frac{|F|+|G|}{n}
 +(1-\varepsilon)\frac{|F\cap G|}{n}
 +\varepsilon\frac{|F|\,|G|}{n^2}.
\]
Apply inclusion-exclusion to require occupancy *after* refreshing of the \(t\) first-only boxes and occupancy *before* refreshing of the \(u\) second-only boxes. Choosing \(i\) of the former and \(j\) of the latter for additional vacancy constraints gives forbidden set cardinalities \(s+t+j\) for \(X\), \(s+u+i\) for \(Y\), and intersection \(s+i+j\). Consequently the following mixed falling-factorial moments are **exact** for every finite size:
\[
\begin{aligned}
\mathbb E[(C)_s(L)_t(R)_u]
&=(n)_{s+t+u}\sum_{i=0}^{t}\sum_{j=0}^{u}
 (-1)^{i+j}\binom ti\binom uj\,Q_{i,j}^{m},\\
Q_{i,j}&=1-\frac{s+t+u+\varepsilon(s+i+j)}{n}
+\frac{\varepsilon(s+t+j)(s+u+i)}{n^2}.
\end{aligned}
\]
Here \((z)_k=z(z-1)\cdots(z-k+1)\) with \((z)_0=1\); if \(s+t+u>n\) the moment is zero. Note that \(Q_{i,j}\) is a probability, hence no alternating-sign approximation has been made.

Set \(k=s+t+u\). For any fixed \(i,j,s,t,u\), since \(m_n/n=\log n+c+o(1)\) and \(m_n/n^2=o(1)\),
\[
 n^k Q_{i,j}^{m_n}\longrightarrow
 \lambda^k\exp[-\tau(s+i+j)]
\]
when \(\tau<\infty\). For \(\tau=\infty\) the same limit holds under the convention that the exponential is \(0\) when \(s+i+j>0\), and \(1\) otherwise. Indeed, the bounded factor \(\exp[-c\varepsilon_n(s+i+j)]\) matters only in terms already tending to zero when \(\tau=\infty\). Combining with \((n)_k/n^k\to1\) gives
\[
\lim\mathbb E[(C_n)_s(L_n)_t(R_n)_u]
=(\lambda p)^s[\lambda(1-p)]^{t+u}.
\]
These are exactly all mixed falling-factorial moments of three independent Poisson variables with the claimed means. The multivariate factorial-moment method applies since the limiting independent-Poisson law has an everywhere finite moment-generating function and the first moments are bounded. Thus the vector converges weakly. On the countable state space \(\mathbb N_0^3\), weak convergence to this proper discrete distribution and tightness imply convergence in total variation (truncate to a sufficiently large finite box).

For the exact finite covariance, sum \(\mathbb E[\mathbf1_{i\in A}\mathbf1_{j\in B}]\) over ordered box pairs. Equal boxes contribute \(b\); unequal boxes contribute \(d\); and \(\mathbb E U=\mathbb E V=na\). Finally, \(na\to\lambda\), \(nb\to\lambda p\), and \(n(n-1)d-n^2a^2\to0\), yielding \(\operatorname{Cov}(U,V)\to\lambda p\). Since \(U=L+C\) and \(V=R+C\), the joint limit also gives the displayed coverage probabilities.

## Verification
The companion standard-library script `checker.py` enumerates all paired allocations for \((n,m,\varepsilon)\) equal to \((2,1,0)\), \((2,3,1/2)\), \((3,3,0)\), \((3,3,1/2)\), \((3,4,1/3)\), \((3,5,2/3)\), \((4,3,1/2)\), and \((4,4,1/3)\). It computes exact rational weights from the independently refreshed transition kernel, then compares all mixed falling-factorial moments of total order at most three with the inclusion-exclusion identity and separately checks the exact covariance. The checker passes 168 exact rational identities. Run with `python3 checker.py`.

## Relationship to prior work
Uniform coupon-collection completion and one-sample vacancy Poisson asymptotics are classical. Pósfai (2010), Sections 1, 4 and 5, gives an extensive treatment of one-collector waiting-time approximations. O'Neill (2023), Sections 1–5, treats univariate occupied-bin distributions under thinning/fall-through. Ilienko (2026), Sections 1–4, studies coupled albums from *successive repeated coupons* and random stopping times. None of these inspected results states the two-configuration independent-ball-refresh model or the three independent limiting vacancy categories. The new content is the **joint overlap/noise crossover**, not the one-sample Poisson law, Poisson thinning, or the general factorial-moment technique.

## Limitations
The law is proved for uniform independent ball allocations with a fixed number of draws. Different refresh mechanisms, unequal coupons, growing numbers of configurations, and quantitative finite-size total-variation rates are not claimed. Priority relative to less accessible correlated-occupancy and noise-sensitivity literature is not fully resolved. The exact checks cover only the listed finite cases and do not replace the analytic limit proof. Independent mathematical audit has not been performed.

## References
1. Anna Pósfai, *Approximation Theorems Related to the Coupon Collector's Problem*, arXiv:1006.3531, public version 17 June 2010, https://arxiv.org/html/1006.3531v1.
2. Ben O'Neill, *Three Distributions in the Extended Occupancy Problem*, Methodology and Computing in Applied Probability 25 (2023), article 84, https://doi.org/10.1007/s11009-023-10053-y.
3. Andrii Ilienko, *Limit theorems in the extended coupon collector's problem*, published online 11 August 2026, https://doi.org/10.15559/26-VMSTA306.
