# Independent Audit — 2026/09/12/048

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `3f50281732cc50d1e3ea60b0712205d9e73a14c4`
- Disposition: **FAILED**

## Correctness

**PASS** — The counterexample mechanism is correct. The binary deformation proportion differs from its limit by order N^(-1/4), the regular free-convolution edge has a nonzero derivative at alpha=1/2, and therefore the finite-N edge differs from the limiting edge by order N^(-1/4), much larger than the N^(-2/3) edge scale. Centering at the limiting edge consequently creates a diverging N^(2/3) deterministic bias along the chosen subsequence.

## Originality

**FAIL** — Lee-Schnelli's deformed-Wigner theorem is explicitly centered at an N-dependent edge Ehat_+(N) determined by the empirical deformation. Remark 2.9 states that Ehat_+(N) may be replaced by the limiting E_+ only when the convergence is sufficiently fast, with the required speed depending on the empirical-measure convergence exponent. Under a target assuming only weak convergence, choosing a deliberately slow N^(-1/4) proportion drift is therefore the routine obstruction already signposted by the prior theorem.

## Scientific value

**FAIL** — The exact derivative and rational enclosure make the example reproducible, but they do not create a new random-matrix phenomenon. The failure follows from the already documented need for finite-N centering or sufficiently fast convergence to the limiting edge; the record chiefly exposes a missing hypothesis in the target formulation.

## Sources

- Edge Universality for Deformed Wigner Matrices (Ji Oon Lee; Kevin Schnelli): https://arxiv.org/abs/1407.8015 — Theorem 2.8 centers at an N-dependent edge; Remark 2.9 says limiting-edge substitution requires sufficiently fast convergence.

## Limitations

- The audit independently checked the edge-drift scaling and treats the finite-N edge theorem as prior input.
- The rejection is about novelty/value, not the mathematical validity of the displayed slow-convergence counterexample.

GitHub was read only as evidence; no repository mutation was performed in this audit chat.
