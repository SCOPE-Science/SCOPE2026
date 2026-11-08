# The twelve-slot first full sign reversal for two-vacancy parking correlations

## Finding

Consider \(n\) labeled spaces on a linear street and \(n-2\) sequentially arriving cars with independent uniform preferences in \(\{1,\ldots,n\}\). If a preference is occupied, car \(k\) searches to the right with any prespecified probability \(p_k\in[0,1]\), and otherwise searches to the left; it takes the nearest vacancy in its chosen direction or fails if none exists. An unsuccessful arrival terminates the experiment. Conditional on all \(n-2\) cars parking, write \(X_i\) for the indicator that site \(i\) is occupied.

**Exact first complete sign classification.** At \(n=12\), for all distinct \(i,j\in\{1,\ldots,12\}\),
\[
\operatorname{Cov}(X_i,X_j)>0 \quad\Longleftrightarrow\quad |i-j|=1,
\]
and the covariance is strictly negative when \(|i-j|\ge2\). Thus there are exactly 11 positive and 55 negative off-diagonal unordered pairs. Moreover, **12 is the smallest integer \(n\ge4\)** for which every adjacent pair has positive covariance. For every \(4\le n\le11\), at least one adjacent pair has negative covariance. All claims hold for every deterministic sequence of biases \((p_1,\ldots,p_{n-2})\), not merely a constant bias.

This is a first-occurrence and exact 12-site classification. Positivity for every \(n>12\) is **not asserted**.

## Assumptions and scope

Preferences are independent and uniform on the fixed street, not drawn conditioned on eventual success. Coins used at occupied preferences are conditionally independent and their biases \(p_k\) are fixed before arrivals, depending only on car index. Directional search does not reverse after reaching a boundary. Every accepted car remains at its first vacant site in the chosen direction. The random indicators and covariance are defined **conditional on all cars parking**, a positive-probability event. There is no wrap-around between sites \(n\) and 1. This is a finite-size statement for \(4\le n\le12\), with a complete sign matrix at \(n=12\).

## Proof

**1. Full-set distribution and independence of the direction biases.** For any set \(S\subseteq\{1,\ldots,n\}\) of size \(m\), let \(B_1,\ldots,B_r\) be its maximal consecutive occupied blocks, with lengths \(b_1,\ldots,b_r\). For the all-right rule, an arriving car whose final position lies in block \(B_h\) must have preferred a site of that same block: it cannot cross an unoccupied separator, because the separator would itself be filled. The restriction of preferences to \(B_h\), retaining their relative order, is a classical parking function on that block. Conversely, independently choosing such parking functions on all blocks and interleaving their ordered subsequences produces exactly \(S\). The classical count for block length \(b\) is \((b+1)^{b-1}\). Thus the number of preference sequences that produce precisely \(S\) without failure is
\[
N(S)=\frac{m!}{\prod_h b_h!}\prod_h(b_h+1)^{b_h-1}.
\]
Reflection of each block gives exactly the same count for the all-left rule. Define \(\mu_m(S)=N(S)/n^m\), a subprobability law supported on \(m\)-element sets.

Let \(K_+\) and \(K_-\) be the one-step sub-Markov kernels for all-right and all-left parking, respectively, restricted to successful extensions. By the preceding counting, \(\mu_mK_+=\mu_{m+1}=\mu_mK_-\) for every \(m<n\). The kernel for car \(k\) with direction bias \(p_k\) is \(K_{p_k}=p_k K_++(1-p_k)K_-\). Starting with \(\mu_0\) and applying induction shows that the success-set law at time \(m\) is \(\mu_m\) for any prescribed sequence of biases. The sum of its masses is the classical success probability, so conditioning on success does not introduce bias dependence. This argument does **not** assert that the full time-dependent path law is independent of the biases.

**2. Exact two-vacancy weights.** Specialize to \(m=n-2\). If the two vacancies lie at \(a<b\), the three occupied runs have lengths \(a-1\), \(b-a-1\), and \(n-b\). Define \(f(0)=1\), and \(f(r)=(r+1)^{r-1}/r!\) for \(r\ge1\). Define the positive integers
\[
W_{a,b}=(n-2)!\,f(a-1)f(b-a-1)f(n-b),\quad 1\le a<b\le n.
\]
Their integrality follows from the multinomial factor in step 1. Set
\[
Z=\sum_{a<b}W_{a,b},\qquad H_i=\sum_{j\ne i}W_{\min(i,j),\max(i,j)}.
\]
Conditionally on success, the probability that vacancies occur at exactly \(a,b\) is \(W_{a,b}/Z\), and the probability that site \(i\) is vacant is \(H_i/Z\). Because occupancy is the complement of vacancy, for distinct sites
\[
\operatorname{Cov}(X_i,X_j)=\frac{Q_{i,j}}{Z^2},\qquad Q_{i,j}=Z W_{\min(i,j),\max(i,j)}-H_iH_j.
\]
Every \(Q_{i,j}\) is an **exact integer**. The known total parking-function count gives \(Z=3(n+1)^{n-3}\), which is independently reproduced by the certificate for all required sizes.

