# Markov persistence amplifies positional fluctuations of integer expanding maps

## Finding

**Theorem (exact persistence law and singular frozen-environment limit).** Fix integers \(a,b\geq2\) and put \(d=a^{-1}\), \(e=b^{-1}\). Let \((E_n)_{n\geq0}\) be a stationary two-state Markov chain with labels \(a,b\), marginal probabilities \(1/2,1/2\), and transition matrix
\[
P_t=\begin{pmatrix}t&1-t\\1-t&t\end{pmatrix},\qquad 0<t<1.
\]
Independently choose \(X_0\) uniformly on \([0,1)\) and evolve
\[
X_{n+1}=\{E_{n+1}X_n\},\qquad
S_N=\sum_{n=0}^{N-1}(X_n-\tfrac12).
\]
Then the pair process \((E_n,X_n)\) is stationary and mixing, and its positional marginal is uniform for every \(t\). Its exact lag-\(k\) covariance, for every integer \(k\geq1\), is
\[
C_k=\frac1{12}\,\pi(P_tD)^k\mathbf1,\qquad
\pi=(\tfrac12,\tfrac12),\quad D=\operatorname{diag}(d,e),\quad\mathbf1=(1,1)^{\mathsf T}.
\]
For every real \(s\in[0,1]\), the processes \(N^{-1/2}S_{\lfloor Ns\rfloor}\), considered jointly in \(s\), converge in the Skorokhod space \(D([0,1])\) to \(\sigma_t B_s\), where \(B\) is standard Brownian motion and
\[
\boxed{\displaystyle
\sigma_t^2=\lim_{N\to\infty}\frac{\operatorname{Var}(S_N)}N
=\frac1{12}\left[1+\frac{d+e+2de-4tde}{1-t(d+e)+(2t-1)de}\right].}
\]
For all \(0<t<1\),
\[
\boxed{\displaystyle \frac{d}{dt}\sigma_t^2
=\frac{(d-e)^2}{12[1-t(d+e)+(2t-1)de]^2}.}
\]
Thus **strict monotonic amplification by persistence** holds exactly when \(a\ne b\), even though the stationary positional density and the one-time slope distribution are unchanged. For \(a=b\), the variance is constant in \(t\).

At the excluded frozen-environment endpoint \(t=1\), start with the same mixture of the two labels and uniform \(X_0\). The normalized sums instead converge to
\[
\boxed{\displaystyle
\frac12\,\mathcal N\!\left(0,\frac{1+d}{12(1-d)}\right)
+\frac12\,\mathcal N\!\left(0,\frac{1+e}{12(1-e)}\right).}
\]
For \(a\ne b\), this is a genuinely non-Gaussian mixture; its variance equals \(\lim_{t\uparrow1}\sigma_t^2\). The limiting law, unlike its variance, therefore changes discontinuously at perfect environmental persistence. For instance, at \((a,b)=(2,3)\),
\[
\sigma_t^2=\frac{12-7t}{12(5-3t)},\quad
\sigma_{1/2}^2=\frac{17}{84},\quad
\lim_{t\uparrow1}\sigma_t^2=\frac5{24},
\]
whereas the frozen-endpoint limit is the equal mixture of \(\mathcal N(0,1/4)\) and \(\mathcal N(0,1/6)\).

## Assumptions and scope

All randomness is annealed: the distribution includes both the stationary environment and the independent initial Lebesgue position. Every slope is an integer \(\geq2\), so the maps \(T_m(x)=\{mx\}\) preserve Lebesgue measure. The transition labels are recorded as \(E_n\); the map performed between times \(n\) and \(n+1\) has slope \(E_{n+1}\). The functional central limit theorem and strict derivative apply to \(0<t<1\), not to the nonergodic frozen endpoint. At the endpoint, only the stated one-dimensional normalized-sum limit is claimed. All covariance identities are exact for the stationary law; the theorem makes no quenched fluctuation claim.

## Proof

