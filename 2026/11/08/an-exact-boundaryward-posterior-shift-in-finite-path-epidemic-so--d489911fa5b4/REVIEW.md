# Self-review

## Correctness — PASS

The statement quantifies over every finite path with \(n\ge4\), each infected prefix length \(3\le k<n\), every common rate \(\lambda>0\), every positive observation age, and every positive source prior for the posterior-order portion. The uniform-prior staircase has exactly \(\lfloor(k-1)/2\rfloor\) ordered MAP changes. Independence of left and right infection fronts establishes the exact fixed-age likelihood, including saturation at the physical left endpoint and the necessary failure to cross the right observed boundary. The strict age derivative is a negative positive-variance quantity, not a finite-difference inference; the strict spatial log-concavity follows from the increasing Poisson upper-tail hazard. Limits show every claimed threshold is unique and all equality cases are covered. A direct independent finite-CTMC uniformization checks the formula and transition behavior in `verify.py` (4137 checks); it is corroboration, not a substitute for proof.

## Originality — PASS, provisional historical priority

The earliest motivating public preprint is Shah and Zaman (September 24, 2009, arXiv:0909.4370); their model supplies independent Poisson fronts on a line, but their displayed rumor-center inference does not imply the present known-age finite-boundary posterior order or its MAP staircase. Shah and Zaman (arXiv:1110.6230) explicitly analyze unknown-age snapshots. Antulov-Fantulin et al. (arXiv:1304.0018, March 2013) permit observation-age-conditioned source estimation, but approximate likelihoods via simulation. Kazemitabar and Amini (arXiv:1906.03052, 2019) give a more general exact event-order likelihood, but its event is *ever reaching an infected set before leaving it* and is time-independent, hence does not imply the present exact-age result. Shi, Zhang and Chu (2022) use discrete-time SIR simulations for observation-time effects, not this theorem. Relevant indexed-source and equivalence searches were compared by implications, and no inspected source contained a dominating analytical statement. The main residual risk is an unindexed or uninspected prior derivation of this simple-geometry special case; historical novelty is not independently certified.

## Value — PASS

A fixed snapshot containing an epidemic path prefix is a natural patient-zero/source-detection observation. The physical end of the contact path and the elapsed outbreak age are inferential information not captured by an unordered infection count. The theorem gives strict posterior shift under *every positive prior* and an exact, complete sequence of \(\lfloor(k-1)/2\rfloor\) MAP changes under a uniform prior, with a root equation for each age threshold and an explicit small/large-age interpretation. This exact structural classification, not merely a finite test, is useful as a benchmark for source inference and for identifying when rumor-centrality intuition can fail. It does not justify claims for SIR recovery, unknown age, general graphs, or real-world public-health deployment.

## Evidence and limitations

The public proof, reproducible verifier, inspected source comparisons, distinct observation definitions, and residual risks appear in `RESULT.md`, `verify.py` and `AUDIT.json`. No independent mathematical or priority audit has occurred; finite diagnostics are not universal proofs.

Self-review: passed. Independent audit: not yet performed.
