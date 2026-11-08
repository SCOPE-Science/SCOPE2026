# Scientific review: Universal distance-scaled first-passage law for fluctuating jump rates

## Correctness — PASS

The proof uses a unit-rate spatial walk, an independent integrated jump-rate clock and a two-parameter Laplace scaling limit. The hitting-time functional is handled through convergence of independent scalar hitting time and operational clock at every fixed time, not through unproved inversion of a discontinuous stable path. The Gaussian representation of Brownian first passage and the Laplace integral for negative stable moments give the exact fractional-moment formula. The discrete heat-kernel reflection bound and gamma integral yield uniform subcritical moment integrability. A standalone checker verifies special-function identities and finite-distance spectral quadratures in 37 deterministic tests. Numerical finite-size comparisons do not replace the proof.

## Originality — PASS, qualified

Levit and Reuveni, arxiv:2609.26925v1, already establish the exact finite-distance spectral survival formula, the fixed-distance power tail and threshold, and for the Mittag--Leffler rate the large-start *mean* when the first moment is finite. The present limit recovers that mean coefficient but additionally identifies a full universal distribution under general Laplace-tail conditions, proves convergence of all subcritical positive moments, and gives their exact values. Arutkin and Reuveni, arxiv:2302.07041, provide the underlying random-rate walk framework; Uchida et al., arxiv:2502.20705, concern finite-mean ergodic diffusivities. Standard inverse-stable time-change theory is prior work and a potential route to general coverage. A broader unindexed theorem could imply parts of the result: a residual publication-priority risk remains. Consult AUDIT.json for four claim-level implication comparisons, source inspections and evidence.

## Value — PASS

The problem is motivated by a current first-passage phase transition: knowing a mean and a fixed-start tail does not identify the law on the physically different large-start scale. The full survival curve determines quantiles; the moment spectrum quantifies rare search durations and makes sense when the mean is infinite. The limit also demonstrates which aspects depend only on the rate-tail index and normalization rather than on the complete rate distribution.

## Limits

Only symmetric nearest-neighbor half-line motion and independent fixed-interval rate refreshes are included. There is no error rate, quenched law, varying-interval limit or independent validation. General inverse-stable-subordination literature was identifiable, but a full global uniqueness survey is impossible.

Self-review: passed. Independent audit: not yet performed.
