---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For each length-three quaternary word abc, the 16-bit shadow mask records ab,ac,bc with duplicates merged. Five words can cover at most 15 of 16 ordered pairs; six are feasible. The proof enumerates six distinct words from 64 using safe remaining-capacity pruning, then classifies the resulting 644 covers by the 48-element group S4 times global reversal. An independent pair-cover search returned exactly 644 covers with excess 0:120,1:336,2:188. The assigned two-enumerator proof and 21-orbit computation are coherent.

## originality

FAIL

FAIL decisively: the October 26, 2026 complete earlier published Resultary theorem has the IDENTICAL source length, alphabet, deletion model, full 644 labeled covers, 21 relabeling/reversal orbits, 120 perfect and 524 nonperfect, and exactly the same excess distribution. Its additional shadow-size profile refines the submitted theorem. The submitted six-word minimum was also known in 2010.

## value

FAIL

FAIL as a separately claimed finding: exact extremizer census would be valuable if unknown, but here all its mathematical distinctions and even a stronger profile are already given by the earlier complete published record. Equivalent enumeration code or notation supplies reproducibility, not a new scientific invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
