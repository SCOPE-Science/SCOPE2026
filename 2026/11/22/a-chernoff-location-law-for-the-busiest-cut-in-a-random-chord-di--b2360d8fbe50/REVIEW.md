# Review of the busiest-cut Chernoff limit

## Correctness

PASS. The full new statement is the joint limit of the centered maximum location and excess height. The proof derives the exact exposure transition probability from uniform matching symmetry and the exact parabolic mean, verifies a bounded-jump martingale functional CLT locally with conditional quadratic variation tending to elapsed time, and proves the indispensable unrestricted-argmax localization using dyadic martingale maximum bounds and Azuma concentration. The explicit scalings \(n^{2/3}\), \(n^{1/3}\), Brownian diffusion one, and parabolic coefficient one-half were independently reconstructed. The standard-library enumeration passed 195 exact assertions through twelve endpoints; finite testing is not used as infinite proof.

## Originality

PASS, with historical-priority qualification. The nearest published research record on the *same open-chord path* supplies the complete finite second moments and a fixed-scale Gaussian bridge, but neither the random optimizing position nor the finer local parabolic/Brownian limit. Acan's chord-diagram preprint establishes the model and studies degree/core and growth questions, not this argmax. Groeneboom–Lalley–Temme establish the distribution of the Brownian limit, not the matching-process convergence to it. Daniels–Skyrme and Kim–Pollard supply broad maximum-process and cube-root frameworks; they may reduce conceptual distance but are not located model-specific matching-cut results. The literature searches cannot conclusively exclude all older or alternatively named matching applications. General-purpose maximum-process results are an acknowledged priority risk rather than treated as absent.

## Value

PASS. The position of a maximum cut in the natural endpoint order is a motivated geometric/algorithmic statistic of a random chord matching. The global Gaussian bridge has order-\(\sqrt n\) fluctuations and is insufficient by itself to describe where the largest cut occurs; the new theorem discovers a genuinely different \(n^{2/3}\) displacement and \(n^{1/3}\) excess scale and determines their joint non-Gaussian distribution. It makes a sharp probabilistic prediction about the busiest point in the scan, not a renaming of the classical Chernoff law.

## Closest literature and limitations

Acan, arXiv:1501.01489v1, Section 2 on single-chord degrees and Section 6 on growth; *Exact crossing-cut Green kernel and Gaussian bridge for uniform pairings*, 2026-10-18 published research record, full theorem/proof inspected; Groeneboom–Lalley–Temme, arXiv:1305.6053, on the Brownian-parabola maximizer. Daniels–Skyrme (1985) and Kim–Pollard (1990) are generic maxima frameworks; the full Daniels–Skyrme text was not obtained, so model-specific antecedents in that literature remain a priority limitation. Neither finite experiments nor a failed search is cited as uniqueness proof. The claim is restricted to uniform matching in the supplied order, without rates or moment convergence.

Self-review: passed. Independent audit: not yet performed.
