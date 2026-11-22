# Universal two-point correlation contraction and a finite-round defect floor for parallel Ising unmasking

## Finding

In a finite zero-field one-dimensional Ising Markov chain, an ideal parallel unmasking decoder cannot increase the *signed* correlation of any pair of spins when reveal batches are selected without using the realized spin values. Moreover, independent random reveal times impose a strictly positive, explicitly quantified excess of local thermodynamic defects at every finite number of rounds.

Precisely, for every length \(L\ge2\), every \(\lambda\in(-1,0)\cup(0,1)\), and every deterministic ordered partition of the sites into reveal batches, the output law \(Q\) obeys, for \(1\le i<j\le L\),
\[
0\le s^{j-i}\mathbb E_Q[\sigma_i\sigma_j]\le\rho^{j-i},\qquad \rho=|\lambda|,\quad s=\operatorname{sgn}\lambda.
\]
If the two adjacent sites \(i,i+1\) occur in the same batch, then
\[
\rho-s\mathbb E_Q[\sigma_i\sigma_{i+1}]\ge c(\rho),\qquad
c(\rho)=\frac{\rho(1-\rho^2)^2}{(1+\rho^3)^2}>0.
\]
For independent identically distributed site reveal-round labels \(R_i\in\{1,\ldots,K\}\) with \(\mathbb P(R_i=k)=a_k\) and \(\sum_{k=1}^K a_k=1\), let \(Q_{\mathbf a}\) be the output averaged over the labels. The excess probability of an energetically unfavorable edge \(D_i=(1-s\sigma_i\sigma_{i+1})/2\) satisfies, for every \(1\le i<L\),
\[
\mathbb E_{Q_{\mathbf a}}D_i-\mathbb E_P D_i
\ge\frac{c(\rho)}2\sum_{k=1}^K a_k^2
\ge\frac{c(\rho)}{2K},\qquad
\mathbb E_P D_i=\frac{1-\rho}{2}.
\]
Consequently the target cross-entropy excess, divided by the number of bonds, has the explicit strictly positive lower bound
\[
\frac{\mathbb E_{Q_{\mathbf a}}[-\log P(\sigma)]-\mathbb E_P[-\log P(\sigma)]}{L-1}
\ge \frac{c(\rho)}{2K}\log\!\frac{1+\rho}{1-\rho}.
\]
The logarithm is natural. The cross-entropy excess above is **not** being identified with either direction of Kullback--Leibler divergence. No optimality of the displayed constant is claimed.

## Assumptions and scope

The target probability law on \(\{-1,+1\}^{L}\) is
\[
P(\sigma_1,\ldots,\sigma_L)
=\frac12\prod_{i=1}^{L-1}\frac{1+\lambda\sigma_i\sigma_{i+1}}2.
\]
The length is finite and at least two, and \(0<|\lambda|<1\). No external magnetic field or periodic wraparound bond is present. A **fixed ordered partition** means disjoint subsets of sites whose union is all sites, revealing one subset in each round. At a round the decoder draws each newly revealed spin *independently of its co-revealed spins*, using the **exact target one-site conditional distribution given the previously revealed spins**. Previously revealed values remain unchanged. The partition may be sampled randomly provided its randomness is independent of all realized spins. For the explicit \(1/K\) bounds, reveal-round labels must additionally be independent and identically distributed across sites, with a common probability vector \(\mathbf a\). Empty rounds are allowed. The theorem does **not** claim the \(1/K\) bound for spatially coordinated or outcome-adaptive reveal schedules; for example a carefully coordinated partition can avoid revealing neighboring sites simultaneously.

We allow both ferromagnetic and antiferromagnetic signs, reducing the latter by a staggered gauge transform. A signed correlation refers to multiplying the physical two-point function by \(s^{j-i}\). Every output law considered is spin-flip symmetric, so these two-point functions are covariances as well.

## Proof

**1. Reduction to positive interactions.** Define \(\tau_j=s^j\sigma_j\). This bijective staggered transformation takes the target into a ferromagnetic zero-field Markov chain with nearest-neighbor correlation \(\rho\in(0,1)\), and takes exact single-site conditional sampling plus within-round independence to the same algorithm for \(\tau\). It suffices to show \(0\le\mathbb E_Q\tau_i\tau_j\le\rho^{j-i}\), and prove the adjacent deficiency for \(\tau\).

