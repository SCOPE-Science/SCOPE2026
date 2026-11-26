---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For odd q, trace-zero Cayley–Hamilton and the anticommutator identity give E(X,Y)=4Q(X)Y−2tr(XY)X. Thus X=0 contributes only to zero; nonzero isotropic X has image its line and fiber q²; anisotropic X has image X-perp and fiber q. For a fixed nonzero isotropic target, its perpendicular plane has q(q−1) anisotropic vectors (nilpotent normal form gives c=0), in addition to the q−1 possible isotropic X in the target line. The split and nonsplit anisotropic normal forms give respectively bc and a²−tb² on the perpendicular plane, hence (q−1)² and q²−1 anisotropic X. The scalar equation a²+bc=t has q² solutions for t=0 and q(q+χ(t)) for t≠0, giving the claimed strata, zero fiber, and equal mass. These conjugacies are under GL₂, so no rational SL₂ conjugacy restriction is needed. In characteristic two the first bracket is scalar, so the second vanishes. The proof covers extensions and small fields; verify_engel.py is direct finite corroboration only, read but not rerun.

## originality

FAIL

A distinct indexed joint-output result gives the exact same odd-characteristic counts as explicit marginals for the same ordered input pairs and target invariant. This establishes coverage of the substantive new claim, not publication order. The elementary characteristic-two observation is outside that result but does not recover a distinct substantive fiber classification.

## value

FAIL

Prescribed-target counts and the odd-field mass comparison are natural invariants in their own right, but here they can be read off from a joint table explicitly supplying the same marginal, with no distinct invariant established. The only uncovered case is the immediate central-commutator collapse in characteristic two; it does not by itself warrant a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
