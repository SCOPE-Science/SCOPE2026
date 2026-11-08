# Geometric lengths of complete-window clusters in the linear expiring coupon collector

## Finding

Let \(a>1\) be fixed. For each \(n\ge2\), set \(M_n=\lfloor an\rfloor\), and sample independent uniform coupon types \(X_t\in\{1,\ldots,n\}\) at all integer times. A length-\(M_n\) window is **onto** if all \(n\) types occur. Condition on the stationary entrance event \(E_0\) that the preceding window is not onto but the window ending at time zero is onto. Define the complete-window cluster length

\[
L_n=\min\{j\ge1:W_j\text{ is not onto}\}.
\]

Let \(\tau_a>0\) be the unique solution of \(\tau_a/(1-e^{-\tau_a})=a\), and put \(q_a=e^{-\tau_a}\). Then

\[
\boxed{\Pr(L_n>k\mid E_0)\longrightarrow(1-q_a)^k\quad\text{for every fixed integer }k\ge0.}
\]

Thus \(L_n\), under entrance conditioning, converges to a geometric random variable supported on \(\{1,2,\ldots\}\) with success parameter \(q_a\). Moreover,

\[
\boxed{\mathbb E(L_n\mid E_0)\longrightarrow e^{\tau_a}.}
\]

At finite size, the immediate-exit probability and mean are exactly

\[
\Pr(L_n=1\mid E_0)=\frac{n-1}{n}\frac{S(M_n-2,n-2)}{S(M_n-1,n-1)},\qquad
\mathbb E(L_n\mid E_0)=\frac{nS(M_n,n)}{(n-1)S(M_n-1,n-1)},
\]

where \(S(m,r)\) is the Stirling number of the second kind. These two identities hold whenever \(M_n\ge n\ge2\), not only on the linear scale.

## Assumptions and scope

All draws are independent and uniform over the same set of \(n\) coupon types; expiration is deterministic, after exactly \(M_n\) draws; conditioning is on a *stationary entrance* into the onto-window set, not on a uniformly sampled onto window or the first complete window of an initially empty process. Limits hold for every fixed real \(a>1\); the integer cutoff is a floor. No simultaneous limit \(a=a_n\to1\), \(a_n\to\infty\), or logarithmic-window conclusion is claimed here. The primary subject is discrete occupancy and stochastic window dynamics (MSC2020 60C05).

## Proof

**1. The entrance law.** Let \(N=n-1\) and \(m=M_n-1\). The entrance-counting argument in Long (2026, Theorem 3.1) implies that, conditioned on \(E_0\), the common middle block \(B=(X_{-M_n+1},\ldots,X_{-1})\), with \(m\) entries, is uniformly distributed over all onto words on the \(N\) types other than the newly appended type \(b=X_0\). The \(m\)-block has \(N!S(m,N)\) possible values, each equally likely. The earlier departing type is constrained to differ from \(b\), but plays no role in future shifts. The fresh future draws remain independent uniform draws from all \(n\) types.

**2. Singleton positions.** For any \(r\) specified, distinct positions of \(B\), the event that all their symbols occur exactly once in the entire block has probability

\[
p_{n,r}=\frac{S(m-r,N-r)}{S(m,N)}.
\]

Indeed, those \(r\) positions must carry distinct colors; after assigning them, the other \(m-r\) positions must be an onto word on the remaining \(N-r\) colors. The factorial factors cancel. Here \(0\le r\le N\) and \(m\ge N\).

Put \(\tau=\tau_a\). The distribution of counts in an onto word coincides with independent zero-truncated Poisson counts of parameter \(\tau\), conditioned on their sum being \(m\). More precisely, for fixed \(r\), let \(D_1,\ldots,D_N\) be independent variables with

\[
\Pr(D_i=j)=\frac{\tau^j}{j!(e^\tau-1)},\qquad j\ge1.
\]

The standard lattice local central limit theorem, with its fixed-shift version, gives

\[
\frac{\Pr(D_1+\cdots+D_{N-r}=m-r)}{\Pr(D_1+\cdots+D_N=m)}\longrightarrow1.
\]

The denominator is asymptotic to \((2\pi N\operatorname{Var}(D_1))^{-1/2}\), since \(m/N\to a=\mathbb E D_1\). For the numerator, its deviation from its own mean is \(r(a-1)+o(1)\), bounded as \(n\to\infty\). The fixed-shift local limit follows directly by Fourier inversion of the analytic span-one characteristic function. Applying the generating-function identity for Stirling numbers yields

\[
p_{n,r}=
\frac{(N)_r}{(m)_r}\left(\frac{\tau}{e^\tau-1}\right)^r
\frac{\Pr(D_1+\cdots+D_{N-r}=m-r)}{\Pr(D_1+\cdots+D_N=m)}
\longrightarrow\left(\frac{\tau}{a(e^\tau-1)}\right)^r=e^{-r\tau}.
\]

