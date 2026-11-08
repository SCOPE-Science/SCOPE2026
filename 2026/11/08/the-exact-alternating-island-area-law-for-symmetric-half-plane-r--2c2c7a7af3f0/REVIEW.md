# Self-review

## Correctness — PASS

The theorem is established by the explicit \(2\)-cycle identity, a necessary-and-sufficient half-plane inequality for every iterate, and exact analysis of the resulting unit-normal orbit. Dense irrational rotations yield the disk interior; a finite cyclic unit-normal group yields a regular polygon, with the order \(N=2q/\gcd(2p+q,2q)\). The geometric area and least-period formulas follow from elementary rotation and polygon identities; the positive excess and continuity set follow from \(\tan u>u\) and \(\tan u=u+u^3/3+O(u^5)\). Crucially, the claim is about the **interior** of all strict itinerary constraints, so it does not misclassify potentially surviving boundary points. The analytic steps address all \(0<\alpha<\pi\); finite numerical tests are supplementary only. The supplied checker was executed on all 153 reduced angles with denominators through 31 and 400 additional irrational tests.

## Originality — PASS within examined evidence

The closest primary literature is [1] Cima–Gasull–Mañosa–Mañosas, arXiv:2306.17543, Theorems A and B and Sections 2–3; [2] Goetz–Quas, *Global properties of a family of piecewise isometries* (2009), Section 2; and [3] Cima et al., arXiv:2010.12901, Sections 2–5. These establish general periodic cells, polygon/disk geometric alternatives, and special tessellations for three rational angles. Their conclusions do not explicitly fix the **distinguished alternating orbit's** side count in all three denominator-congruence classes, its exact two-cell area as a function of the angle, or the resulting rational-spike/irrational-continuity dichotomy. The existing general disk/rational-polygon framework and individual triangle/square/hexagon cases are explicitly excluded from the novelty claim. Semantic searches of published mathematical research records and targeted literature queries found no statement covering the complete area law; those searches alone do not prove uniqueness.

The most important residual priority risk is that the area and continuity formula may be derivable from general older half-plane cell theory by a short calculation, or occur in unindexed secondary literature. This work is presented as an exact quantitative derived classification, not as a fundamentally new dynamical mechanism or independent certification.

## Mathematical value — PASS

The object is the maximal regular island around the simplest nontrivial orbit in an established two-atom planar isometry family. Its two-cell area is a natural dynamical-geometric invariant, and a uniform parameter classification is relevant to resonant stability islands and the rational-to-irrational transition. The full \(q\bmod4\) facet law, exact intrinsic periods and dense arithmetic area jumps give motivated structural information beyond the general assertion that islands are polygons or disks. The result does not claim the measure of all regular cells, the whole plane's periodic set, or an exhaustive count of other islands; no general entropy or global classification follows.

## Limitations and sources

The domain excludes degenerate endpoint angles and switching boundaries. The literature comparison covers the accessible full texts of [1]–[3] and semantic index records; no independent priority certification, specialist refereeing, or all-literature survey is claimed. Computational checks supplement, rather than replace, the proof.

[1] https://arxiv.org/abs/2306.17543

[2] https://www.researchgate.net/publication/243031508_Global_properties_of_a_family_of_piecewise_isometries

[3] https://arxiv.org/abs/2010.12901

Self-review: passed. Independent audit: not yet performed.
