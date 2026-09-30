# Independent Audit — 2026/09/11/027

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `2a0e896e07db0f37d54abe1debba098ad464e2c9`
- Disposition: **FAILED**

## Correctness

**PASS** — The lower bound is correct. A maximal delta-separated set of directions has cardinality comparable to delta^-2; taking all corresponding unit delta-tubes through one point makes the multiplicity comparable to delta^-2 on a ball of radius comparable to delta. Hence the L^2 norm of the tube sum is bounded below by a constant times delta^-1/2 while the square root of the total tube volume stays bounded. Wang–Zahl's sticky definition is compatible with this bush: the axes form a two-dimensional family of lines, the minimal packing dimension required in R^3. Therefore an exponent 0.49 (with sufficiently small epsilon, e.g. 0.005) cannot hold uniformly for that sticky class.

## Originality

**FAIL** — The argument is the classical bush/scaling obstruction for the Kakeya maximal function, applied to a sticky class that already contains the all-directions-through-one-point bush. Once the Wang–Zahl definition is written down, verifying that this bush is sticky and repeating the standard multiplicity calculation is immediate. No new extremizer, multiscale estimate, sticky-structure theorem, or Kakeya exponent is established.

## Scientific value

**FAIL** — The record correctly diagnoses an over-strong target, but the diagnosis is a baseline scaling check that should precede a research attempt rather than constitute an independent research finding. It does not sharpen the known Kakeya maximal bounds or add a new sticky phenomenon. Its value is primarily as a sanity check on formulation.

## Limitations

- The L^2 counterexample does not by itself address every differently normalized union-volume statement; the record correctly notes that distinction.
- The rejection is for lack of research-level originality/value, not a defect in the bush computation.

## Sources

- Sticky Kakeya sets and the sticky Kakeya conjecture — H. Wang; J. Zahl: https://arxiv.org/abs/2210.09581 — Defines the sticky line-family condition used to verify that the origin bush lies in the class.
- Improved bounds for the Kakeya maximal conjecture in higher dimensions — J. Hickman; K. M. Rogers; R. Zhang: https://arxiv.org/abs/1908.05589 — Background for the cited Kakeya maximal exponents; it does not turn the standard bush obstruction into a new result.

GitHub was read only as evidence. The pre-existing AUDIT.json was treated as evidence rather than authority; this disposition reflects an independent three-axis assessment.
