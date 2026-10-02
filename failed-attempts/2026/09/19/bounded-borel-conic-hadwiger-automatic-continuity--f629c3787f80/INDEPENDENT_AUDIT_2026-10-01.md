# Independent scientific audit — SCOPE-20260919-f629c3787f80

Audited at: 2026-10-01T12:12:53.903497Z

Disposition: **failed**

## Correctness — PASS

The induction is valid. After subtracting the intrinsic-volume combination determined by subspace values, restrictions to proper subspaces vanish by induction. Stabilization by a fixed line is again a bounded Borel invariant valuation in one lower dimension, so the residual vanishes on every cone containing a line. The orthoscheme pullback is Borel and bounded on the finite-measure positive spherical chamber, hence integrable; Lotz's general residual-vanishing theorem then applies. The exact norm follows because conic intrinsic volumes are nonnegative, sum to one, and subspaces realize the coefficient coordinates.

## Originality — FAIL

Lotz's primary paper already isolates the substantive vanishing theorem in the stronger regularity form actually needed: any invariant residual valuation satisfying the algebraic vanishing condition and having an integrable orthoscheme restriction vanishes. The same paper then proves spherical Hadwiger by the identical dimension induction. Replacing continuity by bounded Borel measurability merely observes that bounded Borel pullbacks are integrable and reruns the published induction; the final classification is therefore mechanically implied by the published theorem and proof.

### Equivalent formulations

The audited bounded-Borel theorem is exactly the published residual theorem plus the published dimension-induction template with bounded+Borel used as a sufficient condition for L1.

### Broader coverage

The stronger published residual theorem, together with its adjacent induction proof, covers the final implication.

### Exact database or table

Exact wording is immaterial because broader published hypotheses imply the theorem.

### Claim versus prior implication

The final theorem is a direct corollary-level adaptation of the published proof, so originality fails under the implication standard.

## Value — FAIL

Automatic continuity under bounded Borel regularity is a natural statement, but here its proof is essentially the published induction with the explicit published L1 hypothesis and the immediate bounded-Borel-implies-L1 observation. Under the requested bar, this is an expository corollary rather than a distinct worthwhile new finding.

## Sources inspected

- Hadwiger's classification theorem on the sphere via signed orthoscheme decompositions — https://arxiv.org/abs/2609.17437. COVERING: The paper explicitly proves residual vanishing under the L1 orthoscheme hypothesis and already gives the identical induction that reduces Hadwiger classification to that residual theorem.

## Checked sources

- https://arxiv.org/abs/2609.17437
- https://arxiv.org/abs/2608.19110
- https://arxiv.org/abs/2608.26015
- https://arxiv.org/abs/2609.09335
- semantic research-index search

## Residual risks

- No correctness risk was found; the decisive issue is prior implication rather than access.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The bounded-Borel classification remains a correct consequence of Lotz's result.
- The original package should be preserved intact in the designated failed-attempt archive.
