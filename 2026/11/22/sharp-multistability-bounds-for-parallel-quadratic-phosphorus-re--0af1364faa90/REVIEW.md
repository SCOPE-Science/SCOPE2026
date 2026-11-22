# Scientific review: parallel quadratic phosphorus recycling

## Correctness — PASS

For each \(m\geq0\), multiplying the scalar vector field by the positive denominator \(\prod_j(K_j^2+P^2)\) produces a degree-\(2m+1\) polynomial with nonzero leading coefficient \(-a\). Thus the upper bound counts all positive roots, including multiplicities. Interlacing of attractors with other fixed points bounds the number of attracting equilibria. The constructive induction adds a channel of strength \(3K\) and saturation scale \(K\): old witness signs persist at finite fixed concentrations as \(K\) grows, while the new signs at \(K\) and \(4K\) are respectively positive and negative. This forces the maximal number of simple roots for every channel count. Exact rational two-channel signs and a finite-induction replay passed 58 assertions in `verify.py`. The computer checks are ancillary, not an infinite certification.

## Originality — PASS on inspected literature, with residual risk

Zeng et al. (2017, DOI 10.1002/ecs2.1805) give the conventional one-feedback lake-phosphorus Hill model and bistability; Zhao et al. (first online 2024-10-02, DOI 10.1007/s10750-024-05701-4) document distinct internal-P loading mechanisms rather than deriving a sharp equilibrium count. Feliu and Wiuf (2015, DOI 10.1186/s12918-015-0164-0) present feedback-loop criteria in multistationary networks; those do not establish this specific all-\(m\) sharp scalar bound and construction. Two-sigmoid phosphorus models are already known to exhibit five roots, so the bare five-root phenomenon is NOT asserted original. The claim is the general sharp \(2m+1\) count and the inductive attainment for all positive *quadratic Hill* recycling contributions using only one dynamic variable. Duncan et al. (2021, DOI 10.1137/21M1398331, arXiv:2103.17184) was examined in its full preprint, including the switching-limit hypotheses and Theorem 3.13; that theory does not directly provide the exact finite-parameter bound and all-\(m\) construction here. Historical priority remains uncertain for other related sigmoid-sum inequalities. No inspected result directly states or implies this exact theorem.

## Value — PASS

The all-\(m\) theorem distinguishes having \(m\) separately saturating instantaneous phosphorus feedback terms from conventional single-feedback bistability. It proves that the number of stable nutrient regimes can grow linearly without introducing additional dynamic state variables and gives a sharp upper bound for each chosen model complexity. This is an informative structural boundary for reduced lake models and a concrete rational three-attractor illustration, not a claim about observed regime counts, model adequacy, or an ecological intervention.

## Limits and research integrity

All parameters in the construction are positive but not field calibrated. The result uses autonomous deterministic one-state dynamics with instantaneous quadratic saturation. Stochastic, delay, spatial and explicit sediment-state models are outside the proof. Literature inspection cannot exclude every historically equivalent theorem. No independent expert audit or external mathematical certification is claimed.

Self-review: passed. Independent audit: not yet performed.
