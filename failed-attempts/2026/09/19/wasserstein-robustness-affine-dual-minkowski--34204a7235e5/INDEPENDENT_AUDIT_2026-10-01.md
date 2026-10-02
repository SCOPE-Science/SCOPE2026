# Independent mathematical audit — 2026-10-01

## Final claim assessed

Assuming the Zhang--Jin solvability criterion that admissible normalized measures are exactly those not supported in a closed hemisphere, the exact Wasserstein-p distance to nonsolvability is the minimum L to the power p point-to-hemisphere distance; nearest-point projection attains it, the margin is convex-region depth with the stated concavity/Lipschitz properties, and the moment-body and Wasserstein-infinity inradius formulas follow.

## Correctness — PASS

Conditional on the cited Zhang--Jin hemisphere criterion, the transport geometry is correct. For a fixed closed hemisphere H, every coupling to a measure supported in H costs at least the point-to-H distance and a measurable nearest-point projection attains equality; minimizing over hemisphere directions gives distance to the union. The concavity of Delta_p to the power p is the infimum of linear functionals, closedness gives the 1-Lipschitz distance-to-bad-set property, and x<=arcsin x<=(pi/2)x yields the moment-body comparison. An independent three-point circle calculation agrees with the fixed-hemisphere L2 formula. The primary preprint full text could not be retrieved; only its abstract confirming a necessary-and-sufficient criterion was accessible, so the exact attribution of the hemisphere wording remains an access risk rather than contrary evidence.

## Originality — FAIL

The record’s main theorem is mechanically implied by the cited qualitative existence criterion together with the standard optimal-transport fact that distance to measures supported on a fixed closed set is the L to the power p norm of point-to-set distance. Taking the union over hemispheres gives the exact robustness radius; the remaining concavity, projection, support-function, arcsine, and Wasserstein-infinity statements are elementary consequences of that same representation. Under the required implication standard, absence of the exact phrase in prior literature does not establish originality.

## Value — FAIL

Quantitative robustness is a natural motivation, but the final package does not require a new nonstandard lemma once the qualitative hemisphere criterion and standard Wasserstein projection identity are known. The moment-body comparisons are elementary one-line bounds. Under the value bar this is a routine reformulation of existing structure, not a separate mathematical gap.

## Source inspections and risks

- **Affine dual Minkowski problem for general measures** (arXiv:2609.20003): Primary arXiv abstract and metadata were read; arXiv full text and an OA full-text route were unavailable, and the authorized Oxford retrieval returned an unavailable/invalid error. Assessment: PRIMARY_ACCESS_RISK.
- **A user’s guide to optimal transport** (Ambrosio--Gigli, CIME notes): Indexed full-text contents/background; only the generic fixed-closed-set distance fact is used, not a claimed specialized theorem. Assessment: STANDARD_BACKGROUND.

Residual risks: The exact full-text statement of Zhang--Jin Theorem 1.5 was not independently read because all lawful retrieval routes attempted in this run failed; the scientific rejection does not rely on a claim that the paper lacks the robustness formulas, but on mechanical implication from the criterion as quoted in the audited package.; No claim is made that Cai--Leng--Wu--Xi lacks an equivalent robustness statement because its full text was not inspected.