**2. Linear bridge conditionals.** Fix a set \(S\) of previously revealed sites and an unfilled site \(t\notin S\). Let \(l<t<r\) denote the nearest members of \(S\) to its left and right if present; put \(u=\rho^{t-l}\) and \(v=\rho^{r-t}\). Missing boundaries are represented by zero coefficients. With observed spins \(\tau_l=a,\tau_r=b\), the two-endpoint Ising bridge gives
\[
m_t(a,b):=\mathbb E_P(\tau_t\mid\tau_S)
=\frac{ua+vb}{1+uvab}
=A_ta+B_tb,
\]
where
\[
 A_t=\frac{u(1-v^2)}{1-u^2v^2},\qquad
 B_t=\frac{v(1-u^2)}{1-u^2v^2}.
\]
If an endpoint is absent, the corresponding coefficient is zero, with the remaining coefficient equal to the appropriate power of \(\rho\). Both coefficients are nonnegative, depend only on the already-revealed *positions*, and sum to \((u+v)/(1+uv)\le1\). When \(S\) is empty, \(m_t=0\). In short, write \(m_t=\sum_{b\in S}A_{tb}\tau_b\) with at most two nonzero coefficients and \(A_{tb}\ge0\).

For two distinct sites \(i<j\) not in \(S\), the conditional target covariance is zero when \(S\) separates the sites. Otherwise both sites lie in one unrevealed interval. Let \(l\) be the nearest revealed site strictly to the left of \(i\), and \(r\) the nearest strictly to the right of \(j\), and put \(u=\rho^{i-l}\), \(v=\rho^{r-j}\), \(c=\rho^{j-i}\). Set \(u=0\) or \(v=0\) for a missing respective endpoint. Directly summing the four values of the pair in this bridge yields
\[
\operatorname{Cov}_P(\tau_i,\tau_j\mid\tau_S)
=\frac{c(1-u^2)(1-v^2)}{(1+cuv\tau_l\tau_r)^2}\ge0.
\]
For missing endpoints, use the same formula with the irrelevant boundary spin omitted. This identity holds for *each* conditioning configuration, not merely in expectation. For adjacent sites \(j=i+1\) that are both still unrevealed, \(c=\rho\) and \(0\le u,v\le\rho\), so
\[
\operatorname{Cov}_P(\tau_i,\tau_{i+1}\mid\tau_S)
\ge\frac{\rho(1-\rho^2)^2}{(1+\rho^3)^2}=c(\rho).
\]
Indeed, the numerator factors are at least \(1-\rho^2\) and \(1+cuv\tau_l\tau_r\le1+\rho^3\).

**3. Correlation comparison through every round.** Let \(C^Q_{bc}=\mathbb E_Q\tau_b\tau_c\) and \(C^P_{bc}=\rho^{|b-c|}\) at the stage when all sites in \(S\) have been revealed. Because both the target and the decoding rule are invariant under flipping every spin, the means are zero. We inductively assume \(0\le C^Q_{bc}\le C^P_{bc}\) for all distinct previously revealed pairs; for equal indices \(b=c\), both second moments equal one. This holds vacuously before the first round.

For two old sites nothing changes. If \(i\) is new and \(j\) old, the law of conditional expectation under the decoder and under \(P\) is the *same* linear bridge function, so
\[
 C^Q_{ij}=\sum_{b\in S} A_{ib}C^Q_{bj},\qquad
 C^P_{ij}=\sum_{b\in S} A_{ib}C^P_{bj}.
\]
The induction hypothesis and nonnegative coefficients give the bounds. If \(i,j\) are distinct sites newly revealed in the *same* round, their output draws are conditionally independent, and
\[
 C^Q_{ij}=\sum_{b,d\in S} A_{ib}A_{jd}C^Q_{bd},
\]
whereas the target satisfies, by total covariance,
\[
 C^P_{ij}=\sum_{b,d\in S}A_{ib}A_{jd}C^P_{bd}
 +\mathbb E_P[\operatorname{Cov}_P(\tau_i,\tau_j\mid\tau_S)].
\]
All coefficients and all entries on the right are nonnegative, the diagonal entries agree, and the conditional-covariance term is nonnegative. Therefore the pairwise bounds propagate. Moreover the target-output difference for any two co-revealed sites is at least their expected *target* conditional covariance. For an adjacent co-revealed pair the pointwise lower bound from Step 2 supplies \(c(\rho)\) even if its old revealed context is distributed differently under \(Q\) and \(P\), because the induction comparison handles the context-dependent quadratic terms separately. This completes the proof for every ordered partition.

