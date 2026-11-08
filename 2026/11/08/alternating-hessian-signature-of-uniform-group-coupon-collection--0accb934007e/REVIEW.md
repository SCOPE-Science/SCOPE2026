# Self-review

**Reviewed claim:** Alternating Hessian signature of uniform group coupon collection, with all \(n\ge3\), \(1\le s<n\) and exact harmonic eigenvalues.

## Correctness — PASS
The Hessian is the second derivative of an exact missing-coupon inclusion-exclusion expression. All denominators are strictly positive near the uniform interior law. The Johnson decomposition uses a proved up/down commutator and norm recursion; the parity signs follow from strictly positive finite differences. The standalone exact-rational checker tests both mathematical routes and actual perturbed expected times. Finite tests do not stand in for the infinite-parameter proof.

## Originality — PASS (provisional historical priority)
The 2025 first-public Berend–Sher preprint, arXiv:2509.17201, proves Schilling’s global nonoptimality conjecture by constructing better package distributions; it explicitly says the previous Hessian method worked in some special cases. That global theorem does not force the uniform point to be a local saddle, nor determine the entire signed spectrum. The companion arXiv:2605.06953 treats uniform expected-time asymptotics, not the nonuniform local Hessian. Gottlieb’s incidence-matrix theorem supplies standard algebra but not these signed coupon functional weights. Targeted scientific-literature searches and implication comparisons found no covering formula. The 2021 Schilling paper could not be read in full, so priority relative to any additional unpublished or unindexed extensions remains a concrete risk. No full-text noncoverage assertion is made for inaccessible sources.

## Mathematical value — PASS
The theorem completes the natural local-geometry version of a central optimization question in group coupon collection: it proves *arbitrarily small* improvement is possible at every nontrivial package size and exactly classifies all curvature directions. It sharpens global nonoptimality by a nondegenerate strict-saddle statement and gives explicit multiplicities for stability analysis. It does not identify global minimizers.

## Verification and limitations
Run `python3 verify.py` from the extracted package. The exact-rational check is supplementary to the analytical proof. The original 2021 Schilling article was not accessible for direct full-text examination; its credited special cases are not claimed as new. The paper does not assess a nonuniform law’s distant curvature or the global optimization landscape.

Self-review: passed. Independent audit: not yet performed.
