# Self-review

## Correctness — PASS
The feedback coordinate rule is exactly a rotation after one local majority update. Under the cyclic disagreement count, a visit flips a bit only when isolated, removing two disagreeing edges and never creating new isolated sites. Every site is visited once in the first \(n\) clocks. This proves recurrence and the sharp time bound. The last-entry formula is reconstructed by counting interiors with prescribed endpoint bits and a rightmost equal pair of type \(11\). The transfer matrix and Möbius count supply an independent enumeration of rotating periodic words. All finite verification checks passed. Boundary \(n=3\) is handled explicitly; the number of circular positions is preserved by the rotating conjugacy. Finite checks do not prove the formulas for arbitrarily large \(n\); the proofs do.

## Originality — PASS, qualified
Tošić–Agha (2004) prove the stable no-singleton pattern and no nontrivial cycles in standard sequential configurations. Those results explain the eligible target words but not the *number of initial words first entering them on the final clock* in a rotating feedback register. Tošić (2009/2010) treats general complexity, and Benjamini and collaborators treat parallel graph majority. Neither implies the explicit \(E_n\) without analyzing the descending sweep and its initial-bit constraints. Earlier stable-word counts, including an accessible prior numerical coincidence with Lucas-type formulas, are not asserted as new. Relevant exact-population aliases and indexed results were searched. The 2004 sequential-interleavings companion text was not inspected in full, so historical priority remains a qualified assessment.

## Mathematical value — PASS
The settling-time tail is a natural finite-time observable for a minimal nonlinear feedback register. The exact last-clock population shows the worst-case linear settling bound is attained by a positive limiting fraction \(1/12\) under uniform initial conditions, distinguishing a typical final-clock phenomenon from rare worst cases. This is a structural dynamical statement beyond the known enumeration of stable words. Earlier exact entrance-time strata and basin-by-orbit frequencies remain open.

## Supporting sources and residual risk
Primary sources: Tošić and Agha, ACRI 2004, especially Lemmas 3–4; Tošić, DMTCS Proceedings AL (published 2009-12-31), introduction and counting-complexity statements; Benjamini et al., arXiv:1405.2486 (2014), model comparison. Searches included majority-feedback/shift-register aliases and indexed finding records. Inaccessible or unindexed sequential-update and specialized register literature could change the originality assessment. The independent audit status is unperformed.

Self-review: passed. Independent audit: not yet performed.
