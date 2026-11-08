# Scientific review: biased Hata-map excursion and residence laws

## Correctness — PASS

The primary statement fixes the independent map-selection probabilities, the uniform initial distribution on the disfavored half, and the exact definitions of the return count and occupation time. A dyadic cell is sent affinely either onto one dyadic cell or onto the whole opposite half; conditioning on the latter gives the geometric landing index. This establishes a genuine Markov reduction, not a heuristic renewal model. The gambler's-ruin equation gives the return probability \(\theta=(1-\delta)/(1+3\delta)\). The one-level hitting-time equation \(g=z(P+Qg^2)\) and the right-boundary renewal equation yield the displayed generating function. Its derivative at one gives the occupation mean, while expansion at \(z=e^{-s\delta^2}\) and the Laplace continuity theorem give the limiting law. The probability of endless cross-half renewal is zero off criticality, and the strong law gives the endpoint contraction exponent. The reflected-parameter case follows from the identity interchanging the two maps under \(x\mapsto1-x\).

The program `verify.py` ran successfully, with 95 exact, symbolic, and finite random-sample checks. These are supporting diagnostics, not a proof of infinitely many-time statements. The proof covers all \(0<p<1\) except \(p=1/2\), and all \(s\ge0\) in the Laplace limit, under the stated initial-law assumptions. No conclusion about an individual deterministic initial point is asserted.

## Originality — PASS within inspected evidence

Hata–Yano, arXiv:2108.01332v1, Eq. (1.10), Theorem 1.1 and Section 3, supplies the map and the symmetric-choice recurrent partition. Its assertions concern \(p=1/2\) and distributional arcsine and Darling–Kac laws. The present result treats the offcritical coin bias and identifies finite total returns, a complete algebraic residence-time law, two different scaling laws, and the bias-dependent almost-sure endpoint selection. The existing symmetric-case theorem cannot imply these formulas by setting a parameter or applying a reflection alone. The case of geometric deformation of the maps with **equal** choices in Nakamura–Nakano–Toyokawa–Yano, arXiv:2206.00226v1, is different from changing the selection probabilities here. The Pelikan doubling/halving model in arXiv:2308.09269v1 has different branch transitions and does not directly encompass the two-half Hata renewal law. Semantic mathematical-record queries for Hata, bias, return counts, near-critical crossover and occupation-time transforms did not retrieve an equivalent statement; nearby records concern different maps and mechanisms.

Residual risks: The cited 2019 Kyoto University master's thesis by Hata was not available in full; a previously worked out offcritical renewal calculation might exist there or in unindexed work. Abstract general renewal theorems may simplify the derivation but do not, without a map-specific reduction, directly contain the coefficients and limiting transform. Novelty has not undergone independent expert assessment.

## Mathematical value — PASS

The Hata map is an established canonical example of random intermittency with two competing endpoint effects. The relevant, naturally defined observables—the total number of visits to the unfavored half and the total time spent there—are finite only offcriticality. Their exact distributions and quantitative singularity as equal selection is approached distinguish the excursion-count scale \(\delta^{-1}\) from the residence-time scale \(\delta^{-2}\), and the nonexponential limit for residence time shows why counting excursions alone is insufficient. This supplies the missing quantitative offcritical side of the published critical arcsine description; it is not a normalization check, arbitrary finite table, or textbook formula without a dynamical motivation.

The initial-uniformity condition is essential to the exact Markov renewal law. The theorem does not address quenched laws or complete finite-horizon process convergence. Both are genuine limitations, not claims proved here.

Self-review: passed. Independent audit: not yet performed.