**3. Exhaustive, exact sign certificate.** The accompanying standard-library-only Python program `CHECKER.py` computes every \(W_{a,b}\), \(Z\), \(H_i\), and \(Q_{i,j}\) using integer arithmetic. It checks each adjacent covariance for all \(n=4,\ldots,12\), and *every* distinct-site covariance at \(n=12\). For \(n=4,\ldots,8\), all adjacent signs are negative. For \(n=9,10,11\), each sign string in increasing edge order contains both positive and negative entries:

| \(n\) | Signs of \(Q_{i,i+1}\), \(i=1,\ldots,n-1\) |
|---:|:---|
| 4 | `---` |
| 5 | `----` |
| 6 | `-----` |
| 7 | `------` |
| 8 | `-------` |
| 9 | `+--++--+` |
| 10 | `+-+++++-+` |
| 11 | `+-++++++-+` |
| 12 | `+++++++++++` |

For \(n=12\), the **smallest** adjacent integer numerator is \(581409157300000000>0\); among the 55 nonadjacent pairs, the **largest** numerator is \(-3692131919133336000<0\). These exact inequalities certify all 66 signs and minimality at 12. There is no floating-point rounding, random sampling, truncation, or extrapolation.

## Verification

Run `python CHECKER.py` with the standard Python 3 library. The program performs 410 exact integer/rational assertions, compares the analytic two-vacancy weights against direct deterministic all-right enumeration for \(n\le7\), and checks the same weights against dynamic programming with fixed and nonconstant directional-bias sequences. It reproduces the sign strings above and the extremal sign bounds. The proof of bias independence and the weight formula is analytic; the finite sign classification is proved by the transparent exact finite certificate. All source code is embedded with this result.

## Relationship to prior work

Durmić, Han, Harris, Ribeiro, and Yin (2022), Theorem 2, prove **only the total probability that all cars park** is independent of a constant directional bias, and investigate bias-dependent last-car preference statistics. Tian and Treviño (2021) prove a related total success count. Kenyon and Yin (2021) study generalized classical parking functions and forest correspondences. Harris, Ribeiro, and Yin (2025) derive preference distributions using multi-shuffle counting. Most importantly, Nadeau (2026), Proposition 3.5 and Theorem 4.2, already give a much broader bilateral-procedure framework and block-counting tools: **the occupied-set weight formula is not claimed as new here**. The contribution assessed here is the strict *joint spatial covariance sign classification at the first all-adjacent-positive size*, including the exact finite cutoff \(12\), not the classical counts or general bilateral invariance.

Chassaing and Louchard (2002/2005 preprint) analyze asymptotic block sizes in **circular** linear probing. Their model and the block-asymptotic statements do not state this exact finite **linear-street**, two-vacancy sign matrix. A targeted search did not find the particular cutoff or matrix in the inspected sources; this is a best-knowledge originality assessment, not proof of historical uniqueness.

## Limitations

The proof assumes independent uniform preferences, linear non-wrapping search, success conditioning, exactly two vacancies and per-arrival prespecified directional biases. The sign classification covers only \(n=12\), with the minimality check over \(4\le n\le11\). No monotonicity or classification for larger \(n\), other vacancy counts, history-dependent coin biases, or nonuniform preferences is claimed. Exact finite arithmetic verifies the 12-site result, not an infinite-size theorem. The computation follows from known parking-function block counts, which are credited above. Independent mathematical review remains unperformed.

## References

1. I. Durmić, A. Han, P. E. Harris, R. Ribeiro and M. Yin, *Probabilistic Parking Functions*, arXiv:2211.00536v1 (November 1, 2022), Theorems 1–2 and Section 2.6. https://arxiv.org/pdf/2211.00536
2. M. Tian and E. Treviño, *Generalizing Parking Functions with Randomness*, arXiv:2111.12850v1 (November 25, 2021), Section 2. https://arxiv.org/pdf/2111.12850
3. R. Kenyon and M. Yin, *Parking Functions: From Combinatorics to Probability*, arXiv:2103.17180v1 (March 31, 2021). https://arxiv.org/pdf/2103.17180
4. P. E. Harris, R. Ribeiro and M. Yin, *Probabilistic (m,n)-Parking Functions*, *Electronic Journal of Combinatorics* 32(4), P4.39 (2025), Sections 2.1–2.2. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i4p39/pdf/
5. P. Nadeau, *Bilateral Parking Procedures*, arXiv:2602.17210v1 (February 19, 2026), Proposition 3.5, Theorem 4.2. https://arxiv.org/pdf/2602.17210
6. P. Chassaing and G. Louchard, *Phase Transition for Parking Blocks, Brownian Excursion and Coalescence*, *Random Structures & Algorithms* 21 (2002), 76–119; arXiv:math/0501060v1. https://arxiv.org/pdf/math/0501060
