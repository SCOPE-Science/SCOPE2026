# Self-review

## Correctness — PASS

The construction specifies all edges, the common vertex count, identical marked radius neighborhoods including their boundary ambient degrees, and the matched endpoint resistance. The marked-excursion identity is reconstructed using independent Poisson departure streams, the return-time identity, Wald's stopped-sum formula, and terminal-suffix compensation. The clique half-success bound is proved through complete-graph return excursions and a controlled killing hazard; this supplies an explicit negative inequality. The path case reduces to a rational expression with a positive shifted polynomial. The standalone checker independently tests exact finite recurrences and key integer identities. These tests are supporting checks, not substitutes for the quantified proof.

## Originality — PASS (historical priority provisional)

Si (2026, arXiv:2608.27474, Theorem 1.1 and Section 7) explicitly proves arbitrary-radius sign separation only with different graph orders and poses the equal-order strengthening as open. The present equal-order construction is not a corollary of that theorem; it needs a new matched-order family and signs of both responses. Si's general marked-excursion formula is a credited ingredient. Barlow–Ding–Nachmias–Peres (2011) concern broader factor comparisons, and Ding–Lee–Peres (2012) establish coarse universal cover-time comparisons. Published-result semantic searches did not produce a statement implying equal-order arbitrarily large radius separation. Residual risk: a different locality convention or overlooked exact cover-time paper could contain an equivalent result.

## Mathematical value — PASS

A specifically stated open structural boundary of the 2026 motivating paper is resolved: the **global order of a graph** cannot restore local predictability of the sign of its single-edge cover-time response. The construction works for every prescribed radius and preserves several additional natural scalar invariants. It illustrates how slow path discovery and a rapidly covered but edge-rich clique contribute competing terms to expected cover time.

## Closest sources and limitations

Si's full preprint, https://arxiv.org/abs/2608.27474, Sections 3 and 7; Barlow et al., https://doi.org/10.1017/S0963548310000489; Ding et al., https://doi.org/10.4007/annals.2012.175.3.8. The theorem is fixed-start, not worst-start; it does not match total edge count or remote degree sequence, and the order bound is not claimed optimal. Independent verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