Here \((j)_r=j(j-1)\cdots(j-r+1)\). Consequently, for every fixed \(k\), the indicators that the first \(k\) positions of \(B\) are singleton positions converge jointly to \(k\) independent Bernoulli variables with success probability \(q_a=e^{-\tau_a}\). The finite-dimensional assertion follows because all joint all-one probabilities for subsets converge to the appropriate powers.

**3. Singleton positions control short clusters.** Fix \(k\ge1\). During the next \(k\) shifts, the newly appended color \(b\) still lies in the window when \(n\) is large (since \(k<M_n\)). A color whose last occurrence in the original block leaves during these shifts can cause failure. If a color occurs at least twice among the first \(k\) positions, the chance of this obstruction is negligible: for fixed \(k\),

\[
\Pr(\exists i<j\le k:B_i=B_j\mid E_0)=O_{a,k}(1/n).
\]

To check this bound, use exchangeability of positions and the zero-truncated Poisson count representation: the first two positions coincide with conditional probability

\[
\frac{N\,\mathbb E[(D_1)_2\mid\sum_{i=1}^ND_i=m]}{m(m-1)}=O_a(1/N),
\]

since \(\mathbb E[(D_1)_2\mid\sum D_i=m]\) stays bounded, by the fixed-coordinate local limit and the exponential tails of the truncated Poisson law. A union bound gives the claim. Furthermore, any one of the first \(k\) original singleton colors is re-drawn in the next \(k\) independent draws with conditional probability at most \(k/n\), so the probability that any such rescue occurs is at most \(k^2/n\).

Outside these two exceptional events, the consecutive windows remain onto for \(k\) shifts **if and only if** none of the first \(k\) positions of \(B\) was a singleton. Taking limits and using Step 2 gives the geometric survival formula.

**4. Exact finite identities and the limiting mean.** The first departing position of \(B\) is a singleton with probability \(S(m-1,N-1)/S(m,N)\). Given this event, the immediate replacement draw fails to match that singleton with probability \((n-1)/n\). This proves the exact immediate-exit formula.

The stationary onto mass and entrance flux (Long, Proposition 2.1 and Theorem 3.1) are respectively

\[
\pi_{n,M}=\frac{n!S(M,n)}{n^M},\qquad
\mu_{n,M}=\frac{(n-1)(n-1)!S(M-1,n-1)}{n^M}.
\]

Counting total onto-window time by disjoint entrance-initiated runs gives the exact stationary renewal-reward identity \(\mathbb E(L_n\mid E_0)=\pi_{n,M}/\mu_{n,M}\). For completeness, this equality follows by dividing the ergodic long-time frequency of onto windows by the ergodic frequency of new entrances, without assuming independence of successive runs. The same fixed-parameter zero-truncated Poisson local limit as in Step 2, now applied to \((M,n)\) and \((M-1,n-1)\), gives

\[
\frac{S(M,n)}{S(M-1,n-1)}\longrightarrow\frac{a(e^{\tau_a}-1)}{\tau_a}=e^{\tau_a}.
\]

The extra prefactor \(n/(n-1)\to1\) proves the mean limit.

## Verification

Run `python3 checker.py` with Python 3; no external libraries are required. It verifies the exact Stirling identity for prescribed singleton positions, the immediate-exit formula, direct first-shift and multi-shift survival probabilities by enumeration for small \(n,M\), and finite-size approach of the two singleton joint probabilities and mean to their stated limits. The program reports 134 checks and prints the finite values. The asymptotic conclusion for arbitrary \(n\) is established by the proof above; finite checks are not used as an infinite proof.

## Relationship to prior work

Christopher D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws* (arXiv:2604.26298v1, April 29, 2026), establishes the exact entrance flux, rare first-entry asymptotics and linear-window exponential *waiting time* on its exponentially long scale. It discusses clusters and provides a zero-truncated Poisson local estimate. It does not state a distribution for the length of a consecutive run of complete windows conditional on a stationary entrance. The geometric *cluster-length* limit above is distinct from the previously established exponential *first-hitting-time* limit. The exact mean via occupancy divided by flux is a direct consequence of the existing formulas and is not represented as a separately new result. General finite-surjection occupancy asymptotics and local central limit theorems are acknowledged as standard tools.

## Limitations

The result conditions on entrance; it is not the length-biased distribution seen by selecting an arbitrary complete window. It does not establish independence between successive clusters or between lengths and interarrival times. The primary novelty claim is the linear-window geometric cluster-duration distribution, not the finite Stirling counts or the known flux identities. Broad historical priority among scan-statistic and runs literature is not conclusively settled by the targeted searches and primary-source comparisons; independent review remains to be performed.

## References

- C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1 (first posted April 29, 2026). https://arxiv.org/html/2604.26298v1
- V. V. Petrov, *Sums of Independent Random Variables*, Chapter VII: lattice local limit theorems (cited in the preceding paper's Appendix A). Classical result used at fixed positive truncated-Poisson parameter.
- N. G. de Bruijn, *Asymptotic Methods in Analysis*, for coefficient/saddle-point methods for surjection counts (background only; no novel result attributed to this text).
