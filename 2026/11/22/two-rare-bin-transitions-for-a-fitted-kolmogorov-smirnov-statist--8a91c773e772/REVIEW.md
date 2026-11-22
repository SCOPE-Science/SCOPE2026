# Research review

**Claim.** Increasing deterministic logarithmic bin widths for iid Pareto data cause two fitted-KS null transitions: a second-bin Gaussian/Poisson threshold at \(nq_n^2\asymp1\), and a first-bin degeneracy/Poisson-squared threshold at \(nq_n\asymp1\), including a discrete refitted bootstrap limit.

## Correctness (C): PASS

The bin index has geometric survival \(q^j\) and exact likelihood estimate \(S/(n+S)\). Expansion about its population value cancels first-bin fluctuations against those in the fit, leaving \(N_2-nq^2\), with remainder \(O_{\Pr}(\sqrt{nq^3}+q)\) on the count scale when \(nq\to\infty\). Binomial triangular-array central and Poisson limits then prove the first three regimes. At the sparse first-bin boundary the event that no index exceeds one has probability tending to one, and the exact identity \(D=A^2/[n(n+A)]\) gives the Poisson-square limit and the monotone bootstrap-tail formula. Critical edge cases are explicit, including nonexistence of a finite parameter estimate when all indices vanish. The standard-library exact checker passed 1,890 rational finite identities and seeded simulation diagnostics; simulation alone is not used as proof.

## Originality (O): PASS, with residual historical-priority risk

Lin–Newberry arXiv:2301.05690v1 and the journal article *Seeing through noise in power laws* supply the logarithmic Pareto binning likelihood, fitted KS statistic and re-estimating bootstrap. The journal article does discuss increasing binning ratios with sample size, so the distinction is **not** novelty of growing binning or goodness-of-fit. The distinction is the four explicitly normalized null regimes and the exact discrete ideal-bootstrap limit obtained from second-bin cancellation and the next first-bin transition. Virkar–Clauset arXiv:1208.3524 supplies binned-power-law fitting and model checking but not these moving-bin-ratio limit laws. Newberry–Savage 2019 supplies the discrete logarithmic model; no directly equivalent limit theorem was located. Relevant classical plug-in empirical-process and rare-event results can be used to derive component steps, but do not, in the inspected material, already state the joint fitted-statistic classification. Literature searches and mathematical record searches found no direct covering result, which is not a uniqueness proof. The full Newberry–Savage and Kulinskaya publisher texts could not be completely inspected and may contain related results.

## Value (V): PASS

The statistic is used to calibrate whether coarsely binned data resemble a power law. Estimating the tail rate from the same data cancels the dominant first-bin fluctuation, changing the effective rare-event threshold from \(nq\) to \(nq^2\). This creates a meaningful intermediate limit and a second boundary where finite-parameter inference fails with positive probability and ideal bootstrap probabilities cease to have a continuous null law. These exact scales quantify a practical inferential limitation of an existing procedure, rather than merely restating loss of Fisher information.

## Sources and limitations

Primary: Lin and Newberry, arXiv:2301.05690v1, 13 January 2023, https://arxiv.org/abs/2301.05690; Newberry and Lin, *Seeing through noise in power laws*, https://pmc.ncbi.nlm.nih.gov/articles/PMC10465205/; Virkar and Clauset, arXiv:1208.3524, https://arxiv.org/abs/1208.3524. Secondary historical risks: https://doi.org/10.1103/PhysRevLett.122.158303 and https://doi.org/10.1080/10485259508832633.

No result is proved about an estimated threshold, a noisy measurement model, adaptive bin selection, or the frequentist size of a finite-simulation bootstrap test. A finite exponent does not exist on the all-zero-index event; extended boundary fitting is essential. Independent historical-priority and mathematical reviews remain outstanding.

Self-review: passed. Independent audit: not yet performed.