**1. Stationarity and mixing.** Each map \(T_m\) carries Lebesgue measure \(\lambda\) to itself. Thus \(\pi\otimes\lambda\) is stationary for the Markov chain \(Z_n=(E_n,X_n)\); in particular \(X_n\) is Lebesgue-uniform and independent of \(E_n\) at every time. For mixing, use the transfer operator
\[
(\mathcal L_m h)(y)=\frac1m\sum_{j=0}^{m-1}h((y+j)/m).
\]
For any bounded-variation \(h\), \(\operatorname{Var}(\mathcal L_mh)\leq m^{-1}\operatorname{Var}(h)\). Conditional starting densities \(h_i\) under each environment label evolve by a convex Markov combination of these operators, with the new label's slope; their maximal variation contracts by at least \(2^{-n}\). Their masses evolve under \(P_t\) and converge at rate \(|2t-1|^n\). Since an interval function differs from its mean in \(L^1\) by at most its total variation, the joint transfer operator sends every bounded-variation initial density to the stationary density in \(L^1\). Density of these functions in \(L^1\) proves mixing for the stationary chain and hence ergodicity (for \(0<t<1\)).

**2. An exact conditional correlation identity.** Put \(f(x)=x-1/2\). Direct summation gives
\[
\mathcal L_m f(y)=m^{-1}f(y).
\]
In particular, for every integer \(M\geq1\),
\[
\int_0^1 f(x)f(\{Mx\})\,dx=\frac1{12M}.
\]
Indeed, partition the integral into \(M\) equal subintervals and put \(u=\{Mx\}\); the term constant in \(u\) integrates to zero, leaving \(M\) copies of \(1/(12M^2)\). Given slopes \(E_1,\ldots,E_k\), the composite map is multiplication modulo one by \(M=\prod_{j=1}^k E_j\). Averaging the preceding integral over the stationary environment gives \(C_k=(12)^{-1}\pi(P_tD)^k\mathbf1\). Its absolute value is at most \(2^{-k}/12\).

**3. Summation and exact monotonicity.** Because \(\|P_tD\|_\infty\leq\max(d,e)\leq1/2\), the Green–Kubo series converges, and stationarity yields
\[
\lim_{N\to\infty}N^{-1}\operatorname{Var}(S_N)
=C_0+2\sum_{k\geq1}C_k
=\frac1{12}\left[1+2\pi D(I-P_tD)^{-1}\mathbf1\right].
\]
Here \(C_0=1/12\). An explicit inversion of the two-by-two matrix gives the displayed rational variance. Its denominator
\(H=1-t(d+e)+(2t-1)de=\det(I-P_tD)\) is positive: indeed \(\rho(P_tD)<1\) and the real eigenvalues of this nonnegative two-by-two matrix have modulus less than one. With \(U=d+e+2de-4tde\), differentiation reduces exactly to the identity
\[
U'H-UH'=(d-e)^2,
\]
proving the strict criterion and all parameter boundaries stated above.

**4. Functional central limit theorem.** Extend the stationary Markov chain to a two-sided stationary process. Reverse its time direction and denote its one-step conditional-expectation operator by \(Q\). Conditional on the current label \(j\), its predecessor label \(i\) has probability \((P_t)_{ji}\), while its predecessor coordinate is uniformly distributed among the \(j\)-slope inverse branches. Consequently, for \(h(i,x)=v_i f(x)\),
\[
(Qh)(j,y)=\left[D P_t v\right]_j f(y).
\]
Since \(\|DP_t\|_\infty\leq1/2\), the bounded vector \(v=(I-DP_t)^{-1}\mathbf1\) gives a bounded solution \(h-Qh=f\). On the reversed stationary chain \((Y_n)\), the differences \(\xi_n=h(Y_n)-Qh(Y_{n-1})\) are bounded martingale differences, and
\[
\sum_{k=0}^{N-1}f(Y_k)=h(Y_0)-h(Y_N)+\sum_{k=1}^N\xi_k.
\]
Mixing proved in step 1 implies ergodicity of the reverse chain, so its conditional quadratic-variation averages converge almost surely to \(\mathbb E\xi_1^2\). The bounded martingale functional central limit theorem gives a Brownian limit for reversed partial sums. Stationarity transfers this to forward partial sums by reversing each length-\(N\) window; the corresponding map on Brownian paths is \(B_s\mapsto B_1-B_{1-s}\), again Brownian motion. The bounded coboundary contributes uniformly \(O(N^{-1/2})\). Summable covariances and boundedness identify \(\mathbb E\xi_1^2=\sigma_t^2\), so the announced functional limit follows.

