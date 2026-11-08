# Scientific review: sharp logarithmic screening window

## Correctness (PASS)

The one-step selected-label calculation gives exact transitions \(p_t=\beta^{k_t}\) and \(q_t=(1-\beta)^{k_t}\), with no approximation or independence beyond the stated fresh-batch assumption. The three possible pathwise behaviors follow respectively from Borel--Cantelli, nonzero/zero infinite products, and summability of expected transition counts. The distinction between convergence in probability and almost-sure eventual recovery follows from the exact marginal recursion. The logarithmic endpoints, including equality, use elementary comparison with the harmonic series. The packaged `verify.py` independently reproduces the finite transition probabilities and recurrence by exact-rational enumeration (952 checks). The infinite-time conclusions rely on the written proof, not on a simulation.

## Originality (PASS, with priority uncertainty)

The fixed-\(k\) minimum-loss SGD rule and its possible trapping near corrupted quadratic samples are known from Shah--Wu--Sanghavi (2020). The 2026 quantile-loss paper develops fixed-size finite-sum filtering and a small-sample error-floor analysis; the 2026 streaming Kaczmarz paper uses a different quantile criterion and a finite-horizon logarithmic sample size. The present claim is specifically the **sharp pathwise trichotomy under an increasing number of fresh candidates**, including both critical constants, endpoint classification and the strict separation of marginal recovery from eventual pathwise recovery. The relevant primary text and records checked did not reveal this exact conjunction. General inhomogeneous-chain theory and unindexed special-case calculations pose genuine residual priority risks; the result does not assert that its underlying Borel--Cantelli tools or fixed-size SGD behavior are new.

## Mathematical value (PASS)

Minimum-loss screening is a directly motivated robust optimization rule, and the screening workload is a real design parameter. The complete logarithmic-batch law proves a nonmonotone reliability phenomenon: a nonempty middle interval gives eventual almost-sure recovery, a smaller rate causes infinitely many corrupted steps although the error probability vanishes, and a larger rate can permanently trap a run at the corrupted target. The two thresholds identify a precise design boundary unavailable from fixed-batch expected-error bounds. The model is minimal but natural and fully classified. No general convex-loss, finite-data or step-size extension is claimed.

## Closest literature and limitations

- Shah, Wu and Sanghavi, *Choosing the Sample with Lowest Loss Makes SGD Robust* (2020), https://arxiv.org/abs/2001.03316. **Closest shared algorithm and scalar outlier landscape; fixed screening size and static trapping already prior art.**
- Haddock, Ma and Rebrova, *Quantile-based Loss Filtering for Outlier-Robust Stochastic Gradient Descent* (2026), https://arxiv.org/abs/2609.13040. **Fixed screening size, finite index sets sampled without replacement; does not state the fresh-stream time-dependent almost-sure classification in the relevant sections inspected.**
- Battaglia et al., *Quantile Randomized Kaczmarz for Streaming Linear Systems with Massart Noise* (2026), https://arxiv.org/abs/2608.27968. **Fresh-sample streaming and logarithmic finite-horizon screening, but a different quantile update and type of guarantee.**
- General results for time-inhomogeneous two-state Markov chains may cover the probability-theoretic sublemmas. Incompletely indexed or inaccessible historical studies could contain the same sharp specialization.

The proof assumes two point-mass targets, equal quadratic curvature, exact unit gradient step, majority-clean independent fresh batches and deterministic screening sizes. Reproducible finite checks do not establish the infinite assertions. Independent mathematical validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
