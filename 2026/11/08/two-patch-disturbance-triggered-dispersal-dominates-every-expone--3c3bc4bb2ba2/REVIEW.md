# Scientific review

## Correctness — PASS

The claim is precisely scoped to two patches, positive habitat and demographic rates, an initially singly occupied landscape, and a nominal dispersal-rate matching \(c=bq\) with \(0<q\le1\). The two transient Markov generators follow from independent habitat restoration, destruction, local demographic extinction and the two alternative colonization mechanisms. The resolvent difference factors as a strictly positive rational function for every discount \(z\ge0\). Both denominator determinants are positive because the corresponding finite continuous-time chains are transient. In the explicit positive-restoration parameter example, a rational uniformization partial sum is strictly below \(-90\), whereas the entire omitted absolute tail is below \(1/1000\). That proves fixed-time survival reversal without relying on floating-point calculations. The separately reconstructed full five-state model and the symbolic identity replay successfully with `CHECK.py`.

## Originality — PASS within inspected evidence; priority provisional

The closest source is Reigada et al. (2015), which defines the three-state dynamic-habitat framework and compares pulse and continuous dispersal under fixed nominal colonization rate. Its inspected main text treats a mean-field/branching regime and larger finite-landscape simulations, not a strict, all-discount two-patch resolvent factorization accompanied by a positive-restoration fixed-time counterexample. Hill and Caswell (2001) analyze finite-patch chain-binomial extinction times, but do not analyze the same continuous-time destruction-triggered pulse mechanism in the available material. The open 2010 Kang–Lanchier preprint has a two-patch Allee-effect system with density-based invasion rather than this habitat-suitability chain. Querying the mathematical findings database for pulse timing, two patches, exponential deadlines, and resolvent ordering produced no statement covering the claim. Neither absent hits nor partition boundaries constitute a proof of priority. The 2015 supplementary appendices and inaccessible historical literature are residual risks.

## Value — PASS

The primary ecological source explicitly finds that timing of propagule release matters even at matched average rates and that finite-landscape persistence differs from deterministic/mean-field predictions. The exact result isolates a natural minimal habitat network and establishes a structural boundary: a strict advantage for every exponentially randomized deadline and mean persistence does **not** imply superior survival at every fixed deadline. The certified sign reversal prevents a potentially misleading extension of the correct average-persistence result and separates two scientifically distinct management objectives. This is not a recommendation to prefer pulsed dispersal in an arbitrary ecosystem.

## Evidence and remaining limits

The analytical proof gives the all-parameter sign. `CHECK.py` verifies it symbolically, checks full labelled versus lumped generators, and proves the rational finite-deadline counterexample with an explicit convergent tail bound. Both the all-discount result and the failure of deterministic-time domination are confined to the stated finite-state Markov model. Historical priority has not been independently certified; source relevance is assessed from actual inspected primary material and bounded searches, with supplementary materials not fully inspected.

Self-review: passed. Independent audit: not yet performed.