**5. The frozen endpoint.** At \(t=1\), \(E_n\) is a single fair random label for the entire trajectory. Conditional on label \(m\), the preceding single-map reverse-martingale argument yields a normal limit with variance \((1+m^{-1})/[12(1-m^{-1})]\), obtained by summing the covariance \(1/(12m^k)\). Average the two conditional limiting laws to obtain the stated mixture. If \(a\ne b\), its two variances differ, and strict Jensen's inequality for the Laplace transform shows the mixture is not Gaussian. Direct substitution into the rational variance confirms its variance equals the limit as \(t\uparrow1\).

## Verification

The standalone standard-library program `checks/verify.py` independently checks the multiplication-map covariance integral by exact-rational branch integration, enumerates short environmental histories to verify the matrix covariance identity, tests the algebraic derivative and endpoint identities, and compares finite-sum variance with the limiting expression. Run `python3 checks/verify.py` from the directory containing this file. It reports 159 exact-rational checks. These checks do not replace the analytical ergodicity or martingale functional-limit arguments.

## Relationship to prior work

Suzuki (2023), arXiv:2303.17521, develops stationary and samplewise invariant densities for random beta-transformations, including non-independent driving; its inspected results address invariant densities, not a persistence-dependent closed Green–Kubo variance or its endpoint Gaussian-mixture discontinuity. Hafouta (first public version 2021, arXiv:2109.11073; published online 2023) proves general limit theorems for random expanding skew products with mixing drivers; the present Brownian convergence is a special case in spirit, and **is not asserted to be novel by itself**. The new content here is the complete explicit parameter law, its sharp strict monotonicity, and the contrast with the exactly identified non-Gaussian frozen-endpoint limit. Aimino, Nicol and Vaienti (2013) already treat independently chosen integer multiplication maps and general annealed/quenched limit theorems (Example 7.3 and Proposition 3.4), again without correlated Markov persistence. Classical Bernoulli-polynomial eigenfunctions of integer beta maps explain the linear-observable calculation; they are not claimed as new. Prior work on random beta maps may contain unindexed equivalent explicit formulas; see Limitations.

## Limitations

This theorem concerns precisely the centered coordinate observable and symmetric two-state Markov switching between integer slopes. It does not establish monotonicity for general observables, nonsymmetric switching, or noninteger beta maps. The functional CLT is annealed. The endpoint process is nonergodic; its mixture law holds only under the stated stationary fair-label initialization. No independent expert verification or publication-priority certification has been performed.

## References

1. Shintaro Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521, originally posted 2023-03-30. https://arxiv.org/abs/2303.17521
2. Yeor Hafouta, *Large deviations, moment estimates and almost sure invariance principles for skew products with mixing base maps and expanding-on-average fibers*, arXiv:2109.11073, originally posted 2021-09-22; *Ergodic Theory and Dynamical Systems* **44** (2024), 118–158. https://arxiv.org/abs/2109.11073 ; https://doi.org/10.1017/etds.2023.23
3. Romain Aimino, Matthew Nicol and Sandro Vaienti, *Annealed and quenched limit theorems for random expanding dynamical systems*, arXiv:1310.4359, first posted 2013-10-16; see Proposition 3.4 and Example 7.3. https://arxiv.org/abs/1310.4359
4. I. Antoniou and S. Tasaki, *Spectral decomposition of the Rényi map*, *J. Phys. A* **26** (1993), 73–94. https://doi.org/10.1088/0305-4470/26/1/012
