---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The frozen census is mathematically sound, but its r=1 branch has exact same-day coverage. The repaired RESULT limits the theorem to r≥2 and cites the r=1 counts as background. In the repair, the forward-gap composition with a marked occupied site proves the indexed count, including the singleton and empty cases. The equality of readouts is equivalent to a two-periodic XOR difference. A whole-site complement collision forces sitewise alternation, ruled out on odd rings and at separation r≥2. A parity complement forces the other parity to be zero, then excludes both 00 and 11 on the flipped parity sublattice. That gives exactly the complementary residue classes of spacing four when 4 divides n, and requires r=2 or 3. The even and odd pairs yield different alternating outputs because exactly one neighbor is occupied at each opposite-parity site. These exhaust all masks, so no fiber can exceed two in the repaired scope and the exact indexed image and singleton counts follow. The finite checker was inspected, not executed; the exact proof is the replay path, and the claimed finite-run evidence is corroborative only.

## originality

PASS

The repaired claim excludes the demonstrably covered r=1 indexed census, without inferring priority from the shared date. Its distinct content is the separation-dependent r≥2 classification, two exceptional outputs, and sharp uniform threshold.

## value

PASS

The repaired range contains the sharp phenomenon: minimum spacing five is enough at every permitted length, whereas spacings three and four leave exactly two ambiguities at each permitted multiple of four. This gives both a precise design threshold and a complete identification of exceptional observations, more useful than the free-space kernel alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
