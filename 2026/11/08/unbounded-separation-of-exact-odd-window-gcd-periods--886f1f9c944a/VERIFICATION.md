---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Cassini gives primitive seeds and norm µ=b²-ab-a²=L_h, and the recurrence companion matrix sends the state to its negative mod L_h after h steps. For odd k the reversible linear and square recurrences, telescoping identities and alternating norm force both window gcds to divide 2L_h. At every odd prime power of L_h, the original state has exact period 2h while its square sequence has exact period h: h primality, invertibility T²-I and q!=3 exclude smaller periods. Mod 2 gives period 3, with one allowed factor 2. Assembly yields the exact formulas, and maximum B=2L_h occurs in a unique residue mod 3h on odd lengths, proving leastness. Checked h=5,7,11,13,17,19 and odd k<=6h by independent integer recurrence.

## originality

PASS

Best-of-knowledge PASS restricted to infinite prime-indexed unbounded least-period ratio; prior h=5 example, universal odd-window periodicity and general formulae are expressly excluded.

## value

PASS

This converts a published isolated unequal-minimal-period case into a complete infinite structural family with unbounded ratio, resolving a natural severity question about divergence of first- and second-power window gcd periodicities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
