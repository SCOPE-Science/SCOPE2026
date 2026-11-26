---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The Finding is correct, but RESULT.md line 33 incorrectly asserts irreducibility: the count state (a,0), where all flexible voters match their own part's zealot, has no incoming transition and has positive exits. For K_{2,2}, its stationary probability is zero and each other state has probability 1/3. Uniqueness on the labeled chain nonetheless follows: from every configuration first turn all flexible second-part vertices red using the fixed red neighbor, then turn all first-part voters red using a red flexible second-part neighbor. Thus every closed class must contain the all-red flexible state. Within-part symmetry now follows from uniqueness. The one-site drift equations give mu=b/(a+b+1), nu=(b+1)/(a+b+1). Centering the products gives C_A=b C_AB/(b+1), C_B=a C_AB/(a+1), with unavailable pairs omitted. The cross equation after substitution has coefficient (3(a+b)+2)/((a+1)(b+1)) on C_AB and right side (a+b)/(a+b+1)^2, yielding all displayed covariances. The stationary drift of D=X-Y has linear term -2D, a uniform O(1/a+1/b) forcing, and jump-square rate at most 1/a+1/b, so E[D^2] vanishes. The mean coordinate z=(X+Y)/2 has scaled drift (theta-z)/(2 theta(1-theta)) and scaled half jump variance z(1-z)/(4 theta(1-theta)) in stationary L^1; the scaled Taylor remainder is O(1/(a+b)). This gives the recursion (k+1)M_k=(2 theta+k-1)M_{k-1}; compact moment determinacy yields the joint beta limit. The pair disagreement limit follows from the one-site means and covariances. This passes the Finding, not the erroneous irreducibility sentence.

## originality

FAIL

The claimed formulas and limit are already covered by a distinct indexed record and by an equivalent same-date frozen finding plus its proof. This is a coverage judgment, not a priority judgment. No distinct surviving part of the Finding is identified.

## value

FAIL

Synchronization with a nondegenerate beta limit and size-dependent correlations are meaningful facts about this natural model. As a distinct contribution here they add no new regime, structural result or separately useful unknown statistic to the exact overlapping coverage; the extra disagreement statement is a routine moment conversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
