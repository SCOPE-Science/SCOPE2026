---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Huang proves that the singular seminorm Phi is bounded by the Marcinkiewicz norm, vanishes on bounded finite-support functions, and that X=ker Phi is a closed ideal containing all such truncations. For the renorming N_lambda, truncating any test function leaves the singular term zero while monotonically recovering the pairing, so the Köthe associate is exactly the standard associate with equal norm. The same truncation argument applies to X. The standard Fatou/Lorentz-Luxemburg bidual theorem then recovers the ambient Marcinkiewicz space. Huang's explicit alpha=1/2 witness has Phi(f)=0, Phi(g)=1 and base norm one; the seminorm inequality gives distance at least one from g to X and x=0 gives equality. Hahn-Banach supplies a separator, and it cannot be a Köthe integral because X contains every bounded finite-support test.

## originality

FAIL

Every nontrivial input is already in Huang's paper: the ambient fully symmetric Fatou Marcinkiewicz space, the singular seminorm's vanishing on bounded finite-support functions, the equivalent renorming, the kernel ideal, and the explicit norm-one witness. Equality of Köthe associates under such truncations and recovery of a Fatou Banach function space from its Köthe bidual are standard textbook consequences. Thus the audited statements are direct corollaries of published hypotheses plus classical Köthe-duality theory, even if Huang does not spell them out.

## value

FAIL

The observation that a singular seminorm invisible on finite-support truncations disappears under Köthe association is an elementary textbook deduction from the published construction. The distance-one and Hahn-Banach statements are likewise immediate. This is not a new structural boundary or independently motivated invariant under the stated value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
