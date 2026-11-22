---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Using D=a|w|_0/b-|w|_1, a 1-run with starting discrepancy d>=0 has length floor(d)+1 and final discrepancy in [-1,0). After a completed earlier run, a subsequent zero-run of length ell gives d=delta+(a/b)ell. For ell<=b-1 the next 1-run is shorter than a+1; ell=b gives length exactly a; ell>=b+1 gives at least a+2. A first run has length a+1 only after exactly b initial zeros. Hence the marker exists at the beginning but never later; open-cylinder factor language and nonrecurrence prove nontransitivity. Direct independent finite prefix enumeration at several coprime pairs corroborates, but does not prove, the all-rational claim.

## originality

FAIL

The entire stated conclusion is logically covered by the full published same-day theorem for every rational c in (1/2,1). Its explicit two-run witness is different, but the main claim that all rational c>=2/3 are nontransitive is a strict parameter restriction, not an independent originality result. The submitted one-run proof remains a valid alternate derivation; neither that variation nor the subset permits PASS for the unchanged finding.

## value

FAIL

The exact nontransitivity phenomenon and parameter interval are already established by a stronger same-system theorem. The alternate shorter marker is mathematically correct but, as packaged, no independently motivated new invariant/classification/counterexample survives the logical implication. Reject value of the unchanged final finding rather than conflating proof elegance with a new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
