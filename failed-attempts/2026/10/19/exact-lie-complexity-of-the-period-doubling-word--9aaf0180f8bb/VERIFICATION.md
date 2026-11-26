---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two fixed-point identities put every 1 on an odd absolute index, forbid 11 and force any four consecutive zeros to come from consecutive parent 1s, likewise impossible. At odd length, two ones have an even separation in one representative and an odd separation after rotating across one of the two, so full orbit containment is impossible; at length at least five, zero or one 1 instead forces a rotation containing 0000. At length 2m≥4 every fully contained orbit has a 1. Rotate to put its ones in odd relative positions, then all even rotations occur only at aligned starts and desubstitute. Conversely even rotations of δ(u) occur by substitution and odd rotations by shifting one place and appending the next aligned zero. Starting parity also makes the map injective. The prefix 01000101 exhibits all candidates at lengths 1–3, and 11 rules out the rest; the resulting counts are 2,2,2. This gives the two support families by halving and the support count by counting powers separately. Independently generated δ^7(0100) covers the complete language up to length 128, since windows of length at most 128 meet at most two aligned blocks and 0100 contains each allowed adjacent pair (00,01,10). Direct orbit enumeration in that finite language verified the counts and 63 image-set equalities. The parity argument, not enumeration, establishes the arbitrary lengths.

## originality

FAIL

A distinct Resultary theorem explicitly covers the same fixed point, exact all-positive-length census, odd-length exclusion, and the same class-level substitution bijection for m≥2. It gives explicit representatives for both infinite families as well. This is an exact mathematical overlap in an earlier-dated catalogue path; it is not a certification of publication priority.

## value

PASS

As a mathematical result, the substitution bijection for complete orbits and the all-length sparse support classification are meaningful in a canonical non-Sturmian automatic word. The contribution as submitted is nevertheless not distinct from the matched classification; this utility is not a reason to accept a duplicate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
