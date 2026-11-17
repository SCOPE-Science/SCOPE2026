---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Pinned RESULT.md proves all width-two syndromes equal zero, any single column, or a neighboring XOR. Noncyclic telescoping and cyclic repeat-parity force at least one missing nonzero even syndrome in every ordering. Primitive field-power order 0,1,alpha,...,alpha^(Q-2) realizes exactly Q-2 adjacent differences and omits u=1+alpha^(-1), which a nonadjacent two-apart pair realizes inside width-three, for every degree m>=2. Independent GF(4) computation found seven width-two syndromes and all eight width-three syndromes, cyclic and noncyclic. Finite check does not prove all degrees.

## originality

FAIL

FAIL: October 12 2026 published Optimal two-window coverage and three-window burst covering for binary extended Hamming codes proves precisely the SAME all-m, linear and cyclic, max |S2|=2Q-1, min burst radius=3, identical primitive element column ordering and identical sole missing syndrome. Its complete three-section proof matches the telescoping obstruction and two-apart repair. No surviving distinct claim, notwithstanding a 2026 preprint that covers only one small instance.

## value

PASS

Sharp coordinate-order burst covering and the exact one-syndrome width-two deficiency are well-motivated coding invariants; they are valuable mathematical facts even though their earlier complete publication defeats this submission’s originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
