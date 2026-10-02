---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For the positive-parameter Moore--Spiegel oscillator, every nontrivial compact invariant state crosses \(|x|=1\), the exact square-defect identity \(R\langle(x^2-1)y^2\rangle=\langle(z+Tx)^2\rangle\) holds with equality only at the origin, and every nonconstant periodic orbit has \(P>2\pi/\sqrt T\).

## Correctness — PASS

The generator calculations reproduce the stated stationary balances, and direct differentiation of the displayed polynomial \(W\) gives the defect integrand. Equality of the square defect forces \(z+Tx=0\); invariance then forces \((1-x^2)y=0\), hence only the origin. The compact-slab obstruction follows by the same invariant-set argument, and Wirtinger applied to the exact derivative-energy balance gives \(P\ge2\pi/\sqrt T\); equality would be a single harmonic mode and substitution excludes it for \(R>0\). The inspected symbolic artifact verifies all derivative identities but is not the analytic proof.

**Checked sources.** assigned RESULT.md and artifacts/verify_identities.py at tree ac2b2f341ae543eb901226b74d5a82a9ad644d7a; published 2026-09-20 SCOPE Moore--Spiegel balance theorem; Balmforth--Craster 1997 full primary PDF

**Residual risks.** No correctness defect was found.

## Originality — FAIL

The strict period floor is already printed in the 2026-09-20 SCOPE result, and the stronger-looking amplitude defect is a direct elementary consequence of that record's two exact balances plus the standard invariant identity \(\langle xz\rangle=-\langle y^2\rangle\) obtained from \(L(xy)=y^2+xz\). The compact-slab statement then follows because every nonempty compact invariant set supports an invariant probability measure. Thus the final claim is implication-covered by the immediately preceding published theorem plus routine generator algebra.

### Equivalent formulations

The current square-defect identity is an equivalent recombination of the prior balances after averaging \(L(xy)\).

### Broader coverage

No broader historical theorem is needed for the rejection because the prior published result already implies the claimed follow-up.

### Exact database or table

The one-day ordering resolves priority for the implication-covered statements.

### Claim versus prior implication

Positivity gives the \(|x|>1\) excursion except at the equilibrium; compact invariant sets support invariant measures. Hence the substantive new-looking barrier is mechanically implied.

**Checked sources.** published SCOPE 2026-09-20 record 8ed8e017fb90; https://doi.org/10.1063/1.166271; Resultary semantic search

**Residual risks.** No residual historical-search risk can undo the direct prior-SCOPE implication.

## Value — FAIL

A parameter-independent recurrence barrier is mathematically attractive, but here it follows by one standard averaged derivative identity from balances published the previous day; the period theorem is literally repeated. This is a routine follow-up corollary rather than a separate motivated gap.

**Checked sources.** published SCOPE 2026-09-20 balance theorem; current algebraic derivation

**Residual risks.** The explicit polynomial \(W\) is a convenient certificate but does not rescue separate scientific value.

## Limitations

- Invariant-measure statements require compact support.
- The slab statement concerns compact invariant sets, not arbitrary one-sided bounded trajectories.
- The rejection is prior-implication/value failure, not a correctness defect.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
