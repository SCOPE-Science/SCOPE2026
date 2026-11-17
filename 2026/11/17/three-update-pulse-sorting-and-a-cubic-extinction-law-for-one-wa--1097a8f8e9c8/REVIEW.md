# Scientific review

## Correctness — PASS

The local update equations give \(F^2_i=2a_i+m_i\) and \(F^3_i=2m_i+m_{i+1}\), where the markers are separated by at least three sites. The recurrent image and one-site translation follow algebraically. The three-state suffix machine counts the marker number in every cyclic input, and its matrix characteristic polynomial gives the exact extinction formula. Sharp witnesses cover every ring length, and Möbius inversion supplies the primitive-orbit counts. Two standalone integer-only implementations have been executed: one verifies all 243 local windows and complete initial-state spaces through length ten, and the other enumerates all states through length twelve. These runs agree with the formulas. Finite runs are not used as an infinite proof.

## Originality — PASS, qualified

Fisch, Gravner and Griffeath (1993) define the classical excitation model, not this exact oriented-ring law. Fisch and Gravner (1995) treat symmetric line neighborhoods, including periodic-boundary numerics; their one-dimensional theorems do not imply the one-neighbor directed formula. Gravner, Lyu and Sivakoff (2016) treat simple undirected graphs; their comparison and graph covering results do not give the one-way factorization or extinction polynomial. Existing mathematical record searches were compared at the level of their mathematical assumptions and conclusions, not just titles. The earlier Greenberg–Greene–Hastings article could be inspected only at abstract level. Unindexed or unpublished equivalent priority remains a residual risk, and priority is not claimed as absolute.

## Value — PASS

A ring of unidirectionally coupled excitable elements is a canonical feed-forward periodic network. The theorem identifies a uniform sharp time at which all interactions reduce to a rigid shift, a complete initial-state pulse-number distribution, a closed extinction formula, and primitive-period counts. The simultaneous coexistence of a constant-time sorting bound and an exponentially small extinction basin is structurally informative, rather than an isolated finite-state count. No result is asserted for undirected or branched networks.

Self-review: passed. Independent audit: not yet performed.
