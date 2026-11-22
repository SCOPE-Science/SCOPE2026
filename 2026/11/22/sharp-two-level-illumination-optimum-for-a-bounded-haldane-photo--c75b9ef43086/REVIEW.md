# Self-review

## Correctness — PASS

The normalized model is exactly the steady-state Haldane photosynthesis law from the cited primary study after a positive linear irradiance scaling. The derivative, single positive curvature change, tangency quadratic, radical, and contact-set inequality are algebraically derived. The exact slack factorization proves that the piecewise function is the least concave majorant and Jensen's inequality proves the upper bound over *every* probability law. The equality set and the mean constraint prove uniqueness including boundary means. The exact algebraic reduction and 11,188 standard-library test assertions were reproduced with the embedded code. Numerical sampling is not used to justify generality. Residual scientific risk: any deviation from the assumed steady-state response, light cap or mean constraint changes the optimization problem.

## Originality — PASS on inspected literature

The primary full text of Fierro Ulloa–Lu–Bernard, in particular its Haldane equation (4), Lemma 3, and Theorems 1–3, was compared by hypotheses and implications, not title matching. The prior inflection and time-share limit are expressly credited. Theorem 3 optimizes a *difference* under a fixed pair of irradiances both above the inflection; it does not fix a total photon budget while optimizing all intensity distributions. The new low setpoint necessarily lies below that inflection, so it is not covered by the prior specified parameter class. Bernard–Lu optimize Beer–Lambert optical depth and biomass rather than all light laws with a given first moment. General concave-envelope methodology is established; the exact Haldane-specific unique optimizer, radical contact threshold, and sharp loss formula were not found in the inspected statements. The closest abstract-only flashing-light work concerns kinetic flashing and is not treated as full-text evidence. Residual risk: uninspected broader optimization literature might contain or imply the same formula; no independent historical-priority audit has occurred.

## Value — PASS

This is a natural complete optimization classification for a scientifically motivated photoinhibitory response and physical mean/cap illumination constraints. It identifies when constant light is provably optimal, when an entirely different two-level policy is optimal, and the uniquely determined duty fractions; a closed algebraic deficit tells precisely how far any other schedule lies below the idealization. It improves on a local improvement test or a fixed-two-intensity duty-cycle optimum. Practical value is limited to slow, equilibrated illumination and idealized photon budgeting; no experimental productivity gain is claimed.

## Relationship to closest literature and limits

Primary: Fierro Ulloa, Lu and Bernard (2023), DOI 10.1007/s00285-023-01871-2, full text inspected in Sections 2–5. Supporting: Bernard and Lu (2022 preprint), full text inspected in Sections 2–3. The 2023 ACS flashing-light paper was considered at abstract level only and cannot establish full-document absence. General convexification/concavification frameworks are background. The result is not a dynamic Han-control theorem and is not calibrated to a field strain.

Self-review: passed. Independent audit: not yet performed.
