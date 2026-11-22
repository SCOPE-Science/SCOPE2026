# Scientific review: sharp Erlang binary-census information

## Correctness — PASS
For every integer stage number \(k\ge1\), the two Poisson count likelihood gives a diagonal two-parameter information matrix with rate entry \(\theta J_k\). Conditional gamma means make its derivative sign exactly the difference of right and left mean residual lives. Log-concavity of the Erlang CDF and survival function, established directly from the density, gives strict single crossing and global uniqueness. The nearest-centroid argument extends the optimum to all measurable binary partitions, up to relabeling. A bounded-cutoff Laplace/Edgeworth expansion coupled to unique-root bracketing proves the finite absolute offset \(2/[3(\pi-2)]\) and the first relative information correction. High-precision numerical diagnostics check the arithmetic, not the infinite proof.

## Originality — PASS relative to inspected prior work
The stage-progression probability model is pre-existing (Wearing, Rohani and Keeling, 2005). The minimum-squared-error centroid principle is pre-existing (Lloyd), and broad Fisher-optimal scalar quantization is pre-existing (Cabral Farias and Brossier, 2013). Gao et al. (2015) address Gaussian scale-change detection under binary noisy transmission. The claim here is limited to the exact family of Erlang progression two-count cutoffs with jointly unknown Poisson cohort intensity and progression rate, including the fixed **absolute** high-stage threshold offset and the sharp first correction to the retained fraction of Fisher information. Targeted full-text and title/abstract searches did not locate these specific constants or the complete all-stage classification in the inspected sources. An older or broader quantization theorem might imply more of this family than the searches revealed, and historical priority requires independent expert verification.

## Value — PASS
Multi-stage exponential progression is a standard way to replace memoryless residence times in epidemiological and biological models. If a cohort can be observed only once as completed versus pending, the theorem gives the exact locally best follow-up interval, quantifies the information sacrificed relative to individual event-time tracking, and proves that even large numbers of stages retain a nontrivial limiting fraction \(2/\pi\). The absolute stage-offset correction is important because the leading follow-up time \(k/\lambda\) alone is insensitive to where to place the binary census at fixed stage mean. This is a model benchmark, not a practical infection-control recommendation.

## Closest literature and limitations
- Wearing et al. (2005), https://pmc.ncbi.nlm.nih.gov/articles/PMC1181873/ : Erlang-type infectious-period modeling, not a binary follow-up information design.
- Cabral Farias and Brossier (2013), https://arxiv.org/abs/1310.6945 : generic high-resolution Fisher quantization for other distribution families, not fixed one-bit Erlang-stage asymptotics.
- Gao et al. (2015), https://www.mdpi.com/1999-4893/8/3/621 : one-bit Gaussian scale-change testing, distinct family and objective.
- Lloyd (1982 printed), https://doi.org/10.1109/TIT.1982.1056489 : already supplies the quadratic centroid method; no claim of originating it.

Rate misspecification, unknown stage number, nonsynchronous entry, measurement errors, informative loss to follow-up and cost are not analyzed. Independent scientific validation has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
