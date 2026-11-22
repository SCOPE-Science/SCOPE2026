# Stationary Ornstein–Uhlenbeck limit for descents under random transpositions

## Finding

For every integer \(n\ge3\), start a permutation \(\pi_n(0)\) uniformly on \(S_n\). At each integer step, independently choose one of the \(\binom n2\) unordered pairs of **distinct positions** uniformly and swap the entries at those positions. Write \(C_n(k)\) for the number of cyclic descents, counting the comparison between the last and first positions, and \(D_n(k)\) for the number of ordinary descents. Define
\[
X_n(t)=\frac{C_n(\lfloor nt\rfloor)-n/2}{\sqrt n},\qquad
Y_n(t)=\frac{D_n(\lfloor nt\rfloor)-(n-1)/2}{\sqrt n}.
\]
For every finite \(T>0\), jointly in \(D([0,T],\mathbb R^2)\) with the Skorokhod \(J_1\) topology,
\[
(X_n,Y_n)\Longrightarrow(Z,Z),
\qquad dZ_t=-4Z_t\,dt+\sqrt{2/3}\,dB_t,
\qquad Z_0\sim N(0,1/12),
\]
where \(B\) is independent of \(Z_0\). In particular the limit is a stationary Ornstein–Uhlenbeck process with covariance \(\mathbb E[Z_sZ_t]=e^{-4|t-s|}/12\).

The following exact identities underpin the limit. For every \(r\ge0\),
\[
\operatorname{Cov}(C_n(0),C_n(r))=\frac n{12}\left(\frac{n-5}{n-1}\right)^r,
\]
\[
\operatorname{Cov}(D_n(0),D_n(r))
=\frac{n+1}{6n}\left(\frac{n-3}{n-1}\right)^r
+\frac{(n-2)(n+1)}{12n}\left(\frac{n-5}{n-1}\right)^r.
\]
The second term carries the asymptotic \(\sqrt n\)-scale fluctuations, whereas the first reflects the two endpoints of the noncyclic statistic.

## Assumptions and scope

The initial permutation is exactly uniform, and all swaps use distinct **positions** chosen without replacement. The full permutation chain is stationary even though it is periodic. The result is a weak functional limit on each fixed finite time interval, not total-variation convergence, a pointwise finite-size Gaussian identity, or a claim for a nonstationary starting permutation. Cyclic descents count \(\mathbf1\{\pi(i)>\pi(i+1)\}\) for \(1\le i<n\) and \(\mathbf1\{\pi(n)>\pi(1)\}\). Finite sample sizes can have negative transition eigenvalues; no positivity assumption on them is used.

## Proof

**1. Exact cyclic eigenfunction.** For distinct positions \(a,b\), write \(A_{ab}(\pi)=\mathbf1\{\pi(a)>\pi(b)\}-1/2\), so \(A_{ba}=-A_{ab}\). Represent any antisymmetric linear comparison statistic as \(F_x=\sum_{a<b}x_{ab}A_{ab}\), and define its divergence \(d_a=\sum_{b\ne a}x_{ab}\). Counting transpositions that touch neither, one, or both ends of \(a,b\) shows that the one-step conditional expectation operator \(P\) acts by
\[
(Px)_{ab}=\frac{n-5}{n-1}x_{ab}+\frac2{n(n-1)}(d_a-d_b).
\]
For the directed cyclic path with edges \(1\to2\to\cdots\to n\to1\), the comparison coefficient has zero divergence at every position. Hence with \(H=C_n-n/2\),
\[
PH=\rho_n H,\qquad \rho_n=\frac{n-5}{n-1}=1-\frac4{n-1}.
\]
For uniform \(\pi\), consecutive circular comparisons have variance \(1/4\), neighboring covariance \(-1/12\), and otherwise covariance zero. Consequently \(\mathbb EH=0\) and \(\operatorname{Var}(H)=n/12\). By stationarity and the eigenfunction identity, \(\operatorname{Cov}(C_n(0),C_n(r))=(n/12)\rho_n^r\).

**2. Exact ordinary covariance.** Set \(h=D_n-(n-1)/2\). Its antisymmetric coefficient vector comprises the directed path edges \(1\to2\to\cdots\to n\), with divergence \((1,0,\ldots,0,-1)\). Its squared projection onto the gradient sector is \(2/n\), and the orthogonal divergence-free component has squared norm \(n-1-2/n\). The covariance matrix of the centered uniform permutation comparison vector equals \((I+B^\top B)/12\), where \(B\) is the complete-graph incidence matrix: its eigenvalues are \((n+1)/12\) on gradients and \(1/12\) on circulations. The transposition operator's eigenvalues on these sectors are \((n-3)/(n-1)\) and \(\rho_n\), respectively, directly from the formula in step 1. Multiplying their norms and variances gives the displayed ordinary covariance identity. At lag zero it equals the classical \((n+1)/12\).

**3. Deterministic bounds and bracket concentration.** Each swap modifies at most four cyclic comparisons. Thus \(|C_n(k+1)-C_n(k)|\le4\). For a deterministic permutation \(\pi\), put
\[
g_n(\pi)=\frac1{\binom n2}\sum_{a<b}\big(C_n(\pi\circ(a\ b))-C_n(\pi)\big)^2.
\]
From the variance and eigenfunction identities,
\[
\mathbb E g_n(\pi_n(0))=2\frac n{12}(1-\rho_n)=\frac{2n}{3(n-1)}\longrightarrow\frac23.
\]
Generate the uniform permutation by ranking independent continuous \(U_1,\ldots,U_n\). Replacing \(U_i\) changes the summand in \(g_n\) only for swap pairs with at least one endpoint at cyclic distance at most one from \(i\). There are at most \(3(n-1)\) such pairs; each squared increment lies in \([0,16]\). Therefore the replacement changes \(g_n\) by at most \(96/n\). The Efron–Stein inequality yields
\[
\operatorname{Var}(g_n(\pi_n(0)))\le\frac{4608}{n}.
\]
Hence \(g_n(\pi_n(0))\to2/3\) in \(L^2\). By stationarity, the same estimates hold at every integer step.