**4. Random independent reveal labels and information cost.** Conditioning on any realization of the labels yields an ordered partition, so all deterministic correlation bounds survive averaging. Two neighboring labels coincide with probability \(\sum_k a_k^2\). Since the deficiency is nonnegative for every partition and at least \(c(\rho)\) upon their coincidence,
\[
\rho-\mathbb E_{Q_{\mathbf a}}\tau_i\tau_{i+1}
\ge c(\rho)\sum_k a_k^2\ge c(\rho)/K,
\]
where the last step is Cauchy--Schwarz. The displayed defect bound follows by dividing by two. Finally the energy representation of the target gives exactly
\[
-\log P(\sigma)=\log2-(L-1)\log\frac{1+\rho}2
 +\log\frac{1+\rho}{1-\rho}\sum_{i=1}^{L-1}D_i.
\]
Subtracting the expectation under \(P\) from that under \(Q_{\mathbf a}\), then dividing by \(L-1\), finishes the cross-entropy inequality. No thermodynamic limit is used.

## Verification

The standalone standard-library Python program `check.py` exhaustively enumerates finite decoder output laws using exact rational arithmetic. It verifies normalization, spin-flip zero means, all signed pair inequalities and the co-reveal lower bound for \(L\in\{2,3,4,5\}\), both signs of the coupling, and thousands of labelled ordered partitions. It also checks the exact target law for single-site rounds and an independent nonuniform round-label mixture. Run from the folder containing this file as `python3 check.py`. Its verified output was:

```
PASS: 3812 pair inequalities; 571 adjacent co-reveal bounds;
PASS: 12 all-singleton partitions; independent-schedule mixture;
PASS: exact fraction mass, zero means, both interaction signs;
example collision probability = 7/18; conditional constant = 60/361
```

Finite enumeration is a regression test of the formulas, **not** a proof of the all-length theorem, which is the algebraic induction above. The local bridge-covariance identity can independently be verified by summing a two-spin Markov bridge with endpoint factors \((1+u a\tau_i)\), \((1+c\tau_i\tau_j)\), \((1+v b\tau_j)\) and normalizer proportional to \(1+cuvab\).

## Relationship to prior work

Baule's 2026 analysis develops exact labelled-gap evolution, path errors and generative perplexity for independently parallel-unmasked Markov data, and explicitly interprets excess spin switches as output quality loss. Its exact recurrences are broad enough to compute adjacent output counts numerically; the present statement instead proves a global all-pairs **correlation-order envelope for every prescribed non-adaptive batch partition** and an analytic positive local and \(1/K\) cross-entropy floor that does not require solving the gap recursion. Those inequalities and the accompanying sign-independent bridge comparison are the claimed contribution, not the definition of the decoder, the Ising bridge, or the general fact that co-revealed tokens lose correlations.

Lavenant and Zanella (2025) analyze factorization-error bounds and reveal-schedule optimization, and Wen, Liang and Lu (2026) obtain a conditional-total-correlation identity and coordinated zero-error sampling for Markov sources. These do not imply a positive floor for **all** schedules; instead they explain why the independent-identically-distributed label restriction is essential. Existing results that correct joint within-batch dependence by a joint sampler or rejection step fall outside the theorem's conditional-independence assumption. The matched primary text and relevant indexed results were compared by hypotheses and implications, not merely title similarity; implicit coverage in general correlation-inequality treatments remains a residual priority risk.

## Limitations

The theorem assumes the exact target one-site conditionals, a finite open-boundary zero-field nearest-neighbor chain with \(0<|\lambda|<1\), and no selection of reveal sites based on realized spin values. The quantitative \(1/K\) result requires independent identically distributed per-site round labels. Coordinated/hierarchical batches need not incur collisions; the theorem does not impose a uniform floor on them. It does not analyze learned-denoiser error, higher-dimensional or field-biased Ising measures, or the stability of the inequality under arbitrary perturbations of the conditional sampler. The constant \(c(\rho)\) is a conservative universal bound, not asserted sharp. Output cross-entropy excess is not a KL divergence. The source's exact finite-round recursion could conceivably imply related conclusions through further analysis, and priority cannot be certified by a finite literature search.

## References

1. Adrian Baule, *Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding*, arXiv:2611.07845v1 (first public November 5, 2026). https://arxiv.org/html/2611.07845v1
2. Hugo Lavenant and Giacomo Zanella, *Error Bounds and Optimal Schedules for Masked Diffusions with Factorized Approximations*, arXiv:2510.25544 (first public October 29, 2025). https://arxiv.org/abs/2510.25544
3. Chuling Wen, Weijie Liang and Jian Lu, *Conditional Total Correlation and the Serial Depth of Adaptive Parallel Sampling*, arXiv:2608.25505 (first public August 26, 2026). https://arxiv.org/abs/2608.25505
4. Shiyuan Zhang, Xuheng Li, Qiwei Di and Quanquan Gu, *Query-Efficient Rejection Sampling for Parallel Masked Diffusion*, arXiv:2610.22238 (first public October 15, 2026). https://arxiv.org/abs/2610.22238
