# Quenched invariance and a quantitative quadratic-variation bound for independently resampled one-factor bootstrap walks

## Finding

In the inclusion-induced, one-factor Markov bootstrap-walk model of Hamza and Tournier, suppose the cardinality-grouped Bernoulli coefficients are mutually independent **across both time and cardinality**, with success parameters uniformly separated from zero and one. The source's Corollary 9 establishes the *annealed* two-dimensional Brownian limit; the following theorem establishes its *quenched* counterpart with an almost-sure quantitative bound.

For every \(\delta>0\), almost surely with respect to the coefficient environment,
\[
E^{\beta}\!\left[\left(\frac1N\sum_{j=0}^{N-1}\zeta_j\right)^2\right]
=O_{\beta,\delta}\!\left(N^{-1/2+\delta}\right).
\]
Consequently, conditional on almost every environment, the processes
\[
\left(\frac{X_{\lfloor Nt\rfloor}}{\sqrt N},\frac{Y_{\lfloor Nt\rfloor}}{\sqrt N}\right)_{0\le t\le1}
\]
converge weakly in \(D([0,1],\mathbb R^2)\) to a pair of independent standard Brownian motions. This asserts **quenched**, not merely annealed, convergence.

## Assumptions and scope

Let \((\xi_i)_{i\ge1}\) be independent fair signs, and independently let the array \((\beta_{n,k}:n\ge1,0\le k\le n)\) consist of mutually independent Bernoulli variables with deterministic parameters
\[
\epsilon\le p_{n,k}=\mathbb P(\beta_{n,k}=1)\le1-\epsilon,
\qquad 0<\epsilon<\tfrac12.
\]
For \(n\ge1\), put \(S_n=\sum_{i=1}^n\mathbf1_{\{\xi_i=-1\}}\), and set
\[
\zeta_0=1,\qquad
\zeta_n=(-1)^{\sum_{k=0}^{S_n}\binom{S_n}{k}\beta_{n,k}},\qquad
X_N=\sum_{i=1}^N\xi_i,\qquad Y_N=\sum_{i=1}^N\zeta_{i-1}\xi_i.
\]
The exponent of \((-1)\) is interpreted as an integer; even binomial coefficients do not affect parity. Expectations \(E^{\beta}\) integrate over the signs with the entire coefficient environment held fixed. The theorem holds for arbitrary deterministic, nonidentical parameters subject to the displayed uniform bounds. Neither independence of the signs after conditioning on a *random* future nor independence of \(\zeta_n\) under \(E^\beta\) is assumed.

## Proof

**1. Uniform annealed decay.** Write \(c=1-2\epsilon\in(0,1)\), let \(b(s)\) denote the number of ones in the binary expansion of the nonnegative integer \(s\), and define
\[
a_j=E_{\xi}\big[c^{2^{b(S_j)}}\big],\quad j\ge1.
\]
By independence of the \(\beta_{j,k}\) within a time slice and Lucas' binomial parity theorem,
\[
\left|E_{\beta}[\zeta_j\mid\xi]\right|
=\left|\prod_{\substack{0\le k\le S_j\\\binom{S_j}{k}\text{ odd}}}(1-2p_{j,k})\right|
\le c^{2^{b(S_j)}}.
\]
We claim \(a_j=j^{-1/2+o(1)}\) in the *upper-bound* sense \(a_j\le j^{-1/2+o(1)}\). Indeed, \(S_j\) has a \(\operatorname{Bin}(j,1/2)\) law, so its largest point mass is at most \(C(j+1)^{-1/2}\) for a universal constant \(C\). Write \(M_j=\lfloor\log_2 j\rfloor+1\) for \(j\ge2\), and \(h_j=\lceil 2\log_2\log(j+3)\rceil\). At most
\[
\sum_{r=0}^{h_j}\binom{M_j}{r}
\le (h_j+1)M_j^{h_j}=\exp(O((\log\log(j+3))^2))
\]
integers in \(\{0,\ldots,j\}\) have at most \(h_j\) binary ones. On the complementary event, \(c^{2^{b(S_j)}}\le\exp[-|\log c|(\log(j+3))^2]\). Thus
\[
a_j\le\frac{C}{\sqrt{j+1}}\exp(O((\log\log(j+3))^2))
+\exp[-|\log c|(\log(j+3))^2]
\le j^{-1/2+o(1)}.
\]
The constant implicit in the \(o(1)\) estimate depends only on \(\epsilon\).

**2. Annealed empirical-bracket bound.** Write \(Q_N=N^{-1}\sum_{j=0}^{N-1}\zeta_j\), \(F_N(\beta)=E^{\beta}[Q_N^2]\), and \(\bar F_N=E_{\beta}F_N\). If \(0\le i<j\), distinct time slices of the coefficient array are independent, even after conditioning on the entire sign sequence. Since \(|E_{\beta}[\zeta_i\mid\xi]|\le1\), step 1 gives
\[
\left|E_{\beta,\xi}(\zeta_i\zeta_j)\right|\le a_j.
\]
The diagonal contributions equal one. Consequently,
\[
0\le\bar F_N\le \frac1N+\frac2{N^2}\sum_{j=1}^{N-1}j a_j
\le N^{-1/2+o(1)}.
\]
In particular, for every fixed \(\delta>0\), \(\bar F_N=O_{\epsilon,\delta}(N^{-1/2+\delta})\).