**4. Martingale functional limit.** Write \(X_{n,k}=(C_n(k)-n/2)/\sqrt n\), \(\Delta_{n,k}=X_{n,k+1}-X_{n,k}\), and
\[
\xi_{n,k}=\Delta_{n,k}+\frac4{n-1}X_{n,k}.
\]
The \(\xi_{n,k}\) are martingale differences by step 1, each bounded by \(8/\sqrt n\), with conditional variance
\[
\mathbb E(\xi_{n,k}^2\mid\pi_n(k))
=\frac{g_n(\pi_n(k))}{n}-\frac{16X_{n,k}^2}{(n-1)^2}.
\]
For each finite \(T\), the predictable quadratic variation of \(\sum_{k<nt}\xi_{n,k}\) converges uniformly on \([0,T]\), in \(L^1\), to \(2t/3\). Indeed the first sum uses the stationary \(L^1\) concentration in step 3; the second has expectation bounded by \(O(T/n)\) because \(\mathbb EX_{n,k}^2=1/12\). The bounded jumps give Lindeberg. The functional martingale central limit theorem therefore gives Brownian noise of variance rate \(2/3\), jointly with the initial value, with asymptotic independence.

The initial variable \(X_{n,0}\) converges to \(N(0,1/12)\): remove the one wrap-around comparison, then apply the bounded one-dependent triangular-array CLT to the independent-uniform rank comparisons. The recursion
\[
X_{n,k+1}-X_{n,k}=-\frac4{n-1}X_{n,k}+\xi_{n,k}
\]
converges by the Euler integral equation and martingale tightness to the unique solution of \(dZ_t=-4Z_tdt+\sqrt{2/3}dB_t\). Its stationary variance is \((2/3)/8=1/12\).

**5. Ordinary descents share the process limit.** Pathwise at every step,
\[
\left|Y_n(t)-X_n(t)\right|=
\frac{\left|\mathbf1\{\pi_n(\lfloor nt\rfloor,n)>\pi_n(\lfloor nt\rfloor,1)\}-1/2\right|}{\sqrt n}
\le\frac1{2\sqrt n}.
\]
This uniform deterministic bound transfers the functional limit to the pair \((X_n,Y_n)\).

## Verification

The standalone `checker.py` exhaustively enumerates every permutation for \(3\le n\le7\), checks the pointwise cyclic eigenfunction identity for every permutation, checks both stationary variances, the two lag-one covariances and the exact mean squared one-step increment. It reports `PASS: 5936 exact tests; all permutations n=3,...,7`. Run `python3 checker.py` in the extracted directory. The checker also demonstrates a failure of strong lumpability: for the six-position states \((1,2,3,4,6,5)\) and \((1,2,3,5,6,4)\), both with two cyclic descents, the respective conditional squared one-step changes are \(4/3\) and \(16/15\). Exhaustion at these finite sizes verifies algebraic boundary cases, not the infinite functional limit. Steps 1–5 are the all-size proof.

## Relationship to prior work

Hultman (2013) computes the expected **descent count starting from the identity** after random transpositions, with two character-ratio modes. Those same eigenvalues appear here, but the expectation does not specify stationary covariance amplitudes, conditional quadratic variations, or a stationary functional process limit. Garet (2019) proves a one-time central limit theorem for descents under a **growing-permutation insertion chain**, not temporal random-transposition dynamics at fixed deck size. The full comparison-vector covariance and its gradient/circulation decomposition are known separately in a published incidence-precision result; they help verify the finite identities, but do not establish the fluctuation-process limit. Published work on random-to-top shuffles concerns another transition kernel. The present contribution is the stationary path-space Ornstein–Uhlenbeck limit, including the deterministic-bracket proof and equivalence of cyclic and ordinary versions.

## Limitations

The theorem assumes uniform stationarity, uniform distinct-position swaps and observation times of order \(n\). It does not assert Markovianity of the finite-size descent-count projection, or extend automatically to initial decks far from uniform, adjacent-transposition shuffles, alternative shuffle kernels, growing observation horizons, or quantitative convergence rates. Classical martingale FCLT and static one-dependent CLT are invoked as established tools. Published work may contain a more general functional fluctuation theorem covering this special kernel; the historical-priority comparison is necessarily provisional and independent audit is pending.

## References

1. A. Hultman, *Permutation statistics of products of random permutations*, arXiv:1301.0430v1, first posted 2013-01-03, https://arxiv.org/abs/1301.0430; *Advances in Applied Mathematics* 54 (2014), 1–10, https://doi.org/10.1016/j.aam.2013.10.003.
2. O. Garet, *A central limit theorem for the number of descents and some urn models*, arXiv:1906.02980, first posted 2019-06-07, https://arxiv.org/abs/1906.02980.
3. *Incidence precision law for all inversion indicators of a random permutation*, published technical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805.
4. *Universal spectrum and exact relaxation of exchangeable partial-permutation shuffles*, published technical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-spectrum-and-exact-relaxation-of-exchangeable-partial--bb9bd3a50a6a.
5. *Occupancy-mediated joint Gaussian fluctuations of descents and inversions in random-to-top shuffles*, published technical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-occupancy-mediated-joint-gaussian-fluctuations-of-descents-and-i--7cc85a6a6c85.
