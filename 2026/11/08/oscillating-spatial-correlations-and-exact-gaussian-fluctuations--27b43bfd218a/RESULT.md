# Oscillating spatial correlations and exact Gaussian fluctuations in trimer sequential covering

## Finding

Consider random sequential covering of the initially empty integer lattice by length-three intervals (trimers). Each proposed trimer covering sites \(i,i+1,i+2\), \(i\in\mathbb Z\), has an independent rate-one Poisson attempt clock; a proposal is accepted if it covers at least one previously uncovered site. Let \(K_s\) be the terminal number of accepted trimers covering site \(s\). Let \(Y_s=\mathbf 1\{K_s=3\}\) mark a *triply covered* site, and put \(S_n=\sum_{s=1}^{n}Y_s\).

The stationary field \((Y_s)_{s\in\mathbb Z}\) is six-dependent: groups of observations whose index sets are separated by at least seven lattice steps are independent. This range is sharp since the covariance at distance six is strictly positive. Its one-site probability is the known value \(p=\Pr(Y_0=1)=31/630\). The complete nonzero-lag covariance profile is:

| Distance \(d\) | \(\Pr(Y_0=Y_d=1)\) | \(\operatorname{Cov}(Y_0,Y_d)\) |
|---:|---:|---:|
| 1 | \(1/80\) | \(16001/1587600\) |
| 2 | \(127/45360\) | \(601/1587600\) |
| 3 | \(17/30240\) | \(-5903/3175200\) |
| 4 | \(29/59400\) | \(-16879/8731800\) |
| 5 | \(629/151200\) | \(5521/3175200\) |
| 6 | \(583747/194594400\) | \(788077/1362160800\) |
| \(d\ge 7\) | \(p^2\) | \(0\) |

In particular, *the covariance changes sign twice* and is not a monotone function of spatial distance. Writing
\[
\sigma^2=p(1-p)+2\sum_{d=1}^{6}\operatorname{Cov}(Y_0,Y_d)
=\frac{8819999}{136216080}>0,
\]
the number of triply covered sites satisfies
\[
\frac{S_n-np}{\sqrt n}\ \Longrightarrow\ N(0,\sigma^2),
\qquad \frac{S_n}{n}\longrightarrow p\quad\text{almost surely}.
\]
The variance is exactly, for every integer \(n\ge 7\),
\[
\operatorname{Var}(S_n)
=\frac{8819999}{136216080}\,n-\frac{52387}{2702700}.
\]

## Assumptions and scope

The lattice is \(\mathbb Z\), initially empty. Each trimer *start position* has its own independent homogeneous rate-one Poisson process. At an attempted deposition, the trimer is retained precisely when at least one of its three sites is uncovered. Multiple accepted trimers may overlap. The terminal multiplicity at each fixed site is almost surely well-defined and at most three. The claimed finite-window laws are those of the infinite-volume, translation-invariant process; \(S_n\) is measured on \(n\) consecutive sites within that infinite-volume law, not under arbitrary finite-interval boundary rules.

## Proof

**1. First-arrival representation.** Let \(U_i\) denote the first attempt time of the trimer beginning at \(i\). These are independent exponential variables of mean one, and their relative order on every finite set is uniform. The first attempted trimer containing any given site must be accepted, because before that attempt the site is empty. Consequently a later trimer beginning at \(i\) is accepted if and only if it is the first proposed trimer containing at least one of its three sites. Later repeated attempts from the same start cannot succeed once its first attempt has been rejected: every site in its support is already occupied, permanently. Thus the terminal acceptance indicator is exactly
\[
A_i=\mathbf 1\!\left\{\exists u\in\{i,i+1,i+2\}:U_i=\min_{j\in\{u-2,u-1,u\}}U_j\right\},
\qquad K_s= A_{s-2}+A_{s-1}+A_s.
\]
This representation is valid almost surely without any tie convention, since finitely many relevant exponential clocks have distinct first-arrival times.

**2. Finite dependence.** The value \(K_s\) is a function only of the seven independent clocks \(U_{s-4},\ldots,U_{s+2}\). Distinct sets of site observations with separation at least seven use disjoint sets of independent clocks; hence their generated sigma-fields are independent. This proves six-dependence of \((Y_s)\), not merely pairwise zero covariance beyond distance six.