**3. Concentration over time slices.** The \(N-1\) random vectors \(\boldsymbol\beta_j=(\beta_{j,k})_{0\le k\le j}\), \(1\le j<N\), are mutually independent. Replacing one entire time slice, with the sign path held fixed, changes precisely one summand in \(Q_N\), so \(|Q_N-Q'_N|\le2/N\). Since both averages have absolute value at most one, \(|Q_N^2-(Q'_N)^2|\le4/N\), and hence
\[
|F_N(\beta)-F_N(\beta')|\le4/N.
\]
The bounded-differences inequality therefore implies for all \(u>0\)
\[
\mathbb P_{\beta}\bigl(|F_N-\bar F_N|\ge u\bigr)
\le2\exp(-Nu^2/8).
\]
With \(u=N^{-1/2+\delta}\), the right side is summable in \(N\) for any fixed \(\delta>0\). Borel--Cantelli, step 2, and a countable intersection over positive rational \(\delta\) give a *single* full-environment-probability event on which the asserted estimate holds for **every** \(\delta>0\).

**4. Quenched functional limit.** On that event \(F_N(\beta)\to0\), so \(Q_N\to0\) in \(P^{\beta}\)-probability. For any fixed \(t\in(0,1]\),
\[
\frac1N\sum_{j=0}^{\lfloor Nt\rfloor-1}\zeta_j
=\frac{\lfloor Nt\rfloor}{N}\,Q_{\lfloor Nt\rfloor}
\longrightarrow0
\]
in \(P^\beta\)-probability. The partial-sum process is uniformly Lipschitz at grid scale (its increments over \(hN\) indices are at most \(h+1/N\)), so convergence on rational time points yields uniform-in-time convergence in probability. The increments \((\xi_i,\zeta_{i-1}\xi_i)\) form a bounded-increment martingale difference sequence under every fixed environment; their predictable quadratic covariation, divided by \(N\), is exactly the preceding signed partial-sum process. The diagonal quadratic variations converge to \(t\), and the jumps vanish under normalization. The vector martingale functional central limit theorem, equivalently the previously established bootstrap-walk criterion, gives the claimed pair of independent Brownian limits.

## Verification

The finite checker `check.py` independently enumerates all sign prefixes and all coefficient environments through \(N=5\) in the fair-parameter specialization. It verifies exactly, using integer arithmetic, the identities \(E_\beta F_N=1/N\), the time-slice replacement bound, and Lucas' parity identity at the enumerated sizes: 84,143 assertions. Run `python check.py`. The checker tests finite samples of identities and is **not** a proof of the almost-sure or functional limit. Those conclusions follow from the analytic steps above.

## Relationship to prior work

Hamza--Tournier, *Are random random walks normal?* (arXiv:2610.01658v1, October 1, 2026), Section 4.2, Proposition 8 and Corollary 9, derives the **annealed** zero-correlation Brownian limit for precisely the independent time-and-cardinality, uniformly elliptic one-factor model above; its introductory table and discussion explicitly leave the corresponding quenched claim unresolved. The paper's Proposition 7 already proves a quenched *first-moment* condition, but not the required quadratic-variation condition. The present statement provides the missing quenched second-moment convergence and its rate. The count of odd binomial coefficients by Lucas' theorem and the general deterministic-coefficient martingale limit criterion are standard/prior ingredients. Collevecchio--Hamza--Shi--Williams (2022) establishes the deterministic bootstrap-walk functional criterion, not this almost-every-environment conclusion for the random cardinality-grouped array.

## Limitations

The rate is an upper bound, not an optimality claim. The result requires independent **time slices**; it does not assert the analogous statement when coefficient variables persist across time, including the separate time-invariant cardinality-grouped model. The coefficient success probabilities must stay uniformly away from zero and one. No rate in a path-space probability metric is established; the rate controls the quenched empirical cross-bracket in \(L^2\), sufficient for weak convergence. Priority beyond the inspected foundational and motivating texts is not independently certified.

## References

1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1, first posted 2026-10-01. https://arxiv.org/html/2610.01658v1, especially Section 4.2, Proposition 8 and Corollary 9.
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, *Electronic Journal of Probability* **27** (2022), paper 92, DOI 10.1214/22-EJP818; https://arxiv.org/abs/2010.16000.
3. C. McDiarmid, *On the method of bounded differences*, in *Surveys in Combinatorics 1989*, London Mathematical Society Lecture Note Series 141, 1989, pp. 148--188.
4. E. Lucas, *Théorie des Fonctions Numériques Simplement Périodiques*, *American Journal of Mathematics* **1** (1878), 184--196, 197--240, 289--321 (binomial parity theorem).
