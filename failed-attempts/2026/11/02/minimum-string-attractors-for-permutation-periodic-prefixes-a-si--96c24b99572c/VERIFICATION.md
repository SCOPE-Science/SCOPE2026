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

Singleton factors force q markers and the first full period is an attractor. When m=1, a factor either meets a letter occurring once or is contained in both copies of the short prefix. For m≥2, an unwrapped short factor contains a symbol all of whose copies lie in its occurrence union. A wrapped short factor whose wrapped tail fits the appended prefix hits every q−1; otherwise its occurrence union excludes q−1 only in the last full period, r only in the initial period, and j<r only in the two boundary copies. For length at least q, successive occurrences touch or overlap; the missed markers must lie in two end segments of length <q. The right segment must contain the last q−1, which forces it not to contain r; the same restrictions follow. They are inconsistent when r=q−1 and m≥2. For r≤q−2 the literal factor (q−1)0…r has starts q,2q,…,(m−1)q and misses exactly the stated pattern. Independent literal occurrence-union enumeration (python3 /workspace/branches/reproduce.py 4) reproduced 88 cases, 52,430 candidates and 835 failures; the proof, not the census, handles the unbounded parameters. The common witness need not be the only factor a choice misses.

## originality

FAIL

A distinct earlier-dated Resultary record explicitly gives the same full classification, shared obstruction, and three-case count over the same domain. The disagreement with the frozen originality assessment is not limited to the acknowledged alternating-binary case. The claim is covered; this does not establish authorship, dependence, or historical priority beyond the evidence.

## value

FAIL

A single boundary factor deciding all optimal placements is structurally informative in its original context. The frozen record adds no boundary regime, placement information, or stronger invariant to the already available classification; its bounded computation is corroboration of that known result, not a distinct mathematical contribution. No surviving remainder warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