**3. Exact, exhaustive local joint laws.** For each \(1\le d\le 6\), take the \(d+7\) clock indices
\[
B_d=\{-4,-3,\ldots,d+2\}.
\]
For \(S\subseteq B_d\) and an unexposed index \(i\in B_d\setminus S\), define
\[
e(S,i)=\mathbf 1\bigl\{\exists u\in\{i,i+1,i+2\}:S\cap\{u-2,u-1,u\}=\varnothing\bigr\},
\]
\[
\delta_0(S,i)=e(S,i)\mathbf 1\{-2\le i\le0\},\qquad
\delta_d(S,i)=e(S,i)\mathbf 1\{d-2\le i\le d\}.
\]
Let \(F_d(S;a,b)\) be the integer number of permutations of \(S\) that lead to exactly \(a\) accepted trimers covering zero and \(b\) covering \(d\), considering the exposed centers in arrival order. Starting with \(F_d(\varnothing;0,0)=1\), extend *every* state and unexposed center by the exact recurrence
\[
F_d\bigl(S\cup\{i\};a+\delta_0(S,i),b+\delta_d(S,i)\bigr)
\mathrel{+}=F_d(S;a,b).
\]
The accepted status of any trimer contributing to these two sites depends only on the clocks in \(B_d\), so this recursion is exhaustive; the number of terminal permutations is \((d+7)!\). Therefore
\[
\Pr(K_0=a,K_d=b)=\frac{F_d(B_d;a,b)}{(d+7)!}.
\]
Executing the complete integer recurrence (standalone \(\texttt{verify.py}\)) gives the six joint probabilities in the table. Independent direct enumeration of all \(8!\) and \(9!\) arrival orders reproduces the first two joint entries. For each distance the two complete marginals equal \((0,173/315,253/630,31/630)\), agreeing with the established one-point law. The six covariances follow by subtracting \(p^2\); beyond distance six they vanish by Step 2. Since the covariance at distance six is \(788077/1362160800>0\), six is the exact dependence *range* in the sense of nonvanishing pairwise covariance.

**4. Exact variance and limit laws.** Stationarity and six-dependence give, for any integer \(n\ge1\),
\[
\operatorname{Var}(S_n)=np(1-p)+2\sum_{d=1}^{6}(n-d)_+\operatorname{Cov}(Y_0,Y_d).
\]
Inserting the six rational entries produces the stated \(\sigma^2\) and, for \(n\ge7\), the exact additive correction. This verifies explicitly that the limiting variance is strictly positive. The strong law follows by partitioning the stationary sequence into seven independent and identically distributed subsequences according to residue classes modulo seven.

For completeness, the central limit theorem also has a direct blocking proof. Partition \(\{1,\ldots,n\}\) into consecutive main blocks of length \(b_n=\lfloor n^{1/3}\rfloor\), separated by gaps of six indices, and discard any trailing remainder. The centered sums over main blocks are independent because their underlying clock windows do not intersect. Their aggregate variance divided by \(n\) tends to \(\sigma^2>0\) by the covariance identity above; the absolute size of each centered block sum is at most \(b_n=o(\sqrt n)\), so the Lindeberg condition holds. The discarded centered terms have variance \(O(n/b_n+b_n)=o(n)\) because each covariance vanishes beyond distance six. The independent-block central limit theorem and Slutsky's theorem give the claimed Gaussian limit.

## Verification

The standalone Python 3 program \(\texttt{verify.py}\) uses only the standard library and recomputes every rational pair probability using a finite subset-state dynamic program. It verifies full probability normalization, all marginal laws, the sign profile, the lag-seven independence benchmark, the variance constant, and the exact finite-size correction. It separately enumerates every deposition ordering for distances one and two using the original deposition rule rather than the first-arrival acceptance criterion. Run from the extracted artifact directory:

```text
python3 verify.py
```

The independent direct enumerations give \(504/8!=1/80\) and \(1016/9!=127/45360\). These are exhaustive finite checks of the local rational coefficients, not simulations standing in for the limit theorem; the general dependence and central limit proofs are given above.

## Relationship to prior work

Krapivsky (arXiv:2209.03992, first public September 8, 2022) introduced the sequential covering rule, solved dimer statistics, and investigated trimer single-site observables. Viot and Krapivsky (arXiv:2410.12373, first public October 16, 2024) solved the trimer single-site multiplicity probabilities, notably \(\pi_3(\infty)=31/630\), and computed selected joint probabilities needed for their one-site hierarchy. Their discussion notes limited correlation range, but does not state the six-distance *triple-occupation* covariance profile, the alternating signs, or the exact Gaussian variance of the macroscopic count. The one-site probability and general finite-range heuristic are therefore not claimed as new. The new quantitative result concerns the nonconsecutive, long-distance pair laws and the resulting explicitly normalized fluctuation theorem.

## Limitations

The theorem concerns infinite-volume one-dimensional trimer covering with independent homogeneous attempt clocks and observations in the fully covered terminal state. It does not establish the same rational covariance table for dimers, longer polymers, higher dimensions, or a finite interval with different boundary rules. At finite observation times, the clock-localization argument remains valid, but the displayed terminal rational table does not automatically apply. Exact historical priority against all unindexed literature has not been independently established.

## References

1. P. L. Krapivsky, *Random Sequential Covering*, arXiv:2209.03992 (first posted September 8, 2022), https://arxiv.org/abs/2209.03992.
2. P. Viot and P. L. Krapivsky, *Random sequential covering of a one-dimensional lattice by k-mers*, arXiv:2410.12373 (first posted October 16, 2024), https://arxiv.org/abs/2410.12373, published in *Journal of Statistical Mechanics: Theory and Experiment* 2025, 013202, https://doi.org/10.1088/1742-5468/ad930b.
